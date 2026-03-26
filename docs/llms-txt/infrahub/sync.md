# Source: https://docs.infrahub.app/sync.md

# Infrahub Sync

Infrahub Sync is a versatile Python package that synchronizes data between a source and a destination system. It builds on the robust capabilities of `diffsync` to offer flexible and efficient data synchronization across different platforms, including Netbox, Nautobot, and Infrahub. This package features a Typer-based CLI for ease of use, supporting operations such as listing available sync projects, generating diffs, and executing sync processes.

## Guides[​](#guides "Direct link to Guides")

* [Installing Infrahub Sync](/sync/guides/installation.md)
* [Creating a new sync instance](/sync/guides/creation.md)
* [Support adapters with custom CA certificates](/sync/guides/custom-certificates.md)
* [Run a sync instance](/sync/guides/run.md)

## Reference[​](#reference "Direct link to Reference")

* [Sync instance configuration](/sync/reference/config.md)
* [Sync CLI](/sync/reference/cli.md)

## Adapters[​](#adapters "Direct link to Adapters")

* [Infrahub](/sync/adapters/infrahub.md)
* [NetBox](/sync/adapters/netbox.md)
* [Nautobot](/sync/adapters/nautobot.md)
* [IP Fabric](/sync/adapters/ipfabric.md)
* [Cisco ACI](/sync/adapters/aci.md)
* [LibreNMS](/sync/adapters/librenms.md)
* [Observium](/sync/adapters/observium.md)
* [Peering Manager](/sync/adapters/peering-manager.md)
* [Prometheus](/sync/adapters/prometheus.md)

- [Slurp'it](/sync/adapters/slurpit.md)

* [Generic REST API](/sync/adapters/genericrestapi.md)
* [Local Adapters](/sync/adapters/local-adapters.md)

## Contributing[​](#contributing "Direct link to Contributing")

* [Development guide](/sync/development.md) - Set up a development environment, run tests, and publish releases
