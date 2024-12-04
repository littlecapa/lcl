def append_to_file(file_path, content):
    """
    Appends content to a file. If the file does not exist, it will be created.
    
    :param file_path: Path to the file
    :param content: Content to append (string)
    """
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(content + "\n")  # Add a newline after the content
    except Exception as e:
        print(f"An error occurred while appending to {file_path}: {e}")
        raise