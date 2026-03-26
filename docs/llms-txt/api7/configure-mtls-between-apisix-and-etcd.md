# Source: https://docs.api7.ai/apisix/production/security/mtls/configure-mtls-between-apisix-and-etcd.md

# Configure mTLS between APISIX and etcd

*Mutual TLS (mTLS)* is a two-way TLS where client and the server authenticate each other. It is typically implemented to prevent unauthorized access and harden security.

This document will show you how to configure mTLS between APISIX and etcd using a dockerized APISIX and etcd. Adjust the steps accordingly for different deployment approaches.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.

## Generate Certificates and Keys[â](#generate-certificates-and-keys "Direct link to Generate Certificates and Keys")

Create a new directory and navigate into it:

```
mkdir mtls-apisix-etcd && cd mtls-apisix-etcd
```

Generate the certificate authority (CA) key and certificate:

```
openssl genrsa -out ca.key 2048 && \
  openssl req -new -sha256 -key ca.key -out ca.csr -subj "/CN=ROOTCA" && \
  openssl x509 -req -days 36500 -sha256 -extensions v3_ca -signkey ca.key -in ca.csr -out ca.crt
```

Generate the key and certificate with the common name `ETCD` for etcd, and sign with the CA certificate:

```
openssl genrsa -out etcd.key 2048 && \
  openssl req -new -sha256 -key etcd.key -out etcd.csr -subj "/CN=ETCD" && \
  openssl x509 -req -days 36500 -sha256 -extensions v3_req \
  -CA ca.crt -CAkey ca.key -CAserial ca.srl -CAcreateserial \
  -in etcd.csr -out etcd.crt
```

Generate the key and certificate with the common name `CLIENT` for APISIX, and sign with the CA certificate:

```
openssl genrsa -out client.key 2048 && \
  openssl req -new -sha256 -key client.key -out client.csr -subj "/CN=CLIENT" && \
  openssl x509 -req -days 36500 -sha256 -extensions v3_req \
  -CA ca.crt -CAkey ca.key -CAserial ca.srl -CAcreateserial \
  -in client.csr -out client.crt
```

Allow read access for the files in the directories to avoid downstream permission issues:

```
chmod -R a+r ./
```

Copy certificates and keys into `/opt/mtls-apisix-etcd` (or directory of your choice):

```
mkdir /opt/mtls-apisix-etcd
cp ca.crt etcd.key etcd.crt client.key client.crt /opt/mtls-apisix-etcd
```

## Configure mTLS[â](#configure-mtls "Direct link to Configure mTLS")

You will be starting etcd and APISIX in Docker containers with TLS certificates and keys to enable mTLS communication between the two.

### Start etcd[â](#start-etcd "Direct link to Start etcd")

Start an etcd server in Docker:

```
docker run -d \
  --name etcd-prod \
  --network host \
  -v /opt/mtls-apisix-etcd:/opt/bitnami/etcd/certs \
  -e ALLOW_NONE_AUTHENTICATION=yes \
  -e ETCD_ADVERTISE_CLIENT_URLS=https://etcd-prod:2379 \
  -e ETCD_LISTEN_CLIENT_URLS=https://0.0.0.0:2379 \
  -e ETCD_CLIENT_CERT_AUTH=true \
  -e ETCD_CERT_FILE=/opt/bitnami/etcd/certs/etcd.crt \
  -e ETCD_KEY_FILE=/opt/bitnami/etcd/certs/etcd.key \
  -e ETCD_TRUSTED_CA_FILE=/opt/bitnami/etcd/certs/ca.crt \
  bitnami/etcd:3.5.7
```

â¶ Enable client certificate authentication.

â· Set the path to the etcd TLS certificate.

â¸ Set the path to the etcd TLS key.

â¹ Set the path to the trusted CA certificate.

To verify etcd is up and mTLS is properly configured, send a request to etcd with the client certificate and key to get the etcd version:

```
curl -ikv --resolve "ETCD:2379:127.0.0.1" "https://ETCD:2379/version" \
  --cert /opt/mtls-apisix-etcd/client.crt --key /opt/mtls-apisix-etcd/client.key
```

If everything is okay, you should see a `HTTP/2 200` response with the version of etcd:

```
{"etcdserver":"3.5.7","etcdcluster":"3.9.0"}
```

### Start APISIX[â](#start-apisix "Direct link to Start APISIX")

Create an APISIX configuration file in `/opt` (or directory of your choice):

```
echo 'apisix:
  ssl:
    ssl_trusted_certificate: /usr/local/apisix/certs/ca.crt
deployment:
  role: traditional
  role_traditional:
    config_provider: etcd
  admin:
    admin_key_required: true
    admin_key:
      -
        name: admin
        key: Sup3rs3cretWr1teK3y   # replace with your write key
        role: admin
  etcd:
    host:
      - "https://ETCD:2379"
    tls:
      cert: /usr/local/apisix/certs/client.crt
      key: /usr/local/apisix/certs/client.key
' > /opt/config.yaml
```

â¶ Set the path to the trusted CA certificate in the Docker container.

â· Set the path to the client TLS certificate in the Docker container.

â¸ Set the path to the client TLS key in the Docker container.

Start an APISIX instance in Docker:

```
docker run -d \
  --name apisix \
  --network host \
  --add-host ETCD:127.0.0.1 \
  -e APISIX_DEPLOYMENT_ETCD_HOST=https://127.0.0.1:2379 \
  -v /opt/mtls-apisix-etcd:/usr/local/apisix/certs \
  -v /opt/config.yaml:/usr/local/apisix/conf/config.yaml \
  apache/apisix
```

â¶ Mount the TLS certificate and key directory from the host to the Docker container.

â· Mount the APISIX configuration file from the host to the Docker container.

## Verify mTLS[â](#verify-mtls "Direct link to Verify mTLS")

To verify APISIX is up and mTLS is properly configured between APISIX and etcd, send a request to APISIX to get all routes:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -H "X-API-KEY: Sup3rs3cretWr1teK3y"
```

If everything is okay, you should see a `HTTP/1.1 200 OK` response with all the APISIX routes, such as:

```
{"list":[],"total":0}
```
