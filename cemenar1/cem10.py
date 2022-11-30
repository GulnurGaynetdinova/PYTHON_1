import math


x_coordinate_A = float(input('Введите координату точки А по оси Х: '))
y_coordinate_A = float(input('Введите координату точки А по оси Y: '))
x_coordinate_B = float(input('Введите координату точки B по оси Х: '))
y_coordinate_B = float(input('Введите координату точки B по оси Y: '))
AC = x_coordinate_B - x_coordinate_A 
BC = y_coordinate_B - y_coordinate_A
distance = round(math.sqrt(AC**2 + BC**2), 2)
print(distance)