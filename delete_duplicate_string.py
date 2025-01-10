import re

def is_empty_line(text: str) -> bool:
    """Check if a text line is empty."""
    return bool(re.match(r"^\s*$", text))

def is_time_code(text: str) -> bool:
    """Check if a text line contains a timecode."""
    time = r"\d{2}:\d{2}:\d{2}\.\d{3}"
    return bool(re.match(time + r"\s*-->\s*" + time, text))

def is_suitable_line(text: str) -> bool:
    """Check if a line is a suitable subtitle text."""
    return not is_empty_line(text) and not is_time_code(text)

def delete_duplicate_lines(subtitles: list) -> list:
    """Remove duplicate subtitle entries based on their 'text' field.

    Args:
        subtitles (list): List of subtitle dictionaries with 'start', 'end', and 'text'.

    Returns:
        list: Deduplicated list of subtitle dictionaries.
    """
    found_texts = set()
    deduplicated_subtitles = []

    for subtitle in subtitles:
        if not isinstance(subtitle, dict) or "text" not in subtitle:
            # Skip invalid subtitle entries
            continue

        text = subtitle["text"]

        if is_suitable_line(text):
            if text not in found_texts:
                found_texts.add(text)
                deduplicated_subtitles.append(subtitle)

    return deduplicated_subtitles
