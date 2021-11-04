var_w = open('file.txt', 'a+')
var_r = open('file.txt', 'r')

def create(name, value):
    if ' ' in name:
        print(ValueError("SPACES"))
        exit()
    elif name in var_r.read():
        print(ValueError("THE_VARIEBLE_ARLEADY_EXISTS"))
        exit()
    var_w.write(f'{name} {value} \n')

def find(input):
    for varieb in var_r:
        d = varieb.split(' ')
        if d[0] == input:
            return d[1]
    if find(input) == None:
        print(ValueError("THE_VARIEBLE_DOES_NOT_EXIST"))
        exit()

def add(name, how_much):
    for varieb in var_r:
        d = varieb.split(' ')
        if d[0] == name:
            



add('abecadlo_z_pieca_spadlo' , '123')
