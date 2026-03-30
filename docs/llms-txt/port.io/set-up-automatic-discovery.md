# Source: https://docs.port.io/getting-started/set-up-automatic-discovery.md

# Set up automatic data mapping

As part of the onboarding process, Port allows you to create new `services`, `workloads`, `environments`, `users`, and `teams` via the UI.<br /><!-- -->This involves manually selecting the components related to the new [entity]().

These are routine actions that most organizations perform on a regular basis, which is why this manual process is not efficient or scalable.

This guide will walk you through automating the process of creating and updating these entities in a way that suits your organization's standards.

Component definitions

Not sure what these entities mean? See their definitions [here](/getting-started/default-components.md).

## Methods[â](#methods "Direct link to Methods")

This page describes three methods you can use to automatically map and update entities in your catalog:

1. Use the catalog auto discovery which utilizes AI to analyze your existing catalog data and suggest missing entities.
2. Define one of your external tools as a "source of truth" for the resources you want to ingest.
3. Use metadata from your external tools (e.g. labels, naming conventions) to identify and update an [entity]() in Port.

Methods two and three require modifying the [mapping configuration](/build-your-software-catalog/customize-integrations/configure-mapping.md) of the relevant integration.

**How to modify a mapping configuration (click to expand)**

1. Go to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.
2. Under "Exporters", find the relevant integration and click on it.
3. A window will open, containing the mapping configuration. Use the editor in the bottom-left corner to update the configuration.
4. Click on the "Save & Resync" button to save the changes and resync the integration.

## 1. Catalog auto discovery[â](#1-catalog-auto-discovery "Direct link to 1. Catalog auto discovery")

The **auto discovery** capability uses [Port AI](/ai-interfaces/port-ai/overview.md) to discover entities and their relations. It is particularly useful for discovering entities that are not automatically created through integrations, such as `services` and `users`.

To learn more about how Port AI uses your data, see the [security and data controls](/ai-interfaces/port-ai/security-and-data-controls.md) documentation.

### Examples[â](#examples "Direct link to Examples")

To use catalog auto discovery, navigate to the [Catalog](https://app.port.io/organization/catalog) page, open the catalog page of the blueprint you want to discover, click the ![](/img/icons/AI-icon.svg)![](/img/icons/AI-dark-icon.svg) button, and select related blueprints to analyze.

**Providing a prompt is highly recommended** and gives the best and most accurate results.<br /><!-- -->When you enable `Advanced configuration`, you can provide specific instructions that guide the AI to identify patterns relevant to your organization.

**Example 1: Discover services from a monorepo**

If you have a monorepo structure with multiple services, you can discover `service` entities by analyzing your GitHub repositories.

**Recommended prompt:**

```
Services are represented as code in a repository.  
Check the file structure of each repository to identify services.  
Services may be found in specific folders, such as "apps" or "services".
```

Add the relevant blueprints to base the auto discovery on, for example: `GitHub Repository`.

***

**Example 2: Discover services from individual repositories**

If you have individual repositories and want to identify which ones represent services, you can use catalog auto discovery with both GitHub and PagerDuty data.

**Recommended prompt:**

```
Focus on repos that have keywords that can indicate they are services (e.g., "service", "ms", "srv").  
Ignore repos of libraries and packages. Having also a PagerDuty service with a similar name as a repo  
is a strong indication that this is a service.
```

Add the relevant blueprints to base the auto discovery on, for example: `GitHub Repository`, `PagerDuty Service`.

***

**Example 3: Discover users from development activity**

If you want to identify users who contribute to your codebase but don't yet exist in your catalog, you can analyze pull requests and issues.

**Recommended prompt:**

```
Check "Jira issues" assignees and "pull requests" to identify developers in the organization.
```

Add the relevant blueprints to base the auto discovery on, for example: `Jira Issue`, `Jira User` ,`Pull Requests`.

***

Once the discovery process is complete, you can review, edit, approve, or decline the suggested entities individually or in bulk.

For more information, see the [catalog auto discovery](/build-your-software-catalog/catalog-auto-discovery.md) documentation.

## 2. Define a source of truth[â](#2-define-a-source-of-truth "Direct link to 2. Define a source of truth")

This approach is useful when you want to create entities of a specific type (e.g. services, environments, teams, users) based on resources from a specific external tool.

### Full example[â](#full-example "Direct link to Full example")

One example that works for many organizations is to define a **Git repository** as a source of truth for `services`, and automatically create a new `service` in Port for each repository in your Git provider.

To achieve this, we need to update the mapping configuration of the Git integration to include an entry for the `service` [blueprint]().<br /><!-- -->Here is an example using the `GitHub` integration:

```
- kind: repository
  selector:
    query: 'true'
    teams: true
  port:
    entity:
      mappings:
        identifier: .full_name
        title: .name
        blueprint: '"githubRepository"'
        properties:
          readme: file://README.md
          url: .html_url
          defaultBranch: .default_branch
        relations:
          githubTeams: '[.teams[].id | tostring]'
- kind: repository
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .full_name
        title: .full_name
        blueprint: '"service"'
        relations:
          repository: .full_name
```

The first `kind` block is the default mapping when installing the GitHub integration. The meaning of this block is:<br />*For every repository in the GitHub organization, create a new `githubRepository` entity in Port with the specified properties*.

The second `kind` block is the one we need to add. The meaning of this block is:<br />*For every repository in the GitHub organization, create a new `service` entity in Port, and relate it to the relevant `githubRepository` entity*.

With this approach, `services` will always have a related repository upon creation, and can later be enriched with additional data from other assets in your catalog.

### Additional examples by integration[â](#additional-examples-by-integration "Direct link to Additional examples by integration")

Just like the example above, the blocks in the examples below can be added to the mapping configuration of the relevant integration to automatically create entities in your catalog.

* Services
* Environments
* Workloads
* Users
* Teams

Common examples for resources that can be used as a source of truth for `services`:

![](/img/guides/icons/GitHub.svg)![](/img/guides/icons/dark/GitHub.svg) **GitHub repository (click to expand)**

```
- kind: repository
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .full_name
        title: .full_name
        blueprint: '"service"'
        relations:
          repository: .full_name
```

#### Monorepo support

If you are using a monorepo, see the [working with monorepos](/build-your-software-catalog/sync-data-to-catalog/git/working-with-monorepos.md?git-provider=github) page to learn how to tweak the mapping configuration to create entities for each folder in the repository.

Once you have done this, you can add the following block to the mapping configuration to create a `service` entity for each folder in the repository, and relate it to the relevant `githubRepository` entity:

```
# Be sure to change the `path` and `repos` values to match your monorepo structure
- kind: folder
  selector:
    query: "true"
    folders: # Specify the repositories and folders to include under this relative path
      - path: apps/* # Relative path to the folders within the repositories
        repos: # List of repositories to include folders from
          - backend-service
          - frontend-service
  port:
    entity:
      mappings:
        identifier: ".folder.name"
        title: ".folder.name"
        blueprint: '"service"'
        relations:
          repository: ".folder.name"
```

![](/img/guides/icons/GitLab.svg)![](/img/guides/icons/GitLab.svg) **GitLab project (click to expand)**

```
- kind: project
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .path_with_namespace | gsub(" "; "")
        title: .name
        blueprint: '"service"'
        relations:
          git_lab_repositry: .path_with_namespace | gsub(" "; "")
```

#### Monorepo support

If you are using a monorepo, see the [working with monorepos](/build-your-software-catalog/sync-data-to-catalog/git/working-with-monorepos.md?git-provider=gitlab) page to learn how to tweak the mapping configuration to create entities for each folder in the repository.

Once you have done this, you can add the following block to the mapping configuration to create a `service` entity for each folder in the repository, and relate it to the relevant `gitlabRepository` entity:

```
# Be sure to change the `path` and `repos` values to match your monorepo structure
- kind: folder
  selector:
    query: "true"
    folders: # Specify the repositories and folders to include under this relative path
      - path: "apps/" # Relative path to the folders within the repositories
        repos: # List of repositories to include folders from
          - backend-service
          - frontend-service
  port:
    entity:
      mappings:
        identifier: .folder.name
        title: .folder.name
        blueprint: '"service"'
        relations:
          git_lab_repositry: .folder.name
```

![](/img/guides/icons/BitBucket.svg)![](/img/guides/icons/BitBucket.svg) **Bitbucket repository (click to expand)**

```
- kind: repository
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .name
        title: .name
        blueprint: '"service"'
        relations:
          bitbucketRepository: .name
```

#### Monorepo support

If you are using a monorepo, see the [working with monorepos](/build-your-software-catalog/sync-data-to-catalog/git/working-with-monorepos.md?git-provider=bitbucket) page to learn how to tweak the mapping configuration to create entities for each folder in the repository.

Once you have done this, you can add the following block to the mapping configuration to create a `service` entity for each folder in the repository, and relate it to the relevant `bitbucketRepository` entity:

```
# Be sure to change the `path` and `repos` values to match your monorepo structure
- kind: folder
  selector:
    query: "true"
    folders: # Specify the repositories and folders to include under this relative path
      - path: apps/* # Relative path to the folders within the repositories
        repos: # List of repositories to include folders from
          - backend-service
          - frontend-service
  port:
    entity:
      mappings:
        identifier: .folder.name
        blueprint: '"service"'
        relations:
          bitbucketRepository: .folder.name
```

![](/img/guides/icons/AzureDevops.svg)![](/img/guides/icons/AzureDevops.svg) **Azure DevOps repository (click to expand)**

```
- kind: repository
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: >-
          "\(.project.name | ascii_downcase | gsub("[ ();]"; ""))/\(.name | ascii_downcase | gsub("[ ();]"; ""))"
        title: .name
        blueprint: '"service"'
        properties:
          url: .remoteUrl
          readme: file://README.md
          defaultBranch: .defaultBranch
        relations:
          service: >-
            "\(.project.name | ascii_downcase | gsub("[ ();]"; ""))/\(.name | ascii_downcase | gsub("[ ();]"; ""))"
```

![](/img/guides/icons/SonarQube.svg)![](/img/guides/icons/SonarQube.svg) **SonarQube project (click to expand)**

```
- kind: projects_ga
  selector:
    query: 'true'
    apiFilters:
      qualifier:
        - TRK
    metrics:
      - code_smells
      - coverage
      - bugs
      - vulnerabilities
      - duplicated_files
      - security_hotspots
      - new_violations
      - new_coverage
      - new_duplicated_lines_density
  port:
    entity:
      mappings:
        identifier: .key
        title: .name
        blueprint: '"service"'
        relations:
          sonar_project: .key
```

![](/img/guides/icons/Snyk.svg)![](/img/guides/icons/Snyk.svg) **Snyk target (click to expand)**

```
- kind: target
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .attributes.display_name
        blueprint: '"service"'
        relations:
          snyk_target: .id
```

![](/img/guides/icons/PagerDuty.svg)![](/img/guides/icons/PagerDuty.svg) **PagerDuty service (click to expand)**

```
- kind: services
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"service"'
        relations:
          pager_duty_service: .id
```

![](/img/guides/icons/OpsGenie.svg)![](/img/guides/icons/OpsGenie.svg) **OpsGenie service (click to expand)**

```
- kind: service
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"service"'
        relations:
          _opsGenieService: .id
```

Common examples for resources that can be used as a source of truth for `environments`:

![](/img/guides/icons/Kubernetes.svg)![](/img/guides/icons/Kubernetes.svg) **Kubernetes cluster (click to expand)**

```
- kind: v1/namespaces
  selector:
    query: .metadata.name | contains("kube-system")
  port:
    entity:
      mappings:
        - identifier: env.CLUSTER_NAME
          title: env.CLUSTER_NAME
          blueprint: '"environment"'
          relations:
            k8s_cluster: env.CLUSTER_NAME
```

![](/img/guides/icons/ArgoCD.svg)![](/img/guides/icons/ArgoCD.svg) **ArgoCD cluster (click to expand)**

```
- kind: cluster
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .name
        title: .name
        blueprint: '"environment"'
        relations:
          argo_cluster: .name
```

Common examples for resources that can be used as a source of truth for `workloads`:

![](/img/guides/icons/Kubernetes.svg)![](/img/guides/icons/Kubernetes.svg) **Kubernetes workload (click to expand)**

```
- kind: apps/v1/deployments
  selector:
    query: .metadata.namespace | startswith("kube") | not
  port:
    entity:
      mappings:
        - identifier: >-
            .metadata.name + "-Deployment-" + .metadata.namespace + "-" + env.CLUSTER_NAME
          title: .metadata.name
          blueprint: '"workload"'
          relations:
            k8s_workload: .metadata.name + "-Deployment-" + .metadata.namespace + "-" + env.CLUSTER_NAME
```

![](/img/guides/icons/ArgoCD.svg)![](/img/guides/icons/ArgoCD.svg) **ArgoCD application (click to expand)**

```
- kind: application
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.uid
        title: .metadata.name
        blueprint: '"workload"'
        properties:
            version: .status.summary.images[0] | split(":")[-1]
        relations:
          argo_application: .metadata.uid
```

![](/img/guides/icons/Datadog.svg)![](/img/guides/icons/dark/Datadog.svg) **Datadog service (click to expand)**

```
- kind: service
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .attributes.schema."dd-service"
        title: .attributes.schema."dd-service"
        blueprint: '"workload"'
        relations:
          datadog_service: .attributes.schema."dd-service"
```

![](/img/guides/icons/Sentry.svg)![](/img/guides/icons/dark/Sentry.svg) **Sentry project (click to expand)**

```
- kind: project-tag
  selector:
    query: 'true'
    tag: environment
  port:
    entity:
      mappings:
        identifier: .slug + "-" + .__tags.name
        title: .name + "-" + .__tags.name
        blueprint: '"workload"'
        relations:
          sentry_project: .slug + "-" + .__tags.name
```

![](/img/guides/icons/Dynatrace.svg)![](/img/guides/icons/Dynatrace.svg) **Dynatrace entity (click to expand)**

```
- kind: entity
  selector:
    query: 'true'
    entityFields: firstSeenTms,lastSeenTms,tags
    entityTypes:
      - APPLICATION
      - SERVICE
  port:
    entity:
      mappings:
        identifier: .entityId
        title: .displayName
        blueprint: '"workload"'
        relations:
          dynatrace_entity: .entityId
```

Common examples for resources that can be used as a source of truth for `users`:

![](/img/guides/icons/GitHub.svg)![](/img/guides/icons/dark/GitHub.svg) **GitHub user (click to expand)**

```
- kind: user
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .login
        title: .login
        blueprint: '"_user"'
        relations:
          git_hub_user: .login
```

![](/img/guides/icons/GitLab.svg)![](/img/guides/icons/GitLab.svg) **GitLab user (click to expand)**

```
- kind: group-with-members
  selector:
    query: 'true'
    includeBotMembers: 'true'
    includeInheritedMembers: 'true'
  port:
    itemsToParse: .__members
    entity:
      mappings:
        identifier: .item.username
        title: .item.name
        blueprint: '"_user"'
        relations:
          gitlab_user: .item.username
```

![](/img/guides/icons/AzureDevops.svg)![](/img/guides/icons/AzureDevops.svg) **Azure DevOps user (click to expand)**

```
- kind: user
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: '.id'
        title: '.user.displayName'
        blueprint: '"_user"'
        relations:
          azure_devops_user: '.id'
```

Common examples for resources that can be used as a source of truth for `teams`:

![](/img/guides/icons/GitHub.svg)![](/img/guides/icons/dark/GitHub.svg) **GitHub team (click to expand)**

```
- kind: team
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id | tostring
        title: .name
        blueprint: '"_team"'
        relations:
          git_hub_team: .id | tostring
```

![](/img/guides/icons/GitLab.svg)![](/img/guides/icons/GitLab.svg) **GitLab team (click to expand)**

```
- kind: group-with-members
  selector:
    query: 'true'
    includeBotMembers: 'true'
  port:
    entity:
      mappings:
        identifier: .full_path
        title: .name
        blueprint: '"_team"'
        relations:
          gitlab_group: .full_path
```

![](/img/guides/icons/AzureDevops.svg)![](/img/guides/icons/AzureDevops.svg) **Azure DevOps team (click to expand)**

```
- kind: team
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"_team"'
        relations:
          azure_devops_team: .id
```

## 3. Use predefined metadata[â](#3-use-predefined-metadata "Direct link to 3. Use predefined metadata")

In addition to defining "sources of truth", you can use data from your external tools to identify and update entities in Port.<br /><!-- -->This is useful when you want to update entities of a specific type (e.g. services, environments, teams, users) based on a label, naming convention, or other piece of metadata in a specific external tool.

See below for various examples of how to implement this.

### Identifier is **known**[â](#identifier-is-known "Direct link to identifier-is-known")

The most straightforward way to identify and update an [entity]() is to have its identifier somewhere in the metadata of the external tool, for instance:

* In a label/tag.
* Using a naming convention, e.g. naming all PagerDuty services with the prefix `service-<identifier>`.

Here are some examples:

* Service
* Workload

After installing the `PagerDuty` integration and ingesting our PagerDuty services, we may want to automatically connect them to their corresponding `service` [entities]().

To achieve this, we need to update the mapping configuration of the PagerDuty integration to include an entry for the `service` [blueprint]().

This example assumes that each PagerDuty service has a label named `portService` with the value being the identifier of the relevant `service` [entity]() in Port.

```
- kind: services
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.labels.portService
        blueprint: '"service"'
        relations:
          pager_duty_service: .id
```

The meaning of this configuration is:<br />*For every PagerDuty service ingested from PagerDuty, update the `service` entity with the identifier matching the `portService` label, relating it to this `pagerdutyService` entity*.

After installing the `Kubernetes` integration and ingesting our Kubernetes workloads, we may want to automatically connect them to their corresponding `workload` [entities]().

To achieve this, we need to update the mapping configuration of the Kubernetes integration to include an entry for the `workload` [blueprint]().

This example assumes that each Kubernetes workload has a label named `portWorkload` with the value being the identifier of the relevant `workload` [entity]() in Port.

```
- kind: apps/v1/deployments
  selector:
    query: .metadata.namespace | startswith("kube") | not
  port:
    entity:
      mappings:
        - identifier: .metadata.labels.portWorkload
          title: .metadata.name
          blueprint: '"workload"'
          relations:
            k8s_workload: .metadata.name + "-Deployment-" + .metadata.namespace + "-" + env.CLUSTER_NAME
```

The meaning of this configuration is:<br />*For every Kubernetes workload ingested from Kubernetes, update the `workload` entity with the identifier matching the `portWorkload` label, relating it to this `k8s_workload` entity*.

### Identifier is **unknown**[â](#identifier-is-unknown "Direct link to identifier-is-unknown")

If the metadata in your external tool is not an identifier, but some other property of the [entity]() you want to update, you can use a [query rule](/search-and-query/structure-and-syntax.md#rules) to find the relevant entity and update it.

Let's see some examples:

* Service
* Workload

The following example assumes that each PagerDuty service has a label named `portService` with the value being the `title` of the `service` entity in Port:

```
- kind: application
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier:
          combinator: '"and"'
          rules:
            - operator: '"="'
              property: '"$title"'
              value: .metadata.labels.portService
        blueprint: '"service"'
        relations:
          pager_duty_service: .id
```

The meaning of this configuration is:<br />*For every PagerDuty service ingested from PagerDuty, update the `service` entity with the title matching the `portService` label, relating it to this `pagerdutyService` entity*.

The following example assumes that each Kubernetes workload has a label named `portWorkload` with the value being the `title` of the `workload` entity in Port:

```
- kind: apps/v1/deployments
  selector:
    query: .metadata.namespace | startswith("kube") | not
  port:
    entity:
      mappings:
        identifier:
          combinator: '"and"'
          rules:
            - operator: '"="'
              property: '"$title"'
              value: .metadata.labels.portWorkload
        blueprint: '"workload"'
        relations:
          k8s_workload: .metadata.name + "-Deployment-" + .metadata.namespace + "-" + env.CLUSTER_NAME
```

The meaning of this configuration is:<br />*For every workload ingested from Kubernetes, update the `workload` entity with the title matching the `portWorkload` label, relating it to this `k8s_workload` entity*.

## Connect workloads to their respective services[â](#connect-workloads-to-their-respective-services "Direct link to Connect workloads to their respective services")

The methods above demonstrate how to connect `services` and `workloads` to their respective resources.<br /><!-- -->To complete our service catalog, we need to connect `workloads` to their respective `services`.

This too is achieved by updating the mapping configuration of the relevant integration, and adding an entry for the `workload` [blueprint]().<br /><!-- -->One common way to match workloads to services is to use a label.

For example, say we use ArgoCD applications to represent our workloads, and we have a label on each ArgoCD application that matches the identifier of the relevant `service` [entity]() in Port.<br /><!-- -->We can then update the mapping configuration of the ArgoCD integration like this:

```
- kind: application
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.uid
        blueprint: '"workload"'
        relations:
          service: .metadata.labels.portService
```

Note that you do not need a separate entry for this relation in the mapping configuration.<br /><!-- -->This page separates the steps for clarity, but you can add multiple relations in the same mapping configuration block.

For example, this is what the mapping configuration for Kubernetes workloads may look like if we added both the `service` and `k8s_workload` relations at once:

```
- kind: apps/v1/deployments
  selector:
    query: .metadata.namespace | startswith("kube") | not
  port:
    entity:
      mappings:
        - identifier: .metadata.labels.portWorkload
          title: .metadata.name
          blueprint: '"workload"'
          relations:
            k8s_workload: .metadata.name + "-Deployment-" + .metadata.namespace + "-" + env.CLUSTER_NAME
            service: .metadata.labels.portService
```
