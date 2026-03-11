# Source: https://docs.axonius.com/docs/ca-spectrum.md

# CA Spectrum

CA Spectrum is a services and network infrastructure management system that enables the modeling of LAN, WAN, wired, wireless, physical, and virtual networks.

## Parameters

1. **CA Spectrum Domain** – The hostname of the CA Spectrum server.

<Callout icon="📘" theme="info">
  NOTE

  If you have configured your CA Spectrum API to listen on HTTP only based port numbers instead of HTTPS/TLS port numbers such as 443, you will need to prefix the hostname with http\:// for example http\://\[\[CA Spectrum hostname / IP address]]:8080.
</Callout>

2. **User Name** and **Password** – The user name and password for the user used in the connection.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(821).png" />