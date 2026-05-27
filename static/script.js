async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value;

    if (!message) return;

    chatBox.innerHTML += `
        <div class="message user">
            <strong>You:</strong> ${message}
        </div>
    `;

    input.value = "";

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    chatBox.innerHTML += `
        <div class="message ai">
            <strong>VYOM:</strong> ${data.response}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}