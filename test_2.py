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
    delete_vaccine,
)
from src.models import Person, Vaccine


def main():
    scores = []

    persons = [
        Person('Nicole Caballero'),
        Person('Martin Orrego'),
    ]

    vaccines = [
        Vaccine('SINOVAC', '2021-01-13'),
        Vaccine('SINOVAC', '2021-02-14'),
        Vaccine('Pfizer', '2021-03-15'),
        Vaccine('Pfizer', '2021-04-16'),
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
    scores.append(post_vaccines(persons[0], vaccines[0]))

    # 6
    scores.append(post_persons(persons[1]))

    # 7
    scores.append(post_vaccines(persons[1], vaccines[1]))

    # 8
    scores.append(get_vaccines(persons[0]))

    # 9
    scores.append(get_vaccines(persons[1]))

    # 10
    scores.append(post_persons_fail(Person('')))

    # 11
    scores.append(post_vaccines_fail(persons[0], Vaccine('', '')))

    # 12
    scores.append(post_vaccines(persons[0], vaccines[2]))

    # 13
    scores.append(post_vaccines(persons[0], vaccines[3]))

    # 14
    scores.append(get_vaccines(persons[0]))

    # 15
    scores.append(get_vaccines(persons[1]))

    # 16
    scores.append(delete_vaccine(persons[0], persons[0].vaccines[0]))

    # 17
    scores.append(delete_vaccine(persons[1], persons[1].vaccines[0]))

    # 18
    scores.append(get_vaccines(persons[0]))

    # 19
    scores.append(get_vaccines(persons[1]))

    # 20
    scores.append(delete_persons())

    # Score
    for i, score in enumerate(scores):
        print(f'{i + 1:02d} - {score}/3')

    print(f'Total: {sum(scores)}/{len(scores) * 3}')


if __name__ == '__main__':
    main()
