import re

def clean_service_data(lines):
    """Remove service data from the subtitle file lines."""
    cleaned_lines = []
    for line in lines:
        # Remove `<c>` tags and alignment data
        line = re.sub(r"<c[^>]*>", "", line)
        line = re.sub(r"</c>", "", line)
        line = re.sub(r"align:[^ ]+ position:[^ ]+", "", line)
        cleaned_lines.append(line.strip() + "\n")
    return cleaned_lines
