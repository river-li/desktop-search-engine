import jieba
import os
import SearchFiles
import numpy
DOCINDEX = []
WORDLIST = []
ind={}
c_list =[]

class indx(object):
    def __init__(self,word,docid,wordf):
        self.word =word
        self.docid = docid
        self.wordf = wordf

def Create_indx(addre):
    q = SearchFiles.DirFiles(addre)
    f_list = q.Get_File_List(addre)
    global c_list
    c_list = q.Select_Correct_Files(f_list)
    f=[]
    s =""
    d =[]
    for i in range(len(c_list)):         #i为文档编号，f【i】为文档内容，s【i】为文档中
        f = open(c_list[i],'r')
        s = f.read()
        f.close()
        d.append(jieba.lcut(s))
    global ind
    for m in range(len(d)):
        for n in range(len(d[m])):
            w=d[m][n]
            if w not in WORDLIST:
                temp = indx(w,m,1)
                ind[temp.word] = [[m,temp.wordf]]
                WORDLIST.append(w)
            else:
                flags=0
                for r in range(len(ind[w])):
                    if ind[w][r][0] == m:
                        ind[w][r][1] = ind[w][r][1]+1
                        flags = 1
                if flags==0:
                    ind[w].append([m,1])

    os.chdir(os.path.abspath(os.getcwd()))
    k = open('/home/river/index.txt','w+')
    x = ind.items()
    x = list(x)
    for i in range(len(ind)):
        k.write(x[i][0])
        k.write('\n')
        for r in range(len(x[i][1])):
            k.write(str(x[i][1][r]))
        k.write('\n')
    k.flush()
    k.close()




def search_indx(stri):
    wod = stri.split(' ')
    res = []
    for i in range(len(wod)):
        if ind.get(wod[i]) != None:
            for a in range(len(ind[wod[i]])):
                tem=[]
                tem.extend(ind[wod[i]][a])
                res.append(tuple(tem))
    res = sorted(res,key = lambda w:w[1])
    resu = []
    for m in range(len(res)):
        k=res[m][0]
        print(len(c_list))
        print(k)
        f = open(c_list[k],'r')
        resu.append(str(f.read()))
    return resu



    #res 为按照词频排序好的数组，内容为各条目索引
