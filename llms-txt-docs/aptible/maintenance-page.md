# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/maintenance-page.md

# Maintenance Page

# Enable Maintenance Page

Maintenance pages are only available by request. Please get in touch with [Aptible Support](/how-to-guides/troubleshooting/aptible-support) to enable this feature. Maintenance pages are enabled stack-by-stack, so please confirm which stacks you would like to enable this feature when you contact Aptible Support.

# Custom Maintenance Page

You can configure your [App](/core-concepts/apps/overview) with a custom maintenance page.

This page will be served by your [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview) when requests time out, or if your App is down. It will also be served if the Endpoint's underlying [Service](/core-concepts/apps/deploying-apps/services) is scaled to zero.

To configure one, set the `MAINTENANCE_PAGE_URL` [Configuration](/core-concepts/apps/deploying-apps/configuration) variable on your app:

```shell  theme={null}
aptible config:set --app "$APP_HANDLE" \
        MAINTENANCE_PAGE_URL=http://...
```

Aptible will download and cache the maintenance page when deploying your app. If it needs to be served, Aptible will serve the maintenance page directly to clients.

This means:

* Make sure your maintenance page is publicly accessible so that Aptible can download it.
* Don't use relative links in your maintenance page: the page won't be served from its original URL, so relative links will break.

If you don't set up a custom maintenance page, a generic Aptible maintenance page will be served instead.

# Brickwall

If your Service is scaled to zero, Aptible instead will route your traffic to an error page server: *Brickwall*.

Brickwall will serve your `Custom Maintenance Page` if you set one up, and fallback to a generic Aptible error page if you did not.

You usually shouldn't need to, but you can identify responses coming from Brickwall through their `Server` header, which will be set to `brickwall`. Brickwall returns a `502` error code which is not configurable.

If your Service is scaled up, but all app [Containers](/core-concepts/architecture/containers/overview) appear down, Aptible will route your traffic to *all* containers.

# Default Maintenance Page Appearance

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/error_proxy.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=69e1e9b717a673a8745570e3f01339bd" alt="Default Maintenance Page" data-og-width="1488" width="1488" data-og-height="694" height="694" data-path="images/error_proxy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/error_proxy.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=fb48741e5122e2167e6698a6b7dfadd7 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/error_proxy.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=def48083a9743e787a1489c1bff96755 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/error_proxy.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=586e1da87084541795647821184e816d 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/error_proxy.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=da46716bce0183601e8e28ea0e9bd11a 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/error_proxy.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=26698b13ec9f6c4717989b72abc051a2 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/error_proxy.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=44d1b7a02e5abb271485ea9a7527b9dc 2500w" />
