# Microsserviço de Catálogo de Produtos com Python

## Referencia de Como Criar e Implantar Microsserviços com Python

https://kinsta.com/pt/blog/microsservicos-python/

Este projeto demonstra como criar e implantar microsserviços com Python, usando o framework Flask para desenvolver um microsserviço que gerencia um catálogo de produtos. O microsserviço busca dados de produtos de uma fonte externa e retorna as informações no formato JSON, permitindo integração com outros componentes do sistema de eCommerce.

## O que são Microsserviços?

Microsserviços são serviços independentes e autônomos dentro de um aplicativo, cada um atendendo a necessidades comerciais específicas. Eles se comunicam por meio de APIs leves ou corretores de mensagens, formando um sistema abrangente.

### Vantagens dos Microsserviços:
- **Flexibilidade e dimensionamento**: O desacoplamento de serviços individuais permite o dimensionamento de componentes específicos que enfrentam alto tráfego.
- **Modularidade do código**: Cada serviço pode usar uma pilha de tecnologia discreta, permitindo o uso das melhores ferramentas para cada serviço.

### Desafios dos Microsserviços:
- **Monitoramento de múltiplos serviços**: A gestão de múltiplos serviços pode ser desafiadora, especialmente durante falhas ou problemas de rede.
- **Custo**: O desenvolvimento de microsserviços pode ser mais caro devido à necessidade de gerenciar várias infraestruturas e recursos para cada serviço.

## Funcionalidade do Projeto

Este microsserviço é responsável por:
- Gerenciar o catálogo de produtos.
- Buscar dados de produtos de uma fonte externa (como a API pública `https://dummyjson.com/products`).
- Retornar os dados dos produtos em formato JSON para outros serviços ou interfaces.

### Requisitos

Para rodar o projeto, certifique-se de que você tenha os seguintes pré-requisitos:
- Python 3.9 ou superior
- Flask
- Docker Desktop
- Postman (para testar as APIs)

### Como Rodar o Projeto

#### 1. Clonando o Repositório

Primeiro, clone este repositório para sua máquina local:

```bash
git clone <URL_do_repositório>
cd <diretório_do_repositório>
```

2. Instalando as Dependências
Instale as dependências necessárias com pip. Se você não tiver o requirements.txt pronto, crie um arquivo com as dependências:

```bash
pip install -r requirements.txt
```

3. Rodando a Aplicação Localmente
Para rodar a aplicação Flask localmente, use o seguinte comando:

```bash
python services/products.py
```
A aplicação estará disponível em http://127.0.0.1:5000.

4. Usando Docker para Contêinerizar a Aplicação
Para facilitar a implantação, você pode contêinerizar o microsserviço utilizando Docker.

Passo 1: Construir a Imagem Docker

No diretório raiz do projeto, crie o arquivo Dockerfile com o seguinte conteúdo:

```bash
dockerfile
Copiar código
FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "services/products.py"]
```

Passo 2: Criar a Imagem Docker

Execute o comando abaixo para criar a imagem do Docker:

```bash
docker build -t flask-microservice .
```

Passo 3: Rodar o Contêiner

Depois de construir a imagem, rode o contêiner com o seguinte comando:

```bash
docker run -p 5000:5000 flask-microservice
```

A aplicação estará disponível em http://localhost:5000.

Testando a API com Postman
Autenticação (POST /auth):

No Postman, crie uma requisição POST para http://localhost:5000/auth.
No corpo da requisição, envie um JSON com username e password.
Se autenticado corretamente, o servidor retornará um token JWT.
Consultando Produtos (GET /products):

Após a autenticação, faça uma requisição GET para http://localhost:5000/products.
Adicione o token JWT nos cookies ou nos cabeçalhos da requisição para acessar os dados de produtos.
Contribuindo
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.
