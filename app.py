from flask import Flask, request, jsonify
from delete_service_data import clean_service_data
from delete_duplicate_string import delete_duplicate_lines

app = Flask(__name__)

@app.route("/clean_subtitles", methods=["POST"])
def clean_subtitles():
    """API endpoint to clean subtitles."""
    try:
        data = request.get_json()
        if not data or "subtitles" not in data:
            return jsonify({"error": "Invalid input. Provide 'subtitles' array."}), 400
        
        subtitles = data["subtitles"]
        cleaned_data = clean_service_data(subtitles)
        deduplicated_data = delete_duplicate_lines(cleaned_data)
        
        return jsonify({"cleaned_subtitles": deduplicated_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Subtitle Cleaning Service is running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
