FROM python:3.10-slim

WORKDIR /sqlite_streamlit

RUN mkdir data
RUN mkdir logs
RUN touch logs/create_table_app.log

COPY requirements.txt requirements.txt
COPY db_util.py db_util.py
COPY app.py app.py
COPY query_app.py query_app.py
COPY create_table_app.py create_table_app.py

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
