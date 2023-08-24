
import subprocess
import time
import asyncio
from aiogram import Bot
from datetime import datetime
import logging

# Настройка логирования
logging.basicConfig(filename='camera_check.log', level=logging.INFO)

TOKEN = "TOKEN"
CHAT_IDS = ["111111111", "222222222"]

async def ping_camera(ip_address):
    try:
        response = subprocess.check_output(['ping', '-n', '1', ip_address], stderr=subprocess.STDOUT, universal_newlines=True)
        if "Превышен интервал ожидания для запроса." in response:
            return False
        else:
            return True
    except subprocess.CalledProcessError:
        return False

async def send_telegram_message(bot, chat_id, message):
    try:
        await bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения в чат {chat_id}: {e}")

async def main():
    cameras = {
        "192.168.1.2":"АЗС-01",
        "192.168.2.2":"АЗС-02",
    }

    camera_status = {ip: True for ip in cameras.keys()}
    camera_status_time = {ip: datetime.now() for ip in cameras.keys()}

    bot = Bot(token=TOKEN)

    while True:
        for ip, identifier in cameras.items():
            is_online = await ping_camera(ip)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if is_online and not camera_status[ip]:
                downtime_duration = camera_status_time[ip].strftime('%Y-%m-%d %H:%M:%S')
                message = f"Камера с идентификатором {identifier} (IP {ip}) снова в сети (была недоступна с {downtime_duration})."
                for chat_id in CHAT_IDS:
                    await send_telegram_message(bot, chat_id, message)
                camera_status[ip] = True
                camera_status_time[ip] = datetime.now()
            elif not is_online and camera_status[ip]:
                message = f"Камера с идентификатором {identifier} (IP {ip}) недоступна с {current_time}."
                for chat_id in CHAT_IDS:
                    await send_telegram_message(bot, chat_id, message)
                camera_status[ip] = False
                camera_status_time[ip] = datetime.now()
        await asyncio.sleep(60)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())