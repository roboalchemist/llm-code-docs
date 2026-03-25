# 6.13.0 (December 2019)

Kurento Media Server **6.13.0** has been released! It comes with some new API methods that allow to query Kurento about its own resource usage, as well as some new configuration parameters that can be used to fine-tune some aspects of how the server chooses ICE candidates during WebRTC initialization.

To install Kurento Media Server: Installation Guide.

These Release Notes were also posted on the Kurento blog [https://kurento.openvidu.io/blog/kurento-613-felices-fiestas].

## Added

- 

**WebRTC**: Add `externalAddress` to WebRtcEndpoint config & client API.

Allows to specify an external IP address, so Kurento doesn’t need to auto-discover it during WebRTC initialization. This saves time, and also removes the need for configuring external STUN or TURN servers.

The effect of this parameter is that all local ICE candidates that are gathered will be mangled to contain the provided external IP address instead of the local one, before being sent to the remote peer. Thanks to this, remote peers are able to know about the external or public IP address of Kurento.

Use this parameter if you know beforehand what will be the external or public IP address of the media server (e.g. because your deployment has an static IP), although keep in mind that some types of networks will still need you to install a TURN server. Best thing to do is to try with this option enabled, and if WebRTC fails, then default to the standard method of installing and configuring Coturn.

Kurento Client API docs: Java, JavaScript.

- 

**WebRTC**: Add `networkInterfaces` to WebRtcEndpoint config & client API.

If you know which network interfaces should be used to perform ICE (for WebRTC connectivity), you can define them here. Doing so has several advantages:

  - 

The WebRTC ICE gathering process will be much quicker. Normally, it needs to gather local candidates for all of the network interfaces, but this step can be made faster if you limit it to only the interface that you know will work.

  - 

It will ensure that the media server always decides to use the correct network interface. With WebRTC ICE gathering it’s possible that, under some circumstances (in systems with virtual network interfaces such as “docker0”) the ICE process ends up choosing the wrong local IP.

There is the long-running issue of how libnice gathers all possible local IP addresses for its ICE candidates, which introduces latency or connectivity problems for some many-networks deployments (like Amazon EC2, or Docker/Kubernetes): Kurento generates too many ICE candidates, and that results in the situation that sometimes (quite often, in practice) it fails to choose correct pair of ICE candidates and uses those ones from private networks, leading to non-obvious bugs and video stability problems.

More rationale for this feature can be found here: Kurento/bugtracker#278 [https://github.com/Kurento/bugtracker/issues/278] (*RFC: Add WebRtcEndpoint.externalIPs configuration parameter*).

Kurento Client API docs: Java, JavaScript.

- 

**WebRTC** / **RTP**: Add `mtu` to BaseRtpEndpoint config & client API.

Allows configuring the network MTU that Kurento will use for RTP transmissions, in both RtpEndpoint and WebRtcEndpoint. This parameter ends up configured in the GStreamer RTP payloader (`rtpvp8pay`, `rtph264pay`).

Kurento Client API docs: Java, JavaScript.

- 

**RTP**: Add support for `a=rtcp:{Port}` in SDP messages.

Allows a remote peer using non-consecutive RTCP ports. Normally, the RTCP port is just RTP+1, but with an `a=rtcp` attribute, the RTCP port can be set to anything.

Eg. with this SDP media line:

```
m=video 5004 RTP/AVP 96

```