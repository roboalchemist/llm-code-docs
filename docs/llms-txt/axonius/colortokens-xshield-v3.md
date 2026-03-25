# Source: https://docs.axonius.com/docs/colortokens-xshield-v3.md

# ColorTokens Xshield

ColorTokens Xshield is a cybersecurity platform that offers zero trust security and micro-segmentation solutions.

This instance is tailored for users in the Sydney (Australia) region.

### Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User ID, Tenant ID, Fingerprint, Private Key

### APIs

Axonius uses the [Xshield API](https://api-syd.colortokens.com/docs#tag/agents/operation/ListAgents).

### Permissions

The following permissions are required:

* **List assets**:

```json
{"permission":"LIST_ASSET","permissionScope":["ADMIN","USER"]}
```

* **List vulnerabilities per asset**:

```json
{"permission":"READ_ASSET","permissionScope":["AGENT","ADMIN","USER"]}
```

To fetch asset data from the Xshield API, the API key used must be associated with a user account that has the necessary permissions. Specifically, the account should have read access to asset information. The "Viewer" role in Xshield provides the most restricted access, allowing users to view all data within Xshield, making it suitable for integration purposes where data retrieval is required without modification capabilities.

#### Supported From Version

Supported from Axonius version 7.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the ColorTokens Xshield server.
2. **User ID** - The user ID for API authentication. To get the value, see **https\://`{ENV_NAME}`.colortokens.com/api-keys** and click **View Credentials**.
3. **Tenant ID** -  Your tenant ID in ColorTokens. To get the value, see **https\://`{ENV_NAME}`.colortokens.com/api-keys** and click **View Credentials**.
4. **Private Key** - Upload the private key file generated for API authentication.
   **Obtaining and setting up the private key**:
   1. Click on your profile icon in the top-right corner.
   2. Select **Manage APIs**.
   3. Create a new API key and generate it in your browser.
   4. Download the private key.
   5. Remember to save your changes while ensuring the private-public key pair is in PEM format.
5. **Fingerprint** - The private key fingerprint. Once the private key is generated and saved, you should be able to see **Fingerprint** for the public key that was added to this user. To get the value, see **https\://`{ENV_NAME}`.colortokens.com/api-keys**

<Image alt="ColorTokens Xshield.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ColorTokens%20Xshield.png" />

### Optional Parameters

1. **Private Key Passphrase** - Enter the decryption passphrase for the private key if the private key is encrypted.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).