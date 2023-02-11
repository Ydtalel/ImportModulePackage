from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
from tkinter import *

if __name__ == '__main__':
    current_date_time = datetime.today()
    print(current_date_time)
    get_employees()
    calculate_salary()

# Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией. При желании можно написать программу с этим пакетом.  /// готовый проект на tkinter есть тут https://github.com/Ydtalel/passgen
