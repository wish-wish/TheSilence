#coding=utf-8
#__author__ = 'cclin'
#write by cclin 2015.5.10

#from openpyxl import Workbook
#from openpyxl import load_workbook
#import xlrd

import sys
import os,os.path
import re
import xml.dom.minidom as minidom         
from xml.etree import ElementTree as ET   
import codecs
import commands
from subprocess import Popen,PIPE
import subprocess
import time
   
def walk_dirs(dir,list,topdown=True):       
    for root, dirs, files in os.walk(dir, topdown):        
        for name in dirs:            
            path=os.path.join(root,name)+r"/"
            path=path.replace("\\","/")
            #pa=path.lower()
            list.append(path)
            print path

def walk_files(dir,list,topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            ext=os.path.splitext(name)[1]
            file=os.path.join(root,name)     
            file=file.replace("\\","/")
            print file
            if (ext == '.lua') and  file.find(".svn")==-1 and file not in list:                
                list.append(file)
                #print file;
    
def getCurrentPath():
    return os.path.split(os.path.realpath(__file__))[0]+r"/"

def writeArrayToFile(rlist,rfile):        
    f=open(rfile,"a")    
    for line in rlist:
        f.write(line+"\n")
    f.flush()
    f.close()

def writeLineToFile(line,rfile):
    f=open(rfile,"a")        
    f.write(line+"\n")
    f.flush()
    f.close()

def deleteFile(rfile):
    if os.path.exists(rfile):
        os.remove(rfile)
        
def deleteEmptyLine(rfile):
    f=open(rfile,"r")
    newlist=[]
    for line in f:        
        if line.strip()!="":            
            newlist.append(line)            
    wf=open(rfile,"w")     
    wf.truncate()
    wf.writelines(newlist)
     
class TextArea(object):
    def __init__(self):
        self.buffer=[]
    def write(self,*args,**kwargs):
        self.buffer.append(args)        
        stdout.write(str(args)+"\n")
        
if __name__ == '__main__':
    reload(sys) 
    sys.setdefaultencoding( "utf-8" )  
    ss=u"请关注全国留守儿童，请关注全国城乡差距，请关注全国教育现状......"
    print ss
    cmd = "TITLE "+ss
    os.system(cmd.encode('gb2312'))    
    print "author cclin 2015.04"
    print "support:e-mail=12092020@qq.com"
    print "copyright 2015~2018 for anyone to use"
    cmdcompile=getCurrentPath()+"cocos2d/tools/cocos2d-console/bin/cocos.bat compile -p android -ap 10";
        
    #stdout=sys.stdout
    #sys.stdout=TextArea();
    os.system(cmdcompile)
    os.system("adb install-multiple -lr proj.android/bin/skydream-debug.apk");
    os.system("pause")
    #os.system("dir")
    #'''
    p=subprocess.Popen(cmdcompile,stdout=subprocess.PIPE,shell=False)
    #logs=p.communicate()
    #print logs;    
    while p.poll() == None:
        logline=p.stdout.readline()
        if logline.strip()!="":
            print logline,
        time.sleep(1)    
    print "ret code=",p.returncode
    #'''
    #text_area,sys.stdout = sys.stdout,stdout
    #sys.stderr.write("abcd")
    #print text_area.buffer;
    #os.system("pause")
        
    #sys.stdout.write("please input:")
    #print sys.stdin.readline()
    
    #result,output=commands.getstatusoutput('"cocos2d/tools/cocos2d-console/bin/cocos.bat" compile -p android -ap 10')    
    #print(result)
    #print(output)
    
    