# Source: https://docs.axonius.com/docs/opswat-metaaccess.md

# OPSWAT MetaAccess

OPSWAT MetaAccess prevents risky devices from accessing local networks and cloud applications.

## Asset Types Fetched

* Devices
  , Aggregated Security Findings
  , SaaS Applications

## Parameters

1. **OPSWAT Domain** *(required, default: `https://gears.opswat.com`)* - The hostname or IP address of the OPSWAT MetaAccess server.
2. **Client Key** and **Client Secret** *(required)* - Client Key and Client Secret strings provided by OPSWAT MetaAccess. For details, see [APIs](#apis).
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **OPSWAT Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **OPSWAT Domain** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **OPSWAT Domain** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **OPSWAT Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **OPSWAT Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **OPSWAT Domain**.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(799).png" />

## APIs

Axonius uses the [OPSWAT MetaAccess API](https://onlinehelp.opswat.com/metaaccess/1._MetaAccess_APIs.html).

To work with OPSWAT MetaAccess APIs:

1. Set up a MetaAccess account in order to begin registering your applications to our platform.
2. Provide the following details:
   1. Application name.
   2. Application description - purpose of the application.
   3. Application URL - place where your Axonius instance resides.
   4. Callback URL - where user is redirected after authorizing application for access to the account.
3. Following submission, applications are confirmed and **Client Key** and **Client Secret** strings are provided. These keys are unique and should remain confidential.