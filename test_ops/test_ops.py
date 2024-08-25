import allure


class TestExamples:

    @allure.title('Passed test 1')
    @allure.story('Test examples')
    def test_pass_2(self):
        with allure.step("Test passed"):
            assert True

    @allure.title('Passed test 2')
    @allure.story('Test examples')
    def test_pass_1(self):
        with allure.step("Test passed"):
            assert True

    @allure.title('Passed test 3')
    @allure.story('Test examples')
    def test_pass_3(self):
        with allure.step("Test passed"):
            assert True

    @allure.title('Expected test failure 1')
    @allure.story('Test examples')
    def test_fail_1(self):
        with allure.step("Test failed"):
            assert False

    @allure.title('Expected test failure 2')
    @allure.story('Test examples')
    def test_fail_2(self):
        with allure.step("Test failed"):
            assert False
