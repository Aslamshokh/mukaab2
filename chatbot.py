"""
Telegram Support Bot - Премиум Система Поддержки (Русская версия)
Полная поддержка всех типов сообщений: текст, фото, видео, документы
Автор: Advanced Python Bot
Версия: 3.0.0 - Русская версия с полной поддержкой медиа
"""

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import time
import logging
import os
from typing import Dict

# ===================== НАСТРОЙКИ =====================
BOT_TOKEN = ""  # Замените на ваш токен от @BotFather
ADMIN_ID =   # Замените на ваш Telegram ID (узнайте у @userinfobot)
YOUR_TELEGRAM_LINK = ""

# Хранилище данных
user_reply_context: Dict[int, int] = {}  # admin_id -> user_id (кому отвечает админ)
active_users: Dict[int, int] = {}  # user_id -> время последнего сообщения

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')

# ===================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =====================
def is_admin(user_id: int) -> bool:
    """Проверка, является ли пользователь администратором"""
    return user_id == ADMIN_ID

def get_premium_text() -> str:
    """Премиум стиль текста на русском"""
    return """
<b>✨ ПРЕМИУМ СИСТЕМА ПОДДЕРЖКИ ✨</b>

<i>⚡ Круглосуточный чат поддержки</i>
<i>🎯 Мгновенные ответы</i>
<i>🔒 Защищенное соединение</i>

<b>━━━━━━━━━━━━━━━━━━</b>
"""

# ===================== КЛАВИАТУРЫ =====================
def get_main_keyboard(user_id: int) -> InlineKeyboardMarkup:
    """Главная клавиатура в зависимости от роли"""
    keyboard = InlineKeyboardMarkup(row_width=2)

    if is_admin(user_id):
        keyboard.add(
            InlineKeyboardButton("📊 Статистика", callback_data="stats"),
            InlineKeyboardButton("👥 Активные чаты", callback_data="active_chats")
        )
        keyboard.add(
            InlineKeyboardButton("📢 Сделать рассылку", callback_data="broadcast"),
            InlineKeyboardButton("⚙️ Настройки", callback_data="settings")
        )
        keyboard.add(
            InlineKeyboardButton("💬 Ответить пользователям", callback_data="answer_users")
        )
    else:
        keyboard.add(
            InlineKeyboardButton("💬 Связаться с поддержкой", callback_data="start_chat"),
            InlineKeyboardButton("ℹ️ О системе", callback_data="info")
        )
        keyboard.add(
            InlineKeyboardButton("📞 Написать админу", url="https://t.me/your_support"),
            InlineKeyboardButton("⭐ Оценить работу", callback_data="rate")
        )

    return keyboard

def get_admin_reply_keyboard(user_id: int) -> InlineKeyboardMarkup:
    """Клавиатура для ответа админа"""
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("✏️ Ответить пользователю", callback_data=f"reply_{user_id}"),
        InlineKeyboardButton("❌ Закрыть диалог", callback_data=f"close_{user_id}")
    )
    keyboard.row(
        InlineKeyboardButton("🚫 Заблокировать", callback_data=f"ban_{user_id}"),
        InlineKeyboardButton("📊 История чата", callback_data=f"history_{user_id}")
    )
    return keyboard

def get_user_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для пользователя"""
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("📝 Новое обращение", callback_data="new_request"),
        InlineKeyboardButton("❌ Закрыть диалог", callback_data="close_dialog")
    )
    keyboard.row(
        InlineKeyboardButton("📊 Статус заявки", callback_data="status"),
        InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")
    )
    return keyboard

# ===================== ОБРАБОТЧИКИ КОМАНД =====================
@bot.message_handler(commands=['start'])
def start_command(message: Message):
    """Приветственное сообщение при /start"""
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name

    welcome_text = f"""
{get_premium_text()}

<b>🌟 Здравствуйте, {username}!</b>

{'<b>👑 РЕЖИМ АДМИНИСТРАТОРА АКТИВИРОВАН</b>' if is_admin(user_id) else '<b>💎 РЕЖИМ ПОЛЬЗОВАТЕЛЯ</b>'}

<i>✨ Премиум система поддержки готова к работе</i>
<i>🔐 Безопасное и защищенное соединение</i>
<i>⚡ Мгновенная пересылка сообщений</i>

<b>━━━━━━━━━━━━━━━━━━</b>
<b>📌 Статус системы:</b>
• Работает: <code>✅ ОНЛАЙН</code>
• Время ответа: <code>&lt;1 секунды</code>
• Безопасность: <code>🔒 TLS 1.3</code>

<i>Выберите действие ниже:</i>
"""

    bot.reply_to(
        message,
        welcome_text,
        reply_markup=get_main_keyboard(user_id)
    )
    logger.info(f"Пользователь {user_id} ({username}) запустил бота")

    # Уведомление админу
    if not is_admin(user_id):
        bot.send_message(
            ADMIN_ID,
            f"{get_premium_text()}\n\n"
            f"<b>🆕 Новый пользователь!</b>\n"
            f"<b>👤 Имя:</b> {username}\n"
            f"<b>🆔 ID:</b> <code>{user_id}</code>\n"
            f"<b>📅 Время:</b> {time.strftime('%H:%M:%S')}"
        )

# ===================== ОБРАБОТЧИКИ КНОПОК =====================
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    """Обработка нажатий на кнопки"""
    user_id = call.from_user.id
    data = call.data

    # Кнопки для пользователей
    if data == "start_chat":
        bot.answer_callback_query(call.id, "💬 Чат поддержки активирован!")
        bot.edit_message_text(
            f"{get_premium_text()}\n\n<b>💬 ЧАТ ПОДДЕРЖКИ</b>\n\n<i>Ваше сообщение будет мгновенно отправлено администратору.</i>\n\n📝 <b>Напишите ваше сообщение ниже:</b>",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=get_user_keyboard()
        )

    elif data == "new_request":
        bot.answer_callback_query(call.id, "✅ Новое обращение создано")
        bot.send_message(
            user_id,
            f"{get_premium_text()}\n\n<b>🆕 НОВОЕ ОБРАЩЕНИЕ</b>\n\n<i>Пожалуйста, опишите вашу проблему:</i>"
        )

    elif data == "close_dialog":
        bot.answer_callback_query(call.id, "🚪 Диалог закрыт")
        if user_id in active_users:
            del active_users[user_id]
        bot.send_message(
            user_id,
            f"{get_premium_text()}\n\n<b>❌ ДИАЛОГ ЗАКРЫТ</b>\n\n<i>Спасибо за обращение в нашу поддержку!</i>\n\n"
            f"Если понадобится помощь - просто напишите мне снова ✨"
        )

    elif data == "status":
        bot.answer_callback_query(call.id, "📊 Статус вашей заявки")
        status_text = f"""
{get_premium_text()}

<b>📊 СТАТУС ОБРАЩЕНИЯ</b>
━━━━━━━━━━━━━━━━━━
<b>Ваш ID:</b> <code>{user_id}</code>
<b>Роль:</b> <code>Пользователь</code>
<b>Активный диалог:</b> <code>{"Да" if user_id in active_users else "Нет"}</code>
<b>Время ответа:</b> <code>~5-10 минут</code>
"""
        bot.send_message(user_id, status_text)

    elif data == "main_menu":
        bot.edit_message_text(
            f"{get_premium_text()}\n\n<b>🏠 ГЛАВНОЕ МЕНЮ</b>",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=get_main_keyboard(user_id)
        )

    elif data == "info":
        bot.answer_callback_query(call.id, "ℹ️ Информация о системе")
        bot.send_message(
            user_id,
            f"{get_premium_text()}\n\n<b>ℹ️ ИНФОРМАЦИЯ О СИСТЕМЕ</b>\n━━━━━━━━━━━━━━━━━━\n"
            f"<b>Версия:</b> <code>3.0.0</code>\n"
            f"<b>Время ответа:</b> <code>&lt;100 мс</code>\n"
            f"<b>Доступность:</b> <code>24/7</code>\n"
            f"<b>Шифрование:</b> <code>Полное</code>\n"
            f"<b>Поддерживаемые форматы:</b> <code>Текст, фото, видео, документы</code>"
        )

    elif data == "rate":
        bot.answer_callback_query(call.id, "⭐ Спасибо за оценку!")
        bot.send_message(
            user_id,
            f"{get_premium_text()}\n\n<b>⭐ ОЦЕНИТЕ НАШУ РАБОТУ</b>\n\n"
            f"<i>Если вам понравилась поддержка, поставьте оценку:</i>\n\n"
            f"<a href='https://t.me/your_support'>⭐ Поставить оценку</a>"
        )

    # Административные функции
    if is_admin(user_id):
        if data == "stats":
            bot.answer_callback_query(call.id, f"Активных чатов: {len(active_users)}")
            bot.send_message(
                user_id,
                f"{get_premium_text()}\n\n<b>📊 СТАТИСТИКА</b>\n━━━━━━━━━━━━━━━━━━\n"
                f"<b>Активных диалогов:</b> <code>{len(active_users)}</code>\n"
                f"<b>Всего пользователей:</b> <code>{len(active_users)}</code>\n"
                f"<b>Статус:</b> <code>🟢 РАБОТАЕТ</code>\n"
                f"<b>Версия бота:</b> <code>3.0.0 PRO</code>"
            )

        elif data == "active_chats":
            if active_users:
                text = f"{get_premium_text()}\n\n<b>👥 АКТИВНЫЕ ЧАТЫ ({len(active_users)})</b>\n━━━━━━━━━━━━━━━━━━\n"
                for uid in list(active_users.keys())[:20]:
                    text += f"<b>Пользователь:</b> <code>{uid}</code>\n"
                bot.send_message(user_id, text)
            else:
                bot.send_message(user_id, f"{get_premium_text()}\n\n<b>📭 Нет активных чатов</b>")

        elif data == "answer_users":
            bot.answer_callback_query(call.id, "💬 Выберите пользователя для ответа")
            if active_users:
                keyboard = InlineKeyboardMarkup()
                for uid in list(active_users.keys())[:10]:
                    keyboard.add(InlineKeyboardButton(f"Пользователь {uid}", callback_data=f"reply_{uid}"))
                bot.send_message(user_id, "Выберите пользователя для ответа:", reply_markup=keyboard)
            else:
                bot.send_message(user_id, "Нет активных пользователей")

        # Ответ пользователю
        elif data.startswith("reply_"):
            target_user_id = int(data.split("_")[1])
            bot.answer_callback_query(call.id, "✏️ Введите ваш ответ:")
            user_reply_context[user_id] = target_user_id
            bot.send_message(
                user_id,
                f"{get_premium_text()}\n\n<b>✏️ ОТВЕТ ПОЛЬЗОВАТЕЛЮ</b>\n━━━━━━━━━━━━━━━━━━\n"
                f"<b>ID пользователя:</b> <code>{target_user_id}</code>\n\n"
                f"<i>Отправьте ваше сообщение. Оно будет доставлено мгновенно.</i>\n\n"
                f"<b>📝 Ваш ответ:</b>"
            )

        # Закрыть диалог
        elif data.startswith("close_"):
            target_user_id = int(data.split("_")[1])
            if target_user_id in active_users:
                del active_users[target_user_id]
            bot.send_message(
                target_user_id,
                f"{get_premium_text()}\n\n<b>🔒 ДИАЛОГ ЗАКРЫТ АДМИНИСТРАТОРОМ</b>\n\n"
                f"<i>Спасибо за обращение! Если нужна помощь - напишите снова.</i>"
            )
            bot.answer_callback_query(call.id, f"✅ Диалог с {target_user_id} закрыт")

# ===================== ОБРАБОТЧИК ВСЕХ СООБЩЕНИЙ =====================
@bot.message_handler(func=lambda message: True, content_types=['text', 'photo', 'video', 'document', 'audio', 'voice'])
def handle_all_messages(message: Message):
    """Обработка всех типов сообщений"""
    user_id = message.from_user.id

    # Если это администратор
    if is_admin(user_id):
        # Проверяем, находится ли админ в режиме ответа пользователю
        if user_id in user_reply_context:
            target_user_id = user_reply_context[user_id]

            try:
                # Пересылаем сообщение пользователю в зависимости от типа
                if message.text:
                    reply_text = f"""
{get_premium_text()}

<b>📩 ОТВЕТ ПОДДЕРЖКИ</b>

━━━━━━━━━━━━━━━━━━
{message.text}
━━━━━━━━━━━━━━━━━━

<i>⚡ Официальный ответ службы поддержки</i>
<b>🕐 {time.strftime('%H:%M:%S')}</b>
"""
                    bot.send_message(target_user_id, reply_text, reply_markup=get_user_keyboard())

                elif message.photo:
                    bot.send_photo(target_user_id, message.photo[-1].file_id,
                                 caption=f"{get_premium_text()}\n\n<b>📩 ОТВЕТ ПОДДЕРЖКИ</b>\n\n<i>⚡ Ответ от администратора</i>",
                                 reply_markup=get_user_keyboard())

                elif message.video:
                    bot.send_video(target_user_id, message.video.file_id,
                                 caption=f"{get_premium_text()}\n\n<b>📩 ОТВЕТ ПОДДЕРЖКИ</b>\n\n<i>⚡ Видео-ответ от администратора</i>",
                                 reply_markup=get_user_keyboard())

                elif message.document:
                    bot.send_document(target_user_id, message.document.file_id,
                                    caption=f"{get_premium_text()}\n\n<b>📩 ОТВЕТ ПОДДЕРЖКИ</b>\n\n<i>⚡ Документ от администратора</i>",
                                    reply_markup=get_user_keyboard())

                elif message.audio:
                    bot.send_audio(target_user_id, message.audio.file_id,
                                 caption=f"{get_premium_text()}\n\n<b>📩 ОТВЕТ ПОДДЕРЖКИ</b>",
                                 reply_markup=get_user_keyboard())

                elif message.voice:
                    bot.send_voice(target_user_id, message.voice.file_id,
                                 caption=f"{get_premium_text()}\n\n<b>📩 ОТВЕТ ПОДДЕРЖКИ</b>",
                                 reply_markup=get_user_keyboard())

                # Подтверждение админу
                bot.reply_to(message, f"✅ <b>Ответ отправлен пользователю {target_user_id}</b>\n\n<i>✓ Сообщение доставлено</i>")

                # Выход из режима ответа
                del user_reply_context[user_id]
                logger.info(f"Админ ответил пользователю {target_user_id}")

            except Exception as e:
                bot.reply_to(message, f"❌ Ошибка при отправке: {str(e)}")
                logger.error(f"Ошибка отправки: {e}")
        else:
            # Админ не в режиме ответа
            bot.reply_to(
                message,
                f"{get_premium_text()}\n\n<b>👑 РЕЖИМ АДМИНИСТРАТОРА</b>\n\n"
                f"<i>Чтобы ответить пользователю, нажмите кнопку 'Ответить' в его сообщении.</i>",
                reply_markup=get_main_keyboard(user_id)
            )

    # Если это обычный пользователь
    else:
        # Сохраняем пользователя как активного
        active_users[user_id] = int(time.time())

        # Получаем информацию о пользователе
        user_name = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name

        # Формируем сообщение для админа
        admin_header = f"""
{get_premium_text()}

<b>🆕 НОВОЕ СООБЩЕНИЕ ОТ ПОЛЬЗОВАТЕЛЯ</b>

━━━━━━━━━━━━━━━━━━
<b>👤 Пользователь:</b> <code>{user_name}</code>
<b>🆔 ID:</b> <code>{user_id}</code>
<b>📅 Время:</b> <code>{time.strftime('%Y-%m-%d %H:%M:%S')}</code>
<b>📱 Тип:</b> <code>{message.content_type}</code>
━━━━━━━━━━━━━━━━━━

<b>💬 Содержание:</b>
"""

        # Отправляем админу в зависимости от типа сообщения
        try:
            if message.text:
                admin_msg = admin_header + f"\n{message.text}\n━━━━━━━━━━━━━━━━━━\n\n<i>👇 Нажмите кнопку для ответа</i>"
                bot.send_message(ADMIN_ID, admin_msg, reply_markup=get_admin_reply_keyboard(user_id))

            elif message.photo:
                admin_msg = admin_header + "\n📸 <b>Пользователь отправил фото</b>\n━━━━━━━━━━━━━━━━━━\n\n<i>👇 Нажмите кнопку для ответа</i>"
                bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=admin_msg,
                              reply_markup=get_admin_reply_keyboard(user_id))

            elif message.video:
                admin_msg = admin_header + "\n🎥 <b>Пользователь отправил видео</b>\n━━━━━━━━━━━━━━━━━━\n\n<i>👇 Нажмите кнопку для ответа</i>"
                bot.send_video(ADMIN_ID, message.video.file_id, caption=admin_msg,
                              reply_markup=get_admin_reply_keyboard(user_id))

            elif message.document:
                admin_msg = admin_header + f"\n📄 <b>Документ:</b> {message.document.file_name}\n━━━━━━━━━━━━━━━━━━\n\n<i>👇 Нажмите кнопку для ответа</i>"
                bot.send_document(ADMIN_ID, message.document.file_id, caption=admin_msg,
                                 reply_markup=get_admin_reply_keyboard(user_id))

            else:
                admin_msg = admin_header + f"\n<b>Получено сообщение типа: {message.content_type}</b>\n━━━━━━━━━━━━━━━━━━\n\n<i>👇 Нажмите кнопку для ответа</i>"
                bot.send_message(ADMIN_ID, admin_msg, reply_markup=get_admin_reply_keyboard(user_id))

            # Подтверждение пользователю
            confirm_text = f"""
{get_premium_text()}

<b>✅ СООБЩЕНИЕ ОТПРАВЛЕНО</b>

<i>Ваше сообщение доставлено в службу поддержки.</i>
<b>⏱ Ожидаемое время ответа:</b> <code>~5-10 минут</code>

<i>Вы получите уведомление, когда администратор ответит.</i>

<b>📌 Тип сообщения:</b> <code>{message.content_type}</code>
"""

            bot.reply_to(message, confirm_text, reply_markup=get_user_keyboard())
            logger.info(f"Сообщение от {user_name} ({user_id}) переслано админу")

        except Exception as e:
            bot.reply_to(message, f"❌ Ошибка: {str(e)}\nПожалуйста, попробуйте позже.")
            logger.error(f"Ошибка пересылки: {e}")

# ===================== ЗАПУСК БОТА =====================
def main():
    """Запуск бота"""
    print("=" * 50)
    print("🚀 ЗАПУСК ПРЕМИУМ БОТА ПОДДЕРЖКИ (РУССКАЯ ВЕРСИЯ)")
    print("=" * 50)
    print(f"📱 Версия: 3.0.0")
    print(f"👑 ID Админа: {ADMIN_ID}")
    print(f"✅ Поддерживаемые форматы: текст, фото, видео, документы")
    print("=" * 50)

    logger.info("🚀 Запуск премиум бота поддержки...")

    # Удаляем вебхук
    try:
        bot.remove_webhook()
        print("✅ Вебхук удален")
    except Exception as e:
        print(f"⚠️ Ошибка удаления вебхука: {e}")

    # Уведомление админу
    try:
        bot.send_message(
            ADMIN_ID,
            f"{get_premium_text()}\n\n<b>🚀 БОТ ЗАПУЩЕН!</b>\n\n"
            f"<b>Статус:</b> <code>🟢 РАБОТАЕТ</code>\n"
            f"<b>Версия:</b> <code>3.0.0 PRO</code>\n"
            f"<b>Время запуска:</b> <code>{time.strftime('%Y-%m-%d %H:%M:%S')}</code>\n\n"
            f"<b>🌍 Поддерживаемые форматы:</b>\n"
            f"✓ Текст\n✓ Фото\n✓ Видео\n✓ Документы\n✓ Аудио\n✓ Голосовые\n\n"
            f"<i>✅ Бот готов к работе!</i>"
        )
        print("✅ Уведомление отправлено админу")
    except Exception as e:
        print(f"❌ Ошибка отправки уведомления админу: {e}")

    # Запуск polling
    print("🔄 Запуск бесконечного polling...")
    print("✅ Бот работает! Нажмите Ctrl+C для остановки")
    print("=" * 50)

    while True:
        try:
            bot.infinity_polling(timeout=60, skip_pending=True)
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            print("🔄 Перезапуск через 5 секунд...")
            time.sleep(5)

if __name__ == "__main__":
    main()
