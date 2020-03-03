# -*- coding: utf-8 -*-

"""
Приближение функции (target_func) многочленом на отрезке [1, 15].

"""

import numpy as np
import matplotlib.pyplot as plt

# %% объявление функций

def target_func (x: np.ndarray):
    """
    Функция, которую надо приблизить многочленом.
    
    """
    
    return np.sin(x / 5) * np.exp(x / 10) + (5 * np.exp(-x / 2))

def polinome_coeff (points: np.ndarray):
    """
    Получение коэффициентов многочлена путём решения системы линейных
    уравнений. Полученный многочлен совпадает с target_func в точках points.
    
    """
    
    n = points.shape[0]
    
    # Aw = f
    A = np.ones((n, n))
    for i in range(1, n):
        A[:, i] = points ** i
    f = target_func(points)
    
    w = np.linalg.solve(A, f)
    return w

def approx_func (x: np.ndarray, w: np.ndarray):
    """
    Многочлен, коэффициеты которого хранятся в векторе w.
    
    """
    
    ans = np.zeros(x.shape)
    for index, value in np.ndenumerate(w):
        ans += value * (x ** index[0])
    
    return ans

def comparison_graph (w: np.ndarray, file_name='test'):
    """
    График сравнения target_func и многочлена с вектором коэффициентов w.
    
    """
    
    plt.figure(figsize=(12, 8))
    
    x = np.linspace(1, 15, 100)
    plt.plot(x, target_func(x), linewidth=3)
    plt.plot(x, approx_func(x, w), linewidth=3)
    
    assert ('' != file_name)
    plt.savefig('{}.png'.format(file_name), dpi=400)
    
def answer (points: np.ndarray, name: str):
    """
    Функция выводит строку -- ответ на задачу и сохраняет график сравнения
    с целевой функцией.
    
    """
    
    w = polinome_coeff(points)
    
    comparison_graph(w, file_name=name)
    
    ans_line = "Коэффициенты многочлена степени {}: ".format(points.shape[0])
    for index, value in np.ndenumerate(w):
        ans_line += "w_{} = {:.2f}; ".format(index[0], value)
    
    print(ans_line[:-2] + " (смотри рисунок '{}.png')".format(name))

# %% тело программы

if __name__ == '__main__':
    
    answer(points=np.array([1, 15]), name='n=1')
    answer(points=np.array([1, 8, 15]), name='n=2')
    answer(points=np.array([1, 4, 10, 15]), name='n=3')