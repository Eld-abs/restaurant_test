FROM python:3.12

WORKDIR /app

COPY requirements/ ./requirements

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements/dev.txt

COPY . .

EXPOSE 8005

CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]