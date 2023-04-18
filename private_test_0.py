from src.persons import (
    get_persons,
    post_persons,
    post_persons_fail,
    get_person,
    delete_persons,
)

from src.models import Person


def test_0():
    scores = []

    persons = [
        Person('Arturo Silva'),
        Person('Juan Perez'),
        Person('Maria Lopez'),
        Person('Pedro Sanchez'),
        Person('Maria Garcia'),
        Person('Jose Rodriguez'),
        Person('Maria Hernandez'),
    ]

    # 1
    scores.append(delete_persons())

    # 2
    scores.append(post_persons(persons[0]))

    # 3
    scores.append(post_persons(persons[1]))

    # 4
    scores.append(get_person(persons[0]))

    # 5
    scores.append(get_person(persons[1]))

    # 6
    scores.append(get_persons(persons[:2]))

    # 7
    scores.append(post_persons_fail(Person('')))

    # 8
    scores.append(get_persons(persons[:2]))

    # 9
    scores.append(post_persons(persons[2]))

    # 10
    scores.append(post_persons(persons[3]))

    # 11
    scores.append(post_persons(persons[4]))

    # 12
    scores.append(get_persons(persons[:5]))

    # 13
    scores.append(post_persons_fail(Person('')))

    # 14
    scores.append(post_persons(persons[5]))

    # 15
    scores.append(post_persons(persons[6]))

    # 16
    scores.append(get_persons(persons))

    # 17
    scores.append(post_persons_fail(Person('')))

    # 18
    scores.append(get_person(persons[4]))

    # 19
    scores.append(get_persons(persons))

    # 20
    scores.append(delete_persons())

    # Score
    for i, score in enumerate(scores):
        print(f'{i + 1:02d} - {score}/3')

    print(f'Total: {sum(scores)}/{len(scores) * 3}')


if __name__ == '__main__':
    test_0()
