#-------------------------------------------------------------------------------
# Name:        segment
# Purpose:
#
# Author:      haoyun
#
# Created:     23/11/2015
# Copyright:   (c) haoyun 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import HMM

def generate_dic():
    dictionary = {}
    f = open("dic.txt","r")
    file = f.read()
    file = file.replace("\n",' ')
    k = file.split(' ')
    for i in k:
        dictionary[i] = dictionary.get(i,1)
    return(dictionary)

def backward_search(a,dic,new_dic,l):
    #逆序搜索

    point_tail = len(a)
    point_head = max(point_tail - l,0)
    ans = []
    while point_tail > 0 :
        while not(point_tail <= point_head +1 or check(a,point_head,point_tail,dic,new_dic)):
            point_head += 1
        ans.append(a[point_head:point_tail])

        point_tail = point_head
        point_head = max(point_tail - l,0)
    return (ans)

def forward_search(a,dic,new_dic,l):
    #正序搜索
    point_tail = 0
    point_head = min(point_tail + l,len(a))
    ans = []
    while point_tail < len(a) :
        while not(point_head <= point_tail +1 or check(a,point_tail,point_head,dic,new_dic)):
            point_head -= 1
        ans.append(a[point_tail:point_head])

        point_tail = point_head
        point_head = min(point_tail + l,len(a))
    return (ans)

def check(a,head,tail,dic,new_dic):
    t = a[head:tail]
    if t in dic or t in new_dic:
        return True
    else:
        return False

def compare(divide1,divide2):
    #寻找前后不同并用hmm
    p1 = 0
    sum_len1 = 0
    p2 = 0
    sum_len2 = 0
    new_ans = []
    while True:
        sum_len1 += len(divide1[p1])
        sum_len2 += len(divide2[p2])

        if divide1[p1] == divide2[p2]:
            new_ans.append(divide1[p1])
        else:
            prefixpoint = p1  #开始点
            wrongcut= [divide1[p1]]
            while sum_len1!=sum_len2:
                if sum_len1<sum_len2:
                    p1+=1
                    sum_len1 +=len(divide1[p1])
                    wrongcut.append(divide1[p1])
                else:
                    p2+=1
                    sum_len2 += len(divide2[p2])
            suffixpoint = p1  #结束点
            if prefixpoint > 0:
                wrongcut.insert(0,divide1[prefixpoint-1])
                new_ans.pop()
            if suffixpoint < len(divide1)-1:
                if divide1[p1+1] == divide2[p2+1]:
                    wrongcut.append(divide1[suffixpoint+1])
                    divide1.pop(p1+1)
                    divide2.pop(p2+1)
            recut = "".join(wrongcut)
            a = HMM.cutUnrecognized(recut)
            for i in range(len(a)):
                new_ans.append(a[i])
        p1 +=1
        p2 +=1
        if p1>=len(divide1) or p2>=len(divide2):
            break
    re = "|".join(new_ans)
    return re

def recutsingle(divide1):
        #将分的过于疏松的再分一遍
    mark1 = {}
    mark1[-1] = "d"
    devide1_1 = []
    mark1[len(divide1)] = "d"
    for i in range(len(divide1)):
        if len(divide1[i])==1:
            mark1[i] = "s"
        else:
            mark1[i] = "d"
    for i in range(len(divide1)):
        if mark1[i] == "d":
            devide1_1.append(divide1[i])
        if mark1[i-1] == "d" and mark1[i] == "s":
            temp=[]
            j = i
            while mark1[j] == "s":
                temp.append(divide1[j])
                j +=1
            if j-i >=3:
                new = "".join(temp)
                devide1_1 += HMM.cutUnrecognized(new)
            else:
                for t in range(i,j):
                    devide1_1.append(divide1[t])
    return devide1_1

def search(sentence,dic,new_dic):
    #主要结构部分
    l = 5

    divide1 = backward_search(sentence,dic,new_dic,l)
    divide1 = divide1[::-1]
    divide1 = recutsingle(divide1)
    ans1 = "|".join(divide1)

    divide2 = forward_search(sentence,dic,new_dic,l)
    divide2 = recutsingle(divide2)
    ans2 = "|".join(divide2)

    add = compare(divide1,divide2)
    tup = (ans1,add)
    return(tup)
def devide():
    readfile = open("reading.txt","r")
    file_c = readfile.read()
    readfile.close()

    content = file_c
    import string

    readfile_p2 = open("punc2.txt","r")
    punc2 = readfile_p2.read()
    new_dic = {}
    for i in range(len(punc2)//2):
        point1 = content.find(punc2[2*i])
        point2 = content.find(punc2[2*i+1])
        while point1 != -1 and point2 != -1:
            if point2-point1 <= 4:
                new_dic[content[point1+1:point2]] = new_dic.get(content[point1+1:point2],0)+1
            point1 = content.find(punc2[2*i],point1+1)
            point2 = content.find(punc2[2*i+1],point2+1)
    readfile_p2.close()
# 从引号和括号中搜索新词

    readfile_p1 = open("punc1.txt","r")
    punc1 = readfile_p1.read()
    punc = list(punc1)+list(punc2)
    for i in range(len(content)):
        if content[i] in punc:
            content = content.replace(content[i]," ")

    ans = content.split(" ")
    while('' in ans):
        ans.remove('')
    readfile_p1.close()
#按标点分开

    dic = generate_dic()
    writefile = open("writing.txt","w+")
    for number in range(len(ans)):
            tuple_ans = search(ans[number],dic,new_dic)
            writefile.write("{0}\n".format(tuple_ans[1]))
    writefile.close()


if __name__ == '__main__':
    devide()
