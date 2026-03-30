# Source: https://docs.axonius.com/docs/device42.md

# Device42

Device42 is a cloud-based CMDB that maps relationships and dependencies for physical and virtual machines, cloud servers and containers, network components, software, services, and applications.

<Callout icon="📘" theme="info">
  API

  Axonius uses the [Device42 API](https://api.device42.com/).
</Callout>

## Adapter Parameters

1. **Device42 Domain** *(required)* - The hostname of the Device42 server.

2. **User Name** and **Password** *(required)* - The user name and password for an account that has read access to the data to be fetched by the API.
   Device42 API enforces the role-based security that is created with the Device42 app. If you want a user to have access via the API, but not via the UI - deselect **'Staff Status'** for that user from **UI Tools** > **Admins & Permissions** > **Administrators**.
   For details on Device 42 roles and permissions, see [Device42 - Role-based Permissions and Access](https://docs.device42.com/administration/role-based-access-control/role-based-permissions-and-access/).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(362).png" />

<Callout icon="📘" theme="info">
  NOTE

  To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
</Callout>

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Category Include list** *(optional)* - Enter list of categories only from which devices will be fetched.

2. **Fetch only in service devices** - select this option to fetch only devices that their “In Service” status is true.

3. **Add software details** - Select this option to add the installed software details for each device

4. **Pull only latest software versions** - Select this option to fetch ONLY the latest versions of each software on the installed software page.

5. **Parse hostname from custom fields** - Select this option to parse the hostname from the Hostname custom field instead of the name field.

<Callout icon="📘" theme="info">
  NOTE

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>