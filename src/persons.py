from requests import get, post, delete
from http import HTTPStatus


BASE_URL = 'http://localhost:3000'


def get_persons(persons):
    url = f'{BASE_URL}/persons'
    res = get(url)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == HTTPStatus.OK:
        score += 1

    if len(body) == len(persons):
        content_match = all(
            person.is_valid(body[i])
            for i, person in enumerate(persons)
        )
        if content_match:
            score += 2

    return score


def post_persons(person):
    url = f'{BASE_URL}/persons'
    data = person.data()
    res = post(url, json=data)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == HTTPStatus.OK:
        score += 1

    if body['name'] == person.name:
        person.id = body['id']
        score += 2

    return score


def post_persons_fail(person):
    url = f'{BASE_URL}/persons'
    data = person.data()
    res = post(url, json=data)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        score += 1

    if body['name'] == ["can't be blank"]:
        score += 2

    return score


def get_person(person):
    url = f'{BASE_URL}/persons/{person.id}'
    res = get(url)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == HTTPStatus.OK:
        score += 1

    if person.is_valid(body):
        score += 2

    return score


def delete_persons():
    url = f'{BASE_URL}/persons'
    res = delete(url)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == HTTPStatus.OK:
        score += 1

    if body == []:
        score += 2

    return score
