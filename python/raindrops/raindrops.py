def convert(number):
    l = []
    d = { '3': 'Pling', '5':'Plang', '7':'Plong' }
    for num in d:
        if number % int(num) == 0:
            l.append(d[num])           
    if not l:
        l.append(str(number))
    return "".join(map(str,l))
    
