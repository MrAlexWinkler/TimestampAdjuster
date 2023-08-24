# TimestampAdjuster

TimestampAdjuster is a tool specifically designed to adjust auto generated zoom timestamped transcript to your final video edits. It's perfect for video content creators, educators, and anyone in need of accurate video transcriptions.

## Features:

- Adjust timestamps based on a specific entry number.
- Generate an HTML version of the transcript with links.
- (Work in progress) Replace speaker names with predefined links.

## How to Use

### Prerequisites:

1. Ensure you have Python installed.
2. Clone the repository or download the source files to your local machine.

### Steps:

1. **Navigate to the directory where the `TimestampAdjuster` files are located.**

   ```bash
   cd path/to/TimestampAdjuster
2. **Run the adjust_vtt.py script.**
   ```bash  
    python adjust_vtt.py
3. **You will be prompted with the following questions:**

    - **Enter the path to the input VTT file (with quotes):** This is where you input the path to the VTT file you wish to adjust. Ensure the path is enclosed in double quotes.
    - **Enter the entry number to start from:** This is the number from where you want the timestamps to start adjusting. It should match one of the numbers in the VTT file.

    Example Flow:
   ```bash  
    D:\TimestampAdjuster>python adjust_vtt.py
    Enter the path to the input VTT file (with quotes): "c:\path\to\your\file.vtt"
    Enter the entry number to start from: 47
    ```
    

    - After providing the required inputs, the script will adjust the timestamps of the VTT file. It will save the adjusted file in the same directory as the input file but with:
    `-ADJUSTED_{start_entry_number}.vtt` appended to its name. 
    - There will also be an HTML-adjusted version saved with `-ADJUSTED_{start_entry_number}-HTML.vtt` appended.


4. **Check the directory for the adjusted files.**

    You should see the original VTT file along with the adjusted ones.


## Known Issues:

- The `adjust_vtt_timestamps_html` function is not adding the links for the names yet. This is currently being worked on.

## Contribution:

Feel free to fork this repository, make changes, and open a pull request if you think you've made improvements that should be included here.

## Keywords:

Zoom, Transcription, Timestamp Adjustment, Video Content, Open Source

