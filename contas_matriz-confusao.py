#https://medium.com/@mateuspdua/machine-learning-m%C3%A9tricas-de-avalia%C3%A7%C3%A3o-acur%C3%A1cia-precis%C3%A3o-e-recall-d44c72307959
# calculo de matriz de confusão

#acurácia é a quantidade de acertos do nosso modelo divido pelo total da amostra.

def acuracia (vp,vn,fp,fn):
    return (vp + vn) / (vp + vn+ fp + fn)

#precisão

def precisao (vp,vn,fp,fn):
    return vp / (vp + fp)

#revocação

def revocacao (vp,vn,fp,fn):
    return vp / (vp + fn)

#f1 score

def f1score (vp,vn,fp,fn):
    return 2 * ((precisao * revocacao)/(precisao + revocacao))

print(acuracia(25,40,10,25))
