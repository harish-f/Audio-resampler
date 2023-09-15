import os
import librosa
import soundfile as sf

source = input("Input your source file: ").strip()
desired_sample_rate = int(input("Input your desired sample rate: "))
output_file = ""
if input("Do you have a output file[y/n]: ").lower() == "y":
  output_file = input("Output file name: ").strip()
else:
  print("An output file will be automatically generated")
  output_file = input("Output file name: ").strip()
  os.system("touch " + output_file)

y, sr = librosa.load(source, sr=desired_sample_rate)
sf.write(output_file, y, sr)

print("All done! Your resampled audio is called " + output_file)