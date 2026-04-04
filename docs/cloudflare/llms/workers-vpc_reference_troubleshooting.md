# Source: https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/index.md

---

title: Troubleshoot and debug · Cloudflare Workers VPC
description: Troubleshoot and debug errors commonly associated with Workers VPC.
lastUpdated: 2026-01-28T18:55:50.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/
  md: https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/index.md
---

Troubleshoot and debug errors commonly associated with Workers VPC.

## Connection errors

Workers VPC may return errors at runtime when connecting to private services through Cloudflare Tunnel.

### Tunnel errors

| Error Message | Details | Recommended fixes |
| - | - | - |
| `Error: ProxyError: dns_error` | DNS resolution failed when attempting to connect to your private service through the tunnel. | This error may occur if your `cloudflared` version is outdated. Ensure you are running `cloudflared` version 2025.7.0 or later (latest version recommended). See [Cloudflare Tunnel update instructions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/). |
| `Error: ProxyError: dns_error` | Cloudflare Tunnel may be configured with `http2` protocol (`TUNNEL_TRANSPORT_PROTOCOL:http2`), which works for Cloudflare Zero Trust [(see note)](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/#create-and-run-tunnel-cloudflared) traffic but prevents DNS resolution from Workers VPC. | Workers VPC requires Cloudflare Tunnel to connect using the [QUIC transport protocol](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cloudflared-parameters/run-parameters/#protocol). Ensure outbound UDP traffic on port 7844 is allowed through your firewall. |
| Requests not staying within VPC | Worker requests using `.fetch()` with a public hostname are routing out of the VPC to the hostname configured for the VPC Service. | Ensure your Worker code and the VPC Service use the internal VPC hostname for backend services, not a public hostname. |

## Permission errors

If you cannot view, create, or bind VPC Services and Tunnels in the dashboard or via Wrangler, ensure your user has the required roles.

Workers VPC uses the following account roles:

* `Connectivity Directory Read` to view Workers VPC Services and Tunnels.
* `Connectivity Directory Bind` to list/read services and bind them in Workers.
* `Connectivity Directory Admin` to create, update, and delete services.

For role definitions, refer to [Roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#account-scoped-roles).

If your roles were recently updated and commands are still failing, refresh Wrangler authentication:

```sh
npx wrangler logout
npx wrangler login
```

If you authenticate with an API token (`CLOUDFLARE_API_TOKEN`), ensure the token belongs to a user with the required roles.
