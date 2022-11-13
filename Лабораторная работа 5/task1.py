from pprint import pprint

num_amount = 16
pprint([{'bin': bin(num), 'dec': num, 'oct': oct(num), 'hex': hex(num)} for num in range(num_amount)])
