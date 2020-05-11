"""
Somente um teste
"""


def tratment_string(entrada):
    ex = "!.,;:?"
    newtext = ''
    for caracter in entrada:
        for compare in ex:
            if caracter == compare:
                ok = False
                break
            ok = True
        if ok:
            newtext += caracter
    return newtext.lower()


print(tratment_string(input()))
