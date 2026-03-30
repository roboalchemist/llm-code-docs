# Source: https://docs.axonius.com/docs/gateway-health-status.md

# Gateway Health Status

Axonius performs health checks on gateways to ensure they are functioning properly and to notify you when there is a connection problem.

Health status is displayed in the Health Status field of the Gateways page.

<Image alt="GatewaysPageConnectionStatus.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/GatewaysPageConnectionStatus.png" />

Axonius performs the following health checks on gateways:

* VPN connectivity check
* Traffic forwarding
* DNS resolution

The following health statuses are assigned to gateways:

| Connection Status            | Description                                                | Condition                                                    |
| :--------------------------- | :--------------------------------------------------------- | :----------------------------------------------------------- |
| **Healthy**                  | All internal gateway functionality is working properly.    | All health checks work properly                              |
| **Unhealthy (Connectivity)** | The gateway agent is connected to OpenVPN but unreachable. | The gateway agent is connected to OpenVPN but unreachable.   |
| **Disconnected**             | Gateway is disconnected from OpenVPN.                      | Only available post the tunnel’s initial connection attempt. |
| **Pending**                  | Waiting for initial gateway connection.                    | On tunnel creation, before the initial connection attempt.   |

<br />