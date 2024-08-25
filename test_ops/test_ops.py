import allure


class TestExamples:

    @allure.story('Passed test 2')
    @allure.title('Test examples')
    def test_pass_2(self):
        with allure.step("Test passed"):
            assert True

    @allure.story('Passed test 1')
    @allure.title('Test examples')
    def test_pass_1(self):
        with allure.step("Test passed"):
            assert True

    @allure.story('Passed test 3')
    @allure.title('Test examples')
    def test_pass_3(self):
        with allure.step("Test passed"):
            assert True

    @allure.story('Expected test failure 1')
    @allure.title('Test examples')
    def test_fail_1(self):
        with allure.step("Test failed"):
            assert False

    @allure.story('Expected test failure 2')
    @allure.title('Test examples')
    def test_fail_2(self):
        with allure.step("Test failed"):
            assert False
