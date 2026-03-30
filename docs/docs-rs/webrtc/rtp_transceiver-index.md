webrtc
# Module rtp_transceiver 
Source 
## Modules§
rtp_codecrtp_receiverrtp_senderrtp_transceiver_direction
## Structs§
RTCPFeedbackrtcpfeedback signals the connection to use additional RTCP packet types.
https://draft.ortc.org/#dom-rtcrtcpfeedbackRTCRtpCapabilitiesRTPCapabilities represents the capabilities of a transceiver
https://w3c.github.io/webrtc-pc/#rtcrtpcapabilitiesRTCRtpCodingParametersRTPCodingParameters provides information relating to both encoding and decoding.
This is a subset of the RFC since Pion WebRTC doesn’t implement encoding/decoding itself
http://draft.ortc.org/#dom-rtcrtpcodingparametersRTCRtpReceiveParametersRTPReceiveParameters contains the RTP stack settings used by receiversRTCRtpRtxParametersRTPRtxParameters dictionary contains information relating to retransmission (RTX) settings.
https://draft.ortc.org/#dom-rtcrtprtxparametersRTCRtpSendParametersRTPSendParameters contains the RTP stack settings used by receiversRTCRtpTransceiverRTPTransceiver represents a combination of an RTPSender and an RTPReceiver that share a common mid.RTCRtpTransceiverInitRTPTransceiverInit dictionary is used when calling the WebRTC function addTransceiver() to provide configuration options for the new transceiver.
## Constants§
TYPE_RTCP_FB_ACKTYPE_RTCP_FB_ACK ..TYPE_RTCP_FB_CCMTYPE_RTCP_FB_CCM ..TYPE_RTCP_FB_GOOG_REMBTYPE_RTCP_FB_GOOG_REMB ..TYPE_RTCP_FB_NACKTYPE_RTCP_FB_NACK ..TYPE_RTCP_FB_TRANSPORT_CCTYPE_RTCP_FBT_RANSPORT_CC ..
## Type Aliases§
PayloadTypePayloadType identifies the format of the RTP payload and determines
its interpretation by the application. Each codec in a RTP Session
will have a different PayloadType
https://tools.ietf.org/html/rfc3550#section-3RTCRtpDecodingParametersRTPDecodingParameters provides information relating to both encoding and decoding.
This is a subset of the RFC since Pion WebRTC doesn’t implement decoding itself
http://draft.ortc.org/#dom-rtcrtpdecodingparametersRTCRtpEncodingParametersRTPEncodingParameters provides information relating to both encoding and decoding.
This is a subset of the RFC since Pion WebRTC doesn’t implement encoding itself
http://draft.ortc.org/#dom-rtcrtpencodingparametersSSRCSSRC represents a synchronization source
A synchronization source is a randomly chosen
value meant to be globally unique within a particular
RTP session. Used to identify a single stream of media.
https://tools.ietf.org/html/rfc3550#section-3TriggerNegotiationNeededFnOption