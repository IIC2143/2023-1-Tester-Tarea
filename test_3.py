from src.persons import (
    get_persons,
    post_persons,
    post_persons_fail,
    get_person,
    delete_persons,
)
from src.vaccines import (
    get_vaccines,
    post_vaccines,
    post_vaccines_fail,
    patch_vaccines,
    patch_vaccines_fail,
    delete_vaccine,
)
from src.models import Person, Vaccine


def main():
    scores = []

    persons = [
        Person('Carlos Castro'),
        Person('Francisca Robles'),
        Person('Jose Antonio Paredes'),
    ]

    vaccines = [
        Vaccine('Moderna', '2023-05-17'),
        Vaccine('Pfizer', '2023-12-12'),
        Vaccine('Pfizer', '2023-12-13'),
    ]

    update = [
        {'vaccine': {'vaccine_type': 'Sinovac', 'vaccine_date': '2024-01-07'}},
        {'vaccine': {'vaccine_type': 'Sputnik-V'}},
        {'vaccine': {'vaccine_date': '2020-03-01'}},
    ]

    update_fail = [
        {'vaccine': {'vaccine_type': ''}},
        {'vaccine': {'vaccine_date': ''}},
        {'vaccine': {'vaccine_date': '', 'vaccine_type': ''}},
    ]

    # 1
    scores.append(delete_persons())

    # 2
    scores.append(post_persons_fail(Person('')))

    # 3
    scores.append(get_persons([]))

    # 4
    scores.append(post_persons(persons[0]))

    # 5
    scores.append(post_persons(persons[1]))

    # 6
    scores.append(post_persons(persons[2]))

    # 7
    scores.append(get_persons(persons))

    # 8
    scores.append(post_vaccines(persons[0], vaccines[0]))

    # 9
    scores.append(post_vaccines(persons[0], vaccines[1]))

    # 10
    scores.append(post_vaccines_fail(persons[0], Vaccine('', '')))

    # 11
    scores.append(post_vaccines(persons[0], vaccines[2]))

    # 12
    scores.append(get_vaccines(persons[0]))

    # 13
    scores.append(patch_vaccines(
        persons[0],
        persons[0].vaccines[1],
        update[0]
    ))

    # 14
    scores.append(patch_vaccines_fail(
        persons[0],
        persons[0].vaccines[1],
        update_fail[0]
    ))

    # 15
    scores.append(patch_vaccines(
        persons[0],
        persons[0].vaccines[1],
        update[1]
    ))

    # 16
    scores.append(patch_vaccines(
        persons[0],
        persons[0].vaccines[1],
        update[2]
    ))

    # 17
    scores.append(delete_vaccine(persons[0], persons[0].vaccines[1]))

    # 18
    scores.append(delete_vaccine(persons[0], persons[0].vaccines[0]))

    # 19
    scores.append(get_person(persons[0]))

    # 20
    scores.append(delete_persons())

    # Score
    for i, score in enumerate(scores):
        print(f'{i + 1:02d} - {score}/3')

    print(f'Total: {sum(scores)}/{len(scores) * 3}')


if __name__ == '__main__':
    main()
