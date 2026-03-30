# Source: https://docs.axonius.com/docs/hashicorp-consul.md

# HashiCorp Consul

HashiCorp Consul is a multi-cloud service networking platform to connect and secure services across any runtime platform and public or private cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **HashiCorp Domain** *(required)* - The hostname of the HashiCorp Consul server.
2. **API Key** *(optional)* - Specify the Consul token you have generated. For more details, see [Consul ACL Token Create](https://www.consul.io/docs/commands/acl/token/create.html).
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![hashicorp.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/hashicorp.png)

## APIs

Axonius uses the [HashiCorp Consul Catalog HTTP API](https://www.consul.io/api/catalog.html).