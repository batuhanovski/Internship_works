#!/usr/bin/env python
# coding: utf-8

# In[404]:


import os
os.chdir('E:\Cmpe\Ie310\HW2')
data = open('Data6.txt')


# In[405]:


lines=data.readlines()


# In[406]:


n=int(lines[0][:-1])


# In[407]:


glines=[]
glines2=[]
B = []
A = []
C = []
D = []


# In[408]:


for line in lines:
    if line[-1:] != '\n':
        glines.append(line)
    else:    
        glines.append(line[:-1])
for gline in glines:
    glines2.append(gline.split())


# In[409]:


for i in range(1,n+1):
    B.append(float(glines2[i][n]))
for i in range(1,n+1):
    A.append(glines2[i][:-1])
for i in range(0,n):
    for j in range(0,n):
        A[i][j]=float(A[i][j])    


# In[410]:


for i in range(n):
    for j in range(n):
        C.append(A[j][i])
    D.append(list(C))
    C = []


# In[411]:


D=A


# In[412]:


I=[]
row=[]
for i in range (n):
    for j in range (n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    I.append(row)
    row=[]


# In[413]:


def matrixOrganizer():           #2 den fazla 0 olma case'inde çalışmıyor.
    for i in range(n-1):
        if D[i][i]==0:
            for j in range(i+1,n):
                if D[j][i]!=0:
                    temp=D[i]
                    D[i]=D[j]
                    D[j]=temp
                    temp=B[i]
                    B[i]=B[j]
                    B[j]=temp
                    temp=I[i]
                    I[i]=I[j]
                    I[j]=temp


# In[414]:


matrixOrganizer()


# In[415]:


def exchangeRows(first,second):
    temp=D[first]
    D[first]=D[second]
    D[second]=temp
    temp = B[first]
    B[first]=B[second]
    B[second]=temp
    temp=I[first]
    I[first]=I[second]
    I[second]=temp


# In[416]:


def multipleRow(const,rownum):
    for i in range(n):
        D[rownum][i]=round(const*D[rownum][i],5)
        I[rownum][i]=round(const*I[rownum][i],5)
    B[rownum]=round(B[rownum]*const,5)    


# In[417]:


def addmultofRows(multiple,source,dest):
    temp=[]
    tempI=[]
    for i in range(n):
        temp.append(multiple*D[source][i])      
        tempI.append(multiple*I[source][i])
    for i in range(n):    
        D[dest][i]=round(D[dest][i]+temp[i],3)
        I[dest][i]=round(I[dest][i]+tempI[i],3)
    B[dest]=round(multiple*B[source]+B[dest],3)


# In[418]:


def echelonMatrix():
    try:
        for i in range(n):
            matrixOrganizer()
            multipleRow(1/D[i][i],i)
            for j in range(i+1,n):
                addmultofRows(-D[j][i],i,j)
    except ZeroDivisionError:
        if B[n-1]==0: #burda olmayan bi case olabilir
            return 1
        else:
            return 2
    else: return 0


# In[420]:


zeroRow=[]
for i in range(n):
    zeroRow.append(float(0))
zeroRow


# In[433]:


countzeroRow=0
for i in range(n):
    if D[i]==zeroRow:
        countzeroRow=countzeroRow+1


# In[435]:


check=echelonMatrix()


# In[437]:


def findSolution():
    if check == 0:
        for i in range (n):
            matrixOrganizer()
            for j in range(i+1,n):
                addmultofRows(-D[n-1-j][n-1-i],n-1-i,n-1-j)
    elif check == 1:
        for i in range(n):
            matrixOrganizer()
            if D[n-1-i][n-1-i]==0:
                for j in range(i+1,n):
                    addmultofRows(-D[n-2-j][n-2-i],n-2-i,n-2-j)


# In[438]:


findSolution()


# In[444]:


if check == 2:
    print('Inconsistent problem')
elif check == 1:
    print('Arbitrary values: ',end=' ')  
    for i in range(countzeroRow+1):
        print(0.0,end=' ')
    print()    
    print('Arbitrary Solution: ',end=' ') 
    for i in range(n):
        print(B[i],end=' ')
else:
    print('Unique Solution: ',end=' ')
    for i in range(n):
        print(B[i],end=' ')
    print()    
    print('Inverted A:', end=' ')
    for i in range(n):
        print()
        for j in range(n):
            print(I[i][j], end=' ')


# In[ ]:





# In[ ]:





# In[428]:


def rankFinder():
    for i in range(n):
        for j in range(n):
            if D[i]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




