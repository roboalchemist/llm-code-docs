# Source: https://docs.axonius.com/docs/configuring-atlassian-opsgenie-settings.md

# Configuring Atlassian Opsgenie Settings

You can configure an Opsgenie service so that   Adapter connection failures create alarms in the configured Opsgenie server.

**To configure Atlassian Opsgenie:**

1. From the top right corner of any page, click ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **External Integrations**, and select **Atlassian Opsgenie**.

![AtlassianOpsgenieSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AtlassianOpsgenieSettings.png)

* **Use Opsgenie** *(required, default: switched off)* - Toggle on to use Atlassian Opsgenie server.

If switched on, specify the following:

* **Opsgenie API domain** *(required, default: `https://api.opsgenie.com/`)* - Specify the Opsgenie API URL. If using the EU instance of Opsgenie, the URL needs to be *[https://api.eu.opsgenie.com](https://api.eu.opsgenie.com)* for requests to be executed.

* **API key** *(required)* - API key generated from the Opsgenie console.
  **To add an API key:**
  1. Navigate to **Settings** page >> **App Settings** >> **API Key Management**.
     ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(547\).png)

  2. Click **Add New API Key**.

  3. Enter a name for the API key and select the following access rights to give to this API key:
     * Read - Can read the alerts, incidents, and configurations.
     * Create/Update - Can create new alerts, configurations and incidents, and update them.
       ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(548\).png)

  4. Click **Add API Key** to save the new API key.
     For more details, see [Atlassian Opsgenie - API Key Management](https://docs.opsgenie.com/docs/api-key-management).

* **Verify SSL** *(required, default: false)* - Select this option to verify the SSL certificate offered by the value supplied in **Opsgenie API domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Opsgenie API domain**.
  * If supplied, Axonius utilizes the proxy when connecting to the value supplied in **Opsgenie API domain**.
  * If not supplied, Axonius connects directly to the value supplied in **Opsgenie API domain**.

If **Use Opsgenie** is toggled on, Adapter connection failures create alarms in the configured Opsgenie server. The alarm includes the adapter name, ID of the node running the adapter, and connection error.