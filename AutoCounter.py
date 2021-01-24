from pyautogui import write, press
from time import sleep

print("Кто прочитал тот приёмный! by NightMaidBot#7660")
print("Дабавьте 2 к скорость от медленного режима/Add 2 of the slow mode")
swr = input("следуещее число/Next number >")
spd = int(input("Скорость/Speed >"))
print("Открой дискорд,нажми на поле ввода и жди(комп не трогай)/Open Discord, touch the input and wait(don't use PC)")
sleep(10)
def turbo(count, speed):
    while count!= 10001:
        print(count)
        count=str(count)
        write(count)
        press('enter')
        sleep(speed)
        count=int(count)
        count=count+1;
    turbo(swr, spd)
turbo(swr, spd)