# Source: https://docs.axonius.com/docs/configuring-proxy-settings.md

# Configuring Proxy Settings

Customer-hosted admins can set a proxy for the Axonius machine.

<Callout icon="📘" theme="info">
  Note

  * Proxy Settings are not applicable for Axonius-hosted (SaaS) customers.

  * The proxy is used for all outbound communiction from this instance.

  * If a specific adapter needs to use a different proxy than the global one, the adapter level proxy configured supersedes the global proxy.
</Callout>

![Proxy\_Settings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Proxy_Settings.png)

* **Proxy enabled** *(required, default: switched off)* - Toggle on to use a proxy for the Axonius machine, if a proxy service exists in your environment. In this case, configure the following:
  * **Proxy address**
  * **Proxy port** (default is 8080)
  * **Proxy user name**, **Proxy password** for proxy services (optional)
  * **Verify SSL** - Select this option to verify the SSL certificate of the server. By default, the  checkbox is selected.