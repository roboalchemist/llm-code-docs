# Glossary

This is a glossary of terms that often appear in discussion about multimedia transmissions. Some of the terms are specific to GStreamer or Kurento, and most of them are described and linked to their RFC, W3C or Wikipedia documents.

Agnostic media

One of the big problems of media is that the number of variants of video and audio codecs, formats and variants quickly creates high complexity in heterogeneous applications. So Kurento developed the concept of an automatic converter of media formats that enables development of *agnostic* elements. Whenever a media element’s source is connected to another media element’s sink, the Kurento framework verifies if media adaption and transcoding is necessary and, if needed, it transparently incorporates the appropriate transformations making possible the  chaining of the two elements into the resulting Pipeline.

AVI

Audio Video Interleaved, known by its initials AVI, is a multimedia container format introduced by Microsoft in November 1992 as part of its Video for Windows technology. AVI files can contain both audio and video data in a file container that allows synchronous audio-with-video playback. AVI is a derivative of the Resource Interchange File Format (RIFF).

See also

Wikipedia: Audio Video Interleave [https://en.wikipedia.org/wiki/Audio Video Interleave]

Wikipedia: Resource Interchange File Format [https://en.wikipedia.org/wiki/Resource Interchange File Format]