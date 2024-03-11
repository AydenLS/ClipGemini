from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])  # Changed from '/' to '/webhook'
def webhook():
    # Extract intent from Dialogflow request
    req = request.get_json(silent=True, force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')

    # Check name of intent
    if intent_name == "RequestVideoIntent":  # replace with ntent name for video requests
        # Extract video topic parameter (havent written param yet) from the request
        video_topic = req.get('queryResult').get('parameters').get('video_topic')
        # Replace the following line with logic to fetch the appropriate video URL
        video_url = f"http://linktoyourvideo.com/{video_topic}"  # placeholder for video URL
        summary = f"This is your video about {video_topic}."  # placeholder for summary

        # Construct response payload
        response = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [summary]
                    }
                },
                {
                    "text": {
                        "text": [f"Watch the video here: {video_url}"]
                    }
                }
            ]
        }
        return jsonify(response)

    # Default response for unhandled intents and for error handling intents
    return jsonify({"fulfillmentText": "I'm not sure how to respond to that. Would you like to open a ticket?"})

if __name__ == '__main__':
    app.run(port=5000)  
