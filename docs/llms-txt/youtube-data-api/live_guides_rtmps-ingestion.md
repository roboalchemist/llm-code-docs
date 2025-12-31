# Source: https://developers.google.com/youtube/v3/live/guides/rtmps-ingestion.md.txt

# Delivering Live YouTube Content via RTMPS

This document explains how to use RTMPS to stream live data on YouTube from an
encoder. RTMPS is a regular RTMP (RealTime Messaging Protocol) video stream
tunneled through an SSL connection. This document is intended for encoder
vendors who want to add support for RTMPS to encoders that already support RTMP.

RTMPS is a good choice for most ordinary user content, especially if it requires
low latency. See the
[Ingestion Protocol Comparison](https://developers.google.com/youtube/v3/live/guides/ingestion-protocol-comparison)
for an overview of the different ingestion protocols that YouTube Live Streaming
supports.

## Requirements

Sending RTMPS to YouTube Live has a few prerequisites:

- Each part of the connection URL (`<protocol>://<server>/<path>`) must be correct:
  - The protocol must be `rtmps`.
  - The server must be a valid YouTube RTMPS ingestion endpoint.
  - The path must be a valid YouTube Live RTMP application name.
- The connection must be made to port 443 on the ingestion server.
- The multimedia stream must be sent with RTMPS; that is, using RTMP over an SSL connection.

## Getting the connection URL

If your encoder already uses the YouTube Live API, then the process for getting
an RTMPS ingestion URL is similar to the one for RTMP. Send a
[LiveStreams insert (POST)](https://developers.google.com/youtube/v3/live/docs/liveStreams/insert) request to
create a new ingestion stream. In the response, the
[`cdn.ingestionInfo.rtmpsIngestionAddress`](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.ingestionInfo.rtmpsIngestionAddress)
field specifies the RTMPS URL. If you support dual ingestion, the backup address
is [`cdn.ingestionInfo.rtmpsBackupIngestionAddress`](https://developers.google.com/youtube/v3/live/docs/liveStreams#cdn.ingestionInfo.rtmpsBackupIngestionAddress).

## Creating the connection

Use your preferred socket library to create an SSL/TLS connection to port 443 at
the server that the ingestion URL specifies. Since TLS works only with the
transport layer, the server hostname is not strictly required to initiate the
connection; however, it is required for authentication with our servers. So make
sure you add the SNI extension (Server Name Indication) to your SSL handshake,
and set the server name to the server hostname you're connecting to.

Once the SSL connection is established, use it as the connection for your RTMP
client library. An initialized SSL connection has the same API as a standard TCP
connection, and so the RTMP library should be able to work with both of them
identically.

## Troubleshooting

### SSL errors

If you attempt to create an SSL connection but get an invalid certificate, then
you are probably connecting to a YouTube server that expects RTMP. Make sure
that the server name you use has "rtmps" in it --- note the "s".

If the URL looks correct but you still get an SSL error, you might be connecting
to the wrong port. Confirm that you're connecting to port 443.

If the URL and port are correct, your SSL library might not be handling the
certificate correctly. Look for low-level diagnostic messages about SSL
failures, and double-check that you're using SNI in the handshake.

### Connection timed out

If you can connect to the server, but your RTMP library times out without
getting a sensible response, you might have set up a cleartext RTMP connection
to a YouTube server that expects RTMPS. Make sure that you're creating an SSL
connection, not a plain TCP connection.