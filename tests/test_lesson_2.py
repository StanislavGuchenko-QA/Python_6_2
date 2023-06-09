from selene.support.shared import browser
from selene import be, have


def test_lesson_2(set_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('bgdbfgbdbrtddb').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))