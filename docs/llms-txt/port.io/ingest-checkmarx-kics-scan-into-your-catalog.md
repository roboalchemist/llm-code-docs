# Source: https://docs.port.io/guides/all/ingest-checkmarx-kics-scan-into-your-catalog.md

# Ingest Checkmarx KICS scan into your catalog

The following example shows you how to create a `checkmarxScan` blueprint that ingests all scan results in your Checkmarx KICS file using Port's GitHub file ingesting feature.

To ingest the packages to Port, a `port-app-config.yml` file in the needed repository or organisation is used.

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

Create the following blueprint and mapping configuration:

**Checkmarx KICS blueprint (Click to expand)**

Create in Port

```
{
  "identifier": "checkmarxScan",
  "description": "This blueprint represents a Checkmarx KICS scan in our software catalog",
  "title": "Checkmarx Scans",
  "icon": "checkmarx",
  "schema": {
    "properties": {
      "severity": {
        "title": "Severity",
        "type": "string",
        "enum": ["LOW", "MEDIUM", "HIGH", "INFO"],
        "enumColors": {
          "LOW": "green",
          "MEDIUM": "yellow",
          "HIGH": "red",
          "INFO": "yellow"
        }
      },
      "url": {
        "type": "string",
        "title": "Scan URL",
        "format": "url"
      },
      "platform": {
        "title": "Platform",
        "type": "string"
      },
      "files": {
        "items": {
          "type": "object"
        },
        "title": "Files",
        "type": "array"
      },
      "cloud_provider": {
        "title": "Cloud Provider",
        "type": "string"
      },
      "description": {
        "title": "Description",
        "type": "string"
      },
      "category": {
        "title": "Category",
        "type": "string"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

**Checkmarx KICS mapping configuration (Click to expand)**

```
resources:
  - kind: file
    selector:
      query: 'true'
      files:
        - path: '**/results.json'
    port:
      itemsToParse: >-
        [.file.url as $url | .file.content.queries[] | {$url, query_id,
        query_name, severity, platform, files, cloud_provider, description,
        category}]
      entity:
        mappings:
          identifier: .item.query_id
          title: .item.query_name
          blueprint: '"checkmarxScan"'
          properties:
            category: .item.category
            cloud_provider: .item.cloud_provider
            description: .item.description
            files: .item.files
            severity: .item.severity
            platform: .item.platform
            url: .item.url
```

Then click on `Resync` and wait for the entities to be ingested in your Port environment
