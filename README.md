# 🧪 DOM-Heal POC

Este repositório contém a **Prova de Conceito (POC)** da biblioteca [DOM-Heal](https://github.com/seu-usuario/dom-heal), um motor de self-healing para testes automatizados de interfaces web, desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) de Jonnas Christian — UECE, 2025.

---

## 📌 Objetivo

Validar o funcionamento da biblioteca DOM-Heal em um cenário de testes reais com páginas HTML simples, simulando alterações no DOM entre execuções de testes automatizados.

---

## 🧩 Como funciona a POC — Metodologia de Self-Healing

A Prova de Conceito demonstra a estratégia utilizada pela biblioteca DOM-Heal para tornar testes automatizados de interfaces web mais resilientes a mudanças no DOM.

### Fluxo resumido da metodologia:

1. **Captura de seletores antigos (T0):**
   - O QA mantém um arquivo JSON (ex: `contact.json`) com os seletores dos elementos usados nos testes automatizados na versão antiga do site.

2. **Coleta do DOM atualizado (T1):**
   - A POC acessa o site na versão atual (rodando em `localhost`) e extrai todos os elementos relevantes do DOM, com seus principais atributos (`id`, `name`, `class`, `xpath`, etc).

3. **Comparação inteligente:**
   - Cada seletor antigo é comparado com os elementos do DOM novo usando heurísticas híbridas:
     - **Fuzzy matching:** Mede a similaridade entre os nomes/valores.
     - **Prefix matching:** Dá peso extra se o início do seletor antigo e o candidato no DOM novo forem iguais.
     - **Tradução:** Aplica equivalências conhecidas (ex: `name` ↔ `nome`).
     - **Limiar mínimo por tipo de atributo:** Cada tipo de atributo (`id`, `name`, `class`, `xpath`) só é aceito como novo seletor se a correspondência for suficientemente forte.

4. **Atualização automática dos seletores:**
   - Se for encontrado um novo elemento com alta correspondência, o arquivo JSON do QA é atualizado automaticamente com o novo seletor.
   - Um log detalhado das alterações sugeridas é salvo em `ElementosAlterados.json` para revisão.

5. **Garantia de segurança:**
   - Caso não seja encontrada uma correspondência suficientemente robusta, o seletor antigo é mantido e nenhuma alteração é feita, evitando falsos positivos.

---

## 🚀 Estrutura da POC

- **`cypress/fixtures/elements/`**: contém os arquivos `.json` com os seletores antigos (versão T0).
- **Servidor local (`localhost:8000`)**: simula a versão nova do site (versão T1), onde o DOM pode ter mudado.
- **CLI da biblioteca**: executa o processo de self-healing, compara os seletores antigos com o DOM atual e atualiza os arquivos JSON.

---

## 🛠️ Como rodar a POC

1. Suba o servidor local:
   ```bash
   python -m http.server 8000
