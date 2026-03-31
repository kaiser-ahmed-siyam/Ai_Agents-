

//     const res = await fetch("http://127.0.0.1:8000/chat", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ message })
//     });

//     const data = await res.json();

//     chatBox.innerHTML += `<div class="bot">${data.response}</div>`;

//     input.value = "";
// }


async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;

    const chatBox = document.getElementById("chat-box");

    // User message
    chatBox.innerHTML += `<div class="message user">${message}</div>`;

    // Bot message placeholder
    const botDiv = document.createElement("div");
    botDiv.className = "message bot";
    botDiv.textContent = "";
    chatBox.appendChild(botDiv);
    botDiv.style.whiteSpace = "pre-wrap";


    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        botDiv.textContent += chunk;
        

        // auto scroll
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}