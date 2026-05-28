from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Роут для віддачі нашого HTML файлу
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# REST API Ендпоінт для прийому даних форми
@app.route('/api/submit-repair', methods=['POST'])
def submit_repair():
    data = request.get_json() # Отримуємо дані у форматі JSON
    
    # Базова перевірка даних на стороні сервера
    if not data or not data.get('name') or not data.get('device'):
        return jsonify({"status": "error", "message": "Неповні дані"}), 400
    
    # Імітація збереження в базу даних та формування відповіді
    response_message = f"Дякуємо, {data['name']}! Ваша заявка на ремонт ({data['device']}) прийнята."
    
    # Повертаємо результат на клієнт у форматі JSON
    return jsonify({
        "status": "success", 
        "message": response_message
    }), 200

if __name__ == '__main__':
    # Запускаємо сервер на порту 5000
    app.run(host='0.0.0.0', port=5000)