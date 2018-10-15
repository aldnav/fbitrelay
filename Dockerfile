FROM python:3.6.6-alpine3.8

ADD requirements.txt /
RUN pip --no-cache-dir install -r requirements.txt
ADD main.py /

EXPOSE 8888

CMD ["python", "main.py"]