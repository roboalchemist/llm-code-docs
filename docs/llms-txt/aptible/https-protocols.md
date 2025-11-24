# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-protocols.md

# HTTPS Protocols

Aptible offer a few ways to configure the protocols used by your [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview) for HTTPS termination through a set of [Configuration](/core-concepts/apps/deploying-apps/configuration) variables. These are the same variables as can be defined for [TLS Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/tls-endpoints). If set once on the application, they will apply to all TLS and HTTPS endpoints for that application.

# `SSL_PROTOCOLS_OVERRIDE`: Control SSL / TLS Protocols

The `SSL_PROTOCOLS_OVERRIDE` variable lets you customize the SSL Protocols allowed on your Endpoint.

Available protocols depend on your Endpoint platform:

* For ALB Endpoints: you can choose from these 8 combinations:
  * `TLSv1 TLSv1.1 TLSv1.2` (default)
  * `TLSv1 TLSv1.1 TLSv1.2 PFS`
  * `TLSv1.1 TLSv1.2`
  * `TLSv1.1 TLSv1.2 PFS`
  * `TLSv1.2`
  * `TLSv1.2 PFS`
  * `TLSv1.2 PFS TLSv1.3` (see note below comparing ciphers to `TLSv1.2 PFS`)
  * `TLSv1.3`

<Note>
  `PFS` ensures your Endpoint's ciphersuites support perfect forward secrecy on TLSv1.2 or earlier. TLSv1.3 natively includes perfect forward secrecy.
  Note for `TLSv1.2 PFS TLSv1.3`, compared to ciphers for `TLSv1.2 PFS`, this adds `TLSv1.3` ciphers and omits the following:

  * ECDHE-ECDSA-AES128-SHA
  * ECDHE-RSA-AES128-SHA
  * ECDHE-RSA-AES256-SHA
  * ECDHE-ECDSA-AES256-SHA
</Note>

* For Legacy ELB endpoints: the format is Nginx's [ssl\_protocols directive](http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_protocols). Pay very close attention to the format! A bad variable will prevent the proxies from starting.

<Note> The format for ALBs and ELBs is effectively identical: the only difference is the supported protocols. This means that if you have both ELB Endpoints and ALB Endpoints on a given app, or if you're upgrading from ELB to ALB, things will work as expected as long as you use protocols supported by ALBs, which are stricter.</Note>

# `SSL_CIPHERS_OVERRIDE`: Control ciphers

<Note>This variable is only available on Legacy ELB endpoints. On ALB Endpoints, you normally don't need to customize the ciphers available.</Note>

This variable lets you customize the SSL Ciphers used by your Endpoint.

The format is a string accepted by Nginx for its [ssl\_ciphers directive](http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_ciphers).

Pay very close attention to the required format, as here again a bad variable will prevent the proxies from starting.

# `DISABLE_WEAK_CIPHER_SUITES`: an opinionated policy for ELBs

<Note> This variable is only available on Legacy ELB endpoints. On ALB Endpoints, weak ciphers are disabled by default, so that setting has no effect.</Note>

Setting this variable to `true` (it has to be the exact string `true`) causes your Endpoint to stop accepting traffic over the `SSLv3` protocol or using the `RC4` cipher.

We strongly recommend setting this variable to `true` on all ELB Endpoints nowadays. Or, better, yet, upgrade to ALB Endpoints, where that's the default.

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
