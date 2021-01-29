var_w = open('file.txt', 'a+')
var_r = open('file.txt', 'r')

def create(name, value):
    if ' ' in name:
        print(ValueError("sadly we do not allow spaces in the names of variebles"))
        exit()
    elif name in var_r.read():
        print(ValueError("the name of varieble you are trying to create alleady exists "))
        exit()
    var_w.write(f'{name} {value} \n')

def find(input):
    for varieb in var_r:
        d = varieb.split(' ')
        if d[0] == input:
            return d[1]
    if find(input) == None:
        print(ValueError("the varieble you specified does not exist"))
        exit()

def add(name, how_much):
    for varieb in var_r:
        d = varieb.split(' ')
        if d[0] == name:
            



add('abecadlo_z_pieca_spadlo' , '123')
