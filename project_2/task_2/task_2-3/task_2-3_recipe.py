name_pit_sred = input('Введите название питательной среды:')
number_cont_agara = input('Введите концентрацию агара (%):')
temp_ster = input('Введите температуру стерилизации (°C):')

text_txt = f"""
питательной среда: \n{name_pit_sred}
концентрация агара (%): \n{number_cont_agara}
температура стерилизации (°C): \n{temp_ster}"""
print(text_txt,"Файл 'recipe.txt' успешно сформирован!", sep="\n\n")

with open('K:/project 2/task_2/task_2-3/recipe.txt','w',encoding="utf-8") as recipe:
    recipe.write(text_txt)

    
