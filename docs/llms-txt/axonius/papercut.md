# Source: https://docs.axonius.com/docs/papercut.md

# PaperCut

PaperCut is a print management solution that provides print job tracking and reporting.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* -
   1. Enter the hostname or IP address of the PaperCut server by using one of the following formats:
   * `https://[hostname_or_IP]:9192`
   * `http://[hostname_or_IP]:9191` (where `hostname_or_ip` is a specific hostname or IP address)
   2. Add the hostname or IP address to the **Allowed list** in PaperCut by navigating to **Options** `>` **Advanced** `>` **Allowed XML Web Services callers**. Then add the IP address of the Axonius instance into the comma-separated list and save the configuration.

2. **API Token** *(required)* - An API Token associated with a user account that has permissions to fetch assets.
   To generate an API Token, see [Generate an API Token](#generate-an-api-token).

3. **API Health Token** *(required)* - An API Health Token used to obtain the status of each device for the PaperCut team. For information about configuration, see [Configure PaperCut NG/MF system health monitoring](https://www.papercut.com/help/manuals/ng-mf/common/tools-monitor-system-health-api-configure/).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="PaperCut.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PaperCut.png" />

## APIs

Axonius uses the [XML Web Services API](https://www.papercut.com/help/manuals/ng-mf/common/tools-web-services/).

## Generate an API Token

**To generate an API token**

1. Go to **Papercut Console** `>` **Options** `>` **Config Editor (Advanced)** in the right sidebar.
2. Search for the following token: `auth.webservices.auth-token`
3. If the token doesn't exist, create it with any alphanumeric value.
4. Paste the generated value to the **API Key** parameter in the Axonius adapter.

### PaperCut Security

The PaperCut Web Services APIs provide full access to the system’s internals so they must be secured. PaperCut NG/MF secures access using two security layers:

* IP address level security .
* Authentication tokens - required for each method call .

The IP address level security is used to control which systems, denoted by IP addresses, are allowed to connect to the server and call the APIs. By default, this is restricted to localhost (127.0.0.1) only. Since Axonius is making use of the API and resides on another system, then the Axonius system’s IP address must be added to  the list of approved addresses under **Options** `>` **Advanced** `>` **Allowed XML Web Services callers** on PaperCut.