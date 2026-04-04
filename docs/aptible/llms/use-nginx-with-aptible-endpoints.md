# Source: https://www.aptible.com/docs/how-to-guides/app-guides/use-nginx-with-aptible-endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to use Nginx with Aptible Endpoints

Nginx is a popular choice for a reverse proxy to route requests through to Aptible [endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) using a `proxy_pass` directive.

One major pitfall of using Nginx with Aptible endpoints is that, by default, Nginx disregards DNS TTLs and caches the IPs of its upstream servers forever. In contrast, the IPs for Aptible endpoints change periodically (under the hood, Aptible use AWS ELBs, from which they inherit this property). This contrast means that Nginx will, by default, eventually use the wrong IPs when pointed at an Aptible endpoint through a `proxy_pass` directive. To work around this problem, avoid the following configuration pattern in your Nginx configuration:

```sql  theme={null}
location / {
    proxy_pass https://hostname-of-an-endpoint;
}
```

Instead, use this:

```sql  theme={null}
resolver 8.8.8.8;
set $upstream_endpoint https://hostname-of-an-endpoint;

location / {
    proxy_pass $upstream_endpoint;
}
```
