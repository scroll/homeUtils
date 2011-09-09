import os
import optparse

HELP ='''
         Traverses the directory structure from the given root directory
         and deletes a jpg file if it is a duplicate of raw file format.
      '''

RAW = {'hasselblad':['.3fr'],
       'arriflex'  :['.ari'],
       'sony'      :['.arw', '.srf', '.sr2'],
       'canon'     :['.crw', '.cr2'],
       'kodak'     :['.k25', '.kdc'],
       'minolta'   :['.mrw'],
       'nikon'     :['.nef', '.nrw'],
       'olympus'   :['.orf'],
       'pentax'    :['.pef', '.ptx'],
       'red'       :['.r3d'],
       'fuji'      :['.raf'],
       'panasonic' :['.raw', '.rw2'],
       'leica'     :['.raw', '.rwl', '.dng'],
       'samsung'   :['.srw']}

def delete_duplicate_jpg(directory, camera, verbose):
    c = 0
    # traverse all filenames within the root dir
    for dir, dirs, filenames in os.walk(directory):
        for filename in filenames:
            # check if it is jpg
            if filename.endswith('.jpg') or filename.endswith('.JPG'):
                # for every possible raw format
                for ext in RAW[camera]:
                    raw_name = os.path.join(dir,filename.split('.')[0] + ext)
                    raw_upper = os.path.join(dir,filename.split('.')[0] + ext.upper())
                    # check if it exists and remove the jpg if it does
                    if os.path.exists(raw_name) or os.path.exists(raw_upper):
                        if verbose: print 'Deleting: %s'%os.path.join(dir,filename)
                        os.remove(os.path.join(dir,filename))
                        c += 1
    return c


def main():
    '''
    Handles command line options
    '''
    p = optparse.OptionParser(description=HELP)
    p.add_option('-d', '--directory', help='the root directory you want to traverse')
    p.add_option('-v', '--verbose', action='store_true', dest='verbose', default=False, help='verbose mode')
    p.add_option('-c', '--camera', choices=RAW.keys(), help='%r'%RAW.keys())
    opt = p.parse_args()[0]
    if not opt.directory:
        p.error('Directory not specified. Use the -d flag to choose a root directory.')
    if not opt.camera:
        p.error('Camera type not specified. Use the -c flag to choose a camera formats.')

    if opt.verbose:
        print 'Walking: %s'%opt.directory
        print 'Checking for %s types: %r' %(opt.camera.capitalize(), RAW[opt.camera])

    c = delete_duplicate_jpg(opt.directory, opt.camera, opt.verbose)

    if opt.verbose:
        print 'Done!'
        if c == 0: c = 'No'
        print '%r duplicate .jpg files deleted'%c



if __name__ == '__main__':
    main()



