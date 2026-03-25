# Source: https://docs.axonius.com/docs/ngrok.md

# ngrok

ngrok is a secure tunnel service that provides remote access to local servers.

### Asset Types Fetched

* Users, Network/Firewall Rules

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

### APIs

Axonius uses the following APIs:

* [List Application Users](https://ngrok.com/docs/api/resources/application-users/#list-application-users)
* [IP Policies](https://ngrok.com/docs/api/resources/ip-policies/)

### Permissions

To successfully retrieve activity-related data (like sessions, events, abuse reports), the API token must be tied to an account with:

* Authorization scope via the `Authorization: Bearer <API_KEY>` header that grants access to organization-level resources
* Enterprise-tier IP restrictions, since IP-based API access control is only supported on the Enterprise plan
* Explicit rights to fetch:
  * Application sessions (`/application_sessions`)
  * Tunnel sessions (`/tunnel_sessions`)
  * Event sources (`/event_sources`), destinations (`/event_destinations`), and subscriptions (`/event_subscriptions`)
  * Abuse reports (`/abuse_reports`), noting that this endpoint is restricted to authorized accounts only

If the API key isn’t associated with at least Admin-level or Full Read privileges for these resources, you'll likely encounter:

* 403 Forbidden responses
* Empty or incomplete datasets
* Access-denied errors for specific endpoints like `/abuse_reports` or event-related retrievals

**Recommended Steps**:

1. Generate the API key from a user with Admin or equivalent roles in the ngrok Organization Dashboard.

2. Verify the key has privileges for:
   * Listing session data from `/application_sessions` and `/tunnel_sessions`
   * Reading event configurations from `all /event_*` endpoints
   * Accessing `/abuse_reports`
   * Managing IP restrictions via the API (Enterprise plan)

3. Double-check the account’s plan level to confirm IP restrictions and abuse-report visibility are enabled.

4. Test each retrieval endpoint manually (e.g., `GET /application_sessions`) to ensure no permission errors are returned.

#### Supported From Version

Supported from Axonius version 6.1.71

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the ngrok server.
2. **API Key**  - An API Key associated with a user account that has the Required Permissions to fetch assets. For information, see [Authentication](https://ngrok.com/docs/api/#authentication).

<Image alt="ngrok.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ngrok.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).