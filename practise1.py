#导入random函数
import random 
#打开文件，读取模式                      
a = open(r'c:\data.txt','r')
#逐行读取                
content = a.readlines()                   
c1=[]
c2=[]
for line in content:
   #去掉每个对象末尾的\n，并换行返回
   group=line.strip()
   #以’|’为标志，逐行分组
   list = group.split('|')                
   c1.append(list[0])
   #分别将每组的第一，第二个对象插入两个新列表中
   c2.append(list[1])                 
#计算列表长度
x = len(c2)                         
i=0
#当随机进行三倍于列表长度时，可保证不出现重复
while i < x*3:
     #随机取位置信息
    lin_list = random.sample(range(0,x-1),2)     
    t = c2[lin_list[0]]
    c2[lin_list[0]] = c2[lin_list[1]]
   #交换列表c2中随机取的两个位置的对象的位置
    c2[lin_list[1]] = t                   
    i = i+1
i=0
#打开文件，写入模式
b = open(r'c:\data.test','w')         
while i < x:
    b.writelines(c1.pop(0)+','+c2.pop(0)+'\n')   
    i = i+1
a.close()
b.close()
