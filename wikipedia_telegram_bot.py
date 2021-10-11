import logging
# logging.basicConfig(level=logging.INFO)
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '2087063434:AAGi4cUR1GADJUUv0XeR8aKRehfURn-qeog'
wikipedia.set_lang('uz')
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alekum wikipedia botga xush kelibsiz")
@dp.message_handler()
async def wikesend (message: "type.message"):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("kechirasiz Dilshodbek bu mavzuga oid wikipedia topilmadi" )





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
