#!/usr/bin/python3

def decimal_to_base(nb, base) :
    
    base_size = len(base)
    nb = int(nb)
    
    whole = nb // base_size
    output = str(nb % base_size)
    while whole >= base_size :
        output = str(base[whole % base_size]) + output
        whole = whole // base_size
    
    output = str(whole) + output
        
    return output
    
   
def get_lookup_table(base) :
    
    table = {}
    
    for i in range( len(base) ) :
        table.update( { base[i] : i } )
        
    return table
   
   
def to_base_of_10(number, base) :
    
    base_size = len(base)
    table = get_lookup_table(base)
    
    output = 0
    n = len(number)
    
    for i in range(n) :
        output += table[ number[i] ] * pow(base_size, n - i - 1)
    
    return output


def itoBase(nb, base_1, base_2 = None) :
    
    if base_1 and base_2 :
        nb = to_base_of_10(nb, base_1)
        return decimal_to_base(nb, base_2)
    elif base_1 :
        return decimal_to_base(nb, base_1)
    else :
        return
