# Source: https://docs.curator.interworks.com/setup/proxy_configuration/forward_proxy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Forward Proxy

> Configure forward proxy settings for internet access and external connectivity

Curator utilizes internet access to connect to Tableau Server as well as Curator's web servers for updates.
When configured without outbound internet access, Curator upgrades must be performed manually and Tableau Server must
be accessible within the LAN.

Often, IT teams prefer to route internet traffic first through a proxy.
When configured to work through a proxy, Curator doesn't send requests directly to the internet.
Instead, it sends requests to the forward proxy, which in turn forwards the request.

To configure a forward proxy with Curator, Apache configuration files can be used.

On Windows, the `curator.conf` file is a great place for this configuration.
On Linux, `/var/www/html/.htaccess`, or any of the httpd.conf files can also be utilized.

The **proxy\_override** environment variable points Curator to a specific proxy for web requests.
If needed, **no\_proxy\_override** can be used to specify a route that should not use the proxy for traffic.

```conf  theme={null}
SetEnv proxy_override "http://proxy:80"
SetEnv no_proxy_override "www.example.com"
```
