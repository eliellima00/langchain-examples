# Exemplos LangChain

Este projeto contém uma coleção de exemplos e exercícios para o curso de LangChain.

## 🚀 Começando

### Pré-requisitos

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (para gerenciamento de pacotes)

### 📦 Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/eliellima00/langchain-examples.git
   cd langchain-examples
   ```

2. **Crie um ambiente virtual e instale as dependências usando o uv:**

   ```bash
   uv sync
   ```

3. **Configure suas variáveis de ambiente:**

   Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API:

   ```bash
   cp .env.example .env
   ```

   Em seguida, edite o arquivo `.env` com suas credenciais.

### 🏃‍♀️ Executando os Exemplos

O projeto contém vários exemplos nos diretórios `notebooks` e `studio`.

- **Jupyter Notebooks:**

  Para executar os notebooks Jupyter no diretório `notebooks`, você pode iniciar um servidor Jupyter Notebook:

  ```bash
  uv run jupyter notebook
  ```

- **Langsmith Studio:**

  O diretório `studio` contém um agente LangChain que pode ser usado com o Langsmith Studio.

  Para executar o agente com o Langsmith Studio, você precisa ter o `langgraph-cli` instalado. Em seguida, você pode usar o comando `langgraph` para interagir com o agente.

  ```bash
  uv run langgraph dev
  ```

  Para mais informações sobre como usar o Langsmith Studio, consulte a [documentação oficial](https://docs.smith.langchain.com/studio).
