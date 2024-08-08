import streamlit as st
import whisper
import moviepy.editor as mp

st.title("Video-To-Text-Converter")
audio="/Users/hemantkumar/Developer/Projects_ai/video-to-text-Converter/videotest/test2.wav"
file="/Users/hemantkumar/Developer/Projects_ai/video-to-text-Converter/videotest/yc.mp4"


def extract_audio_to_file(file, audio):
  """
  Uses the moviepy package to extract and write
  audio content to a ne file
  """
  # Load the video from file
  video = mp.VideoFileClip(file)
  # Extract the audio file from the video.
  # The codec is chosen to be a compatible format for Whisper
  video.audio.write_audiofile(audio, codec='pcm_s16le')
def video_to_transcript_with_whisper(file, audio):
  extract_audio_to_file(file, audio)
  # First grab the relevant model for the task at hand
  model = whisper.load_model("base.en")
  st.text("Whisper Model Loaded")
  # Transcribe the audio file using the selected model
  result = model.transcribe(audio)
  return result["text"]
if st.sidebar.button("Transcribe Video"):
    if file is not None:
        st.sidebar.success("Transcribing Video")
        transcription=video_to_transcript_with_whisper(file,audio)
        st.sidebar.success("Transcription Compeleted")
        st.write(transcription)
    else:
        st.sidebar.error("Please Upload am video file")

st.sidebar.header("Play Original Video file")
st.sidebar.video(file)

    
