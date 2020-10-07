FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /mr_houssem
COPY . /mr_houssem/
RUN pip install -r /mr_houssem/requirements.txt
WORKDIR /mr_houssem/CalendarProject
RUN chmod +x /mr_houssem/backend-entrypoint.sh
CMD bash /mr_houssem/backend-entrypoint.sh
