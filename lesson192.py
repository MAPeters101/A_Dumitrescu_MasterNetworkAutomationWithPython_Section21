first_name = 'John'
last_name = 'Smith'
age = 40
#print('Hello ' + first_name + ' ' + last_name + '! You are ' + age + ' years old.')
print('Hello ' + first_name + ' ' + last_name + '! You are ' + str(age) + ' years old.')

print(f'Hello {first_name} {last_name}! You are {age} years old!')
print(F'Hello {first_name} {last_name}! You are {age} years old!')
print()

s = f'{2.3 * 4.2 / 5.1}'
print(s)

s = f'{2.3 * 4.2 / 5.1:.4f}'
print(s)

celsius = 15.4
print(f'{celsius} degrees Celsius = {celsius * 1.8 + 32} degrees Fahrenheit.')



