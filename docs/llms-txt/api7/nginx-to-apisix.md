# Source: https://docs.api7.ai/apisix/migration/nginx-to-apisix.md

# Migrate from NGINX to APISIX

Users migrate from NGINX to APISIX because of its ease of use and extensibility. For instance, APISIX:

1. enables configuration reload without downtime.
2. supports [canary release](https://docs.api7.ai/apisix/production/upgrade/canary-deployment.md), [authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/set-up-sso-with-keycloak.md), and [observability](https://docs.api7.ai/apisix/how-to-guide/observability/monitor-apisix-with-prometheus.md) out-of-the-box.
3. can be configured through the [Admin API](https://docs.api7.ai/apisix/reference/admin-api/.md), or [YAML configuration files](https://docs.api7.ai/apisix/reference/standalone-configurations).
4. provides extensibility that allows users to [develop custom plugins in Lua](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/create-plugin-in-lua.md) and other programming languages.

This guide will walk you through the process of migrating NGINX configurations for typical scenarios, to equivalent APISIX configurations.

caution

Make sure to test the migrated configuration in a sandboxed environment before deploying to production.

## Configure Reverse Proxy[â](#configure-reverse-proxy "Direct link to Configure Reverse Proxy")

Acting as a proxy and forwarding requests to an upstream server is the primary functionality of NGINX and APISIX.

This example uses NGINX and APISIX to forward requests to the `/anything/` path to the upstream, `httpbin.org`.

To proxy requests in NGINX, the `proxy_pass` directive is used:

/etc/nginx/nginx.conf

```
http {
    server {
        listen 80;
        location /anything/ {
            proxy_pass http://httpbin.org:80;
        }
    }
}
```

â¶ Listen for requests on port 80.

â· Match locations starting with `/anything/`.

â¸ Proxy the matched request to `httpbin.org`.

APISIX achieves the same configuration through [routes](https://docs.api7.ai/apisix/key-concepts/routes.md).

Create a route as shown below:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" -d '
{
  "id": "apisix-anything",
  "uri": "/anything/*",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "httpbin.org:80": 1
    }
  }
}'
```

â¶ Match all requests with the path prefix `/anything/`.

â· Proxy the matched request to `httpbin.org`.

Send a request to the created route:

```
curl -i "http://127.0.0.1:9080/anything/nothing"
```

You should see a `HTTP/1.1 200 OK` response with the following content:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Host": "127.0.0.1",
    "User-Agent": "curl/8.4.0",
    "X-Amzn-Trace-Id": "Root=1-661fc252-35c621bc2d2b961c6ce98366",
    "X-Forwarded-Host": "127.0.0.1"
  },
  "json": null,
  "method": "GET",
  "origin": "192.168.289.1, 45.253.168.124",
  "url": "http://127.0.0.1/anything/nothing"
}
```

See the [Traffic Management guides](https://docs.api7.ai/apisix/how-to-guide/traffic-management/rate-limiting.md) for more complex routing scenarios.

## Configure Load Balancing[â](#configure-load-balancing "Direct link to Configure Load Balancing")

NGINX is also used extensively as a load balancer to distribute incoming requests among several upstream servers.

This example uses NGINX and APISIX to balance the load between two upstreams, `httpbin.org` and `mock.api7.ai`, while keeping a failover server, `192.0.0.1`, for failures.

These upstreams are specified in an `upstream` block (context) in NGINX configuration:

/etc/nginx/nginx.conf

```
http {
    upstream backend {
        server httpbin.org:443;
        server mock.api7.ai:443;
        server 192.0.0.1:443 backup;
    }

    server {
        listen 80;
        location / {
            proxy_pass https://backend;
        }
    }
}
```

â¶ Create an upstream named `backend`.

â· Configure upstream nodes, `httpbin.org` and `mock.api7.ai`.

â¸ Configure failover server, `192.0.0.1`, to fall back to if the above nodes fail.

APISIX achieves the same configuration through the [`nodes`](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Upstream/paths/~1apisix~1admin~1upstreams/post) attribute in the [upstream](https://docs.api7.ai/apisix/key-concepts/upstreams.md) configuration.

Create a route with multiple upstream nodes:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" -d '
{
  "id": "apisix-headers",
  "uri": "/headers",
  "upstream" : {
    "type": "roundrobin",
    "nodes": [
      { "host": "httpbin.org", "port": 443, "weight": 3 },
      { "host": "mock.api7.ai", "port": 443, "weight": 1 },
      { "host": "192.0.0.1", "port": 443, "priority": -1 }
    ],
    "pass_host": "node",
    "scheme": "https"
  }
}'
```

â¶ Use the weighted round robin algorithm for load balancing. See [Load Balancing](https://docs.api7.ai/apisix/key-concepts/upstreams.md#load-balancing) for other options.

â· Configure upstream nodes, `httpbin.org` and `mock.api7.ai`.

â¸ Configure failover server, `192.0.0.1`, to fall back to if the above nodes fail.

Send 50 requests to the created route to verify load balancing:

```
resp=$(seq 50 | xargs -I{} curl "http://127.0.0.1:9080/headers" -sL) && \
  count_httpbin=$(echo "$resp" | grep "httpbin.org" | wc -l) && \
  count_mockapi7=$(echo "$resp" | grep "mock.api7.ai" | wc -l) && \
  echo httpbin.org: $count_httpbin, mock.api7.ai: $count_mockapi7
```

You should see a similar response:

```
httpbin.org: 49, mock.api7.ai: 1
```

## Serve Static Files[â](#serve-static-files "Direct link to Serve Static Files")

NGINX and APISIX can serve static files directly. These typically include HTML, CSS, JavaScript, images, fonts, and other media files that are served without any modification to the client.

This example uses NGINX and APISIX to cache and proxy static files from the [Web Hypertext Application Technology Working Group (WHATWG) public GitHub repository](https://github.com/whatwg).

NGINX supports using regular expressions in the location block to match files based on their extension, as shown below:

/etc/nginx/nginx.conf

```
http {
    proxy_cache_path /data/nginx/cache keys_zone=mycache:10m;
    server {
        listen 80;
        proxy_cache mycache;
        location ~* ^/whatwg/(.+\.(jpeg|html))$ {
            proxy_pass https://raw.githubusercontent.com;
        }
    }
}
```

â¶ Store the cached content in `/data/nginx/cache` with a shared memory zone of size 10 MB for storing cache keys.

â· Use the created cache, `mycache`.

â¸ Match requests with `/whatwg/` prefix and a file extension of either `.jpeg` or `.html` using a regular expression.

â¹ Proxy matched requests to `raw.githubusercontent.com`.

APISIX uses [variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) to match paths. Then, to cache the responses, APISIX uses the [`proxy-cache`](https://docs.api7.ai/hub/proxy-cache.md) plugin.

Create a route with `proxy-cache` enabled:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" -d '
{
  "id": "apisix-whatwg",
  "uri": "/whatwg/*",
  "vars": [["uri", "~~", "(.jpeg|.html)$"]],
  "plugins": {
    "proxy-cache": {}
  },
  "upstream": {
    "type": "roundrobin",
    "scheme": "https",
    "pass_host": "node",
    "nodes": {
      "raw.githubusercontent.com": 1
    }
  }
}'
```

â¶ Match requests which end in `.jpeg` or `.html` using the `uri` variable.

â· Enable `proxy-cache` to cache responses.

â¸ Proxy matched requests to `raw.githubusercontent.com`.

Send a request to the created route for an HTML file:

```
curl -i "http://127.0.0.1:9080/whatwg/html/main/404.html"
```

You should receive an `HTTP/1.1 200 OK` response and see the following file content:

```
<!DOCTYPE html>
<script src="/link-fixup.js" defer></script>
<title>404 Not Found</title>
<style>
  body.loading div.failed,
  body.failed div.loading,
  div.failed {
    display: none;
  }
  body.loading div.loading,
  body.failed div.failed,
  div.loading {
    display: block;
  }
</style>
<body onload="document.body.className = 'failed'">
  <script>
    document.body.className = "loading";
  </script>
  <div class="loading">
    <p>Loading...</p>
  </div>
  <div class="failed">
    <h1>Not Found</h1>
    <p>The page you are looking for is no longer available at this URL.</p>
    <p>
      Links to the multipage version of the specification are unfortunately
      likely to break over time. You might be able to find what you want from
      <a href="/multipage/">the contents page</a>.
    </p>
    <p>
      If you have found a broken link on the WHATWG site itself, please
      <a href="https://github.com/whatwg/html/issues/new">file an issue</a>. If
      you found a broken link from another site pointing to the WHATWG site,
      please let that site know of the problem instead. Thanks!
    </p>
  </div>
</body>
```

## Configure SSL Termination[â](#configure-ssl-termination "Direct link to Configure SSL Termination")

NGINX can terminate HTTPS traffic from clients to offload the upstream from the additional burden of decryption. APISIX also supports this feature out-of-the-box.

This example uses NGINX and APISIX to terminate SSL before proxying requests to the upstream, `httpbin.org`, over HTTP.

NGINX uses the provided SSL certificates to set up SSL termination:

/etc/nginx/nginx.conf

```
http {
    server {
        listen 443 ssl;
        server_name www.test.com;
        ssl_certificate /etc/nginx/ssl/website.com/certificate.crt;
        ssl_certificate_key /etc/nginx/ssl/website.com/private.key;
        location /ip {
            proxy_pass http://httpbin.org:80;
        }
    }
}
```

â¶ Listen on port 443 for HTTPS requests.

â· Configure path to SSL certificate.

â¸ Configure path to SSL certificate key.

APISIX uses an SSL certificate object to store the certificate and the private key:

```
curl -i "http://127.0.0.1:9180/apisix/admin/ssls" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" -d '
{
  "id": "apisix-test-com-ssl",
  "sni": "www.test.com",
  "cert": "'"$(cat certificate.crt)"'",
  "key": "'"$(cat private.key)"'"
}'
```

â¶ Configure SSL certificate.

â· Configure SSL certificate key.

See [Configure HTTPS Between Client and APISIX](https://docs.api7.ai/apisix/how-to-guide/traffic-management/tls-and-mtls/configure-https-between-client-and-apisix.md) for a detailed guide on configuring SSL.

### Redirect HTTP to HTTPS[â](#redirect-http-to-https "Direct link to Redirect HTTP to HTTPS")

In addition to terminating HTTPS traffic, NGINX can also be configured to redirect HTTP traffic to HTTPS.

NGINX uses the `return` directive to redirect with a `301 Moved Permanently` status code:

/etc/nginx/nginx.conf

```
http {
    server {
        listen 80;
        server_name www.test.com;
        return 301 https://$host$request_uri;
    }
}
```

â¶ Redirect to the HTTPS version of the requested URI.

APISIX uses the `redirect` plugin to achieve the same behavior:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" -d '
{
    "id": "apisix-redirect",
    "uri": "/*",
    "plugins": {
        "redirect": {
            "http_to_https": true,
            "ret_code": 301
        }
    }
}'
```

â¶ Redirect HTTP requests to HTTPS.

â· Return a `301 Moved Permanently` status code while redirecting.

Send an HTTP request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should see an `HTTP/1.1 301 Moved Permanently` response.

## Configure IP Access Control[â](#configure-ip-access-control "Direct link to Configure IP Access Control")

One way to use NGINX as a firewall is by restricting access to your services to specific IP addresses. This helps prevent unauthorized access and malicious users.

This example uses NGINX and APISIX to allow requests only from the IP address `192.168.1.0/24`.

NGINX uses the `allow` directive to allow access to IP addresses and the `deny` directive to deny access as shown below:

/etc/nginx/nginx.conf

```
http {
    server {
        listen 80;
        location /anything/ {
            allow 192.168.1.0/24;
            deny all;
            proxy_pass http://httpbin.org:80;
        }
    }
}
```

â¶ Allow access to the IP address `192.168.1.0/24`.

â· Deny access to all other IP addresses.

APISIX achieves the same configuration through the [`ip-restriction`](https://docs.api7.ai/hub/ip-restriction.md) plugin.

Create a route with `ip-restriction` enabled:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" -d '
{
  "id": "apisix-anything",
  "uri": "/anything",
  "plugins": {
    "ip-restriction": {
      "whitelist": ["192.168.1.0/24"]
    }
  },
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "httpbin.org:80": 1
    }
  }
}'
```

â¶ Add the IP address, `192.168.1.0/24`, to the whitelist to allow access.

Send a request to the created route:

```
curl -i "http://127.0.0.1:9080/anything"
```

If your IP is allowed, you should receive an `HTTP/1.1 200 OK` response. If not, you should receive an `HTTP/1.1 403 Forbidden` response with the following error message:

```
{"message":"Access denied"}
```

## Customize NGINX Configuration Generated by APISIX[â](#customize-nginx-configuration-generated-by-apisix "Direct link to Customize NGINX Configuration Generated by APISIX")

APISIX generates an NGINX configuration file from the configurations in [`apisix/cli/config.lua`](https://github.com/apache/apisix/blob/master/apisix/cli/config.lua). To customize the NGINX configuration, add snippets to the `nginx_config` field in the `conf/config.yaml` file.

The example below shows the available snippets with examples:

```
nginx_config:
  main_configuration_snippet: |
    daemon on;
  http_configuration_snippet: |
    server
    {
        listen 45651;
        server_name _;
        access_log off;

        location /ysec_status {
            req_status_show;
            allow 127.0.0.1;
            deny all;
        }
    }

    chunked_transfer_encoding on;
  http_server_configuration_snippet: |
    set $my "var";
  http_admin_configuration_snippet: |
    log_format admin "$request_time $pipe";
  http_end_configuration_snippet: |
    server_names_hash_bucket_size 128;
  stream_configuration_snippet: |
    tcp_nodelay off;
```

â¶ Add custom directives to the `main` context (outside other contexts).

â· Add custom configuration to the `http` context.

â¸ Add custom directives to the `server` context.

â¹ Add custom directives to the `admin` `server` context.

âº Add custom directives to the end of the `http` context.

â» Add custom configuration to the `stream` context.

caution

Make sure to indent the custom configurations correctly. Incorrect indentation may cause APISIX to fail while generating NGINX configuration.

## FAQ and Troubleshooting[â](#faq-and-troubleshooting "Direct link to FAQ and Troubleshooting")

### HTTP Requests Automatically Redirected to HTTPS with `HTTP/1.1 301 Moved Permanently` or `HTTP/1.1 308 Permanent Redirect` Status Codes[â](#http-requests-automatically-redirected-to-https-with-http11-301-moved-permanently-or-http11-308-permanent-redirect-status-codes "Direct link to http-requests-automatically-redirected-to-https-with-http11-301-moved-permanently-or-http11-308-permanent-redirect-status-codes")

APISIX does not force a `301` redirect to HTTPS unless the `redirect` plugin is configured as shown in the [section above](#redirect-http-to-https).

If you intend to support both HTTP and HTTPS on the same domain, you do not have to configure the `redirect` plugin with `http_to_https` enabled.
