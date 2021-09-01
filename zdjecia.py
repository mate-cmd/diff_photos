import os
import sys
var1 = sys.argv[1:2]
delete_path = "/home/mpanczysz/Desktop/Priv/obrobic/"

def read_photos_list(file_name):
 f = open(file_name,"r")
 f.closed
 f_list  = []
 for row_in_list in f:
     f_list.append(row_in_list.rstrip())
 return f_list

def find_duplicates():
 for row_source in range(0,len(source_list)):
   if source_list[row_source] in dest_list:
       print(source_list[row_source])

def remove_duplicates(var1,delete_path):
    if 'usun' in var1:
     delete_list = read_photos_list("to_delete.txt")
     for row_delete in range(0,len(delete_list)):
      os.system("rm "+delete_path+delete_list[row_delete])
     os.system("rm to_delete.txt")

def generate_sum_list():
    os.system("ls -l "+delete_path+"| awk '{print $9}' | grep -iv ^$>/tmp/suma.txt")

generate_sum_list()

remove_duplicates(var1,delete_path)

os.system("ls -l | awk '{print $9}' | grep -iv ^$>to_check.txt")

source_list = read_photos_list("to_check.txt")
dest_list = read_photos_list("/tmp/suma.txt")

find_duplicates()

os.system("rm to_check.txt")