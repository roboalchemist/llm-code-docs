# Source: https://docs.datadoghq.com/getting_started/continuous_testing.md

# Source: https://docs.datadoghq.com/continuous_testing.md

---
title: Continuous Testing
description: >-
  Customize the number of Continuous Testing tests running in parallel in your
  CI/CD pipelines to increase your testing coverage.
breadcrumbs: Docs > Continuous Testing
---

# Continuous Testing

{% alert level="info" %}
This page is about running Continuous Testing tests in your CI/CD pipelines. If you want to view CI/CD metrics and dashboards, see the CI Visibility documentation.
{% /alert %}

Datadog Continuous Testing offers a set of tools that enable you to automate software testing for a product's entire lifecycle. By offering code-free, reliable end-to-end testing and seamless integrations with [popular CI providers](https://docs.datadoghq.com/continuous_testing/cicd_integrations/) and collaboration tools, Continuous Testing helps you accelerate application development and ship high-quality features faster.

## Test with ease and speed{% #test-with-ease-and-speed %}

Use scalable features such as a codeless [web recorder](https://docs.datadoghq.com/synthetics/browser_tests), [mobile app recorder](https://docs.datadoghq.com/mobile_app_testing/mobile_app_tests), [parallel test runs](https://docs.datadoghq.com/continuous_testing/settings), and built-in multi-location testing to save time and effort for your QA team. You can run your tests sequentially and customize the number of tests you want to run at the same time on the [**Settings** page](https://docs.datadoghq.com/continuous_testing/settings).

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/settings/parallelization.92597a9358f2f264d21398e013d5759a.png?auto=format"
   alt="Choose between running your tests sequentially and customizing the number of tests you want to run at the same time in the Continuous Testing Settings page" /%}

With support for multiple protocols, frameworks, and APIsâincluding gRPC and WebSocketsâyou can test across every level of your application stack, and [across any pre-production environment](https://docs.datadoghq.com/continuous_testing/environments).

## Improve test reliability{% #improve-test-reliability %}

Instead of having to implement test code, you can build software using [Synthetic Monitoring's resilient, scalable, and codeless tests](https://docs.datadoghq.com/synthetics/). Gain confidence in your test results by minimizing false positives through self-healing browser tests, mobile app tests, and automatic test retries.

To ensure your users have the best experience, you can automate [cross-browser testing](https://docs.datadoghq.com/synthetics/browser_tests) and [mobile application testing](https://docs.datadoghq.com/mobile_app_testing/). These Continuous Testing features are useful in CI batches where multiple tests are executed to cover a variety of scenarios and environments.

## Increase efficiency through seamless integrations{% #increase-efficiency-through-seamless-integrations %}

Fast-track your application development by testing and troubleshooting in one platform. Select from the following types of CI providers and collaboration tools such as [Slack](https://docs.datadoghq.com/integrations/slack/) or [Jira](https://docs.datadoghq.com/integrations/jira/) to merge workflows and avoid context switching.

- [github actions](https://docs.datadoghq.com/continuous_testing/cicd_integrations/github_actions/)
- [gitlab](https://docs.datadoghq.com/continuous_testing/cicd_integrations/gitlab/)
- [jenkins](https://docs.datadoghq.com/continuous_testing/cicd_integrations/jenkins/)
- [circleci orb](https://docs.datadoghq.com/continuous_testing/cicd_integrations/circleci_orb/)
- [azure devops extension](https://docs.datadoghq.com/continuous_testing/cicd_integrations/azure_devops_extension/)
- [bitrise upload-tests step](https://docs.datadoghq.com/continuous_testing/cicd_integrations/bitrise_upload/)
- [bitrise run-tests step](https://docs.datadoghq.com/continuous_testing/cicd_integrations/bitrise_run/)

You can use the [Datadog Terraform provider](https://registry.terraform.io/providers/DataDog/datadog/latest/) to control test creation and state management. Leverage your Synthetic tests as [integration and end-to-end tests](https://docs.datadoghq.com/continuous_testing/explorer) for your staging, pre-prod, and canary deployments, or run them directly in your [CI pipelines](https://docs.datadoghq.com/continuous_testing/explorer).

## Accelerate troubleshooting{% #accelerate-troubleshooting %}

Performing tests in a unified monitoring platform helps you find the root cause of failed test runs and reduce Mean Time to Resolution (MTTR).

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/ci_execution_side_panel.f2c77c77277131164450900429c93d74.png?auto=format"
   alt="CI batches side panel in the Synthetic Monitoring & Testing Results Explorer" /%}

You can obtain the full context for troubleshootingâwithout switching between toolsâthrough correlated metrics, traces, and logs surfaced by the Datadog [APM integration](https://docs.datadoghq.com/synthetics/apm/) by looking at executed jobs in the [Synthetic Monitoring & Testing Results Explorer](https://docs.datadoghq.com/continuous_testing/explorer).

## Examine CI batches in the Synthetic Monitoring & Testing Results Explorer{% #examine-ci-batches-in-the-synthetic-monitoring--testing-results-explorer %}

Create [search queries and visualizations](https://docs.datadoghq.com/continuous_testing/explorer) for your Synthetic test runs or batches of tests running in CI/CD pipelines.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/explorer/results_explorer.b6219b5ef0e902371c3007ce1ae5e702.png?auto=format"
   alt="A list of CI batch results in the Synthetic Monitoring & Testing Results Explorer" /%}

You can monitor individual test executions and comprehensive batches of tests, and access relevant insights for each testing type.

## Ready to start?{% #ready-to-start %}

After you have configured some [Synthetic tests](https://docs.datadoghq.com/synthetics/), see the documentation for your preferred [CI/CD provider](https://docs.datadoghq.com/continuous_testing/cicd_integrations/), or use the [`datadog-ci` NPM package](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration) in your CI/CD pipelines. See [Testing Local and Staging Environments](https://docs.datadoghq.com/continuous_testing/environments) to use Continuous Testing in environments that are not publicly available or production, for example, running tests against your local development environment or a staging environment within a private network. Then, start exploring details about your batch runs in the [Synthetic Monitoring & Testing Results Explorer](https://docs.datadoghq.com/continuous_testing/explorer).

{% callout %}
##### Try Synthetic Tests in a CI/CD Pipeline in the Learning Center

The Datadog Learning Center is full of hands-on courses to help you learn about this topic. Enroll at no cost to learn how to run a Datadog Synthetic test in a CI/CD pipeline.

[ENROLL NOW](https://learn.datadoghq.com/courses/synthetic-tests-ci-cd-pipeline)
{% /callout %}

## Further reading{% #further-reading %}

- [Check out the latest Datadog Continuous Testing releases! (App login required)](https://app.datadoghq.com/release-notes?category=Synthetic%20Monitoring)
- [Continuous Testing in a CI/CD Pipeline](https://learn.datadoghq.com/courses/synthetic-tests-ci-cd-pipeline)
- [Learn about Continuous Testing](https://docs.datadoghq.com/getting_started/continuous_testing)
- [Continuous Testing Guides](https://docs.datadoghq.com/continuous_testing/guide)
- [Learn about Private Locations](https://docs.datadoghq.com/synthetics/private_locations/#scale-your-private-location)
- [Learn about Testing in Local and Staging Environments](https://docs.datadoghq.com/continuous_testing/environments)
- [Troubleshoot Continuous Testing and CI/CD](https://docs.datadoghq.com/continuous_testing/troubleshooting/)
- [Use Datadog Continuous Testing to release with confidence](https://www.datadoghq.com/blog/release-confidently-with-datadog-continuous-testing/)
- [Best practices for continuous testing with Datadog](https://www.datadoghq.com/blog/best-practices-datadog-continuous-testing/)
- [Best practices for monitoring progressive web applications](https://www.datadoghq.com/blog/progressive-web-application-monitoring/)
