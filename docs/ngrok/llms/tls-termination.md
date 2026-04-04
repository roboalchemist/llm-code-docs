# Source: https://ngrok.com/docs/universal-gateway/tls-termination.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TLS Termination

> Learn how ngrok automatically handles TLS termination for you, and enables you to manage it yourself.

ngrok automatically handles TLS (SSL) termination and certificate management
for you. There is typically nothing to set up, configure, or manage.

## Overview

ngrok's TLS termination behavior is determined by an endpoint's protocol and
Traffic Policy. You may customize each endpoint to choose where TLS is
terminated, how it is terminated and even whether it is terminated at all. When
ngrok's cloud service terminates TLS, it:

* Uses latest and most secure version of TLS
* Uses the [TLS
  Certificate](/universal-gateway/tls-certificates/) attached to the
  [Domain](/universal-gateway/domains/) which matches the Endpoint URL's
  hostname
* Accelerates your traffic by using the global load balancer to terminate at its
  closest point of presence

ngrok supports [end-to-end encryption](#end-to-end-encryption) where the ngrok
cloud service does not terminate TLS connections and only sees enciphered
traffic. When configured this way, you are responsible for configuring TLS
termination in your upstream service or at the ngrok agent.

## Termination location

TLS connections to your ngrok endpoints are terminated at one of three
locations.

* **ngrok's cloud service**: This is the easiest and most common. All HTTPS
  endpoints terminate TLS at ngrok's cloud service. When connections are
  terminated by ngrok's cloud service, they are re-encrypted before they are
  transmitted over a Secure Tunnel to an agent.
* **ngrok agent**: This is a form of [end-to-end
  encryption](#end-to-end-encryption) where the ngrok cloud service does not
  terminate TLS and you instead configure the ngrok agent to terminate TLS
  connections for you.
* **your upstream service**: This is another form of [end-to-end
  encryption](#end-to-end-encryption) where neither the cloud service nor an
  agent terminates TLS connections. Instead, your upstream application service is
  responsible for TLS termination.

An endpoint's protocol determines the ngrok cloud service's default TLS
termination behavior.

| Endpoint Protocol                 | TLS Termination                                           |
| --------------------------------- | --------------------------------------------------------- |
| [HTTP](/universal-gateway/http/)  | None                                                      |
| [HTTPS](/universal-gateway/http/) | Always at ngrok's cloud service.                          |
| [TLS](/universal-gateway/tls/)    | Default no termination, configurable with `terminate-tls` |
| [TCP](/universal-gateway/tcp/)    | Default no termination, configurable with `terminate-tls` |

### Examples

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

See [Zero-Knowledge TLS at the Agent](/agent/agent-tls-termination/) for additional details.

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

## `terminate-tls`

The [`terminate-tls` Traffic Policy
Action](/traffic-policy/actions/terminate-tls) enables you to terminate TLS
connections at ngrok's cloud service for TCP and TLS endpoints.

You may also use this action on HTTPS endpoints to customize how TLS is
terminated. When you use the `terminate-tls` action on an HTTPS endpoint, ngrok
will skip the default TLS termination step that it runs for all HTTPS endpoints
so as not to terminate TLS twice.

## Acceleration

The ngrok cloud service improves the performance of your endpoints by
accelerating TLS termination using ngrok's [global points
of presence](/universal-gateway/points-of-presence).

TLS connection set up requires multiple network round-trips. When round-trip
times (RTTs) are long, TLS connection establishment slows down. ngrok reduces
the latency of these round-trip times between the client and your endpoint by
terminating connections at the closest [point of
presence](/universal-gateway/points-of-presence/) via its [global load
balancer](/universal-gateway/global-load-balancer).

## Certificates

When the ngrok cloud service terminates TLS connections, it does so with the
[TLS Certificate](/universal-gateway/tls-certificates/) attached to the
[Domain](/universal-gateway/domains/) which matches the Endpoint URL's
hostname. See the documentation on [TLS
Certificates](/universal-gateway/tls-certificates/) for more details on
how they are
[selected](/universal-gateway/tls-certificates/#certificate-selection),
managed, provisioned and renewed.

You may customize which TLS certificate is chosen for termination with the
[`terminate-tls`](/traffic-policy/actions/terminate-tls) Traffic Policy action.

## Mutual TLS

Mutual TLS is supported when terminating TLS at ngrok's cloud service via the
`mutual_tls_certificate_authorities` field of the
[`terminate-tls`](/traffic-policy/actions/terminate-tls) Traffic Policy action.

Mutual TLS is supported when terminating TLS at the agent via the
`mutual_tls_certificate_authorities` property of the [`agent_tls_termination`
section of an endpoint
configuration](/agent/config/v3/#endpoint-configuration-options) in the agent
configuration file.

## Handshake

### TLS version

ngrok uses TLS 1.3 (the latest version) by default. If a client does not
support TLS 1.3, ngrok will use the highest possible version that the client
supports, down to TLS 1.2.

You may customize the minimum and maximum supported versions of TLS with the
[`terminate-tls`](/traffic-policy/actions/terminate-tls) Traffic Policy action.

### ALPN

`https` endpoints negotiate the next protocol via ALPN with the following
default list in order of preference:

```
["h2", "http/1.1"]
```

### SNI

ngrok endpoints do not support legacy clients which do not set the SNI
extension. For example, the following clients (and others) will fail to work
with ngrok endpoints:

* Microsoft Internet Explorer 6.0
* Microsoft Internet Explorer 7 & 8 on Windows XP or earlier
* Native browser on Android 2.X
* Java \<=1.6
* [Python 2.X, 3.0, 3.1 if required modules are not installed](https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484)

### Encrypted client hello

ngrok endpoints do not yet support the draft implementation of [Encrypted
Client Hello](https://datatracker.ietf.org/doc/draft-ietf-tls-esni/).

## FIPS compliance

ngrok does not use a FIPS-compliant TLS implementation by default, but one can
be enabled for your endpoints.

[Contact Support](mailto:support@ngrok.com) if you require a FIPS-compliant TLS
implementation.

## End-to-end encryption

You may choose to terminate TLS at your upstream service or at the ngrok agent
to achieve end-to-end encryption (E2EE), often referred to as Zero-knowledge TLS. When your endpoints operate in this
mode, the ngrok cloud service can not see the payloads that transfer through
your endpoints.

Creating an endpoint with end-to-end encryption is simple:

* Create a TLS or TCP endpoint
* **Do not** add a `terminate-tls` action to its Traffic Policy.

Read the [Agent TLS Termination Guide](/agent/agent-tls-termination/) for a step-by-step approach to set it up.

To set up the agent to terminate TLS for you, consult the following table
because the configuration depends on which kind of agent you are using.

| Agent               | Documentation                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| Agent Config File   | [`agent_tls_termination`](/agent/config/v3/#endpoint-configuration-options)                             |
| Go SDK              | [WithTLSTerminationKeyPair](https://pkg.go.dev/golang.ngrok.com/ngrok/config#WithTLSTerminationKeyPair) |
| Other SDKs          | not supported                                                                                           |
| Kubernetes Operator | not supported                                                                                           |

## Limits and timeouts

<TlsLimits />


Built with [Mintlify](https://mintlify.com).