from flask import Flask, request, json, jsonify

bot = Flask(__name__)
    
# Endpoint homepage   
@bot.route('/')
def homepage() -> str:
    """ URL primary"""
    return 'Bem vindo a pagina inicial do bot'

# Endpoint webhook
@bot.route('/webhook', methods=['POST'])
def handle_webhook() -> json:
    try:
        information = request.get_json()
        return jsonify(f'content: {information}',200)
    except ValueError as ve:
        return jsonify(f'Json Error: {ve}',404)

if __name__=='__main__':
    bot.run(debug=True)