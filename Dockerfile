FROM python:3.6.4-jessie
COPY . /var/www/django_chat

RUN cd /var/www/django_chat && \
    pip install -r requirements.txt