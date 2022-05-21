# Parser Autelpilot

Парсинг сайта  [www.autelpilot.com](https://www.autelpilot.com/)

## Что делает

Извлекает из сайта ссылки, ссылки отбираются по определенному критерию.  
Полученные данные записывает в таблицу Excel

## Как пользоваться

_Предварительно должен быть установлен Python, Pip, система управления версиями Git_

1. `git clone https://github.com/Evgeny-TechnoNinja/parser-autelpilot.git`
2. `cd parser-autelpilot`
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `pip install --upgrade pip`
7. `cd app`
8. `python parser.py`

*Результат работы смотреть в каталоге output, который появится в каталоге parser-autelpilot*
