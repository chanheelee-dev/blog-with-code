FROM python:3.10-slim

WORKDIR /sqlite_streamlit

# Create directories and files
RUN mkdir data
RUN touch data/default.db
RUN mkdir logs
RUN touch logs/create_table_app.log

# Copy files and codes
COPY requirements.txt requirements.txt
COPY db_util.py db_util.py
COPY app.py app.py
COPY query_app.py query_app.py
COPY create_table_app.py create_table_app.py

# Install the required packages
RUN pip install -r requirements.txt

# Expose the port where the app will run
EXPOSE 8501

# Run the app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
