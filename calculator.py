class CashCalculator:
    def __init__(self, limit):
        self.limit = limit
        self.spent = 0.0

    def add_record(self, amount):
        self.spent += float(amount)

    def get_remainder(self):
        return round(self.limit - self.spent, 2)

    def report(self):
        remainder = self.get_remainder()

        if remainder == 0:
            return 'Денег нет, держись'
        if remainder > 0:
            return f'На сегодня осталось {remainder} руб.'
        return f'Денег нет, держись: твой долг - {abs(remainder)} руб.'


if __name__ == '__main__':
    limit = float(input('Введите дневной лимит (руб.): '))
    calc = CashCalculator(limit)

    print('Вводите траты по одной. Пустая строка — конец ввода.')
    while True:
        amount_str = input('Сумма траты (руб., или Enter для завершения): ')
        if not amount_str.strip():
            break
        calc.add_record(amount_str)

    print(calc.report())
