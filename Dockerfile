FROM python:3

RUN git clone https://github.com/porollansantiago/sudoku-comp.git
COPY requirements.txt /sudoku-comp
WORKDIR /sudoku-comp

RUN pip install -r requirements.txt

CMD ["python3", "./main.py"]