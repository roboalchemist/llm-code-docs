# Source: https://docs.axonius.com/docs/configuring-remote-support.md

# Configuring Remote Support

**To configure Remote Support:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **System**, and select **Remote Support**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(824\).png)

<Callout icon="📘" theme="info">
  Note

  Advanced Settings (Remote Support) are not applicable to Axonius-hosted (SaaS) customers.
</Callout>

* **Remote Support** *(required, default: True)* - Allow Axonius to remotely connect to the instance using a telemetry service. Remote support is required to provide continuous updates, maintenance, and troubleshooting. It is strongly recommended to keep this enabled to have the best customer experience.
  If you disable remote support, you can still allow Axonius to remotely connect to the instance for a predefined number of hours.

  <Image alt="RemoteSupport.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/RemoteSupport.png" />
* **Anonymized Analytics** *(required, default: True)* - Anonymized analytics data will be sent to Axonius. This kind of data consists of errors and exceptions, usage alerts,  and more. It is strongly recommended to keep this enabled to have the best customer experience.
* **Remote Access** *(required, default: True)* - Remote Access allows Axonius to keep the system updated by providing continuous updates and speeding up issue resolution time.