M_bel = int(input('Введите массу белков в продукте (г):'))
M_zhir = int(input('Введите массу жиров в продукте (г):'))
M_ugl = int(input('Введите массу углеводов в продукте (г):'))

Kall = M_bel*4+M_zhir*9+M_ugl*4
print(f'Каллории = {Kall}')