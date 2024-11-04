import time
import allure
import pytest
from Nintondo.AutoTests.Pages.Registration_page import CreateMnemonic
from Nintondo.AutoTests.Data import Data
from Nintondo.AutoTests.Pages.Nintondo_Mane import NintondoPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Nintondo.AutoTests.conftest import driver

@pytest.mark.usefixtures("driver")
@allure.feature("")
#
def test_connect(driver):

    restore_by_private_key = CreateMnemonic(driver)
    connect = NintondoPage(driver)

    driver.get(f'chrome-extension:{Data.EX_ID}/index.html')

    time.sleep(0.5)
    restore_by_private_key.enter_password(Data.PASS)  # Ввод пароля
    restore_by_private_key.conf_password(Data.CONFPASS)  # Подтверждение пароля
    restore_by_private_key.click_reg_button()  # Жмем на кнопку продолжения

    restore_by_private_key.type_reg_privacy_key()  # Выбираем восстановление через приватник
    restore_by_private_key.restore_input(Data.KEY_MONEY_WALLET)  # Вводим приватник
    restore_by_private_key.conf_create_wallet()  # Подтверждаем создание кошелька
    restore_by_private_key.choose_type_legacy()  # Выбираем:Legacy Type"
    restore_by_private_key.conf_recover_wallet()  # Подтверждаем создание кошелька

    driver.get("https://nintondo.io/")
    time.sleep(0.5)
    connect.change_network_btn()
    driver.set_window_size(800, 768)
    time.sleep(0.2)
    connect.connect_btn()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    print(driver.title)

    connect.sign_btn()
    time.sleep(1)
    driver.switch_to.window(windows[0])
    driver.set_window_size(1280, 720)