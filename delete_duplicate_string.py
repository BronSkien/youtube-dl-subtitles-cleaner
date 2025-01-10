import re

def is_empty_line(line: str) -> bool:
    """Check if a line is empty."""
    return bool(re.match(r"\s*$", line))

def is_time_code(line: str) -> bool:
    """Check if a line has a timecode."""
    time = r"\d{2}:\d{2}:\d{2}\.\d{3}"
    return bool(re.match(time + r"\s*-->\s*" + time, line))

def is_suitable_line(line: str) -> bool:
    """Check if a line is a suitable subtitle line."""
    return not is_empty_line(line) and not is_time_code(line)

def delete_duplicate_lines(subtitles: list) -> list:
    """Remove duplicate subtitle lines based on their text field.

    Args:
        subtitles (list): List of subtitle dictionaries with 'start', 'end', and 'text'.

    Returns:
        list: Deduplicated list of subtitle dictionaries.
    """
    found_texts = set()
    deduplicated_subtitles = []

    for subtitle in subtitles:
        text = subtitle.get("text", "")
        if is_suitable_line(text):
            if text not in found_texts:
                found_texts.add(text)
                deduplicated_subtitles.append(subtitle)

    return deduplicated_subtitles
