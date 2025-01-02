# Use a imagem base do Python (Alpine é uma versão mais leve)
FROM python:3.9-alpine

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt ./ 

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do projeto para o contêiner
COPY . .

# Expõe a porta 5000, que é a padrão do Flask
EXPOSE 5000

# Comando para rodar o servidor Flask
CMD ["python", "services/products.py"]