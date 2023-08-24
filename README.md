# Python Camera Monitoring Service

## Описание

Эта программа предназначена для мониторинга доступности IP-камер. Она использует пинг для проверки доступности каждой камеры и отправляет уведомления в Telegram, если камера становится недоступной или снова доступна.

## Особенности

- Проверка доступности IP-камер через пинг.
- Отправка уведомлений в Telegram.
- Отслеживание времени, когда камера стала недоступной или снова доступна.
- Логирование ошибок и событий.

## Установка

### Зависимости

- Python 3.7+
- aiogram

Установите необходимые зависимости с помощью pip:

```bash
pip install -r requirements.txt

Замените YOUR_TOKEN на ваш токен бота Telegram.
Замените CHAT_ID1, CHAT_ID2, CHAT_ID3 на ID чатов, в которые будут отправляться уведомления.


![image](https://github.com/ValentinPundikov/CheckCameras/assets/74809607/c557c56d-d45a-4a03-8a70-b5cf662586c4)

