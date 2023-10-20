money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
sum_ = money_capital + salary
while sum_ > 0:
    ost = sum_ - spend
    count += 1
    sum_ = ost + salary
    spend = spend * ((1 + increase)**(count-1))
print("Количество месяцев, которое можно протянуть без долгов:", count)
