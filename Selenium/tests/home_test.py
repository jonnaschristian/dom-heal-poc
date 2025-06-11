import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = r"C:\Users\Jonnas\Documents\dom-heal-poc\chromedriver-win64\chromedriver.exe"
URL = "http://localhost:8000/home.html"

with open("../elements/home.json", encoding="utf-8") as f:
    HOME_SELECTORS = json.load(f)
with open("../elements/post.json", encoding="utf-8") as f:
    POST_SELECTORS = json.load(f)

def aguarda_elemento(driver, by, selector, timeout=10):
    for _ in range(timeout * 2):
        try:
            el = driver.find_element(by, selector)
            if el.is_displayed():
                return el
        except Exception:
            pass
        time.sleep(0.5)
    raise Exception(f"Elemento {selector} não ficou visível em {timeout}s.")

service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    # Teste 1: Deve exibir corretamente o título e subtítulo do blog
    driver.get(URL)
    driver.maximize_window()
    titulo = aguarda_elemento(driver, By.CSS_SELECTOR, HOME_SELECTORS["tituloCabecalho"])
    subtitulo = aguarda_elemento(driver, By.CSS_SELECTOR, HOME_SELECTORS["subtituloCabecalho"])
    assert titulo.text == "Clean Blog", f"Título errado: {titulo.text}"
    assert subtitulo.text == "A Blog Theme by Start Bootstrap", f"Subtítulo errado: {subtitulo.text}"
    print("Teste 1 PASSOU")

    # Teste 2: Deve permitir acessar um post individual a partir de um card na Home
    cards = driver.find_elements(By.CSS_SELECTOR, HOME_SELECTORS["cardsPost"])
    assert len(cards) > 0, "Nenhum card de post encontrado na Home"
    primeiro_card = cards[0]
    primeiro_link = primeiro_card.find_element(By.TAG_NAME, "a")
    primeiro_link.click()

    titulo_post = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["titulo"])
    assert titulo_post.is_displayed() and titulo_post.text.strip() != "", "Título do post não visível ou vazio"
    print("Teste 2 PASSOU")

finally:
    driver.quit()
