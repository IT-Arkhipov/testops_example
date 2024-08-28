import allure


@allure.id("34107")
@allure.title("Проверка добавления элемента")
@allure.story("Добавление/удаление элементов")
@allure.feature("Позитивные тесты")
@allure.label("suite", "Add/Remove Elements")
@allure.label("owner", "allure8")
def test_add_remove():
    with allure.step("Открыть страницу https://the-internet.herokuapp.com/add_remove_elements/ в браузере"):
        with allure.step("Expected Result"):
            with allure.step("Страница открыта"):
                pass
    with allure.step("Кликнуть по кнопке Add Element"):
        with allure.step("Expected Result"):
            with allure.step("Под нажатой кнопкой отображается кнопка Delete"):
                pass


@allure.id("34118")
@allure.title("Сложение двух чисел")
@allure.story("Математические операции")
@allure.feature("Позитивные тесты")
@allure.label("suite", "Math ops")
@allure.label("owner", "allure8")
def test_sum():
    with allure.step("Сложить два числа: 2, 5"):
        with allure.step("Ожидаемый результат"):
            with allure.step("Результат равен сумме двух чисел - 7"):
                assert 2 + 5 == 7
