from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    intent_name = request.json['queryResult']['intent']['displayName']
    response = None

    # Handle different Intents 
    if intent_name == 'RequestVideoIntent':
        # Logic for handling the RequestVideoIntent
        pass  # Placeholder statement
    # Add more elif blocks for other intents as needed
    else:
        # Default response if the intent is not recognized
        response = {
            "fulfillmentText": "I'm not sure how to respond to that. Would you like to open a ticket?"
        }

        # Send the response back to Dialogflow
        return jsonify(response)

    if __name__ == '__main__':
        app.run(debug=True)  # Start the Flask app
