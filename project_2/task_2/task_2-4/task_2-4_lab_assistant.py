volume = int(input('Введите нужный объем раствора: '))

salt_mass = round(volume*0.009, 2)
output = f"""
ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:
-----------------------
Общий объем: [{volume}] мл
Масса соли:  [{salt_mass}] г
Объем воды:  [{volume}] мл"""

with open('K:/project 2/task_2/task_2-4/recipe.txt','w',encoding='utf-8') as f:
    f.write(output)
print(output,'\nфайл сформирован')

