# Source: https://ngrok.com/docs/universal-gateway/tcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TCP Agent Endpoints

> Learn how to create and configure TCP endpoints with ngrok for routing raw TCP traffic to your applications and services.

TCP endpoints enable you to deliver any network service with a TCP-based
protocol. They are commonly used to create connectivity for:

* Remote access protocols like SSH, VNC and RDP
* Databases like MySQL, Postgres, MSSQL and SQLite
* IoT protocols like MQTT
* Gaming servers like Minecraft

If you are accepting TLS traffic, you may prefer to create a [TLS Endpoint](/universal-gateway/tls/).

<Info title="Free Plan Usage">
  TCP endpoints are only available on a free plan after [adding a valid payment method](https://dashboard.ngrok.com/settings#id-verification) to your account.
</Info>

## Quickstart

Agent Endpoints are the easiest way to get started with ngrok. An [agent
endpoint](/universal-gateway/cloud-endpoints/) is started by a
[Secure Tunnels](/agent/) agent. The endpoint lives for the lifetime
of the process and forwards traffic to a port or URL of your choosing.

This example creates a TCP endpoint on a randomly assigned URL - for example,
`tcp://1.tcp.ngrok.io:12345` and forwards its traffic to a local port.

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tcp 22
    ```
  </Tab>

  <Tab title="Agent Config">
    <RandomAgentConfigExample />
  </Tab>

  <Tab title="SSH -R">
    ```bash  theme={null}
    ssh -R 0:localhost:22 v2@connect.ngrok-agent.com tcp
    ```

    <Tip>
      See [the guide on using ngrok with SSH](/using-ngrok-with/ssh) to use simple SSH instead of SSH -R.
    </Tip>
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    import (
    	"context"
    	"net"

    	"golang.ngrok.com/ngrok/v2"
    )

    func ngrokListener(ctx context.Context) (net.Listener, error) {
    	return ngrok.Listen(ctx,
    		ngrok.WithURL("tcp://"),
    	)
    }
    ```

    * [https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithURL](https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithURL)
  </Tab>

  <Tab title="Javascript">
    ```jsx  theme={null}
    const ngrok = require("@ngrok/ngrok");

    (async function () {
    	const listener = await ngrok.forward({
    		addr: 8080,
    		authtoken_from_env: true,
    		proto: "tcp",
    	});

    	console.log(`Ingress established at: ${listener.url()}`);
    })();
    ```

    Javascript SDK Docs

    * [https://ngrok.github.io/ngrok-javascript/classes/TcpListenerBuilder.html](https://ngrok.github.io/ngrok-javascript/classes/TcpListenerBuilder.html)
    * [https://ngrok.github.io/ngrok-javascript/classes/Session.html#tcpEndpoint](https://ngrok.github.io/ngrok-javascript/classes/Session.html#tcpEndpoint)
    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#proto](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#proto)
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import ngrok

    listener = ngrok.forward("localhost:8080", authtoken_from_env=True,
        proto="tcp")

    print(f"Ingress established at: {listener.url()}");
    ```

    Python SDK Docs:

    * [https://ngrok.github.io/ngrok-python/module.html#ngrok.connect](https://ngrok.github.io/ngrok-python/module.html#ngrok.connect)
    * [https://ngrok.github.io/ngrok-python/tcp\_listener\_builder.html#ngrok.TcpListenerBuilder.listen\_and\_forward](https://ngrok.github.io/ngrok-python/tcp_listener_builder.html#ngrok.TcpListenerBuilder.listen_and_forward)
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
            .tcp_endpoint()
            .listen()
            .await?;

        println!("Listening on URL: {:?}", tun.url());

        Ok(tun)
    }
    ```

    Rust Crate Docs

    * [https://docs.rs/ngrok/latest/ngrok/session/struct.Session.html#method.tcp\_endpoint](https://docs.rs/ngrok/latest/ngrok/session/struct.Session.html#method.tcp_endpoint)
    * [https://docs.rs/ngrok/latest/ngrok/config/struct.TcpTunnelBuilder.html](https://docs.rs/ngrok/latest/ngrok/config/struct.TcpTunnelBuilder.html)
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TCP Endpoints are not supported via the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

## URLs

URLs are validated differently depending on their
[binding](/universal-gateway/bindings). Consult the
following documentation for details on valid URLs for TCP endpoints:

* [Public Endpoint URLs](/universal-gateway/public-endpoints/#tcp)
* [Internal Endpoint URLs](/universal-gateway/internal-endpoints/#urls)
* [Kubernetes Endpoint URLs](/universal-gateway/kubernetes-endpoints/#urls)

There is no standard scheme for TCP URLs so ngrok renders them as `tcp://`.

### Static URLs

If you would like a public TCP endpoint to have a static URL, you must first
create a [TCP Address](/universal-gateway/tcp-addresses). When you create a TCP
address, a random hostname and port will be assigned to you, for example,
`1.tcp.ngrok.io:12345`.

A TCP address is only needed to make a public TCP endpoint have a static URL.
They are not needed for TCP endpoints on other bindings, like `internal` or
`kubernetes`.

After you have created a TCP Address, specify the address (for example,
`1.tcp.eu.ngrok.io:12345`) in the URL when you create the endpoint.

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tcp 3389 --url tcp://1.tcp.eu.ngrok.io:12345
    ```
  </Tab>

  <Tab title="Agent Config">
    <FixedAgentConfigExample />
  </Tab>

  <Tab title="SSH Reverse Tunnel">
    ```bash  theme={null}
    ssh -R 1.tcp.eu.ngrok.io:12345:localhost:3389 connect.eu.ngrok-agent.com tcp
    ```
  </Tab>

  <Tab title="Go">
    ```go  theme={null}
    import (
    	"context"
    	"net"

    	"golang.ngrok.com/ngrok/v2"
    )

    func ngrokListener(ctx context.Context) (net.Listener, error) {
    	return ngrok.Listen(ctx,
    		ngrok.WithURL("tcp://1.tcp.ngrok.io:12345"),
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
    		proto: "tcp",
    		remote_addr: "1.tcp.eu.ngrok.io:12345",
    	});

    	console.log(`Ingress established at: ${listener.url()}`);
    })();
    ```

    Javascript SDK Docs:

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#remote\_addr](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#remote_addr)
    * [https://ngrok.github.io/ngrok-javascript/classes/TcpListenerBuilder.html#remoteAddr](https://ngrok.github.io/ngrok-javascript/classes/TcpListenerBuilder.html#remoteAddr)
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import ngrok

    listener = ngrok.forward("localhost:8080", authtoken_from_env=True,
        proto="tcp",
        remote_addr="1.tcp.eu.ngrok.io:12345")

    print(f"Ingress established at: {listener.url()}");
    ```

    Python SDK Docs:

    * [https://ngrok.github.io/ngrok-python/tcp\_listener\_builder.html#ngrok.TcpListenerBuilder.remote\_addr](https://ngrok.github.io/ngrok-python/tcp_listener_builder.html#ngrok.TcpListenerBuilder.remote_addr)
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
            .tcp_endpoint()
            .remote_addr("1.tcp.eu.ngrok.io:12345")
            .listen()
            .await?;

        println!("Listening on URL: {:?}", tun.url());

        Ok(tun)
    }
    ```

    Rust Crate Docs:

    * [https://docs.rs/ngrok/latest/ngrok/config/struct.TcpTunnelBuilder.html#method.remote\_addr](https://docs.rs/ngrok/latest/ngrok/config/struct.TcpTunnelBuilder.html#method.remote_addr)
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TCP Endpoints are not supported via the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

### Custom domains

Public TCP endpoints are assigned randomly on an ngrok-controlled hostname with
a randomly assigned port. You may not choose the hostname and you may not
select the port.

You may, however, simulate a customized hostname by creating a CNAME record to
the hostname of your assigned TCP address. If you do so, be aware that all
ports on that hostname, even those provisioned to other accounts will then be
available on your domain.

For example if your TCP address is `5.tcp.ngrok.io:12345`, you could create the
following CNAME record:

```
CNAME tcp.mydomain.com -> 5.tcp.ngrok.io
```

And then you can access that TCP endpoint with

```
telnet tcp.mydomain.com 12345
```

## Traffic Policy

Attach [Traffic Policy](/traffic-policy/) to endpoints to route, authenticate
and transform the traffic through the endpoint.

### Authentication

When you create public TCP endpoints, you often want to secure them with
authentication. You can secure your TCP endpoints with the following [Traffic
Policy](/traffic-policy/) actions. There is a limited set of actions available
to authenticate TCP traffic because the TCP protocol is low-level.

* [IP Restriction](/traffic-policy/actions/restrict-ips/)
* [Mutual TLS](/traffic-policy/actions/terminate-tls/)

## Agent forwarding

The [ngrok agent](/agent/) and [Agent
SDKs](/agent-sdks/) forward traffic that your endpoints receive
to upstream services. You specify a URL or port number to instruct the ngrok
agent where and how to forward traffic.

### Forward to non-local service

Agents don't just forward to ports on your localhost. You can forward traffic
to any address or URL reachable from the agent. For example, if you want to
forward traffic to a Postgres server running on your network at
`192.168.1.2:5432`:

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tcp 192.168.1.2:5432
    ```
  </Tab>

  <Tab title="Agent Config">
    <NonLocalAgentConfigExample />
  </Tab>

  <Tab title="SSH Reverse Tunnel">
    ```bash  theme={null}
    ssh -R 0:192.168.1.2:5432 v2@connect.ngrok-agent.com tcp
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
    		ngrok.WithUpstream("tcp://192.168.1.2:3306"),
    		ngrok.WithURL("tcp://"),
    	)
    }
    ```

    * [https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithUpstream](https://pkg.go.dev/golang.ngrok.com/ngrok/v2#WithUpstream)
  </Tab>

  <Tab title="Javascript">
    ```jsx  theme={null}
    const ngrok = require("@ngrok/ngrok");

    (async function () {
    	const listener = await ngrok.forward({
    		addr: "192.168.1.2:5432",
    		authtoken_from_env: true,
    		proto: "tcp",
    	});

    	console.log(`Ingress established at: ${listener.url()}`);
    })();
    ```

    Javascript SDK Docs:

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#addr](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#addr)
    * [https://ngrok.github.io/ngrok-javascript/classes/TcpListenerBuilder.html#listenAndForward](https://ngrok.github.io/ngrok-javascript/classes/TcpListenerBuilder.html#listenAndForward)
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import ngrok

    listener = ngrok.forward("192.168.1.2:5432", authtoken_from_env=True,
        proto="tcp")

    print(f"Ingress established at: {listener.url()}");
    ```

    Python SDK Docs:

    * [https://ngrok.github.io/ngrok-python/module.html#ngrok.connect](https://ngrok.github.io/ngrok-python/module.html#ngrok.connect)
    * [https://ngrok.github.io/ngrok-python/tcp\_listener\_builder.html#ngrok.TcpListenerBuilder.listen\_and\_forward](https://ngrok.github.io/ngrok-python/tcp_listener_builder.html#ngrok.TcpListenerBuilder.listen_and_forward)
  </Tab>

  <Tab title="Rust">
    ```rust  theme={null}
    use ngrok::prelude::*;
    use ngrok::tunnel;
    use ngrok::forwarder::Forwarder;
    use url::Url;

    async fn forward_ngrok() -> Result<Forwarder<tunnel::TcpTunnel>, Error> {
        let sess = ngrok::Session::builder()
            .authtoken_from_env()
            .connect()
            .await?;
        sess
            .tcp_endpoint()
            .listen_and_forward(Url::parse("tcp://127.0.0.1:8090")?)
            .await
            .map_err(Into::into)
    }
    ```

    Rust Crate Docs:

    * [https://docs.rs/ngrok/0.14.0-pre.13/ngrok/config/struct.TcpTunnelBuilder.html#method.listen\_and\_forward](https://docs.rs/ngrok/0.14.0-pre.13/ngrok/config/struct.TcpTunnelBuilder.html#method.listen_and_forward)
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TCP Endpoints are not supported via the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

### PROXY Protocol

When you forward traffic to an upstream TCP service, because traffic is coming
from the ngrok agent, it won't know the client's original IP address. You can
add the [PROXY
protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) header
on connections to your upstream service to send connection information like the
original client IP address to your upstream service. You will need to configure
your upstream service to handle the PROXY protocol header.

<Tabs>
  <Tab title="Agent CLI">
    ```bash  theme={null}
    ngrok tcp 22 --upstream-proxy-protocol=2
    ```
  </Tab>

  <Tab title="Agent Config">
    ```yaml  theme={null}
    version: 3
    endpoints:
      - name: example
        url: tcp://1.tcp.ngrok.io:12345
        upstream:
          url: 22
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
    		ngrok.WithUpstream("tcp://localhost:8080",
    			ngrok.WithUpstreamProxyProto(ngrok.ProxyProtoV2),
    		),
    		ngrok.WithURL("tcp://"),
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
    		proto: "tcp",
    		proxy_proto: "2",
    	});

    	console.log(`Ingress established at: ${listener.url()}`);
    })();
    ```

    Javascript SDK Docs:

    * [https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#proxy\_proto](https://ngrok.github.io/ngrok-javascript/interfaces/Config.html#proxy_proto)
    * [https://ngrok.github.io/ngrok-javascript/classes/TcpListenerBuilder.html#proxyProto](https://ngrok.github.io/ngrok-javascript/classes/TcpListenerBuilder.html#proxyProto)
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    import ngrok

    listener = ngrok.forward("localhost:8080", authtoken_from_env=True,
        proto="tcp",
        proxy_proto="2")

    print(f"Ingress established at: {listener.url()}");
    ```

    Python SDK Docs:

    * [https://ngrok.github.io/ngrok-python/tcp\_listener\_builder.html#ngrok.TcpListenerBuilder.proxy\_proto](https://ngrok.github.io/ngrok-python/tcp_listener_builder.html#ngrok.TcpListenerBuilder.proxy_proto)
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
            .tcp_endpoint()
            .proxy_proto(ProxyProto::V2)
            .listen()
            .await?;

        println!("Listening on URL: {:?}", tun.url());

        Ok(tun)
    }
    ```

    Rust Crate Docs:

    * [https://docs.rs/ngrok/latest/ngrok/config/struct.TcpTunnelBuilder.html#method.proxy\_proto](https://docs.rs/ngrok/latest/ngrok/config/struct.TcpTunnelBuilder.html#method.proxy_proto)
  </Tab>

  <Tab title="Kubernetes Controller">
    <Info>
      TCP Endpoints are not supported via the ngrok Kubernetes Operator
    </Info>
  </Tab>
</Tabs>

## Observability

### Traffic Inspector

[Traffic Inspector](/obs/traffic-inspection) does not support TCP endpoints.

### Log exports

You can export logs of traffic to TCP endpoints with [ngrok's events
system](/obs/events/). The following events are published for log exporting:

| Log                                                                        | When                                                         |
| -------------------------------------------------------------------------- | ------------------------------------------------------------ |
| [tcp\_connection\_closed.v0](/obs/events/reference/#tcp-connection-closed) | Published when a TCP connection to a TCP endpoint completes. |

## Limits & timeouts

[Contact Support](mailto:support@ngrok.com) if you need to configure limits and timeouts on
connections to TCP endpoints.

| Limit     | Name                | Notes                                                        |
| --------- | ------------------- | ------------------------------------------------------------ |
| 5 minutes | Client Idle Timeout | Time since data was last transmitted by the upstream service |
| 5 minutes | Server Idle Timeout | Time since data was last transmitted by the upstream service |
| No limit  | Data transmitted    | Data transmitted by the client or upstream service           |

## Errors

If an error is encountered while handling connections to a TCP endpoint for any
reason (for example, Traffic Policy action error, internal server error), the
connection will be closed. Because of the low-level nature of the TCP protocol,
there is no mechanism used to transmit information about what error code was
encountered.

Use the [observability](#observability) features to understand connection
handling errors.

## API

TCP Endpoints can be created programmatically. Consult the documentation on
\[Endpoint APIs]\(/api-reference/endpoints/list.

## Pricing

TCP endpoints are available on all plans. Consult the [Endpoints
Pricing](/universal-gateway/endpoints/#pricing) documentation for
billing details.

TCP endpoints are only available on a free plan after [adding a valid payment
method](https://dashboard.ngrok.com/settings#id-verification) to your account.

See [TCP Addresses pricing](/universal-gateway/tcp-addresses/#pricing) for
details on pricing for fixed TCP Addresses.


Built with [Mintlify](https://mintlify.com).