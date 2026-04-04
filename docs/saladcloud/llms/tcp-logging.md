# Source: https://docs.salad.com/container-engine/how-to-guides/external-logging/tcp-logging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TCP

*Last Updated: October 15, 2024*

# Overview

To enable external logging service on SaladCloud , you must configure your Container Group Deployment with the host
address and port number of your tcp endpoint. The host should be publicly reachable. Note that all communication between
SCE and your TCP endpoint will be encrypted with TLS(Transport Layer Security).

Many tools are available to you when creating your TCP endpoint. In this example, we will be using Logstash. Logstash is
a free and open-source server-sde data processing pipeline for ingesting and transforming data from a variety of
sources.

# Prerequisite

* Logstash Installation: You must have Logstash installed on the endpoint where you want to receive logs from SCE. To
  install Logstash, you can follow
  [the official documentation here](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html).
* TLS/SSL Certificates: Prepare SSL/TLS certificates and private keys for securing the communication between Logstash
  and SCE.

> 📘 A note on certificates
>
> You can use self-signed certificates for testing and development, but in a production environment, it is highly
> recommended to use certificates from a trusted Certificate Authority (CA).

## Generating Self-Signed Certificates

To generate self-signed certificate you can use OpenSSL.

1. Generate a CA (Certificate Authority) Certificate and Key:

```shell  theme={null}
# Generate CA private key
openssl genpkey -algorithm RSA -out ca-key.pem

# Create a self-signed CA certificate
openssl req -x509 -new -key ca-key.pem -out ca-certificate.pem
```

2. Generate Logstash Server Certificate and Key:

```shell  theme={null}
# Generate Logstash server private key
openssl genpkey -algorithm RSA -out logstash-private-key.pem

# Create a CSR (Certificate Signing Request) for Logstash server
openssl req -new -key logstash-private-key.pem -out logstash-csr.pem
```

3. Sign the Logstash server CSR with the CA Certificate:

```shell  theme={null}
# Sign the Logstash server CSR with the CA certificate
openssl x509 -req -in logstash-csr.pem -CA ca-certificate.pem -CAkey ca-key.pem -CAcreateserial -out logstash-certificate.pem
```

# Logstash Configuration

With the certificates ready, it's time to configure Logstash to accept secure log connections from SCE. Create a
Logstash configuration file, typically named logstash.conf, and add the following content:

```shell  theme={null}
input {
  tcp {
    host => "0.0.0.0" # listen on all available network interfaces
    port => 5001      # port to receive logs from SCE
    ssl_enable => true
    ssl_key => "/path/to/logstash-private-key.pem"
    ssl_cert => "/path/to/logstash-certificate.pem"
    ssl_certificate_authorities =>["/path/to/ca-certificate.pem"]
  }
}

# Remove unnecessary fields from log events
filter {
  mutate {
    remove_field => ["host", "port", "@version", "@timestamp"]
  }
}

# add your desired output plugin (e.g Elasticsearch, File, etc.)
output {
  stdout {
    codec => rubydebug
  }
}
```

In the input section, we configure Logstash to listen on port 5001, enable SSL/TLS encryption, and provide the paths to
your Logstash TLS/SSL certificates. For more information about the logstash configuration, please visit their
[official documentation](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-tcp.html).

# Starting Logstash

```shell  theme={null}
$ bin/logstash -f logstash.conf
```

Logstash is now configured and ready to use the SSL/TLS private key and certificate for secure logging service.

# Next Steps

Once you've set up Logstash, you can configure your Container Group Deployment on SCE and provide the host and port
number.

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-tcp.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b96bfe54e96f1514f17bb9fc0f12f9a4" data-og-width="536" width="536" data-og-height="519" height="519" data-path="container-engine/images/select-and-configure-tcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-tcp.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=977f924e6e10e61654b601d3d93d6a46 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-tcp.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b7adc63878226d58ee70f406bc187ab6 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-tcp.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=fb0fe3c7eb435b8aa3493d95f2174439 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-tcp.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=4bc0ef459d2e5010d0e07dd94370f3d5 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-tcp.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b8ccee4afe865a886e2cf67ee67d2946 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/select-and-configure-tcp.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=991887e60638bbda9feda324683e1989 2500w" />

Then, start the container group and, on your TCP endpoint, you should see streaming logs from your containers!

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tcp-logs.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=3251eda183f1e5ad8a18ca456f459127" data-og-width="1836" width="1836" data-og-height="928" height="928" data-path="container-engine/images/tcp-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tcp-logs.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=219ee620a2ed60f15cb6a6f618d5b02d 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tcp-logs.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=410927cbd6aa3417d0369cb64aca4037 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tcp-logs.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=6385503282def8e60fb77a20f120d777 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tcp-logs.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=1f34990a5c43174716c60b2fd523fd6d 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tcp-logs.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a91514261dc5a7f8049d20a5086332de 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tcp-logs.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=b744f3f7b99e2d9e911b125000755b94 2500w" />
