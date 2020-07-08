import pandas as pd
import re
import os
text = pd.read_csv('task_5_final.csv')
ip=text['IP']
sc=text['Status_code']
a=[]
x=0
for i in sc:
    if(i!=200):
        a.append(x)
    x+=1
z=[]
for i in a:
    z.append(ip[i])
y=set(z)
y=str(y)
y=y.replace(",","\n")
y=y.replace("["," ")
y=y.replace("]"," ")
y=y.replace("set("," ")
y=y.replace(")"," ")

file=open("final.txt","a")
file.write(y)
file.close()
file=open("final.txt","r")
os.system("rm final.txt")
file3=open("final.txt","a")
for line in file:
	ip=re.findall(r'[0-9]+(?:\.[0-9]+){3}',line)
	ip=str(ip)
	ip=ip.replace("["," ")
	ip=ip.replace("]"," ")
	ip=ip.replace("'"," ")
	print(ip)
	file3.write(ip)
	file3.write("\n")

file.close()

