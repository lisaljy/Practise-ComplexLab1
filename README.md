# Practise-ComplexLab1  
### 利用知识：  
* Random函数  
```python
import random
random.shuffle（list）  将一个列表中的元素打乱
random.choice （list） 从序列中获取一个随机元素
random.sample （range/list，长度）从指定序列中随机获取指定长度的片断
```
[参考](http://www.cnblogs.com/yd1227/archive/2011/03/18/1988015.html)  
注意编写程序时利用shuffle和sample的效率问题  
随机数的生成若时间相隔较大，可忽略随机重复的问题

* List操作方法
```python
访问列表中的特定对象 list[i]
在列表末尾添加新的元素 list.append(obj) 
列表中元素的计算 len(list)
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值list.pop()
```  
[参考](http://www.jb51.net/article/47978.htm)

* split分组函数
```python
L='spam,asa,sdfs'
L.split(',')
```  
默认分隔符为空格

* 读文件的技巧
```python
for line in f.readlines():  
    print(line.strip()) # 把末尾的'\n'删掉
```  
作用：读取全部数据，分行显示，并去掉末尾的\n
```python
with open('/path/to/file', 'r') as f:
    print f.read()
```  
作用：自动调用f.close()

### 代码：
# 提取数据，分割数据，随机提取，交换连边，写入新文档
# 交换随机位置比交换随机对象方便


