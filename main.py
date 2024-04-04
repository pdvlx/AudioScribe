import streamlit as st
from pytube import YouTube
import os
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

def get_mp3(url):
    yt = YouTube(str(url))
    audio = yt.streams.filter(only_audio = True).first()
    destination = '.'
    out_file = audio.download(output_path=destination)
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file

def get_transcript(audio_file):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"  #If you have GPU else it will use cpu
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model_id = "openai/whisper-tiny"    # define the model
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True)
    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)
    
    # create the pipeline
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=30,
        batch_size=16,
        return_timestamps=True,
        torch_dtype=torch_dtype,
        device=device,)
    
    result = pipe(audio_file, return_timestamps=True)
    result = result["chunks"]
    return result


def format_lyrics(lyrics):
    formatted_lyrics = ""
    for line in lyrics:
        text = line["text"]
        formatted_lyrics += f"{text}\n\n"
    return formatted_lyrics.strip()

def fetch_lyrics(url):
    mp3 = get_mp3(url)
    status_placeholder = st.empty()
    status_placeholder.subheader("Please wait for few seconds. We are preparing the lyrics for you")
    lyrics = get_transcript(mp3)
    status_placeholder.empty()
    lyrics = format_lyrics(lyrics)
    return lyrics


# Get YouTube URL from user
url = input("Enter the YouTube URL: ")

# Fetch lyrics
lyrics = fetch_lyrics(url)

# Display lyrics
print(lyrics)

# Save option
save_choice = input("Do you want to save the lyrics to a .txt file? (y/n): ")

if save_choice.lower() == 'y':
    filename = input("Enter filename (lyrics.txt by default): ") or "lyrics.txt"
    with open(filename, "w") as f:
        f.write(lyrics)
    print(f"Lyrics saved to {filename}")
else:
    print("Lyrics displayed on console.")