# Source: https://docs.axonius.com/docs/manage-gateways.md

# Managing Gateways

Use the **Gateways** page to add and manage Axonius gateways.

An Axonius gateway enables the establishment of a link between an internal network and the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud)

The Axonius-hosted (SaaS) instance resides in the cloud and is not part of your organization's internal network. Axonius securely fetches data from the organization's data sources, known as adapters. To connect adapters that are only accessible by an internal network or segregated network (for Customer-hosted (on-premises / private cloud)), you must configure and install a gateway on a server that has access to those sources.

To view and manage gateways, users must have the following permissions:

**View** -  Allows users to view the Gateways page and gateway details.

**Manage** - In addition to view permissions, allows users to create and edit gateways.

For more details on installing an Axonius gateway, see [Installing Axonius Gateway](/docs/installing-axonius-gateway).

**To access the Gateways page:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **System**, and select **Gateways**.

The page displays the list of existing gateways, and each gateway's details and connection status.

![ManageGateways.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageGateways\(1\).png)

The Gateways table provides the following information about gateways:

* **Gateway ID** - The internal ID of the gateway. When the gateway is configured as the default gateway, 'default' is displayed next to the ID.
* **Gateway Name** - The name of the gateway.
* **Connection Status** - Indicates the health status of the gateway. See [Gateway Health Status](https://docs.axonius.com/axonius-help-docs/docs/gateway-health-status).
* **Host IP** - The IP address of the Axonius instance where the gateway is installed. For example:
  * If the Axonius instance IP address is `1.2.3.4`, and
  * The IP address of the machine where the gateway is installed is `5.6.7.8`
  * Then, the **Host IP** value will be `5.6.7.8`
* **First Connection Time** - The date and time when the gateway first connected with the Axonius instance.
* **Last Status Init** - The data and time when the gateway status was last updated.

## Adding a New Gateway

**To add a new gateway:**

1. Install the gateway installation package based on the instructions described in [Installing Axonius Gateway](/docs/installing-axonius-gateway).

Once the installation is completed and a gateway is successfully connected, you can configure the adapter connection to use the new gateway. For details, see [Configure and connect adapters to use the Axonius gateway](/docs/installing-axonius-gateway#5-configure-and-connect-adapters-to-use-an-axonius-gateway).

## Editing an Existing Gateway

**To edit an existing gateway:**

1. From the **Gateways** page, click an existing **Gateway Record**. The Gateway connection drawer appears.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditGatewayUPdated.png)

2. Click the **Edit** ( ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(696\).png) ) icon.

3. Edit the following gateway settings, as required: **Gateway name**, **Gateway status notification**, **Proxy settings**

4. Click **Save**.

<Callout icon="📘" theme="info">
  NOTE

  If the **Proxy Settings** have been changed, it is necessary to reinstall the Gateway. For more details, see [Installing Axonius Gateway](/docs/installing-axonius-gateway).
</Callout>

## Rotating the Gateway Certificate

You can rotate the gateway certificate for security or compliance purposes, or if the system displays a message that your gateway certificate has expired or is about to expire.

**To rotate the gateway certificate:**

1. On the **Gateways** page, click the gateway whose certificate you want to rotate, the gateway details drawer opens.
2. Click the **Rotate Gateway Certificate** icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Regnerate%20Tunnel.png)  the system tells you that you are about to rotate the certificate.
3. Click **Rotate Certificate** to confirm the message.
4. An updated certificate is generated. The system displays a message that the certificate rotation was successful. The gateway is then set to a pending state.
5. Click on the gateway again, the **Gateway** drawer opens. Click the download button to download the gateway installation package.
6. Follow instructions in step 4 of the **Installing Axonius Gateway** guide -[Install the Gateway Installation Package](/docs/installing-axonius-gateway#4-install-the-gateway-installation-package) -  to install the package. The gateway is then connected using the updated certificate.

## Deleting a Gateway

In order to delete an existing gateway, the following conditions should apply:

* The gateway is not used to access existing Adapter connections.
* The gateway is not used to access existing Enforcement Actions.
* The gateway status is disconnected.

**To remove a gateway:**

1. From the **Gateways** page, click an existing **Gateway Record**. The gateway connection drawer appears.
2. In the gateway connection drawer header, click the **Delete** ( ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(695\).png)) icon.
   * If the selected gateway is in use by at least one adapter connection or Enforcement Action, a notification informs: *This Gateway is used by at least one Adapter Connection/Enforcement Action and cannot be deleted. Reconfigure the Adapter Connections/Enforcement Actions to use another Gateway and try again.*

## Setting a Default Gateway

The default gateway is used by the system to connect to servers that are only accessible by **an internal network** such as LDAP servers and SMTP servers.

**To set a default gateway:**

1. From the **Gateways**  page, click an existing **Gateway Record**. The gateway connection drawer appears.

2. Click the **Edit** ( ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(696\).png) ) icon.

3. Select the **Set as default Gateway connection** checkbox to define the gateway as the system's default gateway.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SetAs%20Default%20gateway%20connection.png)

4. Click **Save**.

## Using a Gateway to Connect to Adapter Connection

For details, see [Configure and connect adapters to use the Axonius Gateway](/docs/installing-axonius-gateway#5-configure-and-connect-adapters-to-use-an-axonius-gateway).

## Setting a Backup Gateway

You can select backup gateways that Axonius will use if the primary gateway is unavailable. Axonius selects the next available gateway. Multiple backup gateways can be configured.

**To set a backup gateway:**

1. From the **Gateways**  page, select a gateway. The gateway connection drawer appears.
2. Click the **Edit** ( ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(696\).png) ) icon.
3. Under **Set Backup Gateway**, select one or more gateways from the **Backup Gateway** list. You can select multiple gateways.

<Image align="center" alt="SetBackupGatewayExisting.png" width="550px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SetBackupGatewayExisting.png" />

4. Click **Save**.

## Upgrading a Gateway

When the Axonius instance is upgraded, it is recommended to upgrade all the gateways connected to that instance.

**To upgrade a gateway:**

1. Shut down the current gateway.
2. Install the newer gateway using the installer. See [Installing Axonius Gateway](https://docs.axonius.com/axonius-help-docs/docs/installing-axonius-gateway).

### Gateway Upgrade Notifications

Axonius can send a weekly notification when at least one installed gateway can be updated. The notification is sent when the version of the gateway agent for the Axonius instance is higher than at least one of the running gateway versions. Notifications can be send via email or webhook as configured in [Configuring Notification Settings](https://docs.axonius.com/axonius-help-docs/docs/configuring-notification-settings).

Additionally, a persistent banner is displayed on the Gateways page and in the gateway’s details drawer. See [System Warnings](https://docs.axonius.com/axonius-help-docs/docs/system-warnings#gateway-issues).

![GatewayPageUpdateBanner.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/GatewayPageUpdateBanner.png)

<Image align="center" alt="GatewayDrawerUpdateBanner.png" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/GatewayDrawerUpdateBanner.png" />

#### Example Email Notification

Message subject: One or more gateways are running an outdated version.

Message content:

```
Please upgrade the following gateways to the latest version (1.0.11):
- Gateway_1 (ID: tunnel1) current: 1.0.5
- Gateway_2 (ID: tunnel2) current: unknown
```

#### Example Webhook Message

Message content:

```
One or more gateways are running an outdated agent version.
Please upgrade the following gateways to the latest version (1.0.11):
- Gateway_1 (ID: tunnel1) current: 1.0.5
- Gateway_2 (ID: tunnel2) current: unknown
```