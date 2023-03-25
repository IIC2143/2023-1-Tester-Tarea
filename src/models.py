class Person:

    def __init__(self, name):
        self.id = None
        self.name = name
        self.vaccines = []

    def data(self):
        return {
            'person': {
                'name': self.name,
            },
        }

    def is_valid(self, data):
        attr_1 = data['name'] == self.name
        attr_2 = data['id'] == self.id

        return attr_1 and attr_2

    def delete_vaccine(self, vaccine):
        self.vaccines.remove(vaccine)

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__repr__()


class Vaccine:

    def __init__(self, vaccine_type, vaccine_date):
        self.id = None
        self.vaccine_type = vaccine_type
        self.vaccine_date = vaccine_date
        self.person_id = None

    def data(self):
        return {
            'vaccine': {
                'vaccine_type': self.vaccine_type,
                'vaccine_date': self.vaccine_date,
            },
        }

    def is_valid(self, data):
        attr_1 = data['id'] == self.id
        attr_2 = data['vaccine_type'] == self.vaccine_type
        attr_3 = data['vaccine_date'] == self.vaccine_date
        attr_4 = data['person_id'] == self.person_id

        return attr_1 and attr_2 and attr_3 and attr_4

    def update(self, data):
        if 'vaccine_type' in data['vaccine']:
            self.vaccine_type = data['vaccine']['vaccine_type']

        if 'vaccine_date' in data['vaccine']:
            self.vaccine_date = data['vaccine']['vaccine_date']

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__repr__()
