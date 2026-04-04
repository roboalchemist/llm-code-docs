# Source: https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures.md

---
title: Adding Custom Tags and Measures to Pipeline Traces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  Adding Custom Tags and Measures to Pipeline Traces
---

# Adding Custom Tags and Measures to Pipeline Traces

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Use the custom tags and measures commands to add user-defined text and numerical tags to your pipeline traces in [CI Pipeline Visibility](https://docs.datadoghq.com/continuous_integration/pipelines/). You can use the [`datadog-ci` NPM package](https://www.npmjs.com/package/@datadog/datadog-ci) to add custom tags to a pipeline trace or a job span, in addition to adding measures to a pipeline trace or a job span. From these custom tags and measures, you can create facets (string value tags) or measures (numerical value tags).

You can use facets and measures to filter, create visualizations, or create monitors for your pipelines in the [CI Visibility Explorer](https://docs.datadoghq.com/continuous_integration/explorer).

### Compatibility{% #compatibility %}

Custom tags and measures work with the following CI providers:

- Buildkite
- CircleCI
- GitLab (SaaS or self-hosted >= 14.1)
- GitHub.com (SaaS): For adding tags and measures to GitHub jobs, see the section below.
- Jenkins: For Jenkins, follow [these instructions](https://docs.datadoghq.com/continuous_integration/pipelines/jenkins?tab=usingui#setting-custom-tags-for-your-pipelines) to set up custom tags in your pipelines.
- Azure DevOps Pipelines

## Install the Datadog CI CLI{% #install-the-datadog-ci-cli %}

Install the [`datadog-ci`](https://www.npmjs.com/package/@datadog/datadog-ci) (>=v1.15.0) CLI globally using `npm`:

```shell
npm install -g @datadog/datadog-ci
```

{% alert level="info" %}
See [More ways to install the CLI](https://github.com/DataDog/datadog-ci?tab=readme-ov-file#more-ways-to-install-the-cli) in the datadog-ci repo for alternative installation options.
{% /alert %}

## Add tags to pipeline traces{% #add-tags-to-pipeline-traces %}

Tags can be added to the pipeline span or to the job span.

To do this, run the `tag` command:

```shell
DATADOG_SITE= datadog-ci tag [--level <pipeline|job>] [--tags <tag1>] [--tags <tag2>] ...
```

You must specify a valid [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) using the environment variable `DATADOG_API_KEY` and the [Datadog site](https://docs.datadoghq.com/getting_started/site/) using the environment variable `DATADOG_SITE`.

The following example adds `team` and `service` tags to the pipeline span.

```shell
DATADOG_SITE= datadog-ci tag --level pipeline --tags team:backend --tags service:processor
```

The following example adds the tag `go.version` to the span for the current job:

```shell
DATADOG_SITE= datadog-ci tag --level job --tags "go.version:`go version`"
```

To create a facet from a tag, click the gear icon next to a tag name on the [Pipeline Executions page](https://app.datadoghq.com/ci/pipeline-executions), and click **Create Facet**.

{% video
   url="https://datadog-docs.imgix.net/images/ci/custom-tags-create-facet.mp4" /%}

## Add measures to pipeline traces{% #add-measures-to-pipeline-traces %}

To add numerical tags to the pipeline span or the job span, run the `measure` command:

```shell
DATADOG_SITE= datadog-ci measure [--level <pipeline|job>] [--measures <measure1>] [--measures <measure2>]...
```

You must specify a valid [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) using the environment variable `DATADOG_API_KEY` and the [Datadog site](https://docs.datadoghq.com/getting_started/site/) using the environment variable `DATADOG_SITE`.

The following example adds `error_rate` and `size` measures to the pipeline span:

```shell
DATADOG_SITE= datadog-ci measure --level pipeline --measures "error_rate:0.56" --measures "size:2327"
```

The following example adds a measure `binary.size` to the span for the currently running job:

```shell
DATADOG_SITE= datadog-ci measure --level job --measures "binary.size:`ls -l dst/binary | awk '{print \$5}' | tr -d '\n'`"
```

To create a measure, click the gear icon next to a measures name on the [Pipeline Executions page](https://app.datadoghq.com/ci/pipeline-executions) and click **Create Measure**.

## Add tags and measures to GitHub jobs{% #add-tags-and-measures-to-github-jobs %}

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
       - run: datadog-ci tag ...
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
       - run: datadog-ci tag ...
   ```

{% /collapsible-section %}

## Limitations{% #limitations %}

- The maximum amount of tags that can be added to a pipeline or job is 100.
- The maximum amount of measures that can be added to a pipeline or job is 100.
- The maximum length of a tag or measure is 300 characters (key + value).

## Further reading{% #further-reading %}

- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
- [Configure pipeline alerts with Datadog CI monitors](https://www.datadoghq.com/blog/configure-pipeline-alerts-with-ci-monitors/)
