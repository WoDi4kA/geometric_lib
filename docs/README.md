
### Общее описание решений
1. Сделал git clone своего репозитория
2. Открыл папку geometric_lib через терминал
2. Создал ветку documentation_(мой ису)
3. Описал решение файлов rectangle.py и triangle.py в PyCharm
4. Сделал git add и git commit каждому файлу
---
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

___
### Описание каждой функции с примерами вызова

* __Circle:__
_def area(r):_
   _return math.pi * r * r_
``` 
in: 7
out: 248,06
```

* __Rectangle:__
_def rectangle(a, b):
   return a * b_
``` 
in: 7 8
out: 56
```

* __Square:__
_def square(a):
   return a * a_
``` 
in: 12
out: 144
```

* __Circle:__
_def circle(r):
return meth.pi * r * 2_
``` 
in: 7
out: 43,96
```

* __Rectangle:__
_def rectangle(a, b):
return 2 * a + 2 * b_
``` 
in: 7 8
out: 30
```

* __Square:__
_def square(a):
return 4 * a_

``` 
in: 7
out: 28
```

___
### ___Rectangle.py___

```
Функция нахождения площади прямоугольника.
```
**def area(a, b):** 
    *'''Принимает число a и число b, возвращает их умножение, возвращает площадь'''* 
    **return a * b**
 >> __Пример__: 
 _Ввод_: 7 8
 _Вывод_: 56

```
Функция нахождения периметра прямоугольника.
```
 **def perimeter(a, b):** 
    *'''Принимает число a и число b, возвращает умноженную на два их сумму, возвращает периметр'''*
    **return (a + b) * 2**
 >> __Пример__: 
 _Ввод_: 7 8
 _Вывод_: 30

 
 
 ### ___Triangle.py___
 
```
Функция нахождения площади треугольника.
```
**def area(a, h):**
    *'''Принимает a, h, возвращает площадь треугольника, a умноженную на половину h'''*
    **return a * h / 2**
 >> __Пример__: 
 _Ввод_: 7 8
 _Вывод_: 28
 
 ```
 Функция нахождения периметра треугольника.
 ```
 **def perimeter(a, b, c):** 
    *'''Принимает a, b, c, возвращает периметр треугольника, сумму всех чисел'''*
    **return a + b + c**
 >> __Пример__: 
 _Ввод_: 7 8 9 
 _Вывод_: 24
 ---

 ## _История изменения проекта с хешами комитов (кроме последней записи)_

 commit **5fddd18761a9c04b73cdcb2775c3142502e8b6d6** 
Author: wodi4ka <platonadanaya@gmail.com>
Date: Thu Oct 5 19:05:04 2023 +0300

    Edit comment to rectangle.py

commit **c11fa1adf6af517989d6a1662cbeec2de61bc2c2** 
Author: wodi4ka <platonadanaya@gmail.com>
Date:   Thu Oct 5 19:15:30 2023 +0300

    Edit comment to circle.py

commit **1518c28d1f2889938c6e42ba7b24f43274abed88** 
Author: wodi4ka <platonadanaya@gmail.com>
Date:   Thu Oct 5 19:18:05 2023 +0300

    Edit comment to square.py

commit **76c90c932305e937774a4edfe291bbaf467c1907** 
Author: wodi4ka <platonadanaya@gmail.com>
Date:   Thu Oct 5 19:19:45 2023 +0300

    Edit comment to triangle.py







