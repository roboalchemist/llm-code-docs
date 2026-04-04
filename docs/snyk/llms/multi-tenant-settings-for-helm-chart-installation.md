# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/advanced-configuration-for-helm-chart-installation/multi-tenant-settings-for-helm-chart-installation.md

# Multi-tenant settings for Helm chart installation

To use the Helm chart in different multi-tenant regions, set the `brokerServerUrl` for the region you are using.

See [Broker URLs](https://docs.snyk.io/snyk-data-and-governance/regional-hosting-and-data-residency#broker-server-urls) for the list of regional URLs.

Use the following command:

```
--set brokerServerUrl=<broker-region-url>
```
