FROM python:3
RUN git clone https://github.com/temPLAY333/Listas_Diccionario
WORKDIR /Listas_Diccionario
RUN pip install -r requirements.txt
CMD ["python3" ,"-m",  "unittest"]