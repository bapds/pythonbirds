"""
Curso Python 
"""

def contar_caracteres(string):
    """Função que retorna a quantidade de caracteres
        presentes na string que recebeu.
        Data 09/05/2020 BAPDS
        >>> contar_carcteres('Bruno')
        {b:1
        n:1
        o:1
        r:1
        u:1
        >>> contar_carcteres('abacate')
        a:3
        b:1
        c:1
        e:1
        t:1

        :param string: string a ser contada
    """
    ordenar_caracteres = sorted(string.lower())

    caracter_anterior = ordenar_caracteres[0]
    contagem = 1
    resultado = {}

    for letra in ordenar_caracteres[1:]:
        if letra == caracter_anterior:
            contagem +=1
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = letra
            contagem = 1     
    resultado[caracter_anterior] = contagem
    return resultado

if __name__ == "__main__":
    """
    contar_caracteres('Bruno')
    print()
    contar_caracteres('abacate')
    print()
    contar_caracteres('banana')
    print()
    contar_caracteres('BANANA')
    print()
    contar_caracteres('pROPAROXÍTONA')
    """
    palavras = open('/home/bapds/Documents/Curso Python Pro/palavras/palavras.txt', 'r')
    palavras_contadas = open('/home/bapds/Documents/Curso Python Pro/palavras/palavras_contadas.txt', 'w')
    indice = 0
    for palavra in palavras:
        indice += 1
        print(f'{palavra} - {indice}')
        palavras_contadas.writelines(f'{palavra} - {indice}')

        print(contar_caracteres(palavra))
        palavras_contadas.writelines(f'{contar_caracteres(palavra)}')
        print()

    palavras.close()
    palavras_contadas.close()