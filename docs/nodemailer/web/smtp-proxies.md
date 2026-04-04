# Source: https://nodemailer.com/smtp/proxies

Title: Proxy support | Nodemailer

URL Source: https://nodemailer.com/smtp/proxies

Markdown Content:
Nodemailer can route [SMTP](https://nodemailer.com/smtp) connections **through an outbound proxy server**. This is useful when your application runs behind a corporate firewall or when you need to route traffic through a specific network path. Proxy support works with both single connections and [pooled connections](https://nodemailer.com/smtp/pooled).

Nodemailer includes built-in support for **HTTP CONNECT** proxies. For **SOCKS4/4a/5** proxies or other protocols, you have two options:

1. Install the [`socks`](https://www.npmjs.com/package/socks) package and Nodemailer will use it automatically.
2. Write a custom proxy handler function for specialized requirements.

Quick start[​](https://nodemailer.com/smtp/proxies#quick-start "Direct link to Quick start")
--------------------------------------------------------------------------------------------

To use a proxy, set the `proxy` option to a URL string when creating your transporter. Nodemailer parses the URL and automatically determines how to establish the tunnel.

`const nodemailer = require("nodemailer");const transporter = nodemailer.createTransport({  host: "smtp.example.com",  port: 465,  secure: true,  proxy: "http://proxy.example.test:3128", // HTTP proxy URL});`

HTTP CONNECT proxies[​](https://nodemailer.com/smtp/proxies#http-connect-proxies "Direct link to HTTP CONNECT proxies")
-----------------------------------------------------------------------------------------------------------------------

HTTP CONNECT proxies work out of the box with **no additional dependencies**. Nodemailer supports both `http://` and `https://` proxy URLs. If your proxy requires authentication, include the credentials in the URL (for example, `http://user:pass@proxy.example.com:3128`).

`const transporter = nodemailer.createTransport({  host: "smtp.example.com",  port: 465,  secure: true,  proxy: process.env.HTTP_PROXY, // You can also use HTTPS_PROXY});`

SOCKS proxies[​](https://nodemailer.com/smtp/proxies#socks-proxies "Direct link to SOCKS proxies")
--------------------------------------------------------------------------------------------------

SOCKS proxy support is **not bundled** with Nodemailer to keep the package lightweight. To use SOCKS proxies, you need to install the `socks` package separately and register it with the transporter.

First, install the package:

`npm install socks --save`

Then configure the transporter and register the SOCKS module:

`const transporter = nodemailer.createTransport({  host: "smtp.example.com",  port: 465,  secure: true,  proxy: "socks5://127.0.0.1:1080",});// Register the socks module so Nodemailer can use ittransporter.set("proxy_socks_module", require("socks"));`

### Supported URL protocols[​](https://nodemailer.com/smtp/proxies#supported-url-protocols "Direct link to Supported URL protocols")

Use one of the following URL schemes depending on your proxy type:

| Protocol | Proxy type | Description |
| --- | --- | --- |
| `socks4:` | SOCKS4 | Basic SOCKS4 protocol |
| `socks4a:` | SOCKS4a | SOCKS4 with remote DNS resolution |
| `socks5:` | SOCKS5 | SOCKS5 with authentication and IPv6 support |
| `socks:` | SOCKS5 | Alias for `socks5:` |

### Local testing with SSH[​](https://nodemailer.com/smtp/proxies#local-testing-with-ssh "Direct link to Local testing with SSH")

You can create a quick SOCKS5 proxy for testing by using SSH dynamic port forwarding. This tunnels all traffic through an SSH connection to a remote server.

Run this command to start the proxy:

`ssh -N -D 0.0.0.0:1080 user@remote.host`

The `-N` flag tells SSH not to execute a remote command (just forward ports), and `-D 0.0.0.0:1080` creates a SOCKS proxy listening on port 1080.

Then configure Nodemailer to use this proxy:

`proxy: "socks5://localhost:1080"`

Custom proxy handlers[​](https://nodemailer.com/smtp/proxies#custom-proxy-handlers "Direct link to Custom proxy handlers")
--------------------------------------------------------------------------------------------------------------------------

If you need special authentication, a proprietary protocol, or any other custom proxy logic, you can write your own handler function. This gives you full control over how the socket connection is established.

To register a custom handler, use `transporter.set()` with a key in the format `proxy_handler_<protocol>`, where `<protocol>` matches the URL scheme you use in the `proxy` option.

`const transporter = nodemailer.createTransport({  host: "smtp.example.com",  port: 465,  secure: true,  proxy: "myproxy://127.0.0.1:9999",});// Register a handler for the "myproxy:" URL schemetransporter.set("proxy_handler_myproxy", (proxy, options, done) => {  const net = require("net");  console.log("Connecting to proxy at %s:%s", proxy.hostname, proxy.port);  const socket = net.connect(proxy.port, proxy.hostname, () => {    // Perform any custom handshake with your proxy here...    // Return the established socket to Nodemailer    done(null, { connection: socket });  });});`

The handler function receives three arguments:

* `proxy` - A parsed URL object containing the proxy address details
* `options` - Connection options including the target `host` and `port`
* `done` - A callback to invoke with `(error, result)` when the connection is ready

### Pre-encrypted connections[​](https://nodemailer.com/smtp/proxies#pre-encrypted-connections "Direct link to Pre-encrypted connections")

If your proxy connection is **already encrypted** (for example, you used `tls.connect()` instead of `net.connect()`), you must set `secured: true` in the result object. This tells Nodemailer that the connection is already secure and it should not attempt a STARTTLS upgrade.

`const tls = require("tls");transporter.set("proxy_handler_myproxys", (proxy, options, done) => {  const socket = tls.connect(proxy.port, proxy.hostname, () => {    // The secured flag indicates the connection is already TLS-encrypted    done(null, { connection: socket, secured: true });  });});`
