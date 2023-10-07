#1 проверка на простоты числа

# while True:
#     simple = int(input('\n''#################################''\n''проверка на простоты числа: '))
#     assistant=0 #для того что бы помочь вывести один результат, а не повторные
#
#     if simple>1:     #что бы определить является ли число проситым
#         for i in range(2, simple):  #работает пока не найдет, простое ли число
#             if simple % i==0:
#                 assistant =0
#                 break
#             else:
#                 assistant=1
#     else:
#         assistant = 0
#
#     if assistant == 0:
#         print(f'число {simple} не является простым')
#     elif assistant == 1:
#         print(f'число {simple} является простым')


# 2 Задача о сортировке массива

# while True:
#     array=[]
#
# quantity=int(input('\n''#################################''\n''сколько цифр нужно отсортировать?  '))
# for i in range(quantity):
#     array.append(int(input('введите числа которые нужно отсортировать:  '))) #нужно для ввода массива с клавы
#
#         for i in range (len(array)):
#             for j in range (0, len(array)-i-1):
#                 if array[j]>array[j+1]:
#                     array[j], array[j+1]=array[j+1],array[j]  #сама сортировка
#
#     print(f"отсортированный список {array}")



#3  Задача о поиске наибольшего элемента в массиве

#######тут легко если сделал пред.задание, потому что достаточно поменять знак равенства что бы сортировка шла с большего и в
#print указать первый элемент массива
#######ну или вообще скопировать прошлое и в конце исправить ##print(array[-1])

# while True:
#     #массив
#     array=[]
#
#     quantity=int(input('\n''#################################''\n''количество цифр, среди которых нужно найти наибольшее:  '))
#     for i in range(quantity):
#         array.append(int(input('введите числа, среди которых нужно найти наибольшее:  ')))   #нужно для ввода массива с клавы:
#
#     for i in range (len(array)):
#          for j in range (0, len(array)-i-1):
#             if array[j]<array[j+1]:
#                 array[j], array[j+1]=array[j+1],array[j] #сортирует массив по убыванию
#     print(f"среди {array} наибольшяя цифра: {array[0]}") #показывает первый элемент отсортированного списка



#4 Задача о вычислении числа Фибоначчи

# while True:
#     number_of_Finobacci=int(input('\n''#################################''\n''номер числа Фибоначчи:  '))
#     fib1 = fib2 = 1
#     number_of_Finobacci = number_of_Finobacci - 2
#     for i in range (number_of_Finobacci):
#         fib1, fib2 = fib2, fib1 + fib2
#     print(f"Значение этого элемента: {fib2}")


#5 Задача на хэш-таблицы

# while True:
#     strings = []
#     quantity = int(input('\n''#################################''\n''сколько слов хотите добавить?:  '))
#     for i in range(quantity):
#         strings.append(input('введите слова которые нужно вставить в массив, чтобы потом показать какое слово больше всего встречается:  '))  # нужно для ввода массива с клавы
#
#     word_count = {}
#     max_count = 0
#     most_common_word = None
#
#     for word in strings:
#         word_count[word] = word_count.get(word, 0) + 1
#         if word_count[word] > max_count:
#             max_count = word_count[word]
#             most_common_word = word
#
#     print("Наиболее часто встречающаяся строка:", most_common_word)