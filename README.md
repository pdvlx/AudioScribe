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

**1. Install Dependencies Directly (Optional):**

* Use `pip install streamlit pytube torch transformers` to install the required dependencies directly into your system-wide Python environment.

**OR**

**2. Use a Virtual Environment (Recommended):**

This method isolates project dependencies and avoids conflicts. Follow these steps:

   - Create a virtual environment named `.venv` using `python -m venv .venv` (or `python3 -m venv .venv` on some systems).
   - Activate the virtual environment:
      - **Windows:** Open a command prompt, navigate to the `.venv\Scripts` directory, and run `activate.bat`.
      - **macOS/Linux:** Open a terminal, navigate to the `.venv` directory, and run `source bin/activate`.
   - Once activated, install dependencies using `pip install streamlit pytube torch transformers`.

**3. Run the Script:**

After installation (either directly or in the virtual environment), run the script using `python main.py`. The program will prompt you to enter the YouTube URL and choose a saving option.

**4. Follow the prompts to enter the YouTube URL and choose the saving option.**

## Note

This is a basic console application. For a more user-friendly experience, you can explore integrating this script with a web framework like Streamlit to create a web app.
