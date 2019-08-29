# SIGEC - Sistema de Gerenciamento de Clientes

------



#### Este projeto teve como foco a criação de um sistema web para gestão de clientes.



## Acesso online

O projeto encontra-se online, por intermédio da plataforma Heroku, no seguinte link:  [**https://sn-sigec.herokuapp.com**](https://sn-sigec.herokuapp.com/).

Para poder entrar no sistema, crie uma conta de acesso na tela de cadastro e faça o login com os dados registrados ou realize o login por intermédio do facebook.



## Instalação e execução local

##### **Requisitos**:

- **Python** >= 3.6: https://www.python.org/downloads/

- **Django** >= 2.1: https://www.djangoproject.com/download/

  

Ao selecionar o diretório em que deseja fazer o download do projeto, digite o comando abaixo em seu terminal:

```t
git clone https://github.com/glauciocorreia/sn-challenge.git
```

Posteriormente, antes de entrar na pasta do projeto baixado, crie e ative a virtualenv:

```
python -m venv venv
cd venv
cd Scripts
activate
cd ..
cd ..
```

Entre no diretório e faça a instalação do Django:

```shell
cd sn-challenge
pip install django
```

Agora, faça a instalação das dependências do projeto:

```shell
pip install -r requirements-dev.txt
```

Depois de instalar as dependências, crie um arquivo na pasta raiz do projeto, com o nome **.env**. Abra o  arquivo e coloque as duas linhas abaixo, salvando antes de fechar:

```
SECRET_KEY=106!s^t(9v)@!h*#(z7iwfo^9hzn#t&hn5l#-4bst4p^9zhvy)
DEBUG=True
```

Por fim, é só executar o projeto:

```shell
python manage.py runserver
```