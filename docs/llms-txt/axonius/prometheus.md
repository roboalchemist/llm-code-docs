# Source: https://docs.axonius.com/docs/prometheus.md

# Prometheus

Prometheus is a monitoring system that offers time-series data collection and alerting.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

#### APIs

Axonius uses the [Prometheus HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/).

#### Supported From Version

Supported from Axonius version 6.1.64

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

* **Host Name or IP Address** - The hostname or IP address of the Prometheus server.

![Prometheus.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Prometheus.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).