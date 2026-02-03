# Source: https://docs.datadoghq.com/continuous_testing/environments.md

---
title: Testing Local and Staging Environments
description: Learn about using Continuous Testing in local and remote environments.
breadcrumbs: Docs > Continuous Testing > Testing Local and Staging Environments
---

# Testing Local and Staging Environments

## Overview{% #overview %}

In the context of [testing within a CI/CD pipeline, also known as shift-left testing](https://www.datadoghq.com/blog/shift-left-testing-best-practices/), the production environment is typically the last link in the chain. Your application is likely to go through several steps before reaching this stage.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/environments.7e2b04937c809de328eb4c9df6a902d4.png?auto=format"
   alt="Continuous Testing can be used all along the development cycle, from the local development environment to staging to prod." /%}

While [scheduled Synthetic tests focus primarily on publicly available production environments](https://www.datadoghq.com/blog/datadog-synthetic-ci-cd-testing/), Continuous Testing allows you to test your application in any or all environments it's deployed in throughout the development cycle.

## Testing in multiple environments{% #testing-in-multiple-environments %}

Continuous Testing can reuse the same scenario from scheduled tests used against the production environment to test publicly available pre-production environments.

Whether it's for a [blueâgreen deployment](https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment), or a dedicated staging environment, Continuous Testing allows you to reroute an existing scenario to a different environment. For more information, see [Testing Multiple Environments](https://docs.datadoghq.com/continuous_testing/environments/multiple_env).

## Testing while using proxies, firewalls, or VPNs{% #testing-while-using-proxies-firewalls-or-vpns %}

Continuous Testing can test your application in the early steps of the development cycle, including behind a private network protected by a proxy, firewall, or VPN.

It can run the same scenario from scheduled Synthetic tests against changes deployed in a local server running on your development environment (such as a dev laptop), or in a CI/CD pipeline where your application is deployed in an ephemeral environment that lasts the same amount of time as the CI/CD job, or in a private staging environment.

Continuous Testing provides a [testing tunnel](https://docs.datadoghq.com/continuous_testing/environments/proxy_firewall_vpn/#what-is-the-testing-tunnel) which allows the Synthetic managed location to reach private environments. For more information, see [Testing While Using Proxies, Firewalls, or VPNs](https://docs.datadoghq.com/continuous_testing/environments/proxy_firewall_vpn).

## Further reading{% #further-reading %}

- [Best practices for shift-left testing](https://www.datadoghq.com/blog/shift-left-testing-best-practices/)
- [Incorporate Datadog Synthetic tests into your CI/CD pipeline](https://www.datadoghq.com/blog/datadog-synthetic-ci-cd-testing/)
- [Learn how to run tests in a CI/CD pipeline](https://learn.datadoghq.com/courses/synthetic-tests-ci-cd-pipeline)
- [Learn about testing in multiple environments](https://docs.datadoghq.com/continuous_testing/environments/multiple_env)
- [Learn about testing while using proxies, firewalls, or VPNs](https://docs.datadoghq.com/continuous_testing/environments/proxy_firewall_vpn)
- [Learn about private locations](https://docs.datadoghq.com/synthetics/private_locations)
