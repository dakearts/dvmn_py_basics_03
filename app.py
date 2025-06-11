import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

email = """%heading%

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

heading = "%heading%"
website = "%website%"
friend_name = "%friend_name%"
sender_name = "%my_name%"
email_from = "serg.chelsea@yandex.ru"
email_to = "dakearts@yandex.ru"

email = email.replace(heading, f"""From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";""")
email = email.replace(website, "https://dvmn.org/profession-ref-program/")
email = email.replace(friend_name, 'Максим')
email = email.replace(sender_name, 'Серёжа')
email = email.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
server.login(login, password)
server.sendmail(email_from, email_to, email)
server.quit()
