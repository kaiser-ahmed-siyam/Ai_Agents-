
let session_id = localStorage.getItem("session_id");

if (!session_id) {
    session_id = Math.random().toString(36).substring(7);
    localStorage.setItem("session_id", session_id);
}


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
        body: JSON.stringify({ message : message,
                               session_id: session_id })
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        botDiv.textContent += chunk;
        // if (isFirstChunk) {
        //      botDiv.textContent = `<i>${chunk}</i>`;
        //      isFirstChunk = false;
        // } else {
        // botDiv.textContent+= chunk;
        // // botDiv.innerHTML += chunk;
        // }

        

        // auto scroll
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}