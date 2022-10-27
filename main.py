from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API

HELP_COMMAND = """
<b>/help</b> - <em>list commands</em>
<b>/start</b> - <em>start work with the bot</em>
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
						 one_time_keyboard=True)# для использования кнопки единожды
kb.add(KeyboardButton('/help'))

async def on_startup(_):
	print("vrode working")

#@dp.message_handler()
#async def echo(message: types.Message):
#	await message.answer(text = message.text)

#@dp.message_handler()						#добавление верхнего регистра 
#async def echo_upper(message: types.Message):
#	await message.answer(text = message.text.upper())

#@dp.message_handler()						#если слов больше чем одно
#async def echo(message: types.Message):
#	if message.text.count (' ') >= 1:
#		await message.answer(text = message.text)


@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
	await message.reply(text = HELP_COMMAND,
						parse_mode = "HTML",
						reply_markup = ReplyKeyboardRemove())# удаление кнопки при ее первом использовании
	
@dp.message_handler(commands = ['start'])
async def help_command(message: types.Message):
	await message.answer(text = "welcome to the cum zone",
						 parse_mode = "HTML",
						 reply_markup = kb)
	await message.delete()

#@dp.message_handler()
#async def check(message: types.Message):#ищет цифры символы слова в сообщении
#	if '0' in message.text:
#		return await message.reply('есть 0')
#	await message.reply ('нету')

@dp.message_handler()
async def echo(message: types.Message):
	await bot.send_message(chat_id = message.chat.id,
						   text = "stfu")#если заменить chat.id на .from_user сообщения из группы будут отправляться мне
	


if __name__ == '__main__':
	executor.start_polling(dp, on_startup = on_startup, skip_updates=True)
	








