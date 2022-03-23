import json
class Employee:
    def __init__(self, name, address, IsAttending, orderQty, order):
        self.name = name
        self.address = address
        self.IsAttending = IsAttending
        self.orderQty = orderQty
        self.order = order

    def __iter__(self):
        yield from {
            "name": self.name,
            "address": self.address,
            "items": [{
                "id": self.order,
                "amount": self.orderQty
            }]
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)
    
    def __repr__(self):
        return self.__str__()
