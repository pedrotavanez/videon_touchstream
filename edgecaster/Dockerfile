# FROM python:3
FROM python:3.8-slim-buster

WORKDIR /usr/src/app/code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY api api/
COPY conf conf/
COPY python_parser python_parser/
COPY handler.py .
COPY helpers helpers/

ENTRYPOINT ["python", "/usr/src/app/code/handler.py"]

