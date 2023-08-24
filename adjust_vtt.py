from vtt_processor import adjust_vtt_timestamps, adjust_vtt_timestamps_html
from parse_name_mappings import parse_name_mappings

input_file = input('Enter the path to the input VTT file (with quotes): ').strip('"')
start_entry_number = int(input('Enter the entry number to start from: '))

# Always use names.py for name-URL mapping
name_url_mapping = parse_name_mappings("names.py")

# Adjust timestamps for the standard version and retrieve the offset
offset = adjust_vtt_timestamps(input_file, start_entry_number)

# Adjust timestamps for the HTML version using the offset
adjust_vtt_timestamps_html(input_file, start_entry_number, name_url_mapping)

print("Timestamps adjusted successfully!")
