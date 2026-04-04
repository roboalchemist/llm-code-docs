# Source: https://docs.port.io/guides/all/ingest-dependencies-from-package-json-to-service.md

# Ingest dependencies from a package.json file and relate them to a service

## Overview[â](#overview "Direct link to Overview")

This guide will demonstrate how to ingest dependencies from a `package.json` file and relate them to the corresponding service entities in Port.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* This guide assumes you have a Port account and that you have finished the [onboarding process](/getting-started/overview.md).
* Install Port's [GitHub app](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github/#setup)

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

### Add a dependency blueprint[â](#add-a-dependency-blueprint "Direct link to Add a dependency blueprint")

1. **Go to the [Builder](https://app.getport.io/settings/data-model)** in your Port portal.

2. **Click on "+ Blueprint"**.

3. **Click on the `{...}` button** in the top right corner, and choose "Edit JSON"

4. **Add this JSON schema**:

   **Dependency blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "dependency",
     "title": "Dependency",
     "icon": "Package",
     "schema": {
       "properties": {
         "package_name": {
           "icon": "DefaultProperty",
           "type": "string",
           "title": "Package name"
         },
         "semver_requirement": {
           "type": "string",
           "title": "Semver requirement"
         },
         "type": {
           "type": "string",
           "title": "Type",
           "enum": [
             "Production",
             "Development"
           ]
         },
         "url": {
           "type": "string",
           "title": "URL",
           "format": "url"
         }
       },
       "required": [
         "package_name",
         "semver_requirement"
       ]
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

## Ingest dependencies from package.json[â](#ingest-dependencies-from-packagejson "Direct link to Ingest dependencies from package.json")

To ingest dependencies listed in `package.json` files, follow these steps:

1. **Go to the [data sources page](https://app.getport.io/settings/data-sources)** in your Port portal, and select your GitHub integration.

2. **Modify the mapping** to include the `file` kind with the configuration provided below:

   **Port Configuration (Click to expand)**

   ```

     - kind: file
       selector:
         query: 'true'
         files:
           - path: '**/package.json'
       port:
         itemsToParse: .file.content.dependencies | to_entries
         entity:
           mappings:
             identifier: >-
               .item.key + "_" +  (.item.value |  gsub("\\^"; "caret_") | 
               gsub("~"; "tilde_") |  gsub(">="; "gte_") |  gsub("<="; "lte_") | 
               gsub(">"; "gt_") |  gsub("<"; "lt_") |  gsub("@"; "at_") | 
               gsub("\\*"; "star") |  gsub(" "; "_"))              
             title: .item.key + "@" + .item.value
             blueprint: '"dependency"'
             properties:
               package_name: .item.key
               semver_requirement: .item.value
   ```

   Configuration Details

   * **`kind: file`** specifies that the source is a file, in this case, `package.json`.
   * **`files:`** defines the path pattern to locate `package.json` files within your repositories.
   * **`itemsToParse:`** identifies the specific array within the `package.json` (i.e., `dependencies`) that you want to parse into individual `dependency` entities.
   * **`identifier:`** constructs a unique identifier for each dependency, accounting for special characters in the version string.
   * **`properties:`** captures essential details like the package name and version.

## Relate the dependencies to the service[â](#relate-the-dependencies-to-the-service "Direct link to Relate the dependencies to the service")

Once the dependencies have been ingested, the next step is to establish relationships between these `dependency` entities and the corresponding `service` entities.

1. **Go to the [Builder](https://app.getport.io/settings/data-model)** in your Port portal, select the `Service` [blueprint](), and click on `New relation` to create a relation between the `service` and `dependency` blueprints.

2. Click on the `...` button in the top right corner of the `Service` blueprint and select `Edit JSON`.

3. **Add this JSON to establish the relationship**:

   ```
     "dependencies": {
       "title": "Dependencies",
       "target": "dependency",
       "required": false,
       "many": true
     }
   ```

4. Head back to the [data sources page](https://app.getport.io/settings/data-sources) and add one of the following mapping approaches:

   * Direct Mapping
   * Search query

   The most straightforward way to set a relation's value is to explicitly specify the related entity's identifier:

   ```
     - kind: file
       selector:
         query: 'true'
         files:
           - path: '**/package.json'
       port:
         entity:
           mappings:
             identifier: .repo.name
             blueprint: '"service"'
             properties: {}
             relations:
               dependencies: >-
                 [.file.content.dependencies | to_entries | map( .key + "_" + 
                 (.value | 
                   gsub("\\^"; "caret_") | 
                   gsub("~"; "tilde_") | 
                   gsub(">="; "gte_") | 
                   gsub("<="; "lte_") | 
                   gsub(">"; "gt_") | 
                   gsub("<"; "lt_") | 
                   gsub("@"; "at_") | 
                   gsub("\\*"; "star") | 
                   gsub(" "; "_")
                 ) ) | .[]]
   ```

   Mapping Details

   This would establish a relation between the `service` and `dependency` entities based on the dependencies listed in the `package.json` file.

   You can also use a [search query](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-mapping#mapping-relations-using-search-queries) to dynamically match services with their dependencies based on package information.

   This approach is particularly useful when you don't know the entity's identifier, but you do know the value of one of its properties.

   Add the snippet below to your mapping configuration to match services with dependencies based on the first package in dependencies/devDependencies.<br /><!-- -->You can adjust the rules to match your organization's needs by:

   ```
   - kind: file
     selector:
       query: 'true'
       files:
         - path: '**/package.json'
     port:
       entity:
         mappings:
           identifier: .repo.name
           blueprint: '"service"'
           properties: {}
           relations:
             dependencies:
               combinator: '"or"'
               rules:
                 - property: '"package_name"'
                   operator: '"="'
                   value: .file.content.dependencies | to_entries[0].key
                 - property: '"package_name"'
                   operator: '"="'
                   value: >-
                     (.file.content.devDependencies // {}) | to_entries[0].key //
                     null
   ```

5. After you add the mapping, click on the **resync** button and watch your repositories being mapped to their dependencies as shown below in this example:

   ![](/img/guides/serviceDependencies.png)

## Conclusion[â](#conclusion "Direct link to Conclusion")

By following these steps, you can effectively ingest dependencies from `package.json` files and relate them to the corresponding repository entities in Port ð.

More relevant guides and examples:

* [Port's GitHub integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github/)
* [Self-service actions and workflows](https://docs.port.io/create-self-service-experiences/setup-backend/github-workflow/)
