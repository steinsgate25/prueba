my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74.753456 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print ('{0:_^25}' .format('Buenos dias!'))
print ('Mi nombre es {}, tengo {} años y me gusta Python!' .format(my_age, my_name))
print ("Let's talk about {0}." .format(my_name))
print ("He's {0:.2f}% inches tall." .format(my_height))
print ("He's {0} pounds heavy." .format(my_weight))
print ("Actually that's not too heavy.")
print ("He's got {0} eyes and {1} hair." .format(my_eyes, my_hair))
print ("His teeth are usually {my_teeth} depending on the cofee." .format(my_teeth = 'White xD'))
print ("Eso seria todo por el momento {name}, les recomiendo que lean {book}" .format(name = 'chicos', book = "'A Byte of Python'"))
#print ('{0} was {1} years old when he wrote this book' .format(my_name, my_age))
#print ('Why is {0} playing whith that python?' .format(my_name))
