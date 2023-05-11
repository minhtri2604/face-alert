import telegram
import asyncio
async def send_telegram(photo_path="alert.png"):
    try:
        my_token = "6141891195:AAGaPjPRaW-NXlXV-4bFItzcSiT91KFYT9g"
        bot = telegram.Bot(token=my_token)
        await bot.sendPhoto(chat_id="6221430251", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")
    
asyncio.run(send_telegram())