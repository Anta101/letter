import smtplib
import os
from dotenv import load_dotenv

load_dotenv('method.env')
DATABASE_LOGIN  = os.getenv('DATABASE_LOGIN')
YA_PASSWORD = os.getenv('YA_PASSWORD')
letter = """\
From: {from_email}
To: {to_email}
Subject: Приглашение
Content-Type: text/plain; charset="UTF-8;

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!
{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 
Регистрируйся → {website} 
На курсы, которые еще не вышли, можно подписаться и получить уведомление
о релизе сразу на имейл.""".format(from_email = 'devmanorg@yandex.ru', to_email= 'anta01@yandex.ru', friend_name ='Ivan', my_name ='Devman', website ='https://dvmn.org/profession-ref-program/')
letter = letter.encode('UTF-8')
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(DATABASE_LOGIN, YA_PASSWORD)
server.sendmail(DATABASE_LOGIN, 'anta01@yandex.ru', letter)

server.quit()
