# Source: https://ngrok.com/docs/universal-gateway/protocols.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Endpoint Protocols

> Learn about the four endpoint protocols supported by ngrok: HTTP/S, TCP, and TLS, and how they determine traffic processing.

Endpoints have one of four supported **protocols**:

* [HTTP/S Endpoints](/universal-gateway/http) - `http`, `https`
* [TCP Endpoints](/universal-gateway/tcp) - `tcp`
* [TLS Endpoints](/universal-gateway/tls) - `tls`

An Endpoint's protocol is specified in the scheme of its URL. For example:

* `https://app.example.com` uses the `https` protocol
* `tcp://db.internal:3306` uses the `tcp` protocol

An Endpoint's protocol determines:

1. How it processes connections that it receives
2. The phases, variables, and actions that may be defined on its [Traffic
   Policy](/traffic-policy).
3. What hostnames and ports may be specified in its URL

Learn more about in the [Endpoints documentation](/universal-gateway/endpoints).


Built with [Mintlify](https://mintlify.com).