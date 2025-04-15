from huey.contrib.djhuey import task

from .methods import do_something


@task()
def task_do_something():
    do_something()
