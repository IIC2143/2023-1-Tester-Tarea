from src.persons import (
    get_persons,
    post_persons,
    get_person,
    delete_persons,
)
from src.vaccines import (
    get_vaccines,
    post_vaccines,
    patch_vaccines,
)
from src.models import Person, Vaccine


def test_2():
    scores = []

    persons = [
        Person('Patana'),
        Person('Bodoque'),
        Person('Juanin'),
        Person('Tulio'),
    ]

    vaccines = [
        Vaccine('RombosMan', '2022-01-20'),
        Vaccine('Television', '2022-07-20'),
        Vaccine('Aire', '2022-05-19'),
        Vaccine('Mi Muneca', '2022-05-09'),
    ]

    update = [
        {'vaccine': {'vaccine_type': 'Mi Mu', 'vaccine_date': '2022-01-01'}},
        {'vaccine': {'vaccine_date': '2023-06-01'}},
    ]

    # 1
    scores.append(delete_persons())

    # 2
    scores.append(post_persons(persons[0]))

    # 3
    scores.append(post_persons(persons[1]))

    # 4
    scores.append(post_persons(persons[2]))

    # 5
    scores.append(post_persons(persons[3]))

    # 6
    scores.append(get_persons(persons))

    # 7
    scores.append(get_person(persons[0]))

    # 8
    scores.append(get_person(persons[1]))

    # 9
    scores.append(get_person(persons[2]))

    # 10
    scores.append(get_person(persons[3]))

    # 11
    scores.append(post_vaccines(persons[0], vaccines[0]))

    # 12
    scores.append(post_vaccines(persons[1], vaccines[1]))

    # 13
    scores.append(post_vaccines(persons[2], vaccines[2]))

    # 14
    scores.append(post_vaccines(persons[3], vaccines[3]))

    # 15
    scores.append(get_vaccines(persons[0]))

    # 16
    scores.append(get_vaccines(persons[1]))

    # 17
    scores.append(get_vaccines(persons[2]))

    # 18
    scores.append(get_vaccines(persons[3]))

    # 19
    scores.append(patch_vaccines(persons[0], vaccines[0], update[0]))

    # 20
    scores.append(patch_vaccines(persons[1], vaccines[1], update[1]))

    # Score
    for i, score in enumerate(scores):
        print(f'{i + 1:02d} - {score}/3')

    print(f'Total: {sum(scores)}/{len(scores) * 3}')


if __name__ == '__main__':
    test_2()
