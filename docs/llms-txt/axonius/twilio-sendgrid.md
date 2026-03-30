# Source: https://docs.axonius.com/docs/twilio-sendgrid.md

# Twilio SendGrid

Twilio SendGrid is a cloud-based email marketing tool that assists marketers and developers with campaign management and audience engagement.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

### Permissions

The following permissions are required:

* The `list accounts /v3/partners/accounts` endpoint requires a reseller membership, or a Pro/Premier plan. Read more on [List Accounts API](https://www.twilio.com/docs/sendgrid/api-reference/account-provisioning-api-account-operations/list-accounts).
* To fetch `all teammates: /v3/teammates`, the `teammates.read` permission is required.

### APIs

Axonius uses the [Twilio SendGrid v3 Web API](https://www.twilio.com/docs/sendgrid/api-reference).

#### Supported From Version

Supported from Axonius version 6.1.64

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Twilio SendGrid server.
2. **API Key**  - An API Key associated with a user account that has the  Required Permissions to fetch assets. For more information, see [API Keys](https://www.twilio.com/docs/sendgrid/api-reference/how-to-use-the-sendgrid-v3-api/authentication#api-keys).

<Image alt="Twilio SendGrid.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Twilio%20SendGrid.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).