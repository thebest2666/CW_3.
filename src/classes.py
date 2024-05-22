from datetime import datetime


class Operation:
    def __init__(
            self,
            state,
            date,
            amount,
            corrency_name,
            description,
            from_,
            to
    ):
        self.state = state
        self.date = date
        self.amount = amount
        self.corrency_name = corrency_name
        self.description = description
        self.from_ = from_ if from_ is not None else ""
        self.to = to

    def convert_date(self):
        """
        Задаем правильный формат даты
        """
        iso_date = datetime.fromisoformat(self.date)
        return iso_date.strftime("%d.%m.%Y")

    def convert_payment(self, payment_info):
        """
        Маскируем номер карты
        """
        info = payment_info.split(" ")
        number_card = info.pop(-1)
        if payment_info.startswith("Счет"):
            number_card = "**" + number_card[-4:]
        elif not payment_info:
            number_card = ""
        else:
            number_card = number_card[:6] + "******" + number_card[-4:]
            number_card = "".join([number_card[i:i+4] for i in range(0, len(number_card), 4)])
        info.append(number_card)
        return " ".join(info)

    def __lt__(self, other):
        """
        Задаем правило сортировки
        """
        return self.date < other.date

    def __gt__(self, other):
        """
        Задаем правило сортировки
        """
        return self.date > other.date

    def __str__(self):
        """
        Выводим сообщение об операции
        """
        from_ = self.convert_payment(self.from_)
        delimiter = " -> " if from_ else ""
        return (
            f"{self.convert_date()} {self.description}\n"
            f"{from_}{delimiter}{self.convert_payment(self.to)}\n"
            f"{self.amount} {self.corrency_name}"
        )
