# Source: https://docs.datadoghq.com/continuous_integration/pipelines/custom_commands.md

---
title: Adding Custom Commands to Pipeline Traces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  Adding Custom Commands to Pipeline Traces
---

# Adding Custom Commands to Pipeline Traces

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Custom commands provide a way to trace individual commands in your CI pipelines, allowing you to measure the time your command takes without taking into account any setup or teardown actions that the job might have (for example, downloading Docker images or waiting for an available node in a Kubernetes-based infrastructure). These spans appear as part of the pipeline's trace:

{% image
   source="https://datadog-docs.imgix.net/images/ci/ci-custom-spans.096550b437f161a7b880daebad7167d4.png?auto=format"
   alt="Details for a single pipeline with custom commands" /%}

## Compatibility{% #compatibility %}

Custom commands work with the following CI providers:

- GitHub.com (SaaS) with datadog-ci CLI >= 2.40. For sending custom commands in GitHub Actions, see Known issue with Github Actions.
- GitLab (SaaS or self-hosted >= 14.1) with datadog-ci CLI >= 2.40.
- Jenkins with the Datadog plugin >= v3.2.0
- CircleCI
- Azure DevOps Pipelines with datadog-ci CLI >= 2.40.
- AWS Codepipeline with datadog-ci CLI >= 2.40. Follow [Adding custom commands](https://docs.datadoghq.com/continuous_integration/pipelines/awscodepipeline/#add-the-pipeline-execution-id-as-an-environment-variable) to set up custom commands in AWS Codepipeline.
- Buildkite with datadog-ci CLI >= 2.40.

## Install the Datadog CI CLI{% #install-the-datadog-ci-cli %}

Install the [`datadog-ci`](https://www.npmjs.com/package/@datadog/datadog-ci) (>=v0.17.0) CLI globally using `npm`:

```shell
npm install -g @datadog/datadog-ci
```

{% alert level="info" %}
See [More ways to install the CLI](https://github.com/DataDog/datadog-ci?tab=readme-ov-file#more-ways-to-install-the-cli) in the datadog-ci repo for alternative installation options.
{% /alert %}

## Trace a command line{% #trace-a-command-line %}

To trace a command line, run:

```shell
datadog-ci trace [--name <name>] -- <command>
```

Specify a valid [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) in the `DATADOG_API_KEY` environment variable. For example:



{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, us3.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com



```

DATADOG_API_KEY=<key> DATADOG_SITE= datadog-ci trace \
--name "Greet" \
-- \
echo "Hello World"
```


{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
CI Visibility is not available in the selected site ().
{% /alert %}


{% /callout %}



### Configuration settings{% #configuration-settings %}

These options are available for the `datadog-ci trace` command:

{% dl %}

{% dt %}
`--name`
{% /dt %}

{% dd %}
Display name of the custom command.**Default**: same value as `<command>`**Example**: `Wait for DB to be reachable`
{% /dd %}

{% dt %}
`--tags`
{% /dt %}

{% dd %}
Key-value pairs in the form `key:value` to be attached to the custom command (the `--tags` parameter can be specified multiple times). When specifying tags using `DD_TAGS`, separate them using commas (for example, `team:backend,priority:high`).**Environment variable**: `DD_TAGS`**Default**: (none)**Example**: `team:backend`**Note**: Tags specified using `--tags` and with the `DD_TAGS` environment variable are merged. If the same key appears in both `--tags` and `DD_TAGS`, the value in the environment variable `DD_TAGS` takes precedence.
{% /dd %}

{% dt %}
`--measures`
{% /dt %}

{% dd %}
Key-value pairs in the form `key:value` to be attached to the custom command as numerical values (the `--measures` parameter can be specified multiple times).*(Requires datadog-ci >=v2.35.0)***Default**: (none)**Example**: `size:1024`
{% /dd %}

{% dt %}
`--no-fail`
{% /dt %}

{% dd %}
Prevents datadog-ci from failing even if run in an unsupported CI provider. In this case, the command is run and nothing is reported to Datadog.**Default**: `false`
{% /dd %}

{% dt %}
`--dry-run`
{% /dt %}

{% dd %}
Prevents datadog-ci from sending the custom span to Datadog. All other checks are performed.**Default**: `false`
{% /dd %}

{% dt %}
Positional arguments
{% /dt %}

{% dd %}
The command that is launched and traced.
{% /dd %}

{% /dl %}

The following environment variables are supported:

{% dl %}

{% dt %}
`DATADOG_API_KEY` (Required)
{% /dt %}

{% dd %}
[Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) used to authenticate the requests.**Default**: (none)
{% /dd %}

{% /dl %}

{% callout %}
# Important note for users on the following Datadog sites: us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com



Additionally, configure the Datadog site to use the selected one ():

{% dl %}

{% dt %}
`DATADOG_SITE`
{% /dt %}

{% dd %}
The Datadog site to upload results to.**Default**: `datadoghq.com`**Selected site**: 
{% /dd %}

{% /dl %}


{% /callout %}

## Trace a command block{% #trace-a-command-block %}

It is possible to trace multiple command lines at once by manually specifying the start and end timestamps (or the duration).

```shell
datadog-ci trace span [--name <name>] [--start-time <timestamp-ms>] [--end-time <timestamp-ms>] # [--duration <duration-ms>] can be used instead of start / end time
```

Specify a valid [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) in the `DATADOG_API_KEY` environment variable. For example:



{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, us3.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com



```

DATADOG_API_KEY=<key> DATADOG_SITE= datadog-ci trace span \
--name "Build Step" \
--duration 10000
```


{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
CI Visibility is not available in the selected site ().
{% /alert %}


{% /callout %}



### Configuration settings{% #configuration-settings-1 %}

These options are available for the `datadog-ci trace span` command:

{% dl %}

{% dt %}
`--name`
{% /dt %}

{% dd %}
Display name of the custom span.**Example**: `Build Step`
{% /dd %}

{% dt %}
`--start-time`
{% /dt %}

{% dd %}
Timestamp in milliseconds since the UNIX epoch representing the start time of the span.**Note**: There are two ways to specify start and end time, by using `--start-time` and `--end-time` or using `--duration`.
{% /dd %}

{% dt %}
`--end-time`
{% /dt %}

{% dd %}
Timestamp in milliseconds since the UNIX epoch representing the end time of the span.**Note**: There are two ways to specify start and end time, by using `--start-time` and `--end-time` or using `--duration`.
{% /dd %}

{% dt %}
`--duration`
{% /dt %}

{% dd %}
Duration amount in milliseconds. Using this, the end time is the current time when executing this command.**Note**: There are two ways to specify start and end time, by using `--start-time` and `--end-time` or using `--duration`.
{% /dd %}

{% dt %}
`--tags`
{% /dt %}

{% dd %}
Key-value pairs in the form `key:value` to be attached to the custom span (the `--tags` parameter can be specified multiple times). When specifying tags using `DD_TAGS`, separate them using commas (for example, `team:backend,priority:high`).**Environment variable**: `DD_TAGS`**Default**: (none)**Example**: `team:backend`**Note**: Tags specified using `--tags` and with the `DD_TAGS` environment variable are merged. If the same key appears in both `--tags` and `DD_TAGS`, the value in the environment variable `DD_TAGS` takes precedence.
{% /dd %}

{% dt %}
`--measures`
{% /dt %}

{% dd %}
Key-value pairs in the form `key:value` to be attached to the custom span as numerical values (the `--measures` parameter can be specified multiple times).*(Requires datadog-ci >=v2.35.0)***Default**: (none)**Example**: `size:1024`
{% /dd %}

{% dt %}
`--dry-run`
{% /dt %}

{% dd %}
Prevents datadog-ci from sending the custom span to Datadog. All other checks are performed.**Default**: `false`
{% /dd %}

{% /dl %}

The following environment variables are supported:

{% dl %}

{% dt %}
`DATADOG_API_KEY` (Required)
{% /dt %}

{% dd %}
[Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) used to authenticate the requests.**Default**: (none)
{% /dd %}

{% /dl %}

{% callout %}
# Important note for users on the following Datadog sites: us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com



Additionally, configure the Datadog site to use the selected one ():

{% dl %}

{% dt %}
`DATADOG_SITE`
{% /dt %}

{% dd %}
The Datadog site to upload results to.**Default**: `datadoghq.com`**Selected site**: 
{% /dd %}

{% /dl %}


{% /callout %}

## Known issue with GitHub Actions{% #known-issue-with-github-actions %}

Starting with `datadog-ci` version `4.1.1`, no additional action is required, even when using custom names or matrix strategies.

{% collapsible-section %}
**For datadog-ci versions prior to 4.1.1**
If you are using `datadog-ci` version `2.29.0` to `4.1.0` and the job name does not match the entry defined in the workflow configuration file (the GitHub [job ID](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_id)), the `DD_GITHUB_JOB_NAME` environment variable needs to be exposed, pointing to the job name. For example:

1. If the job name is changed using the [name property](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#name):

   ```yaml
   jobs:
     build:
       name: My build job name
       env:
         DD_GITHUB_JOB_NAME: My build job name
       steps:
       - run: datadog-ci trace ...
   ```

1. If the [matrix strategy](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs#using-a-matrix-strategy) is used, several job names are generated by GitHub by adding the matrix values at the end of the job name, within parenthesis. The `DD_GITHUB_JOB_NAME` environment variable should then be conditional on the matrix values:

   ```yaml
   jobs:
     build:
       strategy:
         matrix:
           version: [1, 2]
           os: [linux, macos]
       env:
         DD_GITHUB_JOB_NAME: build (${{ matrix.version }}, ${{ matrix.os }})
       steps:
       - run: datadog-ci trace ...
   ```

{% /collapsible-section %}

## Troubleshooting{% #troubleshooting %}

### Payload too large{% #payload-too-large %}

The size limit is approximately `4MB`. The most common cause for this error is extremely large tags. Use the `--dry-run` option to see the traced command's contents before sending it to Datadog.

## Further reading{% #further-reading %}

- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/pipelines/custom_commands/)
