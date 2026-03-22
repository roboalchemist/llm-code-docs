# Source: https://kreya.app/docs/proxy.md

# Proxy

Kreya uses the system proxy settings by default. It respects the OS settings, which includes environment variables. If your system proxy settings are not accurate, you can customize the settings manually. The active proxy settings apply to all requests made by Kreya.

## Proxy environment variables[​](#proxy-environment-variables "Direct link to Proxy environment variables")

| Environment Variable | Description                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `HTTP_PROXY`         | Proxy server used for HTTP requests.                                                                                        |
| `HTTPS_PROXY`        | Proxy server used for HTTPS requests.                                                                                       |
| `ALL_PROXY`          | Proxy server used for HTTP and HTTPS request, if `HTTP_PROXY` and `HTTPS_PROXY` are not set.                                |
| `NO_PROXY`           | Comma-separated list of hostnames that should be excluded from proxying. Use a leading dot if you want to match a subdomain |

**Examples**:

* `HTTP_PROXY=http://127.0.0.1:1234`
* `HTTP_PROXY=http://username:password@127.0.0.1:1234`
* `NO_PROXY=.example-api.kreya.app`

## Custom proxy settings [Enterprise](/pricing.md)[​](#custom-proxy-settings- "Direct link to custom-proxy-settings-")

Kreya supports custom proxy settings with the Enterprise plan. You may even define multiple different proxy settings, which allows you to easily switch between them later on.

Kreya supports the following protocols for proxies:

* `HTTP`
* `HTTPS`
* `SOCKS4`
* `SOCKS4A`
* `SOCKS5`

![Creating a custom proxy](/assets/ideal-img/example-proxy.fdef767.400.png)

## Switch between proxy settings [Enterprise](/pricing.md)[​](#switch-between-proxy-settings- "Direct link to switch-between-proxy-settings-")

Two proxy settings are always pre-defined by Kreya:

* None: Do not use a proxy
* System: Use the OS system proxy settings (the default)

Custom proxy settings will also be selectable once created. Easily switch between proxy settings by clicking the "globe" icon at the lower right corner:

![Switching the active proxy by clicking the globe icon in the lower right corner](/assets/ideal-img/set-active-proxy.6ae9fa4.400.png)
