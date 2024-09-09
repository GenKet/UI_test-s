import requests
import gspread
import os
from general import get_element_by_css, get_elements_by_css, get_link
from google.oauth2.service_account import Credentials
from twocaptcha import TwoCaptcha


solver = TwoCaptcha()

def login_google(driver):
    """Логирование в Google"""
    
    with open('data/google.txt', 'r', encoding='utf-8') as file:
        login = file.readline().strip()
        password = file.readline().strip()
        
    with open('data/twocaptchaapi.txt', 'r', encoding='utf-8') as file:
        api = file.readline().strip()
        
    solver = TwoCaptcha(api) 
    
    get_link(driver, "https://accounts.google.com/v3/signin/identifier?authuser=2&continue=https%3A%2F%2Fmyaccount.google.com%2Fu%2F2%2F%3Fhl%3Dru%26utm_source%3DOGB%26utm_medium%3Dact%26gar%3DWzEyMF0&ec=GAlAwAE&hl=ru&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-536660343%3A1725912617202868&ddm=0")
    
    if get_element_by_css(driver, ".gb_Ld") == None:
        get_element_by_css(driver, ".identifierId").send_keys(login)
        get_element_by_css(driver, ".VfPpkd-vQzf8d").click()
        get_element_by_css(driver, ".whsOnd.zHQkBf").send_keys(password)
        get_element_by_css(driver, ".VfPpkd-RLmnJb").click()
        image_element = get_element_by_css(driver, '.img.f4ZpM.TrZEUc')
        image_url = image_element.get_attribute('src')
        image_data = requests.get(image_url).content

        with open('image.png', 'wb') as file:
            file.write(image_data)
        
        result = solver.normal(image_data)
        os.remove(image_data)
        
        get_element_by_css(driver, ".dMNVAe").send_keys(result['code'])
        get_element_by_css(driver, ".VfPpkd-vQzf8d").click()
        print("Вход в Google выполнен")
    
def change_google_password(driver):
    """Изменение пароля в Google"""
    
    with open('data/google.txt', 'r', encoding='utf-8') as file:
        login = file.readline().strip()
        password = file.readline().strip()
        
    login_google(driver)
    get_link(driver, "https://myaccount.google.com/u/2/signinoptions/password?gar=WzBd&continue=https://myaccount.google.com/u/2/security?hl%3Dru%26utm_source%3DOGB%26utm_medium%3Dact%26gar%3DWzBd&pli=1&rapt=AEjHL4ONMYlftuiE8GshTLEcElyVns1zGWXbyyspJljLDIfovEmrHMTdgYmxtznEa-hBl_ANom7Ddh6bqAMA5fO3UnX_dERqEqMAyUmJ1HR6MnllFWtV-10")
    
    new_password = input("Введите новый пароль")
    inputs = get_elements_by_css(driver, ".VfPpkd-fmcmS-wGMbrd.uafD5")
    inputs[0].send_keys(password)
    inputs[1].send_keys(new_password)
    
    get_element_by_css(driver, ".UywwFc-RLmnJb").click()
    
    with open('data/google.txt', 'w', encoding='utf-8') as file:
        file.write(f"{login}\n")  
        file.write(f"{new_password}\n")
    print("Успешно изменено")

def change_google_name_surname(driver):
    """Изменение имя и фамилии в google"""
    
    login_google(driver)
    get_link(driver, "https://myaccount.google.com/u/2/profile/name/edit?continue=https://myaccount.google.com/u/2/profile/name?gar%3DWzEyMF0%26continue%3Dhttps%253A%252F%252Fmyaccount.google.com%252Fu%252F2%252Fpersonal-info%253Fgar%253DWzEyMF0%2526hl%253Dru%2526utm_source%253DOGB%2526utm_medium%253Dact%26hl%3Dru%26utm_source%3DOGB%26utm_medium%3Dact&pli=1&rapt=AEjHL4PDS0Hebq1y6JEiVtKrrDv2-ULg87vwNJGngmEzGVIa7D_EwcgfgcuSCiK38zwbNW6g7QEzYfo_QiLVRn-f1Bf96omLWxqmSanxu7Ncj7WmI0TMhos")
    
    info = input("Введите новое имя и фамилю через пробел")
    name = info.split(" ")[0]
    second_name = info.split(" ")[1]
    inputs = get_elements_by_css(driver, ".VfPpkd-fmcmS-wGMbrd")
    inputs[0].send_keys(name)
    inputs[1].send_keys(second_name)
    
    get_element_by_css(driver, ".VfPpkd-dgl2Hf-ppHlrf-sM5MNb").click()
    print("Успешно изменено")

def save_google_data_to_table(driver):
    """Сохранение информации в гугл таблицу"""
    
    with open('data/google.txt', 'r', encoding='utf-8') as file:
        login = file.readline().strip()
        password = file.readline().strip()
        
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file("credentials/credentials.json", scopes=scope)
    client = gspread.authorize(creds)
    
    login_google(driver)
    table_name = input("Введите название таблицы")
    worksheet = input("Введите название листа")
    
    sheet = client.open(table_name).worksheet(worksheet)
    
    get_link(driver, "https://myaccount.google.com/u/2/personal-info?hl=ru&utm_source=OGB&utm_medium=act&gar=WzBd")
    info = get_elements_by_css(driver, ".bJCr1d")
    name = info[4].text.split(" ")[0]
    second_name = info[4].text.split(" ")[1]
    bithday = info[5].text
    
    get_link(driver, "https://myaccount.google.com/u/2/security?hl=ru&utm_source=OGB&utm_medium=act&gar=WzBd")
    info = get_elements_by_css(driver,".kFNik")
    if info[3].text == "Добавьте адрес электронной почты":
        backup_email = "Не указано"
    else:
        backup_email = info[3].text
    
    column_a_values = sheet.col_values(1)
    last_row = len(column_a_values) + 1  
    range_to_update = f"A{last_row}:F{last_row}"   
    values = [
    [name, second_name, login, password, bithday, backup_email]
]
    sheet.update(range_to_update, values)
    print("Успешно сохранено")
