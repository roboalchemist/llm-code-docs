# Source: https://rustdesk.com/docs/en/self-host/

# Self-host

If you are using RustDesk you should have your own RustDesk Server, these docs will help you on your RustDesk journey.

Support is available via our Discord for OSS and [email](/cdn-cgi/l/email-protection#0c7f797c7c637e784c7e797f7868697f67226f6361) for Pro.

## How does self-hosted server work?

There are technically two executables (servers):

- `hbbs` - RustDesk ID (rendezvous / signaling) server, listen on TCP (`21114` - for http in Pro only, `21115`, `21116`, `21118` for web socket) and UDP (`21116`)
- `hbbr` - RustDesk relay server, listen on TCP (`21117`, `21119` for web socket)

When you install via installation script / docker compose / deb, the two services will be both installed.

Here are illustrations of how RustDesk client communicates with `hbbr` / `hbbs`.

As long as RustDesk is running on a machine, the machine constantly pings the ID server (`hbbs`) to make its current IP address and port known.

When you start a connection from computer A to computer B, computer A contacts the ID server and requests to communicate with computer B.

The ID server then attempts to connect A and B directly to each other using hole punching.

If hole punching fails, A will communicate with B via the relay server (`hbbr`).

In the majority of cases, hole punching is successful, and the relay server is never used.

Here is a discussion about Should you self-host a rustdesk server?

## Ports Required

Ports required for RustDesk Server self-hosting depends largely on your environment and what you want to do with RustDesk. The Examples shown throughout the docs will generally have all ports suggested to be opened.

Core Ports:
TCP `21114-21119`
UDP `21116`

The above `21115-21117` are the minimum required ports for RustDesk to work, these handle the signal and relay ports as well as NAT traversal.

TCP ports `21118` and `21119` are the WebSocket ports for the RustDesk Web Client, you need a reverse proxy to make it support HTTPS, please refer this sample Nginx configuration.

For Pro users without an SSL Proxy you will need to open TCP port `21114` for the API to work alternatively using an SSL Proxy open TCP port `443`.

RustDesk Server OSSRustDesk Server ProClient ConfigurationClient DeploymentNAT Loopback issues