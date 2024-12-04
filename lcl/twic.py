import os, zipfile, requests
from .download import downloadZip, existFile
from urllib.parse import urljoin
from urllib.error import HTTPError


def unzip_twic_file(filename_zipped, unzip_folder):
    with zipfile.ZipFile(filename_zipped, 'r') as zip_file:
        zip_file.extractall(unzip_folder)
        os.remove(filename_zipped)

def get_file_info(issue_number, base_url, twic_pattern):
    filename_zip = twic_pattern.replace("<<number>>", str(issue_number))
    return filename_zip, urljoin(base_url,filename_zip)

def download_twic_file(base_url, issue_number, download_dir, unzip_dir, twic_pattern):
    filename_zip, url = get_file_info(issue_number, base_url, twic_pattern)
    filename = os.path.join(download_dir, filename_zip)
    try:
        filename_zipped=os.path.join(download_dir, filename)
        downloadZip(url=url, file_name_zip=filename_zipped)
        unzip_twic_file(filename_zipped, unzip_dir)
    except Exception as ex:
        print ("Download TWIC Error: ", str(ex.code))
        raise ex
    
def exist_twic_file(issue_number, base_url, twic_pattern):
    _, url = get_file_info(issue_number, base_url, twic_pattern)
    return existFile(url)
    
def get_highest_twic_issue(highest, base_url, twic_pattern):
    while exist_twic_file(highest+1, base_url, twic_pattern):
        highest += 1
    return highest