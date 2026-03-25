# Source: https://docs.axonius.com/docs/arista-eos.md

# Arista Extensible Operating System (EOS)

Arista Extensible Operating System (EOS) is the core of Arista cloud networking solutions for next-generation data centers and cloud networks.

<Callout icon="📘" theme="info">
  NOTE

  Axonius uses the [Arista eAPI 101](https://eos.arista.com/arista-eapi-101/).
</Callout>

## Asset Types Fetched

* Devices

## Adapter Parameters

1. **Arista EOS Domain** *(required)* - The hostname of the Arista EOS server/switch.
2. **User Name** and **Password** *(required)* - The user name and password to access the Arista switch.
3. **EOS Enable Password** *(optional, default: empty)* - Specify the enable password to authorize executing the enable command. The enable password is required if the Arista switch requires enable command authorization, that controls access to Privileged EXEC and all configuration command modes.
   * If supplied, the API will use the specified enable password to execute the enable command.
   * If not supplied, the API will not be able to execute the enable command. As a result, it may be that minimal or no data will be retrieved from the Arista switch.

4.**Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/arista.png" />