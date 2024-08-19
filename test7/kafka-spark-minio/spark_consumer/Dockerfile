FROM bitnami/spark:latest

USER root

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY consumer.py .

CMD ["/opt/bitnami/spark/bin/spark-submit", "--master", "spark://spark-master:7077", "--conf", "spark.executor.memory=1g", "/app/consumer.py"]
