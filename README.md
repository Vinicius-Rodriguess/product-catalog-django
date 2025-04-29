
# 📝 **Product Catalog (Django)**

Este projeto é uma aplicação de catálogo de produtos, desenvolvida com **Django** e **Python**. Ele permite a criação, edição, exclusão e listagem de produtos, com seus respectivos preços.

---

## 🚀 **Funcionalidades**

### **Back-End**
- API REST para criação, edição, exclusão e listagem de produtos.
- Armazenamento de produtos com nome e preço.
- Persistência de dados utilizando **SQLite**.

---

## 🛠️ **Tecnologias Utilizadas**

- **Django**: Framework Python para desenvolvimento web.
- **Python 3.x**: Linguagem de programação utilizada.
- **SQLite**: Banco de dados local utilizado para desenvolvimento.

---

## 🔧 **Como o Sistema Funciona**

1. **Gerenciamento de Produtos**: Endpoints para criação, atualização, exclusão e listagem de produtos.
2. **Persistência de Dados**: Os dados são armazenados no banco de dados SQLite.
3. **Interface Web**: Interface simples para adicionar e editar produtos com nome e preço.

---

## 📋 **Requisitos**

- **Python 3.x**.
- **Django 4.x** ou superior.

---

## 🔧 **Como Configurar o Projeto**

1. Clone este repositório:
   ```bash
   git clone https://github.com/Vinicius-Rodriguess/product-catalog-django.git
   cd product-catalog-django
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rode as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

4. Execute o servidor localmente:
   ```bash
   python manage.py runserver
   ```

5. Acesse a aplicação em seu navegador através de `http://127.0.0.1:8000`.

---

## 💾 **Exemplo de Uso**

- **Produtos**: Utilize a interface para adicionar, listar, editar e excluir produtos.

---

## 📌 **Limitações**

- O projeto usa **SQLite** para desenvolvimento local. Para produção, é necessário configurar outro banco de dados, como PostgreSQL ou MySQL.
- Não há autenticação de usuários implementada.

---

## ✅ **Melhorias Futuras**

- Implementação de autenticação de usuários.
- Integração com outros bancos de dados, como MySQL ou PostgreSQL.
- Melhoria na interface do usuário.

---

## 👨‍💻 **Autor**

**Vinicius Rodrigues**

- GitHub: [Vinicius-Rodriguess](https://github.com/Vinicius-Rodriguess)
- Email: rodrigues.vini.2004@gmail.com