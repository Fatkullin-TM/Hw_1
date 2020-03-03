# -*- coding: utf-8 -*-

"""
Решите без использования циклов средставми NumPy
(каждый пункт решается в 1-2 строчки).

"""

import numpy as np

# %% объявление функций

def ex_1 ():
    """
    1. Создайте вектор с элементами от 12 до 42.

    """

    return np.arange(12, 42)

def ex_2 ():
    """
    2. Создайте вектор из нулей длины 12, но его пятый елемент
    должен быть равен 1.

    """

    v = np.zeros(12)
    v[4] = 1

    return v

def ex_3 ():
    """
    3. Создайте матрицу (3, 3), заполненую от 0 до 8.

    """

    return np.arange(0, 9).reshape((3, 3))

def ex_4 ():
    """
    4. Найдите все положительные числа в np.array([1,2,0,0,4,0]).

    """

    v = np.array([1,2,0,0,4,0])
    return v[v > 0]

def ex_5 ():
    """
    5. Умножьте матрицу размерности (5, 3) на (3, 2).

    """

    A = np.random.random((5, 3))
    print("A = \n{}".format(A))
    B = np.random.random((3, 2))
    print("B = \n{}".format(B))

    return "A x B = \n{}".format(A.dot(B))

def ex_6 ():
    """
    6. Создайте матрицу (10, 10) так, чтобы на границе были 0, а внтури 1.

    """

    A = np.zeros((10,10))
    A[1:9, 1:9] = 1

    return A

def ex_7 ():
    """
    7. Создайте рандомный вектор и отсортируйте его.

    """

    v = np.random.random(5)

    return np.sort(v)

def ex_8 ():
    """
    8. Каков эквивалент функции enumerate для numpy массивов?

    """

    A = np.arange(9).reshape((3,3))
    print("A = \n{}".format(A))

    print("for index, value in np.ndenumerate(A): print(index, value)")
    for index, value in np.ndenumerate(A):
        print(index, value)

    return "numpy.ndenumerate"

def ex_9 ():
    """
    9. *Создайте рандомный вектор и выполните его нормализацию.

    """

    v = np.random.random(10)
    print("v = \n{}".format(v))

    return "v_norm = \n{}".format((v - v.mean()) / v.std())

def ex_10 ():
    """
    10. *Для заданного числа n найдите ближайший к нему элемент в векторе V.
    
    """

    n = np.random.uniform(0,100)
    print("n = \n{}".format(n))
    V = np.arange(100)
    print("V = \n{}".format(V))

    index = (np.abs(V - n)).argmin()
    return V[index]

def ex_11 ():
    """
    11. *Найдите n наибольших значений в векторе.
    

    """

    n = np.random.randint(1, 10)
    print("n = \n{}".format(n))
    V = np.random.random(10)
    print("V = \n{}".format(V))

    return V[np.sort(V.argsort()[-n:])]

def do_exercise (func):
    """
    Функция выводит текст упражнения и ответ, полученный с помощью одной из
    функций (название функций: ex_N, где N -- номер упражнения).
    
    """

    print("Задание: {}".format(func.__doc__[:-10]))
    print("Ответ: \n{}".format(func()), end='\n\n')


# %% тело программы

if __name__ == '__main__':

    exercise_tuple = (ex_1, ex_2, ex_3, ex_4, ex_5,
                      ex_6, ex_7, ex_8, ex_9, ex_10,
                      ex_11)
    for ex in exercise_tuple:
        do_exercise(ex)