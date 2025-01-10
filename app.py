from flask import Flask, request, jsonify
from delete_service_data import clean_service_data
from delete_duplicate_string import delete_duplicate_lines

app = Flask(__name__)

@app.route("/clean_subtitles", methods=["POST"])
def clean_subtitles():
    """API endpoint to clean subtitles."""
    try:
        data = request.get_json()

        # Validate input
        if not data or "subtitles" not in data:
            return jsonify({"error": "Invalid input. Provide 'subtitles' array."}), 400

        subtitles = data["subtitles"]

        # Preprocess subtitles
        processed_subtitles = preprocess_subtitles(subtitles)

        # Clean and deduplicate
        cleaned_data = clean_service_data(processed_subtitles)
        deduplicated_data = delete_duplicate_lines(cleaned_data)

        return jsonify({"cleaned_subtitles": deduplicated_data}), 200

    except Exception as e:
        import traceback
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500


def preprocess_subtitles(subtitles):
    """Preprocess subtitles to ensure a consistent format."""
    processed = []

    for entry in subtitles:
        # Ensure each entry is a dictionary
        if not isinstance(entry, dict):
            continue

        # Validate and extract keys
        start = entry.get("start", "").strip()
        end = entry.get("end", "").strip()
        text = entry.get("text", "").strip()

        # Skip entries with no text
        if not text:
            continue

        # Add processed entry
        processed.append({"start": start, "end": end, "text": text})

    return processed


@app.route("/", methods=["GET"])
def home():
    """Simple home route for testing."""
    return "Subtitle Cleaning Service is running!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
