# Microsserviço de Catálogo de Produtos com Python

## Referencia de Como Criar e Implantar Microsserviços com Python

https://kinsta.com/pt/blog/microsservicos-python/

## Desenho

![image](https://github.com/user-attachments/assets/73df2da0-60a5-44c0-9a3f-eeaefd9f78f5)


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

## Explicacao

Este código é um microsserviço em Python utilizando Flask que gerencia um catálogo de produtos. Ele possui as seguintes funcionalidades principais:

1. Autenticação de Usuário (POST /auth): A rota /auth recebe as credenciais de um usuário no corpo da requisição e verifica se essas credenciais correspondem aos dados de um arquivo JSON de usuários. Se as credenciais forem válidas, um token JWT é gerado e enviado ao cliente como um cookie. Esse token será usado para autenticar futuras requisições.

2. Proteção de Rota com JWT (GET /products): A rota /products é protegida por um decorador que exige um token JWT válido para acessar os dados. O token é extraído do cookie da requisição, decodificado e validado. Se o token for válido, o microsserviço consulta uma API externa de produtos, obtendo informações sobre o catálogo, que são então formatadas e retornadas em formato JSON. Se o token for inválido ou ausente, a requisição é rejeitada com um erro de autorização.

3. Integração com API Externa: O microsserviço busca dados de produtos da API pública https://dummyjson.com/products utilizando o módulo requests. Ele faz isso dentro da rota /products, recuperando as informações dos produtos como nome, descrição, preço, marca, etc.

4. Contêinerização: O microsserviço está preparado para ser executado dentro de um contêiner Docker. Um Dockerfile é fornecido para criar a imagem Docker, instalar dependências do projeto e expor a aplicação na porta 5000. Isso permite que o microsserviço seja facilmente implantado em qualquer ambiente com Docker.

Em resumo, este microsserviço proporciona a autenticação de usuários, valida o acesso com JWT, busca dados de produtos de uma API externa e permite a execução e distribuição do aplicativo em contêineres Docker.
