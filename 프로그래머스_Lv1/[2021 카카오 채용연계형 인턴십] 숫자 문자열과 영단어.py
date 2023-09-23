def solution(s):
    word={"nine":"9","eight":"8","seven":"7","six":"6","five":"5","four":"4","three":"3","two":"2","one":"1","zero":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0"}
    sentense=""
    answer=""
    for i in s:
        sentense+=i
        if sentense in word:
            answer+=word.get(sentense)
            sentense=""
    
    
    answer=int(answer)
    return answer
