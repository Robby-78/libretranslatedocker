FROM python:3.9-slim
WORKDIR /app
RUN git clone https://github.com/LibreTranslate/LibreTranslate .
RUN pip install -e .
CMD ["libretranslate", "--host", "0.0.0.0", "--port", "${PORT}"]
