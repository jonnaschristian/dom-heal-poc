
# POC — DOM-Heal

**Prova de Conceito: Self-Healing de elementos do DOM**

Este repositório apresenta uma POC (Prova de Conceito) para validar a biblioteca `dom-heal`, demonstrando como ela pode ser integrada e utilizada em quaisquer frameworks de testes automatizados a partir de cenários reais e controlados. Para uma validação controlada, foram definidos três principais e diferentes frameworks de testes - Cypress, Robot Framework e Selenium.

## 🧑‍🏫 Autor

Elaborado por **Jonnas Christian Sousa de Paiva**, fruto do Trabalho de Conclusão de Curso (TCC).   
Contato: [jonnaschristian@gmail.com](mailto:jonnaschristian@gmail.com)

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
Em caso de dúvidas, assista ao video tutorial no tópico seguinte que replica os passos abaixos.
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


### 5. **Execute os Testes Automatizados (Site A)**
> **Contextualização:**  
> Os testes de automação estão inicialmente configurados para rodar sobre o **Site A**.  
> Dessa forma, **todos os testes devem passar sem erro** nos frameworks, validando que a base do projeto está funcionando corretamente.
>
> Caso algum teste falhe neste estágio, verifique as dependências e a estrutura do projeto, pois todos os seletores e fluxos estão alinhados com o Site A.
>
> Siga os passos abaixo para executar cada suíte de teste:

- #### **A) Testes com Cypress**

   1. Execute todos os testes Cypress:

         **Na raiz do projeto**, execute:
         ```bash
         npx cypress open
         ```
         Isso abrirá a interface gráfica do Cypress, onde você pode selecionar e rodar os testes manualmente (os arquivos ficam em `cypress/e2e`).

   2. Observações:
      - No modo visual, clique em "Run 4 specs" ou sobre cada arquivo de teste individualmente para execução e visualização dos resultados no navegador.
      - Não altere a estrutura da pasta `cypress/`, pois os testes esperam esse caminho padrão.
      - Se algum erro de dependência aparecer, repita `npm install` na raiz do projeto.
      - **Sempre execute os comandos acima na raiz do projeto (onde está o arquivo `package.json`).**

- #### **B) Testes com Robot Framework**

   1. Execute todos os testes Robot Framework:

         Em **RobotFramework/tests/**, execute:
         ```bash
         robot *.robot
         ```
         Isso executará todos os testes `.robot` da suíte, utilizando o ChromeDriver já incluído no projeto.

   2. Observações:
      - Os resultados aparecerão no terminal e um relatório detalhado será gerado nas pastas `log.html` e `report.html`.
      - Não altere a estrutura das pastas, nem mova os arquivos do `RobotFramework/tests/`.
      - Se houver erro relacionado ao driver, verifique se o Google Chrome está instalado e o arquivo `chromedriver.exe` está na pasta correta.
      - **Sempre execute os comandos acima em RobotFramework/tests/.**

- #### **C) Testes com Selenium**

   1. Execute todos os testes Selenium:

         Em **Selenium/tests/**, execute:
         ```bash
         pytest
         ```
         Isso executará todos os testes automatizados com Selenium, utilizando o ChromeDriver incluso no projeto.

   2. Observações:
      - Os resultados dos testes aparecerão diretamente no terminal.
      - Não altere a estrutura das pastas, nem mova os arquivos do `Selenium/tests/`.
      - Se houver erro relacionado ao driver, verifique se o Google Chrome está instalado e o arquivo `chromedriver.exe` está na pasta correta.
      - **Sempre execute os comandos acima em Selenium/tests/.**

### 6. **Simulando falha de testes (migração para o Site B)**

> **Contextualização:**  
> Após validar que todos os testes passam normalmente no **Site A**, o próximo passo é simular um cenário realista de manutenção do sistema: mudanças em atributos dos elementos do front-end que resultam na quebra de seletores utilizados nos testes automatizados.
>
> Para isso, utilizaremos o **Site B**, que contém alterações propositalmente feitas nesses atributos. Ao executar os mesmos testes sobre o Site B, é esperado que ocorram falhas, indicando que os seletores antigos não conseguem mais localizar os elementos modificados.
>
> Esse cenário evidencia a importância de mecanismos automáticos de adaptação de seletores, validando o propósito do DOM-Heal.
>
> Siga os passos abaixo para executar os testes automatizados no Site B e observar o impacto dessas mudanças.

1. **Ajuste a configuração dos testes para apontar para o Site B**
    - Em cada framework de testes, é necessário alterar manualmente a URL base dos testes de `http://localhost:8000/home.html` (Site A) para `http://localhost:8001/home.html` (Site B):
        - **Cypress:**  
          Edite o arquivo `Cypress/support/e2e.js` e altere a URL base utilizada nos comandos `cy.visit()` para `http://localhost:8001/home.html`.
        - **Robot Framework:**  
          Em **cada arquivo de teste `.robot`** na pasta `RobotFramework/tests/`, localize a variável `${URL}` e altere seu valor para `http://localhost:8001/home.html`.
        - **Selenium:**  
          Em **cada arquivo de teste Python** na pasta `Selenium/tests/`, localize a variável `URL` e altere seu valor para `http://localhost:8001/home.html`.

2. **Execute novamente os testes em cada framework**  
   Repita o procedimento do passo 5, agora rodando contra o Site B.

    - **Cypress:**  
      ```bash
      npx cypress open
      ```
      (na `raiz` do projeto)

    - **Robot Framework:**  
      ```bash
      robot *.robot
      ```
      (Na pasta `RobotFramework/tests/`)

    - **Selenium:**  
      ```bash
      pytest
      ```
      (Na pasta `Selenium/tests/`)

3. **Observe os resultados**  
   - É esperado que vários testes **falhem**
   - Isso confirma que as mudanças no front-end **quebraram os seletores antigos**.

> **Se todos os testes passaram no Site B, verifique se a versão correta do site está rodando e se os arquivos realmente estão alterados. O esperado é haver falhas para evidenciar a necessidade do self-healing.**


### 7. **Self-healing (executando o DOM-Heal)**

> **Contextualização:**  
> Com os testes automatizados quebrando no Site B devido às mudanças nos seletores, agora será utilizada a biblioteca **DOM-Heal** para identificar automaticamente os seletores que não funcionam mais e sugerir/adaptar novas referências para os elementos modificados no DOM.
>
> O objetivo é demonstrar que, após a execução do DOM-Heal, é possível atualizar os arquivos de seletores e restaurar o funcionamento dos testes automatizados mesmo após mudanças no front-end.

#### **Passos para executar o DOM-Heal**

1. **Certifique-se de que o servidor local do Site B está ativo em** `http://localhost:8001/home.html`

2. **Execute o comando do DOM-Heal apontando para o arquivo de seletores que deseja corrigir**

    - O comando geral é:

      ```bash
      dom-heal rodar --json "CAMINHO/DO/ARQUIVO.json" --url URL_DA_PAGINA_SITE_B
      ```

    - **Exemplo prático — corrigindo seletores do arquivo `contact.json` do Selenium:**

      ```bash
      dom-heal rodar --json "C:\Users\Jonnas\Documents\dom-heal-poc\Selenium\elements\contact.json" --url http://localhost:8001/contact.html
      ```

    - **Observações:**
      - O parâmetro `--json` deve apontar para o caminho exato do arquivo de seletores utilizado pelo framework.
      - O parâmetro `--url` deve ser a URL da página do Site B referente ao teste (por exemplo, `http://localhost:8001/contact.html`).
      - O comando pode ser rodado em qualquer diretório, desde que o caminho passado nos parâmetros esteja correto.

3. **Verifique o resultado**
    - O arquivo JSON escolhido será automaticamente atualizado com os novos seletores sugeridos.
    - Além disso, será gerado um arquivo chamado **`ElementosAlterados.json`**, contendo **somente os elementos que foram corrigidos** pelo DOM-Heal.
    - Caso deseje manter um backup, salve uma cópia do JSON original antes de rodar o comando.
    - Você pode (e deve) executar todos os arquivos de seletores** utilizados nos diferentes frameworks da POC

4. **Rode novamente os testes automatizados**
    - Após a correção de elementos, execute os testes referentes aos que foram feitos o self-healing.
    - É esperado que, agora, os testes passem normalmente, comprovando a eficácia do mecanismo de self-healing.

> **Dica:**  
> Para uma avaliação mais completa da ferramenta, recomenda-se **fazer o processo de execução do DOM-Heal para cada arquivo de seletores** utilizado nos diferentes frameworks da POC (Cypress, Robot Framework e Selenium), sempre ajustando o caminho do JSON e a URL conforme a página de teste.  
> Dessa forma, é possível analisar a capacidade de self-healing em uma maior diversidade de cenários, verificando como o DOM-Heal se comporta diante das diferentes implementações e estruturas de testes automatizados, e obtendo uma visão abrangente dos benefícios da abordagem proposta.




## 🎥 **Tutorial em Vídeo — Execução Completa da POC**

Para complementar o guia passo a passo acima, disponibilizei um **tutorial em vídeo** mostrando na prática toda a execução da POC, desde a preparação do ambiente até a validação final dos testes corrigidos pelo DOM-Heal.

> **O vídeo cobre:**
> - Clonagem do repositório e instalação dos pré-requisitos;
> - Inicialização dos ambientes dos Sites A e B;
> - Execução dos testes em Cypress, Robot Framework e Selenium;
> - Simulação de falhas (migração para o Site B);
> - Aplicação do mecanismo de self-healing (DOM-Heal);
> - Análise dos resultados e a revalidação dos testes.     


**Assista ao vídeo completo aqui:** 
[]

> **Recomendação:**  
> O vídeo é recomendado para todos os participantes e avaliadores para visualizar detalhes práticos da execução, tirar dúvidas pontuais e comparar com o comportamento esperado documentado no README.