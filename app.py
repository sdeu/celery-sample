from pyworker.tasks import render, combine
from celery import chord

def main():
    #render.delay()

    chord(render.s() for i in range(10))(combine.s()).get()

if __name__ == "__main__":
    main()