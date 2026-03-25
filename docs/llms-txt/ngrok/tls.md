# Source: https://ngrok.com/docs/universal-gateway/tls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TLS Agent Endpoints

> Learn how to create and configure TLS endpoints with ngrok for handling encrypted TLS traffic using SNI-based routing.

TLS endpoints enable you to deliver any network service that runs over a TLS-based protocol.
TLS endpoints make no assumptions about the wrapped protocol being transported.

TLS endpoints inspect the [Server Name Indication (SNI)](#sni)
data on incoming TLS connections to route connections to the appropriate
endpoint.

Because the TLS protocol describes no application-level semantics, ngrok can
only offer a [limited set of Traffic Policy actions](/traffic-policy/actions/)
to handle TLS traffic.

If you are delivering an HTTPS application, prefer to create an [HTTP
Endpoint](/universal-gateway/http/).

## Quickstart

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tls 80 \
      --url tls://your-name.ngrok.app \
      --traffic-policy-file traffic-policy.yml
    ```

    ##### `traffic-policy.yml`

    ```yaml  theme={null}
    on_tcp_connect:
      - actions:
          - type: terminate-tls
    ```
  </Tab>

  <Tab title="Agent Config">
    ```yaml  theme={null}
    version: 3
    endpoints:
      - name: example
        url: tls://your-name.ngrok.app
        upstream:
          url: 80
        traffic_policy:
          on_tcp_connect:
            - actions:
                - type: terminate-tls
    ```
  </Tab>

  <Tab title="SSH Reverse Tunnel">
    <Info>
      SSH does not support termination at the edge
    </Info>
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    import (
    	"context"
    	"net"

    	"golang.ngrok.com/ngrok/v2"
    )

    trafficPolicy := `
    on_tls_request:
      - actions:
          - type: terminate-tls
    `

    func ngrokListener(ctx context.Context) (net.Listener, error) {
    	return ngrok.Listen(ctx,
    		ngrok.WithURL("tls://your-name.ngrok.app"),
    		ngrok.WithTrafficPolicy(trafficPolicy),
    	)
    }
    ```

    * [https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithTrafficPolicy](https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithTrafficPolicy)
  </Tab>

  <Tab title="Javascript">
    ```jsx  theme={null}
    const ngrok = require("@ngrok/ngrok");
    const fs = require("fs");

    (async function () {
    	const listener = await ngrok.forward({
    		addr: 8080,
    		authtoken_from_env: true,
    		proto: "tls",
    		domain: "app.example.com",
    		crt: fs.readFileSync("/path/to/app-example-com-crt.pem", "utf8"),
    		key: fs.readFileSync("/path/to/app-example-com-key.pem", "utf8"),
    	});

    	console.log(`Ingress established at: ${listener.url()}`);
    })();
    ```

    Javascript SDK Docs:

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#domain](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#domain)

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#crt](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#crt)

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#key](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#key)

    * [https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#domain](https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#domain)

    * [https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#termination](https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#termination)
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import ngrok

    def load_file(name):
        with open(name, "r") as crt:
            return bytearray(crt.read().encode())

    listener = ngrok.forward("localhost:8080", authtoken_from_env=True,
        proto="tls",
        domain="app.example.com",
        crt=load_file("/path/to/app-example-com-crt.pem"),
        key=load_file("/path/to/app-example-com-key.pem"))

    print(f"Ingress established at: {listener.url()}");
    ```

    Python SDK Docs:

    * [https://ngrok.github.io/ngrok-python/tls\_listener\_builder.html#ngrok.TlsListenerBuilder.domain](https://ngrok.github.io/ngrok-python/tls_listener_builder.html#ngrok.TlsListenerBuilder.domain)
    * [https://ngrok.github.io/ngrok-python/tls\_listener\_builder.html#ngrok.TlsListenerBuilder.termination](https://ngrok.github.io/ngrok-python/tls_listener_builder.html#ngrok.TlsListenerBuilder.termination)
    * [https://ngrok.github.io/ngrok-python/index.html#full-configuration](https://ngrok.github.io/ngrok-python/index.html#full-configuration)
  </Tab>

  <Tab title="Rust">
    <Info>
      The Rust SDK does not support TLS termination at the ngrok edge
    </Info>
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TLS endpoints are not supported by the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

## URLs

URLs are validated differently depending on their
[binding](/universal-gateway/bindings). Consult the
following documentation for details on valid URLs for TLS endpoints:

* [Public Endpoint URLs](/universal-gateway/public-endpoints/#https-tls)
* [Internal Endpoint URLs](/universal-gateway/internal-endpoints/#urls)
* [Kubernetes Endpoint URLs](/universal-gateway/kubernetes-endpoints/#urls)

There is no standard scheme for TLS URLs so ngrok renders them as `tls://`.

## Bindings

TLS endpoints support `public` and `internal` bindings. `kubernetes` binding is
not supported.

## Traffic Policy

Attach [Traffic Policy](/traffic-policy/) to endpoints to route, authenticate
and transform the traffic through your TLS endpoints.

### Authentication

When you create public TLS endpoints, you often want to secure them with
authentication. You can secure your TLS endpoints with the following [Traffic
Policy](/traffic-policy/) actions. There is a limited set of actions available
to authenticate TLS traffic because the TLS protocol is low-level.

* [IP Restriction](/traffic-policy/actions/restrict-ips/)
* [Mutual TLS](/traffic-policy/actions/terminate-tls/)

## TLS

### Termination

TLS Endpoints provide you with the flexibility to define where TLS termination
occurs. You may configure your endpoint to terminate TLS at the ngrok cloud
service or you can achieve [end-to-end
encryption](/universal-gateway/tls-termination/#end-to-end-encryption)
by terminating at the agent or your upstream service. When you use end-to-end
encryption, the ngrok cloud service can not see payload that transit through
your endpoints.

Consult the documentation on [TLS Termination
Locations](/universal-gateway/tls-termination/#termination-location) for
additional details.

#### Cloud service

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tls 80 \
      --url tls://your-name.ngrok.app \
      --traffic-policy-file traffic-policy.yml
    ```

    ##### `traffic-policy.yml`

    ```yaml  theme={null}
    on_tcp_connect:
      - actions:
          - type: terminate-tls
    ```
  </Tab>

  <Tab title="Agent Config">
    ```yaml  theme={null}
    version: 3
    endpoints:
      - name: example
        url: tls://your-name.ngrok.app
        upstream:
          url: 80
        traffic_policy:
          on_tcp_connect:
            - actions:
                - type: terminate-tls
    ```
  </Tab>

  <Tab title="SSH Reverse Tunnel">
    <Info>
      SSH does not support termination at the edge
    </Info>
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    import (
    	"context"
    	"net"

    	"golang.ngrok.com/ngrok/v2"
    )

    trafficPolicy := `
    on_tls_request:
      - actions:
          - type: terminate-tls
    `

    func ngrokListener(ctx context.Context) (net.Listener, error) {
    	return ngrok.Listen(ctx,
    		ngrok.WithURL("tls://your-name.ngrok.app"),
    		ngrok.WithTrafficPolicy(trafficPolicy),
    	)
    }
    ```

    * [https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithTrafficPolicy](https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithTrafficPolicy)
  </Tab>

  <Tab title="Javascript">
    ```jsx  theme={null}
    const ngrok = require("@ngrok/ngrok");
    const fs = require("fs");

    (async function () {
    	const listener = await ngrok.forward({
    		addr: 8080,
    		authtoken_from_env: true,
    		proto: "tls",
    		domain: "app.example.com",
    		crt: fs.readFileSync("/path/to/app-example-com-crt.pem", "utf8"),
    		key: fs.readFileSync("/path/to/app-example-com-key.pem", "utf8"),
    	});

    	console.log(`Ingress established at: ${listener.url()}`);
    })();
    ```

    Javascript SDK Docs:

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#domain](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#domain)

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#crt](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#crt)

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#key](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#key)

    * [https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#domain](https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#domain)

    * [https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#termination](https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#termination)
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import ngrok

    def load_file(name):
        with open(name, "r") as crt:
            return bytearray(crt.read().encode())

    listener = ngrok.forward("localhost:8080", authtoken_from_env=True,
        proto="tls",
        domain="app.example.com",
        crt=load_file("/path/to/app-example-com-crt.pem"),
        key=load_file("/path/to/app-example-com-key.pem"))

    print(f"Ingress established at: {listener.url()}");
    ```

    Python SDK Docs:

    * [https://ngrok.github.io/ngrok-python/tls\_listener\_builder.html#ngrok.TlsListenerBuilder.domain](https://ngrok.github.io/ngrok-python/tls_listener_builder.html#ngrok.TlsListenerBuilder.domain)
    * [https://ngrok.github.io/ngrok-python/tls\_listener\_builder.html#ngrok.TlsListenerBuilder.termination](https://ngrok.github.io/ngrok-python/tls_listener_builder.html#ngrok.TlsListenerBuilder.termination)
    * [https://ngrok.github.io/ngrok-python/index.html#full-configuration](https://ngrok.github.io/ngrok-python/index.html#full-configuration)
  </Tab>

  <Tab title="Rust">
    <Info>
      The Rust SDK does not support TLS termination at the ngrok edge
    </Info>
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TLS endpoints are not supported by the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

<br />

#### Terminate at Agent

See [TLS Termination at the Agent for End-to-End Encryption](/universal-gateway/tls-termination#end-to-end-encryption) for additional details.

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tls 80 \
      --terminate-at agent \
      --url tls://app.example.com \
      --crt /path/to/app-example-com-crt.pem \
      --key /path/to/app-example-com-key.pem
    ```
  </Tab>

  <Tab title="Agent Config">
    ```yaml  theme={null}
    version: 3
    endpoints:
      - name: example
        url: tls://app.example.com"
        upstream:
          url: 80
        agent_tls_termination:
          server_certificate: "/path/to/app-example-com-crt.pem"
          server_private_key: "/path/to/app-example-com-crt.key"
    ```
  </Tab>

  <Tab title="SSH Reverse Tunnel">
    <Info>
      SSH does not support termination at the agent
    </Info>
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    import (
    	"context"
    	"crypto/tls"
    	"net"

    	"golang.ngrok.com/ngrok/v2"
    )

    func ngrokListener(ctx context.Context) (net.Listener, error) {
    	cert, err := tls.LoadX509KeyPair("/path/to/cert.pem", "/path/to/key.pem")
    	if err != nil {
    		return nil, err
    	}

    	tlsConfig := &tls.Config{
    		Certificates: []tls.Certificate{cert},
    	}

    	return ngrok.Listen(ctx,
    		ngrok.WithURL("tls://"),
    		ngrok.WithAgentTLSTermination(tlsConfig),
    	)
    }
    ```
  </Tab>

  <Tab title="Javascript">
    <Info>
      The Javascript SDK does not support TLS termination at the agent.
    </Info>
  </Tab>

  <Tab title="Python">
    <Info>
      The Python SDK does not support TLS termination at the agent.
    </Info>
  </Tab>

  <Tab title="Rust">
    <Info>
      The Rust SDK does not support TLS termination at the agent.
    </Info>
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TLS endpoints are not supported by the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

<br />

#### Terminate at Upstream

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tls 443 \
      --terminate-at upstream \
      --url tls://app.example.com
    ```
  </Tab>

  <Tab title="Agent Config">
    ```yaml  theme={null}
    version: 3
    endpoints:
      - name: example
        url: tls://app.example.com
        upstream:
          url: localhost:443
    ```
  </Tab>

  <Tab title="SSH Reverse Tunnel">
    ```bash  theme={null}
    ssh -R app.example.com:443:localhost:443 v2@connect.ngrok-agent.com tls
    ```
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    import (
    	"context"

    	"golang.ngrok.com/ngrok/v2"
    )

    func ngrokForwarder(ctx context.Context) (ngrok.EndpointForwarder, error) {
    	return ngrok.Forward(ctx,
    		ngrok.WithUpstream("tls://localhost:443"),
    		ngrok.WithURL("tls://app.example.com"),
    	)
    }
    ```
  </Tab>

  <Tab title="Javascript">
    ```jsx  theme={null}
    const ngrok = require("@ngrok/ngrok");

    (async function () {
    	const listener = await ngrok.forward({
    		addr: 8080,
    		authtoken_from_env: true,
    		proto: "tls",
    		domain: "app.example.com",
    	});

    	console.log(`Ingress established at: ${listener.url()}`);
    })();
    ```

    Javascript SDK Docs:

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#domain](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#domain)
    * [https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#domain](https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#domain)
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import ngrok

    listener = ngrok.forward("localhost:8080", authtoken_from_env=True,
        proto="tls",
        domain="app.example.com")

    print(f"Ingress established at: {listener.url()}");
    ```

    Python SDK Docs:

    * [https://ngrok.github.io/ngrok-python/tls\_listener\_builder.html#ngrok.TlsListenerBuilder.domain](https://ngrok.github.io/ngrok-python/tls_listener_builder.html#ngrok.TlsListenerBuilder.domain)
    * [https://ngrok.github.io/ngrok-python/index.html#full-configuration](https://ngrok.github.io/ngrok-python/index.html#full-configuration)
  </Tab>

  <Tab title="Rust">
    ```rust  theme={null}
    use ngrok::prelude::*;

    async fn listen_ngrok() -> anyhow::Result<impl Tunnel> {
        let sess = ngrok::Session::builder()
            .authtoken_from_env()
            .connect()
            .await?;

        let tun = sess
            .tls_endpoint()
            .domain("app.example.com")
            .listen()
            .await?;

        println!("Listening on URL: {:?}", tun.url());

        Ok(tun)
    }
    ```

    Rust Crate Docs:

    * [https://docs.rs/ngrok/latest/ngrok/config/struct.TlsTunnelBuilder.html#method.domain](https://docs.rs/ngrok/latest/ngrok/config/struct.TlsTunnelBuilder.html#method.domain)
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TLS endpoints are not supported by the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

### Certificates

It is very common to encounter certificate errors when working with TLS endpoints.
When terminating TLS at ngrok's cloud service, ngrok will automatically select, provision, and manage certs for you.
When performing [end-to-end encryption](/universal-gateway/tls-termination/#end-to-end-encryption) by terminating at the agent or upstream service, you become responsible for provisioning, managing, and distributing certificates.

Consult the documentation on [TLS
Certificates](/universal-gateway/tls-certificates/) for details about
certificate selection, provisioning and management.

## Agent forwarding

### Re-encrypt to upstream

If you terminate TLS at the ngrok cloud service or ngrok agent, you may want to
re-encrypt the connection from the agent to your upstream service. The ngrok
agent supports this behavior by using the non-standard `tls://` scheme syntax.

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tls tls://localhost:443 --terminate-at=edge
    ```
  </Tab>

  <Tab title="Agent Config">
    ```yaml  theme={null}
    version: 3
    endpoints:
      - name: example
        url: tls://example.ngrok.app
        upstream:
          url: tls://localhost:443
        traffic_policy:
          on_tcp_connect:
            - actions:
                - type: terminate-tls
    ```
  </Tab>

  <Tab title="SSH Reverse Tunnel">
    <Info>
      Re-encrypting the connection to your upstream service with TLS is not supported via SSH.
    </Info>
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    import (
    	"context"
    	"crypto/tls"

    	"golang.ngrok.com/ngrok/v2"
    )

    func ngrokListener(ctx context.Context) (ngrok.EndpointForwarder, error) {
    	// TLS config is optional - can be nil for default settings
    	tlsConfig := &tls.Config{
    		// Add your upstream TLS configuration here
    	}

    	return ngrok.Forward(ctx,
    		ngrok.WithUpstream("tls://localhost:8443",
    			ngrok.WithUpstreamTLSClientConfig(tlsConfig),
    		),
    	)
    }
    ```
  </Tab>

  <Tab title="Javascript">
    ```jsx  theme={null}
    const ngrok = require("@ngrok/ngrok");

    (async function () {
    	const listener = await ngrok.forward({
    		addr: "tls://localhost:443",
    		authtoken_from_env: true,
    		proto: "tls",
    		crt: "",
    		key: "",
    	});

    	console.log(`Ingress established at: ${listener.url()}`);
    })();
    ```

    An empty certificate and key will default to the ngrok edge's automatically provisioned keypair. The upstream certificate of `localhost:443` will be validated by a filepath specified in the `SSL_CERT_FILE` environment variable (for example, `SSL_CERT_FILE=/path/to/ca.crt`), or falling back to the host OS installed trusted certificate authorities.

    Javascript SDK Docs:

    * [https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html](https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html)
    * [https://ngrok.github.io/ngrok-javascript/classes/Session.html#tlsEndpoint](https://ngrok.github.io/ngrok-javascript/classes/Session.html#tlsEndpoint)
    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#addr](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#addr)
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import ngrok

    listener = ngrok.forward("tls://localhost:443", authtoken_from_env=True,
        proto="tls"
        crt=bytearray(),
        key=bytearray())

    print(f"Ingress established at: {listener.url()}");
    ```

    An empty certificate and key will default to the ngrok edge's automatically provisioned keypair. The upstream certificate of `localhost:443` will be validated by a filepath specified in the `SSL_CERT_FILE` environment variable (for example, `SSL_CERT_FILE=/path/to/ca.crt`), or falling back to the host OS installed trusted certificate authorities.

    Python SDK Docs:

    * [https://ngrok.github.io/ngrok-python/module.html#ngrok.connect](https://ngrok.github.io/ngrok-python/module.html#ngrok.connect)
    * [https://ngrok.github.io/ngrok-python/index.html#full-configuration](https://ngrok.github.io/ngrok-python/index.html#full-configuration)
  </Tab>

  <Tab title="Rust">
    <Info>
      Re-encrypting the connection to your upstream service with TLS is not yet supported in the Rust SDK.
    </Info>
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TLS endpoints are not supported by the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

### PROXY Protocol

Add a [PROXY
protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) header
on connection to your upstream service. This sends connection information like
the original client IP address to your upstream service.

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tls 443 --upstream-proxy-protocol=2
    ```
  </Tab>

  <Tab title="Agent Config">
    ```yaml  theme={null}
    version: 3
    endpoints:
      - name: example
        url: tls://example.ngrok.app
        upstream:
          url: 443
          proxy_protocol: 2
    ```
  </Tab>

  <Tab title="SSH Reverse Tunnel">
    <Info>
      PROXY proto is not support via SSH.
    </Info>
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    import (
    	"context"
    	"net"

    	"golang.ngrok.com/ngrok/v2"
    )

    func ngrokListener(ctx context.Context) (net.Listener, error) {
    	return ngrok.Forward(ctx,
    		ngrok.WithUpstream("tls://localhost:8443",
    			ngrok.WithUpstreamProxyProto(ngrok.ProxyProtoV2),
    		),
    		ngrok.WithURL("tls://"),
    	)
    }
    ```

    Go Package Docs:

    * [https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithUpstreamProxyProto](https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithUpstreamProxyProto)
  </Tab>

  <Tab title="Javascript">
    ```jsx  theme={null}
    const ngrok = require("@ngrok/ngrok");

    (async function () {
    	const listener = await ngrok.forward({
    		addr: 8080,
    		authtoken_from_env: true,
    		proto: "tls",
    		proxy_proto: "2",
    	});

    	console.log(`Ingress established at: ${listener.url()}`);
    })();
    ```

    Javascript SDK Docs:

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#proxy\_proto](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#proxy_proto)
    * [https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#proxyProto](https://ngrok.github.io/ngrok-javascript/classes/TlsListenerBuilder.html#proxyProto)
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import ngrok

    listener = ngrok.forward("localhost:8080", authtoken_from_env=True,
        proto="tls",
        proxy_proto="2")

    print(f"Ingress established at: {listener.url()}");
    ```

    Python SDK Docs:

    * [https://ngrok.github.io/ngrok-python/tls\_listener\_builder.html#ngrok.TlsListenerBuilder.proxy\_proto](https://ngrok.github.io/ngrok-python/tls_listener_builder.html#ngrok.TlsListenerBuilder.proxy_proto)
    * [https://ngrok.github.io/ngrok-python/index.html#full-configuration](https://ngrok.github.io/ngrok-python/index.html#full-configuration)
  </Tab>

  <Tab title="Rust">
    ```rust  theme={null}
    use ngrok::prelude::*;

    async fn listen_ngrok() -> anyhow::Result<impl Tunnel> {
        let sess = ngrok::Session::builder()
            .authtoken_from_env()
            .connect()
            .await?;

        let tun = sess
            .tls_endpoint()
            .proxy_proto(ProxyProto::V2)
            .listen()
            .await?;

        println!("Listening on URL: {:?}", tun.url());

        Ok(tun)
    }
    ```

    Rust Crate Docs:

    * [https://docs.rs/ngrok/latest/ngrok/config/struct.TlsTunnelBuilder.html#method.proxy\_proto](https://docs.rs/ngrok/latest/ngrok/config/struct.TlsTunnelBuilder.html#method.proxy_proto)
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TLS Endpoints are not supported via the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

## Compatible clients

### SNI

TLS endpoints only work with modern TLS clients that populate the SNI
extension. See the documentation on [TLS
Termination](/universal-gateway/tls-termination/#sni) for additional
details on compatible clients.

### STARTTLS

Protocols that begin in plain text and upgrade to TLS via a mechanism like
STARTTLS in SMTP, IMAP, etc are not supported. If you need to support
connections which upgrade to TLS, use a [TCP
Endpoint](/universal-gateway/tcp/).

## Observability

### Traffic Inspector

[Traffic Inspector](/obs/traffic-inspection) does not support TLS endpoints.

### Log exports

You can export logs of traffic to TLS endpoints with [ngrok's events
system](/obs/). The following events are published for log exporting:

| Log                                                                        | When                                                         |
| -------------------------------------------------------------------------- | ------------------------------------------------------------ |
| [tcp\_connection\_closed.v0](/obs/events/reference/#tcp-connection-closed) | Published when a TCP connection to a TCP endpoint completes. |

## Limits & timeouts

[Contact Support](mailto:support@ngrok.com) if you need to configure limits and
timeouts on connections to TLS endpoints.

### Connections

| Limit     | Name                | Notes                                                          |
| --------- | ------------------- | -------------------------------------------------------------- |
| 3 seconds | ClientHello Timeout | Time between connection establishment and ClientHello received |
| 5 minutes | Client Idle Timeout | Time since data was last transmitted by the upstream service   |
| 5 minutes | Server Idle Timeout | Time since data was last transmitted by the upstream service   |
| No limit  | Data transmitted    | Data transmitted by the client or upstream service             |

### TLS

| Limit      | Name                     | Notes                                                      |
| ---------- | ------------------------ | ---------------------------------------------------------- |
| 60 seconds | TLS Handshake Duration   | Time between ClientHello received and handshake completion |
| 64 KB      | Handshake Message Size   | Max size of non-certificate handshake messages             |
| 256 KB     | Certificate Message Size | Max size of certificate handshake messages                 |
| 16 KB      | Record Payload Size      |                                                            |

## Errors

If a TLS handshake fails, an appropriate TLS abort code will be sent to the
client.

In all other cases, if an error is encountered while handling TLS connections
to your endpoints (for example, no available backends or internal server error), the
connection will be closed. The TLS protocol and its implementations are not
sufficiently flexible enough to deliver additional rich error information when
failures are encountered.

Use the [observability](#observability) features to understand connection
handling errors.

## API

TLS Endpoints can be created programmatically. Consult the documentation on
\[Endpoint APIs]\(/api-reference/endpoints/list.

## Pricing

TLS endpoints are available on Hobbyist and Pay-as-you-go plans. Consult the [Endpoints
Pricing](/universal-gateway/endpoints/#pricing) documentation for
billing details.

See [Domains pricing](/universal-gateway/domains/#pricing) for details on
pricing for custom domains, wildcard endpoints and more.

Zero-knowledge TLS is available on the Pay-as-you-go plan.


Built with [Mintlify](https://mintlify.com).