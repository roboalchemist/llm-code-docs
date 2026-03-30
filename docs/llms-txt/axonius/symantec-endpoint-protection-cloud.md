# Source: https://docs.axonius.com/docs/symantec-endpoint-protection-cloud.md

# Symantec Endpoint Protection Cloud

Symantec Endpoint Protection Cloud unifies threat protection and device management for PC, Mac, mobile devices, and servers to protect endpoints from ransomware, zero-day threats, and other sophisticated attacks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Client ID** *(required)* - Enter the client ID to be used to get the token.
2. **Client Secret** *(required)* - Enter the secret key that should be shared and stored securely.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Symantec Endpoint Protection Cloud.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Symantec%20Endpoint%20Protection%20Cloud.png)

## APIs

Axonius uses the [Symantec Endpoint Protection Cloud REST API Reference](https://apidocs.symantec.com/home/SEPC#_oauth2_tokens_post).