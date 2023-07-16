from celery import Celery


app = Celery('kernel', broker="amqp://guest:guest@localhost:5672/")
