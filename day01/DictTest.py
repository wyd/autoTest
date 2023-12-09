my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# print(my_dict)
# print(my_dict['key1'])
# for i in my_dict:
#     # print(i+':'+my_dict[i])
#     print(i+':'+my_dict.get(i))
# my_dict['key1']='value10'
# print(my_dict)
for key, value in my_dict.items():
    print("Key:", key, "Value:", value)