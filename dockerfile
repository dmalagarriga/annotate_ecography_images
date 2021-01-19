FROM python:3.6
LABEL maintainer "Daniel Malagarriga <https://dmalagarriga.github.io>"
WORKDIR /
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./ ./
EXPOSE 8050
CMD ["python", "./index.py"]
