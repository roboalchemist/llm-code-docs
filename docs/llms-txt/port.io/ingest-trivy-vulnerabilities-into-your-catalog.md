# Source: https://docs.port.io/guides/all/ingest-trivy-vulnerabilities-into-your-catalog.md

# Ingest Trivy vulnerabilities into your catalog

The following example shows you how to create a `trivyVulnerability` blueprint that ingests all vulnerabilities in your Trivy result file using Port's GitHub file ingesting feature.

To ingest the packages to Port, a `port-app-config.yml` file in the needed repository or organisation is used.

Recommended installation option

While the script provided in this example facilitates scheduled ingestion of Trivy scan results to Port, we highly recommend that you [use our Trivy Kubernetes exporter](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/templates/trivy.md) to continuously scan your kubernetes cluster and ingest vulnerabilities to Port in real time.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes:

* You have a Port account
* You have installed [Port's GitHub app](/build-your-software-catalog/sync-data-to-catalog/git/github/.md#setup) in your organisation or in repositories you are interested in.

## GitHub configuration[â](#github-configuration "Direct link to GitHub configuration")

To ingest GitHub objects, use one of the following methods:

* Using Port's UI
* Using GitHub

To manage your GitHub integration configuration using Port:

1. Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.
2. Under `Exporters`, click on your desired GitHub organization.
3. A window will open containing the default YAML configuration of your GitHub integration.
4. Here you can modify the configuration to suit your needs, by adding/removing entries.
5. When finished, click `resync` to apply any changes.

Using this method applies the configuration to all repositories that the GitHub app has permissions to.

When configuring the integration **using Port**, the YAML configuration is global, allowing you to specify mappings for multiple Port blueprints.

To manage your GitHub integration configuration using a config file in GitHub:

1. Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.
2. Under `Exporters`, click on your desired GitHub organization.
3. A window will open containing the default YAML configuration of your GitHub integration.
4. Scroll all the way down, and turn on the `Manage this integration using the "port-app-config.yml" file` toggle.

This will clear the configuration in Port's UI.

When configuring the integration **using GitHub**, you can choose either a global or granular configuration:

* **Global configuration:** create a `.github-private` repository in your organization and add the `port-app-config.yml` file to the repository.
  <!-- -->
  * Using this method applies the configuration to all repositories that the GitHub app has permissions to (unless it is overridden by a granular `port-app-config.yml` in a repository).
* **Granular configuration:** add the `port-app-config.yml` file to the `.github` directory of your desired repository.
  <!-- -->
  * Using this method applies the configuration only to the repository where the `port-app-config.yml` file exists.

When using global configuration **using GitHub**, the configuration specified in the `port-app-config.yml` file will only be applied if the file is in the **default branch** of the repository (usually `main`).

Important

When **using Port's UI**, the specified configuration will override any `port-app-config.yml` file in your GitHub repository/ies.

## Setting up the blueprint and mapping configuration[â](#setting-up-the-blueprint-and-mapping-configuration "Direct link to Setting up the blueprint and mapping configuration")

Create the following blueprint definition and webhook configuration:

**Trivy vulnerability blueprint (Click to expand)**

Create in Port

```
{
  "identifier": "trivyVulnerability",
  "description": "This blueprint represents a Trivy vulnerability in our software catalog",
  "title": "Trivy Vulnerability",
  "icon": "Trivy",
  "schema": {
    "properties": {
      "version": {
        "title": "Version",
        "type": "string"
      },
      "package_name": {
        "title": "Package Name",
        "type": "string"
      },
      "url": {
        "title": "Primary URL",
        "type": "string",
        "format": "url"
      },
      "description": {
        "title": "Description",
        "type": "string"
      },
      "target": {
        "title": "Target",
        "type": "string"
      },
      "severity": {
        "title": "Severity",
        "type": "string",
        "default": "HIGH",
        "enum": ["HIGH", "MEDIUM", "LOW", "CRITICAL", "UNKNOWN"],
        "enumColors": {
          "HIGH": "red",
          "MEDIUM": "yellow",
          "LOW": "green",
          "CRITICAL": "red",
          "UNKNOWN": "purple"
        }
      },
      "data_source": {
        "title": "Data Source",
        "type": "object"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

**Trivy mapping configuration**

```
- kind: file
  selector:
    query: 'true'
    files:
      - path: '**/result.json' # path to results json file
  port:
    itemsToParse: '[.file.content[] | select(.Vulnerabilities != null) as $input | .Vulnerabilities[] | {VulnerabilityID, PkgName, InstalledVersion, FixedVersion, Title, Description, Severity, References, PrimaryURL, DataSource, Target: $input.Target}]'
    entity:
      mappings:
        identifier: .item.VulnerabilityID
        title: .item.Title
        blueprint: '"trivyVulnerability"'
        properties:
          version: .item.InstalledVersion
          package_name: .item.PkgName
          primaryUrl: .item.PrimaryURL
          description: .item.Description
          target: .item.Target
          severity: .item.Severity
          data_source: .item.DataSource
```

Then click on `Resync` and wait for the entities to be ingested in your Port environment
