import colorama
from math import ceil as uppp
from math import floor as down
SetColor = {
    1: colorama.Fore.RED,
    2: colorama.Fore.YELLOW,
    3: colorama.Fore.GREEN,
    4: colorama.Fore.CYAN,
    5: colorama.Fore.BLUE,
    6: colorama.Fore.MAGENTA
    }
print(colorama.Style.BRIGHT)
koleno = 1
minus = "__" * down(float(input("ваша диаганаль экрана(для красоты): ")) / 337 * 256) * 8
def minercalc(SetColor):
    color = 0
    while 1:
        try:
            # я начинаю делать радугу
            print(colorama.Fore.RED)
            color += 1
            if color > 6:
                color = 1
            print(SetColor[color])
            # я заканчиваю делать радугу
            miner = input("оборудование: ")
            if miner == "stop":
                break
            cost = int(input("цена: "))
            pribilj = int(input("прибыль: "))
            power = int(input("мощность: "))
            maxwatt = int(input("максимальная мощность: "))
            if power > maxwatt:
                print("максимальная мощность не может быть меньше мощности майнера")
                continue
            print("соотношение прибыль/ватт:" + str(round((power / pribilj), 2)) + "\nприбыль со всех майнеров:" + str(pribilj * down(maxwatt / power)) + "\nокупаемость: " + str(cost / pribilj) + " ваших периодов прибыли")
        except ValueError:
            print(minus + "\nвведено неверноe изначальное значение")
            continue
        except ZeroDivisionError:
            print(minus + "\nне может быть параметр в \"0\"")
#########################################################################################################################################
#########################################################################################################################################
def moneymanagement(koleno, SetColor):
        try:
            color = 1
            deposit = int(input(minus + """
депозит: """))
            if deposit < 1:
                print(minus + """
депозит слишком мал""")
                moneymanagement(koleno, SetColor)
            procent = int(input("процент дохода: "))
            if procent > 100:
                print(minus + """
процент не может быть больше 100%""")
                moneymanagement(koleno, SetColor)
            stavka = deposit / 50
            if deposit < stavka:
                print(minus + """
депозит не может быть меньше ставки""")
                moneymanagement(koleno, SetColor)
            if stavka <= 0:
                print(minus + """
такая ставка невозможна""")
                moneymanagement(koleno, SetColor)
            mnoj = 2 / (procent / 100)
            P = 0.4
            oldP = P * 100
            ostatok = deposit - uppp(stavka * (1 / (procent / 100)))
            if procent < 100 and (deposit - stavka) < (uppp(stavka * (1 / (procent / 100)))):
                print(minus + """
это невозможно""")
                moneymanagement(koleno, SetColor)
            stavka = uppp((stavka) * (1 / (procent / 100)))
            SetColor = 1
            if koleno < 555 and ostatok > 0:
                print(colorama.Fore.RED + "\n \n" + minus + "\n  ставка:     " + str(stavka) + "        остаток: " + str(ostatok) + "        вероятность выигрыша:" + str(oldP) + "%")
            while ostatok > 0 and koleno < 555:
                if stavka == None:
                    moneymanagement(koleno, SetColor)
                stavka = uppp(stavka * mnoj)
                # я начинаю делать радугу
                color += 1
                if color > 6:
                    color = 1
                # я заканчиваю делать радугу
                ostatok -= stavka
                if ostatok > 0 and koleno < 555:
                    oldP += 100 * ((1 - (oldP / 100)) * P)
                    print(SetColor[color] + str(koleno) + " колено:     " + str(stavka) + "       остаток: " + str(ostatok) + "        вероятность выигрыша:" + str(oldP) + "%")
                    if stavka == None:
                        moneymanagement(koleno, SetColor)
                    koleno += 1
            if koleno < 555:
                print(SetColor[color] + str(koleno) + " колено:     " + str(ostatok + stavka) + "        остаток: 0" + "        вероятность выигрыша:" + str(100 * ((1 - (oldP / 100)) * P) + oldP) + "%" + "      вообще должно было быть:" + str(stavka))
        except ValueError:
            print(minus + """
введено неверноe изначальное значение""")
            moneymanagement(koleno, SetColor)
        except ZeroDivisionError:
            print(minus + """
процент не может быть 0""")
            moneymanagement(koleno, SetColor)
#########################################################################################################################################

#########################################################################################################################################
def binarycalc(koleno):
    try:
        color = 1
        deposit = int(input(minus + """
депозит: """))
        if deposit < 1:
            print(minus + """
депозит слишком мал""")
            binarycalc(koleno)
        procent = int(input("процент дохода: "))
        if procent > 100:
            print(minus + """
процент не может быть больше 100%""")
            binarycalc(koleno)
        stavka = int(input("ставка: "))
        if deposit < stavka:
            print(minus + """
депозит не может быть меньше ставки""")
            binarycalc(koleno)
        if stavka <= 0:
            print(minus + """
такая ставка невозможна""")
            binarycalc(koleno)
        mnoj = 2 / (procent / 100)
        P = 0.4
        oldP = P * 100
        ostatok = deposit - uppp(stavka * (1 / (procent / 100)))
        if procent < 100 and (deposit - stavka) < (uppp(stavka * (1 / (procent / 100)))):
            print(minus + """
это невозможно""")
            binarycalc(koleno)
        stavka = uppp((stavka) * (1 / (procent / 100)))
        SetColor = 1
        if koleno < 555 and ostatok > 0:
            print(colorama.Fore.RED + "\n \n" + minus + "\n  ставка:     " + str(stavka) + "        остаток: " + str(ostatok) + "        вероятность выигрыша:" + str(oldP) + "%")
        while ostatok > 0 and koleno < 555:
            if stavka == None:
                binarycalc(koleno)
            stavka = uppp(stavka * mnoj)
            # я начинаю делать радугу
            color += 1
            if color > 6:
                color = 1
            SetColor = {
                1: colorama.Fore.RED,
                2: colorama.Fore.YELLOW,
                3: colorama.Fore.GREEN,
                4: colorama.Fore.CYAN,
                5: colorama.Fore.BLUE,
                6: colorama.Fore.MAGENTA
            }
            # я заканчиваю делать радугу
            ostatok -= stavka
            if ostatok > 0 and koleno < 555:
                oldP += 100 * ((1 - (oldP / 100)) * P)
                print(SetColor[color] + str(koleno) + " колено:     " + str(stavka) + "       остаток: " + str(ostatok) + "        вероятность выигрыша:" + str(oldP) + "%")
                if stavka == None:
                    binarycalc(koleno)
                koleno += 1
        if koleno < 555:
            print(SetColor[color] + str(koleno) + " колено:     " + str(ostatok + stavka) + "        остаток: 0" + "        вероятность выигрыша:" + str(100 * ((1 - (oldP / 100)) * P) + oldP) + "%" + "      вообще должно было быть:" + str(stavka))
    except ValueError:
        print(minus + """
введено неверноe изначальное значение""")
        binarycalc(koleno)
    except ZeroDivisionError:
        print(minus + """
процент не может быть 0""")
        binarycalc(koleno)
#########################################################################################################################################
#########################################################################################################################################
def otbiv(koleno):
    try:
        color = 1
        deposit = int(input(minus + """
депозит: """))
        if deposit < 1:
            print(minus + """
депозит слишком мал""")
            otbiv(koleno)
        procent = int(input("процент дохода: "))
        if procent > 100:
            print(minus + """
процент не может быть больше 100%""")
            otbiv(koleno)
        stavka = int(input("ставка: "))
        if deposit < stavka:
            print(minus + """
депозит не может быть меньше ставки""")
            otbiv(koleno)
        if stavka <= 0:
            print(minus + """
такая ставка невозможна""")
            otbiv(koleno)
        mnoj = 1 / (procent / 100)
        P = 0.4
        oldP = P * 100
        ostatok = deposit - uppp(stavka * (1 / (procent / 100)))
        if procent < 100 and (deposit - stavka) < (uppp(stavka * (1 / (procent / 100)))):
            print(minus + """
это невозможно""")
            otbiv(koleno)
        stavka = uppp((stavka) * (1 / (procent / 100)))
        SetColor = 1
        if koleno < 555 and ostatok > 0:
            print(colorama.Fore.RED + "\n \n" + minus + "\n  ставка:     " + str(stavka) + "        остаток: " + str(ostatok) + "        вероятность выигрыша:" + str(oldP) + "%")
        while ostatok > 0 and koleno < 555:
            if stavka == None:
                otbiv(koleno)
            stavka = uppp(stavka * mnoj)
            # я начинаю делать радугу
            color += 1
            if color > 6:
                color = 1
            SetColor = {
                1: colorama.Fore.RED,
                2: colorama.Fore.YELLOW,
                3: colorama.Fore.GREEN,
                4: colorama.Fore.CYAN,
                5: colorama.Fore.BLUE,
                6: colorama.Fore.MAGENTA
            }
            # я заканчиваю делать радугу
            ostatok -= stavka
            if ostatok > 0 and koleno < 555:
                oldP += 100 * ((1 - (oldP / 100)) * P)
                print(SetColor[color] + str(koleno) + " колено:     " + str(stavka) + "       остаток: " + str(ostatok) + "        вероятность выигрыша:" + str(oldP) + "%")
                if stavka == None:
                    otbiv(SetColor, koleno)
                koleno += 1
        if koleno < 555:
            print(SetColor[color] + str(koleno) + " колено:     " + str(ostatok + stavka) + "        остаток: 0" + "        вероятность выигрыша:" + str(100 * ((1 - (oldP / 100)) * P) + oldP) + "%" + "      вообще должно было быть:" + str(stavka))
    except ValueError:
        print(minus + """
введено неверноe изначальное значение""")
        otbiv(koleno)
    except ZeroDivisionError:
        print(minus + """
процент не может быть 0""")
        otbiv(koleno)
#########################################################################################################################################
#########################################################################################################################################
def otbiv2(koleno):
    try:
        color = 1
        deposit = int(input(minus + """
депозит: """))
        if deposit < 1:
            print(minus + """
депозит слишком мал""")
            otbiv2(koleno)
        procent = int(input("процент дохода: "))
        if procent > 100:
            print(minus + """
процент не может быть больше 100%""")
            otbiv2(koleno)
        stavka = float(input("ставка: "))
        if deposit < stavka:
            print(minus + """
депозит не может быть меньше ставки""")
            otbiv2(koleno)
        if stavka <= 0:
            print(minus + """
такая ставка невозможна""")
            otbiv2(koleno)
        mnoj = 1 / (procent / 100)
        P = 0.4
        oldP = P * 100
        ostatok = deposit - stavka * (1 / (procent / 100))
        if procent < 100 and (deposit - stavka) < (stavka * (1 / (procent / 100))):
            print(minus + """
это невозможно""")
            otbiv2(koleno)
        stavka = (stavka) * (1 / (procent / 100))
        SetColor = 1
        if koleno < 555 and ostatok > 0:
            print(colorama.Fore.RED + "\n \n" + minus + "\n  ставка:     " + str(stavka) + "        остаток: " + str(ostatok) + "        вероятность выигрыша:" + str(oldP) + "%")
        while ostatok > 0 and koleno < 555:
            if stavka == None:
                otbiv2(koleno)
            stavka = round(stavka * mnoj, 2)
            # я начинаю делать радугу
            color += 1
            if color > 6:
                color = 1
            SetColor = {
                1: colorama.Fore.RED,
                2: colorama.Fore.YELLOW,
                3: colorama.Fore.GREEN,
                4: colorama.Fore.CYAN,
                5: colorama.Fore.BLUE,
                6: colorama.Fore.MAGENTA
            }
            # я заканчиваю делать радугу
            ostatok -= stavka
            if ostatok > 0 and koleno < 555:
                oldP += 100 * ((1 - (oldP / 100)) * P)
                print(SetColor[color] + str(koleno) + " колено:     " + str(stavka) + "       остаток: " + str(ostatok) + "        вероятность выигрыша:" + str(oldP) + "%")
                if stavka == None:
                    otbiv2(SetColor, koleno)
                koleno += 1
        if koleno < 555:
            print(SetColor[color] + str(koleno) + " колено:     " + str(ostatok + stavka) + "        остаток: 0        вероятность выигрыша:" + str(100 * ((1 - (oldP / 100)) * P) + oldP) + "%" + "      вообще должно было быть:" + str(stavka))
    except ValueError:
        print(minus + """
введено неверноe изначальное значение""")
        otbiv2(koleno)
    except ZeroDivisionError:
        print(minus + """
процент не может быть 0""")
        otbiv2(koleno)
#########################################################################################################################################
#########################################################################################################################################
while 1:
    try:
        model = input(minus + "\n1 = стдандарт\n2 = money management(ставка 2% от депозита)\n3 = майнинг калькулятор\n4 = отбить прошлую ставку(меньше рисков)\n5 = отбить прошлую ставку(меньше рисков) с точностью 2 знака после \",\" \n-->")
        if model == "1":
            binarycalc(koleno)
            continue
        if model == "2":
            moneymanagement(koleno, SetColor)
            continue
        if model == "3":
            print("для выхода из режима введите \"stop\"")
            minercalc(SetColor)
            continue
        if model == "4":
            otbiv(koleno)
            continue
        if model == "5":
            otbiv2(koleno)
            continue
        else:
            print(minus + "\nтакого режима не существует")
    except TypeError:
        continue
