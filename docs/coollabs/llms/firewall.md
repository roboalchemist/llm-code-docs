# Source: https://docs.coollabs.io/coolify/v3/firewall.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coollabs.io/llms.txt
> Use this file to discover all available pages before exploring further.

# null

You need to allow the following ports in your firewall:

* Coolify: `3000` (required)
* Reverse Proxy: `80, 443` (optional)
* [Public Port Range](./settings.md#public-port-range): `9000-9100` (optional)

<Warning>
  If you are using `Oracle Cloud free ARM server`, you need to allow these ports inside Oracle's Dashboard, otherwise you cannot reach your instance from the internet after installation.
</Warning>
