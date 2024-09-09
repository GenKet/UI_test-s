from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from app.google import change_google_password, change_google_name_surname, save_google_data_to_table
from app.twitter import change_X_password, make_random_tweet


with open('data/proxy.txt', 'r', encoding='utf-8') as file:
    proxy = file.readline().strip()  
    
with open('data/user_agent.txt', 'r', encoding='utf-8') as file:
    user_agent = file.readline().strip()  


firefox_options = Options()
firefox_options.set_preference("general.useragent.override", user_agent)
firefox_options.add_argument('--headless')
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy,
    "proxyType": "MANUAL",
}

gecko_driver_path = r'C:\Driver\geckodriver.exe'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)
driver.implicitly_wait(30)

def google_menu():
    """Меню выбора для google"""
    
    print("\n--- Google Почта ---")
    print("1. Изменить пароль")
    print("2. Изменить Имя и Фамилию")
    print("3. Сохранение данных в таблицу")
    choice = input("Выберите действие (1-3): ")

    try:
        if choice == '1':
            change_google_password(driver)
        elif choice == '2':
            change_google_name_surname(driver)
        elif choice == '3':
            save_google_data_to_table(driver)
        else:
            raise ValueError("Неверный выбор!")
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте снова.")

def X_menu():
    """Меню выбора для X"""
    
    print("\n--- X ---")
    print("1. Изменить пароль")
    print("2. Сделать пост в X с помощью ChatGPT")
    choice = input("Выберите действие (1-2): ")

    try:
        if choice == '1':
            change_X_password(driver)
        elif choice == '2':
            make_random_tweet(driver)
        else:
            raise ValueError("Неверный выбор!")
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте снова.")

def main_menu():
    """Меню выбора для main menu"""
    
    while True:
        print("\n--- Главное Меню ---")
        print("1. Google Почта")
        print("2. X")
        print("3. Выход")
        choice = input("Выберите действие (1-3): ")

        try:
            if choice == '1':
                google_menu()
            elif choice == '2':
                X_menu()
            elif choice == '3':
                print("Выход из программы.")
                break
            else:
                raise ValueError("Неверный выбор!")
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")


main_menu()
