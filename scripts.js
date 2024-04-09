// scripts.js
$(document).ready(function() {
    $('#send-button').click(function() {
        sendMessage();
    });

    $('#user-input').keypress(function(event) {
        if (event.which === 13) {
            sendMessage();
        }
    });

    function sendMessage() {
        var userInput = $('#user-input').val();
        if (userInput.trim() !== '') {
            appendMessage('user', userInput);
            $('#user-input').val('');

            // Send user message to Flask backend
            $.ajax({
                url: 'http://localhost:5000/message',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ message: userInput }),
                success: function(response) {
                    var botResponse = response.messages[0];
                    appendMessage('bot', botResponse);
                },
                error: function() {
                    appendMessage('bot', 'Oops! Something went wrong. Please try again.');
                }
            });
        }
    }

    function appendMessage(sender, message) {
        if (sender === 'bot') {
            $('#bot-response').text(message);
        } else {
            var messageElement = $('<div>').addClass('message').addClass(sender);
            messageElement.text(message);
            $('#chatbot-messages').append(messageElement);
            $('#chatbot-messages').scrollTop($('#chatbot-messages')[0].scrollHeight);
        }
    }
});