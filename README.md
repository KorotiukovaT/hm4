# Homework 4

Створити FastAPI додаток, який буде отимувати данні з NIST про CVE та виводити їх користувачеві.

## Встановлення та запуск

Щоб налаштувати середовище для цього проекту, виконайте наступні кроки:
```Bash 

cd hm4/
python3 -m venv env
env\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=src uvicorn src.main:app --reload  
```