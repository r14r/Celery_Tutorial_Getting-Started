import sys
import time
import click

from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)
 
from tasks import add, fib

@click.command()
@click.argument('op')
@click.argument('par1', default='1')
@click.argument('par2', default='1')
def main(op, par1, par2):
    if (op == "add"):
        task=add.delay(int(par1), int(par2))
    elif (op == "fib"):
        task=fib.delay(int(par1))
    elif (op == "get"):
        task = app.AsyncResult(par1)
    else:
        print(f"Task: {op} not implemented")
        sys.exit(1)

    print(f"Task: task={task}, ready={task.ready()}")
        

    if task.ready():
        result = task.get(timeout=1)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()