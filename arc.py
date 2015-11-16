#!/usr/bin/python
# coding:utf-8

__version__ = '1.0'
__author__ = "wstchql@gmail.com"

import sys
import os
import struct

dirname = os.path.dirname(os.path.abspath(__file__))#make dirname
if dirname.endswith('.zip'):
	dirname = os.path.dirname(dirname)
os.chdir(dirname)#change dir
#os.path.abspath = os.path.dirname + os.path.basename 

python_dll = "python%d%d.dll" % sys.version_info[:2]#define python_dll

arcname = os.path.join(dirname, 'python27.zip')#define zipfile's path
assert os.path.isfile(arcname), u'%s not exists!' % arcname

arcbytes = open(arcname, "rb").read()#read the original file
arcfile = open(arcname, "wb")

# bundle pythonxy.dll
print "Adding %s to %s" % (python_dll, arcname)
arcfile.write("<pythondll>")
bytes = open(os.path.join(dirname, python_dll), "rb").read()
arcfile.write(struct.pack("i", len(bytes)))
arcfile.write(bytes) # python dll

arcfile.write(arcbytes)#restore the original file
arcfile.close()
print "Success!"