# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/gitlab/mapping_extensions.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/gitlab-v2/mapping_extensions.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/azure-devops/mapping_extensions.md

# Mapping Extensions

## Introduction[â](#introduction "Direct link to Introduction")

The default way to map your data to Port is by using [JQ JSON processor](https://stedolan.github.io/jq/manual/) to map and transform your data to Port entities.

However, in some cases you may want to map data to Port in a way that default JQ mapping is not enough.

Possible Use Cases:

* Map your repository README.md file contents into Port;
* Check if a specific file exists in your repository;
* Check if a specific string exists in your repository;
* Check if a specific version of a package is used in your repository;
* Check if a CI/CD pipeline is configured in your repository;

## Mapping file content into Port[â](#mapping-file-content-into-port "Direct link to Mapping file content into Port")

The following example demonstrates how to define and export your Azure Devops projects and their **README.md** file contents to Port:

**Repository blueprint (click to expand)**

Create in Port

```
  {
    "identifier": "azureDevopsRepository",
    "title": "Service",
    "icon": "AzureDevops",
    "schema": {
      "properties": {
        "url": {
          "title": "URL",
          "format": "url",
          "type": "string",
          "icon": "Link"
        },
        "readme": {
          "title": "README",
          "type": "string",
          "format": "markdown",
          "icon": "Book"
        },
        "workItemLinking": {
          "title": "Work Item Linking",
          "default": false,
          "type": "boolean"
        },
        "minimumApproverCount": {
          "title": "Minimum Approver Count",
          "default": 0,
          "type": "number"
        },
        "slack": {
          "icon": "Slack",
          "type": "string",
          "title": "Slack",
          "format": "url"
        },
        "tier": {
          "title": "Tier",
          "type": "string",
          "description": "How mission-critical the service is",
          "enum": [
            "Mission Critical",
            "Customer Facing",
            "Internal Service",
            "Other"
          ],
          "enumColors": {
            "Mission Critical": "turquoise",
            "Customer Facing": "green",
            "Internal Service": "darkGray",
            "Other": "yellow"
          },
          "icon": "DefaultProperty"
        }
      },
      "required": []
    },
    "mirrorProperties": {
      "defaultTeam": {
        "title": "Default Team",
        "path": "project.defaultTeam"
      }
    },
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
      "project": {
        "title": "Project",
        "target": "azureDevopsProject",
        "required": false,
        "many": false
      }
    }
  }
```

As we can see one of the properties is of type markdown, this means that we need to map the **README.md** file contents into Port.

To do so, we will use the `includedFiles` selector to specify which files to fetch, and then reference them in the mapping using `.__includedFiles["<file_path>"]`.

Deprecation notice

The `file://` prefix is deprecated and will be removed in a future version. Use the `includedFiles` selector instead.<br /><!-- -->The `file://` prefix will continue to work but will show deprecation warnings in the logs.

```
  - kind: repository
    selector:
      query: 'true'
      includedFiles:
        - README.md
    port:
      entity:
        mappings:
          identifier: .id
          title: .name
          blueprint: '"service"'
          properties:
            url: .remoteUrl
            readme: .__includedFiles["README.md"]
```

## Link pipelines to repositories via selector[â](#link-pipelines-to-repositories-via-selector "Direct link to Link pipelines to repositories via selector")

You can configure your selector to include repository information in the pipeline entity mapping. This allows you to create a direct relationship between a pipeline and its source repository.

```
- kind: pipeline
  selector:
    query: 'true'
    includeRepo: 'true'
  port:
    entity:
      mappings:
        identifier: ."__projectId" + "/" + (.id | tostring)
        title: .name
        blueprint: '"azureDevopsPipeline"'
        properties:
          url: .url
          revision: .revision
          folder: .folder
        relations:
          project: .__projectId | gsub(" "; "")
          repository: if .__repository then .__repository.id else null end
```

Recommendation

Use this only when necessary, as including repository data requires an extra API call per pipeline, which increases the number of requests made and can impact your Azure DevOps API rate limits.

If you donât require repo-level linkage, itâs more efficient to relate pipelines â projects instead.
