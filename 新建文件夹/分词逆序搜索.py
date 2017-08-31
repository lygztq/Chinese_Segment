#-------------------------------------------------------------------------------
# Name:        妯″潡1
# Purpose:
#
# Author:      haoyun
#
# Created:     18/11/2015
# Copyright:   (c) haoyun 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def generate_dic():
    dictionary = {}
    f = open("dictionary.txt","r")
    file = f.read()
    k = file.split(' ')
    for i in k:
        dictionary[i] = dictionary.get(i,1)
    return(dictionary)


def backward_search(a,dic,l):
    point_tail = len(a)
    point_head = point_tail - l
    ans = []
    while point_tail >0 :
        while not(point_tail <= point_head +1 or check(a,point_head,point_tail,dic)):
            point_head += 1
        ans.append(a[point_head:point_tail])

        point_tail = point_head
        point_head = max(point_tail - l,0)
    return (ans)

def forward_search(a,dic,l):
    point_tail = 0
    point_head = point_tail + l
    ans = []
    while point_tail < len(a) :
        while not(point_head <= point_tail +1 or check(a,point_tail,point_head,dic)):
            point_head -= 1
        ans.append(a[point_tail:point_head])

        point_tail = point_head
        point_head = min(point_tail + l,len(a))
    return (ans)

def check(a,head,tail,dic):
    t = a[head:tail]
    if t in dic:
        return True
    else:
        return False

def main():
    dic = generate_dic()
    l = 3

    readfile = open("reading.txt","r")
    file = readfile.read()
    readfile.close()

    divide1 = backward_search(file,dic,l)
    divide1 = divide1[::-1]
    ans1 = "|".join(divide1)

    divide2 = forward_search(file,dic,l)
    ans2 = "|".join(divide2)

    writefile = open("writing.txt","w")
    writefile.write("{0}\n{1}".format(ans1,ans2))
    writefile.close()

main()






