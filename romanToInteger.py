ro_vals = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D':500,'M': 1000}
ro_vals_ex = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
extra = ['I','X','C']
extra_1 = ['V','X','L','C','D','M']
def romanToInteger(n):
     num_list = [str(x) for x in n.split(',')]
     value = 0
     for i in num_list:
         rom = num_list(i)
         if( i in ro_vals):
             if(i in extra):
                 key = i + 1
                 if(num_list(key) in extra_1):
                     rom = rom + num_list(key)
                     if(rom in ro_vals_ex):
                         value = value + ro_vals_ex[rom]
             else:
                 value = value + ro_vals[i]
     return value
            
         
     
