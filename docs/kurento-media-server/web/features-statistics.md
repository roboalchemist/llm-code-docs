# WebRTC Statistics

[TODO full review]

## Introduction

WebRTC streams (audio, video, or data) can be lost, and experience varying
amounts of network delay. In order to assess the performance of WebRTC
applications, it could be required to be able to monitor the WebRTC features of
the underlying network and media pipeline.

To that aim, Kurento provides WebRTC statistics gathering for the server-side
(Kurento Media Server, KMS). The implementation of this capability follows the
guidelines provided in the
W3C WebRTC’s Statistics API [https://www.w3.org/TR/webrtc-stats/].
Therefore, the statistics gathered in the KMS can be divided into two groups:

- 

*inboundrtp*: statistics on the stream received in the KMS.

- 

*outboundrtp*: statistics on the stream sent by KMS.

## API description

As usual, WebRTC statistics gathering capability is provided by the KMS and is
consumed by means of the different Kurento client implementations (Java,
JavaScript clients are provided out of the box). To read these statistics,
first it should be enabled using the method *setLatencyStats* of a Media
Pipeline object. Using the Kurento Java client this is done as follows:

```
String kmsWsUri = "ws://localhost:8888/kurento";
KurentoClient kurentoClient = KurentoClient.create(kmsWsUri);
MediaPipeline mediaPipeline = kurentoClient.createMediaPipeline();
mediaPipeline.setLatencyStats(true);

// ...

```