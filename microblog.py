from app import app, db
from app.models import User, Post

import logging
from logging.handlers import SMTPHandler


if not app.debug:
	if app.config['MAIL_SERVER']:
		auth = None
		if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
			auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
		secure = None
		if app.config['MAIL_USE_TLS']:
			secure = ()
		mail_handler = SMTPHandler(                                        # отправка лога с ошибкой
			mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
			fromaddr='no-reply@' + app.config['MAIL_SERVER'],
			toaddrs=app.config['ADMINS'], subject='Blog Failure',
			credentials=auth, secure=secure)
		mail_handler.setLevel(logging.ERROR)
		app.logger.addHandler(mail_handler)


@app.shell_context_processor     # создание контекста оболочки, который добавляет экземпляр и модели бд в сеанс оболочки
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
	# app.run(host='localhost', port=5000)
	# app.run(host='10.55.130.176', port=5000)
	# app.run(host='10.55.130.54', port=5000)
	app.run(host='192.168.0.102', port=5000)


"""
Использование SMTP-сервера отладки от Python
(venv) $ python -m smtpd -n -c DebuggingServer localhost:8025

Устанавливаем переменные:  
export MAIL_SERVER=localhost и  export MAIL_PORT=8025

запускаем приложение, при появлении ошибки, будет отправлена c no-reply@localhost на ADMINS


Для отправки на настоящую почту надо установить: (будет падать на ADMINS) (надо активировать окружение venv)

export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-gmail-username>   # 
export MAIL_PASSWORD=<your-gmail-password>   # 


"""
