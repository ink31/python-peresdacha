import datetime
import sys

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

def get_status_color(status):
    if status == 'past':
        return RED
    elif status == 'current':
        return GREEN
    else:
        return BLUE

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

def main():
    today = datetime.date.today()
    try:
        with open('tasks_data.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Файл tasks_data.txt не найден")
        return

    print("=== Список задач ===\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Теперь делим строку всего на 2 части: дата и описание
        parts = line.split(maxsplit=1)
        if len(parts) < 2:
            continue
        date_str, description = parts
        
        try:
            task_date = parse_date(date_str)
        except ValueError:
            continue
        
        # Считаем разницу в днях
        delta = (task_date - today).days
        
        # Сами автоматически определяем статус по дням:
        if delta < 0:
            status = 'past'
            days_ago = -delta
            output = f"Прошло {days_ago} дней от {description}"
        elif delta == 0:
            status = 'current'
            output = f"Прямо щаз происходит {description}"
        else: # если delta > 0
            status = 'future'
            output = f"Осталось {delta} дней до {description}"
        
        # Красим в нужный цвет в зависимости от вычисленного статуса
        color = get_status_color(status)
        print(f"{color}{output}{RESET}")

if __name__ == '__main__':
    main()
