
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







