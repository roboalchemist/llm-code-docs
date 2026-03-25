wolfssl
# Struct SessionConfig 
Source 

```
pub struct SessionConfig<IOCB: IOCallbacks> {
    pub io: IOCB,
    pub dtls_use_nonblock: Option<bool>,
    pub dtls_mtu: Option<u16>,
    pub server_name_indicator: Option<String>,
    pub checked_domain_name: Option<String>,
    pub keyshare_group: Option<CurveGroup>,
    pub dtls13_allow_ch_frag: Option<bool>,
    pub ssl_verify_mode: Option<SslVerifyMode>,
}
```

## Fields§
§`io: IOCB`

I/O callback handlers
§`dtls_use_nonblock: Option<bool>`

If set and the session is DTLS, sets the nonblocking mode.
§`dtls_mtu: Option<u16>`

If set and the session is DTLS, sets the MTU of the session.

If value exceeds wolfSSL’s `MAX_RECORD_SIZE` (currently 2^14), or
is 0, ignored.
§`server_name_indicator: Option<String>`

If set, configures SNI (Server Name Indication) for the session with the
given hostname.
§`checked_domain_name: Option<String>`

If set, configures the session to check the given domain against the
peer certificate during connection.
§`keyshare_group: Option<CurveGroup>`

If set, specifies a curve group to use for key share
§`dtls13_allow_ch_frag: Option<bool>`

If set, specifies if fragmented ClientHello (CH) is allowed
§`ssl_verify_mode: Option<SslVerifyMode>`

SSL Verify mode

## Implementations§