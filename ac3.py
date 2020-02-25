import math

n = float(input())
cinco = (n/(5.4*7))
vinte = (n/(24*7))

final = (math.floor((n/(24*7))) * 91.00) + (math.ceil((n%(24*7))/(5.4*7)) * 23.00)

print("a)" ,math.ceil(vinte) ,"lata(s) de 24 litros: R$ {0:.2f}".format(math.ceil(vinte)*91.00))

print("b)" ,math.ceil(cinco) ,"lata(s) de 5.4 litros: R$ {0:.2f}".format(math.ceil(cinco)*23.00))

print("c)" ,math.floor((n/(24*7))) ,"lata(s) de 24 litros e" ,math.ceil((n%(24*7))/(5.4*7)) ,"lata(s) de 5.4 litros: R$ {0:.2f}".format(final))