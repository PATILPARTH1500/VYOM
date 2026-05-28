const input = document.getElementById("cmdInput");

const chatBox = document.getElementById("chatBox");

function fillCmd(cmd) {

    input.value = cmd;

    input.focus();

}

async function handleSend() {

    const message = input.value.trim();

    if (!message) return;

    // USER MESSAGE

    const userRow = document.createElement("div");

    userRow.className = "msg-row";

    userRow.innerHTML = `

        <div class="msg-tag user-tag">
            YOU
        </div>

        <div class="msg-content">
            ${message}
        </div>

    `;

    chatBox.appendChild(userRow);

    input.value = "";

    // THINKING

    const thinkingId = "thinking-" + Date.now();

    const thinkRow = document.createElement("div");

    thinkRow.className = "msg-row thinking-row";

    thinkRow.id = thinkingId;

    thinkRow.innerHTML = `

        <div class="msg-tag ai-tag">
            VYOM
        </div>

        <div class="msg-content">
            thinking...
        </div>

    `;

    chatBox.appendChild(thinkRow);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

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

        document.getElementById(thinkingId).remove();

        const aiRow = document.createElement("div");

        aiRow.className = "msg-row";

        aiRow.innerHTML = `

            <div class="msg-tag ai-tag">
                VYOM
            </div>

            <div class="msg-content ai-content">
                ${data.response}
            </div>

        `;

        chatBox.appendChild(aiRow);

    }

    catch (error) {

        document.getElementById(thinkingId).remove();

        const errRow = document.createElement("div");

        errRow.className = "msg-row";

        errRow.innerHTML = `

            <div class="msg-tag ai-tag">
                ERROR
            </div>

            <div class="msg-content">
                Flask backend not responding.
            </div>

        `;

        chatBox.appendChild(errRow);

        console.error(error);

    }

    chatBox.scrollTop = chatBox.scrollHeight;

    input.focus();

}

input.addEventListener("keydown", function (e) {

    if (e.key === "Enter") {

        handleSend();

    }

});

function updateTime() {

    const now = new Date();

    const h = String(now.getHours()).padStart(2, "0");

    const m = String(now.getMinutes()).padStart(2, "0");

    document.getElementById("time-stat").innerText = `${h}:${m}`;

}

function updateCPU() {

    const cpu = Math.floor(Math.random() * 30) + 5;

    document.getElementById("cpu-stat").innerText = `CPU ${cpu}%`;

}

updateTime();

updateCPU();

setInterval(updateTime, 1000);

setInterval(updateCPU, 4000);

input.focus();