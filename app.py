from flask import Flask, render_template, request, jsonify
from test import MistralAssistant  # Importation de la classe depuis test.py

app = Flask(__name__)

# Initialisation de l'assistant Mistral
assistant = MistralAssistant()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'response': " Aucun message reçu."}), 400

    # Utilisation de l'assistant pour obtenir une réponse
    bot_response = assistant.ask(user_message)
    if bot_response:
        return jsonify({'response': bot_response})
    else:
        return jsonify({'response': " Une erreur est survenue lors du traitement de votre message."}), 500
    


@app.route('/historique', methods=['GET'])
def historique():
    # Récupérer l'historique depuis l'instance de MistralAssistant
    historique_conversations = assistant.conversation_history
    
    # Retourner l'historique au format JSON
    return jsonify({'historique': historique_conversations})

if __name__ == '__main__':
    app.run(debug=True)