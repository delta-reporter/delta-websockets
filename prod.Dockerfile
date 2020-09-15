FROM python:3.7.7-alpine as base

FROM base as builder 
RUN mkdir /install
RUN apk update && apk add gcc musl-dev
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt  

FROM base
COPY --from=builder /install /usr/local
ADD . /app
WORKDIR /app
EXPOSE 8080
CMD ["python", "app.py"]
