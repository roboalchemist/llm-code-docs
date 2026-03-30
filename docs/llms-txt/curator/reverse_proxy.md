# Source: https://docs.curator.interworks.com/setup/proxy_configuration/reverse_proxy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reverse Proxy

> Configure reverse proxy and load balancing solutions for Curator

When installing Curator, you may wish to place Curator behind a reverse proxy or load balanced solution.

## Health Checks

Health checks should be run against the `/ping` route instead of simply the base `/` route.
The base / route will often return a 302 redirect, which many load balancers view as a "down" response.
The /ping route will always return a 200 response.

## Headers

When your users access Curator over the reverse proxy, specific "headers" are used to tell Curator how to process the
request.

**X-FORWARDED-FOR** : The IP address of the end user.

**X-FORWARDED-HOST** : The host name of the request.
*Note: A "Forced Domain" in Portal Settings->Security overrides this value.*

**X-FORWARDED-PROTO** :  Whether to use HTTPS or HTTP for routes.

## Unable to adjust headers

Often, reverse proxy solutions are missing some or all of these headers.

To help configure a reverse proxy with Curator, Apache configuration files can be used.

On Windows, the `curator.conf` file is a great place for this configuration.
On Linux, `/var/www/html/.htaccess`, or any of the httpd.conf files can also be utilized.

```conf  theme={null}
SetEnv HOST "example.curator.interworks.com"
SetEnv HTTP_X_FORWARDED_HOST "example.curator.interworks.com"

SetEnv HTTPS "on"
SetEnv HTTP_X_FORWARDED_PROTO "https"
```

In addition to these settings, the security settings in **Settings** > **Curator** > **Portal Settings** > **General**
can be used.
In particular, **Forced Domain** and **Force SSL** should be utilized to specify the domain of Curator and to use SSL.
