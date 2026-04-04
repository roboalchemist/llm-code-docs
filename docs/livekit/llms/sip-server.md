# Source: https://docs.livekit.io/transport/self-hosting/sip-server.md

LiveKit docs › Self-hosting › SIP server

---

# SIP server

> Setting up and configuring a self-hosted SIP server for LiveKit telephony apps.

## Overview

LiveKit SIP server allows you to make and receive phone calls using your LiveKit deployment. It's a self-hosted solution that allows you to deploy a SIP server on your own infrastructure.

> 🔥 **Caution**
> 
> Both SIP signaling port (`5060`) and media port range (`10000-20000`) must be accessible from the Internet. See [Firewall configuration](https://docs.livekit.io/transport/self-hosting/ports-firewall.md) for details.

## Docker Compose

The easiest way to run SIP Server is by using Docker Compose:

```shell
wget https://raw.githubusercontent.com/livekit/sip/main/docker-compose.yaml
docker compose up

```

This starts a local LiveKit server and SIP server connected to Redis.

## Running natively

You can also run SIP server natively without Docker.

1. Install SIP server by following the [Running locally](https://github.com/livekit/sip/#running-locally) instructions.
2. Create the `config.yaml` file with the following contents:

```yaml
api_key: <your-api-key>
api_secret: <your-api-secret>
ws_url: ws://localhost:7880
redis:
  address: localhost:6379
sip_port: 5060
rtp_port: 10000-20000
use_external_ip: true
logging:
  level: debug

```
3. Run the SIP server:

```shell
livekit-sip --config=config.yaml

```
4. Determine your SIP URI. Once your SIP server is running, you would have to determine the public IP address of the machine. Then your SIP URI should be in the format of `<public-ip-address>:5060`.

---

This document was rendered at 2026-02-03T03:25:21.509Z.
For the latest version of this document, see [https://docs.livekit.io/transport/self-hosting/sip-server.md](https://docs.livekit.io/transport/self-hosting/sip-server.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).