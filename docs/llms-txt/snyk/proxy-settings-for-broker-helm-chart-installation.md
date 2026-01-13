# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/advanced-configuration-for-helm-chart-installation/proxy-settings-for-broker-helm-chart-installation.md

# Proxy settings for Broker Helm chart installation

To use the Helm chart behind a proxy, set the `httpProxy` and `httpsProxy` values.

```
--set httpsProxy=<PROXY_URL>
```
