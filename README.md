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
- Mensagem específica para consultas que excedem o timeout
- Tratamento do limite de consultas (`429` ou `403` com `X-RateLimit-Remaining: 0`)
- Tratamento de nome e biografia ausentes, vazios ou contendo apenas espaços
- Exibição de:
  - username
  - nome
  - biografia
  - quantidade de repositórios públicos
  - seguidores

## Testes

O projeto utiliza `pytest` para testar a validação de username, a apresentação do perfil, o cliente HTTP e o fluxo principal da aplicação.

Atualmente os testes cobrem casos como:

- username válido
- username vazio
- hífen no início
- hífens consecutivos
- caracteres inválidos
- limite de 39 caracteres
- username com mais de 39 caracteres
- hífen no final e hífen válido no meio
- espaços, acentos, underscore e caracteres fora do padrão ASCII
- letras maiúsculas, números e username com um caractere

Os testes do fluxo principal utilizam respostas simuladas, sem acessar a API real, e cobrem:

- importação do módulo sem solicitar entrada ou consultar a API
- consulta com sucesso e remoção de espaços nas bordas da entrada
- username inválido sem realizar consulta
- usuário inexistente e outros erros HTTP
- falha de conexão e timeout
- limite de consultas, sem confundir outros erros `403` com limite esgotado

Os testes de apresentação verificam nome e biografia ausentes ou vazios e a remoção de espaços nas bordas.

Os testes de `github_client.py` simulam `requests.get` para verificar a URL, o timeout de 10 segundos, o retorno da resposta HTTP e a propagação de falhas de rede para o fluxo principal. Todos esses testes funcionam sem requisições reais.

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
│   ├── test_github_client.py
│   ├── test_main.py
│   ├── test_perfil.py
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

A função `main()` é executada apenas quando o arquivo é iniciado diretamente, permitindo importar o módulo nos testes sem solicitar entrada no terminal.

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

Tempo limite excedido:

```text
A consulta demorou demais. Tente novamente.
```

Limite de consultas atingido:

```text
Limite de consultas atingido. Tente novamente mais tarde.
```

Essa mensagem é exibida para respostas `429` ou `403` com o cabeçalho `X-RateLimit-Remaining` igual a `0`. Outros erros HTTP continuam exibindo o código recebido. A aplicação não repete a consulta automaticamente.

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
- exibir repositórios públicos
- exibir linguagens utilizadas
- melhorar a interface do terminal
- continuar refinando a organização do código

## Objetivo

Mais do que construir um GitHub Profile Viewer, este projeto serve como registro do meu aprendizado em programação e desenvolvimento de software através da construção, teste, depuração, refatoração e versionamento de uma aplicação Python real.
