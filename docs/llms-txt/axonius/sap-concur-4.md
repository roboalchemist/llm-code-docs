# Source: https://docs.axonius.com/docs/sap-concur-4.md

# SAP Concur 4.x

SAP Concur provides travel, expense and invoice management.
​

<Callout icon="📘" theme="info">
  Note

  This adapter supports SAP Concur API Version 4. If you are using SAP Concur API v3 use the [SAP Concur 3.x](/docs/sap-concur) adapter.
</Callout>

**Related Enforcement Actions**

* [Create User - SAP Concur 4](/docs/create-update-sap-concur-4-user)
* [Update User - SAP Concur 4](/docs/update-sap-concur-4-user)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
  ​

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SAP Concur server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Client ID** and **Client Secret** *(required)* - Provided by SAP when registering the application.
3. **Refresh Token** *(required)* - The token used for company level authentication. In order to retrieve the Refresh Token, send one of the following code options:

<Callout icon="📘" theme="info">
  Note

  * You will need to replace the values for: DOMAIN, CLIENT\_ID, CLIENT\_SECRET, COMPANY\_UUID, COMPANY\_AUTH\_TOKEN.

  * The Auth Token expires after 24 hours, so a new token is required if it is older than this.
</Callout>

**Multiple-line curl option**:
**Note**: This option works best on a Terminal (Linux/MacOS).

```
curl -X POST “https://DOMAIN/oauth2/v0/token” \
    -H “Content-Type: application/x-www-form-urlencoded” \
    -d “client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=password&username=COMPANY_UUID&password=COMPANY_AUTH_TOKEN&credtype=authtoken”
```

**One-line curl option**:
**Note**: This option works best for Windows Command Prompt.

```
curl -X POST "https://DOMAIN/oauth2/v0/token" -H "Content-Type: application/x-www-form-urlencoded" -d "client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=password&username=COMPANY_UUID&password=COMPANY_AUTH_TOKEN&credtype=authtoken"     
```

**PowerShell option**:
**Note**: This option works best in a PowerShell console/PowerShell ISE.

```
$headers = @{
    "Content-Type" = "application/x-www-form-urlencoded"
}

$body = @{
    client_id = "CLIENT_ID"
    client_secret = "CLIENT_SECRET"
    grant_type = "password"
    username= "Company UUID"
    password= "AUTH TOKEN"
    credtype = "authtoken"
}

$response = Invoke-RestMethod -Uri https://xx.api.domain.com/oauth2/v0/token -Method Post -Headers $headers -Body $body
$response
```

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SAP%20Concur%204.x](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAP%20Concur%204.x.png)

## APIs

Axonius uses the:

* [SAP Concur OAuth2 API](https://developer.concur.com/api-reference/authentication/getting-started.html#obtain-your-application-clientid-and-clientsecret-)

* [SAP Concur Identity v4 API](https://developer.concur.com/api-reference/profile/v4.identity.html)

## Required Ports

Axonius must be able to communicate with the value supplied in [Geo Location](#parameters) via the following ports:

* **TCP port 443**: (HTTPS default)

## Required Permissions

The following permissions are required:

* identity.user.ids.read
* identity.user.core.read
* identity.user.coresensitive.read
* identity.user.enterprise.read
* identity.user.sap.read

## Supported From Version

Supported from Axonius version 6.0