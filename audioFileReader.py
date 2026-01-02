import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()


def transcribe_audio(path):
    # use the audio file as the audio source
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        # try converting it to text
        text = r.recognize_google(audio_listened)
    return text

class file_reader:
    def save_file(file_name, text):
        if not os.path.isdir("Audio Transcripts"):
            os.mkdir("Audio Transcripts")
        with open(os.path.join("Audio Transcripts", file_name), "w") as file:
            file.write(text)

    def convert_to_text(file):
        sound = AudioSegment.from_file(file)
        # split audio sound where silence is 500 miliseconds or more and get chunks
        chunks = split_on_silence(sound,
                                  # experiment with this value for your target audio file
                                  min_silence_len=500,
                                  # adjust this per requirement
                                  silence_thresh=sound.dBFS - 14,
                                  # keep the silence for 1 second, adjustable as well
                                  keep_silence=500,
                                  )

        folder_name = "audio-chunks"
        # create a directory to store the audio chunks
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""
        # process each chunk
        for i, audio_chunk in enumerate(chunks, start=1):
            # export audio chunk and save it in
            # the `folder_name` directory.
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            # recognize the chunk
            try:
                text = transcribe_audio(chunk_filename)
            except sr.UnknownValueError as e:
                print(e)
            else:
                text = text.capitalize() + ". "
                print(chunk_filename, ":", text)
                whole_text += text
        return whole_text
        # return the text for all chunks detected
        # save_file(name, whole_text)

