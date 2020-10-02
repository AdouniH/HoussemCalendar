FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /mr_houssem
WORKDIR /mr_houssem
COPY . /mr_houssem/
RUN pip install -r requirements.txt
CMD python /mr_houssem/backend/CalendarProject/manage.py runserver 0.0.0.0:8000
