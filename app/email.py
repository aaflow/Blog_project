from flask_mail import Message
from app import app, mail
from flask import render_template
from threading import Thread


def send_async_email(app, msg):  # функция асинхронной отправки сообщений (отправка в отдельном потоке)
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_password_reset_email(user):  # на входе пользователь, определённый по введённой в форме почте
    token = user.get_reset_password_token()
    send_email('[Blog] Reset Your Password',
               sender=app.config['ADMINS'][0],      # отправитель
               recipients=[user.email],             # получатель
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))


# отправка пользователю user_to уведомления о появлении интересующего его сообщения
def send_email_notification(user_from, user_to, post):
    """
    user_from: тот, кто запостил сообщение на стене
    user_to: пользователь, кому отправится письмо
    post: сообщение, которое написал user_from
    """
    send_email('[Blog] {} wrote a post'.format(user_from.username),
               sender=app.config['ADMINS'][0],
               recipients=[user_to.email],
               text_body='Post from Blog user',
               html_body=render_template('email/post_notification.html',
                                         user_from=user_from, user_to=user_to, post=post))


'''
def send_email(subject, sender, recipients, text_body, html_body):  # функция, отправляющая письмо
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
'''