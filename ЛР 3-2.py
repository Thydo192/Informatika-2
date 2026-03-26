def find_common_participants(group1, group2, delimiter=','):
    #Разбиваем строку group1 на список по разделителю
    list1 = group1.split(delimiter)
    #Разбиваем строку group2 на список по разделителю
    list2 = group2.split(delimiter)
    # Создаем пустой список для общих участников
    common = []
# Перебираем каждого участника из первого списка
    for i in list1:
        #Проверяем: есть ли этот участник во втором списке?
        if i in list2:
            # Если есть - добавляем в список общих участников
            common.append(i)
        #Сортируем список общих участников в алфавитном порядке
    common.sort()
    return common
# Проверка работы функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызываем функцию с разделителем '|'
result = find_common_participants(participants_first_group, participants_second_group, '|')
print(result)