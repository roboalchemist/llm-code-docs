# Source: https://www.aptible.com/docs/core-concepts/apps/deploying-apps/configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration

> Learn about how configuration variables provide persistent environment variables for your app's containers, simplifying settings management

# Overview

Configuration variables contain a collection of keys and values, which will be made available to your app's containers as environment variables. Configurable variables persist once set, eliminating the need to repeatedly set the variables upon deploys. These variables will remain available in your app containers until modified or unset.

You can use the following configuration variables:

* `FORCE_SSL` (See [HTTPS Redirect](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-redirect))
* `STRICT_HEALTH_CHECKS` (See [Strict Health Checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#strict-health-checks))
* `IDLE_TIMEOUT` (See [Endpoint Timeouts](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#timeouts))
* `SSL_PROTOCOLS_OVERRIDE` (See [HTTPS Protocols](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-protocols))
* `SSL_CIPHERS_OVERRIDE` (See [HTTPS Protocols](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-protocols))
* `DISABLE_WEAK_CIPHER_SUITE` (See [HTTPS Protocols](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/https-protocols))
* `SHOW_ELB_HEALTHCHECKS` (See [Endpoint configuration variables](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs#configuration-options))
* `RELEASE_HEALTHCHECK_TIMEOUT` (See [Release Health Checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#release-health-checks))
* `MAINTENANCE_PAGE_URL` (See [Maintenance Page](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/maintenance-page))
* `APTIBLE_PRIVATE_REGISTRY_USERNAME` (See [Private Registry Authentication](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy#private-registry-authentication))
* `APTIBLE_PRIVATE_REGISTRY_PASSWORD` (See [Private Registry Authentication](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy#private-registry-authentication))
* `APTIBLE_DO_NOT_WIPE` (See [Disabling filesystem wipes](/core-concepts/architecture/containers/container-recovery#disabling-filesystem-wipes))
* `APTIBLE_ACK_COMPANION_REPO_DEPRECATION` (See [Companion Git Repository](/core-concepts/apps/deploying-apps/image/deploying-with-docker-image/companion-git-repository))

# FAQ

<AccordionGroup>
  <Accordion title="How do I set or modify configuration variables?">
    See related guide:

    <Card title="How to set or modify configuration variables" icon="book-open-reader" iconType="duotone" href="https://www.aptible.com/docs/set-configuration-variables" />
  </Accordion>

  <Accordion title="How do I synchronize configuration and code change?">
    See related guide:

    <Card title="How to synchronize configuration and code changes" icon="book-open-reader" iconType="duotone" href="https://www.aptible.com/docs/synchronized-deploys" />
  </Accordion>
</AccordionGroup>
