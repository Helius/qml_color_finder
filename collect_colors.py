#!/usr/bin/python

import sys
import os
import re

if len(sys.argv) != 3:
    print ("Usage: path-to-qml-src gitlab-domain")
    exit(1)
print ("Gonna collect data from " + sys.argv[1])

src_path = sys.argv[1]
src_url  = sys.argv[2]

def get_files(path):
    arr = []
    for root, subdirs, files in os.walk(path, topdown=True):
        subdirs[:] = [d for d in subdirs if d != "Templates-Out"]
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension == ".qml" or file_extension == ".js":
                arr.append(os.path.join(root, file))
    return arr


#{file, color, name}

def process_line(filename, strnum, line):
    #print(line)
    url = ""
    name = ""

    # skip comments
    if re.match("\s*//", line):
        return None

    line.strip()
    
    # skip line without color code
    p0 = re.compile('.*\"(#[abcdefABCDEF0-9]+)\"')
    res = p0.findall(line)
    if len (res) == 0:
        return None
    color = res[0]
    print filename    

    url = re.sub("^.*qmlsdk/ProjectsQml", src_url + "/v4/qmlsdk/blob/master/ProjectsQml",filename)\
            +"#L"\
            +str(strnum)

    p1 = re.compile(".*color\s*([^\s]+)\s*:\s*\"#[0-9abcdefABCDEF]+\"")
    res = p1.findall(line)
    if len(res) > 0:
        name = res[0]

#    print url
#    print strnum
#    print line
#    print color
#    print name

    return [url, color, name]


def process_files():
    colors = []

    for file in get_files(src_path):
        with open(file) as f:
                tmp = f.read().splitlines()
        strnum = 0
        for line in tmp:
            strnum = strnum+1
            new_color = process_line(file, strnum ,line)
            if new_color != None:
                colors.append(new_color)
                #print new_color
    return colors

    

colors = process_files()

with open(".tmp.colors", 'w') as f:
    for item in colors:
        f.write("%s;%s;%s\n" % (item[0], item[1], item[2]))

