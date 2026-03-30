# Source: https://docs.api7.ai/ingress-controller/tls-and-mtls/configure-downstream-mtls.md

# Configure mTLS Between Client and Gateway

Mutual TLS (mTLS) is a two-way TLS protocol in which both the client and the server authenticate each other. It is commonly used to prevent unauthorized access and enhance security.

This guide explains how to use the Ingress Controller to configure the gateway to require mutual TLS (mTLS) from clients.

<!-- -->

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Enable SSL on the Gateway[â](#enable-ssl-on-the-gateway "Direct link to Enable SSL on the Gateway")

Ensure that your gateway has enabled SSL.

* APISIX Gateway
* API7 Gateway

```
helm upgrade apisix apisix/apisix \
  --set ... \ # add other parameters
  --set "apisix.ssl.enabled=true" \
  --set "apisix.ssl.containerPort=9443"
```

By default, API7 Gateway enables [SSL on container port `9443` and service port `443`](https://github.com/api7/api7-helm-chart/blob/main/charts/gateway/values.yaml#L317-L322), so no additional configuration is required for this step.

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

## Configure mTLS for the Gateway[â](#configure-mtls-for-the-gateway "Direct link to Configure mTLS for the Gateway")

* Gateway API
* APISIX CRD

The Ingress Controller currently does not support the configuration of mTLS between client and gateway using Gateway API.

Create two Kubernetes secrets:

```
kubectl create secret tls test-mtls-secret \
  --cert=server.crt \
  --key=server.key \
  --namespace=aic

kubectl create secret generic test-ca-secret \
  --from-file=cert=ca.crt \
  --namespace=aic
```

Create a Kubernetes manifest file for mTLS configuration:

mtls.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixTls
metadata:
  namespace: aic
  name: test-mtls
spec:
  ingressClassName: apisix
  hosts:
    - test.com
  secret:
    name: test-mtls-secret
    namespace: aic
  client:
    caSecret:
      name: test-ca-secret
      namespace: aic
    depth: 1
```

Apply the configuration to your cluster:

```
kubectl apply -f mtls.yaml
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

* Gateway API
* APISIX CRD

The Ingress Controller currently does not support the configuration of mTLS between client and gateway using Gateway API.

Create an example route that forwards all requests with the path `/ip` to the upstream service `httpbin.org`:

httpbin-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: httpbin-ip
spec:
  ingressClassName: apisix
  http:
    - name: httpbin-ip
      match:
        paths:
          - /ip
      upstreams:
      - name: httpbin-external-domain
```

Apply the configuration to your cluster:

```
kubectl apply -f httpbin-route.yaml
```

## Verify[â](#verify "Direct link to Verify")

To verify mTLS between the client and the gateway, first port-forward the gatewayâs SSL port to your local machine:

```
kubectl port-forward svc/<your-gateway-svc-name> 9443:443 &
```

### With Client Certificate[â](#with-client-certificate "Direct link to With Client Certificate")

Since the certificate is valid only for the CN `test.com`, you should use `test.com` as the gatewayâs domain name. Send a request to the route with the client certificate:

```
curl -ikv --resolve "test.com:9443:127.0.0.1" "https://test.com:9443/ip" \
  --cert client.crt --key client.key
```

An mTLS handshake similar to the following verifies the mTLS between the client and the gateway is enabled:

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
...
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
< HTTP/2 200 
HTTP/2 200 
...
```

Note that the gateway and the client successfully verified each other's certificate during the handshake and established a connection.

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
...
* TLSv1.3 (IN), TLS alert, unknown (628):
* OpenSSL SSL_read: error:1409445C:SSL routines:ssl3_read_bytes:tlsv13 alert certificate required, errno 0
* Failed receiving HTTP2 data
* OpenSSL SSL_write: SSL_ERROR_ZERO_RETURN, errno 0
* Failed sending HTTP2 data
* Connection #0 to host test.com left intact
```

The handshake failed due to the lack of client certificate.
