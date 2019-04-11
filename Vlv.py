list = [ 100, 200, 500, 0, 9, 600]

def mx(list):
    m = list[0]
    mi = list[0]
    for i in list:   
        if i > m:
            m = i
        if i < mi:
            mi = i
    return m + mi
            
print(mx(list))