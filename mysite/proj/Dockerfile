FROM python:3.9.14-alpine3.16
USER root
COPY . .
# RUN apk update && pip install --upgrade pip && 
RUN pip install bandit pylint
ENTRYPOINT ["python", "analyze.py"]
 
