def numeros_repetidos(list):
    cuenta = {}
    for elem in list:
        if elem in cuenta.keys():
            cuenta[elem] += 1
        else:
            cuenta[elem] = 1
    return cuenta