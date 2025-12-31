# Source: https://herd.laravel.com/docs/macos/sites/securing-sites.md

# Securing Sites

# Securing Sites with TLS

By default, Herd serves sites over HTTP.
However, if you would like to serve a site over encrypted TLS using HTTP/2, you may secure your sites. This is sometimes necessary when working with redirect URLs and other scenarios.

## Via the GUI

You can secure/unsecure a site in the [Site Manager](/macos/sites/managing-sites). You can open the Sites window via the Herd menu bar icon and selecting "Sites".

If you see a closed lock icon, the site is secure and if there is crossed out lock, the site does not have a certificate and is served via HTTP.

<Frame>
  <img alt="Secure Sites" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c65c8e6b90fe38ff3148452fc0e0c1be" data-og-width="1868" width="1868" data-og-height="1122" height="1122" data-path="images/docs/sites_secure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1d2d73721585cf4defb780676c83d2d0 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b7bdda1fc266bad91f537a262080442d 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=cd305ae76d5fd80a3d7c46e18968491e 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d17986a9cd5f91dda2bda5ca0a5a6558 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=706675c1c17b9689c6feffc48b34a4aa 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=cc82e311d0f626467593e1c88bd79060 2500w" />
</Frame>

Clicking on the lock icon toggles the status of the site. If you're securing the site, you may need to confirm one or more permission related popups to create the local certificate.

## Via the CLI

If you prefer to use the CLI, you can use the `herd secure` command to secure/unsecure a site.
For example, if Herd serves your site via the `example-site.test` domain, you need run the following command to secure it:

```shell  theme={null}
# secure the current working directory
herd secure

# secure example-site.test from anywhere
herd secure example-site 
```

To "unsecure" a site and revert back to serving its traffic over plain HTTP, use the `unsecore` command.
Like the `secure` command, this command accepts the sitename that you wish to unsecure:

```shell  theme={null}
# unsecure the current working directory
herd unsecure

# unsecure example-site.test from anywhere
herd unsecure example-site 
```

After unsecuring a site, you man need to restart your browser session because many browsers like Google Chrome cache redirects to HTTPS and will give you a hard time.

## Listing all secure sites

The Herd CLI has a command to list all sites that have a local TLS certificate. You may want to use that for debugging purposes.

```shell  theme={null}
herd secured
```

This gives you a similar output to this:

```
+----------------------------+----------------------------+
| Site                       | Valid Until                |
+----------------------------+----------------------------+
| expose.dev.test            | 2024-08-10 12:07:38 GMT    |
| herd-templates.test        | 2024-09-05 25:12:77 GMT    |
| reverb-110.test            | 2024-09-11 13:44:56 GMT    |
| tinkerwell.app.test        | 2024-10-16 19:53:32 GMT    |
+----------------------------+----------------------------+
```
