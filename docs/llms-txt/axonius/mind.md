# Source: https://docs.axonius.com/docs/mind.md

# MIND

MIND is a data security platform that provides autonomous data loss prevention and insider risk management via AI-driven discovery, classification, and automated response.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### APIs

Axonius uses the MIND API.

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 7.0.8

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api.mind.io`)* - The hostname or IP address of the MIND server.
2. **API Token**  - An API Token associated with a user account that has permissions to fetch assets.
   **To obtain a token**:
   1. Navigate to **Settings** -> **API Tokens**.
   2. Click **Create token**.
   3. Provide a descriptive name such as "axonius-token" and set an appropriate expiration.
   4. Copy the API Token and click **Close**.

![MIND.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MIND.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).