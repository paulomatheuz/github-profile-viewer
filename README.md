# GitHub Profile Viewer

Aplicação de terminal desenvolvida em Python para consultar e exibir informações públicas de usuários do GitHub através da GitHub REST API.

O projeto foi construído de forma incremental com foco no aprendizado prático de Python, APIs, HTTP, JSON, testes automatizados, Git e GitHub.

## Status

✅ **V1.0 publicada**

A primeira versão funcional do projeto está marcada com a tag `v1.0`.

O desenvolvimento continua após a V1, com melhorias na organização do código e adição de testes automatizados com `pytest`.

## Funcionalidades

- Entrada de username pelo terminal
- Remoção de espaços extras
- Validação do formato do username
- Limite máximo de 39 caracteres
- Validação de hífens
- Rejeição de caracteres inválidos
- Rejeição de caracteres fora do padrão ASCII
- Consulta à API pública do GitHub
- Tratamento de usuário inexistente (`404`)
- Tratamento de outros status HTTP
- Tratamento de falhas de conexão e timeout
- Tratamento de campos ausentes no perfil
- Exibição de:
  - username
  - nome
  - biografia
  - quantidade de repositórios públicos
  - seguidores

## Testes

O projeto utiliza `pytest` para testar as regras de validação de username.

Atualmente os testes cobrem casos como:

- username válido
- username vazio
- hífen no início
- hífens consecutivos
- caracteres inválidos
- limite de 39 caracteres
- username com mais de 39 caracteres

Para executar os testes:

```bash
python -m pytest
```

## Tecnologias

- Python
- Requests
- Pytest
- Git
- GitHub
- GitHub REST API
- JSON
- HTTP

## Estrutura do projeto

```text
github-profile-viewer/
├── tests/
│   └── test_validators.py
├── .gitignore
├── github_client.py
├── main.py
├── README.md
├── requirements.txt
└── validators.py
```

### `main.py`

Responsável por coordenar o fluxo principal da aplicação.

### `validators.py`

Contém as regras de validação do username.

### `github_client.py`

Responsável pela comunicação com a API do GitHub.

### `tests/`

Contém os testes automatizados do projeto.

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/paulomatheuz/github-profile-viewer.git
```

Entre na pasta:

```bash
cd github-profile-viewer
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação

```bash
python main.py
```

Digite um username:

```text
Digite um usuário do GitHub: paulomatheuz
```

Exemplo de saída:

```text
Usuário: paulomatheuz
Nome: Não informado
Biografia: Software Engineering Student.
Repositórios públicos: 7
Seguidores: 11
```

Os dados são obtidos diretamente da API do GitHub e podem mudar.

## Tratamento de erros

Username inválido:

```text
Username inválido
```

Usuário inexistente:

```text
Usuário não encontrado
```

Falha de conexão:

```text
Erro de conexão. Tente novamente.
```

## Conceitos praticados

Durante o desenvolvimento deste projeto pratiquei:

- variáveis e tipos
- strings
- condicionais
- operadores lógicos
- loops
- listas e dicionários
- funções
- parâmetros e retornos
- escopo
- módulos e imports
- validação de dados
- tratamento de exceções
- HTTP e status codes
- consumo de APIs
- JSON
- Requests
- testes automatizados com pytest
- debugging
- refatoração
- separação de responsabilidades
- Git e GitHub

## Histórico de desenvolvimento

O histórico de commits foi mantido como uma linha do tempo da evolução do projeto e do meu aprendizado.

O projeto começou apenas validando um username e evoluiu gradualmente para:

1. validação de entrada;
2. consumo da API do GitHub;
3. interpretação de JSON;
4. tratamento de erros;
5. publicação da V1;
6. testes automatizados;
7. separação do código em módulos.

## Versão

A primeira versão funcional está marcada com:

```text
v1.0
```

O código presente na branch `master` pode conter melhorias realizadas após essa versão.

## Próximos passos

Possíveis evoluções futuras:

- ampliar a cobertura de testes
- testar o cliente da API sem depender de requisições reais
- exibir repositórios públicos
- exibir linguagens utilizadas
- melhorar a interface do terminal
- continuar refinando a organização do código

## Objetivo

Mais do que construir um GitHub Profile Viewer, este projeto serve como registro do meu aprendizado em programação e desenvolvimento de software através da construção, teste, depuração, refatoração e versionamento de uma aplicação Python real.