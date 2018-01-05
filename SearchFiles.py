#文中变量名称统一小写，函数名称首字母大写并且单词间加下划线；类名称首字母大写
#全局通用变量全部为大写字母
import os
FILE_EXT = ['doc','txt','html']
FILEDICT = {}           #用于储存符合要求的文件,key为文件位置及名称,value 为文件类型


class DirFiles(object):
    def __init__(self,st):
        try:
            os.chdir(st)
        except:
            os.path.isfile(st) | os.path.isdir(st) == False
    npath = os.getcwd()
    file_list = []
             #npath为当前目录

    def Get_File_List(self,path):
        #用于获得当前目录下所有文件的方法，返回一个列表，列表中的项是文件的路径
        if os.path.isdir(path)==True:
            #如果路径存在则获取目录下所有子项
            aldirs = os.listdir(path)
        else:
            aldirs=None

        file_list=[]
        #一个空的列表，用于储存结果
        if aldirs!=None:
            for x in aldirs:
                if os.path.isfile(path+'/'+x)==True:
                    file_list.append(path+'/'+x)
            cdir_list = self.Get_Dir_List(path)
            # 获取当前目录下的子目录
            if len(cdir_list) == 0:         #若当前目录下无其他目录,则返回现有文件列表
               return file_list
            else:
                for dirs in cdir_list:
                    file_list.extend(self.Get_File_List(dirs))    #递归调用查找文件函数对对子文件夹进行搜索
        return file_list

    def Get_Dir_List(self,path):
       dir_list=[]
       if os.path.isdir(path)!=False:
           for x in os.listdir(path+'/'):
               if os.path.isdir(path+'/')== True:
                   dir_list.append(path+'/'+x)
               else:
                   pass
       return dir_list




    def Select_Correct_Files(self,file_list):    #筛选文件列表中符合要求的文件,返回符合要求的文件个数
        correct_list = []
        global FILE_EXT
        for file in file_list:              #将列表中文件遍历，并以.分割，若后缀符合要求则添加至字典及列表
            b = str(file).split('.')
            if b[-1] in FILE_EXT:
                FILEDICT[file]=b[-1]
                correct_list.append(file)
        return correct_list
