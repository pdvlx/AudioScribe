# AudioScribe

AudioScribe is a Python script that leverages Whisper for speech recognition and extracts lyrics or dialogue from YouTube videos.

## How it works

1. Enter the YouTube URL of the video you want to transcribe.
2. AudioScribe downloads the audio portion of the video and uses Whisper to convert it to text.
3. The transcribed text (lyrics or dialogue) is displayed on the console.
4. You can choose to save the transcript to a .txt file for future reference.

## Dependencies

* streamlit
* pytube
* torch
* transformers

## Instructions

1. Install the required dependencies using `pip install streamlit pytube torch transformers`. (you can pip3 install -r requirements.txt too )
2. Run the script using `python3 main.py`.
3. Follow the prompts to enter the YouTube URL and choose the saving option.

1. **Set up a virtual environment (optional but recommended):**
    - It's recommended to use a virtual environment to isolate project dependencies and avoid conflicts with system-wide Python installations.
    - Create a virtual environment named `.venv` using `python -m venv .venv` (or `python3 -m venv .venv` on some systems).
    - Activate the virtual environment:
        - **Windows:** Open a command prompt, navigate to the `.venv\Scripts` directory, and run `activate.bat`.
        - **macOS/Linux:** Open a terminal, navigate to the `.venv` directory, and run `source bin/activate`.
2. Install the required dependencies:
    - Inside the activated virtual environment (if you created one), run `pip install streamlit pytube torch transformers`.
3. Run the script:
    - Still within the activated virtual environment (if applicable), run `python audio_scribe.py`.
4. Follow the prompts to enter the YouTube URL and choose the saving option.

## Note

This is a basic console application. For a more user-friendly experience, you can explore integrating this script with a web framework like Streamlit to create a web app.
