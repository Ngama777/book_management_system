# Book Management System 📖
[Portugês](#português) | [English](#english)

Português
Um sistema de gerenciamento de livros desenvolvido com *Python* e o framework *Flask*. O projeto foca na implementação de uma API REST completa com operações CRUD, utilizando uma arquitetura organizada com Controllers e persistência de dados em arquivos JSON.

## 🚀 Funcionalidades
* *Adicionar Livros*: Rota POST para cadastrar novos títulos com geração de ID automático.
* *Consultar Acervo*: Rota GET para listar todos os livros ou buscar um específico por ID.
* *Atualizar Informações*: Rota PUT para editar detalhes como título, autor e gênero de livros existentes.
* *Remover Títulos*: Rota DELETE para exclusão lógica de registros do sistema.

## 🛠️ Tecnologias Utilizadas
* *Linguagem*: Python 3.x
* *Framework*: Flask
* *Persistência*: Arquivo JSON (Data Handling)
* *Testes de API*: Insomnia

## 📁 Estrutura do Projeto
O projeto segue o padrão de organização modular para facilitar a manutenção:
* app.py: Ponto de entrada e configuração das rotas.
* controllers/: Onde reside a lógica de controle e manipulação das requisições.
* data/: Armazenamento persistente (arquivo book.json).

## 🔧 Como Executar
1. Clone este repositório.
2. Certifique-se de ter o Python instalado.
3. Instale o Flask: 
   ```bash
   pip install flask

English

This project is a REST API developed with Python and the Flask framework to manage a book collection. The system allows performing all fundamental CRUD operations (Create, Read, Update, Delete) with data persistence in JSON files.

##​🚀 Features
​Create Books: POST route that receives data and generates an automatic ID for the new record.
​List Collection: GET route to view all registered books or a specific title by ID.
​Update Data: PUT route that allows editing information for existing books.
​Delete Books: DELETE route to permanently remove records from the data file.

​##🛠️ Technologies / Tecnologias
​Python 3.x
​Flask
​JSON (Persistence/Persistência)
​Insomnia (API Testing/Testes)

##​📁 Structure / Estrutura
​app.py: Entry point and route configuration / Ponto de entrada e configuração de rotas.
​controllers/: Business logic and data handling / Lógica de negócio e manipulação de dados.
​data/: Storage (book.json) / Armazenamento (book.json).
​Developed by Pandoro Gama – Designer & Software Engineering Student.