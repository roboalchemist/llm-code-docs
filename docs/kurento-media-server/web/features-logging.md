# Debug Logging

Kurento Media Server prints log messages by using the GStreamer logging library [https://gstreamer.freedesktop.org/documentation/gstreamer/running.html]. This is a very flexible library that allows users to fine-tune the amount of verbosity that they want to get from the media server.

Logging verbosity is controlled by setting the *GST_DEBUG* environment variable with an appropriate string. In this section we’ll show some useful examples, and then provide complete technical documentation about the logging features available for Kurento.

Table of Contents

- 

Debug Logging

  - 

Default levels

  - 

Verbose logging

    - 

Flowing of media

    - 

Transcoding of media

    - 

WebRtcEndpoint and RtpEndpoint

    - 

PlayerEndpoint

    - 

RecorderEndpoint

    - 

Other components

    - 

3rd-Party libraries

      - 

libnice

      - 

libsoup

      - 

libusrsctp (WebRTC DataChannels)

  - 

Logs Location

    - 

Logs Rotation

  - 

Log Contents

    - 

Log colors

  - 

Logging levels and components