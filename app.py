import sys
sys.path.append('..')
import analysis
from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__, template_folder='src')

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['user_message']
    
    # Handle text message
    bot_response = "Bot: Hello! I am a bot. You said: " + user_message
    
    # Handle pasted image
    # if 'image_data' in request.json:
    #     image_data = request.json['image_data']
    #     image_data = image_data.replace('data:image/png;base64,', '')
    #     image_data = image_data.replace('data:image/jpeg;base64,', '')
    #     image_data = image_data.replace(' ', '+')
        
    #     with open('pasted_image.png', 'wb') as f:
    #         f.write(base64.b64decode(image_data))
        
    #     bot_response += " (Image pasted: pasted_image.png)"
    
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
