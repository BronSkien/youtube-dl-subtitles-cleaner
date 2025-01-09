from flask import Flask, request, jsonify
from cleaner.delete_duplicate_string import delete_duplicate_lines
from cleaner.delete_service_data import clean_service_data

app = Flask(__name__)

@app.route('/clean_subtitles', methods=['POST'])
def clean_subtitles():
    try:
        data = request.json
        if not data or 'subtitles' not in data:
            return jsonify({"error": "Invalid input: 'subtitles' array is required"}), 400
        
        subtitles = data['subtitles']
        cleaned_subtitles = []

        for subtitle in subtitles:
            text = subtitle.get('text', '')
            text = delete_duplicate_lines(text)  # Remove duplicate lines
            text = clean_service_data(text)     # Remove metadata/service data
            subtitle['text'] = text
            cleaned_subtitles.append(subtitle)

        return jsonify({"cleaned_subtitles": cleaned_subtitles}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
