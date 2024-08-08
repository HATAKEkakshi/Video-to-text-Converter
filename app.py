import moviepy.editor as mp
import whisper




def extract_audio_to_file(video_path, audio_path):
  """
  Uses the moviepy package to extract and write
  audio content to a ne file
  """
  # Load the video from file
  video = mp.VideoFileClip(video_path)
  # Extract the audio file from the video.
  # The codec is chosen to be a compatible format for Whisper
  video.audio.write_audiofile(audio_path, codec='pcm_s16le')

def video_to_transcript_with_whisper(video_path, audio_path):
  extract_audio_to_file(video_path, audio_path)
  # First grab the relevant model for the task at hand
  model = whisper.load_model("base.en")
  # Transcribe the audio file using the selected model
  result = model.transcribe(audio_path)
  return result["text"]

if __name__ == "__main__":
  filename = "/Users/hemantkumar/Developer/Projects_ai/video-to-text-Converter/videotestsong"
  audio_path = f"/Users/hemantkumar/Developer/Projects_ai/video-to-text-Converter/videotest/test.wav"
  video_path = f"/Users/hemantkumar/Developer/Projects_ai/video-to-text-Converter/videotest/song.mp4"
  transcript = video_to_transcript_with_whisper(video_path, audio_path)
  print(transcript)