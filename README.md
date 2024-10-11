[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/dnftm_dev)
[![Static Badge](https://img.shields.io/badge/Telegram-Support-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/erbesteratu)

# 🎨 NotPx.APP - Автофарм Not Pixel 🎨

> [!WARNING]
> Я не несу ответственности за ваши аккаунты. Пожалуйста, учитывайте потенциальные риски перед использованием этого бота!

> [!IMPORTANT]
> [!] Данный скрипт закрашивает пиксели ПО ТРАФАРЕТУ! Это позволяет получать +8 БОНУСНЫХ $PX за каждое закрашивание!
> [+] Краткая инструкция по установке и использованию : [telegra.ph](https://telegra.ph/NotPxAPP--autofarm-10-04)
> [+] Инструкция по замене трафарета на свой : [telegra.ph](https://telegra.ph/Kak-dobavit-svoj-trafaret-v-skript-10-11)

# 🔥🔥 Используйте PYTHON версии 3.10 🔥🔥


## Функционал  
|                  Функционал                   | Поддерживается |
|:---------------------------------------------:|:--------------:|
|                Многопоточность                |       ✅        | 
|           Привязка прокси к сессии            |       ✅        | 
|          Поддержка pyrogram .session          |       ✅        |
| Авто-регистрация аккаунта по вашему реф. коду |       ✅        |
|                  Авто таски                   |       ✅        |
|                Авто рисование ПО ТРАФАРУТУ ( +8PX )                 |       ✅        |
|                 Авто апгрейд                  |       ✅        |
|               Авто сбор наград               |       ✅        |


## Настройки ( указываются в файле config.env )

|                     Настройки                     |                                                          Описание                                                           |
|:-------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
|               **API_ID / API_HASH**               |                     Данные платформы, с которой будет запущена сессия Telegram                  |
|            **USE_RANDOM_DELAY_IN_RUN**            |                                                     Использование задержки перед запуском сессии ( True \ False )                                                  |
|              **RANDOM_DELAY_IN_RUN**              |                                Задержка перед запуском сессии ( в секундах, от и до )   
|             **SLEEP_TIME_IN_MINUTES**             |                        Рандомная задержка в минутах между цыклами (по умолчанию - [20, 40, 60, 80])                         |
|                    **USE_REF**                    |                      Регистрировать ваши аккаунты по вашей реф. ссылке или нет (по умолчанию - False)                       |
|                    **REF_ID**                     |                           Ваш реферальный аргумент (идет после app/startapp? в вашей реф. ссылке)                           |
|              **USE_PROXY_FROM_FILE**              |                           Использовать ли прокси из файла `bot/config/proxies.txt` (True / False)                           |
|               **ENABLE_AUTO_TASKS**               |                                 Включить ли автоматическое выполнение тасков (True / False)                                 |
|               **ENABLE_AUTO_DRAW**                |                                  Включить ли автоматическое выполнение игр (True / False)                                   |
|            **ENABLE_JOIN_TG_CHANNELS**            |                             Включить ли автоматическое подключение к тг каналам (True / False)                              |
|              **ENABLE_CLAIM_REWARD**              |                                   Включить ли автоматический збор ревардов (True / False)                                   |
|              **ENABLE_AUTO_UPGRADE**              |                                     Включить ли автоматический апгрейд  (True / False)                                      |
|                  **ENABLE_SSL**                   | Включить проверку ssl сертификатов (думаю может помочь с решением SSL: CERTIFICATE_VERIFY_FAILED ошибки)  (default - False) |

## Быстрый старт 📚

Для быстрой установки и последующего запуска - запустите файл run.bat

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/) **версии 3.10**

## Получение API ключей
1. Перейдите на сайт [my.telegram.org](https://my.telegram.org) и войдите в систему, используя свой номер телефона.
2. Выберите **"API development tools"** и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `.env`, предоставленные после регистрации вашего приложения.
