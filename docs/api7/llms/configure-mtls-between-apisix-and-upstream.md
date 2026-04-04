# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/tls-and-mtls/configure-mtls-between-apisix-and-upstream.md

# Configure mTLS Between APISIX and Upstream

*Mutual TLS (mTLS)* is a two-way TLS where the client and the server authenticate each other. It is typically implemented in high-security environments to prevent unauthorized access and harden security.

This guide will walk you through how to configure mTLS between APISIX and an upstream service, using NGINX as a sample upstream service.

<br />

![mTLS between APISIX and Upstream](https://static.api7.ai/uploads/2024/12/12/1lMaoJUZ_oidc_flows.svg)

<br />

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the service for testing.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

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

Start an NGINX server as a sample upstream service in the same Docker network as APISIX:

```
docker run -d \
  --name quickstart-nginx \
  --network=apisix-quickstart-net \
  -p 8443:8443 \
  nginx
```

Copy CA certificate, server certificate public and private keys into NGINX:

```
docker cp ca.crt quickstart-nginx:/var/ca.crt
docker cp server.crt quickstart-nginx:/var/server.crt
docker cp server.key quickstart-nginx:/var/server.key
```

Configure an HTTPS server listening on `/hello` and port `8443` in NGINX configuration file:

/etc/nginx/nginx.conf

```
http {
    # ...
    server {
        listen 8443 ssl;
        server_name            test.com;
        ssl_certificate        /var/server.crt;
        ssl_certificate_key    /var/server.key;
        ssl_client_certificate /var/ca.crt;
        ssl_verify_client on;
        location /hello {
            return 200 "Hello APISIX!";
        }
    }
}
```

â¶ `server_name`: set to `test.com` to be consistent with the server certificate CN value.

â· `ssl_certificate`: configure the path to the server certificate public key `server.crt`.

â¸ `ssl_certificate_key`: configure the path to the server certificate private key `server.key`.

â¹ `ssl_client_certificate`: configure the path to the CA certificate public key `ca.crt`.

âº `ssl_verify_client`: set to `on` to verify the client certificate.

Reload the NGINX server to apply the configuration changes:

```
docker exec quickstart-nginx nginx -s reload
```

To verify that the NGINX instance is properly configured, send a request to the Nginx service's route with client certificate and key:

```
curl -ik "https://127.0.0.1:8443/hello" --cert client.crt --key client.key
```

You should receive an `HTTP/1.1 200 OK` response and see the following message:

```
Hello APISIX!
```

If you send a request to the Nginx service's route without any client certificate or key:

```
curl -ik "https://127.0.0.1:8443/hello"
```

You should receive an `HTTP/1.1 400 Bad Request` response.

## Configure mTLS for APISIX[â](#configure-mtls-for-apisix "Direct link to Configure mTLS for APISIX")

You can optionally load the content of `client.crt` and `client.key` into environment variables:

```
client_cert=$(cat client.crt)
client_key=$(cat client.key)
```

* Admin API

Create a route to the NGINX server:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "mtls-nginx",
  "uri": "/hello",
  "upstream": {
    "scheme": "https",
    "nodes": {
      "quickstart-nginx:8443":1
    },
    "tls": {
      "client_cert": "'"${client_cert}"'",
      "client_key": "'"${client_key}"'"
    },
    "type": "roundrobin"
  }
}'
```

â¶ `scheme`: set to `https`.

â· `nodes`: set to the NGINX server hostname `quickstart-nginx` and port `8443`.

â¸ `tls.client_cert`: configure the certificate public key `client.crt`.

â¹ `tls.client_key`: configure the certificate private key `client.key`.

## Verify mTLS between APISIX and Upstream Service[â](#verify-mtls-between-apisix-and-upstream-service "Direct link to Verify mTLS between APISIX and Upstream Service")

Send a request to the route:

```
curl -ikv "http://127.0.0.1:9080/hello"
```

You should receive an `HTTP/1.1 200 OK` response and see the following message:

```
Hello APISIX!
```

This verifies the successful establishment of mTLS between APISIX and the upstream service.

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have learned how to set up mTLS between APISIX and upstream services. APISIX also supports mTLS between clients and APISIX. See [Configure mTLS between Client and APISIX](https://docs.api7.ai/apisix/how-to-guide/traffic-management/tls-and-mtls/configure-mtls-between-client-and-apisix.md) to learn more.
