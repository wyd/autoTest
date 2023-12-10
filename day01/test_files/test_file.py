f = open('C:\python_workspace\PycharmProjects\pythonProject\day01\\test_files\\test_data.txt',
         "r", encoding='utf-8')
list_a = f.readlines()
print(list_a)
for s in list_a:
    print(s.format())
f.close()
