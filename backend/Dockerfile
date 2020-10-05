FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /mr_houssem
COPY . /mr_houssem/
RUN pip install -r /mr_houssem/requirements.txt
WORKDIR /mr_houssem/CalendarProject
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
