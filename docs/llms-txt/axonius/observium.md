# Source: https://docs.axonius.com/docs/observium.md

# Observium

Observium is an auto-discovering network monitoring platform supporting a wide range of device types, platforms and operating systems.

<Callout icon="📘" theme="info">
  API

  Axonius uses the [Observium API](https://docs.observium.org/api/)
</Callout>

## Adapter Parameters

* **Observium Domain** *(required)* - The hostname of the Observium server.
* **User Name** and **Password** *(required)* - The user name and password for an account that has read access to the API.
* **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the host supplied in **Observium Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
  * If enabled, the SSL certificate offered by the host will be verified against the CA database inside of Axonius. If it fails validation, the connection will fail with an error.
  * If disabled, the SSL certificate offered by the host will not be verified against the CA database inside of Axonius.
* **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to **Observium Domain**.
  * If supplied, Axonius will utilize the proxy when connecting to the host defined for this connection.
  * If not supplied, Axonius will connect directly to the host defined for this connection.

<Image border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Observium.png" className="border" />

<Callout icon="📘" theme="info">
  Note

  For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).
</Callout>