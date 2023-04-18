from src.persons import (
    get_persons,
    post_persons,
    get_person,
    delete_persons,
)
from src.vaccines import (
    get_vaccines,
    post_vaccines,
)
from src.models import Person, Vaccine


def test_1():
    scores = []

    persons = [
        Person('Andrea Silva'),
        Person('Cristobal Araujo'),
        Person('Alexis Suarez'),
    ]

    vaccines = [
        Vaccine('Pfizer', '2022-01-20'),
        Vaccine('SINOVAC', '2022-07-20'),
        Vaccine('Pfizer', '2022-05-09'),
        Vaccine('Moderna', '2022-05-19'),
        Vaccine('Pfizer', '2022-09-09'),
        Vaccine('SINOVAC', '2022-09-19'),
        Vaccine('Sputnik V', '2022-09-29'),
    ]

    # 1
    scores.append(delete_persons())

    # 2
    scores.append(post_persons(persons[0]))

    # 3
    scores.append(get_persons(persons[:1]))

    # 4
    scores.append(post_persons(persons[1]))

    # 5
    scores.append(get_person(persons[0]))

    # 6
    scores.append(post_persons(persons[2]))

    # 7
    scores.append(get_persons(persons))

    # 8
    scores.append(post_vaccines(persons[0], vaccines[0]))

    # 9
    scores.append(post_vaccines(persons[0], vaccines[1]))

    # 10
    scores.append(get_vaccines(persons[0]))

    # 11
    scores.append(post_vaccines(persons[1], vaccines[2]))

    # 12
    scores.append(get_vaccines(persons[1]))

    # 13
    scores.append(post_vaccines(persons[2], vaccines[3]))

    # 14
    scores.append(post_vaccines(persons[2], vaccines[4]))

    # 15
    scores.append(post_vaccines(persons[2], vaccines[5]))

    # 16
    scores.append(get_vaccines(persons[2]))

    # 17
    scores.append(post_vaccines(persons[0], vaccines[6]))

    # 18
    scores.append(get_vaccines(persons[0]))

    # 19
    scores.append(get_vaccines(persons[1]))

    # 20
    scores.append(get_vaccines(persons[2]))

    # Score
    for i, score in enumerate(scores):
        print(f'{i + 1:02d} - {score}/3')

    print(f'Total: {sum(scores)}/{len(scores) * 3}')


if __name__ == '__main__':
    test_1()
