# Source: https://docs.axonius.com/docs/configuring-syslog-settings.md

# Configuring Syslog Settings

Axonius supports integration with a Syslog server. This allows you to manage Axonius logs along with your other system logs. You can configure multiple Syslog instances to use multiple Syslog servers.

When **Use Syslog** is enabled, all log entries shown in the Activity Logs module are also sent to the configured Syslog server. Examples of events sent include:

* **Login**
  * Sent on success or failure of each login attempt.
  * Entries  include the supplied user name and the result.
* **Discovery cycle phase**
  Sent at the beginning and end of each discovery cycle phase.
* **Adapter connection failures**
  * Sent when an adapter connection fails to connect using the supplied configuration.
  * Entries include the adapter name, ID of the node running the adapter, and connection error.
* **Adapter connection asset cleanup**
  * Sent when an adapter decides to remove assets due to the configuration defined in Advanced Settings.
  * Entries include the number of assets removed.
  * To learn more, see: **[Adapter Advanced Settings](/docs/advanced-settings)**.

In addition, low disk space notifications are also sent to the configured Syslog server.

<Callout icon="📘" theme="info">
  Note

  Syslog settings must be configured to use the Enforcement Action **[Syslog Server - Send Log Message](/docs/send-to-syslog-server)**.
</Callout>

**To configure Syslog settings:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **External Integrations**, select **Syslog**, and enable **Use Syslog**.
3. To add a JSON formatted string to the HTTPS Log JSON, select **Extra headers around message (JSON format)**. This enables efficient integration with tools that accept JSON input. The input should appear as follows:
   ```json
    {"index": 12345, "sourcetype": "_json"}
   ```
4. To send all Syslog messages using the RFC 5424 protocol, select **Use RFC5424 Compliant messages format**.  If you want to send a token as well, enter a password into the **Additional token** field. Tokens are included in the structured data part of the message according to RFC5424 and tokens longer than 32 characters are supported.
5. For each Syslog instance (multiple instances are supported), configure the following:
   1. **Syslog gateway** *(default: No gateway)* - Enter the gateway to use.
   2. **Syslog host** - Enter the host name of the Syslog server.
   3. **Port** *(default: 514)* - Specify the port the Syslog server uses.
   4. **Protocol** *(default: UDP)* - Select the Syslog protocol: **UDP** or **TCP**. When using UDP, no further configuration is necessary.
6. When using **TCP**, you need to also configure the following:
   * **Use SSL for connection** *(default: Unencrypted)* - Select **Unencrypted** or **Encrypted**.
   * When using **Encrypted**, configure:
     * **SSL Certificate Verification** *(default: Unverified)* - Select **Unverified** or **Verified**. Unverified means that all certificate files will be accepted, including self-signed certificates. Verified means that only CA signed certificates will be accepted.
     * **Certificate file** - Upload the certificate file.
7. To configure another Syslog server, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddIcon.png). Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteIcon.png) to remove a Syslog server.