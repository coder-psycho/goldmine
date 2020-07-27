#!/usr/bin/python

import re 
import sys
import os 
import collections, pprint

def main(infilename, outfilename):
    """To analyse the session list output from a firewall
     for example: 'diag sys session list' and interpret the value

    Args:
            infilename (str) : path of the sessionlist file
            outfilename (str) : path of the output file
    """
    
    #Check whether input file exists
    if not os.path.exists(infilename):
        print("Error: The input file does not exist")
        sys.exit()
    
    #Get text from input file
    outfile = open(outfilename, 'w') 
    infile = open(infilename, 'r')
    # lines = infile.readlines()
    pattern='no_ofld_reason:'
    outputList=[]

    for line in infile:
        if re.search(pattern, line):
            outputList.append(line.strip())

    occurrences = collections.Counter(outputList)
    sort_occur = sorted(occurrences.items(), key = lambda x : x[1])

    outfile.write("""
The number of sessions which are not offloaded, along with it's reason:
=======================================================================
 
""")
    x = ('\n'.join(''.join(str(elems)) for elems in sort_occur))
    outfile.write(x)
    
    outfile.close()
    infile.close()



if __name__ == "__main__":
    if not len(sys.argv) == 3:
        print("Usage: {} input_file output_file".format(sys.argv[0]))

    main(sys.argv[1], sys.argv[2])