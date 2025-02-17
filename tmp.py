import asyncio
import time
import requests

async def send_mail(num):
    print(f'Улетело сообщение {num}')
    await asyncio.sleep(1)  # Имитация отправки сообщения по сети
    print(f'Сообщение {num} доставлено')


async def main():
    tasks = [send_mail(i) for i in range(10)]
    await asyncio.gather(*tasks)


start_time = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {time.time() - start_time} с')

import requests


api_url = 'http://numbersapi.com/43'

response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)  # При другом коде ответа выводим этот код