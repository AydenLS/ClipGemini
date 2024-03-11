const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json()); // for parsing application/json

app.post('/webhook', (req, res) => {
    const intentName = req.body.queryResult.intent.displayName;
    let response;

    // Handle different Intents with custom logic
    if (intentName === 'RequestVideoIntent') {
        // Logic for handling the RequestVideoIntent
        response = { /* ... */ };
    } else if (intentName === 'AnotherIntentName') {
        // Logic for handling a different intent
        response = { /* ... */ };
    } else {
        // Default response if the intent is not handled
        response = {
            "fulfillmentText": "I'm not sure how to respond to that. Would you like to open a ticket?"
        };
    }

    // Send the response back to Dialogflow
    res.json(response);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
