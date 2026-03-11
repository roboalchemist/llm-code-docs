# Source: https://docs.axonius.com/docs/cylanceprotect.md

# CylancePROTECT

CylancePROTECT uses artificial intelligence to detect and protect against ransomware, advanced threats, fileless malware, and malicious documents.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Cylance Domain** *(required)* - Use either `protectapi.cylance.com` or  `protectapi.us.cylance.com`.\
   Note this value is different from the common domain, which is **protect.cylance.com**.
2. **Application ID** , **Application Secret** and **Tenant API Key** *(required)* - The application ID, secret and associated API Key created in the 'Integrations' section of the Cylance console. See details below.
3. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Cylance Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Cylance Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **Cylance Domain**.
4. **Tenant Tag** *(optional, default: empty)* - Automatically tag all devices discovered by the specific adapter server.
5. **Cylance Zones Include list** *(optional, default: empty)* - Specify a comma-separated list of Cylance zones.
   * If supplied, the connection for this adapter will only fetch devices associated with at least one of the zones provided in this list.
   * If not supplied, the connection for this adapter will fetch all devices from Cylance.
6. **Cylance Zones Exclude list** *(optional, default: empty)* - Specify a comma-separated list of Cylance zones.
   * If supplied, the connection for this adapter will not fetch devices associated with at least one of the zones provided in this list.
   * If not supplied, the connection for this adapter will fetch all devices from Cylance.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CylanceProtext.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CylanceProtext.png" />

## Create Application ID and Application Secret in CylancePROTECT

To create an Application ID and Application Secret:

1. On the Integration tab, click “Add Application.”
2. Specify a name (e.g., Axonius\_adapter), and check all the boxes in the “Read” column.  Then click “Save.”

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(146).png" />

3. A window will appear with the Application ID and the Application Secret.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(147).png" />

4. Copy the values into the Axonius UI, and the adapter is configured.

5. To get an API Key, from the **Settings** menu, select **Integrations** and copy the tenant ID.

<Callout icon="📘" theme="info">
  NOTE

  if you do not see an “Integrations” option in the Settings menu of your Cylance management console, please contact Cylance Support to have it enabled.
</Callout>

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(143).png" />

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(144).png" />

<br />

### Related Enforcement Action

* [Cylance - Delete Devices](/docs/cylance-delete-devices)

<br />