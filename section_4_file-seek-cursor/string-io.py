from io import StringIO

arquivo_em_memoria = StringIO()

arquivo_em_memoria.write('Learning StringIO, writing in memory')
arquivo_em_memoria.seek(0)

string_out = arquivo_em_memoria.read()

disk_file = open('test.txt', 'w')
disk_file.write(string_out)
disk_file.close()
