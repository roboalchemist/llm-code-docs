# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/grpc-endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# gRPC Endpoints

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/ccfd24b-tls-endpoints.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=7358d127473451d0a602a354f7e57f3e" alt="Image" data-og-width="1280" width="1280" data-og-height="720" height="720" data-path="images/ccfd24b-tls-endpoints.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/ccfd24b-tls-endpoints.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=02685d80d3c363e03e462e338e368ec3 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/ccfd24b-tls-endpoints.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f6b273562653d772a67f8b70d89c0e28 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/ccfd24b-tls-endpoints.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0d6188bfeab9e1a6f474a24ba12df6f5 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/ccfd24b-tls-endpoints.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d583b15b03bcfde42fec239a2fd37d27 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/ccfd24b-tls-endpoints.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d1344f39716ca678eeb696708a89e47d 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/ccfd24b-tls-endpoints.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=3b74f97b8ec524ba8b3774720013e051 2500w" />

gRPC Endpoints can be created using the [`aptible endpoints:grpc:create`](/reference/aptible-cli/cli-commands/cli-endpoints-grpc-create) command.

<Warning>Like TCP/TLS endpoints, gRPC endpoints do not support [Endpoint Logs](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs)</Warning>

# Traffic

gRPC Endpoints terminate TLS traffic and transfer it as plain TCP to your app.

# Container Ports

gRPC Endpoints are configured similarly to [TLS Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/tls-endpoints).

The Endpoint will listen for encrypted gRPC traffic on exposed ports and transfer it as plain gRPC traffic to your app over the same port. For example, if your [Image](/core-concepts/apps/deploying-apps/image/overview) exposes port `123`, the Endpoint will listen for gRPC traffic on port `123`, and forward it as plain gRPC traffic to your app [Containers](/core-concepts/architecture/containers/overview) on port `123`.

<Tip>Unlike [TLS Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/tls-endpoints), gRPC Endpoints DO provide [Zero-Downtime Deployment](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview#zero-downtime-deployment).</Tip>

# Zero-Downtime Deployment / Health Checks

gRPC endpoints provide [Zero-Downtime Deployment](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview#zero-downtime-deployment) by leveraging [gRPC Health Checking](https://grpc.io/docs/guides/health-checking/).
Specifically, Aptible will use [health/v1](https://github.com/grpc/grpc-proto/blob/master/grpc/health/v1/health.proto)'s Health.Check call against your service, passing in an empty service name, and will only continue with the deploy if your application responds `SERVING`.

<Warning>When implementing the health service, please ensure you register your service with a blank name, as this is what Aptible looks for.</Warning>

# SSL / TLS Settings

Aptible offer a few ways to configure the protocols used by your endpoints for TLS termination through a set of [Configuration](/core-concepts/apps/deploying-apps/configuration) variables. These are the same variables as can be defined for [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview). If set once on the application, they will apply to all gRPC, TLS, and HTTPS endpoints for that application.

# `SSL_PROTOCOLS_OVERRIDE`: Control SSL / TLS Protocols

The `SSL_PROTOCOLS_OVERRIDE` variable lets you customize the SSL Protocols allowed on your Endpoint. The format is that of Nginx's [ssl\_protocols directive](http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_protocols). Pay very close attention to the format, as a bad variable will prevent the proxies from starting.

# `SSL_CIPHERS_OVERRIDE`: Control ciphers

This variable lets you customize the SSL Ciphers used by your Endpoint.

The format is a string accepted by Nginx for its [ssl\_ciphers directive](http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_ciphers).

Pay very close attention to the required format, as here, again a bad variable will prevent the proxies from starting.

# `DISABLE_WEAK_CIPHER_SUITES`: an opinionated policy

Setting this variable to `true` (it has to be the exact string `true`) causes your Endpoint to stop accepting traffic over the `SSLv3` protocol or using the `RC4` cipher.

We strongly recommend setting this variable to `true` on all Endpoints nowadays.

# Examples

## Set `SSL_PROTOCOLS_OVERRIDE`

```shell  theme={null}
aptible config:set --app "$APP_HANDLE" \
        "SSL_PROTOCOLS_OVERRIDE=TLSv1.1 TLSv1.2"
```

## Set `DISABLE_WEAK_CIPHER_SUITES`

```shell  theme={null}
# Note: the value to enable DISABLE_WEAK_CIPHER_SUITES is the string "true"
# Setting it to e.g. "1" won't work.
aptible config:set --app "$APP_HANDLE" \
        DISABLE_WEAK_CIPHER_SUITES=true
```
