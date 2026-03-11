# Source: https://docs.anyscale.com/reference.md

# Anyscale API reference

[View Markdown](/reference.md)

# Anyscale API reference

This page provides an overview of the Anyscale APIs and provides links to API references.

## What is an Anyscale API?[​](#what-is-an-anyscale-api "Direct link to What is an Anyscale API?")

Anyscale APIs are a collection developer tools for programmatic interaction with the Anyscale platform. Most Anyscale APIs have the following three components:

| Component | Description                                                                                                                                         |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| CLI       | A command line interface for running commands from a terminal or Bash script. See [Anyscale CLI overview](#cli).                                    |
| SDK       | A Python software development kit for interacting with Anyscale infrastructure from Python applications. See [Anyscale Python SDK overview](#sdk).  |
| Models    | Objects that represent Anyscale components using structured fields and values, used with the CLI or SDK. See [Models in the Anyscale API](#models). |

The Anyscale platform is optimized for running Ray applications. Use the following [Ray documentation](https://docs.ray.io/en/latest/index.html) to review the API reference for Ray Core and the Ray AI libraries:

* [Ray Core API](https://docs.ray.io/en/latest/ray-core/api/index.html)
* [Ray Data API](https://docs.ray.io/en/latest/data/api/api.html)
* [Ray Train API](https://docs.ray.io/en/latest/train/api/api.html)
* [Ray Tune API](https://docs.ray.io/en/latest/tune/api/api.html)
* [Ray Serve API](https://docs.ray.io/en/latest/serve/index.html)
* [Ray RLlib API](https://docs.ray.io/en/latest/rllib/package_ref/index.html)

## Option naming for Anyscale APIs[​](#option-naming-for-anyscale-apis "Direct link to Option naming for Anyscale APIs")

Most options in the Anyscale CLI, SDK, and models use the following general rules for naming:

* The CLI uses feature flags for specifying options and hyphens for multi-word options. Some CLI commands provide optional positional arguments and have alternate short flags for command options.
* The SDK uses standard Python casing for classes, functions, and parameters.
* Most keywords in models share the same snakecase formatting for both the SDK and CLI.

The following table shows an example of specifying the working directory for a job or service:

| CLI                    | SDK model              | YAML config for CLI     |
| ---------------------- | ---------------------- | ----------------------- |
| `--working-dir ./path` | `working_dir="./path"` | `working_dir: "./path"` |

## Anyscale CLI overview[​](#cli "Direct link to Anyscale CLI overview")

The Anyscale command line interface (CLI) provides programmatic tools for authenticating and interacting with the Anyscale platform from the command line, Bash scripts, and other similar tooling. See [CLI configuration](/reference/quickstart-cli.md).

Use the following links to navigate to CLI docs for common Anyscale features:

* [Compute Config CLI](/reference/compute-config-api.md#compute-config-cli)
* [Image CLI](/reference/image.md#image-cli)
* [Workspaces CLI](/reference/workspaces.md#workspaces-cli)
* [Service CLI](/reference/service-api.md#service-cli)
* [Job CLI](/reference/job-api.md#job-cli)
* [Schedule CLI](/reference/schedule-api.md#schedule-cli)
* [Service Account CLI](/reference/service-account.md#service-account-cli)
* [Cloud CLI](/reference/cloud.md#cloud-cli)
* [Machine Pool CLI](/reference/machine-pool.md#machine-pool-cli)
* [Resource Quotas CLI](/reference/resource-quotas.md#resource-quotas-cli)
* [Aggregated Instance Usage CLI](/reference/aggregated-instance-usage.md)
* [Logs CLI](/reference/logs.md#logs-cli)

## Anyscale Python SDK overview[​](#sdk "Direct link to Anyscale Python SDK overview")

The Anyscale Python software develoment kit (SDK) provides a set of classes and methods to programmatically interact with features and products in the Anyscale platform. See [Get started with the Anyscale SDK](/reference/quickstart-sdk.md).

note

Some Anyscale APIs are available in the CLI but not the SDK. Contact [Anyscale support](mailto:support@anyscale.com) to request new functionality.

Use the following links to navigate to SDK docs for common Anyscale features:

* [Compute Config SDK](/reference/compute-config-api.md#compute-config-sdk)
* [Image SDK](/reference/image.md#image-sdk)
* [Workspaces SDK](/reference/workspaces.md#workspaces-sdk)
* [Service SDK](/reference/service-api.md#service-sdk)
* [Job SDK](/reference/job-api.md#job-sdk)
* [Schedule SDK](/reference/schedule-api.md#schedule-sdk)
* [Aggregated Instance Usage SDK](/reference/aggregated-instance-usage.md)

## Models in the Anyscale API[​](#models "Direct link to Models in the Anyscale API")

Anyscale API *models* are data structures that define or describe Anyscale infrastructure.

Anyscale formats field names returned in response models to match field names in configuration models. You can use either the CLI or SDK to programmatically capture information about existing resources and reuse those fields and values to construct configuration models for other API calls.

The following table provides a high-level overview of configuration and response models for the SDK and CLI:

|                   | SDK                                                                                          | CLI                                                                           |
| ----------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Configuration** | Use Python classes with keyword arguments to build out configurations for other SDK methods. | Use YAML config files to pass options to CLI commands in a structured format. |
| **Response**      | Use Python classes to capture the return from SDK methods in a structured format.            | CLI commands return information about Anyscale assets structured as YAML.     |

Models in the SDK have a `to_dict()` method that allows you output the contents of a model formatted as a Python dict. The dict keys have the same names as keyword arguments for the model.

Use the following links to navigate to models for common API features:

* [Compute Config Models](/reference/compute-config-api.md#compute-config-models)
* [Image Models](/reference/image.md#image-models)
* [Workspaces Models](/reference/workspaces.md#workspaces-models)
* [Service Models](/reference/service-api.md#service-models)
* [Job Models](/reference/job-api.md#job-models)
* [Schedule Models](/reference/schedule-api.md#schedule-models)
* [Cloud Models](/reference/cloud.md#cloud-models)
* [Service Account Models](/reference/service-account.md#service-account-models)
* [Aggregated Instance Usage Models](/reference/aggregated-instance-usage.md)
