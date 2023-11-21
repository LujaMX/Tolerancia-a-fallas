from flask import Flask, request

app = Flask(__name__)

@app.route('/sumar', methods=['POST'])
def sumar():
    try:
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        resultado = num1 + num2
        return {'resultado': resultado}
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)