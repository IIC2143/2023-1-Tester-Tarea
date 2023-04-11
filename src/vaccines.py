from requests import get, post, patch, delete
from http import HTTPStatus


BASE_URL = 'http://localhost:3000'


def get_vaccines(person):
    url = f'{BASE_URL}/persons/{person.id}/vaccines'
    res = get(url)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == 200:
        score += 1

    if len(body) == len(person.vaccines):
        content_match = all(
            vaccine.is_valid(body[i])
            for i, vaccine in enumerate(person.vaccines)
        )

        if content_match:
            score += 2

    return score


def post_vaccines(person, vaccine):
    url = f'{BASE_URL}/persons/{person.id}/vaccines'
    data = vaccine.data()
    res = post(url, json=data)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == 200:
        score += 1

    if len(body) == len(person.vaccines) + 1:
        attr_1 = body[-1]['person_id'] == person.id
        attr_2 = body[-1]['vaccine_type'] == vaccine.vaccine_type
        attr_3 = body[-1]['vaccine_date'] == vaccine.vaccine_date

        if attr_1 and attr_2 and attr_3:
            score += 2
            vaccine.id = body[-1]['id']
            vaccine.person_id = body[-1]['person_id']
            person.vaccines.append(vaccine)

    return score


def post_vaccines_fail(person, vaccine):
    url = f'{BASE_URL}/persons/{person.id}/vaccines'
    data = vaccine.data()
    res = post(url, json=data)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        score += 1

    if vaccine.vaccine_type == '' and vaccine.vaccine_date == '':
        if body['vaccine_type'] == body['vaccine_date'] == ['can\'t be blank']:
            score += 2

    elif vaccine.vaccine_type == '':
        if body['vaccine_type'] == ['can\'t be blank']:
            score += 2

    elif vaccine.vaccine_date == '':
        if body['vaccine_date'] == ['can\'t be blank']:
            score += 2

    return score


def patch_vaccines(person, vaccine, new_params):
    url = f'{BASE_URL}/persons/{person.id}/vaccines/{vaccine.id}'
    res = patch(url, json=new_params)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == 200:
        score += 1

    if len(body) == len(person.vaccines):
        vaccine.update(new_params)

        body.sort(key=lambda x: x['id'])
        person.vaccines.sort(key=lambda x: x.id)

        content_match = all(
            vaccine.is_valid(body[i])
            for i, vaccine in enumerate(person.vaccines)
        )

        if content_match:
            score += 2

    return score


def patch_vaccines_fail(person, vaccine, new_params):
    url = f'{BASE_URL}/persons/{person.id}/vaccines/{vaccine.id}'
    res = patch(url, json=new_params)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        score += 1

    new_params = new_params['vaccine']

    if 'vaccine_type' in new_params and 'vaccine_date' in new_params:
        if body['vaccine_type'] == body['vaccine_date'] == ['can\'t be blank']:
            score += 2

    elif 'vaccine_type' in new_params:
        if body['vaccine_type'] == ['can\'t be blank']:
            score += 2

    elif 'vaccine_date' in new_params:
        if body['vaccine_date'] == ['can\'t be blank']:
            score += 2

    return score


def delete_vaccine(person, vaccine):
    url = f'{BASE_URL}/persons/{person.id}/vaccines/{vaccine.id}'
    res = delete(url)

    body = res.json()
    status_code = res.status_code

    score = 0

    if status_code == 200:
        score += 1

    if len(body) == len(person.vaccines) - 1:
        person.delete_vaccine(vaccine)
        content_match = all(
            vaccine.is_valid(body[i])
            for i, vaccine in enumerate(person.vaccines)
        )

        if content_match:
            score += 2

    return score
