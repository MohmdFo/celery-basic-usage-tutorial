import time

from celery import Celery


app = Celery('kernel', broker="amqp://guest:guest@localhost:5672/")


@app.task(name='worker.add')
def add(num1, num2):
    time.sleep(5)
    return num1 + num2
