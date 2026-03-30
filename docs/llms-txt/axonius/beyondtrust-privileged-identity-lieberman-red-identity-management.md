# Source: https://docs.axonius.com/docs/beyondtrust-privileged-identity-lieberman-red-identity-management.md

# BeyondTrust Privileged Identity (Lieberman RED Identity Management)

BeyondTrust Privileged Identity (formerly Lieberman RED Identity Management) is a password management solution that helps companies secure, manage, and administer credentials for privileged users and IT vendors.

## Types of Assets Fetched

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the BeyondTrust Privileged Identity server.

2. **LoginType** *(required)* - The login type of the authentication. Valid values:
   * NativeStaticAccount (Privileged Identity explicit accounts) or FullyQualifiedAccount.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![BeyondTrust Privileged Identity](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrust%20Privileged%20Identity.png)

## APIs

Axonius uses the [Privileged Identity REST API](https://www.beyondtrust.com/docs/archive/privileged-identity/documents/5-5-4/pi-rest-api-5-5-4.pdf).