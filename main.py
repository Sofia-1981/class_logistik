import sys
import lib1 as l

car1=l.AVTO('golf_1', 10)
car2=l.AVTO('golf_2', 20)
car3=l.AVTO('golf_3', 30)
car4=l.AVTO('golf_4', 40)

my_garaze=l.GARAZH('my', 15)
my_garaze.add_to_garaze(car1.marka, car1)
my_garaze.add_to_garaze(car2.marka, car2)
my_garaze.add_to_garaze(car3.marka, car3)
my_garaze.add_to_garaze(car4.marka, car4)

print(my_garaze.garaze)

my_garaze.chek_free()


while True:
    try:
        need_tonn=int(input('Введите нужное колличество тонн'))
        #сюда пишем код с клиентом
        sys.exit()
    except ValueError:
        print("Введено неверное колличество тонн")


