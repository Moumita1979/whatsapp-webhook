from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = 'myverifytoken123'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Meta verification
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        mode = request.args.get('hub.mode')

        if token == VERIFY_TOKEN and mode == 'subscribe':
            return challenge, 200
        else:
            return 'Verification token mismatch', 403

    elif request.method == 'POST':
        # Handle incoming messages here
        data = request.get_json()
        print("Webhook received:", data)
        return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    app.run(port=5000)
