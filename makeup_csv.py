#!/usr/bin/python
# @Time : 2018/6/15 15:24
# @Author : lanceqli 

import sys
import os 

working_path = sys.path[0] + os.path.sep
def check_file(template_file, dict_keys):
    #print ("check: %s" % (template_file))
    fr = open(template_file)
    for line in fr:
        #print "--------------------------------------------------" 
        #print line 
        #break each line into a list
        values = line.split('@@@')     
        #print values
        for j, key in enumerate(values):
            #print j, key
            # check key
            csv_key = "@@@" + key + "@@@"
            nPos = line.find(csv_key)
            #find and matched
            if j%2 != 0 and nPos >= 0:
                #print("%s," % (csv_key))
                dict_keys[csv_key] = "aaa"

    fr.close()


def scan_path(rootDir, dict_keys): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        for f in files: 
            template_file = os.path.join(root, f)
            check_file(template_file, dict_keys) 


def save_keys(dict_keys, csv_file):
    fw = open(csv_file, 'a')
    list_keys = dict_keys.keys()
    for j, key in enumerate(list_keys):
        fw.write("%s,\n" % (key))
    fw.close()


def usage():
    print("============ usage =============")
    print("usage:python makeup_csv.py  <template_path> <keymap.csv>")
    print("============= usage ============")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    template_path = sys.argv[1]
    csv_file = sys.argv[2]
    dict_keys = {}

    scan_path(template_path, dict_keys)
    save_keys(dict_keys, csv_file)
    
