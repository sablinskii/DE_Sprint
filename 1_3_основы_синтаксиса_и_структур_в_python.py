# -*- coding: utf-8 -*-
"""
**Задание 1**
"""

import requests
import json
import time
import os
import tqdm

def getPage(key,page = 0):
    params = {
        'text': 'NAME:'+key,
        'area': 113, # Россия
        'page': page, 
        'per_page': 100
    }
    req = requests.get('https://api.hh.ru/vacancies', params) 
    data = req.content.decode()
    req.close()
    return data
    
n = 5  # нужное количество вакансий
key = 'python разработчик' # запрос
for page in range(0, n//100):
    jsObj = json.loads(getPage(key,page))
    if (jsObj['pages'] - page) <= 1:
        break
    time.sleep(0.25)

dt = {"data":[]}

i=0
for js in tqdm.tqdm(jsObj['items']):
    req = requests.get(js['url'])
    data = req.content.decode()
    req.close()

    if js['salary'] != None: salary = str(js['salary']['from'])+' '+js['salary']['currency']
    else: salary = 'не указана'
                
    dt["data"].append({'title':js['name'],'region':js['area']['name'],'salary':salary})
    i+=1
    if i==n: break
    time.sleep(0.25)
    
with open('data.json', 'w') as file:
    json.dump(dt,file,ensure_ascii=False)
    
print('\n\nВакансии собраны!!!')

"""
**Задание 2**
"""

stroka = input('Введите строку: ').replace(' ','').lower()
print('Это палиндром!!!') if stroka == stroka[::-1] else print('Это не палиндром!!!')

"""
**Задание 3**
"""

def arab_in_rim(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),'M CM D CD C XC L XL X IX V IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result

def input_num():
  num = input('Введите натуральное число: ')
  return num

n = input_num()
while not n.isdigit(): 
    print('\nВнимание!!! Вы ввели не натуральное число!!!!\n')
    n = input_num()

print(f'\nЧислу {n} соответствует римское число {arab_in_rim(int(n))}')

"""
**Задание 4**
"""

def is_balanced(text, brackets="()[]{}"):
    opening, closing = brackets[::2], brackets[1::2]
    stack = []
    for character in text:
        if character in opening:
            stack.append(opening.index(character))
        elif character in closing:
            if stack and stack[-1] == closing.index(character):
                stack.pop()
            else:
                return False
    return (not stack)

is_balanced('(dfff))')

"""
**Задание 5**
"""

def prov(num1,num2):
  if all(ch=='0' or ch=='1' for ch in num1+num2): return True
  else: return False

def input_num():
  num1,num2 = input('Введите первое бинарное число: '), input('Введите второе бинарное число: ')
  return num1,num2

num1_2,num2_2 = input_num()

while not prov(num1_2,num2_2):
  print('\nВнимание!!! Вы ввели не бинарные числа!!!!\n')
  num1_2,num2_2 = input_num()

num_mult_10 = int(num1_2,2) * int(num2_2,2)
num_mult_2 = bin(num_mult_10)[2:]
print(f'\nПроизведение {num1_2} на {num2_2} равно {num_mult_2}')
