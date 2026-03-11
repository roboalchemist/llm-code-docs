# Source: https://docs.axonius.com/docs/docebo.md

# Docebo

Docebo is a learning management system that offers e-learning solutions for training and development.

### Asset Types Fetched

* Devices, Users, Groups, Organizational Units, Permissions, SaaS Applications, Application Add-Ons, Application Extensions, Admin Managed Extensions, User Initiated Extensions, Application Extension Instances, Admin Managed Extension Instances, User Initiated Extension Instances, Application Add-Ons Instances, Application Keys

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Oauth2 authentication using a password

### APIs

Axonius uses the [Docebo API](https://help.docebo.com/hc/en-us/articles/360020127899-Activating-and-managing-the-API-and-SSO-app).

### Permissions

The account used must have sufficient permissions to read users, courses, and enrollments in order to fetch assets.

#### Supported From Version

Supported from Axonius version 7.0.8

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Docebo server.
2. **OAuth2 Client ID** and **OAuth2 Client Secret** - For information on how to retrieve these parameters, see the [Docebo documentation](https://help.docebo.com/hc/en-us/articles/360020082060-APIs-authentication#h_01HJ6PBHP8XAXZJJRSEBVF1VE3).
3. **Username** and **Password** -  Credentials to for Docebo API

<br />

![Docebo adapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Docebo.png)

![](https://github.com/Axonius/ax-docs-pub/blob/main/img/adapters/Docebo.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Related Enforcement Actions

* [ Docebo - Create User](https://docs.axonius.com/axonius-help-docs/docs/docebo-create-user-draft)
* [Docebo - Suspend User](https://docs.axonius.com/axonius-help-docs/docs/docebo-suspend-user-draftr)
* [Docebo - Update User](https://docs.axonius.com/axonius-help-docs/docs/docebo-update-user-draft)
* [Docebo - Assign User to Group](https://docs.axonius.com/axonius-help-docs/docs/docebo-assig-user-to-group-draft)