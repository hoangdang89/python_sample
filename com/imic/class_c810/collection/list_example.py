#reverse list in new list without use reverse method

def REVERSE(k):
    s=[]
    for i in range(len(k)-1,-1,-1):
        s.append(k[i])
    return s
    
    
h=[10,20,'c',2,'a']
print(REVERSE(h))


danh_sach.insert(3, 'a')