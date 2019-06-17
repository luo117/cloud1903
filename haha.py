
pen("./test.txt", "w")
f.write('''this is my first line.
that is my second line.
that my third line.''')
f.close()

# # file文件的读取01.
# file = open("./test.txt", "r")
# txt = file.read(10)
# print(txt)
# file.close()

# file文件的读取02.
# file = open("./test.txt", "r")
# for line in file:
#     print(line)
# file.close()

# file文件读取03.
file = open("./test.txt", "r")
txt = file.readlines()
for i in range(len(txt)):
    print(txt[i])
file.close()

# file文件写入(追加).
file = open("./test.txt", "a")
file.write("\n4444444444444444\n")
file.close()

file = open("./test.txt", "a")
file.writelines('''this 55555
this 66666
this 77777
''')
file.writelines("this 88888")
file.close()

file = open("./test.txt", "a")
file.writelines("\nthis 88888")
file.close()
