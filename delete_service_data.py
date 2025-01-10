import re

def clean_service_data(subtitles):
    """Clean unnecessary service data from subtitle text."""
    cleaned_subtitles = []
    for subtitle in subtitles:
        text = subtitle.get("text", "")
        # Perform cleaning on the text
        text = re.sub(r"<c[^>]*>", "", text)  # Remove tags like <c>
        text = re.sub(r"<\d+:\d+:\d+\.\d+>", "", text)  # Remove timestamp tags
        text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces
        # Add cleaned text back to the subtitle entry
        cleaned_subtitles.append({
            "start": subtitle.get("start", ""),
            "end": subtitle.get("end", ""),
            "text": text
        })
    return cleaned_subtitles
