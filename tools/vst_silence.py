#coding=utf-8
#__author__ = 'cclin'
#write by cclin 2021.03.24

import sys
import os,os.path
import re
import codecs
import xml.dom.minidom as minidom         
from xml.etree import ElementTree as ET

# ==由于minidom默认的writexml()函数在读取一个xml文件后，修改后重新写入如果加了newl='\n',会将原有的xml中写入多余的行
#　 ==因此使用下面这个函数来代替
def fixed_writexml(self, writer, indent="", addindent="", newl=""):
    # indent = current indentation
    # addindent = indentation to add to higher levels
    # newl = newline string
    writer.write(indent+"<" + self.tagName)

    attrs = self._get_attributes()
    a_names = attrs.keys()
    a_names.sort()

    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        minidom._write_data(writer, attrs[a_name].value)
        writer.write("\"")
    if self.childNodes:
        if len(self.childNodes) == 1 \
          and self.childNodes[0].nodeType == minidom.Node.TEXT_NODE:
            writer.write(">")
            self.childNodes[0].writexml(writer, "", "", "")
            writer.write("</%s>%s" % (self.tagName, newl))
            return
        writer.write(">%s"%(newl))
        for node in self.childNodes:
            if node.nodeType is not minidom.Node.TEXT_NODE:
                node.writexml(writer,indent+addindent,addindent,newl)
        writer.write("%s</%s>%s" % (indent,self.tagName,newl))
    else:
        writer.write("/>%s"%(newl))

minidom.Element.writexml = fixed_writexml

'''
    # 1.创建DOM树对象
    dom=minidom.Document()
    # 2.创建根节点。每次都要用DOM对象来创建任何节点。
    root_node=dom.createElement('root')
    # 3.用DOM对象添加根节点
    dom.appendChild(root_node)

    # 用DOM对象创建元素子节点
    book_node=dom.createElement('book')
    # 用父节点对象添加元素子节点
    root_node.appendChild(book_node)
    # 设置该节点的属性
    book_node.setAttribute('price','199')

    name_node=dom.createElement('name')
    root_node.appendChild(name_node)
    # 也用DOM创建文本节点，把文本节点（文字内容）看成子节点
    name_text=dom.createTextNode('计算机程序设计语言 第1版')
    # 用添加了文本的节点对象（看成文本节点的父节点）添加文本节点
    name_node.appendChild(name_text)
    
    <?xml version="1.0" encoding="utf8"?>
    <root>
        <book price="99">
            <name>计算机程序设计语言 第1版</name>
        </book>
    </root>
    
    # 其他属性与方法：
    # 获取根节点
    root=dom.documentElement
    # 节点名称
    print(root.nodeName)
    # 节点类型：'ELEMENT_NODE'，元素节点； 'TEXT_NODE'，文本节点； 'ATTRIBUTE_NODE'，属性节点
    print(root.nodeType)
    # 获取某个节点下所有子节点，是个列表
    print(root.childNodes)
    # 根据标签名获取元素节点，是个列表
    book=root.getElementsByTagName('book')
    # 获取节点属性
    print(book[0].getAttribute('price'))
    # 获取某节点的父节点
    print(author.parentNode.nodeName)
'''

def walk_dirs(dir,list,topdown=True):       
    for root, dirs, files in os.walk(dir, topdown):        
        for name in dirs:            
            path=os.path.join(root,name)+r"/"
            path=path.replace("\\","/")
            #pa=path.lower()
            list.append(path)
            print path

def walk_files(dir,list,aext,topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            ext=os.path.splitext(name)[1]
            file=os.path.join(root,name)     
            file=file.replace("\\","/")
            #print file
            if (ext == aext) and  file.find(".svn")==-1 and file not in list:                
                list.append(file)
                #print file;

def forceDirectory(file):
    path=os.path.dirname(file);    
    if not os.path.exists(path):
        os.makedirs(path);

def nappendArrayToFile(rlist,rfile):        
    f=open(rfile,"a")    
    for line in rlist:
        f.write(line+"\n")
    f.flush()
    f.close()
    
def nwriteArrayToFile(rlist,rfile):
    forceDirectory(rfile);
    f=open(rfile,"w")    
    for line in rlist:
        f.write(line+"\n")
    f.flush()
    f.close()

def deleteEmptyLine(rfile):
     f=open(rfile,"r")
     newlist=[]
     for line in f:        
        if line.strip()!="":            
            newlist.append(line)            
     wf=open(rfile,"w")     
     wf.truncate()
     wf.writelines(newlist)

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

def isPlatformRealWin32(projfile):
    iswin32s=[];
    iswin32s.append("2d/libcocos2d.");
    iswin32s.append("proj.win32/");
    isWin32Proj=False;
    for line in iswin32s:
        if projfile.find(line)>=0:
            isWin32Proj=True;
    nowin32s=[];
    nowin32s.append("__PACKAGE_NAME__");
    nowin32s.append("-template-");
    for line in nowin32s:
        if projfile.find(line)>=0:
            isWin32Proj=False;
    return isWin32Proj;
    
def getRootDir(projfile):
    dirtrees=projfile.split("/");
    rootdir="";
    for dir in dirtrees:
        if dir.startswith("cocos2d"):
            break;
        if rootdir!="":
            rootdir=rootdir+"/";
        rootdir=rootdir+dir;
    if projtype=="project":
        rootdir=rootdir+"\\..\\..";
    #print rootdir;
    forceDirectory(rootdir);
    #print rootdir;
    return rootdir;
    
def getEngineDir(projectfiles):    
    for line in projectfiles:
        if line.find("/dragonbones/renderer/")>-1:
            continue;
        if line.find("cocos2d")>-1:
            rootdir=getRootDir(line);
            return rootdir;
    print "error get Enginedir";
    return "";
    
def SolutionRelList(fileName):
    namelist=[];
    namelist.append("libbox2d.vcxproj");
    namelist.append("libcocos2d.vcxproj");
    namelist.append("libluacocos2d.vcxproj");
    namelist.append("libJSBinding.vcxproj");
    namelist.append("libsimulator.vcxproj");
    namelist.append("libSpine.vcxproj");
    namelist.append("skydream.vcxproj");
    namelist.append("quick_libs.vcxproj");
    for line in namelist:        
        if fileName.strip()==line.strip():            
            return True;
    return False;
    
def changeOutDir(projfile,rootdir):
    #print projfile;
    arr=projfile.split("/");    
    #print arr[len(arr)-1];
    rootdir=rootdir.replace("/","\\");
    if projtype=="project":
        outdir="$(SolutionDir)..\\..\\..\\_out\\$(SolutionName)\\$(Configuration).$(Platform)\\";
        intdir="$(SolutionDir)..\\..\\..\\_out\\$(SolutionName)\\_int\\$(ProjectName)_$(Configuration).$(Platform)\\";
        logdir="$(SolutionDir)..\\..\\..\\_out\\$(SolutionName)\\_log\\$(ProjectName)_$(Configuration).$(Platform)\\";#vs log 2013
    else:
        outdir=rootdir+"\\_out\\$(SolutionName)\\$(Configuration).$(Platform)\\";
        intdir=rootdir+"\\_out\\$(SolutionName)\\_int\\$(ProjectName)_$(Configuration).$(Platform)\\";
        logdir=rootdir+"\\_out\\$(SolutionName)\\_log\\$(ProjectName)_$(Configuration).$(Platform)\\";#vs log 2013
    print projtype,arr[len(arr)-1],outdir;
    
    proj_dom=minidom.parse(projfile)
    items=proj_dom.getElementsByTagName("OutDir")
    for item in items:
        item.childNodes[0].nodeValue=outdir;
    
    items=proj_dom.getElementsByTagName("IntDir")
    for item in items:
        item.childNodes[0].nodeValue=intdir;
    '''
    items=proj_dom.getElementsByTagName("Path")
    for item in items:
        item.childNodes[0].nodeValue=logdir;
    '''
    prettyxml=proj_dom.toprettyxml()
    f=open(projfile,"w")
    f.write(prettyxml)  
    f.close()

def listVSProjs(path):
    #path=r"F:\_ccWork\cocos\skydream\client";
    projfiles=[];
    global projtype;
    realwinewproj=[];
    projtypes=[];
    walk_files(path,projfiles,".vcxproj");
    for line in projfiles:        
        if isPlatformRealWin32(line):
            realwinewproj.append(line);
            projtypes.append(getDirType(line))
    nwriteArrayToFile(realwinewproj,getCurrentPath()+"./vsprojs.txt");  

    projtype=getDirType(realwinewproj[0]);
    rootdir=getEngineDir(realwinewproj);
    #convert out & int dirs
    i=0;
    for line in realwinewproj:
        #print line;
        projtype=projtypes[i];
        changeOutDir(line,path);
        i=i+1;

def getDirType(projfile):
    atype="project";
    if projfile.endswith("Naruto.vcxproj"):
        atype="project";
    elif projfile.find(projroot)>-1 and projfile.find("cjoy_proj")==-1:
        atype="project";
    elif projfile.find("samples")>=0:
        atype="samples";
    elif projfile.find("template")>=0 or projfile.find("templates")>=0:
        atype="template";
    else:
        atype="engine";
    return atype;

def listSolution(path):
    slnfiles=[];    
    walk_files(path,slnfiles,".sln");    
    nwriteArrayToFile(slnfiles,getCurrentPath()+"./vsslns.txt");
    for line in slnfiles:
        print line;
    return slnfiles;
    
def copyProjects(path):
    slnfiles=[];
    projfiles=[];
    global c2dx_ver
    c2dx_ver="cocos2d-x-2.2.6";
    global projroot
    projroot="dx2-project";
    global toolset
    toolset="v142"
    #toolset="v120_xp"
    global buildir
    buildir="$(SolutionDir)..\\..\\..\\_out\\$(SolutionName)\\"
    global gpath
    gpath="D:\\Cocos\\TheSilence\\"+projroot+"\\Naruto";
    walk_files(gpath,slnfiles,".sln"); 
    global c2dx
    c2dx="D:\\Cocos\\TheSilence\\"+c2dx_ver;
    walk_files(c2dx,projfiles,".vcxproj");
    global prj
    prj="D:\\Cocos\\TheSilence\\"+projroot+"\\";
    walk_files(path,projfiles,".vcxproj");
    '''
    sprj=os.path.split(os.path.realpath(slnfiles[0]))[0]+r"/";
    forceDirectory(sprj+"cjoy_proj"+r"/");
    parseSolution(sprj,slnfiles[0],projfiles);
    '''
    for line in slnfiles:
        print "copyProjects",line;
        if line.find("cjoy.sln")>-1:
            continue;
        path=os.path.split(os.path.realpath(line))[0]+r"/";
        forceDirectory(path+"cjoy_proj"+r"/");
        parseSolution(path,line,projfiles);
    
def trim(s):
    if len(s)==0:
        return ''
    if s[:1]==' ':
        return trim(s[1:])
    elif s[-1:]=='':
        return trim(s[:-1])
    else:
        return s
        
def trimyin(s):
    if len(s)==0:
        return ''
    if s[:1]=='"' or s[:1]=="'" or s[:1]==' ':
        return trim(s[1:]);
    elif s[-1:]=='"' or s[-1:]=="'" or s[-1:]==' ':
        return trim(s[:-1])
    else:
        return s
        
def convertPath(slnpath,projfile,projfiles):
    realpath="";
    newfile="";
    for line in projfiles:
        arr=line.split("/");
        if projfile==arr[len(arr)-1]:#TODO:同名
            realpath=line;
            break;
    dt=getDirType(realpath);
    print "dt",dt
    if realpath!="": #and getDirType(realpath)!="project":
        rf=open(realpath,"r")
        cnts=[]
        for line in rf:
            cnts.append(line);
        newfile=slnpath+"cjoy_proj\\"+projfile;
        print realpath,newfile;
        wf=open(newfile,"w")
        wf.truncate();
        wf.writelines(cnts)
        wf.close();
        
        fp=realpath+".filters";
        if dt=="project":
            fp=slnpath+projfile+".filters";
        if os.path.exists(fp):
            rff=open(fp,"r")
            cntfs=[]
            for line in rff:
                cntfs.append(line);
            newfilef=slnpath+"cjoy_proj\\"+projfile+".filters";
            print "-----------------",fp,newfilef;
            wff=open(newfilef,"w")
            wff.truncate();
            wff.writelines(cntfs)
            wff.close();
            
    if dt=="project":
        return newfile,slnpath+projfile;
    else:
        return newfile,realpath;

def parseSolution(path,slnfile,projfiles):
    rf=open(slnfile,"r")
    cnts=[];
    spath=os.path.split(os.path.realpath(slnfile))[0]+r"/";
    ar=os.path.splitext(os.path.realpath(slnfile))[0].split("\\");
    fs=ar[len(ar)-1];
    #print "a",fs
    for line in rf:
        if line.startswith("Project"):
            arr=line.split(",");
            brr=trim(arr[1])[1:-1].split("\\");
            fn=brr[len(brr)-1];
            fn1=fn.split(".")[0];
            #print "b",trim(arr[1]),fn,fn1;
            
            cnts.append(arr[0]+',".\\cjoy_proj\\'+fn+'",'+arr[2]);
            newfile,realpath=convertPath(path,fn,projfiles);
            print "p",newfile,realpath
            if newfile!="":
                convertCodeRelative(newfile,realpath);
        else:
            cnts.append(line);
    wf=open(spath+ar[len(ar)-1]+"_cjoy.sln","w");
    wf.truncate();
    wf.writelines(cnts);

def pathRelative(path1,path2):#path1 to path2
    relpath=os.path.relpath(path2,path1);
    #print "rel",relpath;
    return relpath

def setFilters(filters1,filters2,inc,incnew):
    i=0;
    for it in filters1:
        if it.getAttribute('Include')==inc:
            #print i,len(filters1[i].childNodes),inc,incnew;
            filters1[i].setAttribute('Include',incnew);
            #if len(filters1[i].childNodes)>0:
            #    filters1[i].appendChild(filters2[i].childNodes[0]);
        i=i+1;
            
def convertCodeRelative(newfile,realpath):
    real_dom=minidom.parse(realpath)
    print newfile;
    new_dom=minidom.parse(newfile)
    real_dom_filter=minidom.parse(realpath+".filters")
    new_dom_filter=minidom.parse(newfile+".filters")
    
    ritems=real_dom.getElementsByTagName("AdditionalIncludeDirectories")
    nitems=new_dom.getElementsByTagName("AdditionalIncludeDirectories")
    
    npath=os.path.split(os.path.realpath(newfile))[0]+r"/";
    rpath=os.path.split(os.path.realpath(realpath))[0]+r"/";
    #print npath,"aaa",rpath;
    dt=getDirType(newfile);
    print dt,"abcde",newfile
    i=0;
    for it in ritems:
        val=ritems[i].childNodes[0].nodeValue;
        #print val;
        vals=val.split(";");
        nvals="";
        for line in vals:
            #print 'line',line;
            codepath=line;
            if line[0:]!="$" and line.startswith(".."):
                pa=pathRelative(npath,rpath+line);
                codepath=pa;
                #print 'bbb',pa;
            elif line.find("$(ProjectDir)")>-1:
                pa=os.path.split(os.path.realpath(line))[0]+r"/";
                if dt=="project":
                    pa=rrpath=trimyin(trimyin(os.path.normpath(line.replace("$(ProjectDir)..\\..\\..\\","$(ProjectDir)..\\..\\..\\..\\..\\..\\"+c2dx_ver+"\\"))));
                    print 'aaa',pa
                else:
                    rrpath=trimyin(trimyin(os.path.normpath(line.replace("$(ProjectDir)",rpath))));
                    #print 'ccc',rrpath,npath;
                    pa=pathRelative(npath,rrpath);
                codepath="$(ProjectDir)"+pa;
            nvals=nvals+codepath+";";
            print "codepath,",codepath;
        nitems[i].childNodes[0].nodeValue=nvals;
        i=i+1;
    
    rcompiles=real_dom.getElementsByTagName("ClCompile")
    ncompiles=new_dom.getElementsByTagName("ClCompile")
    
    rcompiles_filters=real_dom_filter.getElementsByTagName("ClCompile")
    ncompiles_filters=new_dom_filter.getElementsByTagName("ClCompile")
    
    i=0;
    for it in rcompiles:#TODO;
        #print rcompiles[i].parentNode.nodeName,rcompiles[i].getAttribute('Include')
        if rcompiles[i].parentNode.nodeName!="ItemGroup":
            #print "continue"
            i=i+1;
            continue;
        val=rcompiles[i].getAttribute('Include');
        pa=rpath+val;
        nval=pathRelative(npath,pa);
        '''
        if newfile.find("Naruto.vcxproj")>-1:
            print 'ClCompile',val;
            print nval;'''
        ncompiles[i].setAttribute('Include',nval);
        setFilters(ncompiles_filters,rcompiles_filters,val,nval);
        i=i+1;
        
    rincludes=real_dom.getElementsByTagName("ClInclude")
    nincludes=new_dom.getElementsByTagName("ClInclude")
    
    rincludes_filters=real_dom_filter.getElementsByTagName("ClInclude")
    nincludes_filters=new_dom_filter.getElementsByTagName("ClInclude")
    
    i=0;
    for it in rincludes:#TODO;
        if rincludes[i].parentNode.nodeName!="ItemGroup":
            #print "continue"
            continue;
        val=rincludes[i].getAttribute('Include');
        #print 'ClInclude',val;
        pa=rpath+val;
        nval=pathRelative(npath,pa);
        nincludes[i].setAttribute('Include',nval);
        setFilters(nincludes_filters,rincludes_filters,val,nval);
        i=i+1;
        
    outdir=buildir+"$(Configuration).$(Platform)\\";
    intdir=buildir+"_int\\$(ProjectName)_$(Configuration).$(Platform)\\";
    logdir=buildir+"_log\\$(ProjectName)_$(Configuration).$(Platform)";
        
    items=new_dom.getElementsByTagName("OutDir")
    for item in items:
        item.childNodes[0].nodeValue=outdir;
    
    items=new_dom.getElementsByTagName("IntDir")
    for item in items:
        item.childNodes[0].nodeValue=intdir;

    items=new_dom.getElementsByTagName("Path")
    for item in items:
        item.childNodes[0].nodeValue=logdir;
        
    items=new_dom.getElementsByTagName("PlatformToolset");
    parnodes=[];
    for item in items:
        if not item.parentNode in parnodes:
            parnodes.append(item.parentNode);
    for par in parnodes:
        for item in items:
            if item.parentNode!=par:
                continue;
            is142=False;
            #print item.childNodes[0].nodeValue;
            if item.childNodes[0].nodeValue==toolset:
                #print it.nodeType;
                is142=True;
                break;
        if not is142:
            version_node=new_dom.createElement('PlatformToolset')
            par.appendChild(version_node)
            name_text=new_dom.createTextNode(toolset);
            version_node.appendChild(name_text);
    prettyxml=new_dom.toprettyxml()
    f=open(newfile,"w")
    f.write(prettyxml)  
    f.close()
    
    prettyxml=new_dom_filter.toprettyxml()
    f=open(newfile+".filters","w")
    f.write(prettyxml)  
    f.close()

def listUsers(path):
    slnfiles=[];    
    walk_files(path,slnfiles,".user");    
    nwriteArrayToFile(slnfiles,getCurrentPath()+"./vsusers.txt");
    
if __name__ == '__main__':
    reload(sys) 
    sys.setdefaultencoding( "utf-8" )  
    ss=u"请关注全国留守儿童，请关注全国城乡差距，请关注全国教育现状......"
    print ss
    cmd = "TITLE "+ss
    os.system(cmd.encode('gb2312'))    
    print "author cclin 2015.04/modify 2021.3.16"
    print "support:e-mail=12092020@qq.com"
    print "copyright 2015~2030 for anyone to use"
    
    #print trimyin(trimyin('"abc"'));
    
    #getRootDir("E:/_work/cocos2d-x-3.7/cocos/audio");
    path = getCurrentPath();
    #listVSProjs(path);
    
    #pathRelative(r"D:\Cocos\"+projroot+"\Naruto2.2.5\proj.win32","D:\Cocos\cocos2d-x\cocos2dx\proj.win32");
    
    copyProjects(path);
    
    #listSolution(path);
    
    #listUsers(path);