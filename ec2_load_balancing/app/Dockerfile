FROM python:slim-buster
WORKDIR /app
COPY ["app/requirements.txt","./"]
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]