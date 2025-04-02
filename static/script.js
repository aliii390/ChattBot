const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');

function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // message de l'user
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'message test';
    userMessageDiv.textContent = message;
    chatMessages.appendChild(userMessageDiv);

   
    userInput.value = '';

    // envoyer un message au serveur
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
        const botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'message bot-message';
        botMessageDiv.textContent = data.response;
        chatMessages.appendChild(botMessageDiv);

      
        chatMessages.scrollTop = chatMessages.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });


    fetch('/historique', {
        method: 'GET',
        headers:{
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({})
    })




    
}