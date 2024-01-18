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
        self._from = self.convert_payment(_from)
        self._to = self.convert_payment(_to)



    def convert_date(self, iso_date: str):
        date = datetime.fromisoformat(iso_date)
        return date.strftime("%d.%m/%Y")


    def convert_payment(self, payment: str):
        if payment:
            if payment.startswith("..."):
                ...
            else:
                ...
            return ""


        def __str__(self):
            return (f"{self.date} {self.description}"
                    f"{self._from} -> {self._to}"
                    f"{self.operation_amount['amount']}{self.operation_amount['name']}")




