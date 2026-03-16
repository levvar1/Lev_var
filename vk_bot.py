from vkbottle.bot import Bot,Message
TOKEN="vk1.a.ef9k3UeoZSCBh_y0AWx8AMolStyxxsPaP05RS1p-r5eNiccSiK-J_Z3HHuE_ViCcMJ7UcyUznQtMF9sucBXh6prtVWBW3BsOLwQgxN2BtRxdu1FYVsmntkPtfn1gdwiIBCwDUC8sJsYmh-CgugKe563VumZWR0hVWp40ADqVplQbbqArCulDnfod_jFmmvcbcHe_Mhjfb2Mk480X1rz-3g"

bot=Bot(TOKEN)
#команда start
@bot.on.message(text="/start")
async def start_handler(message:Message):
    await message.answer("ПРивет я твой первый бот в ВК")
#ответ на любое сообщение
@bot.on.message(text="Привет")
async def hi_handler(message:Message):
    user_id=message.from_id
    await message.answer(f"И тебе привет id пользователя {user_id}")
#обработка остального текста
@bot.on.message()
async def any_message(message:Message):
    text=message.text
    if text:
        await message.answer(f"ты написал {text} молодец ")
if __name__=="__main__":
    print("бот запущен")
    bot.run_forever()