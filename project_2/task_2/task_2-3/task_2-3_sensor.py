name = input('Введите имя оператора:')
p = input('Введите текущее значение давления (Па):')

text_txt = f"""Имя оператора\t{name}
текущее значения давления(Па)\t{p}"""

print(text_txt,'Данные успешно сохранены в sensor_log.txt')

with open('K:/project 2/task_2/task_2-3/sensor.txt','w',encoding='utf-8') as f:
    f.write(text_txt)

with open('K:/project 2/task_2/task_2-3/sensor.txt','r',encoding='utf-8') as f:
    print(f.read())