"""
Curso Python 
"""

def contar_caracteres(string):
    """Função que retorna a quantidade de caracteres
        presentes na string que recebeu.
        Data 09/05/2020 BAPDS
        >>> contar_carcteres('Bruno')
        {'b': 1, 'r': 1, 'u': 1, 'n': 1, 'o': 1}

        >>> contar_carcteres('abacate')
        {'a': 3, 'b': 1, 'c': 1, 't': 1, 'e': 1}

        :param string: string a ser contada
    """
    resultado = {}

    for letra in string.lower():
        contagem = resultado.get(letra, 0)
        contagem += 1
        resultado[letra] = contagem

    return resultado


if __name__ == "__main__":
    
    println(contar_caracteres('Bruno'))
    print()
    print(contar_caracteres('abacate'))
    print()
    print(contar_caracteres('banana'))
    print()
    print(contar_caracteres('BANANA'))
    print()
    print(contar_caracteres('pROPAROXÍTONA'))
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
    """