# Source: https://docs.api7.ai/ingress-controller/proxy-tcp-traffic-over-tls.md

# Proxy TCP Traffic over TLS by SNI

This guide will show you how to configure the gateway to route TLS-encrypted TCP traffic based on the Server Name Indication (SNI) using the Ingress Controller.

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

## Start an Example Upstream Service[â](#start-an-example-upstream-service "Direct link to Start an Example Upstream Service")

Create a Kubernetes manifest file for a TCP echo upstream service:

echo-tcp.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: aic
  name: echo-tcp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: echo-tcp
  template:
    metadata:
      labels:
        app: echo-tcp
    spec:
      containers:
      - name: echo-tcp
        image: alpine:3.20
        command:
          - sh
          - -c
          - |
            apk add --no-cache socat &&
            socat TCP-LISTEN:8443,reuseaddr,fork EXEC:"cat"
        ports:
        - containerPort: 8443
---
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: echo-tcp
spec:
  selector:
    app: echo-tcp
  ports:
    - name: tcp
      port: 8443
      targetPort: 8443
```

Apply the configuration to your cluster:

```
kubectl apply -f echo-tcp.yaml
```

## Enable Gateway Stream Proxy[â](#enable-gateway-stream-proxy "Direct link to Enable Gateway Stream Proxy")

Upgrade your gateway to enable stream mode and set TCP port `9100`:

* APISIX Gateway
* API7 Gateway

```
helm upgrade -n aic apisix apisix/apisix \
  --set ... \ # add other parameters
  --set "service.stream.enabled=true" \
  --set "service.stream.tcp[0].addr=9100" \
  --set "service.stream.tcp[0].tls=true"
```

```
helm upgrade -n aic api7-ee-3-gateway api7/gateway \
  --set ... \ # add other parameters
  --set "gateway.stream.enabled=true" \
  --set "gateway.stream.only=false" \
  --set "gateway.stream.tcp[0].addr=9100" \
  --set "gateway.stream.tcp[0].tls=true"
```

## Generate Certificate and Key[â](#generate-certificate-and-key "Direct link to Generate Certificate and Key")

Generate the certificate authority (CA) key and certificate:

```
openssl genrsa -out ca.key 2048 && \
  openssl req -new -sha256 -key ca.key -out ca.csr -subj "/CN=ROOTCA" && \
  openssl x509 -req -days 36500 -sha256 -extensions v3_ca -signkey ca.key -in ca.csr -out ca.crt
```

Generate the key and certificate with the common name `test.com`, and sign with the CA certificate:

```
openssl genrsa -out server.key 2048 && \
  openssl req -new -sha256 -key server.key -out server.csr -subj "/CN=test.com" && \
  openssl x509 -req -days 36500 -sha256 -extensions v3_req \
  -CA ca.crt -CAkey ca.key -CAserial ca.srl -CAcreateserial \
  -in server.csr -out server.crt
```

Create a Kubernetes TLS secret:

```
kubectl create secret tls test-tls-secret \
  --cert=server.crt \
  --key=server.key \
  --namespace=aic
```

## Configure Gateway TLS[â](#configure-gateway-tls "Direct link to Configure Gateway TLS")

* Gateway API
* APISIX CRD

Update your Gateway manifest file to add a TLS listener:

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
    - name: tcptls
      protocol: TLS
      port: 9100
      hostname: test.com
      tls:
        # TLS termination only. Passthrough is not supported.
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

Note that the `port` in the Gateway listener is required but ignored. This is due to limitations in the data plane: it cannot dynamically open new ports. Since the Ingress Controller does not manage the data plane deployment, it cannot automatically update the configuration or restart the data plane to apply port changes.

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

* Gateway API
* APISIX CRD

Create a Kubernetes manifest that defines a TLSRoute:

tls-tcp-route.yaml

```
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: TLSRoute
metadata:
  namespace: aic
  name: tls-route
spec:
  parentRefs:
  - name: apisix
  hostnames: ["test.com"]
  rules:
  - backendRefs:
    - name: echo-tcp
      port: 8443
```

about hostname

The hostname configuration appears in both the Gateway listener and the TLSRoute because each serves a distinct purpose:

* Gateway listener `hostname`: specifies which hostnames the gateway will accept on this listener.
* TLSRoute `hostnames`: defines the hostnames to which the route applies, effectively filtering traffic received by the listener.

The `hostnames` in the TLSRoute is required and represents a subset of the listener hostnames. This explicit declaration ensures precise routing.

Create a Kubernetes manifest that defines a TCP stream route:

tls-tcp-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: tls-stream-route
  namespace: aic
spec:
  ingressClassName: apisix
  stream:
    - name: tls-stream-route
      protocol: TCP
      match:
        ingressPort: 9100
      backend:
        serviceName: echo-tcp
        servicePort: 8443
```

Apply the configuration to your cluster:

```
kubectl apply -f tls-tcp-route.yaml
```

## Verify[â](#verify "Direct link to Verify")

Expose the gatewayâs TCP TLS service port to your local machine:

```
# replace with your gatewayâs service name
kubectl port-forward svc/<gateway-service-name> 9100:9100 &
```

To test that TLS-encrypted TCP traffic is routed correctly by the gateway using the SNI `test.com`, run:

```
openssl s_client -connect 127.0.0.1:9100 -servername test.com
```

After the TLS handshake completes, you can type any text and press Enter. The upstream echo server will echo it back, confirming that the gateway correctly terminated TLS and forwarded the plain TCP payload to the upstream:

```
...
subject=CN=test.com
issuer=CN=ROOTCA
...
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Protocol: TLSv1.3
Server public key is 2048 bit
...
---
read R BLOCK

hello world
hello world
```

To verify the behavior when the SNI does not correspond to any configured route, run:

```
openssl s_client -connect 127.0.0.1:9100 -servername random.com
```

The connection will be terminated as the gateway cannot identify a matching stream route.
