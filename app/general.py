import openai
from selenium.webdriver.common.by import By



def get_link(driver, link):
    """Get-запрос по ссылке"""
    
    driver.get(link)
    
def generate_text(prompt):
    """Генерирует текст поста с помощью ChatGPT"""
    
    with open('data/x.txt', 'r', encoding='utf-8') as file:
        key = file.readline().strip()
    
    openai.api_key = key
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=1024,  
        n=1,  
        stop=None,  
        temperature=0.7,  
    )

    tweet_text = response.choices[0].text.strip()
    return tweet_text
    

def get_elements_by_css(driver, selector):
    """ Получаем элементы через CSS"""
    
    elements = driver.find_elements(By.CSS_SELECTOR, selector)
    return elements

def get_element_by_css(driver, selector):
    """ Получаем элемент через CSS"""
    
    element = driver.find_element(By.CSS_SELECTOR, selector)
    return element