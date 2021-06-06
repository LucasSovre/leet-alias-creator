# -*- coding: utf-8 -*-
file= open('modifiedBadWordList1.txt' , "r", encoding='utf8')
liste = []
variant =[]
ligne= file.readlines()

#here we got the text and spread all words in a list
for line in ligne : 
    liste.extend(line.split(","))

#we take the list and itere changments on each list's item
for item in liste : 
   
    #prevent from leetspeak :
    #replace a by 4, @ and ∂:
    c=item.replace('a','4')
    if item != c :
        variant.append(c)
    d=item.replace('a','@')
    if item != d:
        variant.append(d)
    e=item.replace('a','∂')
    if item != e :
        variant.append(e)
    #replace B by 8 or ß
    f=item.replace('b','8')
    if item != f :
        variant.append(f)
    g=item.replace('b','ß')
    if item != g :
        variant.append(g)
    #replace c by ¢ or ©
    h=item.replace('c','¢')
    if item != h :
        variant.append(h)
    i=item.replace('c','©')
    if item != i :
        variant.append(i)
    #replace E by 3, € or ë
    j=item.replace('e','3')
    if item != j :
        variant.append(j)
    k=item.replace('e','€')
    if item != k:
        variant.append(k)
    l=item.replace('e',"ë")
    if item != l:
        variant.append(l)
    #replace f by ƒ
    m=item.replace('f','ƒ')
    if item != m :
        variant.append(m)
    #replace h by #
    n=item.replace('h','#')
    if item != n:
        variant.append(n)
    #replace i by [, ], |, !
    o=item.replace('i','[')
    if item != o:
        variant.append(o)
    p=item.replace('i',']')
    if item != p:
        variant.append(p)
    q= item.replace('i','|')
    if item != q:
        variant.append(q)
    r= item.replace('i','|')
    if item != r:
        variant.append(r)
    #replace j by ʝ
    s= item.replace('j','ʝ')
    if item != s:
        variant.append(s)
    #replace k by X and ɮ
    t= item.replace('k','X')
    if item != t:
        variant.append(t)
    u= item.replace('k','ɮ')
    if item != u:
        variant.append(u)
    #replace l by 1, £, ℓ
    r= item.replace('l','1')
    if item != r :
        variant.append(r)
    s=item.replace('l','£')
    if item != s :
        variant.append(s)
    t= item.replace('l','ℓ')
    if item != t :
        variant.append(t)
    #replace o by 0 
    u=item.replace('o','0')
    if item != u :
        variant.append(u)
    #replace p by 9 and ?
    v=item.replace('p','9')
    if item != v :
        variant.append(v)
    w=item.replace('p','?')
    if item != w :
        variant.append(w)
    #replace R by ® ,Я
    x=item.replace('r','®')
    if item != x :
        variant.append(x)
    y=item.replace('r','Я')
    if item != y :
        variant.append(y)
    #replace s by 5,$,z,§
    z=item.replace('s','5')
    if item != z :
        variant.append(z)
    a1=item.replace('s','$')
    if item != a1 :
        variant.append(a1)
    a2=item.replace('s','z')
    if item != a2 :
        variant.append(a2)
    a3=item.replace('s','§')
    if item != a3 :
        variant.append(a3)
    #replace t by 7
    a4=item.replace('t','7')
    if item != a4 :
        variant.append(a4)
    #replace v by u and µ
    a5=item.replace('v','u')
    if item != a5 :
        variant.append(a5)
    a6=item.replace('v','µ')
    if item != a6 :
        variant.append(a6)
    #replace w by vv, ɰ 
    a7=item.replace('w','vv')
    if item != a7 :
        variant.append(a7)
    a8=item.replace('w','ɰ')
    if item != a8 :
        variant.append(a8)
    #replace x by Ж,×
    a9=item.replace('x','Ж')
    if item != a9 :
        variant.append(a9)
    b1=item.replace('x','×')
    if item != b1:
        variant.append(b1)
    #replace y by Ψ ,¥, Ч
    b2=item.replace('y','Ψ')
    if item != b2 :
        variant.append(b2)
    b3=item.replace('y','Ч')
    if item != b3 :
        variant.append(b3)
    b4=item.replace('y','¥')
    if item != b4 :
        variant.append(b4)
    #replace z by 2,%
    b5=item.replace('z','2')
    if item != b5:
        variant.append(b5)
    b6=item.replace('z','%')
    if item != b6 :
        variant.append(b6)
for item in liste :
    if item.endswith("s") == False:
        a=item+'s'
        variant.append(a)
liste.extend(variant)
file.close()
modifiedFile= open('modifiedBadWordList2.txt','w',encoding='utf8')
mylist = list(dict.fromkeys(liste))
listestr=','.join(mylist)
modifiedFile.write(listestr)
modifiedFile.close()