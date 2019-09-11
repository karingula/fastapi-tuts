FROM python:3.7.4-slim
LABEL version="1.0"
LABEL description="Example Image"
LABEL maintainer="Vijay Karingula"
RUN apt-get -y update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install python3-dev python3-setuptools
#===App requirements===#
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /fastapi-tuts
WORKDIR /fastapi-tuts
EXPOSE 8000
ENTRYPOINT [ "uvicorn" ]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]
