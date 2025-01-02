import requests
from flask import Flask, jsonify, request, make_response
import jwt
from functools import wraps
import json
import os
from jwt.exceptions import DecodeError, ExpiredSignatureError, InvalidTokenError

# Flask application setup
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
port = int(os.environ.get('PORT', 5000))

BASE_URL = "https://dummyjson.com"

# Function to check for JWT token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'error': 'Authorization token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user_id = data['user_id']
        except ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        except DecodeError:
            return jsonify({'error': 'Error decoding token'}), 401
        return f(current_user_id, *args, **kwargs)
    return decorated

# Load user data
with open('users.json', 'r') as f:
    users = json.load(f)

# Authentication route
@app.route('/auth', methods=['POST'])
def authenticate_user():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Unsupported Media Type'}), 415
    username = request.json.get('username')
    password = request.json.get('password')
    for user in users:
        if user['username'] == username and user['password'] == password:
            token = jwt.encode({'user_id': user['id']}, app.config['SECRET_KEY'], algorithm="HS256")
            response = make_response(jsonify({'message': 'Authentication successful'}))
            response.set_cookie('token', token)
            return response, 200
    return jsonify({'error': 'Invalid username or password'}), 401

# Products endpoint
# Products endpoint
@app.route('/products', methods=['GET'])
@token_required
def get_products(current_user_id):
    try:
        token = request.cookies.get('token')
        if not token:
            return jsonify({'error': 'Token not found in cookies'}), 401
        
        # Decodificar o token
        try:
            decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            print(f"Decoded Token: {decoded_token}")  # Verifique o token decodificado
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        # Fazer requisição à API externa
        print(f"Making request to {BASE_URL}/products with token: {token}")
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(f"{BASE_URL}/products", headers=headers)

        print(f"API Response Status: {response.status_code}")
        print(f"API Response Body: {response.text}")

        if response.status_code != 200:
            return jsonify({'error': response.json()['message']}), response.status_code

        # Processar a resposta dos produtos
        products = []
        for product in response.json().get('products', []):
            # Garantir que 'brand' existe antes de tentar acessá-lo
            product_data = {
                'id': product['id'],
                'title': product['title'],
                'brand': product.get('brand', 'No brand'),  # Usando .get() para evitar KeyError
                'price': product['price'],
                'description': product['description']
            }
            products.append(product_data)

        return jsonify({'data': products}), 200 if products else 204

    except Exception as e:
        print(f"Error: {e}")  # Log de erro
        return jsonify({'error': str(e)}), 500



# Home route
@app.route("/")
def home():
    return "Hello, this is a Flask Microservice"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
