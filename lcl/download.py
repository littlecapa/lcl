import requests, time, os
from urllib.error import HTTPError

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7)'

def downloadZip(url, file_name_zip, attempts=1):

    # User Agent is required by TWIC / see https://deviceatlas.com/blog/list-of-user-agent-strings
    
    for attempt in range(1, attempts+1):
        try:
            print("Try ", url)
            if attempt > 1:
                time.sleep(10)  # 10 seconds wait time between downloads
            with requests.get(url, headers={"User-Agent": USER_AGENT}, stream=True) as response:
                print ("Status: ", response.status_code)
                if response.status_code == HTTPError:
                    print ("Ende")
                    return True
                response.raise_for_status()
                with open(file_name_zip, 'wb') as out_file:
                    print("File open")
                    for chunk in response.iter_content(chunk_size=1024*1024):  # 1MB chunks
                        out_file.write(chunk)
                print("Success")

        except Exception as ex:
            print("Error: ", str(ex))
            raise ex
        
def existFile(url):
    try:
        response = requests.head(url, headers={"User-Agent": USER_AGENT}, allow_redirects=True)
        # Check if the response status code indicates success (200 OK)
        print(response.status_code)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking file at {url}: {e}")
        return False
    
def delete_all_files_in_directory(directory):
    """
    Deletes all files in the specified directory.
    """
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    if not os.path.isdir(directory):
        print(f"'{directory}' is not a valid directory.")
        return

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
