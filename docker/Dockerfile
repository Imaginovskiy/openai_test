FROM python:3.10-alpine
ADD requirements.txt /
ADD app.py /
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python", "./app.py"]