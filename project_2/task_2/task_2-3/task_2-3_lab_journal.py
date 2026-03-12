fio = input('Введите ФИО:')
data = input('Дата:')
name_exp = input('Названия эксперимента:')
vivod = input('Вывод:')

fio +=' '*(29-len(fio))
data +=' '*(30-len(data))
name_exp +=' '*(30-len(name_exp))
vivod +=' '*(142-len(vivod))

text_lab = f"""
+--------------------------------------------------+
| Электронный лабораторный журнал                  |
+--------------------------------------------------+
| ФИО исследователя : {fio}|
| Дата             : {data}|
| Эксперимент      : {name_exp}|
+--------------------------------------------------+
| Вывод:                                           |
| {vivod[:47]}  |
| {vivod[48:94]}   |
| {vivod[95:141]}  |
+--------------------------------------------------+"""

print(text_lab,'Данные успешно сохранены в journal.txt',sep="\n")

with open('K:/project 2/task_2/task_2-3/journal.txt','w', encoding='utf-8') as f:
    f.write(text_lab)

with open('K:/project 2/task_2/task_2-3/journal.txt','r', encoding='utf-8') as f:
    print(f.read())