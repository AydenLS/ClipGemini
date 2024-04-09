<!--- index.cfm --->
<html>
<head>
    <title>ClipBot - Chatbot UI</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="scripts.js"></script>
</head>
<body>
    <div id="chatbot-container">
        <div id="chatbot-header">
            <h1>ClipBot - Chatbot UI</h1>
        </div>
        <div id="chatbot-messages">
            <div id="bot-response"></div>
            <!--- Chat messages displayed here --->
        </div>
        <div id="chatbot-input">
            <input type="text" id="user-input" placeholder="Type your message...">
            <button id="send-button">Send</button>
        </div>
    </div>
</body>
</html>