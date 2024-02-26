import time
import os
print("Vytvořil larisek")
print("Github: https://github.com/larisek")
print("1.stopky")
print("2.časovač")
chsmain = input("Výběr: ")
if int(chsmain) == 1:
    from datetime import datetime
    input("start")
    start = datetime.now()
    input("stop")
    end = datetime.now()
    time_taken = end - start
    print('čas: ',time_taken) 
elif int(chsmain) == 2:
    print("Vyber možnost")
    print("1. sekundy")
    print("2. minuty")
    print("3. hodiny")
    chs = input()
    for i in range(1, 101):
        print()
    if int(chs) == 1:
        chos = input("Sekundy: ")
        for i in range(0, int(chos)):
            print(chos)
            time.sleep(1)
            chos = int(chos) - 1
    elif int(chs) == 2:
        chos = input("minuty: ")
        chos2 = input("sekundy: ")
        cal = int(chos2) + 60 * int(chos)
        for i in range(cal):
            if int(chos2) == 0:
                chos2 = int(chos2) + 60
                chos = int(chos) - 1
            time.sleep(1)
            for i in range(1, 50):
                print()
            print(f"{chos} : {chos2}")
            chos2 = int(chos2) - 1
    elif int(chs) == 3:
        chos3 = input("Hodiny: ")
        chos = input("Minuty: ")
        chos2 = input("Sekundy: ")
        cal = int(chos2) + 60 * int(chos) + 3600 * int(chos3)
        for i in range(cal):
            if int(chos2) == 0:
                time.sleep(1)
                for i in range(1, 50):
                    print()
                print(f"{chos3} : {chos} : {chos2}")
                chos2 = int(chos2) - 1
                if int(chos) == 0:
                    chos = int(chos) + 59
                    chos2 = int(chos2) + 60
                    chos3 = int(chos3) - 1
                else:
                    chos2 = int(chos2) + 60
                    chos = int(chos) - 1
            time.sleep(1)
            for i in range(1, 50):
                print()
            print(f"{chos3} : {chos} : {chos2}")
            chos2 = int(chos2) - 1
    else:
        import end
        from end import end
        print(end)
else:
    import end
    from end import end
    print(end)
