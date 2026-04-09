# RTP Streaming Commands

In this document you will find several examples of command-line programs that can be used to generate RTP and SRTP streams. These streams can then be used to feed any general (S)RTP receiver, although the intention here is to use them to connect an *RtpEndpoint* from a Kurento Media Server pipeline.

The tool used for all these programs is gst-launch [https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html], part of the GStreamer multimedia library.

These examples start from the simplest and then build on each other to end up with a full featured RTP generator. Of course, as more features are added, the command grows in complexity. A very good understanding of *gst-launch* and of GStreamer is recommended.

To run these examples, follow these initial steps:

- 

Install required packages:

```
sudo apt-get update ; sudo apt-get install --no-install-recommends \
    gstreamer1.0-{tools,libav} \
    gstreamer1.0-plugins-{base,good,bad,ugly}

```