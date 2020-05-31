# -*- coding: utf-8 -*-
"""
SkillFactory DataScience module 0 task
version: 0.1
Created on Sun May 31 19:20:55 2020
@author: insar
"""

def game_core_v3(number):
    count = 1
    left_boundary = 0
    right_boundary = 100
    predict = int((right_boundary - left_boundary)/2)

    while predict != number:
        if predict < number:
            left_boundary = predict+1
        elif predict > number:
            right_boundary = predict-1
        predict = left_boundary + int((right_boundary - left_boundary)/2)
        count += 1
    return(count)
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)