import os

RAW_NAMES = ['.crw', '.cr2', '.arw']

def delete_duplicate_jpg(directory, verbose=True):
    '''
    Traverses the directory structure from the given root directory
    and deletes a jpg file if it is a duplicate of raw file format.
    '''
    for dir, dirs, filenames in os.walk(directory):
        # traverse all filenames within the root dir
        for filename in filenames:
            # check if it is jpg
            if filename.endswith('.jpg') or filename.endswith('.JPG'):
                # for every possible raw format
                for ext in RAW_NAMES:
                    raw_name = filename.split('.')[0] + ext
                    # check if it exists and remove the jpg if it does
                    if os.path.exists(os.path.join(dir,raw_name)):
                        if verbose: print 'Deleting: %s'%os.path.join(dir,filename)
                        os.remove(os.path.join(dir,filename))


