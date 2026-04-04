# Source: https://docs.api7.ai/apisix/networking/port-reference.md

# Port Reference

By default, APISIX exposes the following ports:

| Port   | Protocol | Description                                                                                                                                                                                           |
| ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `9080` | HTTP     | Listen for user requests.                                                                                                                                                                             |
| `9443` | HTTPS    | Listen for user requests with SSL enabled.                                                                                                                                                            |
| `9181` | PROXY    | Listen for HTTP traffic with PROXY protocol.                                                                                                                                                          |
| `9182` | PROXY    | Listen for HTTPS traffic with PROXY protocol.                                                                                                                                                         |
| `9090` | TCP      | Listen for requests to Control API.                                                                                                                                                                   |
| `9100` | TCP      | Listen for TCP traffic when [transport layer (L4) proxy](https://docs.api7.ai/apisix/how-to-guide/traffic-management/proxy-transport-layer-l4-traffic.md#enable-transport-layer-l4-proxy) is enabled. |
| `9200` | UDP      | Listen for UDP traffic when [transport layer (L4) proxy](https://docs.api7.ai/apisix/how-to-guide/traffic-management/proxy-transport-layer-l4-traffic.md#enable-transport-layer-l4-proxy) is enabled. |
| `9180` | HTTP(S)  | Listen for requests to Admin API.                                                                                                                                                                     |
| `9091` | HTTP     | The port where APISIX exports metrics for Prometheus.                                                                                                                                                 |
| `8443` | HTTPS    | The port for HTTPS traffic when `redirect` plugin is used to redirect HTTP traffic to HTTPS.                                                                                                          |

To learn more about how to change the default ports, see [configuration files](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample).
