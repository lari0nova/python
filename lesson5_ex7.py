# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


import json

profit = {}
profit_av = {}

with open('text_7.txt', 'r', encoding="utf-8") as file_7:
    aver = 0
    y = 0
    for line in file_7:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if (int(earning) - int(damage)) > 0:
            aver = aver + (int(earning) - int(damage))
            y = y + 1
    aver = aver / y
    profit_av['average_profit'] = aver
    print(profit, profit_av)

with open("profit_file.json", "w") as write_file:
    json.dump([profit, profit_av], write_file, ensure_ascii=False, indent=4, separators=(", ", " : "))
