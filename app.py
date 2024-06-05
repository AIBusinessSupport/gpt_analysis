import sys
sys.path.append('..')
import config
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
    print(user_message)
    res = ''
    if config.new_image_bool:
        gpt_ana = analysis.Conversation(config.API_KEY)
        res = gpt_ana.handler('image')
    # Handle text message
    else:
        gpt_ = config.gpt_conversation
        res = gpt_.handler(user_message)
    
    bot_response = res
    
    # Handle pasted image
    # if 'image_data' in request.json:
    #     image_data = request.json['image_data']
    #     image_data = image_data.replace('data:image/png;base64,', '')
    #     image_data = image_data.replace('data:image/jpeg;base64,', '')
    #     image_data = image_data.replace(' ', '+')
        
    #     with open('pasted_image.png', 'wb') as f:
    #         f.write(base64.b64decode(image_data))
        
    #     bot_response += " (Image pasted: pasted_image.png)"
    config.gpt_conversation = gpt_ana
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
