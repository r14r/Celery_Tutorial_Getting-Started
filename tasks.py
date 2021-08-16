from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)
 
@app.task
def add(x, y):
    return x + y

@app.task
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)