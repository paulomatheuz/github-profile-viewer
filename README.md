# GitHub Profile Viewer

Projeto em Python criado com o objetivo de praticar programação na construção de uma aplicação real, evoluindo de forma incremental.

A ideia do projeto é desenvolver um visualizador de perfis do GitHub utilizando a API pública do GitHub.

## Estado atual

Atualmente o programa:

- solicita um username do GitHub pelo terminal;
- remove espaços extras da entrada;
- valida se o username está vazio;
- valida o limite máximo de 39 caracteres;
- rejeita hífen no início ou no fim;
- rejeita dois hífens consecutivos;
- rejeita caracteres que não sejam letras, números ou hífen;
- rejeita caracteres fora do padrão ASCII.

Ainda não há integração com a API do GitHub.

## Tecnologias

- Python
- Git
- GitHub

## Como executar

Clone o repositório e entre na pasta do projeto.

Execute:

```bash
python main.py
```

Digite um username quando solicitado:

```text
Digite um usuario do GitHub: paulomatheuz
```

Exemplo de saída:

```text
Username recebido: paulomatheuz
```

Caso o formato seja inválido:

```text
Username invalido
```

## O que estou praticando

Durante o desenvolvimento deste projeto estou praticando:

- funções;
- parâmetros e retornos;
- condicionais;
- operadores lógicos;
- strings;
- loops;
- validação de dados;
- separação de responsabilidades;
- Git e histórico de commits;
- debugging.

## Próximos passos

O projeto ainda está em desenvolvimento.

Algumas evoluções planejadas são:

- trabalhar com dados de perfis;
- aprender os fundamentos de HTTP;
- consumir a API do GitHub;
- interpretar respostas JSON;
- exibir informações reais de um usuário;
- tratar usuários inexistentes e erros de conexão.

## Objetivo de aprendizado

Mais do que criar uma aplicação pronta, este projeto serve como registro da minha evolução em Python, Git e desenvolvimento de software.
