FROM python:3.10-alpine

WORKDIR /app
ENV PATH="/src:${PATH}"

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "src/main.py"]