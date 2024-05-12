from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/execute-python', methods=['POST'])
def execute_python():
    script_path = './bots.py'
    try:
        result = subprocess.check_output(['python', script_path], stderr=subprocess.STDOUT, text=True)
        return jsonify({'output': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e.output)})

if __name__ == '__main__':
    app.run(debug=True)