#coding=utf-8
#__author__ = 'cclin'
#write by cclin 2021.3.17

import sys
import os,os.path
import re
import codecs
import xml.dom.minidom as minidom         
from xml.etree import ElementTree as ET

if __name__ == '__main__':
    reload(sys) 
    sys.setdefaultencoding( "utf-8" )
    print u'中文'
    ssa=u'请关注全国留守儿童，请关注全国城乡差距，请关注全国教育现状......'
    print(ssa)
    cmd = "TITLE "+ssa
    os.system(cmd.encode('gb2312'))    
    print "author cclin 2015.04/modify 2021.3.16"
    print "support:e-mail=12092020@qq.com"
    print "copyright 2015~2030 for anyone to use"
    
    print u"hello vsc中文"