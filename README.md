
# POC — DOM-Heal

**Prova de Conceito: Self-Healing de elementos do DOM**

Este repositório apresenta uma POC (Prova de Conceito) para validar a biblioteca `dom-heal`, demonstrando como ela pode ser integrada e utilizada em quaisquer frameworks de testes automatizados a partir de cenários reais e controlados. Para uma validação controlada, foram definidos três principais e diferentes frameworks de testes - Cypress, Robot Framework e Selenium.



## 🎯 Objetivos da POC

- Demonstrar a capacidade da biblioteca DOM-Heal em identificar e corrigir automaticamente seletores quebrados após mudanças no front-end;

- Validar que a abordagem é agnóstica ao framework: funciona com qualquer suíte de testes web que consome arquivos JSON de elementos.



## 🗂️ Estrutura do Projeto

```
dom-heal-poc/
├── Cypress/
│   ├── e2e/         # Testes automatizados Cypress
│   └── fixtures/    # Arquivos JSON de seletores usados nos testes
│   └── support/     # Arquivos de suporte para os testes automatizados
│
├── RobotFramework/
│   ├── elements/    # Arquivos JSON de seletores usados nos testes
│   └── tests/       # Testes automatizados Robot Framework
│
├── Selenium/
│   ├── elements/    # Arquivos JSON de seletores usados nos testes
│   └── tests/       # Testes automatizados Selenium
│
└── Sites
    ├── A/dist       # Site de referência original
    ├── B/dist       # Site alterado propositalmente (quebra seletores)
```



## 🧪 Frameworks de Teste

A POC inclui o mesmo cenário de teste implementado nos três principais frameworks de automação web:
- **Cypress:** Testes escritos em JavaScript, usando os seletores armazenados nos fixtures JSON.
- **Robot Framework:** Testes em linguagem tabular, também utilizando arquivos JSON de seletores.
- **Selenium (Python):** Testes Python, lendo os seletores de arquivos JSON.

> Todos os frameworks consomem os mesmos arquivos de seletores, reforçando a abordagem universal do DOM-Heal.



## 🕸️ Sites A e B

- **Site A:** É a versão base/original. Os arquivos HTML/CSS/JS aqui representam o funcionamento esperado do sistema — é a referência dos testes.
- **Site B:** É uma versão com pequenas mudanças nos atributos dos elementos (id, class, name, etc), simulando mudanças típicas de manutenção/evolução de front-end e **quebrando** intencionalmente alguns seletores.

> **O objetivo é simular um cenário real: ao migrar os testes para o site B, alguns testes falham pois os seletores antigos não existem mais.**



## 🚀 **Como Executar a POC – Passo a Passo**

### 1. **Clone ou Baixe o Repositório**

Clone este repositório com o comando:

```bash
git clone https://github.com/jonnaschristian/dom-heal-poc.git
```

Ou [baixe o ZIP aqui](https://github.com/jonnaschristian/dom-heal-poc/archive/refs/heads/master.zip).


### 2. **Pré-requisitos**

- **Python 3.13.0 ou superior**  
  - Faça o download em:  
    [Download Python](https://www.python.org/downloads/)

  - Após instalar, verifique a versão:

    ```bash
    python --version
    ```
  - Recomendado criar um ambiente virtual:

    ```bash
    python -m venv venv
    ```
  - Ative o ambiente virtual:

      ```bash
      venv\Scripts\activate
      ```

- **Node.js 22.15.0 ou superior**
  - Faça o download em:  
  [Download Node.js](https://nodejs.org/)
  
  - Verifique a versão:
    ```bash
    node --version
    ```

- **Google Chrome**
  - Faça o download em:  
  [Download Chrome](https://www.google.com/chrome/)

- **WebDriver (ChromeDriver)**
  - Já está incluso no projeto: não precisa instalar nem baixar nada extra.
  - O arquivo está em: `chromedriver-win64/chromedriver.exe`
  - Usado automaticamente nos testes Robot Framework e Selenium.
  - **Obrigatório:** Ter o Google Chrome instalado.

- **Cypress e dependências**
  - Todas as bibliotecas necessárias (`cypress`, `@faker-js/faker`, `cypress-xpath`) já estão declaradas no arquivo `package.json`.
  - Na raiz do projeto, rode:

    ```bash
    npm install
    ```
  - **Importante:** Sempre execute esse comando na raiz do projeto, e não dentro da pasta `cypress/`.

- **Robot Framework e dependências**  

   Instale todas as bibliotecas necessárias com:

    ```bash
    pip install robotframework
    pip install robotframework-seleniumlibrary
    pip install robotframework-jsonlibrary
    ```

- **Selenium e dependências**

   Instale tudo o que precisa com:

    ```bash
    pip install selenium pytest
    ```


### 3. **Instale a biblioteca DOM-Heal**

   Com o ambiente virtual ativo, instale a biblioteca self-healing DOM-Heal:

   ```bash
   pip install dom-heal
   ```


### 4. **Inicie os Ambientes dos Sites A e B**

Antes de rodar qualquer teste, é necessário subir os servidores locais dos sites A e B em portas diferentes.
- #### **Inicie o servidor local do Site A**
   1. Abra um terminal e navegue até a pasta `dist` do Site A:

      ```bash
      cd Sites/A/dist
      ```
   2. Execute o servidor local na porta 8000:

      ```bash
      python -m http.server 8000
      ```
   3. O Site A ficará disponível em:

      ```bash
      http://localhost:8000/home.html
      ```
   
- #### **Inicie o servidor local do Site B**
   1. Abra outro terminal e navegue até a pasta `dist` do Site B:

      ```bash
      cd Sites/B/dist
      ```
   2. Execute o servidor local na porta 8001:

      ```bash
      python -m http.server 8001
      ```
   3. O Site B ficará disponível em:

      ```bash
      http://localhost:8001/home.html
      ```




### 5. **Execute os Testes Automatizados**
> **Contextualização:**  
> Os testes de automação estão inicialmente configurados para rodar sobre o **Site A**.  
> Dessa forma, **todos os testes devem passar sem erro** nos frameworks, validando que a base do projeto está funcionando corretamente.
>
> Caso algum teste falhe neste estágio, verifique as dependências e a estrutura do projeto, pois todos os seletores e fluxos estão alinhados com o Site A.
>
> Siga os passos abaixo para executar cada suíte de teste:

- #### **A) Testes com Cypress**

   1. Abra o Cypress:

         **Na raiz do projeto**, execute:
         ```bash
         npx cypress open
         ```
         Isso abrirá a interface gráfica do Cypress, onde você pode selecionar e rodar os testes manualmente (os arquivos ficam em `cypress/e2e`).

   2. Observações:
      - No modo visual, clique sobre cada arquivo de teste para executá-lo e ver os resultados no navegador.
      - Não altere a estrutura da pasta `cypress/`, pois os testes esperam esse caminho padrão.
      - Se algum erro de dependência aparecer, repita `npm install` na raiz do projeto.
      - **Sempre execute os comandos acima na raiz do projeto (onde está o arquivo `package.json`).**

- #### **B) Testes com Robot Framework**

   1. Execute todos os testes Robot Framework:

         **Na raiz do projeto**, execute:
         ```bash
         robot RobotFramework/tests/
         ```
         Isso executará todos os testes `.robot` da suíte, utilizando o ChromeDriver já incluído no projeto.

   2. Observações:
      - Os resultados aparecerão no terminal e um relatório detalhado será gerado nas pastas `log.html` e `report.html`.
      - Sempre execute o comando a partir da raiz do projeto para garantir que o caminho do ChromeDriver seja reconhecido automaticamente.
      - Não altere a estrutura das pastas, nem mova os arquivos do `RobotFramework/tests/`.
      - Se houver erro relacionado ao driver, verifique se o Google Chrome está instalado e o arquivo `chromedriver.exe` está na pasta correta.

- #### **C) Testes com Selenium**

   1. Execute todos os testes Selenium:

         **Na raiz do projeto**, execute:
         ```bash
         pytest Selenium/tests/
         ```
         Isso executará todos os testes automatizados com Selenium, utilizando o ChromeDriver incluso no projeto.

   2. Observações:
      - Os resultados dos testes aparecerão diretamente no terminal.
      - Sempre execute o comando a partir da raiz do projeto para garantir que o caminho do ChromeDriver seja reconhecido automaticamente.
      - Não altere a estrutura das pastas, nem mova os arquivos do `Selenium/tests/`.
      - Se houver erro relacionado ao driver, verifique se o Google Chrome está instalado e o arquivo `chromedriver.exe` está na pasta correta.





### 6. **Simulando quebra de testes**

1. Altere o alvo dos testes para o **Site B** (estrutura com atributos modificados).
2. Execute os testes novamente. Alguns devem falhar devido a seletores desatualizados.
3. Rode o DOM-Heal para atualizar os seletores automaticamente:
    ```bash
    dom-heal rodar --json ./Cypress/fixtures/home.json --url http://localhost:8000/siteB/home.html
    ```
4. Valide que o arquivo JSON foi atualizado e rode novamente os testes – agora devem passar mesmo após as mudanças no DOM.

---

### 7. **(Opcional) Assista ao tutorial em vídeo**

Assista ao passo a passo em vídeo:  
[Coloque o link aqui após gravar]

---

## ℹ️ **Dicas e Observações**

- Cada framework possui sua própria pasta de seletores (sempre formato JSON).
- Recomenda-se usar um arquivo de seletores por página.
- A biblioteca DOM-Heal é chamada externamente, via CLI.

---

## ❓ **Dúvidas Frequentes**

- **Erro ao instalar dependências?**  
  Verifique as versões do Python/Node.js e se está no diretório correto.

- **Problemas ao rodar comandos?**  
  Confira se está no ambiente virtual e se todas as dependências foram instaladas.

- **Não sabe por onde começar?**  
  Siga o passo a passo acima ou assista ao vídeo do tutorial.


---

## 🕸️ Sites A e B

- **Site A:** É a versão base/original. Os arquivos HTML/CSS/JS aqui representam o funcionamento esperado do sistema — é a referência dos testes.
- **Site B:** É uma versão com pequenas mudanças nos atributos dos elementos (id, class, name, etc), simulando mudanças típicas de manutenção/evolução de front-end e **quebrando** intencionalmente alguns seletores.

> **O objetivo é simular um cenário real: ao migrar os testes para o site B, alguns testes falham pois os seletores antigos não existem mais.**

---

## 🧪 Frameworks de Teste

A POC inclui o mesmo cenário de teste implementado nos três principais frameworks de automação web:

- **Cypress:** Testes escritos em JavaScript, usando os seletores armazenados nos fixtures JSON.
- **Robot Framework:** Testes em linguagem tabular, também utilizando arquivos JSON de seletores.
- **Selenium (Python):** Testes Python, lendo os seletores de arquivos JSON.

> Todos os frameworks consomem os mesmos arquivos de seletores, reforçando a abordagem universal do DOM-Heal.

---

## ⚙️ Fluxo de Uso/Revalidação

1. **Execute os testes automatizados no Site A**  
   (devem passar, já que os seletores batem com o DOM atual)

2. **Altere o alvo dos testes para o Site B**  
   (alguns testes vão falhar, pois os seletores estão desatualizados)

3. **Rode o DOM-Heal passando o JSON e a URL do Site B**  
   ```bash
   dom-heal rodar --json ./Cypress/fixtures/home.json --url http://localhost:8000/siteB/home.html
   ```

4. **Valide que o JSON foi atualizado**  
   O arquivo agora contém os seletores ajustados para o Site B.  
   O log de alterações detalha o que mudou.

5. **Rode novamente os testes com o JSON atualizado**  
   (Os testes devem passar mesmo com as alterações do front-end, sem necessidade de intervenção manual)

---

## 📝 Observações Importantes

- **Cada framework tem sua própria pasta de elementos/fixtures, mas o formato é sempre JSON**.
- É fundamental usar um arquivo de seletores por página para facilitar o controle das alterações.
- A biblioteca DOM-Heal é externa ao projeto de testes: pode ser chamada como CLI ou integrada via adaptação.

---

## 👨‍💻 Requisitos

- Node.js (para Cypress)
- Python 3.7+ (para Robot e Selenium)
- Google Chrome instalado localmente

---

## 🧑‍🏫 Autor

Prova de Conceito por **Jonnas Christian Sousa de Paiva**  
Contato: [jonnaschristian@gmail.com](mailto:jonnaschristian@gmail.com)

---
