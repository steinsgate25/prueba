# input() en python3, toma la entrada del usuario y retorna siempre un string; si queremos realizar alguna operacion con otro tipo de dato saltara ERROR.
# input en pytho3 es == a raw_input en python2
# en python2 input, evalua cualquier tipo de codigo de python y lo procesa.
#input en python2 == a eval(), es condigo se usa asi 'eval(input())'

print ("Cuantos años tienes?"),
edad = input()
print("Que tan alto eres?"),
altura = input()
print ("Cual es tu peso?"),
peso = input()

print ("Entonces, tu tienes %r años, mides %r y pesas %r." % (edad, altura, peso))
