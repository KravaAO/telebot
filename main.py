from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "5468320241:AAGIueJH96ydg5I22A-7je42MMgzOLXyalc"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

#@dp.message_handler()
#async def echo(message: types.Message):
#	await message.answer(text = message.text)

#@dp.message_handler()						#добавление верхнего регистра 
#async def echo_upper(message: types.Message):
#	await message.answer(text = message.text.upper())

@dp.message_handler()						#если слов больше чем одно
async def echo(message: types.Message):
	if message.text.count (' ') >=1:
		await message.answer(text = message.text)	
	


if __name__ == '__main__':
	print("vrode working")
	executor.start_polling(dp)
	








