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
    delete_vaccine,
)
from src.models import Person, Vaccine


def main():
    scores = []

    persons = [
        Person('Javier Fernandez'),
        Person('Laura Alcocer'),
    ]

    vaccines = [
        Vaccine('SINOVAC', '2022-01-20'),
        Vaccine('SINOVAC', '2022-07-20'),
        Vaccine('Pfizer', '2022-05-09'),
    ]

    update = [
        {'vaccine': {'vaccine_date': '2022-01-01'}}
    ]

    # 1
    scores.append(delete_persons())

    # 2
    scores.append(post_persons(persons[0]))

    # 3
    scores.append(post_persons(persons[1]))

    # 4
    scores.append(get_persons(persons))

    # 5
    scores.append(get_person(persons[0]))

    # 6
    scores.append(get_person(persons[1]))

    # 7
    scores.append(post_vaccines(persons[0], vaccines[0]))

    # 8
    scores.append(post_vaccines(persons[0], vaccines[1]))

    # 9
    scores.append(post_vaccines(persons[1], vaccines[2]))

    # 10
    scores.append(get_vaccines(persons[0]))

    # 11
    scores.append(get_vaccines(persons[1]))

    # 12
    scores.append(patch_vaccines(
        persons[0],
        persons[0].vaccines[0],
        update[0]
    ))

    # 13
    scores.append(delete_vaccine(persons[0], persons[0].vaccines[0]))

    # Score
    for i, score in enumerate(scores):
        print(f'{i + 1:02d} - {score}/3')

    print(f'Total: {sum(scores)}/{len(scores) * 3}')


if __name__ == '__main__':
    main()
