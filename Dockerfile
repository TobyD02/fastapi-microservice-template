FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENTRYPOINT ["uvicorn", "public.index:app", "--host", "0.0.0.0", "--port", "80", "--reload"]