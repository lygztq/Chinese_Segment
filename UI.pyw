#-*- coding:utf-8 –*-
from tkinter import *
import tkinter.filedialog
import HMM
def main():
    pass

def test():
    print('test')

def quit():
    root.destroy()

def OpenFiles():
        filename=tkinter.filedialog.askopenfilename()
        filename=filename[2:]
        file=open(filename,"r")
        inputs.insert(1.0,file.read())

def addWords():
    kuangjia=Toplevel(root)
    newWordLabel=Label(kuangjia,text="please input your new word",fg='dark green')
    newWord=Text(kuangjia,height=2,width=15)
    pingLvLabel=Label(kuangjia,text="Please input the words frequency",fg='dark green')
    pinglv=Text(kuangjia,height=2,width=15)
    newWordLabel.pack()
    newWord.pack()
    pingLvLabel.pack()
    pinglv.pack()
    def addwordbutton():
        word=newWord.get(1.0,END)
        frequency=pinglv.get(1.0,END)
        oldDic=open('dic.txt','r')
        word=word[:-2]
        word=word+' '+frequency
        add=oldDic.readlines()
        oldDic.close()
        add=add+[word]
        add=''.join(add)
        newDic=open('dic.txt','w')
        newDic.write(add)
        newDic.close()
    finish=Button(kuangjia,text='Finish',command=addwordbutton,height=2,width=8)
    finish.pack()



def modifyWords():
    modifyframe=Toplevel(root)
    label=Label(modifyframe,text='you can modify the word directly on the box',fg='dark green',font=('Comic Sans MS',))
    text=Text(modifyframe,height=50,width=50)
    jindutiao=Scrollbar(modifyframe)
    jindutiao.pack(side=RIGHT,fill=Y)
    text['yscrollcommand']=jindutiao.set
    jindutiao['command']=text.yview
    label.pack()
    text.pack()
    dictionary=open('dic.txt','r')
    neiRong=dictionary.readlines()
    dictionary.close()
    neiRong=''.join(neiRong)
    text.insert(1.0,neiRong)
    def finishModify():
        newdictionary=open('dic.txt','w')
        newdictionary.truncate()
        newdictionary.write(text.get(1.0,END))
        newdictionary.close()
    Finish=Button(modifyframe,text='OK,I finish',font=('Comic Sans MS',),command=finishModify)
    Finish.pack()


def deleteWords():
    modifyframe=Toplevel(root)
    label=Label(modifyframe,text='you can delete the word directly on the box',fg='dark green',font=('Comic Sans MS',))
    text=Text(modifyframe,height=50,width=50)
    jindutiao=Scrollbar(modifyframe)
    jindutiao.pack(side=RIGHT,fill=Y)
    text['yscrollcommand']=jindutiao.set
    jindutiao['command']=text.yview
    label.pack()
    text.pack()
    dictionary=open('dic.txt','r')
    neiRong=dictionary.readlines()
    dictionary.close()
    neiRong=''.join(neiRong)
    text.insert(1.0,neiRong)
    def finishModify():
        newdictionary=open('dic.txt','w')
        newdictionary.truncate()
        newdictionary.write(text.get(1.0,END))
        newdictionary.close()
    Finish=Button(modifyframe,text='OK,I finish',command=finishModify)
    Finish.pack()


def generate_dic():
    dictionary = {}
    f = open("dic.txt","r",encoding='gbk')
    file = f.read().replace("\n",' ')
    k = file.split(' ')
    for i in k:
        dictionary[i] = dictionary.get(i,1)
    return(dictionary)


def Savefiles():
    filename=tkinter.filedialog.asksaveasfilename()
    filename=filename[2:]
    filename=filename+".txt"
    print(filename)
    file=open(filename,'w')
    a=inputs.get(1.0,END)
    file.write(a)
    file.close()

def Saveoutputfiles():
    filename=tkinter.filedialog.asksaveasfilename()
    filename=filename[2:]
    filename=filename+".txt"
    print(filename)
    file=open(filename,'w')
    a=outputs.get(1.0,END)
    file.write(a)
    file.close()


def copyrightfunc():
    a=Toplevel(root)
    a.title('Copyright')
    cp=Message(a,text="(c)Author:Chu HapYun;Zhang TianQi;Yan YuChen 2015",width=300)
    cp.pack()



def loadTheLexicon():
    dicname=tkinter.filedialog.askopenfilename()
    dictionary = {}
    f = open(dicname,"r")
    file = f.read()
    file = file.replace("\n",' ')
    k = file.split(' ')
    for i in k:
        dictionary[i] = dictionary.get(i,1)
    return(dictionary)


def loadTheRuleLibrary():
    libraryname=tkinter.filedialog.askopenfilename()
    rulelibrary={}
    f=open(libraryname,'r')
    file=f.readlines()
    for i in file:
        rulelibrary[i] = rulelibrary.get(i,1)
    return(rulelibrary)

def generate_rulelibrary():
    rulelibrary = {}
    f = open("rule.txt","r")
    k = f.readlines()
    for i in k:
        rulelibrary[i] = rulelibrary.get(i,1)
    return(rulelibrary)

def addRules():
    kuangjia=Toplevel(root)
    ruleFunctionLabel=Label(kuangjia,text='please input the typr of the rule(DELETE/SUBSTITUTE)(upward please):',fg='dark green')
    ruleFunction=Text(kuangjia,height=2,width=30)
    rulenameLabel=Label(kuangjia,text='Please input the word(if you want to substitute,please input the target word behind the old and a blank should be inputted between them):',fg='dark green')
    rulename=Text(kuangjia,height=2,width=30)
    ruleFunctionLabel.pack()
    ruleFunction.pack()
    rulenameLabel.pack()
    rulename.pack()
    def rulebuttonCommand():
        oldlibrary=open('rule.txt','r')
        text=oldlibrary.readlines()
        ruletype=ruleFunction.get(1.0,END)
        ruletype=ruletype[:-2]
        rule=rulename.get(1.0,END)
        text=text+[ruletype+' '+rule+'\n']
        newlibrary=open('rule.txt','w')
        for i in text:
            newlibrary.write(i)
        newlibrary.close()
    ruleButton=Button(kuangjia,text='Finish',command=rulebuttonCommand,height=2,width=8)
    ruleButton.pack()


def instructionfunc():
    a=Toplevel(root)
    a.title('HELP')
    Help=Text(a,height=50,width=100)
    Help.pack()
    file=open('help.txt','r')
    neirong=file.read()
    Help.insert(1.0,neirong)


def cleanTheText2():
    outputs.delete(0.0,END)
    inputs.delete(0.0,END)




def modifyRules():
    modifyframe=Toplevel(root)
    label=Label(modifyframe,text='you can modify or delete the rules directly on the box',fg='dark green',font=('Comic Sans MS',))
    text=Text(modifyframe,height=50,width=50)
    jindutiao=Scrollbar(modifyframe)
    jindutiao.pack(side=RIGHT,fill=Y)
    text['yscrollcommand']=jindutiao.set
    jindutiao['command']=text.yview
    label.pack()
    text.pack()
    dictionary=open('rule.txt','r')
    neiRong=dictionary.readlines()
    dictionary.close()
    neiRong=''.join(neiRong)
    text.insert(1.0,neiRong)
    def finishModify():
        newdictionary=open('rule.txt','w')
        newdictionary.truncate()
        newdictionary.write(text.get(1.0,END))
        newdictionary.close()
    Finish=Button(modifyframe,text='OK,I finish',command=finishModify)
    Finish.pack()


def segmentAText():
    def generate_rulelibrary():
        global rulelibrary
        rulelibrary = {}
        f = open("rule.txt","r")
        k = f.readlines()
        for i in k:
            rulelibrary[i] = rulelibrary.get(i,1)
        return(rulelibrary)

    def generate_dic():
        dictionary = {}
        f = open("dic.txt","r")
        file = f.read()

        k = file.split('\n')
        for i in range(len(k)):
            j = k[i].split(' ')
            if len(k[i])>3 or len(j[0])>1:
                dictionary[j[0]] = dictionary.get(j[0],1)
        return(dictionary)

        f.close()

    def backward_search(a,dic,new_dic,l):
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

    def isalnum(ob):
        return ob in string.ascii_letters or ob in string.digits
    def engordigit(content):
        a = set(content)
        return all(map(isalnum,a))

    def check(a,head,tail,dic,new_dic):
        t = a[head:tail]
        if t in dic or t in new_dic or engordigit(t):
            return True
        else:
            return False

    def compare(divide1,divide2):

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
                prefixpoint = p1
                wrongcut= [divide1[p1]]
                while sum_len1!=sum_len2:
                    if sum_len1<sum_len2:
                        p1+=1
                        sum_len1 +=len(divide1[p1])
                        wrongcut.append(divide1[p1])
                    else:
                        p2+=1
                        sum_len2 += len(divide2[p2])
                suffixpoint = p1
#               if prefixpoint > 0:
#                  wrongcut.insert(0,divide1[prefixpoint-1])
#                   new_ans.pop()
#               if suffixpoint < len(divide1)-1:
#                   if divide1[p1+1] == divide2[p2+1]:
#                       wrongcut.append(divide1[suffixpoint+1])
#                       divide1.pop(p1+1)
#                       divide2.pop(p2+1)
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
        # main algorithm
        l = 5

#        specialcase(sentence)

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
    # find new word from "" and ()
    filename=tkinter.filedialog.askopenfilename()
    generate_rulelibrary()
    openfile=open(filename,'r')
    file_c = openfile.read()
    openfile.close()
    content = file_c
    for i in list(rulelibrary.keys()):
        i=i.split()
        if i==[]:
            pass
        elif i[0]=='DELETE':
            content=content.replace(i[1],'')
        elif i[0]=='SUBSTITUTE':
            content=content.replace(i[1],i[2])
    print(content)
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

    tempc = []
    for i in range(len(content)):
        if content[i]!= "\n" and content[i]!= " " and content[i]!= "　":
            tempc.append(content[i])
    content ="".join(tempc)

    divpunc = "，。！？；"
    part = []
    i = 0
    while i < len(content):
        if content[i] in divpunc:
            part.append(content[i])
            i += 1
        else:
            tempp = []
            while content[i] not in divpunc:
                tempp.append(content[i])
                i += 1
            p = "".join(tempp)
            part.append(p)

    while('' in part):
        part.remove('')

# divide using , . ! ? ;
    outputfilename=tkinter.filedialog.asksaveasfilename()
    outputfilename=outputfilename+'.txt'
    outputfile=open(outputfilename,'w+')
    dic = generate_dic()
    no = 1
    for number in range(len(part)):
        if len(part[number])>1:
            tuple_ans = search(part[number],dic,new_dic)
            if part[number+1] in divpunc:
                 outputfile.write("{0}. {1}".format(no,tuple_ans[1]))
            else:
                 outputfile.write("{0}. {1}\n".format(no,tuple_ans[1]))
                 no +=1
        else:
             outputfile.write("{0}\n".format(part[number]))
             no +=1
    outputfile.close()
    teli=open(outputfilename,'r')
    neiRong=teli.read()
    for i in list(rulelibrary.keys()):
        i=i.split()
        if i==[]:
            pass
        elif i[0]=='DELETE':
            neiRong=neiRong.replace(i[1],'')
        elif i[0]=='SUBSTITUTE':
            neiRong=neiRong.replace(i[1],i[2])
    teli.close()
    subsText=open(outputfilename,'w')
    subsText.write(neiRong)
    subsText.close()

def devide():
    def generate_dic():
        dictionary = {}
        f = open("dic.txt","r")
        file = f.read()

        k = file.split('\n')
        for i in range(len(k)):
            j = k[i].split(' ')
            if len(k[i])>3 or len(j[0])>1:
                dictionary[j[0]] = dictionary.get(j[0],1)

        return(dictionary)

        f.close()

    def generate_rulelibrary():
        global rulelibrary
        rulelibrary = {}
        f = open("rule.txt","r")
        k = f.readlines()
        for i in k:
            rulelibrary[i] = rulelibrary.get(i,1)
        return(rulelibrary)

    def backward_search(a,dic,new_dic,l):
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

    def isalnum(ob):
        return ob in string.ascii_letters or ob in string.digits
    def engordigit(content):
        a = set(content)
        return all(map(isalnum,a))

    def check(a,head,tail,dic,new_dic):
        t = a[head:tail]
        if t in dic or t in new_dic or engordigit(t):
            return True
        else:
            return False

    def compare(divide1,divide2):

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
                prefixpoint = p1
                wrongcut= [divide1[p1]]
                while sum_len1!=sum_len2:
                    if sum_len1<sum_len2:
                        p1+=1
                        sum_len1 +=len(divide1[p1])
                        wrongcut.append(divide1[p1])
                    else:
                        p2+=1
                        sum_len2 += len(divide2[p2])
                suffixpoint = p1
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
        #main algorithm
        l = 5

#        specialcase(sentence)

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
    #main program
    file_c = inputs.get(1.0,END)
    generate_rulelibrary()
    outputs.delete(0.0,END)

    content = file_c
    for i in list(rulelibrary.keys()):
        i=i.split()
        if i==[]:
            pass
        elif i[0]=='DELETE':
            content=content.replace(i[1],'')
        elif i[0]=='SUBSTITUTE':
            content=content.replace(i[1],i[2])
    print(content)
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
# search new word from () and ""

    tempc = []
    for i in range(len(content)):
        if content[i]!= "\n" and content[i]!= " " and content[i]!= "　":
            tempc.append(content[i])
    content ="".join(tempc)

    divpunc = "，。！？；"
    part = []
    i = 0
    while i < len(content):
        if content[i] in divpunc:
            part.append(content[i])
            i += 1
        else:
            tempp = []
            while content[i] not in divpunc:
                tempp.append(content[i])
                i += 1
            p = "".join(tempp)
            part.append(p)

    while('' in part):
        part.remove('')

#divide word

    dic = generate_dic()
    no = 1
    for number in range(len(part)):
        if len(part[number])>1:
            tuple_ans = search(part[number],dic,new_dic)
            if part[number+1] in divpunc:
                 outputs.insert(END,"{0}. {1}".format(no,tuple_ans[1]))
            else:
                 outputs.insert(END,"{0}. {1}\n".format(no,tuple_ans[1]))
                 no +=1
        else:
             outputs.insert(END,"{0}\n".format(part[number]))
             no +=1
    teli=outputs.get(1.0,END)
    for i in list(rulelibrary.keys()):
        i=i.split()
        if i==[]:
            pass
        elif i[0]=='DELETE':
            teli=teli.replace(i[1],'')
        elif i[0]=='SUBSTITUTE':
            teli=teli.replace(i[1],i[2])
    outputs.delete(0.0,END)
    outputs.insert(1.0,teli)



def devidesentence():
    outputs.delete(0.0,END)
    sentenceSet=[]
    text=inputs.get(1.0,END)
    text=text.replace('\n','')
    text=text.replace('。”','.”\n')
    text=text.replace('？”','?”\n')
    text=text.replace('！”','!”\n')
    text=text.replace('。','。\n')
    text=text.replace('？','？\n')
    text=text.replace('!','！\n')
    text=text.replace('，','，\n')
    text=text.splitlines()
    for i in range(len(text)):
        sentence=str(i+1)+'.'+text[i]+'\n'
        sentenceSet=sentenceSet+[sentence]
        print(i)
    for i in sentenceSet:
        outputs.insert(END,i)




if __name__ == '__main__':
    main()
root=Tk()

menubar=Menu(root)
root.title('Chinese Segment Program')
generate_dic()
generate_rulelibrary()


filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label='Open files',font=('Comic Sans MS',),command=OpenFiles)
filemenu.add_command(label='Save files(inputs)',font=('Comic Sans MS',),command=Savefiles)
filemenu.add_command(label='Save files(outputs)',font=('Comic Sans MS',),command=Saveoutputfiles)
filemenu.add_command(label='Quit',font=('Comic Sans MS',),command=quit)
menubar.add_cascade(label='File',menu=filemenu)

segmentationmenu=Menu(menubar,tearoff=0)
segmentationmenu.add_command(label='Segment a text',font=('Comic Sans MS',),command=segmentAText)
menubar.add_cascade(label='Segmentation',menu=segmentationmenu)


lexiconmenu=Menu(menubar,tearoff=0)
lexiconmenu.add_command(label='Load the lexicon',font=('Comic Sans MS',),command=loadTheLexicon)
lexiconmenu.add_command(label='Add a new word',font=('Comic Sans MS',),command=addWords)
lexiconmenu.add_command(label='Modify a word',font=('Comic Sans MS',),command=modifyWords)
lexiconmenu.add_command(label='Delete a word',font=('Comic Sans MS',),command=deleteWords)
menubar.add_cascade(label='Lexicon',menu=lexiconmenu)

rulemenu=Menu(menubar,tearoff=0)
rulemenu.add_command(label='Load the rule library',font=('Comic Sans MS',),command=loadTheRuleLibrary)
rulemenu.add_command(label='Add a new rule',font=('Comic Sans MS',),command=addRules)
rulemenu.add_command(label='Modify a rule',font=('Comic Sans MS',),command=modifyRules)
menubar.add_cascade(label="Rule",menu=rulemenu)

bangzhumenu=Menu(menubar,tearoff=0)
bangzhumenu.add_command(label='Instructions',font=('Comic Sans MS',),command=instructionfunc)
bangzhumenu.add_command(label='Copyright',font=('Comic Sans MS',),command=copyrightfunc)
menubar.add_cascade(label='Help',menu=bangzhumenu)

root['menu']=menubar

labelInput=Label(root,text='Please input your text here(中文句子请加标点)',fg='dark green',font=('Comic Sans MS',),anchor='w')
labelInput.pack()



inputjiemian=Frame(height=300,width=400)
inputjiemian.pack()
inputs=Text(inputjiemian,height=20,width=50)
inputsgundongtiao=Scrollbar(inputjiemian)
inputsgundongtiao.pack(side=RIGHT,fill=Y)
inputs['yscrollcommand']=inputsgundongtiao.set
inputs.pack(side=RIGHT)
inputsgundongtiao['command']=inputs.yview




startseg=Button(inputjiemian,text='segment',command=devide,width=10,font=('Comic Sans MS',),relief='raised',height=4)
getsentences=Button(inputjiemian,text='get sentence',command=devidesentence,width=10,font=('Comic Sans MS',),relief='raised',height=4)
startseg.pack(anchor=W)
getsentences.pack()



labelOutput=Label(root,text='the result:',fg='dark green',anchor='w',font=('Comic Sans MS',))
labelOutput.pack()



outputjiemian=Frame(height=300,width=400)
outputs=Text(outputjiemian,height=20,width=50)
outputjiemian.pack()
outputsgundongtiao=Scrollbar(outputjiemian)
outputsgundongtiao.pack(side=RIGHT,fill=Y)
outputs['yscrollcommand']=outputsgundongtiao.set
outputsgundongtiao['command']=outputs.yview
outputs.pack(side=RIGHT)
clean2=Button(outputjiemian,text='clean',command=cleanTheText2,font=('Comic Sans MS',),width=10,height=6)
clean2.pack(anchor=W)



cv=Canvas(root,width=400,height=90)
img=PhotoImage(file='xiaohui.gif')
cv.create_image((200,40),image=img)
cv.pack()


root.mainloop()
