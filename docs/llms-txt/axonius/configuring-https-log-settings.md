# Source: https://docs.axonius.com/docs/configuring-https-log-settings.md

# Configuring HTTPS Log Settings

Axonius supports integration with an HTTPS log server.  You can configure HTTPS Logs to send all Activity Logs to this server, as well as to use the Send to HTTPS Log Server action.
![HTTPSSettings-New.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HTTPSSettings-New.png)

**To configure HTTPS Logs settings:**

1. From the top right corner of any page, click ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **External Integrations**, and select **HTTPS Logs**.

* **Use HTTPS logs** *(required, default: switched off)* - Toggle on to use an HTTPS logs server. This setting must be switched on  if you want to use the **[Send to HTTPS Log Server](/docs/send-to-https-log-server)** action.

  When **Use HTTPS logs** is activated, all log entries shown in the Activity Logs module are sent to the configured HTTPS log server.
* **HTTPS gateway** *(optional, default: No gateway)* - Enter or select the gateway to use.
* **HTTPS logs host** *(required)* - Enter the log host.
* **Port** *(optional)* - The port to use for HTTPS log host.
* **HTTPS proxy** *(optional)* - Enter a proxy.
* **Authorization header** -  An authorization header to be used for authentication with the log server. For example: “Basic AaBbCc123456”
* **Extra headers around message (JSON format)** *(optional)* - Use this setting to add a JSON formatted string that can be added to the HTTPS Log JSON thus enabling efficient integration with tools that accept input of JSON. The input should appear as follows:
  ```json
   {"index": 12345, "sourcetype": "_json"}
  ```
* **Max retries** *(optional, default = 3)* - The maximum number of retries to perform if connection to the HTTPS logging server is not successful.
* **Backoff for retries in seconds**  *(optional, default = 0.5)* - The number of  seconds to wait  between retries, using exponential backoff. (By default, the wait between retries is 0.5s, 1s, 2s.)