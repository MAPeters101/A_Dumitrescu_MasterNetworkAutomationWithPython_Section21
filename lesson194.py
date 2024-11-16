
my_str = 'I learn Python Programming.'

print(my_str.upper())
print(my_str)
print(my_str.lower())
print(my_str)

ip = '  192.168.0.1    '
print(ip)
print(ip.strip())
ip = ip.strip()
print(ip)
print()

value = '$$200$$$$'
print(value.strip('$'))
print()

new_value = value.replace('$', '@')
print(new_value)

txt = 'I learn Python, Python is cool!'
n = txt.count('Python')
print(n)

txt = 'I learn PytHon, pythoN is cool!'
n = txt.count('Python')
print(n)

txt = 'I learn PytHon, pythoN is cool!'
n = txt.lower().count('Python')
print(n)

txt = 'I learn PytHon, pythoN is cool!'
n = txt.lower().count('python')
print(n)

print(txt.count('y'))
print()

my_list = txt.split()
print(my_list)

txt = 'I le arn PytH    on, pythoN is c\nool!'
n = txt.lower().count('python')
print(n)

my_list = txt.split()
print(my_list)
print()

print('10.1.2.3'.split('.'))
print()

ip = '10.1.2.3'
ip_list = ip.split('.')
print(ip_list)

ip_str = '.'.join(ip_list)
print(ip_str)

ip_str = ','.join(ip_list)
print(ip_str)

ip_str = '-'.join(ip_list)
print(ip_str)

ip_str = 'xxxxxx'.join(ip_list)
print(ip_str)
print()

my_str = 'I learn Python Programming.'
print(my_str.find('Python'))
print(my_str.find('Pyxthon'))
print('Python' in my_str)
print('Golang' in my_str)
print()

print('Python' not in my_str)
print('Golang' not in my_str)
print()



