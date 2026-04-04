# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/tls-and-mtls/configure-mtls-between-client-and-apisix.md

# Configure mTLS Between Client and APISIX

*Mutual TLS (mTLS)* is a two-way TLS where the client and the server authenticate each other. It is typically implemented to prevent unauthorized access and harden security.

This guide will show you how to configure mTLS between downstream client applications and APISIX.

<br />

![mTLS between Client and APISIX](https://static.api7.ai/uploads/2023/05/24/ESNFa0Qi_mtls-client-apisix.jpg)

<br />

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route that forwards all requests to `/ip` to the upstream `httpbin.org`:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "quickstart-ip",
  "uri": "/ip",
  "upstream": {
    "nodes": {
      "httpbin.org:80":1
    },
    "type": "roundrobin"
  }
}'
```

## Generate Certificates and Keys[â](#generate-certificates-and-keys "Direct link to Generate Certificates and Keys")

Generate the Certificate Authority (CA) key and certificate:

```
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 36500 -sha256 \
  -key ca.key \
  -out ca.crt \
  -subj "/CN=MyTestCA" \
  -extensions v3_ca \
  -config <(printf "[req]\ndistinguished_name=req\n[ v3_ca ]\nbasicConstraints=critical,CA:TRUE\nkeyUsage=critical,keyCertSign,cRLSign\nsubjectKeyIdentifier=hash\nauthorityKeyIdentifier=keyid:always,issuer")
```

Generate the key and certificate signing request (CSR):

```
openssl genrsa -out server.key 2048
openssl req -new -sha256 \
  -key server.key \
  -out server.csr \
  -subj "/CN=test.com"
```

Sign the server CSR with the CA certificate to generate the server certificate:

```
openssl x509 -req -days 36500 -sha256 \
  -in server.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out server.crt \
  -extensions v3_req \
  -extfile <(printf "[v3_req]\nbasicConstraints=CA:FALSE\nkeyUsage=digitalSignature,keyEncipherment\nextendedKeyUsage=serverAuth")
```

Generate the key and certificate signing request (CSR) for the client:

```
openssl genrsa -out client.key 2048
openssl req -new -sha256 \
  -key client.key \
  -out client.csr \
  -subj "/CN=CLIENT"
```

Sign the client CSR with the CA certificate to generate the client certificate:

```
openssl x509 -req -days 36500 -sha256 \
  -in client.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out client.crt \
  -extensions v3_req \
  -extfile <(printf "[v3_req]\nbasicConstraints=CA:FALSE\nkeyUsage=digitalSignature,keyEncipherment\nextendedKeyUsage=clientAuth")
```

## Configure mTLS for APISIX[â](#configure-mtls-for-apisix "Direct link to Configure mTLS for APISIX")

You can optionally load the content of `server.crt`, `server.key`, and `ca.crt` into environment variables:

```
export server_cert=$(cat server.crt)
export server_key=$(cat server.key)
export ca_cert=$(cat ca.crt)
```

* Admin API
* ADC

Create an SSL certificate object to save the server certificate, server certificate key, and CA certificate:

```
curl -i "http://127.0.0.1:9180/apisix/admin/ssls" -X PUT -d '
{
  "id": "quickstart-mtls-client-ssl",
  "sni": "test.com",
  "cert": "'"${server_cert}"'",
  "key": "'"${server_key}"'",
  "client": {
    "ca": "'"${ca_cert}"'"
  }
}'
```

â¶ `sni`: `test.com`, the same as server certificate CN value

â· `cert`: server certificate `server.crt`

â¸ `key`: server certificate key `server.key`

â¹ `client.ca`: CA certificate `ca.crt`

## Verify mTLS between Client and APISIX[â](#verify-mtls-between-client-and-apisix "Direct link to Verify mTLS between Client and APISIX")

### With Client Certificate[â](#with-client-certificate "Direct link to With Client Certificate")

As the certificate is only valid for the CN `test.com`, you should use `test.com` as the domain name where APISIX is hosted.

Send a request to `https://test.com:9443/ip` with client certificate and resolve `test.com` to `127.0.0.1`:

```
curl -ikv --resolve "test.com:9443:127.0.0.1" "https://test.com:9443/ip" \
  --cert client.crt --key client.key
```

An mTLS handshake similar to the following verifies the mTLS between client and APISIX is enabled:

```
* Added test.com:9443:127.0.0.1 to DNS cache
* Hostname test.com was found in DNS cache
*   Trying 127.0.0.1:9443...
* Connected to test.com (127.0.0.1) port 9443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Request CERT (13):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Certificate (11):
* TLSv1.3 (OUT), TLS handshake, CERT verify (15):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=test.com
*  start date: Apr 21 07:47:54 2023 GMT
*  expire date: Mar 28 07:47:54 2123 GMT
*  issuer: CN=ROOTCA
*  SSL certificate verify result: unable to get local issuer certificate (20), continuing anyway.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x5625339a72e0)
> GET /ip HTTP/2
> Host: test.com:9443
> user-agent: curl/7.74.0
> accept: */*
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
< HTTP/2 200 
HTTP/2 200 
...
```

Note that APISIX and the client successfully verified each other's certificate during the handshake and established a connection.

### Without Client Certificate[â](#without-client-certificate "Direct link to Without Client Certificate")

Send a request to `https://test.com:9443/ip` but without client certificate:

```
curl -ikv --resolve "test.com:9443:127.0.0.1" "https://test.com:9443/ip"
```

A failed mTLS handshake is similar to the following:

```
* Added test.com:9443:127.0.0.1 to DNS cache
* Hostname test.com was found in DNS cache
*   Trying 127.0.0.1:9443...
* Connected to test.com (127.0.0.1) port 9443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Request CERT (13):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Certificate (11):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=test.com
*  start date: Apr 21 07:47:54 2023 GMT
*  expire date: Mar 28 07:47:54 2123 GMT
*  issuer: CN=ROOTCA
*  SSL certificate verify result: unable to get local issuer certificate (20), continuing anyway.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x55f791e252e0)
> GET /ip HTTP/2
> Host: test.com:9443
> user-agent: curl/7.74.0
> accept: */*
> 
* TLSv1.3 (IN), TLS alert, unknown (628):
* OpenSSL SSL_read: error:1409445C:SSL routines:ssl3_read_bytes:tlsv13 alert certificate required, errno 0
* Failed receiving HTTP2 data
* OpenSSL SSL_write: SSL_ERROR_ZERO_RETURN, errno 0
* Failed sending HTTP2 data
* Connection #0 to host test.com left intact
```

The handshake failed due to the lack of client certificate.

## Next Steps[â](#next-steps "Direct link to Next Steps")

You can learn more about mTLS and APISIX SSL object in [SSL Certificates](https://docs.api7.ai/apisix/key-concepts/ssl-certificates.md).

APISIX also supports TLS connection between clients and APISIX. See [Configure HTTPS between client and APISIX](https://docs.api7.ai/apisix/how-to-guide/traffic-management/tls-and-mtls/configure-https-between-client-and-apisix.md) for more details.
