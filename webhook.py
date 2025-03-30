from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "your_verify_token"  # You can choose any secure string

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Verification
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("WEBHOOK VERIFIED")
            return challenge, 200
        else:
            return "Verification token mismatch", 403

    elif request.method == "POST":
        # Message received from WhatsApp
        data = request.json
        print("Received message:", data)
        return "EVENT_RECEIVED", 200

    return "Hello from webhook", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
