# Java - Send DataChannel

This tutorial connects a player with a QR code detection filter and sends output
to WebRTC. Code detection events are sent to browser using WebRTC datachannels.

Note

Web browsers require using *HTTPS* to enable WebRTC, so the web server must use SSL and a certificate file. For instructions, check Configure a Java server to use HTTPS.

For convenience, this tutorial already provides dummy self-signed certificates (which will cause a security warning in the browser).