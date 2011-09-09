import os
import string
from __future__ import with_statement

def lat2cyr(input, output):
    in = ''
    if os.path.exists(input):
        with file.open(input)
        
    
    


def main():
    '''
    Handles command line options
    '''
    p = optparse.OptionParser(description='Translates latin characters to the corresponding bulgarian-phonetic.')
    p.add_option('-i', '--input', help='The string input you want to translate. You can also point to a file.')
    p.add_option('-o', '--output', help='File to be used as output.')
    opt = p.parse_args()[0]
    if not opt.input:
        p.error('Neither input string or file given. Use -i flag.')

    lat2cyr(opt.input, opt.output)





if __name__ == '__main__':
    main()



