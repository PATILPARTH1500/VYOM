const input = document.getElementById("cmdInput");

const chatBox = document.getElementById("chatBox");

// ------------------------------------
// FILL COMMAND
// ------------------------------------

function fillCmd(cmd) {

    input.value = cmd;

    input.focus();

}

// ------------------------------------
// ADD MESSAGE
// ------------------------------------

function addMessage(tag, content, isAI = false) {

    const row = document.createElement("div");

    row.className = "msg-row";

    row.innerHTML = `

        <div class="msg-tag ${isAI ? "ai-tag" : "user-tag"}">
            ${tag}
        </div>

        <div class="msg-content ${isAI ? "ai-content" : ""}">
            ${content}
        </div>

    `;

    chatBox.appendChild(row);

    chatBox.scrollTop = chatBox.scrollHeight;

}

// ------------------------------------
// SEND MESSAGE
// ------------------------------------

async function handleSend() {

    const message = input.value.trim();

    if (!message) return;

    // USER MESSAGE

    addMessage("YOU", message);

    input.value = "";

    // THINKING MESSAGE

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

        const thinkingElement =
            document.getElementById(thinkingId);

        if (thinkingElement) {

            thinkingElement.remove();

        }

        // AI RESPONSE

        addMessage("VYOM", data.response, true);

    }

    catch (error) {

        const thinkingElement =
            document.getElementById(thinkingId);

        if (thinkingElement) {

            thinkingElement.remove();

        }

        addMessage(

            "ERROR",

            "Flask backend not responding."

        );

        console.error(error);

    }

    input.focus();

}

// ------------------------------------
// ENTER KEY
// ------------------------------------

input.addEventListener("keydown", function (e) {

    if (e.key === "Enter") {

        handleSend();

    }

});

// ------------------------------------
// TIME
// ------------------------------------

function updateTime() {

    const now = new Date();

    const h = String(now.getHours()).padStart(2, "0");

    const m = String(now.getMinutes()).padStart(2, "0");

    document.getElementById("time-stat").innerText =
        `${h}:${m}`;

}

// ------------------------------------
// SYSTEM STATS
// ------------------------------------

async function updateSystemStats() {

    try {

        const response = await fetch("/system");

        const data = await response.json();

        document.getElementById("cpu-stat").innerText =
            `CPU ${data.cpu}%`;

    }

    catch (error) {

        console.log(error);

    }

}

// ------------------------------------
// INITIALIZE
// ------------------------------------

updateTime();

updateSystemStats();

setInterval(updateTime, 1000);

setInterval(updateSystemStats, 3000);

input.focus();

chatBox.scrollTop = chatBox.scrollHeight;