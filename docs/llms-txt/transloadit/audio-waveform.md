# Source: https://transloadit.com/docs/robots/audio-waveform.md

We recommend that you use an [🤖/audio/encode](/docs/robots/audio-encode.md) Step prior to your waveform Step to convert audio files to MP3. This way it is guaranteed that [🤖/audio/waveform](/docs/robots/audio-waveform.md) accepts your audio file and you can also down-sample large audio files and save some money.

Similarly, if you need the output image in a different format, please pipe the result of this Robot into [🤖/image/resize](/docs/robots/image-resize.md).
