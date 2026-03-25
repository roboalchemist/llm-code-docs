# Source: https://www.apollographql.com/docs/graphos/routing/security/tls.md

# Source: https://www.apollographql.com/docs/graphos/connectors/security/tls.md

# Connectors TLS Configuration

Connectors support the router's [TLS features](https://www.apollographql.com/docs/graphos/routing/security/tls) to authenticate and encrypt communications.

You can configure TLS for all Connectors or a specific Connector source.

* To configure all Connectors, set TLS configurations on `tls.connector.all`.
* To configure a specific Connector source, set TLS configurations on `tls.connector.sources.X` where `X` is your `subgraph_name.source_name`.
* If you configure both, specific Connector source configurations override configurations set on `tls.connector.all`.

## Example TLS configuration

The example configuration below sets [certificate authorities](https://www.apollographql.com/docs/graphos/routing/security/tls#overriding-certificate-authorities-for-subgraphs) and [client authentication](https://www.apollographql.com/docs/graphos/routing/security/tls#tls-client-authentication-for-subgraph-requests) for all Connectors and overrides the configuration for the `endpoint1` source on the `subgraph1` subgraph.

```yaml title=router.yaml
tls:
  connector:
    # Set TLS configurations for all Connectors
    all:
      certificate_authorities: ${file./path/to/ca.crt}
      client_authentication:
        certificate_chain: ${file./path/to/certificate_chain.pem}
        key: ${file./path/to/key.pem}
    # Override global setting for specific sources
    sources:
      subgraph1.endpoint1:
        certificate_authorities: ${file./path/to/specific_ca.crt}
        client_authentication:
          certificate_chain: ${file./path/to/specific_certificate_chain.pem}
          key: ${file./path/to/specifc_key.pem}
```
