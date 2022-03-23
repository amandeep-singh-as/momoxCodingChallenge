import json
class Address:
    def __init__(self, street, city, postalCode):
        self.street = street
        self.city = city
        self.postalCode = postalCode

    def __iter__(self):
        yield from {
            "street": self.street,
            "city": self.city,
            "postal_code": self.postalCode
        }.items()
    
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()