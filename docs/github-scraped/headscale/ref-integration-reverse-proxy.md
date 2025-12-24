# Source: https://headscale.net/stable/ref/integration/reverse-proxy/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/ref/integration/reverse-proxy.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/ref/integration/reverse-proxy.md "View source of this page")

# Running headscale behind a reverse proxy[¶](#running-headscale-behind-a-reverse-proxy "Permanent link")

Community documentation

This page is not actively maintained by the headscale authors and is written by community members. It is *not* verified by headscale developers.

**It might be outdated and it might miss necessary steps**.

Running headscale behind a reverse proxy is useful when running multiple applications on the same server, and you want to reuse the same external IP and port - usually tcp/443 for HTTPS.

### WebSockets[¶](#websockets "Permanent link")

The reverse proxy MUST be configured to support WebSockets to communicate with Tailscale clients.

WebSockets support is also required when using the Headscale [embedded DERP server](../../derp/). In this case, you will also need to expose the UDP port used for STUN (by default, udp/3478). Please check our [config-example.yaml](https://github.com/juanfont/headscale/blob/main/config-example.yaml).

### Cloudflare[¶](#cloudflare "Permanent link")

Running headscale behind a cloudflare proxy or cloudflare tunnel is not supported and will not work as Cloudflare does not support WebSocket POSTs as required by the Tailscale protocol. See [this issue](https://github.com/juanfont/headscale/issues/1468)

### TLS[¶](#tls "Permanent link")

Headscale can be configured not to use TLS, leaving it to the reverse proxy to handle. Add the following configuration values to your headscale config file.

[config.yaml]

    server_url: https://<YOUR_SERVER_NAME> # This should be the FQDN at which headscale will be served
    listen_addr: 0.0.0.0:8080
    metrics_listen_addr: 0.0.0.0:9090
    tls_cert_path: ""
    tls_key_path: ""

## nginx[¶](#nginx "Permanent link")

The following example configuration can be used in your nginx setup, substituting values as necessary. `<IP:PORT>` should be the IP address and port where headscale is running. In most cases, this will be `http://localhost:8080`.

[nginx.conf]

    map $http_upgrade $connection_upgrade 

    server 
    }

## istio/envoy[¶](#istioenvoy "Permanent link")

If you using [Istio](https://istio.io/) ingressgateway or [Envoy](https://www.envoyproxy.io/) as reverse proxy, there are some tips for you. If not set, you may see some debug log in proxy as below:

    Sending local reply with details upgrade_failed

### Envoy[¶](#envoy "Permanent link")

You need to add a new upgrade_type named `tailscale-control-protocol`. [see details](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-upgradeconfig)

### Istio[¶](#istio "Permanent link")

Same as envoy, we can use `EnvoyFilter` to add upgrade_type.

    apiVersion: networking.istio.io/v1alpha3
    kind: EnvoyFilter
    metadata:
      name: headscale-behind-istio-ingress
      namespace: istio-system
    spec:
      configPatches:
        - applyTo: NETWORK_FILTER
          match:
            listener:
              filterChain:
                filter:
                  name: envoy.filters.network.http_connection_manager
          patch:
            operation: MERGE
            value:
              typed_config:
                "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
                upgrade_configs:
                  - upgrade_type: tailscale-control-protocol

## Caddy[¶](#caddy "Permanent link")

The following Caddyfile is all that is necessary to use Caddy as a reverse proxy for headscale, in combination with the `config.yaml` specifications above to disable headscale\'s built in TLS. Replace values as necessary - `<YOUR_SERVER_NAME>` should be the FQDN at which headscale will be served, and `<IP:PORT>` should be the IP address and port where headscale is running. In most cases, this will be `localhost:8080`.

[Caddyfile]

    <YOUR_SERVER_NAME> 

Caddy v2 will [automatically](https://caddyserver.com/docs/automatic-https) provision a certificate for your domain/subdomain, force HTTPS, and proxy websockets - no further configuration is necessary.

For a slightly more complex configuration which utilizes Docker containers to manage Caddy, headscale, and Headscale-UI, [Guru Computing\'s guide](https://blog.gurucomputing.com.au/smart-vpns-with-headscale/) is an excellent reference.

## Apache[¶](#apache "Permanent link")

The following minimal Apache config will proxy traffic to the headscale instance on `<IP:PORT>`. Note that `upgrade=any` is required as a parameter for `ProxyPass` so that WebSockets traffic whose `Upgrade` header value is not equal to `WebSocket` (i. e. Tailscale Control Protocol) is forwarded correctly. See the [Apache docs](https://httpd.apache.org/docs/2.4/mod/mod_proxy_wstunnel.html) for more information on this.

[apache.conf]

    <VirtualHost *:443>
        ServerName <YOUR_SERVER_NAME>

        ProxyPreserveHost On
        ProxyPass / http://<IP:PORT>/ upgrade=any

        SSLEngine On
        SSLCertificateFile <PATH_TO_CERT>
        SSLCertificateKeyFile <PATH_CERT_KEY>
    </VirtualHost>