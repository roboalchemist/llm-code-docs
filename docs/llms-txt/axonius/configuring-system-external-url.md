# Source: https://docs.axonius.com/docs/configuring-system-external-url.md

# Configuring System External URL

<Callout icon="📘" theme="info">
  Note

  System External URL setting is not applicable for Axonius-hosted (SaaS) customers.
</Callout>

Customer-hosted admins can set an external URL to be part of every link to the system.

**To open the System External URL settings:**

1. From the top right corner of any page, click ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Access Management**, and select **URL**.

![SystemExternalURL](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SystemExternalURL.png)

* **Use external URL** *(optional, default: switched off)* - An external URL to be part of every link to the system.
  * Toggle on to configure the host name or IP address (without http\:// or https\://) to be used for links redirecting to the system in:
    * Reports
    * Reset password links
    * Emails
    * Enforcement actions under the following categories:
      * Notify
      * Create Incident
  * Toggle off (default) so that all links redirecting back to the system use the host name or IP address that the user uses to access the Axonius node.