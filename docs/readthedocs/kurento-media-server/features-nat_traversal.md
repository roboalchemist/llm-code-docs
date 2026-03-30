# NAT Traversal

NAT Traversal, also known as *Hole Punching*, is the procedure of opening an inbound port in the NAT tables of the routers which implement this technology (which are the vast majority of home and corporate routers).

There are different types of NAT, depending on how they behave: **Full Cone**, **Address-Restricted Cone**, **Port-Restricted Cone**, and **Symmetric**. For a comprehensive explanation of NAT and the different types that exist, please read our Knowledge Base document: NAT Types and NAT Traversal.

## WebRTC with ICE

ICE is the standard method used by WebRTC to solve the issue of NAT Traversal. Kurento supports ICE by means of a 3rd-party library: libnice, The GLib ICE implementation [https://nice.freedesktop.org].

Refer to the logging documentation if you need to enable the debug logging for this library.

## RTP without ICE

KMS is able to automatically infer what is the public IP and port of any remote peer which is communicating with it through an RTP connection. This removes the need to use ICE in some specific situations, where that complicated mechanism is not desired. This new automatic port discovery was inspired by the **Connection-Oriented Media Transport** (COMEDIA) as presented by the early Drafts of what finally would become the **RFC 4145** [https://datatracker.ietf.org/doc/html/rfc4145.html].

**TCP-Based Media Transport in the Session Description Protocol** (SDP) (IETF RFC 4145 [https://tools.ietf.org/html/rfc4145]) defines an SDP extension which adds TCP connections and procedures, such as how a passive machine would wait for connections from a remote active machine and be able to obtain connection information from the active one, upon reception of an initial connection.

Early Drafts of **RFC 4145** [https://datatracker.ietf.org/doc/html/rfc4145.html] (up to Draft 05 [https://tools.ietf.org/html/draft-ietf-mmusic-sdp-comedia-05]) also contemplated the usage of this same concept of “Connection-Oriented Media Transport in SDP” with UDP connections, as a way of aiding NAT Traversal. This is what has been used as a basis for the implementation of automatic port discovery in KMS.

It works as follows:

- 

The machine behind a NAT router acts as the active peer. It sends an SDP Offer to the other machine, the passive peer.

  - 

Sending an SDP Offer from behind a NAT means that the IP and port specified in the SDP message are actually just the private IP and port of that machine, instead of the public ones. The passive peer won’t be able to use these to communicate back to the active peer. Due to this, the SDP Offer states the port *9* (*Discard port*) instead of whatever port the active machine will be using.

  - 

The SDP Offer includes the media-level attribute `a=direction:active`, so the passive peer is able to acknowledge that the Connection-Oriented Media Transport is being used for that media, and it writes `a=direction:passive` in its SDP Answer.

- 

The passive peer receives the SDP Offer and answers it as usual, indicating the public IP and port where it will be listening for incoming packets. Besides that, it must ignore the IP and port indicated in the received SDP Offer. Instead, it must enter a wait state, until the active peer starts sending some packets.

- 

When the active peer sends the first RTP/RTCP packets to the IP and port specified in the SDP Answer, the passive peer will be able to analyze them on reception and extract the public IP and reception port of the active peer.

- 

The passive peer is now able to send RTP/RTCP packets to the discovered IP and port values of the active peer.

This mechanism has the following requisites and/or limitations:

- 

Only the active peer can be behind a NAT router. The passive peer must have a publicly accessible IP and port for RTP.

- 

The active peer must be able to receive RTP/RTCP packets at the same ports that are used to send RTP/RTCP packets. In other words, the active peer must be compatible with *Symmetric RTP and RTCP* as defined in IETF RFC 4961 [https://tools.ietf.org/html/rfc4961].

- 

The active peer must actually do send some RTP/RTCP packets before the passive peer is able to send any data back. In other words, it is not possible to establish a one-way stream where only the passive peer sends data to the active peer.

This is how to enable the Connection-Oriented Media Transport mode:

- 

The SDP Offer must be sent from the active peer to the passive peer.

- 

The IP stated in the SDP Offer can be anything (as it will be ignored), so *0.0.0.0* can be used.

- 

The Port stated in the SDP Offer should be *9* (*Discard port*).

- 

The active peer must include the media-level attribute `a=direction:active` in the SDP Offer, for each media that requires automatic port discovery.

- 

The passive peer must acknowledge that it supports the automatic port discovery mode, by including the media-level attribute `a=direction:passive` in its SDP Answer. As per normal rules of the SDP Offer/Answer Model (IETF RFC 3264 [https://tools.ietf.org/html/rfc3264]), if this attribute is not present in the SDP Answer, then the active peer must assume that the passive peer is not compatible with this functionality and should react to this fact as whatever is deemed appropriate by the application developer.

### Example

This is a minimal example of an SDP Offer/Answer negotiation that a machine would perform with KMS from behind a NAT router. The highlighted lines are those relevant to NAT Traversal:

SDP Offer