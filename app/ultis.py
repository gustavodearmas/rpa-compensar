strr = 'idDeporte=544&idCiclo=26554&idSede=2&start=0&limit=100'

def conver_to_dict(_str_):
    r = _str_.split("&")
    dicto = {}
    for i in range(0, len(r)):
        f = r[i].split("=")
        dicto[f[0]] = f[1]
    return dicto

print(conver_to_dict(strr))
