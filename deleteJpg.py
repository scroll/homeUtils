import os
import optparse

RAW_NAMES = ['.crw', '.cr2', '.arw']

RAW = {'hasselblad':['.3fr'],
       'arriflex'  :['.ari'],
       'sony'      :['.arw', '.srf', '.sr2'],
       'canon'     :['.crw', '.cr2'],
       'kodak'     :['.k25', '.kdc'],
       'minolta'   :['.mrw'],
       'nikon'     :['.nef', '.nrw'],
       'olympus'   :['.orf'],
       'pentax'    :['.pef', '.ptx'],
       'red'       :['.R3D'],
       'fuji'      :['.raf'],
       'panasonic' :['.raw', '.rw2'],
       'leica'     :['.raw', '.rwl', '.dng'],
       'samsung'   :['.srw']}

def delete_duplicate_jpg(directory, file_types, verbose):
    '''
    Traverses the directory structure from the given root directory
    and deletes a jpg file if it is a duplicate of raw file format.
    '''

    if not file_types:
        file_types = RAW_NAMES

    # traverse all filenames within the root dir
    for dir, dirs, filenames in os.walk(directory):
        for filename in filenames:
            # check if it is jpg
            if filename.endswith('.jpg') or filename.endswith('.JPG'):
                # for every possible raw format
                for ext in file_types:
                    raw_name = os.path.join(dir,filename.split('.')[0] + ext)
                    raw_upper = os.path.join(dir,filename.split('.')[0] + ext.upper())
                    # check if it exists and remove the jpg if it does
                    if os.path.exists(raw_name) or os.path.exists(raw_upper):
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
    p.add_option('-v', '--verbose', action='store_true', dest='verbose', default=False, help='verbose mode')
    opt, args = p.parse_args()
    print len(args)
    if not opt.directory:
        p.error('Directory not specified. Use the -d flag to choose a root directory.')

    if opt.verbose:
        print 'Walking: %s'%opt.directory

    delete_duplicate_jpg(opt.directory, opt.file_types, opt.verbose)

    if opt.verbose:
        print 'Done!'



if __name__ == '__main__':
    main()



