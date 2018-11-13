FROM 'python:3.7.1-alpine3.8'
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD main.py /
EXPOSE 8080
CMD python main.py

