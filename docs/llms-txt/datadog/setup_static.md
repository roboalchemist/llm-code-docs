# Source: https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_static.md

---
title: Set up SCA in your repositories
description: >-
  Learn about Datadog Software Composition Analysis to scan your imported
  open-source libraries for known security vulnerabilities before you ship to
  production.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Software Composition Analysis > Set
  up SCA in your repositories
---

# Set up SCA in your repositories

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog Software Composition Analysis (SCA) scans your repositories for open-source libraries and detects known security vulnerabilities before you ship to production.

To get started:

1. Open [Code Security settings](https://app.datadoghq.com/security/configuration/code-security/setup).
1. In **Activate scanning for your repositories**, click **Manage Repositories**.
1. Choose where to run SCA scans (Datadog-hosted or CI pipelines).
1. Follow the setup instructions for your source code provider.

### Supported languages and dependency manifests{% #supported-languages-and-dependency-manifests %}

Datadog SCA scans libraries in the following languages using dependency manifests (such as lockfiles and other supported manifest files) to identify vulnerable dependencies.

| Language | Package Manager | File                                  |
| -------- | --------------- | ------------------------------------- |
| C#       | .NET            | `packages.lock.json`, `.csproj` files |
| C++      | Conan           | `conan.lock`                          |
| Go       | mod             | `go.mod`                              |
| JVM      | Gradle          | `gradle.lockfile`                     |
| JVM      | Maven           | `pom.xml`                             |
| Node.js  | npm             | `package-lock.json`                   |
| Node.js  | pnpm            | `pnpm-lock.yaml`                      |
| Node.js  | yarn            | `yarn.lock`                           |
| PHP      | composer        | `composer.lock`                       |
| Python   | PDM             | `pdm.lock`                            |
| Python   | pip             | `requirements.txt`, `Pipfile.lock`    |
| Python   | poetry          | `poetry.lock`                         |
| Python   | UV              | `uv.lock`                             |
| Ruby     | bundler         | `Gemfile.lock`                        |
| Rust     | Cargo           | `cargo.lock`                          |

**Note:** If both a `packages.lock.json` and a `.csproj` file are present, the `packages.lock.json` takes precedence and provides more precise version resolution.

## Select where to run static SCA scans{% #select-where-to-run-static-sca-scans %}

By default, scans are automatically run upon each commit to a lockfile within an enabled repository. Default branch results are updated every hour to detect new vulnerabilities on existing packages.

### Scan with Datadog-hosted scanning{% #scan-with-datadog-hosted-scanning %}

You can run Datadog Static SCA scans directly on Datadog infrastructure. Supported repository types include:

- [GitHub](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_static/?tab=github#select-your-source-code-management-provider) (excluding repositories that use [Git Large File Storage](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage))
- [GitLab.com and GitLab Self-Managed](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_static/?tab=gitlab#select-your-source-code-management-provider)
- [Azure DevOps](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_static/?tab=azuredevops#select-your-source-code-management-provider)

To get started, navigate to the [**Code Security** page](https://app.datadoghq.com/security/configuration/code-security/setup).

{% alert level="info" %}
Datadog-hosted SCA scanning is not supported for repositories that contain file names longer than 255 characters.For these cases, scan using CI Pipelines.
{% /alert %}

### Scan in CI pipelines{% #scan-in-ci-pipelines %}

Datadog Static Code Analysis runs in your CI pipelines using the [`datadog-ci` CLI](https://docs.datadoghq.com/integrations/guide/source-code-integration).

Configure your Datadog API and application keys by adding `DD_APP_KEY` and `DD_API_KEY` as secrets. Make sure the application key has the `code_analysis_read` scope.

{% alert level="info" %}
You must scan your default branch at least once before results appear in Code Security.
{% /alert %}

## Select your source code management provider{% #select-your-source-code-management-provider %}

Datadog SCA supports all source code management providers, with native support for GitHub, GitLab, and Azure DevOps.

{% tab title="GitHub" %}
Configure a GitHub App with the [GitHub integration tile](https://docs.datadoghq.com/integrations/github/#link-a-repository-in-your-organization-or-personal-account) and set up the [source code integration](https://docs.datadoghq.com/integrations/guide/source-code-integration) to enable inline code snippets and [pull request comments](https://docs.datadoghq.com/security/code_security/dev_tool_int/github_pull_requests).

When installing a GitHub App, the following permissions are required to enable certain features:

- `Content: Read`, which allows you to see code snippets displayed in Datadog
- `Pull Request: Read & Write`, which allows Datadog to add feedback for violations directly in your pull requests using [pull request comments](https://docs.datadoghq.com/security/code_security/dev_tool_int/github_pull_requests).
- `Checks: Read & Write`, which allows you to create checks on SAST violations to block pull requests

{% /tab %}

{% tab title="GitLab" %}
See the [GitLab source code setup instructions](https://docs.datadoghq.com/integrations/gitlab-source-code/#setup) to connect GitLab to Datadog. Both GitLab.com and Self-Managed instances are supported.
{% /tab %}

{% tab title="Azure DevOps" %}
**Note:** Your Azure DevOps integrations must be connected to a Microsoft Entra tenant. Azure DevOps Server is **not** supported.

See the [Azure source code setup instructions](https://docs.datadoghq.com/integrations/azure-devops-source-code/#setup) to connect Azure DevOps repositories to Datadog.
{% /tab %}

{% tab title="Other" %}
If you are using another source code management provider, configure SCA to run in your CI pipelines using the `datadog-ci` CLI tool and upload the results to Datadog.
{% /tab %}

### Authentication{% #authentication %}

To upload results to Datadog, you must be authenticated. To ensure you're authenticated, configure the following environment variables:

| Name         | Description                                                                                                                                                                                                                    | Required | Default         |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- | --------------- |
| `DD_API_KEY` | Your Datadog API key. This key is created by your [Datadog organization](https://docs.datadoghq.com/security/code_security/software_composition_analysis/) and should be stored as a secret.                                   | Yes      |
| `DD_APP_KEY` | Your Datadog application key. This key, created by your [Datadog organization](https://app.datadoghq.com/security/configuration/code-security/setup), should include the `code_analysis_read` scope and be stored as a secret. | Yes      |
| `DD_SITE`    | The [Datadog site](https://docs.datadoghq.com/getting_started/site/) to send information to. Your Datadog site is .                                                                                                            | No       | `datadoghq.com` |

### Running options{% #running-options %}

There are two ways to run SCA scans from within your CI Pipelines:

- **Via Pipelines Integration** (GitHub Actions, Azure DevOps)
- **Via Customizable Script** (for any provider)

#### Run Via Pipelines Integration{% #run-via-pipelines-integration %}

You can run SCA scans automatically as part of your CI/CD workflows using built-in integrations for popular CI providers.

{% alert level="danger" %}
Datadog Software Composition Analysis CI jobs are only supported on `push` event trigger. Other event triggers (`pull_request`, for example) are not supported and can cause issues with the product.
{% /alert %}

{% tab title="GitHub" %}
**GitHub Actions**

SCA can run as a job in your GitHub Actions workflows. The action provided below invokes Datadog's recommended SBOM tool, [Datadog SBOM Generator](https://github.com/DataDog/datadog-sbom-generator), on your codebase and uploads the results into Datadog.

Add the following code snippet in `.github/workflows/datadog-sca.yml`.

Make sure to replace the `dd_site` attribute with the [Datadog site](https://docs.datadoghq.com/getting_started/site/) you are using.

In the `datadog-sca.yml` file:

```yaml
on: [push]

name: Datadog Software Composition Analysis

jobs:
  software-composition-analysis:
    runs-on: ubuntu-latest
    name: Datadog SBOM Generation and Upload
    steps:
    - name: Checkout
      uses: actions/checkout@v3
    - name: Check imported libraries are secure and compliant
      id: datadog-software-composition-analysis
      uses: DataDog/datadog-sca-github-action@main
      with:
        dd_api_key: ${{ secrets.DD_API_KEY }}
        dd_app_key: ${{ secrets.DD_APP_KEY }}
        dd_site: "datadoghq.com"
```

**Related GitHub Actions**

[Datadog Static Code Analysis (SAST)](https://docs.datadoghq.com/getting_started/code_security/?tab=datadoghosted#linking-services-to-code-violations-and-libraries) analyzes your first-party code. Static Code Analysis can be set up using the [`datadog-static-analyzer-github-action`](https://github.com/DataDog/datadog-static-analyzer-github-action) GitHub action.
{% /tab %}

{% tab title="Azure DevOps" %}
**Azure DevOps Pipelines**

To add a new pipeline in Azure DevOps, go to **Pipelines > New Pipeline**, select your repository, and then create/select a pipeline.

Add the following content to your Azure DevOps pipeline YAML file:

In the `datadog-sca.yml` file:

```yaml
trigger:
  branches:
    include:
      # Optionally specify a specific branch to trigger on when merging
      - "*"

variables:
  - group: "Datadog"

jobs:
  - job: DatadogSoftwareCompositionAnalysis
    displayName: "Datadog Software Composition Analysis"
    steps:
      - script: |
          npm install -g @datadog/datadog-ci
          export DATADOG_OSV_SCANNER_URL="https://github.com/DataDog/datadog-sbom-generator/releases/latest/download/datadog-sbom-generator_linux_amd64.zip"
          mkdir -p /tmp/datadog-sbom-generator
          curl -L -o /tmp/datadog-sbom-generator/datadog-sbom-generator.zip $DATADOG_OSV_SCANNER_URL
          unzip /tmp/datadog-sbom-generator/datadog-sbom-generator.zip -d /tmp/datadog-sbom-generator
          chmod 755 /tmp/datadog-sbom-generator/datadog-sbom-generator
          /tmp/datadog-sbom-generator/datadog-sbom-generator scan --output=/tmp/sbom.json .
          datadog-ci sbom upload /tmp/sbom.json
        env:
          DD_APP_KEY: $(DD_APP_KEY)
          DD_API_KEY: $(DD_API_KEY)
          DD_SITE: datadoghq.com
```

{% /tab %}

{% tab title="Other" %}
For all other providers, use the customizable script in the section below to run SCA scans and upload results to Datadog.
{% /tab %}

#### Run Via Customizable Script{% #run-via-customizable-script %}

If you use a different CI provider or want more control, you can run SCA scans using a customizable script. This approach lets you manually install and run the scanner, then upload results to Datadog from any environment.

{% alert level="info" %}
For non-GitHub repositories, run your first scan on the default branch.If your branch name is custom (not master, main, default, stable, source, prod, or develop), upload once and set the default branch in [Repository Settings](https://app.datadoghq.com/source-code/repositories).
{% /alert %}

Prerequisites:

- Unzip
- Node.js 14 or later

```bash
# Set the Datadog site to send information to
export DD_SITE="<YOUR_DATADOG_SITE>"

# Install dependencies
npm install -g @datadog/datadog-ci

# Download the latest Datadog SBOM Generator:
# https://github.com/DataDog/datadog-sbom-generator/releases
DATADOG_SBOM_GENERATOR_URL=https://github.com/DataDog/datadog-sbom-generator/releases/latest/download/datadog-sbom-generator_linux_amd64.zip

# Install Datadog SBOM Generator
mkdir /datadog-sbom-generator
curl -L -o /datadog-sbom-generator/datadog-sbom-generator.zip $DATADOG_SBOM_GENERATOR_URL
unzip /datadog-sbom-generator/datadog-sbom-generator.zip -d /datadog-sbom-generator
chmod 755 /datadog-sbom-generator/datadog-sbom-generator

# Run Datadog SBOM Generator to scan your dependencies
/datadog-sbom-generator/datadog-sbom-generator scan --output=/tmp/sbom.json /path/to/repository

# Upload results to Datadog
datadog-ci sbom upload /tmp/sbom.json
```

{% alert level="info" %}
This script uses the Linux x86_64 datadog-sbom-generator. For other systems, update the download URL. See all releases [here](https://github.com/DataDog/datadog-sbom-generator/releases).
{% /alert %}

## Upload third-party SBOM to Datadog{% #upload-third-party-sbom-to-datadog %}

Datadog recommends using the [Datadog SBOM generator](https://github.com/DataDog/datadog-sbom-generator), but it is also possible to ingest a third-party SBOM.

You can upload SBOMs generated by other tools if they meet these requirements:

- Valid CycloneDX [1.4](https://cyclonedx.org/docs/1.4/json/), [1.5](https://cyclonedx.org/docs/1.5/json/), or [1.6](https://cyclonedx.org/docs/1.6/json/) JSON schema
- All components have type `library`
- All components have a valid `purl` attribute

Third-party SBOM files are uploaded to Datadog using the [`datadog-ci`](https://github.com/DataDog/datadog-ci/?tab=readme-ov-file#how-to-install-the-cli) command.

You can find optional arguments and other information in the `datadog-ci` [README](https://github.com/DataDog/datadog-ci/tree/master/packages/plugin-sbom).

You can use the following command to upload your third-party SBOM. Ensure the environment variables `DD_API_KEY`, `DD_APP_KEY`, and `DD_SITE` are set to your API key, APP key, and [Datadog site](https://docs.datadoghq.com/getting_started/site/), respectively.

```bash
datadog-ci sbom upload /path/to/third-party-sbom.json
```

{% alert level="info" %}
If you already have automatic scanning enabled for a repository, a manual upload will replace any existing result for that commit.
{% /alert %}

## Link findings to Datadog services and teams{% #link-findings-to-datadog-services-and-teams %}

Datadog associates code and library scan results with Datadog services and teams to automatically route findings to the appropriate owners. This enables service-level visibility, ownership-based workflows, and faster remediation.

To determine the service where a vulnerability belongs, Datadog evaluates several mapping mechanisms in the order listed in this section.

Each vulnerability is mapped with one method only: if a mapping mechanism succeeds for a particular finding, Datadog does not attempt the remaining mechanisms for that finding.

{% alert level="danger" %}
Using service definitions that include code locations in the Software Catalog is the only way to explicitly control how static findings are mapped to services. The additional mechanisms described below, such as Error Tracking usage patterns and naming-based inference, are not user-configurable and depend on existing data from other Datadog products. Consequently, these mechanisms might not provide consistent mappings for organizations not using these products.
{% /alert %}

### Mapping using the Software Catalog (recommended){% #mapping-using-the-software-catalog-recommended %}

Services in the Software Catalog identify their codebase content using the `codeLocations` field. This field is available in the **Software Catalog [schema version `v3`](https://docs.datadoghq.com/software_catalog/service_definitions/v3-0/)** and allows a service to specify:

- a repository URL

```yaml
apiVersion: v3
kind: service
metadata:
  name: billing-service
  owner: billing-team
datadog:
  codeLocations:
    - repositoryURL: https://github.com/org/myrepo.git
```

- one or more code paths inside that repository

```yaml
apiVersion: v3
kind: service
metadata:
  name: billing-service
  owner: billing-team
datadog:
  codeLocations:
    - repositoryURL: https://github.com/org/myrepo.git
      paths:
        - path/to/service/code/**
```

If you want all the files in a repository to be associated with a service, you can use the glob `**` as follows:

```yaml
apiVersion: v3
kind: service
metadata:
  name: billing-service
  owner: billing-team
datadog:
  codeLocations:
    - repositoryURL: https://github.com/org/myrepo.git
      paths:
        - path/to/service/code/**
    - repositoryURL: https://github.com/org/billing-service.git
      paths:
        - "**"
```

The schema for this field is described in the [Software Catalog entity model](https://docs.datadoghq.com/internal_developer_portal/software_catalog/entity_model/?tab=v30#codelocations).

Datadog goes through all Software Catalog definitions and checks whether the finding's file path matches. For a finding to be mapped to a service through `codeLocations`, it must contain a file path.

Some findings might not contain a file path. In those cases, Datadog cannot evaluate `codeLocations` for that finding, and this mechanism is skipped.

{% alert level="danger" %}
Services defined with a Software Catalog schema v2.x do not support codeLocations. Existing definitions can be upgraded to the v3 schema in the Software Catalog. After migration is completed, changes might take up to 24 hours to apply to findings. If you are unable to upgrade to v3, Datadog falls back to alternative linking techniques (described below). These rely on less precise heuristics, so accuracy might vary depending on the Code Security product and your use of other Datadog features.
{% /alert %}

#### Example (v3 schema){% #example-v3-schema %}

```yaml
apiVersion: v3
kind: service
metadata:
  name: billing-service
  owner: billing-team
datadog:
  codeLocations:
    - repositoryURL: https://github.com/org/myrepo.git
      paths:
        - path/to/service/code/**
    - repositoryURL: https://github.com/org/billing-service.git
      paths:
        - "**"
```

#### SAST finding{% #sast-finding %}

If a vulnerability appeared in `github.com/org/myrepo` at `/src/billing/models/payment.py`, then using the `codeLocations` for `billing-service` Datadog would add `billing-service` as an owning service. If your service defines an `owner` (see above), then Datadog links that team to the finding too. In this case, the finding would be linked to the `billing-team`.

#### SCA finding{% #sca-finding %}

If a library was declared in `github.com/org/myrepo` at `/go.mod`, then Datadog would not match it to `billing-service`.

Instead, if it was declared in `github.com/org/billing-service` at `/go.mod`, then Datadog would match it to `billing-service` due to the `"**"` catch-all glob. Consequently, Datadog would link the finding to the `billing-team`.

{% alert level="info" %}
Datadog attempts to map a single finding to as many services as possible. If no matches are found, Datadog continues onto the next linking method.
{% /alert %}

### When the Software Catalog cannot determine the service{% #when-the-software-catalog-cannot-determine-the-service %}

If the Software Catalog does not provide a match, either because the finding's file path does not match any `codeLocations`, or because the service uses the v2.x schema, Datadog evaluates whether Error Tracking can identify the service associated with the code. Datadog uses only the last 30 days of Error Tracking data due to product [data-retention limits](https://docs.datadoghq.com/data_security/data_retention_periods/).

When Error Tracking processes stack traces, the traces often include file paths. For example, if an error occurs in: `/foo/bar/baz.py`, Datadog inspects the directory: `/foo/bar`. Datadog then checks whether the finding's file path resides under that directory.

**If the finding file is under the same directory:**

- Datadog treats this as a strong indication that the vulnerability belongs to the same service.
- The finding inherits the *service* and *team* associated with that error in Error Tracking.

If this mapping succeeds, Datadog stops here.

### Service inference from file paths or repository names{% #service-inference-from-file-paths-or-repository-names %}

When neither of the above strategies can determine the service, Datadog inspects naming patterns in the repository and file paths.

Datadog evaluates whether:

- The file path contains identifiers matching a known service.
- The repository name corresponds to a service name.

When using the finding's file path, Datadog performs a reverse search on each path segment until it finds a matching service or exhausts all options.

For example, if a finding occurs in `github.com/org/checkout-service` at `/foo/bar/baz/main.go`, Datadog takes the last path segment, `main`, and sees if any Software Catalog service uses that name. If there is a match, the finding is attributed to that service. If not, the process continues with `baz`, then `bar`, and so on.

When all options have been tried, Datadog checks whether the repository name, `checkout-service`, matches a Software Catalog service name. If no match is found, Datadog is unsuccessful at linking your finding using Software Catalog.

This mechanism ensures that findings receive meaningful service attribution when no explicit metadata exists.

### Link findings to teams through Code Owners{% #link-findings-to-teams-through-code-owners %}

If Datadog is able to link your finding to a service using the above strategies, then the team that owns that service (if defined) is associated with that finding automatically.

Regardless of whether Datadog successfully links a finding to a service (and a Datadog team), Datadog uses the `CODEOWNERS` information from your finding's repository to link Datadog and GitHub teams to your findings.

{% alert level="info" %}
You must accurately map your Git provider teams to your [Datadog Teams](https://docs.datadoghq.com/account_management/teams/) for team attribution to function properly.
{% /alert %}

## Filter by reachable vulnerabilities{% #filter-by-reachable-vulnerabilities %}

Datadog offers static reachability analysis to help teams assess whether vulnerable code paths in dependencies are referenced within their application code. This capability supports more effective prioritization by identifying vulnerabilities that are statically unreachable and therefore present minimal immediate risk.

This functionality is supported only when using the [Datadog SBOM Generator](https://docs.datadoghq.com/security/code_security/software_composition_analysis/) with the `--reachability` flag enabled or when running scans through Datadog-hosted infrastructure.

Reachability analysis is available exclusively for Java projects and applies only to a defined set of vetted security advisories. Vulnerabilities not included in this set are excluded from reachability evaluation.

{% collapsible-section open=null #id-for-anchoring %}
#### Supported advisories

Static reachability analysis is available for the following advisories:

- [GHSA-h7v4-7xg3-hxcc](https://osv.dev/vulnerability/GHSA-h7v4-7xg3-hxcc)

- [GHSA-jfh8-c2jp-5v3q](https://osv.dev/vulnerability/GHSA-jfh8-c2jp-5v3q)

- [GHSA-7rjr-3q55-vv33](https://osv.dev/vulnerability/GHSA-7rjr-3q55-vv33)

- [GHSA-2p3x-qw9c-25hh](https://osv.dev/vulnerability/GHSA-2p3x-qw9c-25hh)

- [GHSA-cm59-pr5q-cw85](https://osv.dev/vulnerability/GHSA-cm59-pr5q-cw85)

- [GHSA-qrx8-8545-4wg2](https://osv.dev/vulnerability/GHSA-qrx8-8545-4wg2)

- [GHSA-p8pq-r894-fm8f](https://osv.dev/vulnerability/GHSA-p8pq-r894-fm8f)

- [GHSA-64xx-cq4q-mf44](https://osv.dev/vulnerability/GHSA-64xx-cq4q-mf44)

- [GHSA-g5w6-mrj7-75h2](https://osv.dev/vulnerability/GHSA-g5w6-mrj7-75h2)

- [GHSA-xw4p-crpj-vjx2](https://osv.dev/vulnerability/GHSA-xw4p-crpj-vjx2)

- [GHSA-cxfm-5m4g-x7xp](https://osv.dev/vulnerability/GHSA-cxfm-5m4g-x7xp)

- [GHSA-3ccq-5vw3-2p6x](https://osv.dev/vulnerability/GHSA-3ccq-5vw3-2p6x)

- [GHSA-mjmj-j48q-9wg2](https://osv.dev/vulnerability/GHSA-mjmj-j48q-9wg2)

- [GHSA-36p3-wjmg-h94x](https://osv.dev/vulnerability/GHSA-36p3-wjmg-h94x)

- [GHSA-ww97-9w65-2crx](https://osv.dev/vulnerability/GHSA-ww97-9w65-2crx)

- [GHSA-8jrj-525p-826v](https://osv.dev/vulnerability/GHSA-8jrj-525p-826v)

- [GHSA-4wrc-f8pq-fpqp](https://osv.dev/vulnerability/GHSA-4wrc-f8pq-fpqp)

- [GHSA-4cch-wxpw-8p28](https://osv.dev/vulnerability/GHSA-4cch-wxpw-8p28)

- [GHSA-6w62-hx7r-mw68](https://osv.dev/vulnerability/GHSA-6w62-hx7r-mw68)

- [GHSA-2q8x-2p7f-574v](https://osv.dev/vulnerability/GHSA-2q8x-2p7f-574v)

- [GHSA-rmr5-cpv2-vgjf](https://osv.dev/vulnerability/GHSA-rmr5-cpv2-vgjf)

- [GHSA-4jrv-ppp4-jm57](https://osv.dev/vulnerability/GHSA-4jrv-ppp4-jm57)

- [GHSA-mw36-7c6c-q4q2](https://osv.dev/vulnerability/GHSA-mw36-7c6c-q4q2)

- [GHSA-hph2-m3g5-xxv4](https://osv.dev/vulnerability/GHSA-hph2-m3g5-xxv4)

- [GHSA-j9h8-phrw-h4fh](https://osv.dev/vulnerability/GHSA-j9h8-phrw-h4fh)

- [GHSA-3gm7-v7vw-866c](https://osv.dev/vulnerability/GHSA-3gm7-v7vw-866c)

- [GHSA-645p-88qh-w398](https://osv.dev/vulnerability/GHSA-645p-88qh-w398)

- [GHSA-g5h3-w546-pj7f](https://osv.dev/vulnerability/GHSA-g5h3-w546-pj7f)

- [GHSA-c27h-mcmw-48hv](https://osv.dev/vulnerability/GHSA-c27h-mcmw-48hv)

- [GHSA-r4x2-3cq5-hqvp](https://osv.dev/vulnerability/GHSA-r4x2-3cq5-hqvp)

- [GHSA-24rp-q3w6-vc56](https://osv.dev/vulnerability/GHSA-24rp-q3w6-vc56)

- [GHSA-c9hw-wf7x-jp9j](https://osv.dev/vulnerability/GHSA-c9hw-wf7x-jp9j)

- [GHSA-4gq5-ch57-c2mg](https://osv.dev/vulnerability/GHSA-4gq5-ch57-c2mg)

- [GHSA-vmfg-rjjm-rjrj](https://osv.dev/vulnerability/GHSA-vmfg-rjjm-rjrj)

- [GHSA-crg9-44h2-xw35](https://osv.dev/vulnerability/GHSA-crg9-44h2-xw35)

- [GHSA-qmqc-x3r4-6v39](https://osv.dev/vulnerability/GHSA-qmqc-x3r4-6v39)

- [GHSA-4w82-r329-3q67](https://osv.dev/vulnerability/GHSA-4w82-r329-3q67)

- [GHSA-qr7j-h6gg-jmgc](https://osv.dev/vulnerability/GHSA-qr7j-h6gg-jmgc)

- [GHSA-9mxf-g3x6-wv74](https://osv.dev/vulnerability/GHSA-9mxf-g3x6-wv74)

- [GHSA-f3j5-rmmp-3fc5](https://osv.dev/vulnerability/GHSA-f3j5-rmmp-3fc5)

{% /collapsible-section %}

## Data Retention{% #data-retention %}

Datadog stores findings in accordance with our [Data Rentention Periods](https://docs.datadoghq.com/data_security/data_retention_periods/). Datadog does not store or retain customer source code.

## Further Reading{% #further-reading %}

- [Set up runtime detection of library vulnerabilities](https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_runtime/)

- [Static Code Analysis (SAST)](https://docs.datadoghq.com/security/code_security/static_analysis/)
- [Infrastructure as Code (IaC)](https://docs.datadoghq.com/security/cloud_security_management/iac_scanning/)
- [Secrets Scanning](https://docs.datadoghq.com/security/code_security/secret_scanning/)
