data = input('Введите дату: ')
files = ["seq1", "seq2", "seq3", "seq4"]

for name in files:
   new_name = name + ".fasta"+f' [{data}]'
   print(f"{new_name}")