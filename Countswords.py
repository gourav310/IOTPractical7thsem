# name - Gourav khurana 
# Roll no - 17EEBCS028
# Iot lab Examination 
# Date- 19 Feb 2021 

def count_words(string):
    string1=string.strip()
    count=1
    for i in string1:
        if i==" ":
            count+=1
     
    return count
filepath = 'd:/PycharmProjects/College IOT/filee.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       n=count_words(line)
       print("Line {}: {}".format(cnt, line.strip()))
       print("No of words :",n)
       line = fp.readline()
       cnt += 1

