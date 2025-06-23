const API_BASE = "https://askverse-the-chatbot-9wcc.onrender.com";

const token = localStorage.getItem("token");
if (!token) {
  alert("Please log in first.");
  window.location.href = "login.html";
}

const messagesDiv = document.getElementById("messages");

function appendMessage(text, isUser = false) {
  const div = document.createElement("div");
  div.className = isUser ? "msg-user" : "msg-bot";
  div.innerText = text;
  messagesDiv.appendChild(div);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

async function sendMessage() {
  const promptInput = document.getElementById("prompt");
  const prompt = promptInput.value.trim();
  if (!prompt) return;

  appendMessage(prompt, true);
  promptInput.value = "";

  appendMessage("Thinking...", false);
  try {
    const res = await fetch(`${API_BASE}/chat/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
      },
      body: JSON.stringify({ prompt })
    });

    const data = await res.json();
    // Remove "Thinking..." and append real response
    messagesDiv.lastChild.remove();
    appendMessage(data.response || "Bot error 😢");
  } catch (e) {
    messagesDiv.lastChild.remove();
    appendMessage("Failed to get response from bot ❌");
  }
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "login.html";
}
