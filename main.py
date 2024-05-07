# Завдання 1

# import random
# import threading
#
# class Result:
#     def __init__(self):
#         self.numbers = []
#         self.sum = 0
#         self.mean = 0
#
# def random_numbers(results, n):
#     for _ in range(n):
#         results.numbers.append(random.randint(1, 100))
#
# def summa(results):
#     results.sum = sum(results.numbers)
#
# def cal_mean(results):
#     results.mean = sum(results.numbers) / len(results.numbers)
#
# results = Result()
# n = 5
#
# num_thread = threading.Thread(target=random_numbers, args=(results, n))
# sum_thread = threading.Thread(target=summa, args=(results,))
# mean_thread = threading.Thread(target=cal_mean, args=(results,))
#
# num_thread.start()
# num_thread.join()
#
# sum_thread.start()
# mean_thread.start()
#
# sum_thread.join()
# mean_thread.join()
#
# print("Список чисел:", results.numbers)
# print("Сума елементів списку:", results.sum)
# print("Середнє арифметичне значення:", results.mean)



# Завдання 2
# import threading
# import random
# import math
#
# class Results:
#     def __init__(self):
#         self.prime_num = []
#         self.factorials = []
#
# def random_num(filename, n):
#     with open(filename, 'w') as file:
#         for _ in range(n):
#             file.write(str(random.randint(1, 100)) + '\n')
#
# def find_prime_numbers(filename, results):
#     prime_num = []
#     with open(filename, 'r') as file:
#         for line in file:
#             num = int(line.strip())
#             if is_prime(num):
#                 prime_num.append(num)
#     results.prime_num = prime_num
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(math.sqrt(num))+ 1):
#         if num % i == 0:
#             return False
#     return True
#
# def cal_factorial(filename, results):
#     factorials = []
#     with open(filename, 'r') as file:
#         for line in file:
#             num = int(line.strip())
#             factorials.append(math.factorial(num))
#     results.factorials = factorials
#
# filename = input('Введіть шлях до файлу:')
# n = 10
#
# results = Results()
#
# random_thread = threading.Thread(target=random_num, args=(filename, n))
# prime_thread = threading.Thread(target=find_prime_numbers, args=(filename, results))
# factorial_thread = threading.Thread(target=cal_factorial, args=(filename, results))
#
# random_thread.start()
# random_thread.join()
#
# prime_thread.start()
# factorial_thread.start()
#
# prime_thread.join()
# factorial_thread.join()
#
# with open('prime_num.txt', 'w') as file:
#     file.write('Прості числа:\n')
#     for prime in results.prime_num:
#         file.write(str(prime) + '\n')
#
# with open('factorial.txt', 'w') as file:
#     file.write('Факторіал чисел:\n')
#     for factorial in results.factorials:
#         file.write(str(factorial) + '\n')
#
# print("Кількість згенерованих чисел:", n)
# print("Кількість простих чисел:", len(results.prime_num))
# print("Кількість обчислених факторіалів:", len(results.factorials))

# Завдання 3

import os
import threading

def search_files(directory, keyword, result_file):
    result_content = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if keyword in content:
                    result_content.append(content)

    with open(result_file, 'w') as result:
        result.writelines(result_content)


def filter_words(input_file, banned_words_file):
    with open(banned_words_file, 'r') as banned_words:
        banned = set(banned_words.read().split())

    with open(input_file, 'r') as f:
        content = f.read()

    for word in banned:
        content = content.replace(word, '')

    with open(input_file, 'w') as f:
        f.write(content)


directory_path = input("Введіть шлях до директорії: ")
search_word = input("Введіть слово для пошуку: ")

result_file = "result.txt"

search_thread = threading.Thread(target=search_files, args=(directory_path, search_word, result_file))
search_thread.start()

search_thread.join()

filter_thread = threading.Thread(target=filter_words, args=(result_file, "banned_words.txt"))
filter_thread.start()

filter_thread.join()

print("Операції виконані успішно.")













