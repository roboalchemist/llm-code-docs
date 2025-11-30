# Source: https://www.electronjs.org/docs/latest/api/structures/proxy-config

# ProxyConfig Object

- `mode` string (optional) - The proxy mode. Should be one of `direct`, `auto_detect`, `pac_script`, `fixed_servers` or `system`. Defaults to `pac_script` proxy mode if `pacScript` option is specified otherwise defaults to `fixed_servers`.
  - `direct` - In direct mode all connections are created directly, without any proxy involved.
  - `auto_detect` - In auto_detect mode the proxy configuration is determined by a PAC script that can be downloaded at [http://wpad/wpad.dat](http://wpad/wpad.dat).
  - `pac_script` - In pac_script mode the proxy configuration is determined by a PAC script that is retrieved from the URL specified in the `pacScript`. This is the default mode if `pacScript` is specified.
  - `fixed_servers` - In fixed_servers mode the proxy configuration is specified in `proxyRules`. This is the default mode if `proxyRules` is specified.
  - `system` - In system mode the proxy configuration is taken from the operating system. Note that the system mode is different from setting no proxy configuration. In the latter case, Electron falls back to the system settings only if no command-line options influence the proxy configuration.
- `pacScript` string (optional) - The URL associated with the PAC file.
- `proxyRules` string (optional) - Rules indicating which proxies to use.
- `proxyBypassRules` string (optional) - Rules indicating which URLs should bypass the proxy settings.

When `mode` is unspecified, `pacScript` and `proxyRules` are provided together, the `proxyRules` option is ignored and `pacScript` configuration is applied.

The `proxyRules` has to follow the rules below:

``` 
proxyRules = schemeProxies[";"<schemeProxies>]
schemeProxies = [<urlScheme>"="]<proxyURIList>
urlScheme = "http" | "https" | "ftp" | "socks"
proxyURIList = <proxyURL>[","<proxyURIList>]
proxyURL = [<proxyScheme>"://"]<proxyHost>[":"<proxyPort>]
```

For example:

- `http=foopy:80;ftp=foopy2` - Use HTTP proxy `foopy:80` for `http://` URLs, and HTTP proxy `foopy2:80` for `ftp://` URLs.
- `foopy:80` - Use HTTP proxy `foopy:80` for all URLs.
- `foopy:80,bar,direct://` - Use HTTP proxy `foopy:80` for all URLs, failing over to `bar` if `foopy:80` is unavailable, and after that using no proxy.
- `socks4://foopy` - Use SOCKS v4 proxy `foopy:1080` for all URLs.
- `http=foopy,socks5://bar.com` - Use HTTP proxy `foopy` for http URLs, and fail over to the SOCKS5 proxy `bar.com` if `foopy` is unavailable.
- `http=foopy,direct://` - Use HTTP proxy `foopy` for http URLs, and use no proxy if `foopy` is unavailable.
- `http=foopy;socks=foopy2` - Use HTTP proxy `foopy` for http URLs, and use `socks4://foopy2` for all other URLs.

The `proxyBypassRules` is a comma separated list of rules described below:

- `[ URL_SCHEME "://" ] HOSTNAME_PATTERN [ ":" <port> ]`

  Match all hostnames that match the pattern HOSTNAME_PATTERN.

  Examples: \"foobar.com\", \"\*foobar.com\", \"\*.foobar.com\", \"\*foobar.com:99\", \"[https://x.\\\*.y.com:99](https://x.%5C*.y.com:99)\"

- `"." HOSTNAME_SUFFIX_PATTERN [ ":" PORT ]`

  Match a particular domain suffix.

  Examples: \".google.com\", \".com\", \"[http://.google.com](http://.google.com)\"

- `[ SCHEME "://" ] IP_LITERAL [ ":" PORT ]`

  Match URLs which are IP address literals.

  Examples: \"127.0.1\", \"\[0:0::1\]\", \"\[::1\]\", \"http://\[::1\]:99\"

- `IP_LITERAL "/" PREFIX_LENGTH_IN_BITS`

  Match any URL that is to an IP literal that falls between the given range. IP range is specified using CIDR notation.

  Examples: \"192.168.1.1/16\", \"fefe:13::abc/33\".

- `<local>`

  Match local addresses. The meaning of `<local>` is whether the host matches one of: \"127.0.0.1\", \"::1\", \"localhost\".

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/proxy-config.md)