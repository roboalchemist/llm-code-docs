# Source: https://docs.axonius.com/docs/mend-io.md

# Mend.io

Mend.io is a software tool that provides automated open-source security and compliance management.

### Asset Types Fetched

* Devices, Vulnerabilities, SaaS Applications

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Email/Key and Organization ID

### APIs

Axonius uses the following APIs:

* [Findings - Project](https://api-docs.mend.io/platform/3.0/findings-project)
* [Get Organization Projects](https://api-docs.mend.io/platform/3.0/projects/getorganizationprojects)

### Permissions

To successfully make a GET request to `/api/v3/projects/{projectId}/findings` and retrieve the findings, the API key or authentication token you are using must be associated with a user role that has been granted the "Read Project Findings" permission within the Mend.io platform.

To successfully make a GET request to `/api/v3/projects` and retrieve a list of projects for the entire organization, the API key or authentication token you are using must be associated with a user role that has been granted the "Read Organization Projects" permission within the Mend.io platform.

#### Supported From Version

Supported from Axonius version 6.1.66

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Mend.io server.
2. **User Email** and **User Key** - The credentials for a user account that has the Required Permissions to fetch assets.
3. **Organization ID** - Specify your Mend.io organization ID.

![Mend.io.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Mend.io.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).