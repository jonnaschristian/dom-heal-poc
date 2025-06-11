*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           JSONLibrary
Library           String

Suite Setup       Carregar Seletores

*** Variables ***
${URL}            http://localhost:8000/home.html
${CHROMEDRIVER}   ../../chromedriver-win64/chromedriver.exe
${SELECTORS}      ${EMPTY}

*** Keywords ***
Carregar Seletores
    ${json}    Load JSON From File    ../elements/contact.json
    Set Suite Variable    ${SELECTORS}    ${json}

Abrir Navegador e Acessar Menu Contato
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service(executable_path="${CHROMEDRIVER}")    sys
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    ${driver}=     Create WebDriver    Chrome    options=${options}    service=${service}
    Go To    ${URL}
    Maximize Browser Window
    Click Element   css=${SELECTORS['menu']}

Fechar Navegador
    Close Browser

Preencher Formulário Contato
    [Arguments]    ${nome}    ${email}    ${telefone}    ${mensagem}
    Input Text    css=${SELECTORS['inputNome']}        ${nome}
    Input Text    css=${SELECTORS['inputEmail']}       ${email}
    Input Text    css=${SELECTORS['inputTelefone']}    ${telefone}
    Input Text    css=${SELECTORS['inputMensagem']}    ${mensagem}

Clicar Botão Enviar
    Wait Until Element Is Visible    css=${SELECTORS['btnEnviar']}    10s
    Wait Until Element Is Enabled    css=${SELECTORS['btnEnviar']}    10s
    Execute JavaScript    document.querySelector('${SELECTORS["btnEnviar"]}').click()


Validar Título Página Contato
    Wait Until Element Is Visible    css=${SELECTORS['tituloContato']}    10s
    Element Text Should Be           css=${SELECTORS['tituloContato']}    Contact Me

*** Test Cases ***
Enviar mensagem com todos os campos válidos com sucesso
    [Setup]    Abrir Navegador e Acessar Menu Contato
    Validar Título Página Contato
    ${nome}=      Generate Random String    10
    ${email}=     Set Variable    teste@gmail.com
    ${telefone}=  Set Variable    (85) 99999-9999
    ${mensagem}=  Set Variable    Mensagem automática gerada por teste Robot
    Preencher Formulário Contato    ${nome}    ${email}    ${telefone}    ${mensagem}
    Clicar Botão Enviar
    Wait Until Element Is Visible    css=${SELECTORS['mensagemSucesso']}    5s
    Element Should Be Visible        css=${SELECTORS['mensagemSucesso']}
    Element Should Contain           css=${SELECTORS['mensagemSucesso']}    Form submission successful!
    [Teardown]     Fechar Navegador

Enviar mensagem sem preencher campos deve dar erro (botão desabilitado)
    [Setup]    Abrir Navegador e Acessar Menu Contato
    Validar Título Página Contato
    ${class}=    Get Element Attribute    css=${SELECTORS['btnEnviar']}    class
    Should Contain    ${class}    disabled
    [Teardown]     Fechar Navegador


Não deve permitir envio se e-mail for inválido
    [Setup]    Abrir Navegador e Acessar Menu Contato
    Validar Título Página Contato
    ${nome}=      Generate Random String    10
    ${telefone}=  Set Variable    (85) 88888-8888
    ${mensagem}=  Set Variable    Teste de envio com email inválido
    Preencher Formulário Contato    ${nome}    emailinvalido    ${telefone}    ${mensagem}
    Wait Until Element Is Visible    css=${SELECTORS['mensagemErro']}    5s
    Element Should Be Visible        css=${SELECTORS['mensagemErro']}
    Element Should Contain           css=${SELECTORS['mensagemErro']}    Email is not valid.
    [Teardown]     Fechar Navegador
