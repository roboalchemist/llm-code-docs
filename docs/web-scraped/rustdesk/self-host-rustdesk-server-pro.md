# Source: https://rustdesk.com/docs/en/self-host/rustdesk-server-pro/

# RustDesk Server Pro

RustDesk Server Pro has more features compared to the open source version.

- Account
- Web console
- API
- OIDC, LDAP, 2FA
- Address book
- Log management (Connection, file transfer, alarm, etc.)
- Device management
- Security Settings sync
- Access control
- Multiple relay servers (automatically selects your closest relay)
- Custom client generator
- WebSocket
- Web client self-host

Note

If you build your own server on your home/office, and can&rsquo;t connect it through public IP/domain, please check this article.

Note

We recommend reading this first before proceeding, How does self-hosted server work?.

## Hardware requirement

Lowest level VPS is enough for your use cases. The server software is not CPU and memory intensive. Our public ID server hosted on a 2 CPU/4 GB Vultr server serves 1.0+ million endpoints. Each relay connection consumes avg 180kb per second. 1 cpu core and 1G ram is enough to support 1000 relay concurrent connections.

## Article tutorials

Step-by-Step Guide: Self-Host RustDesk Server Pro on Cloud via Docker for Secure Remote Access

## Video tutorials

[Beginner&rsquo;s Guide: Self-Host RustDesk Server Pro for Novice Linux User](https://www.youtube.com/watch?v=MclmfYR3frk)

Quick Guide: Self-Host RustDesk Server Pro for Adavanced Linux User

## License

You can get license from https://rustdesk.com/pricing.html, check license page for more details.

## Get started

### 1, Installation

```
bash <(wget -qO- https://get.docker.com)
wget rustdesk.com/pro.yml -O compose.yml
sudo docker compose up -d
```

For more details, please check Docker.

### 2, Ports Required

You need port `21114`-`21119` TCP and `21116` UDP open, please ensure these ports are setup when you set firewall rules and Docker port mapping.

More information about these ports, please check here.

### 3, Set license

Open your web console by accessing `http://<server ip>:21114`, log in using the default credentials admin/test1234 `admin`/`test1234`. Follow this guide to set the license.

### 4, Setup HTTPS for web console

You can skip this step if you don&rsquo;t want to use HTTPS during the trial, but remember to change the client&rsquo;s API address after you set up HTTPS

Here is a simple tutorial of manual HTTPS setup.

### 5, Configure client to use the self-hosted server

https://rustdesk.com/docs/en/self-host/client-configuration/

### 6, Set up WebSocket

To enable web client or desktop / mobile client work properly with WebSocket, you need to add the following settings to your reverse proxy configuration.

https://rustdesk.com/docs/en/self-host/rustdesk-server-pro/faq/#8-add-websocket-secure-wss-support-for-the-id-server-and-relay-server-to-enable-secure-communication-for-all-platforms

## Upgrade Server

This guide covers how to upgrade RustDesk Server Pro from a lower version, addressing different installation methods.

## Migrate to new host and backup / restore

Here is a detailed tutorial.

## Migrate license

Please follow this guide.

## Upgrade license

Follow this guide to upgrade your license for more users and devices at any time.

## About security

https://github.com/rustdesk/rustdesk/discussions/9835