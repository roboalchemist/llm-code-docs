# Source: https://headscale.net/stable/ref/debug/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/ref/debug.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/ref/debug.md "View source of this page")

# Debugging and troubleshooting[¶](#debugging-and-troubleshooting "Permanent link")

Headscale and Tailscale provide debug and introspection capabilities that can be helpful when things don\'t work as expected. This page explains some debugging techniques to help pinpoint problems.

Please also have a look at [Tailscale\'s Troubleshooting guide](https://tailscale.com/kb/1023/troubleshooting). It offers a many tips and suggestions to troubleshoot common issues.

## Tailscale[¶](#tailscale "Permanent link")

The Tailscale client itself offers many commands to introspect its state as well as the state of the network:

- [Check local network conditions](https://tailscale.com/kb/1080/cli#netcheck): `tailscale netcheck`
- [Get the client status](https://tailscale.com/kb/1080/cli#status): `tailscale status --json`
- [Get DNS status](https://tailscale.com/kb/1080/cli#dns): `tailscale dns status --all`
- Client logs: `tailscale debug daemon-logs`
- Client netmap: `tailscale debug netmap`
- Test DERP connection: `tailscale debug derp headscale`
- And many more, see: `tailscale debug --help`

Many of the commands are helpful when trying to understand differences between Headscale and Tailscale SaaS.

## Headscale[¶](#headscale "Permanent link")

### Application logging[¶](#application-logging "Permanent link")

The log levels `debug` and `trace` can be useful to get more information from Headscale.

    log:
      # Valid log levels: panic, fatal, error, warn, info, debug, trace
      level: debug

### Database logging[¶](#database-logging "Permanent link")

The database debug mode logs all database queries. Enable it to see how Headscale interacts with its database. This also requires the application log level to be set to either `debug` or `trace`.

    database:
      # Enable debug mode. This setting requires the log.level to be set to "debug" or "trace".
      debug: false

    log:
      # Valid log levels: panic, fatal, error, warn, info, debug, trace
      level: debug

### Metrics and debug endpoint[¶](#metrics-and-debug-endpoint "Permanent link")

Headscale provides a metrics and debug endpoint. It allows to introspect different aspects such as:

- Information about the Go runtime, memory usage and statistics
- Connected nodes and pending registrations
- Active ACLs, filters and SSH policy
- Current DERPMap
- Prometheus metrics

Keep the metrics and debug endpoint private

The listen address and port can be configured with the `metrics_listen_addr` variable in the [configuration file](../configuration/). By default it listens on localhost, port 9090.

Keep the metrics and debug endpoint private to your internal network and don\'t expose it to the Internet.

Query metrics via <http://localhost:9090/metrics> and get an overview of available debug information via <http://localhost:9090/debug/>. Metrics may be queried from outside localhost but the debug interface is subject to additional protection despite listening on all interfaces.

Direct accessSSH port forwardingVia debug keyVia debug IP address

Access the debug interface directly on the server where Headscale is installed.

    curl http://localhost:9090/debug/

Use SSH port forwarding to forward Headscale\'s metrics and debug port to your device.

    ssh <HEADSCALE_SERVER> -L 9090:localhost:9090

Access the debug interface on your device by opening <http://localhost:9090/debug/> in your web browser.

The access control of the debug interface supports the use of a debug key. Traffic is accepted if the path to a debug key is set via the environment variable `TS_DEBUG_KEY_PATH` and the debug key sent as value for `debugkey` parameter with each request.

    openssl rand -hex 32 | tee debugkey.txt
    export TS_DEBUG_KEY_PATH=debugkey.txt
    headscale serve

Access the debug interface on your device by opening `http://<IP_OF_HEADSCALE>:9090/debug/?debugkey=<DEBUG_KEY>` in your web browser. The `debugkey` parameter must be sent with every request.

The debug endpoint expects traffic from localhost. A different debug IP address may be configured by setting the `TS_ALLOW_DEBUG_IP` environment variable before starting Headscale. The debug IP address is ignored when the HTTP header `X-Forwarded-For` is present.

    export TS_ALLOW_DEBUG_IP=192.168.0.10       # IP address of your device
    headscale serve

Access the debug interface on your device by opening `http://<IP_OF_HEADSCALE>:9090/debug/` in your web browser.