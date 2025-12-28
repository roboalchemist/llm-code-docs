# Source: https://meta-pytorch.org/torchcodec/stable/generated_examples/encoding/video_encoding.html

# Encoding video frames with VideoEncoder[¶](#encoding-video-frames-with-videoencoder)

In this example, we’ll learn how to encode video frames to a file or to raw
bytes using the [`VideoEncoder`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder) class.

First, we’ll download a video and decode some frames to tensors.
These will be the input to the [`VideoEncoder`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder). For more details on decoding,
see [Decoding a video with VideoDecoder](../decoding/basic_example.html#sphx-glr-generated-examples-decoding-basic-example-py).
Otherwise, skip ahead to [Creating an encoder](#creating-encoder).

import requests
from torchcodec.decoders import VideoDecoder
from IPython.display import Video

def play_video(encoded_bytes):
    return Video(
        data=encoded_bytes.numpy().tobytes(),
        embed=True,
        width=640,
        height=360,
        mimetype="video/mp4",
    )

# Video source: https://www.pexels.com/video/adorable-cats-on-the-lawn-4977395/
# Author: Altaf Shah.
[url](https://docs.python.org/3/library/stdtypes.html#str) = "https://videos.pexels.com/video-files/4977395/4977395-hd_1920_1080_24fps.mp4"

response = requests.get([url](https://docs.python.org/3/library/stdtypes.html#str), headers={"User-Agent": ""})
if [response.status_code](https://docs.python.org/3/library/functions.html#int) != 200:
    raise RuntimeError(f"Failed to download video. {[response.status_code](https://docs.python.org/3/library/functions.html#int) = }.")

[raw_video_bytes](https://docs.python.org/3/library/stdtypes.html#bytes) = response.content

decoder = VideoDecoder([raw_video_bytes](https://docs.python.org/3/library/stdtypes.html#bytes))
[frames](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor) = decoder.get_frames_in_range(0, 60).data  # Get first 60 frames
[frame_rate](https://docs.python.org/3/library/functions.html#float) = [decoder.metadata.average_fps](https://docs.python.org/3/library/functions.html#float)

## Creating an encoder[¶](#creating-an-encoder)

Let’s instantiate a [`VideoEncoder`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder). We will need to provide
the frames to be encoded as a 4D tensor of shape
`(num_frames, num_channels, height, width)` with values in the `[0, 255]`
range and `torch.uint8` dtype. We will also need to provide the frame rate of the input
video.

Note

The `frame_rate` parameter corresponds to the frame rate of the
*input* video. It will also be used for the frame rate of the *output* encoded video.

from torchcodec.encoders import VideoEncoder

print(f"{[frames.shape](https://docs.pytorch.org/docs/stable/size.html#torch.Size) = }, {[frames.dtype](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch.dtype) = }")
print(f"{[frame_rate](https://docs.python.org/3/library/functions.html#float) = } fps")

encoder = VideoEncoder([frames](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor)=[frames](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor), [frame_rate](https://docs.python.org/3/library/functions.html#float)=[frame_rate](https://docs.python.org/3/library/functions.html#float))

frames.shape = torch.Size([60, 3, 1080, 1920]), frames.dtype = torch.uint8
frame_rate = 24.0 fps

## Encoding to file, bytes, or file-like[¶](#encoding-to-file-bytes-or-file-like)

[`VideoEncoder`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder) supports encoding frames into a
file via the [`to_file()`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder.to_file) method, to
file-like objects via the [`to_file_like()`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder.to_file_like)
method, or to raw bytes via [`to_tensor()`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder.to_tensor).
For now we will use [`to_tensor()`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder.to_tensor), so we
can easily inspect and display the encoded video.

[encoded_frames](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor) = encoder.to_tensor(format="mp4")
play_video([encoded_frames](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor))

 Your browser does not support the video tag.

Now that we have encoded data, we can decode it back to verify the
round-trip encode/decode process works as expected:

decoder_verify = VideoDecoder([encoded_frames](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor))
[decoded_frames](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor) = decoder_verify.get_frames_in_range(0, 60).data

print(f"Re-decoded video: {[decoded_frames.shape](https://docs.pytorch.org/docs/stable/size.html#torch.Size) = }")
print(f"Original frames: {[frames.shape](https://docs.pytorch.org/docs/stable/size.html#torch.Size) = }")

Re-decoded video: decoded_frames.shape = torch.Size([60, 3, 1080, 1920])
Original frames: frames.shape = torch.Size([60, 3, 1080, 1920])

## Codec Selection[¶](#codec-selection)

By default, the codec used is selected automatically using the file extension provided
in the `dest` parameter for the [`to_file()`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder.to_file) method,
or using the `format` parameter for the
[`to_file_like()`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder.to_file_like) and
[`to_tensor()`](../../generated/torchcodec.encoders.VideoEncoder.html#torchcodec.encoders.VideoEncoder.to_tensor) methods.

For example, when encoding to MP4 format, the default codec is typically `H.264`.

To use a codec other than the default, use the `codec` parameter.
You can specify either a specific codec implementation (e.g., `"libx264"`)
or a codec specification (e.g., `"h264"`). Different codecs offer
different tradeoffs between quality, file size, and encoding speed.

Note

To see available encoders on your system, run `ffmpeg -encoders`.

Let’s encode the same frames using different codecs:

import tempfile
from pathlib import [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)

# H.264 encoding
[h264_output](https://docs.python.org/3/library/stdtypes.html#str) = [tempfile.NamedTemporaryFile](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile)(suffix=".mp4", delete=False).[name](https://docs.python.org/3/library/stdtypes.html#str)
encoder.to_file([h264_output](https://docs.python.org/3/library/stdtypes.html#str), codec="libx264")

# H.265 encoding
[hevc_output](https://docs.python.org/3/library/stdtypes.html#str) = [tempfile.NamedTemporaryFile](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile)(suffix=".mp4", delete=False).[name](https://docs.python.org/3/library/stdtypes.html#str)
encoder.to_file([hevc_output](https://docs.python.org/3/library/stdtypes.html#str), codec="hevc")

# Now let's use ffprobe to verify the codec used in the output files
import subprocess

for [output](https://docs.python.org/3/library/stdtypes.html#str), [name](https://docs.python.org/3/library/stdtypes.html#str) in [([h264_output](https://docs.python.org/3/library/stdtypes.html#str), "h264_output"), ([hevc_output](https://docs.python.org/3/library/stdtypes.html#str), "hevc_output")]:
    [result](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess) = [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run)(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=codec_name",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            [output](https://docs.python.org/3/library/stdtypes.html#str),
        ],
        capture_output=True,
        text=True,
    )
    print(f"Codec used in {[name](https://docs.python.org/3/library/stdtypes.html#str)}: {[result](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess).stdout.strip()}")

Codec used in h264_output: h264
Codec used in hevc_output: hevc

## Pixel Format[¶](#pixel-format)

The `pixel_format` parameter controls the color sampling (chroma subsampling)
of the output video. This affects both quality and file size.

Common pixel formats:

- 
`"yuv420p"` - 4:2:0 chroma subsampling (standard quality, smaller file size, widely compatible)

- 
`"yuv444p"` - 4:4:4 chroma subsampling (full chroma resolution, higher quality, larger file size)

Most playback devices and platforms support `yuv420p`, making it the most
common choice for video encoding.

Note

Pixel format support depends on the codec used. Use `ffmpeg -h encoder=<codec_name>`
to check available options for your selected codec.

# Standard pixel format
[yuv420_encoded_frames](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor) = encoder.to_tensor(
    format="mp4", codec="libx264", pixel_format="yuv420p"
)
play_video([yuv420_encoded_frames](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor))

 Your browser does not support the video tag.

## CRF (Constant Rate Factor)[¶](#crf-constant-rate-factor)

The `crf` parameter controls video quality, where lower values produce higher quality output.

For example, with the commonly used H.264 codec, `libx264`:

- 
Values range from 0 (lossless) to 51 (worst quality)

- 
Values 17 or 18 are considered visually lossless, and the default is 23.

Note

The range and interpretation of CRF values depend on the codec used, and
not all codecs support CRF. Use `ffmpeg -h encoder=<codec_name>` to
check available options for your selected codec.

# High quality (low CRF)
[high_quality_output](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor) = encoder.to_tensor(format="mp4", codec="libx264", crf=0)
play_video([high_quality_output](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor))

 Your browser does not support the video tag.

Low quality (high CRF)

[low_quality_output](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor) = encoder.to_tensor(format="mp4", codec="libx264", crf=50)
play_video([low_quality_output](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor))

 Your browser does not support the video tag.

## Preset[¶](#preset)

The `preset` parameter controls the tradeoff between encoding speed and file compression.
Faster presets encode faster but produce larger files, while slower
presets take more time to encode but result in better compression.

For example, with the commonly used H.264 codec, `libx264` presets include
`"ultrafast"` (fastest), `"fast"`, `"medium"` (default), `"slow"`, and
`"veryslow"` (slowest, best compression). See the
[H.264 Video Encoding Guide](https://trac.ffmpeg.org/wiki/Encode/H.264#a2.Chooseapresetandtune)
for additional details.

Note

Not all codecs support the `presets` option. Use `ffmpeg -h encoder=<codec_name>`
to check available options for your selected codec.

# Fast encoding with a larger file size
[fast_output](https://docs.python.org/3/library/stdtypes.html#str) = [tempfile.NamedTemporaryFile](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile)(suffix=".mp4", delete=False).[name](https://docs.python.org/3/library/stdtypes.html#str)
encoder.to_file([fast_output](https://docs.python.org/3/library/stdtypes.html#str), codec="libx264", preset="ultrafast")
print(f"Size of fast encoded file: {[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)([fast_output](https://docs.python.org/3/library/stdtypes.html#str)).stat().st_size} bytes")

# Slow encoding for a smaller file size
[slow_output](https://docs.python.org/3/library/stdtypes.html#str) = [tempfile.NamedTemporaryFile](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile)(suffix=".mp4", delete=False).[name](https://docs.python.org/3/library/stdtypes.html#str)
encoder.to_file([slow_output](https://docs.python.org/3/library/stdtypes.html#str), codec="libx264", preset="veryslow")
print(f"Size of slow encoded file: {[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)([slow_output](https://docs.python.org/3/library/stdtypes.html#str)).stat().st_size} bytes")

Size of fast encoded file: 7253009 bytes
Size of slow encoded file: 2110051 bytes

## Extra Options[¶](#extra-options)

The `extra_options` parameter accepts a dictionary of codec-specific options
that would normally be set via FFmpeg command-line arguments. This enables
control of encoding settings beyond the common parameters.

For example, some potential extra options for the commonly used H.264 codec, `libx264` include:

- 
`"g"` - GOP (Group of Pictures) size / keyframe interval

- 
`"max_b_frames"` - Maximum number of B-frames between I and P frames

- 
`"tune"` - Tuning preset (e.g., `"film"`, `"animation"`, `"grain"`)

Note

Use `ffmpeg -h encoder=<codec_name>` to see all available options for
a specific codec.

[custom_output](https://docs.python.org/3/library/stdtypes.html#str) = [tempfile.NamedTemporaryFile](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile)(suffix=".mp4", delete=False).[name](https://docs.python.org/3/library/stdtypes.html#str)
encoder.to_file(
    [custom_output](https://docs.python.org/3/library/stdtypes.html#str),
    codec="libx264",
    extra_options={
        "g": 50,                # Keyframe every 50 frames
        "max_b_frames": 0,      # Disable B-frames for faster decoding
        "tune": "fastdecode",   # Optimize for fast decoding
    }
)

**Total running time of the script:** (0 minutes 35.225 seconds)

[`Download Jupyter notebook: video_encoding.ipynb`](../../_downloads/e8868f804bffbeae56ed6b335353e809/video_encoding.ipynb)

[`Download Python source code: video_encoding.py`](../../_downloads/2da325461f15d27a53d05baddd7a3f9c/video_encoding.py)

[`Download zipped: video_encoding.zip`](../../_downloads/b642c54b41acc0759a9f5f6a35c7bb9a/video_encoding.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io)