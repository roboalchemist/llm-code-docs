# Source: https://docs.axonius.com/docs/icinga.md

# Icinga

Icinga is an open-source computer system and network monitoring application. It monitors data centers and clouds availability and performance, gives access to data and raises alerts.

<Callout icon="📘" theme="info">
  Note

  Axonius supports Icinga 2, and uses the Icinga 2 API which is not enabled by default. To enable the API see [Icinga Documentation](https://icinga.com/docs/icinga2/latest/doc/12-icinga2-api/).
</Callout>

The Icinga adapter connection requires the following parameters:

<Callout icon="📘" theme="info">
  Note

  You can authenticate either using a **User Name** and **Password** or a  X.509 **certificate file** and a  **Private key file**.
</Callout>

1. **Icinga Domain** – The hostname for Icinga.
2. **User Name** and **Password** – The user name and password for the API user used in the connection.
3. **Certificate file** - Upload the  X.509 certificate file issued by Icinga,[refer to Icinga2 API for details](https://icinga.com/docs/icinga-2/latest/doc/12-icinga2-api/#authentication)
4. **Private key file** - Upload the private key file created.
5. **API Port** (optional) – The port used for the connection (Default 5665).
6. **Verify SSL** – Choose whether to verify the SSL certificate of the server.
7. **HTTPS Proxy** (optional) – Connect the adapter to a proxy instead of directly connecting it to the domain.

![icinga.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/icinga.png)