const API_BASE = "https://askverse-the-chatbot-9wcc.onrender.com";

async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const data = await res.json();
  if (res.ok) {
    localStorage.setItem("token", data.access_token);
    window.location.href = "chat.html";
  } else {
    alert(data.detail || "Login failed");
  }
}

async function register() {
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const role = document.getElementById("role").value;
  const field_of_interest = document.getElementById("field").value;

  const res = await fetch(`${API_BASE}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, email, password, role, field_of_interest })
  });

  const data = await res.json();
  if (res.ok) {
    alert("Registration successful. Please log in.");
    window.location.href = "login.html";
  } else {
    alert(data.detail || "Registration failed");
  }
}
