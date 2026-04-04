# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/http3-quic.md

# Configure HTTP/3 QUIC Between Client and APISIX

[HTTP/3](https://en.wikipedia.org/wiki/HTTP/3) is the third major version of the Hypertext Transfer Protocol (HTTP). Unlike its predecessors which rely on TCP, HTTP/3 is based on [QUIC (Quick UDP Internet Connections) protocol](https://en.wikipedia.org/wiki/QUIC). It brings several benefits that collectively result in reduced latency and improved performance:

* enabling seamless transition between different network connections, such as switching from Wi-Fi to mobile data.
* eliminating head-of-line blocking, so that a lost packet does not block all streams.
* negotiating TLS versions at the same time as the TLS handshakes, allowing for faster connections.
* providing encryption by default, ensuring that all data transmitted over an HTTP/3 connection is protected and confidential.
* providing zero round-trip time (0-RTT) when communicating with servers that clients have already established connections to.

APISIX currently supports HTTP/3 connections between downstream clients and APISIX. HTTP/3 connections with upstream services are not yet supported.

caution

This feature is currently experimental and not recommended for production use.

This guide will show you how to configure APISIX to enable HTTP/3 connections between client and APISIX.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [static-curl](https://github.com/stunnel/static-curl) or other curl that has HTTP/3 support.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Enable HTTP/3 in APISIX[â](#enable-http3-in-apisix "Direct link to Enable HTTP/3 in APISIX")

Enable HTTP/3 on port `9443` by adding the following configurations to APISIX's `config.yaml` [configuration file](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample):

```
docker exec apisix-quickstart /bin/sh -c "echo '
apisix:
  enable_control: true
  control:
    ip: 0.0.0.0
    port: 9092
  ssl:
    listen:
      - port: 9443
        enable_http3: true
deployment:
  role: traditional
  role_traditional:
    config_provider: etcd
  admin:
    admin_key_required: false
    allow_admin:
      - 0.0.0.0/0
plugin_attr:
  prometheus:
    export_addr:
      ip: 0.0.0.0
      port: 9091
' > /usr/local/apisix/conf/config.yaml"
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for configuration changes to take effect:

```
docker exec apisix-quickstart apisix reload
```

## Generate Certificates and Keys[â](#generate-certificates-and-keys "Direct link to Generate Certificates and Keys")

HTTP/3 requires TLS. You can purchase the certificates or self-generate them, whichever is applicable.

To self-generate, first generate the certificate authority (CA) key and certificate:

```
openssl genrsa -out ca.key 2048 && \
  openssl req -new -sha256 -key ca.key -out ca.csr -subj "/CN=ROOTCA" && \
  openssl x509 -req -days 36500 -sha256 -extensions v3_ca -signkey ca.key -in ca.csr -out ca.crt
```

Next, generate the key and certificate with the common name `test.com` for APISIX, and sign with the CA certificate:

```
openssl genrsa -out server.key 2048 && \
  openssl req -new -sha256 -key server.key -out server.csr -subj "/CN=test.com" && \
  openssl x509 -req -days 36500 -sha256 -extensions v3_req \
  -CA ca.crt -CAkey ca.key -CAserial ca.srl -CAcreateserial \
  -in server.csr -out server.crt
```

## Configure HTTPS[â](#configure-https "Direct link to Configure HTTPS")

* Admin API

You can optionally load the content of `server.crt` and `server.key` into shell variables:

```
server_cert=$(cat server.crt)
server_key=$(cat server.key)
```

Create an SSL certificate object to save the server certificate and its key:

```
curl -i "http://127.0.0.1:9180/apisix/admin/ssls" -X PUT -d '
{
  "id": "quickstart-tls-client-ssl",
  "sni": "test.com",
  "cert": "'"${server_cert}"'",
  "key": "'"${server_key}"'"
}'
```

â¶ Configure the SNI to match the server certificate CN.

â· Configure the server certificate.

â¸ Configure the private key for the server certificate.

## Create a Route in APISIX[â](#create-a-route-in-apisix "Direct link to Create a Route in APISIX")

Create a sample route to `httpbin.org`:

* Admin API

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id":"httpbin-route",
  "uri":"/get",
  "upstream": {
    "type":"roundrobin",
    "nodes": {
      "httpbin.org:80": 1
    }
  }
}'
```

## Verify HTTP/3 Connections between Client and APISIX[â](#verify-http3-connections-between-client-and-apisix "Direct link to Verify HTTP/3 Connections between Client and APISIX")

Send a request to the route:

```
curl -kv --http3-only \
  -H "Host: test.com" \
  --resolve "test.com:9443:127.0.0.1" "https://test.com:9443/get"
```

You should receive an `HTTP/3 200` response similar to the following:

```
* Added test.com:9443:127.0.0.1 to DNS cache
* Hostname test.com was found in DNS cache
*   Trying 127.0.0.1:9443...
* QUIC cipher selection: TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_CCM_SHA256
* Skipped certificate verification
* Connected to test.com (127.0.0.1) port 9443
* using HTTP/3
* [HTTP/3] [0] OPENED stream for https://test.com:9443/get
* [HTTP/3] [0] [:method: GET]
* [HTTP/3] [0] [:scheme: https]
* [HTTP/3] [0] [:authority: test.com]
* [HTTP/3] [0] [:path: /get]
* [HTTP/3] [0] [user-agent: curl/8.7.1]
* [HTTP/3] [0] [accept: */*]
> GET /get HTTP/3
> Host: test.com
> User-Agent: curl/8.7.1
> Accept: */*
> 
* Request completely sent off
< HTTP/3 200 
...
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Content-Length": "0", 
    "Host": "test.com", 
    "User-Agent": "curl/8.7.1", 
    "X-Amzn-Trace-Id": "Root=1-6656013a-27da6b6a34d98e3e79baaf5b", 
    "X-Forwarded-Host": "test.com"
  }, 
  "origin": "172.19.0.1, 123.40.79.456", 
  "url": "http://test.com/get"
}
* Connection #0 to host test.com left intact
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have learned how to configure HTTP/3 between client and APISIX. HTTP/3 connections with upstream services are not yet supported and any contribution is welcome.
