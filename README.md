# Python-Starlette-REST-Starter (Python 3.6+)
Kick starter to your async REST application.

## How to run in development?
```
cd src
python main.py
```

## How to run in production?
Using gunicorn with uvicorn workers.
```
cd src
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -e ENV=production -b 0.0.0.0:8000
```
