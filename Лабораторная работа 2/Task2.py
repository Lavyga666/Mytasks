salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0


# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
for count in range(months):
    ost = salary - spend
    money_capital += abs(ost)
    spend += spend * (increase)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
