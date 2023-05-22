from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
import emoji

storage=MemoryStorage()

BOT_TOKEN = '5738307243:AAEPQL075EFOZfxYEpUJYbt9-S7AW8UK2AY'
    
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

b1 = KeyboardButton('Первый корпус')
b2 = KeyboardButton('Второй корпус')
b3 = KeyboardButton('Третий корпус')


kb_client_korpus= ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

kb_client_korpus.add(b1).add(b2).add(b3)

b11 = KeyboardButton('1 этаж (первый корпус)')
b22 = KeyboardButton('2 этаж (первый корпус)')
b33 = KeyboardButton('3 этаж (первый корпус)')
b44 = KeyboardButton('4 этаж (первый корпус)')
b55 = KeyboardButton('5 этаж (первый корпус)')

kb_client_floor = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_client_floor.add(b11).add(b22).add(b33).add(b44).add(b55)

photo1 = open('photos/1floor.jpg', 'rb')
photo2 = open('photos/2floor.jpg', 'rb')
photo3 = open('photos/3floor.jpg', 'rb')
photo4 = open('photos/4floor.jpg', 'rb')
photo5 = open('photos/5floor.jpg', 'rb')

@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    await message.reply(text=("Привет " + emoji.emojize(":waving_hand:") + "\n \nЗаблудился в университете? Я помогу."),reply_markup=kb_client_korpus)

@dp.message_handler(lambda message: message.text == 'Первый корпус')
async def answer_to_korpus_main(message: types.Message):
    await message.reply('Напиши номер нужного этажа в ответом сообщении.', reply_markup=kb_client_floor)

@dp.message_handler(lambda message: message.text == 'Второй корпус')
async def answer_to_korpus_error1(message: types.Message):
    await message.reply('Упс… В скором времени добавим твой корпус.')

@dp.message_handler(lambda message: message.text == 'Третий корпус')
async def answer_to_korpus_error2(message: types.Message):
    await message.reply('Упс… В скором времени добавим твой корпус.')

@dp.message_handler(lambda message: message.text == '1 этаж (первый корпус)')
async def answer_to_korpus_floor1(message: types.Message):
    await message.reply('Держи карту со всеми аудиториями.')
    await bot.send_photo(message.from_user.id, photo1)

@dp.message_handler(lambda message: message.text == '2 этаж (первый корпус)')
async def answer_to_korpus_floor2(message: types.Message):
    await message.reply('Держи карту со всеми аудиториями.')
    await bot.send_photo(message.from_user.id, photo2)

@dp.message_handler(lambda message: message.text == '3 этаж (первый корпус)')
async def answer_to_korpus_floor3(message: types.Message):
    await message.reply('Держи карту со всеми аудиториями.')
    await bot.send_photo(message.from_user.id, photo3)

@dp.message_handler(lambda message: message.text == '4 этаж (первый корпус)')
async def answer_to_korpus_floor4(message: types.Message):
    await message.reply('Держи карту со всеми аудиториями.')
    await bot.send_photo(message.from_user.id, photo4)

@dp.message_handler(lambda message: message.text == '5 этаж (первый корпус)')
async def answer_to_korpus_floor5(message: types.Message):
    await message.reply('Держи карту со всеми аудиториями.')
    await bot.send_photo(message.from_user.id, photo5)





executor.start_polling(dp, skip_updates=True)