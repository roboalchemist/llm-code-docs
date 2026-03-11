# Source: https://docs.axonius.com/docs/managing-api-settings.md

# Managing Advanced API Settings

The Axonius REST API is available for regular user accounts for Axonius v6.1.73 and earlier. For Axonius v6.1.74 and later, the REST API is accessible only using [service accounts](https://docs.axonius.com/axonius-help-docs/docs/manage-service-accounts).

**To enable advanced API settings:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, select **API**.
3. Toggle on **Enable advanced API settings** and select the options you want:

* **Enable API destroy endpoints** - Select this checkbox to gain access to the /users/destroy and /devices/destroy endpoints, enabling you to delete all assets.

* **Allow cross-domain requests from developer.axonius.com** - When enabled, you can connect to your Axonius instance from the Readme API reference documentation. Once enabled, it may take a few minutes to take effect.