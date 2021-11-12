arquivo = open('info.txt')
print(type(arquivo))

print(arquivo.read())
print(arquivo.read())

arquivo.seek(0)
print(arquivo.read())

arquivo.close()