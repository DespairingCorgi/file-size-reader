import os


def convert_readable(bytes, decimal=2):
    tmp = bytes
    for i,b in enumerate(['TB', 'GB', 'MB', 'KB', 'B']):
        if tmp//(1024**(4-i)):
            storage = float(bytes)/float(1024**i)
            storage = round(storage, decimal)
            return f"{storage}{b}"
    return "0B"

def get_byte_size(path):
    """
    Returns the real size of the file on disk in Windows
    """
    if not os.path.isfile(path):
        print(f"The path {path} is not a file.")
        return None

    allocation_size = os.stat(path).st_size  # Get the allocation size
    actual_size = os.path.getsize(path)  # Get the actual size of the file
    real_size = ((actual_size + allocation_size - 1) // allocation_size) * allocation_size
    return real_size

def get_file_size(path, decimal=2):
    size = get_byte_size(path)
    readable_size = convert_readable(size, decimal)
    return readable_size

###########example###############
import glob
jss = glob.glob("*.json")

for js in jss:
    redable_byte = get_file_size(js)
    print(js, redable_byte)
    
