
# Batalha Naval

Esse projeto é uma implementação simples do jogo Batalha Naval, desenvolvido em python para a disciplina de **Verificação e Validação**.
## Desenvolvedores

- [@hugorplobo](https://www.github.com/hugorplobo) - Antônio Hugo
- [@Joaopfq](https://www.github.com/Joaopfq) - João Paulo
- [@MLeandr0](https://www.github.com/MLeandr0) - Matheus Leandro


## Histórias de usuário

Você ver as histórias de usuário da aplicação [aqui](#) juntamente com os cenários de validação do BDD.


## Como executar

O projeto usa o [Poetry](https://python-poetry.org/) para o gerenciamento de dependências e ambientes virtuais. Para instruções de como instalá-lo acesse [aqui](https://python-poetry.org/docs/#installation).

- Utilizando o poetry (**recomendado**):
```bash
  $ poetry install
  $ poetry run pytest
  $ poetry run start
```

- Sem o poetry:
```bash
  $ source .venv/bin/activate
  $ pytest
  $ python3 batalha_naval/__init__.py
  $ deactivate
```