#!/usr/bin/python
# -*- coding: iso-8859-5 -*-

from __future__ import with_statement
import os
import codecs
import optparse
from string import maketrans

def lat2cyr(inputText, output):
    i = 'abcdefghijklmnopqrstuvwxyz`[]\\ABCDEFGHIJKLMNOPQRSTUVWXYZ~{}|'
    o = 'абцдефгхийклмнопярстужвьъзчшщюАБЦДЕФГХИЙКЛМНОПЯРСТУЖВЪЪЗЧШЩЮ'
    table = maketrans(i,o)
    
    result = ''
    if os.path.exists(inputText):
        with open(inputText) as f:
            inputText = f.read()

    for char in inputText:
        if char in i:
            result = result + char.translate(table)

        else :
            result = result + char

    if output:
        with codecs.open(output, 'w', 'utf-8') as f:
            f.write(result.decode('iso-8859-5'))
    else:
        print result.decode('iso-8859-5')
                

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



