# Source: https://docs.axonius.com/docs/awake-security.md

# Awake Security

Awake Security (Arista NDR) is a network traffic analysis solution capable of detecting and visualizing behavioral, mal-intent and compliance incidents.

## Use Cases the Adapter Solves

The Awake Security adapter could be used in various use cases, including:

* **Add Network-Discovered Devices to the Inventory** - Fetch assets identified by the Awake Security passive network analysis to discover unmanaged devices, IoT devices, or devices without a management agent.
* **Prioritize Network Threats** - Combine the Awake Security threat data with asset details (owner, software, vulnerabilities) to help prioritize risk and response.
* **Query for Network Anomalies** - Identify devices with unusual network behavior or policy violations as detected by Awake Security.
* **Configure Automated Actions on Threat Detection** - Use the Awake Security threat or incident data as a trigger for Enforcement Center actions, such as tagging an asset or creating a service desk ticket.

## Asset Types Fetched

This Awake Security adapter fetches the following types of assets:

* Devices

## Data Retrieved through the Adapter

The following data is retrieved through the Awake Security adapter:

* **Network Details** - IP address (IPv4, IPv6), MAC address, and hostname.
* **Device Identification** - Device type (for example: IoT, printer, server), manufacturer, and operating system (as observed from network traffic).
* **Location** - Network segment or VLAN on which the device was seen.
* **Threat and Incident Data** - Associated threat scores, risk levels, and specific incident/threat names.
* **Activity Details** - Protocols used (for example: SSH, RDP), as well as domains or IP addresses communicated with.
* **First/Last Seen** - Timestamps for when the device was first and last observed on the network.

## Before You Begin

### Required Ports

* TCP port 443

### Authentication Methods

You must have the **Username** and **Password** of a user account on the Awake Security appliance.

### Required Permissions

The Awake Security appliance user account must have a role with **Read-Only** access to the Awake Security data.

### APIs

The Awake Security adapter connects to the Awake Appliance API. The API resources are hosted under the `/awakeapi/v1/` path prefix.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the Awake Security server that Axonius can communicate with via the [Required Ports](#required-ports). Specify either `http://` or `https://` in the beginning of the hostname or IP address.
2. **User Name** and **Password** - Enter the credentials for a user account that has permission to fetch assets.

<Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Awake_Security_Add_connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **Scan History (Days)** - Enter the number of days that defines the period for fetching data with this adapter. You can enter a number of days or keep the default value of 30 days.
3. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
5. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).