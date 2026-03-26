# Source: https://docs.api7.ai/apisix/production/security/mtls/configure-mtls-between-client-and-admin-api.md

# Configure mTLS between Client and APISIX Admin API

*Mutual TLS (mTLS)* is a two-way TLS where the client and the server authenticate each other. It is typically implemented to prevent unauthorized access and harden security.

This document will show you how to configure mTLS between a client and APISIX Admin API, such that only authenticated users could interact and manage APISIX resources with Admin API.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.

## Generate Certificates and Keys[â](#generate-certificates-and-keys "Direct link to Generate Certificates and Keys")

Create a new directory and navigate into it:

```
mkdir mtls-apisix-admin && cd mtls-apisix-admin
```

Generate the Certificate Authority (CA) key and certificate:

```
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 36500 -sha256 \
  -key ca.key \
  -out ca.crt \
  -subj "/CN=ROOTCA" \
  -extensions v3_ca \
  -config <(printf "[req]\ndistinguished_name=req\n[ v3_ca ]\nbasicConstraints=critical,CA:TRUE\nkeyUsage=critical,keyCertSign,cRLSign\nsubjectKeyIdentifier=hash\nauthorityKeyIdentifier=keyid:always,issuer")
```

Generate the key and certificate signing request (CSR):

```
openssl genrsa -out admin_api.key 2048
openssl req -new -sha256 \
  -key admin_api.key \
  -out admin_api.csr \
  -subj "/CN=test.com"
```

Sign the server CSR with the CA certificate to generate the server certificate:

```
openssl x509 -req -days 36500 -sha256 \
  -in admin_api.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out admin_api.crt \
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

Allow read access for the files in the directory to avoid downstream permission issues:

```
chmod -R a+r ./
```

Copy certificates and keys into `/opt/mtls-apisix-admin-api` (or directory of your choice):

```
mkdir /opt/mtls-apisix-admin-api
cp ca.crt admin_api.key admin_api.crt client.key client.crt /opt/mtls-apisix-admin-api
```

## Configure mTLS[â](#configure-mtls "Direct link to Configure mTLS")

You will be starting etcd and APISIX in Docker containers and configuring APISIX to enable mTLS for Admin API.

### Start etcd[â](#start-etcd "Direct link to Start etcd")

Start an etcd server in Docker:

```
docker run -d \
  --name etcd \
  --network host \
  -e ALLOW_NONE_AUTHENTICATION=yes \
  -e ETCD_ADVERTISE_CLIENT_URLS=http://etcd:2379 \
  -e ETCD_LISTEN_CLIENT_URLS=http://0.0.0.0:2379 \
  bitnami/etcd:3.5.7
```

### Start APISIX[â](#start-apisix "Direct link to Start APISIX")

Create an APISIX configuration file in `/opt` (or directory of your choice):

```
echo '
apisix:
  ssl:
    ssl_trusted_certificate: /usr/local/apisix/certs/ca.crt
deployment:
  admin:
    admin_key_required: true
    admin_key:
      -
        name: admin
        key: Sup3rs3cretWr1teK3y   # replace with your write key
        role: admin
    admin_listen:
      port: 9180
    https_admin: true
    admin_api_mtls:
      admin_ssl_cert: /usr/local/apisix/certs/admin_api.crt
      admin_ssl_cert_key: /usr/local/apisix/certs/admin_api.key
      admin_ssl_ca_cert: /usr/local/apisix/certs/ca.crt
' > /opt/config.yaml
```

â¶ Set the path to the trusted CA certificate in the Docker container.

â· Set the listening address for Admin API.

â¸ Require TLS for accessing Admin API.

â¹ Set the path to the server TLS certificate in the Docker container.

âº Set the path to the server TLS key in the Docker container.

â» Set the path to the CA certificate in the Docker container.

Start an APISIX instance in Docker:

```
docker run -d \
  --name apisix \
  --network host \
  -e APISIX_DEPLOYMENT_ETCD_HOST=https://127.0.0.1:2379 \
  -v /opt/mtls-apisix-admin-api:/usr/local/apisix/certs \
  -v /opt/config.yaml:/usr/local/apisix/conf/config.yaml \
  apache/apisix
```

â¶ Mount the TLS certificate and key directory on the host to the Docker container.

â· Mount the APISIX configuration file on the host to the Docker container.

## Verify mTLS[â](#verify-mtls "Direct link to Verify mTLS")

To verify APISIX is up and mTLS is properly configured for Admin API, send a request to get all routes:

```
curl -ik --resolve "test.com:9180:127.0.0.1" "https://test.com:9180/apisix/admin/routes" \
  --cert client.crt --key client.key \
  -H "X-API-KEY: Sup3rs3cretWr1teK3y"
```

If everything is ok, you should see a `HTTP/1.1 200 OK` response with all the APISIX routes, such as:

```
{"list":[],"total":0}
```
