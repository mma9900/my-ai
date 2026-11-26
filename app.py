from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MY AI</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 0;
            background: #101010;
            color: white;
            font-family: Arial, sans-serif;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }

        header {
            background: #191919;
            padding: 18px;
            display: flex;
            align-items: center;
            gap: 12px;
            border-bottom: 2px solid #701d2b;
        }

        .logo {
            background: #701d2b;
            width: 42px;
            height: 42px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
        }

        .brand h2 {
            margin: 0;
            font-size: 19px;
        }

        .brand p {
            margin: 4px 0 0;
            color: #999;
            font-size: 12px;
        }

        #chat {
            flex: 1;
            overflow-y: auto;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .message {
            padding: 13px 15px;
            border-radius: 14px;
            max-width: 85%;
            line-height: 1.7;
            overflow-wrap: anywhere;
        }

        .bot {
            background: #252525;
            align-self: flex-start;
            border-right: 3px solid #701d2b;
        }

        .user {
            background: #701d2b;
            align-self: flex-end;
        }

        .welcome {
            text-align: center;
            margin: auto;
            color: #aaa;
        }

        .welcome h1 {
            color: white;
            font-size: 28px;
        }

        .welcome span {
            color: #a12c40;
        }

        footer {
            padding: 14px;
            background: #191919;
            border-top: 1px solid #333;
        }

        .input-area {
            display: flex;
            gap: 9px;
        }

        input {
            flex: 1;
            min-width: 0;
            background: #292929;
            border: 1px solid #444;
            border-radius: 12px;
            padding: 14px;
            color: white;
            outline: none;
            font-size: 15px;
        }

        input:focus {
            border-color: #a12c40;
        }

        button {
            background: #701d2b;
            border: none;
            border-radius: 12px;
            color: white;
            padding: 0 18px;
            font-size: 18px;
            cursor: pointer;
        }

        button:active {
            background: #a12c40;
        }

        .status {
            color: #888;
            text-align: center;
            font-size: 11px;
            margin-top: 10px;
        }
    </style>
</head>

<body>

    <header>
        <div class="logo">AI</div>
        <div class="brand">
            <h2>MY AI</h2>
            <p>Your Personal Assistant</p>
        </div>
    </header>

    <main id="chat">

        <div class="welcome" id="welcome">
            <h1>Welcome to <span>MY AI</span></h1>
            <p>أهلاً بك! ابدأ محادثتك مع مساعدك الذكي.</p>
        </div>

    </main>

    <footer>
        <div class="input-area">
            <input
                id="message"
                type="text"
                placeholder="اكتب رسالتك هنا..."
                autocomplete="off"
            >
            <button onclick="sendMessage()">➤</button>
        </div>

        <div class="status">MY AI - الإصدار الأول</div>
    </footer>

    <script>
        const chat = document.getElementById("chat");
        const input = document.getElementById("message");

        function addMessage(text, type) {
            const welcome = document.getElementById("welcome");

            if (welcome) {
                welcome.remove();
            }

            const div = document.createElement("div");
            div.className = "message " + type;
            div.textContent = text;

            chat.appendChild(div);
            chat.scrollTop = chat.scrollHeight;
        }

        async function sendMessage() {
            const message = input.value.trim();

            if (!message) return;

            addMessage(message, "user");
            input.value = "";

            addMessage("استلمت رسالتك! جاري تجهيز الذكاء الاصطناعي...", "bot");
        }

        input.addEventListener("keydown", function(event) {
            if (event.key === "Enter") {
                sendMessage();
            }
        });
    </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
