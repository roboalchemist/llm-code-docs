# Source: https://docs.axonius.com/docs/honeywell-tdc-3000.md

# Honeywell TDC 3000

Honeywell TDC 3000 is a legacy Distributed Control System (DCS) used in industrial automation to manage and monitor complex process operations. It features modular controllers, proprietary networks, and operator stations for real-time control and visualization.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

### Permissions

To retrieve activity session data from the Honeywell TDC3000 system, the requesting account or interface must have adequate permissions to:

* Access the system’s Event Journal or Historical Data Interface (HDI)
* View operator session logs and console activity records
* Query system-level diagnostics and timestamped user actions

If the account lacks the necessary access rights, session data may be incomplete, inaccessible, or return access-denied errors.

**Recommended Steps**:

1. Confirm the user role or service account has "Read" or "Audit" access to the TDC3000 Event Journal or equivalent subsystem.

2. Ensure access to the Data Hiway or LCN interface used for exporting session data.

3. Verify that any firewall or DCS gateway policies allow remote logging or journal access operations.

#### Supported From Version

Supported from Axonius version 6.1.70

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

* **File Path** - Select a local CSV file to import. Click **Upload File** to manually upload the file.

![Honeywell TDC 3000.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Honeywell%20TDC%203000.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).