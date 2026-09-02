# GitHub Profile Viewer

Projeto em Python para consultar e exibir informações públicas de usuários do GitHub através da API oficial do GitHub.

O projeto está sendo desenvolvido de forma incremental com foco no aprendizado prático de Python, APIs, HTTP, JSON, Git e GitHub.

## Status

🚧 Em desenvolvimento — pré-V1 funcional.

Atualmente o programa já consegue validar um username, consultar a API do GitHub e exibir informações reais de um perfil.

## Funcionalidades atuais

- Entrada de username pelo terminal
- Remoção de espaços extras com `strip()`
- Validação básica do formato do username
- Limite máximo de 39 caracteres
- Validação de hífen no início ou final
- Validação de hífens consecutivos
- Rejeição de caracteres inválidos
- Rejeição de caracteres fora do padrão ASCII
- Consulta à API pública do GitHub
- Tratamento de usuário encontrado (`200`)
- Tratamento de usuário inexistente (`404`)
- Tratamento básico de outros status HTTP
- Conversão da resposta JSON para dados Python
- Exibição de:
  - username
  - nome
  - biografia
  - quantidade de repositórios públicos
  - seguidores
- Tratamento de nome ou biografia não informados

## Tecnologias

- Python
- Requests
- Git
- GitHub
- GitHub REST API

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/paulomatheuz/github-profile-viewer.git
```

Entre na pasta:

```bash
cd github-profile-viewer
```

### 2. Instale a dependência

O projeto utiliza a biblioteca `requests` para realizar requisições HTTP.

```bash
pip install requests
```

### 3. Execute

```bash
python main.py
```

Digite um username do GitHub quando solicitado:

```text
Digite um usuario do GitHub: paulomatheuz
```

Exemplo de saída:

```text
Usuário: paulomatheuz
Nome: Não informado
Biografia: Software Engineering Student.
Repositórios públicos: 7
Seguidores: 11
```

Os valores exibidos são obtidos diretamente da API do GitHub e podem mudar.

## Exemplo de usuário inexistente

```text
Digite um usuario do GitHub: usuario-que-nao-existe-123456789xyz
Usuário não encontrado
```

## Conceitos praticados

Durante o desenvolvimento estou praticando:

- variáveis e tipos
- strings
- condicionais
- operadores `and`, `or` e `not`
- loops
- listas
- dicionários
- funções
- parâmetros e retornos
- escopo de variáveis
- tratamento de dados ausentes
- JSON
- HTTP
- requisições `GET`
- status codes
- consumo de APIs
- debugging
- Git e GitHub
- organização incremental de código

## Estrutura atual

```text
github-profile-viewer/
├── main.py
└── README.md
```

A estrutura ainda é simples de propósito. O código será reorganizado conforme o projeto crescer e essa necessidade surgir naturalmente.

## Próximos passos

Algumas melhorias previstas para chegar à V1:

- tratar erros de conexão
- melhorar a organização das responsabilidades do código
- melhorar a apresentação das informações no terminal
- revisar casos extremos
- realizar testes finais da aplicação
- revisar documentação da V1

## Objetivo do projeto

O objetivo não é apenas criar um visualizador de perfis.

Este repositório também registra minha evolução aprendendo Python e desenvolvimento de software através da construção de um projeto real, mantendo um histórico de commits que acompanha essa evolução.
