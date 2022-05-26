FROM python:3.8

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install --no-cache-dir \
    gunicorn \


COPY . /app

EXPOSE 5000

CMD ["python3", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:5002", "--certfile", "/etc/letsencrypt/live/tbriggserver.co.uk-0001/fullchain.pem", "--keyfile", "/etc/letsencrypt/live/tbriggserver.co.uk-0001/privkey.pem", "app:app", "--timeout", "120"]