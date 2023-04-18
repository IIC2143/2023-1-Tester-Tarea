from src.persons import (
    get_persons,
    post_persons,
    post_persons_fail,
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


def test_3():
    scores = []

    persons = [
        Person('Diego'),
        Person('Glot'),
        Person('Javier'),
        Person('Laura'),
    ]

    vaccines = [
        Vaccine('SINOVAC', '2022-01-20'),
        Vaccine('SINOVAC', '2022-07-20'),
        Vaccine('Pfizer', '2022-05-09'),
        Vaccine('Moderna', '2022-05-19'),
    ]

    update = [
        {'vaccine': {'vaccine_date': '2022-01-01'}},
        {'vaccine': {'vaccine_date': '2023-06-01'}},
    ]

    update_fail = [
        {'vaccine': {'vaccine_type': ''}},
        {'vaccine': {'vaccine_date': ''}},
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
    scores.append(post_persons_fail(Person('')))

    # 7
    scores.append(post_vaccines(persons[0], vaccines[0]))

    # 8
    scores.append(post_vaccines(persons[0], vaccines[1]))

    # 9
    scores.append(post_vaccines(persons[1], vaccines[2]))

    # 10
    scores.append(post_vaccines(persons[2], vaccines[3]))

    # 11
    scores.append(post_vaccines_fail(persons[3], Vaccine('', '')))

    # 12
    scores.append(get_vaccines(persons[0]))

    # 13
    scores.append(get_vaccines(persons[1]))

    # 14
    scores.append(delete_vaccine(persons[0], persons[0].vaccines[1]))

    # 15
    scores.append(delete_vaccine(persons[0], persons[0].vaccines[0]))

    # 16
    scores.append(patch_vaccines(
        persons[1],
        persons[1].vaccines[0],
        update[0]
    ))

    # 17
    scores.append(patch_vaccines_fail(
        persons[2],
        persons[2].vaccines[0],
        update_fail[0]
    ))

    # 18
    scores.append(patch_vaccines(
        persons[2],
        persons[2].vaccines[0],
        update[1]
    ))

    # 19
    scores.append(patch_vaccines_fail(
        persons[2],
        persons[2].vaccines[0],
        update_fail[1]
    ))

    # 20
    scores.append(get_persons(persons))

    # Score
    for i, score in enumerate(scores):
        print(f'{i + 1:02d} - {score}/3')

    print(f'Total: {sum(scores)}/{len(scores) * 3}')


if __name__ == '__main__':
    test_3()
