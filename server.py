from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import asyncio

app = Flask(__name__)
CORS(app)

@app.route('/execute-python', methods=['POST'])
async def execute_python():
    script_path = './bots.py'
    try:
        # Use asyncio.subprocess to run the command asynchronously
        process = await asyncio.create_subprocess_exec('python', script_path,
                                                       stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        result = stdout.decode()  # Decode the output bytes to a string
        return jsonify({'output': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e.output)})

if __name__ == '__main__':
    app.run(debug=True)