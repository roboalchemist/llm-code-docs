webrtc::rtp_transceiver
# Module rtp_codec 
Source 
## Structs§
RTCRtpCodecCapabilityRTPCodecCapability provides information about codec capabilities.RTCRtpCodecParametersRTPCodecParameters is a sequence containing the media codecs that an RtpSender
will choose from, as well as entries for RTX, RED and FEC mechanisms. This also
includes the PayloadType that has been negotiated
https://w3c.github.io/webrtc-pc/#rtcrtpcodecparametersRTCRtpHeaderExtensionCapabilityRTPHeaderExtensionCapability is used to define a RFC5285 RTP header extension supported by the codec.
https://w3c.github.io/webrtc-pc/#dom-rtcrtpcapabilities-headerextensionsRTCRtpHeaderExtensionParametersRTPHeaderExtensionParameter represents a negotiated RFC5285 RTP header extension.
https://w3c.github.io/webrtc-pc/#dictionary-rtcrtpheaderextensionparameters-membersRTCRtpParametersRTPParameters is a list of negotiated codecs and header extensions
https://w3c.github.io/webrtc-pc/#dictionary-rtcrtpparameters-members
## Enums§
RTPCodecTypeRTPCodecType determines the type of a codec