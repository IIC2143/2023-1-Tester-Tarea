from src.persons import (
    get_persons,
    post_persons,
    post_persons_fail,
    get_person,
    delete_persons,
)
from src.vaccines import (
    post_vaccines,
    post_vaccines_fail,
    patch_vaccines,
    patch_vaccines_fail,
)
from src.models import Person, Vaccine


def main():
    scores = []

    persons = [
        Person('Nicolas Alvarez'),
        Person('Andrea Perez'),
        Person('Felipe Gonzalez'),
    ]

    vaccines = [
        Vaccine('Moderna', '2021-05-17'),
        Vaccine('Pfizer', '2022-12-12'),
    ]

    update = [
        {'vaccine': {'vaccine_type': 'Moderna', 'vaccine_date': '2021-03-01'}},
        {'vaccine': {'vaccine_type': 'Sputnik'}}
    ]

    update_fail = [
        {'vaccine': {'vaccine_type': ''}},
    ]

    # 1
    scores.append(delete_persons())

    # 2
    scores.append(post_persons(persons[0]))

    # 3
    scores.append(get_person(persons[0]))

    # 4
    scores.append(post_persons_fail(Person('')))

    # 5
    scores.append(post_persons(persons[1]))

    # 6
    scores.append(get_persons(persons[:2]))

    # 7
    scores.append(post_vaccines(persons[0], vaccines[0]))

    # 8
    scores.append(post_vaccines(persons[0], vaccines[1]))

    # 9
    scores.append(post_vaccines_fail(persons[0], Vaccine('', '')))

    # 10
    scores.append(patch_vaccines(
        persons[0],
        persons[0].vaccines[1],
        update[0]
    ))

    # 11
    scores.append(patch_vaccines_fail(
        persons[0],
        persons[0].vaccines[1],
        update_fail[0]
    ))

    # Score
    for i, score in enumerate(scores):
        print(f'{i + 1:02d} - {score}/3')

    print(f'Total: {sum(scores)}/{len(scores) * 3}')


if __name__ == '__main__':
    main()
