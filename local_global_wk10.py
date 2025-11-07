g_var = 3 #global variable


def print_local_global():
    '''This shows how to uselocal variables vs global variables'''
    l_var =3 #local variable
    global inside_global
    inside_global = 4
    print(g_var)
    print(l_var)
   
print_local_global()
print(print_local_global.__doc__)
print(g_var)
#print(l_var) error
print(inside_global)



print()


def celc_2_hr(celcius):
    F = (9/5)*celcius+32
    return F

print(celc_2_hr(25))
    
