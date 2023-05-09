import os
import sys
from pydub import AudioSegment

# Get the MP3 files folder and destination folder paths from command line arguments
mp3_folder = sys.argv[1]
dest_folder = sys.argv[2]

# Make sure the destination folder exists, otherwise create it
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Loop through all the files in the MP3 files folder
for filename in os.listdir(mp3_folder):
    # Make sure it's an MP3 file
    if filename.endswith(".mp3"):
        # Load the MP3 file
        mp3_path = os.path.join(mp3_folder, filename)
        sound = AudioSegment.from_mp3(mp3_path)

        # Save the WAV file to the destination folder
        wav_filename = os.path.splitext(filename)[0] + ".wav"
        wav_path = os.path.join(dest_folder, wav_filename)
        sound.export(wav_path, format="wav")

