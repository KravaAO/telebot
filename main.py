from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

#HELP_COMMAND = """
#/help - list commands
#/start - start work with the bot
#"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(text = message.text)

#@dp.message_handler()						#добавление верхнего регистра 
#async def echo_upper(message: types.Message):
#	await message.answer(text = message.text.upper())

#@dp.message_handler()						#если слов больше чем одно
#async def echo(message: types.Message):
#	if message.text.count (' ') >=1:
#		await message.answer(text = message.text)


#@dp.message_handler(commands = ['help'])
#async def help_command(message: types.Message):
#	await message.reply(text = HELP_COMMAND)			
	
#@dp.message_handler(commands = ['start'])
#async def help_command(message: types.Message):
#	await message.answer(text = "welcome to the cum zone")
#	await message.delete()			
	

if __name__ == '__main__':
	print("vrode working")
	executor.start_polling(dp)
	








