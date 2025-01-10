import work_with_files as files
from delete_service_data import clean_service_data
from delete_duplicate_string import delete_duplicate_lines

def main():
    input_file_name = files.get_input_file_name()
    output_file_name = files.get_output_file_name()
    
    # Read the input file
    lines = files.read_file(input_file_name)
    
    # Clean service data
    cleaned_lines = clean_service_data(lines)
    
    # Remove duplicate lines
    final_lines = delete_duplicate_lines(cleaned_lines)
    
    # Write to the output file
    files.write_to_file(final_lines, output_file_name)

if __name__ == "__main__":
    main()
