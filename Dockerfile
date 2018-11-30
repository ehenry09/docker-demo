FROM python:3.7
COPY . /app
RUN pip install seaborn
CMD ["python", "/app/scripts/make-plot.py"]