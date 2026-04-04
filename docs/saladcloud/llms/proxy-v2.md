# Source: https://docs.salad.com/gateway-service/explanation/proxy-v2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using PROXY v2 Protocol

> Connect to SGS using HAProxy's PROXY v2 protocol

*Last Updated: September 24, 2024*

### Requesting PROXY v2 support

SGS can also support HAproxy’s PROXY v2 protocol, which uses a client certificate rather than a password for
authentication. If you require PROXY protocol support, please contact your account manager and we'll be happy to
generate a client cert for you and enable PROXY v2 protocol support on the SGS server.

<Note>
  PROXY v2 protocol may be simpler to implement depending on how your infrastructure is configured, and may offer some
  performance benefits over HTTP CONNECT over TLS.
</Note>
