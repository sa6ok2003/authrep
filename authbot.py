from pyrogram import Client,filters,types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

my_id = 44520977
id_chat= '-518604271'

@app.on_message(filters.command('b'))
async def echo (client,message):
    if message.from_user.id == my_id:
        id_user = message.chat.id
        try:
            await app.add_chat_members(chat_id=id_chat,user_ids=id_user)
            await app.send_message(chat_id=message.chat.id, text='Добавил тебя в чат')
        except:
            await app.send_message(chat_id=message.chat.id, text='Не могу тебя добавить в чат так как тебя '
                                                                 'запрещено добавлять в беседы\n'
                                                                 'Что бы это исправить переходи в настройки, нажимай\n\n'
                                                                 '- Конфидециальность\n'
                                                                 '- Группы и каналы\n'
                                                                 'И добавь меня в список тех, кто тебя может приглашать в группы\n\n'
                                                                 'После этого напиши мне  и мы повторим попытку')


@app.on_message(filters.text)
async def payments (client,message):
    if message.from_user.id == my_id and message.text == 'Рр':
        await app.edit_message_text(message_id=message.message_id,chat_id=message.chat.id,text=
                                    '🇷🇺Если ты с РФ\n'
                                    '4817760152002113\n'
                                    'Вадим Сергеевич Л.\n\n\n'
                                    '🇰🇬Если с Кыргызстана\n'
                                    'Mbank online : 996552152071\n'
                                    'На мобильный банкинг не единицами, не на баланс, только мбанкинг, любой банкомат подойдет, можно очень просто, заплатить) Чек ( фото или скрин, обязательно, отправить мне!!!)\n\n\n'
                                    '🇺🇿Если ты с Узбекистана:\n'
                                    'uzcard - 8600 1204 2026 7414\n'
                                    'AKSENOVA ANGELINA\n\n\n'
                                    '🇰🇿Казахстан КАСПИ - +77088338356\n\n\n'
                                    '🥝Так же ты можешь оплатить на киви ( Неважно с какой ты страны):\n'
                                    '+79183561047\n\n'
                                    '💰Юмани(ЯндексДеньги), неважно с какой страны :\n'
                                    '410019301888334\n\n\n'
                                    '<b>Сумма для оплаты :</b>\n'
                                    'Для РФ - 354р\n'
                                    'Для Кыргызстана - 407 сом\n'
                                    'Для Узбекистана - 50 150 сум\n'
                                    'Для Казахстана - 2005 тенге\n\n'
                                    'Чек сюда, после проверки добавлю в чат!',parse_mode='html')

app.run()