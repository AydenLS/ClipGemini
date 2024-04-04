from flask import jsonify
from intent_handlers import handle_request_video_intent, handle_another_intent

def handle_webhook(request):
    intent_name = request.json['queryResult']['intent']['displayName']

    try:
        if intent_name == 'RequestVideoIntent':
            return handle_request_video_intent(request.json['queryResult'])
        elif intent_name == 'AnotherIntentName':
            return handle_another_intent(request.json['queryResult'])
        else:
            return jsonify({
                'fulfillmentText': "I'm not sure how to respond to that. Would you like to open a ticket?"
            })
    except Exception as e:
        # Log the error and return an appropriate error response
        print(f"Error: {str(e)}")
        return jsonify({
            'fulfillmentText': "An error occurred while processing your request. Please try again later."
        }), 500