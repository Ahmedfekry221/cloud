FROM python:alpine
WORKDIR /app
COPY . /app
RUN pip install nltk
RUN python -m nltk.downloader stopwords
CMD ["python", "code.py"]

