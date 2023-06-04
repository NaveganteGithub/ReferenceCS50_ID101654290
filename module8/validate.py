import re
'''
    Validaciones con expresiones regulares

    Recordemos que las expresiones regulares son patrones de caracteres

    . significa cualquier caracter excepto los saltos de linea o una linea en blanco
    * significa que puede haber de 0 a n caracteres
    + significa que puede haber de 1 a n caracteres
    ? significa que puede haber de 0 a 1 caracteres
    \ hace que cualquier caracter con significado en las expresiones regulares sean
      interpretados como un string, pero eso si con la expresion r de regular expresion
      si no pusieramos la r este simbolo significa nueva linea o que hay un salto de linea
    {m} significa que puede haber m numero de caracteres
    {m,n} significa que puede haber m a n numero de caracteres
    ^ indica que el patron de caracteres tiene que estar al principio de la cadena
    $ indica que el patron de caracteres tiene que estar al final de la cadena
    [] conjunto de caracteres permitidos
        [abcdefgh]
    [^] conjunto de caracteres no permitidos
        [^abcdefgh]
    []+ conjunto de caracteres permitidos, y tienen que ser de 1 a n
    \w es el conocido caracter de palabra que equivale a [a-zA-Z0-9_]

    La expresion r sirve para indicar al interprete que la cadena de texto debe ser
    interpretada como una expresion regular y no como una cadena de texto literal
        r".+@.+\.edu"


'''
email = input("What´s your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


'''if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")'''


'''if re.search(r".{1}.*@.*", email):
    print("Valid")
else:
    print("Invalid")'''

'''if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")'''

'''if re.search(r"^[abcdefgh]+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")'''

'''if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")'''

'''if re.search(r".+@.+\.edu", email): # La expresion r sirve para indicar que un texto es una expresion regular
    print("Valid")
else:
    print("Invalid")'''

'''if re.search("..*@.*", email):
    print("Valid")
else:
    print("Invalid")'''

'''if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")'''

'''if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")'''

'''
search es una funcion del modulo re que permite
examinar expresiones regulares o patrones

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

'''

# Validaciones sin Expresiones regulares

# email = input("What´s your email? ").strip()

'''username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")'''

'''
Una variable en un if sera examinada para si tiene algun valor,
lo que dara True, y si no lo tiene entonces el resultado sera
False

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")
'''

'''
in es una palabra clave que examina una cadena de texto
para ver si contiene cierto caracter o cierto conjunto
de caracteres

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
'''
