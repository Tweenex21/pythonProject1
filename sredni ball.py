grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students) # Сортировка словаря по алфавиту



students_dict = {} # создаем зону для нового словаря ключ и значение

students_dict[students[0]] = sum(grades[0])/len(grades[0]) # 1 ключ, 2 сумма в списке, 3 длина списка
students_dict[students[1]] = sum(grades[1])/len(grades[1])
students_dict[students[2]] = sum(grades[2])/len(grades[2])
students_dict[students[3]] = sum(grades[3])/len(grades[3])
students_dict[students[4]] = sum(grades[4])/len(grades[4])


print(students_dict)