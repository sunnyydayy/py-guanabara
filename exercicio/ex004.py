var1 = input('Digite algo:')

print('O tipo e?', type(var1))
print('So tem espacos?', var1.isspace())
print('E um numero?', var1.isnumeric())
print('E alfabetico?', var1.isalpha())
print('E alfanumerico?', var1.isalnum())
print('Esta em maiuscula?', var1.isupper())
print('Esta em minuscula?', var1.islower())
print('Esta capitalizada?', var1.istitle())