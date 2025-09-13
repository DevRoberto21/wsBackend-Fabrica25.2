# 🐶 PetShop API

Uma API RESTful construída com Django para gerenciar o cadastro de donos de pets e seus respectivos cachorros. Este projeto é uma demonstração de habilidades de desenvolvimento backend, incluindo a implementação de um sistema CRUD, a modelagem de entidades relacionadas e a integração com APIs externas.

## 📘 Funcionalidades

📝 Funcionalidades

- **Gerenciamento de Usuários e Pets:**
  - CRUD completo para a entidade `Pessoa` (donos).
  - CRUD completo para a entidade `Cachorro`.
- **Relacionamentos de Dados:**
  - Cada `Cachorro` é associado a um `Pessoa`, permitindo a navegação de um dono para seus pets.
- **Validação de Dados:**
  - Validação de formato para campos como e-mail e telefone.
- **Consumo de API Externa:**
  - Integração com a [Dog API](https://dog.ceo/dog-api/) para obter dados de raças.

## 💻 Tecnologias

- **Backend:** Python 3.9.6
- **Framework:** Django 4.2.24
- **Dependências:** `requests` para requisições HTTP.
- **Banco de Dados:** SQLite3.

## 🚀 Rodando localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/DevRoberto21/wsBackend-Fabrica25.2.git](https://github.com/DevRoberto21/wsBackend-Fabrica25.2.git)
    cd wsBackend-Fabrica25.2
    ```
2.  **Configurar o ambiente:**

    ```bash
    # Crie e ative o ambiente virtual
    python3 -m venv venv
    source venv/bin/activate

    # Instale as dependências
    pip install -r requirements.txt
    ```

3.  **Executar o projeto:**

    ```bash
    # Aplicar as migrações do banco de dados
    python3 manage.py makemigrations
    python3 manage.py migrate

    # Iniciar o servidor de desenvolvimento
    python3 manage.py runserver
    ```

    O servidor estará rodando em `http://127.0.0.1:8000/`.

## 🏁 Endpoints

| Recurso     | Método   | URL                           | Descrição                          |
| :---------- | :------- | :---------------------------- | :--------------------------------- |
| `Pessoas`   | `POST`   | `/pessoas/criar/`             | Cadastra uma nova pessoa.          |
|             | `GET`    | `/pessoas/`                   | Lista todas as pessoas.            |
|             | `GET`    | `/pessoas/<id>/`              | Detalha uma pessoa específica.     |
|             | `PATCH`  | `/pessoas/atualizar/<id>/`    | Atualiza dados de uma pessoa.      |
|             | `DELETE` | `/pessoas/deletar/<id>/`      | Deleta uma pessoa.                 |
| `Cachorros` | `POST`   | `/cachorros/criar/<id_dono>/` | Cadastra um cachorro para um dono. |
|             | `GET`    | `/cachorros/<id_dono>/`       | Lista os cachorros de um dono.     |
|             | `PATCH`  | `/cachorros/atualizar/<id>/`  | Atualiza um cachorro.              |
|             | `DELETE` | `/cachorros/deletar/<id>/`    | Deleta um cachorro.                |
