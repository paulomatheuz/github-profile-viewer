# GitHub Profile Viewer

Aplicação de terminal desenvolvida em Python para consultar e exibir informações públicas de usuários do GitHub através da GitHub REST API.

O projeto foi construído de forma incremental com foco no aprendizado prático de Python, APIs, HTTP, JSON, Git e GitHub.

## Status

✅ V1.0 concluída e publicada.

A primeira versão funcional do projeto já está disponível no GitHub e marcada com a tag `v1.0`.

## Funcionalidades

- Entrada de username pelo terminal
- Validação básica do formato do username
- Remoção de espaços extras
- Limite máximo de 39 caracteres
- Validação de hífens
- Rejeição de caracteres inválidos
- Rejeição de caracteres fora do padrão ASCII
- Consulta à API pública do GitHub
- Tratamento de usuário inexistente
- Tratamento de outros status HTTP
- Tratamento de falhas de conexão e timeout
- Tratamento de campos ausentes no perfil
- Exibição de:
  - username
  - nome
  - biografia
  - repositórios públicos
  - seguidores

## Tecnologias

- Python
- Requests
- Git
- GitHub
- GitHub REST API
- JSON
- HTTP

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

Outros erros HTTP:

```text
Erro ao buscar usuário: <status>
```

## Estrutura do projeto

```text
github-profile-viewer/
├── main.py
└── README.md
```

A estrutura foi mantida simples de propósito para acompanhar a evolução gradual do projeto.

## Conceitos praticados

Durante o desenvolvimento deste projeto pratiquei:

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
- validação de dados
- tratamento de exceções
- tratamento de dados ausentes
- HTTP
- requisições `GET`
- status codes
- consumo de APIs
- JSON
- biblioteca Requests
- debugging
- Git e GitHub
- refatoração
- separação de responsabilidades

## Histórico de desenvolvimento

O histórico de commits deste repositório foi mantido como uma linha do tempo da evolução do projeto e do meu aprendizado.

A aplicação começou com uma validação simples de username e evoluiu gradualmente até:

- realizar requisições reais à API do GitHub;
- interpretar respostas JSON;
- tratar usuários inexistentes;
- tratar falhas de conexão;
- organizar responsabilidades em funções;
- chegar à primeira versão funcional publicada.

## Versão atual

`v1.0`

Esta versão representa a primeira entrega funcional do projeto.

## Próximas versões

Possíveis evoluções futuras incluem:

- exibição de repositórios públicos
- linguagens utilizadas nos repositórios
- testes automatizados
- melhorias na interface de terminal
- organização em múltiplos módulos
- novas informações do perfil
- melhorias no tratamento de erros

## Objetivo do projeto

Mais do que construir um GitHub Profile Viewer, este projeto serviu como exercício prático para aprender a estruturar, testar, depurar, versionar e evoluir uma aplicação Python real.

O histórico do repositório também funciona como registro da minha evolução durante o desenvolvimento.