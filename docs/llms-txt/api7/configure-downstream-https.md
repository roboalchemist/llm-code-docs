# Source: https://docs.api7.ai/ingress-controller/tls-and-mtls/configure-downstream-https.md

# Configure HTTPS Between Client and Gateway

This guide explains how to use the Ingress Controller to configure the gateway to accept HTTPS requests from clients.

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

Generate the certificate authority (CA) key and certificate:

```
openssl genrsa -out ca.key 2048 && \
  openssl req -new -sha256 -key ca.key -out ca.csr -subj "/CN=ROOTCA" && \
  openssl x509 -req -days 36500 -sha256 -extensions v3_ca -signkey ca.key -in ca.csr -out ca.crt
```

Generate the key and certificate with the common name `test.com` for the gateway, and sign with the CA certificate:

```
openssl genrsa -out server.key 2048 && \
  openssl req -new -sha256 -key server.key -out server.csr -subj "/CN=test.com" && \
  openssl x509 -req -days 36500 -sha256 -extensions v3_req \
  -CA ca.crt -CAkey ca.key -CAserial ca.srl -CAcreateserial \
  -in server.csr -out server.crt
```

## Configure Downstream HTTPS[â](#configure-downstream-https "Direct link to Configure Downstream HTTPS")

Create a Kubernetes TLS secret:

```
kubectl create secret tls test-tls-secret \
  --cert=server.crt \
  --key=server.key \
  --namespace=aic
```

* Gateway API
* APISIX CRD

Update your Gateway manifest file as such:

gateway.yaml

```
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  namespace: aic
  name: apisix
spec:
  gatewayClassName: apisix
  listeners:
    - name: http
      protocol: HTTP
      port: 80
    - name: https
      protocol: HTTPS
      port: 443
      hostname: test.com
      tls:
        certificateRefs:
          - kind: Secret
            group: ""
            name: test-tls-secret
  infrastructure:
    parametersRef:
      group: apisix.apache.org
      kind: GatewayProxy
      name: apisix-config
```

note

The `port` in the Gateway listener is required but ignored. This is due to limitations in the data plane: it cannot dynamically open new ports. Since the Ingress Controller does not manage the data plane deployment, it cannot automatically update the configuration or restart the data plane to apply port changes.

Apply the configuration to your cluster:

```
kubectl apply -f gateway.yaml
```

Create a Kubernetes manifest file for TLS configuration:

tls.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixTls
metadata:
  namespace: aic
  name: test-tls
spec:
  ingressClassName: apisix
  hosts:
    - test.com
  secret:
    name: test-tls-secret
    namespace: aic
```

Apply the configuration to your cluster:

```
kubectl apply -f tls.yaml
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create an example route that forwards all requests with the path `/ip` to the upstream service `httpbin.org`:

* Gateway API
* APISIX CRD

httpbin-route.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: quickstart-client-ip
spec:
  parentRefs:
  - name: apisix
  rules:
  - matches:
    - path:
        type: Exact
        value: /ip
    backendRefs:
    - name: httpbin-external-domain
      port: 80
```

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
  name: quickstart-client-ip
spec:
  ingressClassName: apisix
  http:
    - name: quickstart-client-ip
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

To verify HTTPS connectivity between the client and the gateway, first port-forward the gatewayâs SSL port to your local machine:

```
kubectl port-forward svc/<your-gateway-svc-name> 9443:443 &
```

Since the certificate is valid only for the CN `test.com`, you should use `test.com` as the gatewayâs domain name. Send a request to the route:

```
curl -ikv --resolve "test.com:9443:127.0.0.1" "https://test.com:9443/ip"
```

A TLS handshake process similar to the following verifies that TLS between client and gateway is enabled:

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
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=test.com
*  start date: Dec 31 07:47:54 2025 GMT
*  expire date: Dec 31 07:47:54 2125 GMT
*  issuer: CN=ROOTCA
*  SSL certificate verify result: unable to get local issuer certificate (20), continuing anyway.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x556274d632e0)
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
