# Source: https://headscale.net/stable/setup/requirements/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/setup/requirements.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/setup/requirements.md "View source of this page")

# Requirements[¶](#requirements "Permanent link")

Headscale should just work as long as the following requirements are met:

- A server with a public IP address for headscale. A dual-stack setup with a public IPv4 and a public IPv6 address is recommended.
- Headscale is served via HTTPS on port 443^[1](#fn:1)^ and [may use additional ports](#ports-in-use).
- A reasonably modern Linux or BSD based operating system.
- A dedicated local user account to run headscale.
- A little bit of command line knowledge to configure and operate headscale.

## Ports in use[¶](#ports-in-use "Permanent link")

The ports in use vary with the intended scenario and enabled features. Some of the listed ports may be changed via the [configuration file](../../ref/configuration/) but we recommend to stick with the default values.

- tcp/80
  - Expose publicly: yes
  - HTTP, used by Let\'s Encrypt to verify ownership via the HTTP-01 challenge.
  - Only required if the built-in Let\'s Enrypt client with the HTTP-01 challenge is used. See [TLS](../../ref/tls/) for details.
- tcp/443
  - Expose publicly: yes
  - HTTPS, required to make Headscale available to Tailscale clients^[1](#fn:1)^
  - Required if the [embedded DERP server](../../ref/derp/) is enabled
- udp/3478
  - Expose publicly: yes
  - STUN, required if the [embedded DERP server](../../ref/derp/) is enabled
- tcp/50443
  - Expose publicly: yes
  - Only required if the gRPC interface is used to [remote-control Headscale](../../ref/remote-cli/).
- tcp/9090
  - Expose publicly: no
  - [Metrics and debug endpoint](../../ref/debug/#metrics-and-debug-endpoint)

## Assumptions[¶](#assumptions "Permanent link")

The headscale documentation and the provided examples are written with a few assumptions in mind:

- Headscale is running as system service via a dedicated local user `headscale`.
- The [configuration](../../ref/configuration/) is loaded from `/etc/headscale/config.yaml`.
- SQLite is used as database.
- The data directory for headscale (used for private keys, ACLs, SQLite database, ...) is located in `/var/lib/headscale`.
- URLs and values that need to be replaced by the user are either denoted as `<VALUE_TO_CHANGE>` or use placeholder values such as `headscale.example.com`.

Please adjust to your local environment accordingly.

------------------------------------------------------------------------

1.  ::: 
    The Tailscale client assumes HTTPS on port 443 in certain situations. Serving headscale either via HTTP or via HTTPS on a port other than 443 is possible but sticking with HTTPS on port 443 is strongly recommended for production setups. See [issue 2164](https://github.com/juanfont/headscale/issues/2164) for more information. [↩](#fnref:1 "Jump back to footnote 1 in the text")[↩](#fnref2:1 "Jump back to footnote 1 in the text")
    :::