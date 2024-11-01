import pytest
import allure


@allure.feature('Memes')
@allure.story('Get memes')
@allure.title('Получение списка всех мемов')
def test_get_all_memes(get_meme_list_endpoint):
    get_meme_list_endpoint.do_authorize()
    get_meme_list_endpoint.get_memes_list()
    get_meme_list_endpoint.check_response_code_is_(200)

#########################################################
@allure.story('Get meme by id')
@allure.title('Получение одного мема')
def test_get_one_meme(get_one_meme_endpoint, mem_id):
    get_one_meme_endpoint.do_authorize()
    get_one_meme_endpoint.get_meme_by_id(mem_id)
    get_one_meme_endpoint.check_response_code_is_(200)

#############################################################
@allure.title('Получение мема по неверному  ID')
def test_check_meme_not_found(get_one_meme_endpoint):
    get_one_meme_endpoint.do_authorize()
    get_one_meme_endpoint.get_meme_by_id(999999)
    get_one_meme_endpoint.check_response_code_is_(404)

################################################################
@allure.title('Создание нового мема')
@allure.step('Создание нового мема с проверкой Text')
@pytest.mark.parametrize(
    'text', [
        'Long title ljksdhflks fsdlfhsldfj slfljshflsfkh sldf',
        '     ',
        '',
        None
        ],
)
@allure.step('Создание нового мема с проверкой Info')
@pytest.mark.parametrize(
    'info', [
        {"adress": 666, "city": 888},
        {"adress": 666},
        None,
        ],
)
@allure.step('Создание нового мема с проверкой url')
@pytest.mark.parametrize(
    'url', [
        'www.yandex.ru',
        '',
        None,
        ],
)
@allure.step('Создание нового мема с проверкой Tags')
@pytest.mark.parametrize(
    'tags', [
        ["hot", "cold"],
        ["xxx"],
        None,
        ],
)
def test_create_meme_text(create_meme_endpoint, text, info, tags, url):
    create_meme_endpoint.do_authorize()
    create_meme_endpoint.create_meme(
        {"text": text,
         "url": url,
         "tags": tags,
         "info": info
    })
    expected_result = 200
    if text is None or info is None or tags is None or url is None:
        expected_result = 400

    create_meme_endpoint.check_response_code_is_(expected_result)
    if expected_result == 200:
        create_meme_endpoint.check_response_field_is_("text", text)
        create_meme_endpoint.check_response_field_is_("url", url)
        create_meme_endpoint.check_response_field_is_("tags", tags)
        create_meme_endpoint.check_response_field_is_("info", info)

#########################################################
@allure.story('Delete meme by id')
@allure.title('Удаление одного мема')
def test_delete_one_meme(delete_meme_endpoint, mem_id):
    delete_meme_endpoint.do_authorize()
    delete_meme_endpoint.delete_meme(mem_id)
    delete_meme_endpoint.check_response_code_is_(200)


@allure.story('Failed delete meme by id')
@allure.title('Проверка удаления с неверным id')
def test_failed_delete_meme(delete_meme_endpoint, mem_id):
    delete_meme_endpoint.do_authorize()
    delete_meme_endpoint.delete_meme(9999999)
    delete_meme_endpoint.check_response_code_is_(404)

######################################################################
@allure.title('Изменение существующего мема')
@allure.step('Изменение существующего мема с проверкой  Text')
@pytest.mark.parametrize(
    'text', [
        'Long title ljksdhflks fsdlfhsldfj slfljshflsfkh sldf',
        '     ',
        '',
        None
        ],
)
@allure.step('Изменение существующего мема с проверкой  info')
@pytest.mark.parametrize(
    'info', [
        {"adress": 666, "city": 888},
        {"adress": 666},
        None,
        ],
)
@allure.step('Изменение существующего мема с проверкой  Url')
@pytest.mark.parametrize(
    'url', [
        'www.yandex.ru',
        '',
        None,
        ],
)
@allure.step('Изменение существующего мема с проверкой Tags')
@pytest.mark.parametrize(
    'tags', [
        ["hot", "cold"],
        ["xxx"],
        None,
        ],
)
def test_update_meme_text(update_meme_endpoint, mem_id, text, info, tags, url):
    update_meme_endpoint.do_authorize()
    update_meme_endpoint.update_meme(
        {"id": mem_id,
        "text": text,
         "url": url,
         "tags": tags,
         "info": info
    }, mem_id)

    expected_result = 200
    if text is None or info is None or tags is None or url is None:
        expected_result = 400

    update_meme_endpoint.check_response_code_is_(expected_result)
    if expected_result == 200:
        update_meme_endpoint.check_response_field_is_("id", str(mem_id))
        update_meme_endpoint.check_response_field_is_("text", text)
        update_meme_endpoint.check_response_field_is_("url", url)
        update_meme_endpoint.check_response_field_is_("tags", tags)
        update_meme_endpoint.check_response_field_is_("info", info)
