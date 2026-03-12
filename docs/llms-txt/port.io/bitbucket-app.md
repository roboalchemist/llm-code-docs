# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-app.md

# Bitbucket app (deprecated)

Port's Bitbucket App integration allows you to model Bitbucket resources in your software catalog and ingest data into them.

Deprecation Notice

This app will be deprecated in the future and support for the app will be discontinued soon.

To integrate Port with Bitbucket Cloud, we recommend using the [Bitbucket Cloud integration](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-cloud/.md).

This documentation covers Port's integration with **Bitbucket Cloud**. For information about integrating with Bitbucket Server (Self-Hosted), please refer to the [Bitbucket Server integration documentation](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-server/.md).

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired Bitbucket resources and their metadata in Port (see supported resources below).
* Watch for Bitbucket object changes (create/update/delete) in real-time, and automatically apply the changes to your software catalog.
* Manage Port entities using GitOps.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Bitbucket into Port are listed below.<br /><!-- -->It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`repository`](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-get)
* [`pull-request`](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-get)
* [`folder`](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-repositories-workspace-repo-slug-src-commit-path-get)

## Setup[â](#setup "Direct link to Setup")

To install Port's Bitbucket app, follow these steps:

1. Go to the [Bitbucket app installation page](https://marketplace.atlassian.com/apps/1229886/port-connector-for-bitbucket?hosting=cloud\&tab=overview).

2. Click `Get it now`.

3. Select your desired workspace and click on `Grant access`.

4. Once the installation has finished, you will be redirected to Port.

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration for this integration:

**Default mapping configuration (Click to expand)**

```
deleteDependentEntities: true
createMissingRelatedEntities: true
enableMergeEntity: true
resources:
- kind: repository
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .name
        title: .name
        blueprint: '"bitbucketRepository"'
        properties:
          url: .links.html.href
          defaultBranch: .main_branch
          last_activity: .updated_on
- kind: pull-request
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .destination.repository.name + (.id|tostring)
        title: .title
        blueprint: '"bitbucketPullRequest"'
        properties:
          status: .state
          createdAt: .created_on
          updatedAt: .updated_on
          link: .links.html.href
        relations:
          repository: .destination.repository.name
          bitbucket_creator: .author.display_name | gsub(" ";"_")
          bitbucket_assignees: .participants | map(.user.display_name) | map(gsub(" ";"_"))
          bitbucket_reviewers: .reviewers | map(.display_name) | map(gsub(" ";"_"))
          service:
            combinator: '"and"'
            rules:
            - operator: '"="'
              property: '"bitbucket_repository"'
              value: .destination.repository.name
          creator:
            combinator: '"and"'
            rules:
            - operator: '"="'
              property: '"bitbucket_username"'
              value: .author.display_name | gsub(" ";"_")
          assignees:
            combinator: '"and"'
            rules:
            - operator: '"in"'
              property: '"bitbucket_username"'
              value: .participants | map(.user.display_name) | map(gsub(" ";"_"))
          reviewers:
            combinator: '"and"'
            rules:
            - operator: '"in"'
              property: '"bitbucket_username"'
              value: .reviewers | map(.display_name) | map(gsub(" ";"_"))
```

To ingest Bitbucket objects, use one of the following methods:

* Using Port's UI
* Using Bitbucket

To manage your Bitbucket integration configuration using Port:

1. Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.
2. Under `Exporters`, click on your desired BitBucket organization.
3. A window will open containing the default YAML configuration of your BitBucket integration.
4. Here you can modify the configuration to suit your needs, by adding/removing entries.
5. When finished, click `resync` to apply any changes.

Using this method applies the configuration to all repositories in your Bitbucket workspace.

When configuring the integration **using Port**, the YAML configuration is global, allowing you to specify mappings for multiple Port blueprints.

To manage your Bitbucket integration configuration using a config file in BitBucket:

1. Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.
2. Under `Exporters`, click on your desired BitBucket organization.
3. A window will open containing the default YAML configuration of your GitHub integration.
4. Scroll all the way down, and turn on the `Manage this integration using the "port-app-config.yml" file` toggle.

This will clear the configuration in Port's UI.

When configuring the integration **using BitBucket**, you can choose either a global or granular configuration:

* **Global configuration:** create a `.bitbucket-private` repository in your workspace and add the `port-app-config.yml` file to the repository;
  <!-- -->
  * Using this method applies the configuration to all repositories in your Bitbucket workspace (unless it is overridden by a granular `port-app-config.yml` in a repository);
* **Granular configuration:** add the `port-app-config.yml` file to the root of your desired repository;
  <!-- -->
  * Using this method applies the configuration only to the repository where the `port-app-config.yml` file exists.

When using global configuration **using Bitbucket**, the configuration specified in the `port-app-config.yml` file will only be applied if the file is in the **default branch** of the repository (usually `main`).

Important

When **using Port's UI**, the specified configuration will override any `port-app-config.yml` file in your BitBucket repository/ies.

## Capabilities[â](#capabilities "Direct link to Capabilities")

### Ingesting Git objects[â](#ingesting-git-objects "Direct link to Ingesting Git objects")

By using Port's Bitbucket app, you can automatically ingest Bitbucket resources into Port based on real-time events.

The app allows you to ingest a variety of objects resources provided by the Bitbucket API, including repositories, pull requests and more. It also allows you to perform "extract, transform, load (ETL)" on data from the Bitbucket API into the desired software catalog data model.

The Bitbucket app uses a YAML configuration file to describe the ETL process to load data into the developer portal. The approach reflects a golden middle between an overly opinionated Git visualization that might not work for everyone and a too-broad approach that could introduce unneeded complexity into the developer portal.

After installing the app, Port will automatically create a `repository` blueprint in your catalog (representing a BitBucket repository), along with a default YAML configuration file that defines where the data fetched from BitBucket's API should go in the blueprint.

## Permissions[â](#permissions "Direct link to Permissions")

Port's Bitbucket integration requires the following scopes:

* `account`;
* `repository`;
* `pullrequest`.

Default permissions

You will be prompted to confirm these permissions when first installing the App.

## Examples[â](#examples "Direct link to Examples")

Refer to the [examples](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-app/examples.md) page for practical configurations and their corresponding blueprint definitions.

## Relevant Guides[â](#relevant-guides "Direct link to Relevant Guides")

For relevant guides and examples, see the [guides section](https://docs.port.io/guides?tags=BitBucket).

## GitOps[â](#gitops "Direct link to GitOps")

Port's Bitbucket app also provides GitOps capabilities, refer to the [GitOps](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-app/gitops/.md) page to learn more.

## Advanced[â](#advanced "Direct link to Advanced")

Refer to the [advanced](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-app/advanced.md) page for advanced use cases and examples.
