__author__ = "chuhaoyun"
import HMM.prob_emit,HMM.prob_trans,HMM.prob_start
import string
import math

minnum = -3.14e100
status = ("b","m","e","s")
prestatus = {"b":("s","e"),"m":("m","b"),"e":("b","m"),"s":("e","s")}

start_P, trans_P, emit_P = {},{},{}
def init_P():
    global start_P,trans_P,emit_P
    start_P = HMM.prob_start.P
    trans_P = HMM.prob_trans.P
    emit_P = HMM.prob_emit.P
#读取参数矩阵

def cutbyhmm(content):
    init_P()
    words = []
    weight,path = viterbi(content)
    word = ""
    for i in range(len(content)):
        sym = path[i]
        if sym == "e":
            word = word + content[i]
            words.append(word)
            word = ""
        elif sym == "m" or sym == "b":
            word = word + content[i]
        elif sym == "s":
            words.append(content[i])
    return words
#切分算法

def viterbi(sentence):
    global start_P,trans_P,emit_P
    w = [{}]
    path = [{}]
    for s in status:
        w[0][s] = start_P[s] + emit_P[s].get(sentence[0],minnum)
        path[0][s] = [s]
    for i in range(1,len(sentence)):
        char = sentence[i]
        w.append({})
        newpath = {}
        for s in status:
            emit = emit_P[s].get(char,minnum)
            prob_max = minnum
            status_max = prestatus[s][0]
            for prest in prestatus[s]:
                a = trans_P[prest][s]
                x = w[i-1][prest]
                prob = emit + trans_P[prest][s] + w[i-1][prest]
                if prob>prob_max:
                    prob_max = prob
                    status_max = prest
            w[i][s]= prob_max
            newpath[s] = path[i-1][status_max] + [s]
        path.append(newpath)

    final_prob = minnum
    final_status = "e"
    for fs in ("e","s"):
         p = w[len(sentence)-1][fs]
         if p > final_prob:
            final_prob = p
            final_status = fs
    return(final_prob,path[len(sentence)-1][final_status])
#维特比算法

def cutUnrecognized(content):
    init_P()
    return cutbyhmm(content)




