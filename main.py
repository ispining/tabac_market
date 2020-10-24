import telebot
from telebot import TeleBot
from functools import wraps
import config
from telebot import types
import os

welcome_text = "ברוכים הבאים לבוט הפרסום של קבוצת הסיגריות. \n\n🧐איך זה עובד?🧐\nפשוט תשלחו את הפרסום שלכם לבוט והוא מיד יופיע בערוץ. \n\n לא הגבלנו בפרסומים, אבל המגזים בכמויות הפרסומים - יחסם."
bot = telebot.TeleBot(config.token)

banned_users = []



print("\n\n Bot name:    @TABAC_MARKET\n")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, welcome_text)
    if message.from_user.username == None:
        bot.send_message(message.chat.id,  'לשימוש בבוט יש להגדיר שם משמש (יוזרניים)')
    elif message.from_user.username is not None:
        bot.send_message(message.chat.id, 'שלח תמונה עם כיתוב (בהודעה אחת)')






@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    if message.chat.id == message.from_user.id & message.chat.id not in banned_users:
        global photo
        global mention
        user_id = message.from_user.username
        mention = "'https://t.me/'+str(user_id)"
        if message.caption is not None :
            if message.photo != 0 :
                photo = message.photo[-1].file_id
                keyboard = types.InlineKeyboardMarkup()
                button_geza = types.InlineKeyboardButton(text="🌐מעבר לבוט הגזע🌐", url="https://t.me/ge420za_bot")
                button_mention = types.InlineKeyboardButton(text="👈פניה לסוחר👉", url="https://t.me/"+str(user_id))
                # button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
                keyboard.add(button_mention)
                keyboard.add(button_geza)
                bot.send_photo(config.chat_idr, photo, caption=message.caption+"\nשם הסוחר: @"+message.from_user.username, reply_markup=keyboard)
                bot.send_message(message.chat.id, "המודעה נשלחה בהצלחה!")
                print("\nAction:    --New post--")
                print("\nUsername:  --@" + user_id + "--")
                print("Post text:   " + message.caption)
                print("#############################################")
        else:
            bot.send_message(message.chat.id, "תמונה ללא טקסט אינה מתקבלת. נסה שנית...")
    else:
        bot.send_message(message.chat.id, "הינך חסום במערכת.\nלביטול החסימה יש לפנות ל @big420boss")



if __name__ == '__main__':
    bot.polling(none_stop=True)
    while True:
        try:
            logging.info("Bot running..")
            bot.polling(none_stop=True, interval=2)

            # Предполагаю, что бот может мирно завершить работу, поэтому
            # даем выйти из цикла
            break
        except telebot.apihelper.ApiException as e:
            logging.error(e)
            bot.stop_polling()

            time.sleep(15)

            logging.info("Running again!")

