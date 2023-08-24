import re
from time_utils import vtt_time_to_seconds, seconds_to_vtt_time
from names import name_url_mapping as default_name_mapping

def adjust_vtt_timestamps(input_file, start_entry_number):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
        
    start_time = None
    start_index = None
    for idx, line in enumerate(lines):
        if line.strip() == str(start_entry_number):
            start_time = re.search(r"(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})", lines[idx + 1]).group(1)
            start_index = idx
            break
            
    if not start_time:
        raise ValueError("Start entry number not found in VTT file.")
    
    offset = -vtt_time_to_seconds(start_time)
    
    adjusted_lines = ["\n"]
    in_entry = False
    for line in lines[start_index + 1:]:
        if re.match(r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}", line):
            start, end = line.strip().split(" --> ")
            adjusted_start = seconds_to_vtt_time(vtt_time_to_seconds(start) + offset)
            adjusted_end = seconds_to_vtt_time(vtt_time_to_seconds(end) + offset)
            adjusted_lines.append(f"{adjusted_start} --> {adjusted_end}\n")
        elif line.strip().isdigit():
            continue
        else:
            adjusted_lines.append(line)
            
    output_file = input_file.replace('.vtt', f'-ADJUSTED_{start_entry_number}.vtt')
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(adjusted_lines)
        
    print(f"File adjusted and saved as: {output_file}")


def adjust_vtt_timestamps_html(input_file, start_entry_number, name_url_mapping=default_name_mapping):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    start_time = None
    start_index = None
    for idx, line in enumerate(lines):
        if line.strip() == str(start_entry_number):
            start_time = re.search(r"(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})", lines[idx + 1]).group(1)
            start_index = idx
            break
            
    if not start_time:
        raise ValueError("Start entry number not found in VTT file.")
    
    offset = -vtt_time_to_seconds(start_time)

    adjusted_lines = ["\n"]
    for line in lines[start_index + 1:]:
        if re.match(r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}", line):
            start, end = line.strip().split(" --> ")
            adjusted_start = seconds_to_vtt_time(vtt_time_to_seconds(start) + offset)
            adjusted_end = seconds_to_vtt_time(vtt_time_to_seconds(end) + offset)
            adjusted_lines.append(f"<p>{adjusted_start} --&gt; {adjusted_end}<br />\n")
        elif line.strip().isdigit():
            continue
        else:
            for name, url in name_url_mapping.items():
                line = line.replace(name + ":", f'<a href="{url}" target="_blank">{name}</a>:')
            adjusted_lines.append(line + "</p>\n")

    output_file = input_file.replace('.vtt', f'-ADJUSTED_{start_entry_number}-HTML.vtt')
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(adjusted_lines)

    print(f"HTML adjusted file saved as: {output_file}")
