# -*- coding: utf-8 -*-
"""
SkillFactory DataScience module 0 task
version: 0.2
Created on Sun May 31 19:20:55 2020
@author: insar
"""


def game_core_v3(number, left_boundary, right_boundary):
    '''
    Начинаем с числа посередине заданного промежутка. Сравниваем с загаданным числом.
    В зависимости от результата сравнения берем одну из половинок - и снова берем
    число посередине.
    '''
    count = 1
    predict = int((right_boundary - left_boundary)/2)  # в первый раз берем число посередине.

    while predict != number:
        if predict < number:
            left_boundary = predict+1
        elif predict > number:
            right_boundary = predict-1
        # выбираем промежуток, в который попадает загаданное число
        predict = left_boundary + int((right_boundary - left_boundary)/2)
        count += 1
    return(count)


def score_game(game_core, left_boundary=1, right_boundary=100, size=1000):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    left_boundary - нижняя граница возможного числа,
    right_boundary - правая граница загаданного числа,
    size - количество экспериментов.
    '''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(left_boundary, right_boundary+1, size)
    for number in random_array:
        count_ls.append(game_core(number, left_boundary, right_boundary))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)
