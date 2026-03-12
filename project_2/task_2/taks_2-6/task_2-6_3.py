phenotype_donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
phenotype_pation = input("Введите фенотип группы крови пациента (I, II, III, IV): ").strip().upper()

if phenotype_pation == phenotype_donor or phenotype_donor == "I" :
    print("Можно перелевать")
elif phenotype_pation != phenotype_donor and phenotype_donor != "I" and phenotype_pation=='I': 
    print(f"Нельзя перелевать!! Нужна кровь {phenotype_pation} группы ")
else:
    print(f"Нельзя перелевать!! Нужна кровь {phenotype_pation}  или I группы")