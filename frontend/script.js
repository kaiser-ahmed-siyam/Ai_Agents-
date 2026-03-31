async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user">${message}</div>`;

    const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const data = await res.json();

    chatBox.innerHTML += `<div class="bot">${data.response}</div>`;

    input.value = "";
}