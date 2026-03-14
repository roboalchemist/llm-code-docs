webrtc::mux
# Module mux_func 
Source 
## Functions§
match_allmatch_all always returns truematch_dtlsMatchFuncs as described in RFC7983
https://tools.ietf.org/html/rfc7983
+––––––––+
|        [0..3] -+–> forward to STUN
|                |
|      [16..19] -+–> forward to ZRTP
|                |
packet –>  |      [20..63] -+–> forward to DTLS
|                |
|      [64..79] -+–> forward to TURN Channel
|                |
|    [128..191] -+–> forward to RTP/RTCP
+––––––––+
match_dtls is a MatchFunc that accepts packets with the first byte in [20..63]
as defined in RFC7983match_rangematch_range is a MatchFunc that accepts packets with the first byte in [lower..upper]match_srtcpmatch_srtcp is a MatchFunc that only matches SRTCP and not SRTPmatch_srtpmatch_srtp is a MatchFunc that only matches SRTP and not SRTCPmatch_srtp_or_srtcp
## Type Aliases§
MatchFuncMatchFunc allows custom logic for mapping packets to an Endpoint