# Source: https://docs.datadoghq.com/continuous_integration.md

---
title: Continuous Integration Visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Continuous Integration Visibility
---

# Continuous Integration Visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="info" %}
This page is about bringing your continuous integration (CI) metrics and data into Datadog dashboards. If you want to run Continuous Testing tests in your CI pipelines, see the Continuous Testing and CI/CD section.
{% /alert %}

{% callout %}
##### Join an enablement webinar session

Join the Introduction to CI Visibility session to understand how Datadog CI Visibility enhances the efficiency of CI pipelines and how to configure the Testing Visibility and Pipeline Visibility products.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=CI)
{% /callout %}

## Overview{% #overview %}

Datadog Continuous Integration (CI) Visibility provides a unified view of pipeline results, performance, trends, and reliability across your CI environments. By integrating Datadog with your CI pipelines, you can create monitors, display data within [Datadog dashboards](https://app.datadoghq.com/dashboard/lists) and [notebooks](https://app.datadoghq.com/notebook/list), and create visualizations for your organization's CI health.

CI Visibility helps developers understand the causes of pipeline disruptions and monitor trends in pipeline execution times. It also offers build engineers insights into cross-organization CI health and pipeline performance over time.

## Improve pipeline reliability and create traces{% #improve-pipeline-reliability-and-create-traces %}

CI Visibility helps you troubleshoot pipeline failures and broken builds by connecting the most significant development outages to the commits that caused them. You can instrument your pipelines and trace them as they execute, enabling deeper insights into pipeline performance.

## Increase efficiency through seamless integrations{% #increase-efficiency-through-seamless-integrations %}

Datadog integrates with a variety of CI providers to collect metrics that track the performance of your CI pipelines from commit to deployment. These metrics are used to identify performance trends and improvement opportunities.

- [aws codepipeline](https://docs.datadoghq.com/continuous_integration/pipelines/awscodepipeline/)
- [azure devops extension](https://docs.datadoghq.com/continuous_integration/pipelines/azure/)
- [buildkite](https://docs.datadoghq.com/continuous_integration/pipelines/buildkite/)
- [circleci orb](https://docs.datadoghq.com/continuous_integration/pipelines/circleci/)
- [codefresh](https://docs.datadoghq.com/continuous_integration/pipelines/codefresh/)
- [github actions](https://docs.datadoghq.com/continuous_integration/pipelines/github/)
- [gitlab](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab/)
- [jenkins](https://docs.datadoghq.com/continuous_integration/pipelines/jenkins/)
- [teamcity](https://docs.datadoghq.com/continuous_integration/pipelines/teamcity/)
- [other ci providers](https://docs.datadoghq.com/continuous_integration/pipelines/custom/)

You can use the `datadog-ci` CLI to [trace commands](https://docs.datadoghq.com/continuous_integration/pipelines/custom_commands/) and add [custom tags and measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/), which allows you to add user-defined text and numerical tags in your pipeline traces.

## Ready to start?{% #ready-to-start %}

Visit [Pipeline Visibility](https://docs.datadoghq.com/continuous_integration/pipelines/) for instructions on setting up CI Visibility with your CI providers, including details on compatibility requirements and steps for configuring data collection. Then, start exploring details about your pipeline executions in the [CI Visibility Explorer](https://docs.datadoghq.com/continuous_integration/explorer/) and export your search query into a [CI Pipeline Monitor](https://docs.datadoghq.com/monitors/types/ci/).

## Further reading{% #further-reading %}

- [Check out the latest Software Delivery releases! (App login required)](https://app.datadoghq.com/release-notes?category=Software%20Delivery)
- [Monitor your CircleCI environment with Datadog](https://www.datadoghq.com/blog/circleci-monitoring-datadog/)
- [Configure pipeline alerts with Datadog CI monitors](https://www.datadoghq.com/blog/configure-pipeline-alerts-with-ci-monitors/)
- [Explore pipeline data to resolve build problems](https://docs.datadoghq.com/continuous_integration/pipelines/)
- [Learn about billing considerations for CI Visibility](https://docs.datadoghq.com/account_management/billing/ci_visibility)
- [Explore test data to find and fix problem tests](https://docs.datadoghq.com/continuous_integration/tests/)
- [Best practices for monitoring static web applications](https://www.datadoghq.com/blog/static-web-application-monitoring-best-practices/)
- [Best practices for CI/CD monitoring](https://www.datadoghq.com/blog/best-practices-for-ci-cd-monitoring/)
- [Best practices for monitoring software testing in CI/CD](https://www.datadoghq.com/blog/best-practices-for-monitoring-software-testing/)
- [Monitor your CI/CD modernizations with Datadog CI Pipeline Visibility](https://www.datadoghq.com/blog/modernize-your-ci-cd-environment/)
- [How we use Datadog for detection as code](https://www.datadoghq.com/blog/datadog-detection-as-code/)
- [Patterns for safe and efficient cache purging in CI/CD pipelines](https://www.datadoghq.com/blog/cache-purge-ci-cd/)
- [Troubleshoot faster with the GitLab Source Code integration in Datadog](https://www.datadoghq.com/blog/gitlab-source-code-integration)
