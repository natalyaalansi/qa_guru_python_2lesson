import pytest

"""Документация"""
# Комментарий

@pytest.fixture()
def choice_user():
    user_id = 123
    yield user_id
    print("Удаляем пользователя 123")

@pytest.fixture()
def configure_mobile_browser():
    "Устанавливает мобильное соотношение сторон браузера"
    print('Я мобильная фикстура')

@pytest.fixture()
def configure_desktop_browser():
    "Устанавливает десктопное соотношение сторон браузера"
    print('Я десктопная фикстура')

def test_first(configure_mobile_browser):
    print(configure_mobile_browser)

def test_second(configure_desktop_browser):
    print(configure_desktop_browser)

def test_third(choice_user):
    print(choice_user)
    assert choice_user == 123