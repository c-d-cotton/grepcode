#!/usr/bin/env python3

import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

# argparse fileinputs
sys.path.append(str(__projectdir__ / Path('submodules/argparse-fileinputs/')))
from argparse_fileinputs import add_fileinputs
from argparse_fileinputs import process_fileinputs

def greplist(filelist, searchterm):
    for filename in filelist:
        try:
            with open(filename) as f:
                text = f.read()
        except:
            continue
        if text.replace(searchterm, '', 1)==text:
            continue
        print('FILENAME: ' + filename)
        textarray = text.splitlines()
        num = sum([t.replace(searchterm,'') != t for t in textarray])
        if num > 10:
            print(str(num) + ' occurrences')
        else:
            for linenum in range(0, len(textarray)):
                t = textarray[linenum]
                if t.replace(searchterm,'') != t:
                    tsplit = t.split(searchterm)
                    lineprint = tsplit[0][-50:] + searchterm + searchterm.join(tsplit[1:])[:50]
                    print('LINENUM: ' + str(linenum + 1) + '. TEXT: ' + lineprint)
        print('')


def greplist_ap():
    import argparse

    #Argparse:{{{
    parser=argparse.ArgumentParser()
    parser.add_argument("searchterm",type=str,help="default: ")

    parser = add_fileinputs(parser)

    args=parser.parse_args()
    # End argparse:}}}


    filelist = process_fileinputs(args)

    greplist(filelist, args.searchterm)


# Run:{{{1
if __name__ == "__main__":
    greplist_ap()
