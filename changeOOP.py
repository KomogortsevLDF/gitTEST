a = []; n = 30; flag = 0; w = 0
class car:
    name = "Volkswagen"
    color = "Black"
    year = 1999
    probeg = 100
    lamp = "выкл"
    def __init__(self,name):
        self.name = name
    def set(self, name, color, year, probeg, lamp):
        self.name = name
        self.color = color
        self.year = year
        self.probeg = probeg
        self.lamp = lamp
def out(a1):
    v = 1; global flag
    while v > 0:
        v-=1
        print("     Параметры","       ", "  Текущие параметры")
        print("1) Название машины -","       ", a[a1-1].name)
        print("2) Цвет машины -","           ", a[a1-1].color)  
        print("3) Год выпуска машины -","    ", a[a1-1].year)
        print("4) Пробег машины (км) -","    ", a[a1-1].probeg,"км")
        print("5) Фары -","                  ", a[a1-1].lamp)
        print("")
        print("6) Изменить все параметры ")
        print("7) Возврат к выбору машин ")
        print("8) Выход ")
        ans2 = input("\n--> ")
        if ans2 == "8" or ans2 == "!":
            print("")
            flag = 0
            break
        elif ans2 == "7":
             global ans; ans = "2"; flag = 1; break
        elif ans2 == "1":
            a[a1-1].name = input("\nВведите название ")
            flag = 0
        elif ans2 == "2":
            a[a1-1].color = input("\nВведите цвет ")
            flag = 0
        elif ans2 == "3":
            a[a1-1].year = input("\nВведите год ")
            flag = 0
        elif ans2 == "4":
            a[a1-1].probeg = input("\nВведите пробег ")
            flag = 0
        elif ans2 == "5":
            a[a1-1].lamp = input("\nВведите положение фар (вкл/выкл) ")
            flag = 0
        elif ans2 == "6":
            a[a1-1].name = input("Введите название ")
            a[a1-1].color = input("Введите цвет ")
            a[a1-1].year = input("Введите год ")
            a[a1-1].probeg = input("Введите пробег ")
            a[a1-1].lamp = input("Введите положение фар (вкл/выкл) ")
            flag = 0
        else:
            print("\nТакого параметра не существует\n")
            v = 1
        if v != 1:
            print("")        
            print("     Параметры","       ", "  Текущие параметры")
            print("1) Название машины -","       ", a[a1-1].name)
            print("2) Цвет машины -","           ", a[a1-1].color)  
            print("3) Год выпуска машины -","    ", a[a1-1].year)
            print("4) Пробег машины -","         ", a[a1-1].probeg,"км")
            print("5) Фары -","                  ", a[a1-1].lamp)
            input("\nEnter\n")

while 1 > 0:
    n = w
    k = c = 0
    for i in range(n):
        if a[i] != 0:
            k+=1
            c+=1
    if flag == 0:
        print("""Выберите дейтвие:
        1) Добавить машину в гараж
        2) Посмотреть/Изменить параметры машины
        3) Удалить машину из гаража
        4) Список машин (гараж)
        5) Добавить сразу много машин
        6) Очистить гараж\n\n""", "Машин в гараже - ", k,"\n")
        ans = input("--> ")
        print("")
    else:
        print("")
    if ans == "1":
        while 1 > 0:
            a.append(0)
            w+=1
            n = w
            for i in range(n):
                if a[i] == 0:
                    name = input("Введите имя ")
                    print("")
                    a[i] = car(name)
                    print("Машина добавлена\n")
                    break
            break
        input("Enter\n")
    elif ans == "2":
        if c == 0:
            print("Вы ещё не добавили ни одной машины")
            input("\nEnter\n")
        else:
            print("Выберите машину\n")
            for i in range(n):
                if a[i] != 0:
                    print(str(i+1)+")",a[i].name)
            print("\nДля выхода введите - !")
            ans1 = input("\n--> ")
            if ans1 == "!":
                print("")
                flag = 0
            else:
                print("")
                try:
                    answer1 = int(ans1)
                except ValueError:
                    print("Введено невеное значение\n")
                    ans = "2"; flag = 1
                else:
                    if answer1 <= c:
                        for i in range(k):
                            if answer1 == i+1:
                                out(answer1)
                    else:
                        print("Такой машины нет")
                        ans = "2"; flag = 1
    elif ans == "3":
        if c == 0:
            print("Вы ещё не добавили ни одной машины")
            input("\nEnter\n")
        else:
            print("Выберите машину\n")
            for i in range(n):
                if a[i] != 0:
                    print(str(i+1)+")",a[i].name)
            print("\nДля выхода введите - !\n")
            ans1 = input("--> ")
            if ans1 == "!":
                flag = 0
                print("")
            else:
                try:
                    answer1 = int(ans1)
                except:
                    print("\nВведено невеное значение")
                    ans = "3"; flag = 1
                else:
                    if answer1 <= k:
                        a[answer1-1] = 0
                        for i in range(n-1):
                            if a[i] == 0 and a[i+1] != 0:
                                a[i] = a[i+1]
                                a[i+1] = 0
                        print("\nМашина удалена\n")
                        input("Enter\n"); flag = 0
                    else:
                        print("\nМашины с таким номером не существует")
                        ans = "3"; flag = 1
    elif ans == "4":
        if c == 0:
            print("Вы ещё не добавили ни одной машины")
            input("\nEnter\n")
        else:
            for i in range(n):
                if a[i] != 0:
                    print(str(i+1)+")",a[i].name)
            input("\nEnter\n")
    elif ans == "5":
        flag2 = 0
        while 1 > 0:
            a.append(0)
            w+=1; n = w
            for i in range(n):
                k = 0
                for j in range(n):
                    if a[j] != 0:
                        k+=1
                if a[i] == 0:
                    name = input("Введите название машины        Для выхода введите - !\n\n")
                    if name == "!" or name == "STOP" or name == "Stop":
                        if k == 0:
                            print("")
                        else:
                            print("\nМашины успешно добавлены\n")
                        flag2 = 1
                        break
                    else:
                        a[i] = car(name)
                        print("\nМашина добавлена","             Машин в гараже - ", k+1,"\n")
            if flag2 == 1:
                flag2 = 0
                break
        input("Enter\n")
    elif ans == "6":
        if c == 0:
            print("\nГараж пуст \n")
            input("\nEnter\n")
            flag = 0
        else:
            ans1 = input("""Вы действительно хотите очистить весь гараж?

    1) Да
    2) Нет\n\n--> """)
            if ans1 == "1":
                flag = 0
                for i in range(n):
                    a[i] = 0
                print("\nГараж пуст")
                input("\nEnter\n")
            elif ans1 == "2":
                print("\nДействие отменено")
                input("\nEnter\n")
                flag = 0
            else:
                print("\nВведено неверное значение")
                ans = "6"; flag = 1
    else:
        print("\nВведено неверное значение\n")
