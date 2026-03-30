# Source: https://docs.salad.com/transcription/how-to-guides/technical/splitting-large-audio-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Split Large Audio Files for Salad Transcription API

*Last Updated: February 28, 2025*

## Introduction

When using Salad Transcription API, audio files have a maximum length limit of 2.5 hours each. If you have audio files
longer than this to transcribe, you will need to split these into shorter segments first.

***

## Prerequisites

Before you begin, make sure you have:

1. **Python Installed**: Ensure you have Python 3.8 or higher.
2. **Libraries Installed**: Use the following command to install the required libraries:
   ```bash  theme={null}
   pip install pydub
   ```
3. **FFmpeg Installed**: FFmpeg is needed by pydub for processing audio:
   * **Linux**: `sudo apt install ffmpeg`
   * **MacOS**: `brew install ffmpeg`
   * **Windows**: [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.

***

*Last Updated: February 28, 2025*

## Splitting the audio files

### 1. Create the script:

Create a Python script named `split_audio.py` to split the audio file:

```Python  theme={null}
from pydub import AudioSegment
import os

def split_audio(file_path, output_dir, segment_length=int(2.5*60*60*1000)): ## Adjust this value if you want even shorter segments.
  audio = AudioSegment.from_file(file_path)
  total_length = len(audio)
  os.makedirs(output_dir, exist_ok=True)

  for i in range(0, total_length, segment_length):
    segment = audio[i:i+segment_length]
    file_constant = os.path.splitext(os.path.basename(file_path))[0]
    segment.export(os.path.join(output_dir, f"{file_constant}_segment_{i//segment_length + 1}.

if __name__ == "__main__":
  input_file = "path/to/file.mp3" ## Set this to the location of the file you want to split. MP3 and MP4 files are compatible, but will always convert to MP3.
  output_directory = "output/directory" ## Set this to the output directory you want to use.
  split_audio(input_file, output_directory)
```

This script will split your large audio file into smaller segments of 2.5 hours maximum each and save them in the
specified output directory. You can input either audio or video files, and they will convert to MP3 when splitting. Make
sure to set the input, and output, directories for your files.

### 2. Run the script:

```bash  theme={null}
python split_audio.py
```

After running the script, your output directory should now contain your original audio clip split into compatible
segments to transcribe with Salad Transcription API. It should look something like this:

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/audio-split.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=5539bffc2340de2ab99a486b0b269734" data-og-width="960" width="960" data-og-height="92" height="92" data-path="transcription/images/audio-split.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/audio-split.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=16ac140c757667416c537a5b6f84f761 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/audio-split.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=b0fafe6720cd1d385669a69658afa053 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/audio-split.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=01f427813c11ddb6d208d5f042788e71 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/audio-split.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=98686c7528d02dad2d9024896cdb84fd 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/audio-split.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=98316713131777fbca58124eb35bbe93 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/audio-split.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=c6925f68a5d4d123ea52e0cfce78bceb 2500w" />

You can now use these audio files to transcribe with using
[Salad Transcription API.](/transcription/tutorials/transcription-quick-start)
