
import config
import logging
import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from base import SQL  # подключение класса SQL из файла base

db = SQL('db.db')  # соединение с БД

bot = Bot(token=config.TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

#inline клавиатура
buttons = [
        [InlineKeyboardButton(text="Да", callback_data="yes")]
    ]
kb = InlineKeyboardMarkup(inline_keyboard=buttons)

buttons2 = [
        [InlineKeyboardButton(text="Прокачка силы✊", callback_data="uppowers")],
        [InlineKeyboardButton(text="Прокачка ловкости🏃", callback_data="uplovkost")],
        [InlineKeyboardButton(text="Дуэли и битвы⚔️", callback_data="duelibitva")],
    ]
kb2 = InlineKeyboardMarkup(inline_keyboard=buttons2)

buttons3 = [
        [InlineKeyboardButton(text="Битвы с животными", callback_data="pvpanimals")],
        [InlineKeyboardButton(text="Тренировка на мишенях", callback_data="trenmish")]
    ]
kb3 = InlineKeyboardMarkup(inline_keyboard=buttons3)

buttons4 = [
        [InlineKeyboardButton(text="Уклонение от предмета", callback_data="yklonpredmet")]
         ]
kb4 = InlineKeyboardMarkup(inline_keyboard=buttons4)

buttons5 = [
        [InlineKeyboardButton(text="Битва с гоблином", callback_data="bgoblin")],
        [InlineKeyboardButton(text="Битва с темным рыцарем", callback_data="btemrizar")],
        [InlineKeyboardButton(text="Битва с светлым рыцарем", callback_data="bsvetrizar")],
        [InlineKeyboardButton(text="Битва с Боссом", callback_data="boss")],
         ]
kb5 = InlineKeyboardMarkup(inline_keyboard=buttons5)

buttons6 = [
        [InlineKeyboardButton(text="Лево", callback_data="left")],
        [InlineKeyboardButton(text="Центр", callback_data="center")],
        [InlineKeyboardButton(text="Право", callback_data="right")],
    ]
kb6 = InlineKeyboardMarkup(inline_keyboard=buttons6)

buttons7 = [
        [InlineKeyboardButton(text="Информация обо мне", callback_data="infome")],
        [InlineKeyboardButton(text="Прокачки", callback_data="proka")],
        [InlineKeyboardButton(text="Магазин", callback_data="magaz")],
    ]
kb7 = InlineKeyboardMarkup(inline_keyboard=buttons7)


buttons9 = [
        [InlineKeyboardButton(text="Главное меню", callback_data="glavmenu")]
         ]
kb9 = InlineKeyboardMarkup(inline_keyboard=buttons9)
buttons11 = [
        [InlineKeyboardButton(text="Возродится", callback_data="vozr")],
        [InlineKeyboardButton(text="Магазин", callback_data="magaz")]
    ]
kb11 = InlineKeyboardMarkup(inline_keyboard=buttons11)
buttons12 = [
        [InlineKeyboardButton(text="Магазин", callback_data="magaz")]
    ]
kb12 = InlineKeyboardMarkup(inline_keyboard=buttons12)
buttons13 = [
    [InlineKeyboardButton(text="Аптечка   [100]", callback_data="apt")],
    [InlineKeyboardButton(text="Броня   [100]", callback_data="bron")]
    ]
kb13 = InlineKeyboardMarkup(inline_keyboard=buttons13)
buttons14 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="apt_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb14 = InlineKeyboardMarkup(inline_keyboard=buttons14)
buttons15 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="bron_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb15 = InlineKeyboardMarkup(inline_keyboard=buttons15)
#когда пользователь написал сообщение
@dp.message()
async def start(message):
    id = message.from_user.id
    if not db.user_exist(id):  # если пользователя нет в бд
        db.add_user(id)  # добавляем
    status = db.get_field("users", id, "status")  # получаем статус пользователя
    if status == 0:
        await message.answer(
            "Привет👋 я главный лесник этого леса. Лес восстал! Магия древних деревьев пробудила животных, и теперь они яростно😡 защищают свои земли🏞. Тебе предстоит пробиваться⚔️ через суровый лес, сражаясь с огромными волками, взбешенными медведями. Используй оружие чтобы выжить и добраться до сердца леса, и заполучить спрятанные сокровища💰."
            "Ты готов оставить информацию о себе?",reply_markup=kb)
    status = db.get_field("users", id, "status")
    if status >=2:
         await message.answer("Главное меню:", reply_markup=kb7)
         #db.update_field("users", id, "status", 1) #изменяем статус пользователя
    #await message.answer("Выбери вариант!", reply_markup=kb2)#отправка сообщения с клавиатурой
    if status == 1:
        name = message.text
        db.update_field("users", id, "name", name)
        #name = db.get_field("users", id, "name")
        #hp = db.get_field("users", id, "hp")
        #power = db.get_field("users", id, "power")
        #lovkost = db.get_field("users", id, "lovkost")
        #yudacha = db.get_field("users", id, "yudacha")
        #brona = db.get_field("users", id, "brona")
        #await message.answer(f"Вот информация о тебе: \nИмя: {name}\nЗдоровье❤️: {hp}\nСила✊: {power}\nЛовкость🏃: {lovkost}\nУдача🤞: {yudacha}\nБроня🛡: {brona}")
        db.update_field("users", id, "status", 2)
        await message.answer("Главное меню:", reply_markup=kb7)
#когда пользователь нажал на inline кнопку
@dp.callback_query()
async def start_call(call):
    id = call.from_user.id
    if not db.user_exist(id):#если пользователя нет в бд
        db.add_user(id)#добавляем
    status = db.get_field("users", id, "status")  # получаем статус пользователя
    if call.data == "yes":
        await call.answer("Введите свое имя!")
        db.update_field("users", id, "status", 1)
    if call.data == "uppowers":
        await call.message.answer("Хороший выбор! Давай приступим!", reply_markup=kb3)
        db.update_field("users", id, "status", 2)
    if call.data == "uplovkost":
        await call.message.answer("Хороший выбор! Давай приступим!", reply_markup=kb4)
        db.update_field("users", id, "status", 3)
    if call.data == "duelibitva":
        await call.message.answer("Хороший выбор! Давай приступим!", reply_markup=kb5)
        db.update_field("users", id, "status", 4)
    if call.data == "trenmish":
        db.update_field("users", id, "status", 2)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Мишень стоит тебе надо попасть по ней! Куда будем стрелять?", reply_markup=kb6)
    if call.data in ["left", "center", "right"] and status == 2:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            power = db.get_field("users", id, "power")
            power -= 1
            db.update_field("users", id, "lovkost", power)
            await call.message.answer(f"Ты попал по мишени!+1 сила! Твоя сила: {power}", reply_markup=kb9)
            return
        else:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
    if call.data == "pvpanimals":
        db.update_field("users", id, "status", 2)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! животное стоит тебе надо попасть по нему! Куда будем стрелять?", reply_markup=kb9)
        return
    if call.data in ["pvpaleft", "pvpacenter", "pvparight"] and status == 2:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            power = db.get_field("users", id, "power")
            power -= 1
            db.update_field("users", id, "lovkost", power)
            await call.message.answer(f"Ты попал по животному!+1 сила! Твоя сила: {power}", reply_markup=kb9)
            return
        else:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
    if call.data == "yklonpredmet":
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Противник кинул в тебя булыжник! Куда будешь уклоняться",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status==3:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            lovkost = db.get_field("users", id, "lovkost")
            lovkost -= 1
            db.update_field("users", id, "lovkost", lovkost)
            await call.message.answer(f"Ты не уклонился от булыжника!-1 ловкость! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
        else:
            lovkost = db.get_field("users", id, "lovkost")
            lovkost += 1
            db.update_field("users", id, "lovkost", lovkost)
            await call.message.answer(f"Ты уклонился от булыжника!+1 ловкость! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
    if call.data == "bgoblin":
        db.update_field("users", id, "status", 5)
        db.update_field("users", id, "hp_goblin", 50)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
    if call.data in ["left","center","right"] and status==5:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            await call.message.answer("Ты попал!")
            db.update_field("users", id, "status", 6)
            d = 10 + random.randint(5,15)
            hp_goblin = db.get_field("users", id, "hp_goblin")
            yron = hp_goblin - d
            await call.message.answer(f"Вы снесли гоблину {d}хп")
            db.update_field("users", id, "hp_goblin", yron)
            await call.message.answer("Теперь твоя задача уклонится от атаки гоблина! Куда будем уклонятся?",reply_markup=kb6)
            db.update_field("users", id, "status", 6)
        hp_goblin = db.get_field("users", id, "hp_goblin")
        if hp_goblin <= 0:
            await call.message.answer("Гоблин был повержен! Ты получаешь +20 к силе, +30 к ловкости, +5 к удаче, +1000 к балансу!", reply_markup=kb9)
            power = db.get_field("users", id, "power")
            lovkost = db.get_field("users", id, "lovkost")
            yudacha = db.get_field("users", id, "yudacha")
            money = db.get_field("users", id, "money")
            power +=20
            lovkost +=30
            yudacha +=5
            money +=1000
            db.update_field("users", id, "power", power)
            db.update_field("users", id, "lovkost", lovkost)
            db.update_field("users", id, "yudacha", yudacha)
            db.update_field("users", id, "money", money)
        else:
            await call.message.answer("Ты промазал!")
            db.update_field("users", id, "status", 6)
            await call.message.answer("Теперь твоя задача уклонится от атаки гоблина! Куда будем уклонятся?",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status == 6:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            d = 10 + random.randint(-5, 5)
            hp = db.get_field("users", id, "hp")
            await call.message.answer(f"Вы не уклонились от атаки гоблина! -{d}")
            yron = hp - d
            db.update_field("users", id, "status", 5)
            db.update_field("users", id, "hp", yron)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        hp = db.get_field("users", id, "hp")
        if hp <= 0:
            await call.message.answer("Вы мертв! Вы можете возродится, но при возрождении все ваши ресурсы и навыки будут потеряны, или можете купить зелье излечения в магазине!", reply_markup=kb11)
        else:
            await call.message.answer("Вы уклонились от атаки гоблина!")
            db.update_field("users", id, "status", 5)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        return

    if call.data == "btemrizar":
        hp = db.get_field("users", id, "hp")
        if hp < 100:
            await call.message.answer("Вам может не хватить хп для битвы нужно выличиться в магазине", reply_markup=kb12)
            return
        power = db.get_field("users", id, "power")
        if power < 50:
            await call.message.answer("Твоя сила мала минимально 50 силы для запуска!", reply_markup=kb9)
            return
        lovkost = db.get_field("users", id, "lovkost")
        if lovkost < 50:
            await call.message.answer("Твоя ловкость мала минимально 50 ловкости для запуска!", reply_markup=kb9)
        db.update_field("users", id, "status", 7)
        db.update_field("users", id, "hp_temric", 75)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
    if call.data in ["left","center","right"] and status==7:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            await call.message.answer("Ты попал!")
            db.update_field("users", id, "status", 8)
            d = 10 + random.randint(10,15)
            hp_temric = db.get_field("users", id, "hp_temric")
            yron = hp_temric - d
            await call.message.answer(f"Вы снесли рыцарю {d}хп")
            db.update_field("users", id, "hp_temric", yron)
            await call.message.answer("Теперь твоя задача уклонится от атаки рыцаря! Куда будем уклонятся?",reply_markup=kb6)
        hp_temric = db.get_field("users", id, "hp_temric")
        if hp_temric <= 0:
            await call.message.answer("Рыцарь был повержен! Ты получаешь +50 к силе, +50 к ловкости, +15 к удаче, +3000 к балансу!", reply_markup=kb9)
            power = db.get_field("users", id, "power")
            lovkost = db.get_field("users", id, "lovkost")
            yudacha = db.get_field("users", id, "yudacha")
            money = db.get_field("users", id, "money")
            power +=50
            lovkost +=50
            yudacha +=15
            money +=3000
            db.update_field("users", id, "power", power)
            db.update_field("users", id, "lovkost", lovkost)
            db.update_field("users", id, "yudacha", yudacha)
            db.update_field("users", id, "money", money)
        else:
            await call.message.answer("Ты промазал!")
            db.update_field("users", id, "status", 8)
            await call.message.answer("Теперь твоя задача уклонится от атаки рыцаря! Куда будем уклонятся?",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status == 8:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            d = 10 + random.randint(-2, 5)
            hp = db.get_field("users", id, "hp")
            await call.message.answer(f"Вы не уклонились от атаки рыцаря! -{d}")
            yron = hp - d
            db.update_field("users", id, "status", 7)
            db.update_field("users", id, "hp", yron)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        hp = db.get_field("users", id, "hp")
        if hp <= 0:
            await call.message.answer("Вы мертв! Вы можете возродится, но при возрождении все ваши ресурсы и навыки будут потеряны, или можете купить зелье излечения в магазине!", reply_markup=kb11)
        else:
            await call.message.answer("Вы уклонились от атаки рыцаря!")
            db.update_field("users", id, "status", 7)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        return




    if call.data == "bsvetrizar":
        hp = db.get_field("users", id, "hp")
        if hp < 100:
            await call.message.answer("Вам может не хватить хп для битвы нужно выличиться в магазине", reply_markup=kb12)
            return
        power = db.get_field("users", id, "power")
        if power < 80:
            await call.message.answer("Твоя сила мала минимально 80 силы для запуска!", reply_markup=kb9)
            return
        lovkost = db.get_field("users", id, "lovkost")
        if lovkost < 80:
            await call.message.answer("Твоя ловкость мала минимально 80 ловкости для запуска!", reply_markup=kb9)
        db.update_field("users", id, "status", 9)
        db.update_field("users", id, "hp_swetric", 75)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
    if call.data in ["left","center","right"] and status==9:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            await call.message.answer("Ты попал!")
            db.update_field("users", id, "status", 10)
            d = 10 + random.randint(10,20)
            hp_swetric = db.get_field("users", id, "hp_swetric")
            yron = hp_swetric - d
            await call.message.answer(f"Вы снесли рыцарю {d}хп")
            db.update_field("users", id, "hp_swetric", yron)
            await call.message.answer("Теперь твоя задача уклонится от атаки рыцаря! Куда будем уклонятся?",reply_markup=kb6)
        hp_swetric = db.get_field("users", id, "hp_swetric")
        if hp_swetric <= 0:
            await call.message.answer("Рыцарь был повержен! Ты получаешь +75 к силе, +75 к ловкости, +25 к удаче, +5000 к балансу!", reply_markup=kb9)
            power = db.get_field("users", id, "power")
            lovkost = db.get_field("users", id, "lovkost")
            yudacha = db.get_field("users", id, "yudacha")
            money = db.get_field("users", id, "money")
            power +=75
            lovkost +=75
            yudacha +=25
            money +=5000
            db.update_field("users", id, "power", power)
            db.update_field("users", id, "lovkost", lovkost)
            db.update_field("users", id, "yudacha", yudacha)
            db.update_field("users", id, "money", money)
        else:
            await call.message.answer("Ты промазал!")
            db.update_field("users", id, "status", 10)
            await call.message.answer("Теперь твоя задача уклонится от атаки рыцаря! Куда будем уклонятся?",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status == 10:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            d = 10 + random.randint(-2, 5)
            hp = db.get_field("users", id, "hp")
            await call.message.answer(f"Вы не уклонились от атаки рыцаря! -{d}")
            yron = hp - d
            db.update_field("users", id, "status", 9)
            db.update_field("users", id, "hp", yron)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        hp = db.get_field("users", id, "hp")
        if hp <= 0:
            await call.message.answer("Вы мертв! Вы можете возродится, но при возрождении все ваши ресурсы и навыки будут потеряны, или можете купить зелье излечения в магазине!", reply_markup=kb11)
        else:
            await call.message.answer("Вы уклонились от атаки рыцаря!")
            db.update_field("users", id, "status", 9)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        return
    if call.data == "boss":
        db.update_field("users", id, "hp", 1000)
        db.update_field("users", id, "hp_boss", 1500)
        db.update_field("users", id, "status", 11)
        await call.message.answer("Отлично! В этом режиме у тебя 1000 хп, а у Босса 1000 в целом как и у тебя. Твой урон варируется от 50 до 300, а его атака варируется от 75 до 150")
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
    if call.data in ["left","center","right"] and status==11:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            await call.message.answer("Ты попал!")
            db.update_field("users", id, "status", 12)
            d = 50 + random.randint(0,150)
            hp_boss = db.get_field("users", id, "hp_boss")
            yron = hp_boss - d
            await call.message.answer(f"Вы снесли Боссу {d}хп")
            db.update_field("users", id, "hp_boss", yron)
            await call.message.answer("Теперь твоя задача уклонится от атаки Босса! Куда будем уклонятся?",reply_markup=kb6)
        hp_boss = db.get_field("users", id, "hp_boss")
        if hp_boss <= 0:
            await call.message.answer("Босс был повержен! Ты получаешь +100 к силе, +100 к ловкости, +35 к удаче, +10000 к балансу!", reply_markup=kb9)
            power = db.get_field("users", id, "power")
            lovkost = db.get_field("users", id, "lovkost")
            yudacha = db.get_field("users", id, "yudacha")
            money = db.get_field("users", id, "money")
            power +=100
            lovkost +=100
            yudacha +=35
            money +=10000
            db.update_field("users", id, "power", power)
            db.update_field("users", id, "lovkost", lovkost)
            db.update_field("users", id, "yudacha", yudacha)
            db.update_field("users", id, "money", money)
        else:
            await call.message.answer("Ты промазал!")
            db.update_field("users", id, "status", 12)
            await call.message.answer("Теперь твоя задача уклонится от атаки Босса! Куда будем уклонятся?",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status == 12:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            d = 75 + random.randint(0, 75)
            hp = db.get_field("users", id, "hp")
            await call.message.answer(f"Вы не уклонились от атаки Босса! -{d}")
            yron = hp - d
            db.update_field("users", id, "status", 11)
            db.update_field("users", id, "hp", yron)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        hp = db.get_field("users", id, "hp")
        if hp <= 0:
            await call.message.answer("Вы мертв! Вы можете возродится, но при возрождении все ваши ресурсы и навыки будут потеряны, или можете купить зелье излечения в магазине!", reply_markup=kb11)
        else:
            await call.message.answer("Вы уклонились от атаки Босса!")
            db.update_field("users", id, "status", 11)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        return




    if call.data == "infome":
        name = db.get_field("users", id, "name")
        hp = db.get_field("users", id, "hp")
        power = db.get_field("users", id, "power")
        lovkost = db.get_field("users", id, "lovkost")
        yudacha = db.get_field("users", id, "yudacha")
        brona = db.get_field("users", id, "brona")
        money = db.get_field("users", id, "money")
        await call.message.answer(f"Вот информация о тебе: \nИмя: {name}\nЗдоровье❤️: {hp}\nСила✊: {power}\n Ловкость🏃: {lovkost}\nУдача🤞: {yudacha}\nБроня🛡: {brona}\nБаланс💰: {money}")
    if call.data == "proka":
        await call.message.answer("Давай приступим", reply_markup=kb2)
    if call.data == "glavmenu":
        await call.message.answer("Главное меню", reply_markup=kb7)
    if call.data =="vozr":
       db.del_user(id)
       await call.message.answer(
           "Привет👋 я главный лесник этого леса. Лес восстал! Магия древних деревьев пробудила животных, и теперь они яростно😡 защищают свои земли🏞. Тебе предстоит пробиваться⚔️ через суровый лес, сражаясь с огромными волками, взбешенными медведями. Используй оружие чтобы выжить и добраться до сердца леса, и заполучить спрятанные сокровища💰."
           "Ты готов оставить информацию о себе???", reply_markup=kb)
    if call.data == "magaz":
        await call.message.answer("Вот товары имеющиеся в магазине:", reply_markup=kb13)
    if call.data == "apt":
        await call.message.answer(f"Аптечка прибовляет 10хп \n Подтвердить???", reply_markup=kb14)
    if call.data == "apt_yes":
        await call.message.answer("Успешно", reply_markup=kb12)
        db.update_field("users", id, "hp", (db.get_field("users", id, "hp"))+10)
        db.update_field("users", id, "money", (db.get_field("users", id, "money")-100))
    if call.data == "bron":
        await call.message.answer(f"Броня прибовляет 10хп \n Подтвердить???", reply_markup=kb15)
    if call.data == "bron_yes":
        await call.message.answer("Успешно", reply_markup=kb12)
        db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+10)
        db.update_field("users", id, "money", (db.get_field("users", id, "money")-100))
    if call.data == "no":
        await call.message.answer("Успешно отклонено!", reply_markup=kb9)







    #if call.data == "yes": проверка нажатия на кнопку
    #await call.answer("Оповещение сверху")
    #await call.message.answer("Отправка сообщения")
    #await call.message.edit_text("Редактирование сообщения")
    #await call.message.delete()#удаление сообщения
    await bot.answer_callback_query(call.id)#ответ на запрос, чтобы бот не зависал

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
