with open('C:/Users/andre_33ifa79/Downloads/project_4/task_4-8/task_4-8-1.txt','a',encoding='utf-8') as f:
    a = [7, 3, 8, 1, 4, 6, 2, 5]
    n = len(a)
    end = n
    p = False
    for i in range(n):
        if p==True:
            break
        else:
            p = True
            print(f'\nИтерация {i+1}:',file=f)
        for j in range(n-1):
            if end==j:
                break
            if a[j]>a[j+1]:
                temp = a[j]
                a[j]=a[j+1]
                a[j+1]= temp
                print(f'{a} ({a[j+1]} и {a[j]} поменялись)',file=f)
                p = False
            else:
                print(f'{a} ({a[j+1]} и {a[j]} не меняются)',file=f)
        end -= 1 