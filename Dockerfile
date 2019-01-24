FROM python:3
RUN pip3 install flask
COPY ./app.py /app.py
ENTRYPOINT ["./app.py"]
