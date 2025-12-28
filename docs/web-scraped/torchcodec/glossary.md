# Source: https://meta-pytorch.org/torchcodec/stable/glossary.html

# Glossary[¶](#glossary "Permalink to this heading")

pts[¶](#term-pts "Permalink to this term")

:   Presentation Time Stamp. The time at which a frame or audio sample should be played. In TorchCodec, pts are expressed in seconds.

best stream[¶](#term-best-stream "Permalink to this term")

:   The notion of "best" stream is determined by FFmpeg. Quoting the [FFmpeg docs](https://ffmpeg.org/doxygen/trunk/group__lavf__decoding.html#ga757780d38f482deb4d809c6c521fbcc2):

    > <div>
    >
    > *The best stream is determined according to various heuristics as the most likely to be what the user expects.*
    >
    > </div>

scan[¶](#term-scan "Permalink to this term")

:   A scan corresponds to an entire pass over a video file, with the purpose of retrieving metadata about the different streams and frames. **It does not involve decoding**, so it is a lot cheaper than decoding the file. The [[`VideoDecoder`]](generated/torchcodec.decoders.VideoDecoder.html#torchcodec.decoders.VideoDecoder "torchcodec.decoders.VideoDecoder") performs a scan when using [`seek_mode="exact"`], and doesn't scan when using [`seek_mode="approximate"`].

clips[¶](#term-clips "Permalink to this term")

:   A clip is a sequence of frames, usually in [[pts]](#term-pts) order. The frames may not necessarily be consecutive. A clip is represented as a 4D [[`FrameBatch`]](generated/torchcodec.FrameBatch.html#torchcodec.FrameBatch "torchcodec.FrameBatch"). A group of clips, which is what the [[samplers]](api_ref_samplers.html#samplers) return, is represented as 5D [[`FrameBatch`]](generated/torchcodec.FrameBatch.html#torchcodec.FrameBatch "torchcodec.FrameBatch").