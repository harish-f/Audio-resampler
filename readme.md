# Python Audio Resampler

## Description
A simple and easy-to-use audio resampler. I have created this as I realised audio resampling with other apps like Audacity wasn't very straightforward. This may be especially helpful for those who resample wav files recorded from satellites to make them usable to be processed by apps like WXtoIMG to generate an image.

**Note:** This was tested and run on python 3.9.13 and hasn't been tested on other versions but should most likely work anyways


## Usage

You'll need the python Librosa audio library to help to process the audio files.
```bash
pip3 install librosa
```

To run the file
```bash
python3 resample.py
```

The program will then ask for your input file and output sample rate. Additionally, it will also ask you if you already have an output file, if you don't it will automatically generate one for you.