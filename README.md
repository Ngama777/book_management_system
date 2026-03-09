# Book Management System 📖

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