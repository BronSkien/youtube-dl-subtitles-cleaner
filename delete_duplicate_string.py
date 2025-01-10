import re

def is_empty_line(line):
    """Check if a line is empty."""
    return bool(re.match(r"\s*\n", line))

def is_time_code(line):
    """Check if a line contains a timecode."""
    time = r"\d{2}:\d{2}:\d{2}\.\d{3}"
    return bool(re.match(time + r"\s*-->\s*" + time + r"\s*\n", line))

def is_suitable_line(line):
    """Check if a line is a valid subtitle text."""
    return not is_empty_line(line) and not is_time_code(line)

def get_chunk(text):
    """Generate chunks of lines for processing."""
    for index in reversed(range(1, len(text) - 1)):
        yield index, text[index-1:index+2]

def is_empty_timecode(chunk):
    """Check if a chunk consists of an empty timecode."""
    return is_empty_line(chunk[0]) and is_time_code(chunk[1]) and is_empty_line(chunk[2])

def del_chunk_with_index(index, text):
    """Delete a chunk of lines by index."""
    text.pop(index + 1)
    text.pop(index)
    text.pop(index - 1)

def delete_duplicate_lines(input_text):
    """Remove duplicate lines and unnecessary timecodes."""
    found_lines = set()
    output_text = list(input_text)

    for index, line in reversed(list(enumerate(input_text))):
        if is_suitable_line(line):
            if line not in found_lines:
                found_lines.add(line)
            else:
                output_text.pop(index)

    for index, chunk in get_chunk(output_text):
        if is_empty_timecode(chunk):
            del_chunk_with_index(index, output_text)

    return output_text
