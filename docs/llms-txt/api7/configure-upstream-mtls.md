# Source: https://docs.api7.ai/ingress-controller/tls-and-mtls/configure-upstream-mtls.md

# Configure mTLS Between Gateway and Upstream

Mutual TLS (mTLS) is a two-way TLS protocol in which both the client and the server authenticate each other. It is commonly used to prevent unauthorized access and enhance security.

This guide explains how to use the Ingress Controller to configure the gateway to communicate with upstream services over mutual TLS (mTLS).

<!-- -->

## Prerequisite[â](#prerequisite "Direct link to Prerequisite")

1. Complete [Set Up Ingress Controller and Gateway](https://docs.api7.ai/ingress-controller/set-up-ingress-controller-and-gateway.md).

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

## Configure Upstream Service[â](#configure-upstream-service "Direct link to Configure Upstream Service")

This guide uses NGINX as the example upstream service to demonstrate mutual TLS (mTLS).

Create a Kubernetes secret for NGINX:

```
kubectl create secret generic nginx-certs \
  --from-file=server.crt=server.crt \
  --from-file=server.key=server.key \
  --from-file=ca.crt=ca.crt \
  --namespace=aic
```

Create a ConfigMap for NGINX, in which TLS certificates are configured:

nginx-cm.yaml

```
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: aic
  name: nginx-config
data:
  default.conf: |
    server {
        listen 8443 ssl;
        server_name test.com;
        ssl_certificate        /etc/nginx/ssl/server.crt;
        ssl_certificate_key    /etc/nginx/ssl/server.key;
        ssl_client_certificate /etc/nginx/ssl/ca.crt;
        ssl_verify_client on;
        location /hello {
            return 200 "Hello World!";
        }
    }
```

â¶ `server_name`: set to `test.com` to be consistent with the server certificate CN value.

â· `ssl_certificate`: configure the path to the server certificate public key `server.crt`.

â¸ `ssl_certificate_key`: configure the path to the server certificate private key `server.key`.

â¹ `ssl_client_certificate`: configure the path to the CA certificate public key `ca.crt`.

âº `ssl_verify_client`: set to `on` to verify the client certificate.

Create a Kubernetes manifest file for the NGINX example upstream service deployment and service:

nginx.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: quickstart-nginx
spec:
  type: NodePort
  selector:
    app: quickstart-nginx
  ports:
    - name: https
      port: 8443
      targetPort: 8443
---
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: aic
  name: quickstart-nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: quickstart-nginx
  template:
    metadata:
      labels:
        app: quickstart-nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 8443
          volumeMounts:
            - name: config
              mountPath: /etc/nginx/conf.d
            - name: certs
              mountPath: /etc/nginx/ssl
      volumes:
        - name: config
          configMap:
            name: nginx-config
        - name: certs
          secret:
            secretName: nginx-certs
```

Apply the configuration to your cluster:

```
kubectl apply -f nginx-cm.yaml -f nginx.yaml
```

To verify that the NGINX instance is properly configured, port-forward the NGINX service port to your local machine's port:

```
kubectl port-forward service/quickstart-nginx 8443:8443 &
```

Send a request to the Nginx service's route with client certificate and key:

```
curl -ik "https://127.0.0.1:8443/hello" --cert client.crt --key client.key
```

You should receive an `HTTP/1.1 200 OK` response and see the following message:

```
Hello World!
```

If you send a request without any client certificate or key:

```
curl -ik "https://127.0.0.1:8443/hello"
```

You should receive an `HTTP/1.1 400 Bad Request` response.

## Configure mTLS on the Gateway[â](#configure-mtls-on-the-gateway "Direct link to Configure mTLS on the Gateway")

* Gateway API
* APISIX CRD

The Ingress Controller currently does not support the configuration of upstream mTLS using Gateway API.

Create a Kubernetes secret:

```
kubectl create secret tls test-mtls-secret \
  --cert=client.crt \
  --key=client.key \
  --namespace=aic
```

Create a Kubernetes manifest file for a route to the NGINX service:

upstream-mtls-route.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: quickstart-nginx  # should match the service name
spec:
  ingressClassName: apisix
  scheme: https
  tlsSecret:
    name: test-mtls-secret
    namespace: aic
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: mtls-nginx
spec:
  ingressClassName: apisix
  http:
  - name: mtls-nginx
    match:
      paths:
      - /hello
    backends:
    - serviceName: quickstart-nginx
      servicePort: 8443
```

Apply the configuration to your cluster:

```
kubectl apply -f upstream-mtls-route.yaml
```

## Verify[â](#verify "Direct link to Verify")

To verify mTLS between the gateway and the upstream service, send a request to the route:

```
curl -ikv "http://127.0.0.1:9080/hello"
```

You should receive an `HTTP/1.1 200 OK` response and see the following message:

```
Hello World!
```

This verifies the successful establishment of mTLS between the gateway and the upstream service.
