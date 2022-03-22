from json import JSONEncoder

class EmployeeEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__