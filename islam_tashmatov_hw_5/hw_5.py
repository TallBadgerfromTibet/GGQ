import re

file_path4 = 'MOCK_DATA.txt'
result_file_path4 = '../islam_tashmatov_hw_5/name.txt'
file_reader4 = open(file_path4, mode="r", encoding="Latin-1")
final_result4 = open(result_file_path4, mode="w", encoding="Latin-1")

text = file_reader4.read()

s4 = r"[A-Z]+[A-z]+\w+\s+[A-z]+[a-z]+\w+|[A-Z]+[A-z]+\w+\s+[A-Z][']\s+[A-z]+[a-z]+\w+"
results_all = re.findall(s4, text)

for item in results_all:
    final_result4.write(item+'\n')
    print(f"total:{str(len(results_all))}")

file_path3 = 'MOCK_DATA.txt'
result_file_path3 = '../islam_tashmatov_hw_5/mail.txt'

file_reader3 = open(file_path3, mode='r', encoding="UTF-8")
final_results3 = open(result_file_path3, mode='w', encoding="UTF-8")

text3 = file_reader3.read()

s3 = r'\w+@\w+.[a-z]+'
results_all = re.findall(s3, text3)

for item in results_all:
    final_results3.write(item + '\n')
print(f'Total:{str(len(results_all))}')

# номера
file_path2 = 'MOCK_DATA.txt'
result_file_path2 = '../islam_tashmatov_hw_5/adresse.txt'

file_reader2 = open(file_path2, mode='r', encoding="UTF-8")
final_results2 = open(result_file_path2, mode='w', encoding="UTF-8")

text2 = file_reader2.read()

s2 = r'#\w+'
results_all = re.findall(s2, text2)

for item in results_all:
    final_results2.write(item + '\n')
print(f'Total:{str(len(results_all))}')

# расширенная информация
file_path1 = 'MOCK_DATA.txt'
result_file_path1 = '../islam_tashmatov_hw_5/info.txt'

file_reader1 = open(file_path1, mode='r', encoding="UTF-8")
final_results1 = open(result_file_path1, mode='w', encoding="UTF-8")

text1 = file_reader1.read()

s1 = r"[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+\w+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+[0-9]|" \
     r"[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+[0-9]" \

results_all = re.findall(s1, text1)

for item in results_all:
    final_results1.write(item + '\n')
print(f'Total:{str(len(results_all))}')