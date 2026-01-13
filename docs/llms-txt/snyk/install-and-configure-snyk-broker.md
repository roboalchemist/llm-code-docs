# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker.md

# Install and configure Snyk Broker

## How to use Snyk Broker

Snyk Broker is an open-source tool that acts as a proxy between Snyk and special integrations, providing for access by [snyk.io](http://snyk.io/) to scan code in repositories that are not internet-reachable and return results to you. SCM integrations with Broker support Snyk Open Source, Snyk Code, Snyk Container (Dockerfile), and Snyk IaC. For details, see [Integrations with Snyk Broker](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/..#integrations-supported-by-snyk-broker).

For comprehensive information about Snyk Broker, including how it works, how to deploy it, commit signing, upgrading, and troubleshooting, see the full [Snyk Broker user documentation](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker).

{% hint style="info" %}
[Broker version 4.205.1](https://github.com/snyk/broker/blob/cb4f89e05eb42605f076321b952cdb7e57bf4111/config.default.json#L8) has been [released](https://updates.snyk.io). In this version, all `ACCEPT` rule flags will be enabled by default. This reduces needed configuration. If you do not want a specific `ACCEPT` rule flag to be enabled, you can opt out of the default `ACCEPT` all behavior by adding `ACCEPT_=false` to your Broker client configuration.
{% endhint %}

## **Deployment options**

<table data-card-size="large" data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Install Snyk Broker with the</strong> <a href="https://github.com/snyk/snyk-broker-helm"><strong>Broker Helm Chart</strong></a>. For details, see <a href="install-and-configure-snyk-broker/install-and-configure-broker-using-helm">Install and configure Broker using Helm</a>.</td><td></td><td></td><td><a href="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4512bb77fa57427ed36360ef06489cdee749599a%2Fhelmkube.png?alt=media">helmkube.png</a></td><td><a href="install-and-configure-snyk-broker/install-and-configure-broker-using-helm">install-and-configure-broker-using-helm</a></td></tr><tr><td><strong>Install Snyk Broker</strong> <strong>using the</strong> <a href="https://github.com/snyk/broker"><strong>Docker images</strong></a> provided by Snyk. For details, see <a href="install-and-configure-snyk-broker/install-and-configure-broker-using-docker">Install and configure Broker using Docker</a>.</td><td></td><td></td><td><a href="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-efb27a5f61f0f6058d74098127f0f545a7812c1d%2FDocker-Logo.jpg?alt=media">Docker-Logo.jpg</a></td><td><a href="install-and-configure-snyk-broker/install-and-configure-broker-using-docker">install-and-configure-broker-using-docker</a></td></tr></tbody></table>

Alternatively, you can use the binaries available for [each Github release](https://github.com/snyk/broker/releases). However, this approach falls outside of Snyk product support and is made available only for specific use cases where containers cannot be used. The containerized version is strongly recommended.

## Additional information for developers

If you need to upgrade, see [Upgrade the Snyk Broker Client](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/update-the-snyk-broker-client).

Troubleshooting information is provided on the [Troubleshooting Broker](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/troubleshooting-broker) page.

You can view the [license, Apache License, Version 2.0](https://github.com/snyk/broker/blob/master/LICENSE).

To submit pull requests, see [Contributing](https://github.com/snyk/broker/blob/master/.github/CONTRIBUTING.md).

See [Security](https://github.com/snyk/broker/blob/master/SECURITY.md) for specific information about Broker.
