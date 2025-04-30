from flask import Flask, request, jsonify
from core.intent_handler import IntentHandler  # Changed from relative to absolute import

app = Flask(__name__)
intent_handler = IntentHandler()

@app.route("/process_intent", methods=["POST"])
def process_intent():
    """Process an intent with parameters."""
    data = request.json
    
    # Check if required fields are present
    if not data or "intent" not in data:
        return jsonify({
            "status": "error",
            "message": "Missing required field: intent"
        }), 400
    
    intent = data.get("intent")
    params = data.get("params", {})
    
    # Process the intent
    result = intent_handler.process_intent(intent, params)
    
    return jsonify(result)

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def index():
    """Welcome page."""
    return jsonify({
        "message": "Welcome to NEXI API",
        "endpoints": {
            "/process_intent": "POST - Process an intent",
            "/health": "GET - Health check"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)