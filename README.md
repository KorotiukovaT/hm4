# hm4

## для запуску проекту потрібно активувати середовище venv

"""
Можливі помилки
PowerShell встановлена політика заборони запуску скриптів
Вирішення:

Тимчасова зміна політики виконання: (Діє лише на поточну сесію)
- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
"""

- env\Scripts\activate
- uvicorn main:app --reload