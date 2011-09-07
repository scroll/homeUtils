import os
import optparse

RAW_NAMES = ['.crw', '.cr2', '.arw']

RAW = {'hasselblad':['.3fr']
       'arriflex'  :['.ari']
       'sony'      :['.arw', '.srf', '.sr2'],
       'canon'     :['.crw', '.cr2'],
       'kodak'     :['.k25', '.kdc'],
       'minolta'   :['.mrw'],
       'nikon'     :['.nef', '.nrw']
       'olympus'   :['.orf'],
       'pentax'    :['.pef', '.ptx'],
       'red'       :['.R3D'],
       'fuji'      :['.raf'],
       'panasonic' :['.raw', '.rw2'],
       'leica'     :['.raw', '.rwl', '.dng'],
       'samsung'   :['.srw']}

def delete_duplicate_jpg(directory, file_types, verbose=True):
    '''
    Traverses the directory structure from the given root directory
    and deletes a jpg file if it is a duplicate of raw file format.
    '''
    if not directory:
        raise SystemError, 'No directory supplied as argument.'

    if not file_types:
        file_types = RAW_NAMES

    print type(file_types)
    print 'Checking for following formats: %r'%(file_types,)

    # traverse all filenames within the root dir
    for dir, dirs, filenames in os.walk(directory):
        for filename in filenames:
            # check if it is jpg
            if filename.endswith('.jpg') or filename.endswith('.JPG'):
                # for every possible raw format
                for ext in file_types:
                    raw_name = filename.split('.')[0] + ext
                    # check if it exists and remove the jpg if it does
                    if os.path.exists(os.path.join(dir,raw_name)):
                        if verbose: print 'Deleting: %s'%os.path.join(dir,filename)
                        os.remove(os.path.join(dir,filename))


def main():
    '''
    Handles command line options
    '''
    p = optparse.OptionParser(description='''Traverses the directory structure from the given root
                                             directory and deletes a jpg file if it is a duplicate
                                             of raw file format.''')
    p.add_option('-d', '--directory', help='the root directory you want to traverse')
    p.add_option('-f', '--file_types', help='list of file types you want to track i.e. [".cr2",".arw"]')
    p.add_option('-v', '--verbose', help='verbose mode')
    opt, args = p.parse_args()
    if opt.verbose:
        print 'Traversing %s '%opt.directory
    print opt.file_types
    delete_duplicate_jpg(opt.directory, opt.file_types, opt.verbose)



if __name__ == '__main__':
    main()



