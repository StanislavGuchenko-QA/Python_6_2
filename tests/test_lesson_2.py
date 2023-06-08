from selene.support.shared import browser
from selene import be, have


def test_lesson_2(set_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('QA.GURU').press_enter()
    browser.element('[id="search"]').should(have.text('QA.GURU — Курсы тестировщиков - онлайн-обучение'))