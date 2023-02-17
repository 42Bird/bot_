# tg bot API 5549838211:AAFOBdRyPbbM0OV_-xiSEvFdEyMlugmJJrU


import telebot
import time
import os
import sqlite3
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
import lxml
import re
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve
import shutil
from transliterate import translit
from telebot import types
import telebot
from urllib.request import urlopen



# Создаем экземпляр бота
bot = telebot.TeleBot('5549838211:AAFOBdRyPbbM0OV_-xiSEvFdEyMlugmJJrU')

MAX_RETIES = 20
PASSWORD = '123'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message: str, res=False) -> str:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("ВОЕННЫЕ ПРЕСТУПНИКИ")
            btn2 = types.KeyboardButton("БАТАЛЬОН РЕВАНШ")
            btn3 = types.KeyboardButton("72 ЦИПСО")
            btn4 = types.KeyboardButton("16 ЦИПСО")
            btn5 = types.KeyboardButton("УЧАСТНИКИ АТО")
            btn6 = types.KeyboardButton("СБУ")
            btn7 = types.KeyboardButton("ГУР")
            btn8 = types.KeyboardButton("СВР УКРАИНЫ")
            btn9 = types.KeyboardButton("ПОЛК АЗОВ")
            btn10 = types.KeyboardButton("БАТАЛЬОН ДОНБАСС")
            btn11 = types.KeyboardButton("БАТАЛЬОН ТОРНАДО")
            btn12 = types.KeyboardButton("БАТАЛЬОНЫ АЙДАР, АСКЕР, ДНЕПР-1")
            btn13 = types.KeyboardButton("НАЦ. КОРПУС")
            btn14 = types.KeyboardButton("ПРАВЫЙ СЕКТОР")
            btn15 = types.KeyboardButton("УЛЬТРАС ФК")
            btn16 = types.KeyboardButton("ПАТРИОТЫ УКРАИНЫ, ПРАВОРАДИКАЛЫ")
            btn17 = types.KeyboardButton("ИНОСТРАННЫЕ НАЕМНИКИ")
            btn18 = types.KeyboardButton("IT ARMY OF UA")
            btn19 = types.KeyboardButton("SAVE UA")
            btn20 = types.KeyboardButton("КИБЕРВОЙСКА УКРАИНЫ")
            
            
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18,btn19,btn20)
            bot.send_message(message.chat.id, text="Информационно-поисковая система 'Марс'", reply_markup=markup)            
            bot.send_message(message.chat.id, text="Схема расположения региональных отделений националистических организаций на территории Украины", reply_markup=markup)

            bot.send_photo(message.chat.id, photo=open('map.jpg', 'rb'))
            bot.send_message(message.chat.id, text="Участие укронационалистов в антиправительственных митингах", reply_markup=markup)
            bot.send_photo(message.chat.id, photo=open('naz2.jpg', 'rb'))
            bot.send_photo(message.chat.id, photo=open('naz1.jpg', 'rb'))
            bot.send_message(message.chat.id, text="Введите ИМЯ, ФАМИЛИЯ ИМЯ, ФАМИЛИЯ ИМЯ ОТЧЕСТВО, а также возможен ввод рода деятельности, номера телефона, адреса проживания, должности, социальных сетей и даты рождения военнослужащего Украины для поиска", reply_markup=markup)
            bot.send_message(message.chat.id, text="Для начала работы с ботом введите ключ", reply_markup=markup)


            
@bot.message_handler(content_types=["text"])
def handle_text(message: str) -> str:

        if (message.text != PASSWORD):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, text="ДОСТУП ЗАПРЕЩЕН", reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, text="Начните поиск", reply_markup=markup)
            
            @bot.message_handler(content_types=["text"])
            def handle_text(message: str) -> str:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
                name = message.text
                ### nemezida
                
                url = f"https://nemez1da.ru/?s={name}"
                
                response = requests.get(url, allow_redirects = True,headers={
                "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                })



                soup = BeautifulSoup(response.text, 'lxml')
                PAGE_NUMBERS = []
                for page in soup.find_all('a', class_='page-numbers'):
                    PAGE_NUMBERS.append(page.text)
                try:
                    PAGE_NUMBERS.pop(-1)
                    PAGE_NUMBERS.pop(0)
                    print(PAGE_NUMBERS[-1])
                except:
                    pass
                
                
                    
                url = f"https://nemez1da.ru/?s={name}"
                
                response = requests.get(url, allow_redirects = True,headers={
                "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                })



                soup = BeautifulSoup(response.text, 'lxml')
                
                links = []

                for link in soup.find_all('a', class_='simple-grid-grid-post-thumbnail-link'):
                                links.append(link.get('href'))

                if links == []:
                                bot.send_message(message.chat.id, text="Не найдено. Попробуйте другой запрос или запрос на украинском языке", reply_markup=markup) 

                        #
                for link in links:
                                response = requests.get(link, allow_redirects = True, headers={
                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                        })

                                soup = BeautifulSoup(response.text, 'lxml')
                                
                                name_tag = soup.find('h1')
                                name = name_tag.text
                                
                                #bot.send_message(message.chat.id, text=f"{name}", reply_markup=markup)

                                category_tag = soup.find(rel = 'category tag')
                                #bot.send_message(message.chat.id, text=f"{category_tag.text}", reply_markup=markup)
                             
                                
                                info_tag = soup.find('div', class_ = 'entry-content simple-grid-clearfix')
                            
                                #bot.send_message(message.chat.id, text=f"{info_tag.text}", reply_markup=markup)
                            
                                ### html


                                f = open(f'{name} {category_tag.text}.html', 'w',  encoding="cp1251")
                                html_template = f"""
                                                            <html>
                                                            <head>
                                                            <title>{name} {category_tag.text} </title>
                                                            </head>
                                                            <body>
                                                            <h2>{name}</h2>
                                                            <h3>{category_tag.text}</h3>
                                                            <p>Информация</p>
                                                            
                                                            
                                                            <p></p>
                                                            
                                                            {info_tag.text}







                                                            </body>
                                                            </html>


                                        """
                                f.write(html_template)
                                f.close()
                                bot.send_document(message.chat.id, document = open(f'{name} {category_tag.text}.html','rb'))


                                ### html
                                
                                # Загружаем картинки
                                pictures = []

                                try:
                                        img = soup.find("div", {"class": "photos_single_place"}).find("img")
                                        print(img["data-src"])
                                        pictures.append(img["data-src"])
                                except:
                                        pass
                                
                                try:
                                        p = requests.get(pictures[0], allow_redirects = True,headers={
                                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                                        })
                                        out = open("img.jpg", "wb")
                                        out.write(p.content)
                                        bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'))
                                       
                                                
                                        out.close()
                                except:
                                        pass

                                try:
                                        p = requests.get(pictures[1], allow_redirects = True,headers={
                                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
                                        })
                                        out = open("img.jpg", "wb")
                                        out.write(p.content)
                                        bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'))
                                                
                                        out.close()
                                except:
                                        pass











            ### Солнцепек
            
            HTMLFILE = open("messages.html", "r", encoding = 'utf8')
            index = HTMLFILE.read()
            SP = BeautifulSoup(index, 'lxml')
            SP_MAS = SP.find_all("div", class_="message default clearfix")
            for i in SP_MAS:
                if (f"{name}" in i.text):
                    
                    
                    
                    f = open(f'{name}_SP.html', 'w',  encoding="cp1251")
                    html_template = f"""
                                                <html>
                                                <head>
                                                <title>{name}</title>
                                                </head>
                                                <body>
                                                <h2>{i.text[55:]}</h2>
                                                
                      



                                                </body>
                                                </html>


                            """
                    f.write(html_template)
                    f.close()
                    bot.send_document(message.chat.id, document = open(f'{name}_SP.html','rb'))
            
        
                
                
# Запускаем бота
bot.polling(none_stop=True, interval=0)
