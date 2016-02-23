import os

def get_dirlist(path):
    """
    Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path"""
    if prefix == "": # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = " | "

    dirlist = get.dirlist(path)
    for f in dirlist:
        print(prefix+f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_files(fullname, prefix + " | ")
