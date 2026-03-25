# Source: https://docs.anyscale.com/ci-cd.md

# CI/CD with Anyscale jobs and services

[View Markdown](/ci-cd.md)

# CI/CD with Anyscale jobs and services

Continuous integration (CI) and continuous deployment (CD) for machine learning systems enables the automatic execution of workloads for developing, deploying, monitoring, and maintaining your applications. An automated pipeline may trigger a cascade of workflows in response to a variety of events such as fresh data, performance regressions, or code updates.

This guide outlines the steps for integrating your existing CI/CD pipeline with Anyscale jobs and services.

## Continuous integration with Anyscale jobs[​](#ci-jobs "Direct link to Continuous integration with Anyscale jobs")

[Anyscale jobs](/jobs.md) automate machine learning workloads, including tasks like data processing, batch embedding generation, or model fine-tuning. Submitting jobs provides automatic failure handling, email alerts, and log management.

To integrate Anyscale jobs into your CI pipeline:

1. [Authenticate with Anyscale](/get-started.md#setup-env) and your chosen cloud storage provider.
2. Include the necessary [CLI](/reference/job-api.md) or [Python SDK](/reference/job-api.md) commands within the action steps of the pipeline.
3. Store the outputs, like processed data or models, in cloud storage so that subsequent jobs can then retrieve and process these artifacts.

tip

When using an orchestration framework that employs directed acyclic graphs (DAGs), like Airflow or Prefect, it may be helpful to use [the `--wait` flag](/reference/job-api.md#anyscale-job-submit) with Anyscale job submissions to block the CLI command until the job succeeds. Consider the implications of blocking a process in terms of pipeline efficiency and resource usage.

## Continuous deployment with Anyscale services[​](#cd-services "Direct link to Continuous deployment with Anyscale services")

[Anyscale services](/services.md) allow you to deploy and monitor Ray Serve apps in production. They ensure scalability, fault tolerance, and high availability with zero downtime upgrades, even under critical loads.

Similar to Anyscale jobs, to automatically deploy Anyscale services:

1. [Authenticate with Anyscale](/get-started.md#setup-env) and your chosen cloud storage provider.
2. Connect to cloud storage to retrieve artifacts and store outputs.
3. Include the necessary [CLI](/reference/service-api.md) or [Python SDK](/reference/service-api.md) commands within the action steps of the pipeline. During rollouts, you can configure the way traffic shifts from the service to the upgraded version.
4. [Monitor the service](/services/monitoring.md) through the service detail page, Ray Dashboard, or Grafana.

## Integrate with CI/CD tools[​](#integrate-tools "Direct link to Integrate with CI/CD tools")

The Anyscale [CLI](/reference.md) and [Python SDK](/reference.md) serve as integration points for jobs and services with your orchestration tools, such as:

* **GitHub Actions**: Use Anyscale CLI commands within action steps triggered by repository events, like pushes to `main`. These commands execute in GitHub-hosted or self-hosted runners. See the [GitHub Actions example](/ci-cd/github-actions.md).
* **Prefect**: Use Anyscale's [Prefect integration](https://github.com/anyscale/prefect-anyscale) to use Anyscale as the compute infrastructure for Prefect workloads.
* **Airflow**: Use Anyscale's [Airflow integration](/ci-cd/apache-airflow.md) to incorporate Anyscale CLI commands or SDK calls within tasks or DAGs.
