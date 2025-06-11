import json
import time
import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = r"C:\Users\Jonnas\Documents\dom-heal-poc\chromedriver-win64\chromedriver.exe"
URL = "http://localhost:8000/home.html"

def load_selectors():
    with open("../elements/contact.json", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def driver():
    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def gerar_nome():
    nomes = ["João QA", "Maria Teste", "Jonnas QA", "Ana Souza"]
    return random.choice(nomes)

def gerar_telefone():
    return "(85) 9" + str(random.randint(1000, 9999)) + "-" + str(random.randint(1000, 9999))

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

def abrir_menu_contato(driver, SELECTORS):
    driver.get(URL)
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, SELECTORS["menu"]).click()
    aguarda_elemento(driver, By.CSS_SELECTOR, SELECTORS["tituloContato"])

def test_envio_sucesso(driver):
    SELECTORS = load_selectors()
    abrir_menu_contato(driver, SELECTORS)
    assert "Contact Me" in driver.find_element(By.CSS_SELECTOR, SELECTORS["tituloContato"]).text

    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputNome"]).send_keys(gerar_nome())
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputEmail"]).send_keys("teste@gmail.com")
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputTelefone"]).send_keys(gerar_telefone())
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputMensagem"]).send_keys("Mensagem de teste via Selenium")
    btn = driver.find_element(By.CSS_SELECTOR, SELECTORS["btnEnviar"])
    driver.execute_script("arguments[0].click();", btn)

    sucesso = aguarda_elemento(driver, By.CSS_SELECTOR, SELECTORS["mensagemSucesso"])
    assert "Form submission successful!" in sucesso.text

def test_botao_desabilitado_quando_vazio(driver):
    SELECTORS = load_selectors()
    abrir_menu_contato(driver, SELECTORS)
    assert "Contact Me" in driver.find_element(By.CSS_SELECTOR, SELECTORS["tituloContato"]).text

    btn = driver.find_element(By.CSS_SELECTOR, SELECTORS["btnEnviar"])
    classes = btn.get_attribute("class")
    assert "disabled" in classes, "Botão não está desabilitado como esperado"

def test_email_invalido(driver):
    SELECTORS = load_selectors()
    abrir_menu_contato(driver, SELECTORS)
    assert "Contact Me" in driver.find_element(By.CSS_SELECTOR, SELECTORS["tituloContato"]).text

    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputNome"]).send_keys(gerar_nome())
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputEmail"]).send_keys("emailinvalido")
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputTelefone"]).send_keys(gerar_telefone())
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputMensagem"]).send_keys("Mensagem com email inválido")

    erro = aguarda_elemento(driver, By.CSS_SELECTOR, SELECTORS["mensagemErro"])
    assert "Email is not valid." in erro.text
