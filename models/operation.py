from datetime import datetime


class Operation:
    def __init__(
            self,
            pk: int,
            state: str,
            date: str,
            operation_amount: dict,
            description: str,
            _from: str,
            _to: str
    ):
        self.pk = pk
        self.state = state
        self.date = self.convert_date(date)
        self.operation_amount = operation_amount
        self.description = description
        self._from = self.convert_payment_from(_from)
        self._to = self.convert_payment_to(_to)



    def convert_date(self, iso_date: str):
        date = datetime.fromisoformat(iso_date)
        return date.strftime("%d.%m.%Y")


    def convert_payment_from(self, payment: str):
        if payment:
            payment_list = payment.split()
            payment = payment_list.pop()
            card_name = " ".join(payment_list)
            return card_name+f" {payment[:4]} {payment[4:6]}** **** {payment[-4:]}"

        return ""
    def convert_payment_to(self, payment: str):
        payment_list = payment.split()
        payment = payment_list.pop()
        card_name = " ".join(payment_list)
        return card_name+f" ** {payment[-4:]}"


    def __str__(self):
        return (f"{self.date} {self.description}\n"
                f"{self._from} =-> {self._to}\n"
                f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}\n")

