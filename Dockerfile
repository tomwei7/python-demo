FROM python:2.7
COPY . /testapp
WORKDIR /testapp
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python", "app.py"]
