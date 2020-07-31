#!/usr/bin/python3

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
    
    pattern='no_ofld_reason:'
    patter= re.compile(r'proto=[0-9]*')
    patte='npu_state_err'
    patt=re.compile(r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*:[0-9]*->[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*:[0-9]*')
    pat=re.compile(r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*:[0-9]*')
    
    outputList=[]
    outputLis=[]
    outputLi=[]
    outputL=[]
    
        
    for line in infile:
        if re.search(pattern, line):
            outputList.append(line.strip())
        if re.search(patter, line):
            #print(line, end = '')
            y = re.search(patter, line).group()
            outputLis.append(y.strip())
        if re.search(patte, line):
            outputLi.append(line.strip())
        if re.search(patt, line):
            b = re.search(patt, line).group()
            c = re.search(pat, b).group()
            outputL.append(c.strip())

    occurrences = collections.Counter(outputList)
    sort_occur = sorted(occurrences.items(), key = lambda x : x[1])

    occurrence = collections.Counter(outputLis)
    sort_occu = sorted(occurrence.items(), key = lambda x : x[1])

    occurrenc = collections.Counter(outputLi)
    sort_occ = sorted(occurrenc.items(), key = lambda x : x[1])


    occurren = collections.Counter(outputL)
    sort_oc= sorted(occurren.items(), key = lambda x : x[1])
    sort = sort_oc[-10:]

    outfile.write("""
The number of sessions which are not offloaded, along with it's reason:
=======================================================================
 
""")
    x = ('\n'.join(''.join(str(elems)) for elems in sort_occur))
    outfile.write(x)
    
    outfile.write("""


The protocols seen in the session list, along with it's count:
==============================================================
 
""")
    
    z = ('\n'.join(''.join(str(elem)) for elem in sort_occu))
    outfile.write(z)

    outfile.write("""


The npu errors seen in the session list, along with it's count:
==============================================================
 
""")
    
    a = ('\n'.join(''.join(str(elem)) for elem in sort_occ))
    outfile.write(a)

    outfile.write("""


Top 10 IP addresses seen in the session list:
=============================================
 
""")


    d = ('\n'.join(''.join(str(elem)) for elem in sort))
    outfile.write(d)



    outfile.close()
    infile.close()


if __name__ == "__main__":
    if not len(sys.argv) == 3:
        print("Usage: {} input_file output_file".format(sys.argv[0]))

    main(sys.argv[1], sys.argv[2])