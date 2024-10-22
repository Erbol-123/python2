from aiogram import types, Bot,executor,Dispatcher
from datas import add_to_db,show_user

api = '7295955633:AAEyfoycpAtPZ4B2wqPO88bdLVuIFkGIjIo'
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    admin_id =  6538857550

    if sms.from_user.id==admin_id:
        await sms.answer(text='Salem admin')

        @dp.message_handler(text='reklama')
        async def send_ad(mess:types.Message):
            if mess.from_user.id==admin_id:
             a = await show_user()
             for i in a:
                await bot.send_message(
                    chat_id=i[0],
                    text=f'Bul reklama {i[1]}'
                )

        @dp.message_handler(text='count_of_users')
        async def send_count(ess:types.Message):
            if ess.from_user.id==admin_id:
                a = await show_user()
                await sms.answer(text=len(a))

    else:
        await add_to_db(id=sms.from_user.id,
                        name=sms.from_user.first_name,
                        username=sms.from_user.username)
        await sms.answer(text='Salem')



if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)