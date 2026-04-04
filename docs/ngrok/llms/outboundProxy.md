# Source: https://ngrok.com/docs/using-ngrok-with/outboundProxy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with an outbound proxy

> Learn how to configure ngrok to work through HTTP or SOCKS5 outbound proxies using environment variables or configuration files.

ngrok works correctly through an HTTP or SOCKS5 proxy. ngrok respects the standard unix environment variable `http_proxy`. You may also set proxy configuration explicitly in the ngrok configuration file:

* [Set the configuration variable `proxy_url`](/agent/config/v3/#proxy-url)


Built with [Mintlify](https://mintlify.com).