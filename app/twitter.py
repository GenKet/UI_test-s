from general import get_element_by_css, get_elements_by_css, get_link, generate_text

def login_tw(driver):
    """Логирование в Х"""
    
    with open('data/x.txt', 'r', encoding='utf-8') as file:
        login = file.readline().strip()
        password = file.readline().strip() 
        
    get_link(driver, r"https://x.com/i/flow/login?redirect_after_login=%2Fx_login")
    
    if get_element_by_css(driver, ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3") == None:
        get_element_by_css(driver, ".r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7").send_key(login)
        get_element_by_css(driver, ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3").click()
        get_element_by_css(driver, ".r-30o5o.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7").send_key(password)
        get_element_by_css(driver, ".css-146c3p1.r-bcqeeo.r-qvutc0.r-37j5jr.r-q4m81j.r-a023e6.r-rjixqe.r-b88u0q.r-1awozwy.r-6koalj.r-18u37iz.r-16y2uox.r-1777fci").click()
        while True:
            if get_element_by_css(driver, ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3") != None:
                break
            password = input("Введите корректный пароль")
            get_element_by_css(driver, ".r-30o5o.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7").send_key(password)
            get_element_by_css(driver, ".css-146c3p1.r-bcqeeo.r-qvutc0.r-37j5jr.r-q4m81j.r-a023e6.r-rjixqe.r-b88u0q.r-1awozwy.r-6koalj.r-18u37iz.r-16y2uox.r-1777fci").click()

def change_X_password(driver):
    """Изменение пароля Х"""
    
    with open('data/x.txt', 'r', encoding='utf-8') as file:
        login = file.readline().strip()
        password = file.readline().strip() 
    login_tw(driver)
    get_link(driver, r"https://x.com/settings/password")
    while True:
        cntr = 0
        if get_element_by_css(driver, ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3") != None:
            print("Пароль успешно изменен")
            break
        elif cntr >0:
            print("Неправильные данные, попробуйте еще раз")
        new_password = input("Введите новый пароль")
        input = get_elements_by_css(driver, ".r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")
        input[0].send_key(password)
        input[1].send_key(new_password)
        input[2].send_key(new_password)
        get_element_by_css(driver, ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3").click()
        cntr += 1


def make_random_tweet(driver):
    """Рандомный твит"""
    
    login_tw(driver)
    get_link(driver, r"https://x.com/home?lang=en")
    
    get_element_by_css(driver, ".css-146c3p1.r-bcqeeo.r-qvutc0.r-37j5jr.r-q4m81j.r-a023e6.r-rjixqe.r-b88u0q.r-1awozwy.r-6koalj.r-18u37iz.r-16y2uox.r-1777fci").click()
    prompt = input("Введи тему для твита")
    text = generate_text(prompt)
    get_element_by_css(driver, ".public-DraftStyleDefault-block public-DraftStyleDefault-ltr").send_key(text)
    get_element_by_css(driver, ".css-1jxf684.r-dnmrzs.r-1udh08x.r-3s2u2q.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3.r-a023e6.r-rjixqe").click()
    print("Твит отправлен")