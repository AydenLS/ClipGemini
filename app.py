from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import dialogflow_v2beta1 as dialogflow
import uuid
import logging
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the Dialogflow CX client
session_client = dialogflow.SessionsClient()

@app.route('/message', methods=['POST'])
def handle_message():
    data = request.get_json()
    user_message = data['message']
    logger.info(f"Received message: {user_message}")

    # Set up the Dialogflow CX session
    project_id = 'clipbot-408116'
    session_id = str(uuid.uuid4())  # Generate a random session ID
    session = session_client.session_path(project_id, session_id)

    try:
        # Create the Dialogflow CX query input
        text_input = dialogflow.types.TextInput(text=user_message, language_code='en')
        query_input = dialogflow.types.QueryInput(text=text_input)

        # Send the query to Dialogflow CX and get the response
        response = session_client.detect_intent(session=session, query_input=query_input)

        # Extract the response messages from Dialogflow CX
        response_messages = [message.text.text[0] for message in response.query_result.response_messages]

        # Log the response
        logger.info(f"Response: {response_messages}")
        # Return response messages as JSON
        return jsonify({'messages': response_messages})

    except Exception as e:
        # Log the error
        logger.error(f"Error: {str(e)}")
        logger.error(traceback.format_exc())

        # Return an error response with default message
        error_message = f"An error occurred while processing your request: {str(e)}"
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)