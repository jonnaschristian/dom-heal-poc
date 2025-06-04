import json
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = r"C:\Users\Jonnas\Documents\dom-heal-poc\chromedriver-win64\chromedriver.exe"
URL = "http://localhost:8000"

with open("../elements/contact.json", encoding="utf-8") as f:
    SELECTORS = json.load(f)

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

service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def abrir_menu_contato():
    driver.get(URL)
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, SELECTORS["menu"]).click()
    aguarda_elemento(driver, By.CSS_SELECTOR, SELECTORS["tituloContato"])

try:
    # Teste 1: Enviar mensagem com todos os campos válidos
    abrir_menu_contato()
    assert "Contact Me" in driver.find_element(By.CSS_SELECTOR, SELECTORS["tituloContato"]).text

    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputNome"]).send_keys(gerar_nome())
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputEmail"]).send_keys("teste@gmail.com")
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputTelefone"]).send_keys(gerar_telefone())
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputMensagem"]).send_keys("Mensagem de teste via Selenium")
    btn = driver.find_element(By.CSS_SELECTOR, SELECTORS["btnEnviar"])
    driver.execute_script("arguments[0].click();", btn)  # Clique via JS para evitar interceptação

    sucesso = aguarda_elemento(driver, By.CSS_SELECTOR, SELECTORS["mensagemSucesso"])
    assert "Form submission successful!" in sucesso.text
    print("Teste 1 PASSOU")

    # Teste 2: Enviar mensagem sem preencher campos deve dar erro
    abrir_menu_contato()
    assert "Contact Me" in driver.find_element(By.CSS_SELECTOR, SELECTORS["tituloContato"]).text

    btn = driver.find_element(By.CSS_SELECTOR, SELECTORS["btnEnviar"])
    classes = btn.get_attribute("class")
    assert "disabled" in classes, "Botão não está desabilitado como esperado"
    print("Teste 2 PASSOU")

    # Teste 3: Não deve permitir envio se e-mail for inválido
    abrir_menu_contato()
    assert "Contact Me" in driver.find_element(By.CSS_SELECTOR, SELECTORS["tituloContato"]).text

    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputNome"]).send_keys(gerar_nome())
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputEmail"]).send_keys("emailinvalido")
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputTelefone"]).send_keys(gerar_telefone())
    driver.find_element(By.CSS_SELECTOR, SELECTORS["inputMensagem"]).send_keys("Mensagem com email inválido")

    erro = aguarda_elemento(driver, By.CSS_SELECTOR, SELECTORS["mensagemErro"])
    assert "Email is not valid." in erro.text
    print("Teste 3 PASSOU")

finally:
    driver.quit()
