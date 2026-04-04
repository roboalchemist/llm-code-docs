# Source: https://docs.api7.ai/enterprise/api-security/upstream-mtls.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-security/upstream-mtls.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-security/upstream-mtls.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-security/upstream-mtls.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-security/upstream-mtls.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-security/upstream-mtls.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-security/upstream-mtls.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-security/upstream-mtls.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-security/upstream-mtls.md

# Configure mTLS between API7 Enterprise and Upstream

Mutual TLS (mTLS) is a two-way TLS where the client and the server authenticate each other. It is typically implemented in high-security environments to prevent unauthorized access and harden security.

This guide will walk you through how to configure mTLS between APISIX and an upstream service, using NGINX as a sample upstream service.

Below is an interactive demo that provides a hands-on guidance.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
* [Launch Your First API](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).
* Create a token on API7 Enterprise.

## Generate Certificates and Keys[â](#generate-certificates-and-keys "Direct link to Generate Certificates and Keys")

1. Generate the certificate authority (CA) key and certificate.

   ```
   openssl genrsa -out ca.key 2048
   openssl req -x509 -new -nodes -key ca.key -sha256 -days 36500 -out ca.crt \
   -subj "/CN=ROOTCA"
   ```

2. Generate the server key and certificate with the common name `test.com` for API7 Enterprise, and sign with the CA certificate.

   ```
   openssl genrsa -out server.key 2048 && \
   openssl req -new -key server.key -out server.csr -subj "/CN=test.com" && \
   cat > server.ext << EOF
   authorityKeyIdentifier=keyid,issuer
   basicConstraints=CA:FALSE
   keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
   subjectAltName = @alt_names
   [alt_names]
   DNS.1 = test.com
   EOF
   openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
   -CAcreateserial -out server.crt -days 36500 \
   -sha256 -extfile server.ext
   ```

3. Generate the key and certificate with the common name `CLIENT` for a client, and sign with the CA certificate.

   ```
   openssl genrsa -out client.key 2048 && \
   openssl req -new -key client.key -out client.csr -subj "/CN=client" && \
   cat > client.ext << EOF
   authorityKeyIdentifier=keyid,issuer
   basicConstraints=CA:FALSE
   keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
   extendedKeyUsage = clientAuth
   EOF
   openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 36500 -sha256 -extfile client.ext
   ```

4. After generating certificates and keys, check your local device to locate these files.

   â¶ `client.crt`: client certificate

   â· `client.key`: client certificate key

   â¸ `ca.crt`: CA certificate

## Configure Upstream Service[â](#configure-upstream-service "Direct link to Configure Upstream Service")

Start an NGINX server as a sample upstream service:

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
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    server {
        listen 8443 ssl;
        server_name            test.com;
        ssl_certificate        /var/server.crt;
        ssl_certificate_key    /var/server.key;
        ssl_client_certificate /var/ca.crt;
        ssl_verify_client on;
        location /hello {
            return 200 "Hello API7!";
        }
    }

    include /etc/nginx/conf.d/*.conf;
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

To verify that the NGINX instance is properly configured, send a request to the route with client certificate and key:

```
curl -ik "https://127.0.0.1:8443/hello" --cert client.crt --key client.key
```

You should receive an `HTTP/1.1 200 OK` response.

## Configure mTLS for API7 Enterprise[â](#configure-mtls-for-api7-enterprise "Direct link to Configure mTLS for API7 Enterprise")

### Create a Route to the NGINX Server[â](#create-a-route-to-the-nginx-server "Direct link to Create a Route to the NGINX Server")

1. Log in to the API7 Enterprise Dashboard, choose the `default` gateway group.
2. Create a service named `mtls-nginx`, and a route `/hello` with the `GET` method.
3. Configure it with an upstream node. In the **Host** field, enter the IP address of your API7 dashboard, and set `8443` in the **Port** field.
4. Select `HTTPS` in the **Scheme** field.

### Configure SSL Certificates[â](#configure-ssl-certificates "Direct link to Configure SSL Certificates")

1. Click **SSL Certificates** from the side navigation bar, and then click **+ Add SSL Certificate**.

2. From the **+ Add SSL Certificate** dialog box, do the following:

   * In the **Type** field, choose `Client certificate`.
   * Choose **Upload** as the method.
   * In the **Certificate** field, upload the `client.crt` file.
   * In the **Private Key** field, upload the `client.key` file.
   * Turn on the **Peer Authentication** button.
   * In the **CA Certificate (Optional)** field, upload the `ca.crt` file.
   * Click **Add**.

3. An SSL certificate with an ID and `test.com` as SNIS is successfully added.

### Modify TLS Configuration of Upstream Service[â](#modify-tls-configuration-of-upstream-service "Direct link to Modify TLS Configuration of Upstream Service")

Set environment variables:

```
export service_id=${YOUR_SERVICE_ID}
export gateway_group_id=${YOUR_GATEWAY_GROUP_ID}
export client_cert_id=${YOUR_CLIENT_CERT_KEY}
export X_API_KEY=${YOUR_API_KEY}
```

View the service configuration:

```
curl -k -X GET "https://192.168.31.29:7443/apisix/admin/services/$service_id?gateway_group_id=$gateway_group_id" \
  -H 'Content-Type: application/json' \
  -H 'X-API-KEY: ${YOUR_API_KEY}'
```

You will receive a similar response without a TLS key:

```
..."service_id":"b7c9c7bc-19b3-47db-b2a2-4867380e2ff1","id":"b7c9c7bc-19b3-47db-b2a2-4867380e2ff1","service_version_id":"5e59b458-e5e3-426e-9f9e-668ced45e522","gateway_group_id":"default","gateway_group_name":"default","status":1,
...
```

Modify TLS Configuration of Upstream Service:

```
curl -k -X PATCH "https://192.168.31.29:7443/apisix/admin/services/$service_id?gateway_group_id=$gateway_group_id" \
  -H 'Content-Type: application/json' \
    -H 'X-API-KEY: ${YOUR_API_KEY}' \
  -d '[{"op":"add", "path":"/upstream/tls", "value": {"client_cert_id": ${YOUR_CLIENT_CERT_ID}}}]'
```

You will receive a similar response with a TLS key:

```
...
"tls":{"client_cert_id":"58999f7b-3400-493a-a518-99716439488e"}},
"service_id":"b7c9c7bc-19b3-47db-b2a2-4867380e2ff1","id":"b7c9c7bc-19b3-47db-b2a2-4867380e2ff1","service_version_id":"5e59b458-e5e3-426e-9f9e-668ced45e522","gateway_group_id":"default","gateway_group_name":"default","status":1,
...
```

## Verify mTLS between API7 Enterprise and Upstream Service[â](#verify-mtls-between-api7-enterprise-and-upstream-service "Direct link to Verify mTLS between API7 Enterprise and Upstream Service")

Send a request to the route:

```
curl -ik "http://127.0.0.1:9080/hello"
```

You should receive an `HTTP/1.1 200 OK` response, verifying that the mTLS between API7 Enterprise and upstream has been set up successfully.

## Additional Resource(s)[â](#additional-resources "Direct link to Additional Resource(s)")

* Key Concepts
  <!-- -->
  * [SSL Certificates](https://docs.api7.ai/enterprise/3.3.x/key-concepts/ssl-certificates.md)
* Getting Started
  <!-- -->
  * [Launch Your First API](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md)
