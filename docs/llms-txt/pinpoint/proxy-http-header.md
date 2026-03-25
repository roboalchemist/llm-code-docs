# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.2.2/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.3.0/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.3.1/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.3.2/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.3.3/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.4.0/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.0/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.1/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.2/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.3/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v2.5.4/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.0/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.1/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.2/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.3/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/v3.0.4/documents/proxy-http-header.md

# Source: https://pinpoint-apm.gitbook.io/pinpoint/documents/proxy-http-header.md

# Monitoring Proxy Server

## Proxy monitoring using HTTP headers <a href="#proxy-monitoring-using-http-headers" id="proxy-monitoring-using-http-headers"></a>

It is used to know the elapsed time between proxy and WAS.

![overview](https://2967689678-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MgQ1Is59jDrgEN5nG-0-3931491796%2Fuploads%2Fgit-blob-257fbee4518c6805487a8e000f6da518440eb974%2Fproxy-http-header-overview.png?alt=media\&token=ed6c55aa-00dd-444c-b98e-6dc57e679303)

## Pinpoint Configuration

pinpoint.config

```
profiler.proxy.http.header.enable=true
```

## Proxy Configuration

### Apache HTTP Server

* <http://httpd.apache.org/docs/2.4/en/mod/mod_headers.html>

Add HTTP header.

```
Pinpoint-ProxyApache: t=991424704447256 D=3775428 i=51 b=49
```

e.g.

httpd.conf

```
<IfModule mod_jk.c>
...
RequestHeader set Pinpoint-ProxyApache "%t %D %i %b"
...
</IfModule>
```

**%t is required value.**

### Nginx

* <http://nginx.org/en/docs/http/ngx_http_core_module.html>
* <http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_set_header>

Add HTTP header.

```
Pinpoint-ProxyNginx: t=1504248328.423 D=0.123
```

e.g.

nginx.conf

```
...
  server {
        listen       9080;
        server_name  localhost;

        location / {
            ...
            set $pinpoint_proxy_header "t=$msec D=$request_time";
            proxy_set_header Pinpoint-ProxyNginx $pinpoint_proxy_header;
        }
  }
...
```

or

```
http {
...

    proxy_set_header Pinpoint-ProxyNginx t=$msec;

...
}
```

**t=$msec is required value.**

### App

Milliseconds since epoch (13 digits) and app information.

Add HTTP header.

```
Pinpoint-ProxyApp: t=1594316309407 app=foo-bar
```

**t=epoch is required value.**
