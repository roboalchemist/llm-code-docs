# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-mapping.md

# Configure mapping

[YouTube video player](https://www.youtube.com/embed/tx4aWVKY5x4)

<br />

The mapping of an integration's data source defines the ingested data and its destination. It allows you to specify:

* **Which data** you wish to ingest from the integrated tool.
* **Which properties** in the integration's blueprints will be filled with the ingested data.

## How does mapping work?[â](#how-does-mapping-work "Direct link to How does mapping work?")

Integration mapping is configured in the [data sources page](https://app.getport.io/settings/data-sources) of your portal, under `Exporters`.<br /><!-- -->Each integration has its own mapping, written in `YAML`.

To understand how mapping works, let's take a look at an example. After you complete the [onboarding](/getting-started/overview.md) and connect your Git provider to Port, you will see an exporter entry in your [data sources page](https://app.getport.io/settings/data-sources):

![](/img/software-catalog/customize-integrations/mappingExampleEntry.png)

<br />

<br />

Clicking on this entry will open the mapping configuration. In the bottom left panel, you will see the YAML configuration of the mapping.<br /><!-- -->Note that Port provides default mapping, providing values to the properties defined in the relevant blueprint:

![](/img/software-catalog/customize-integrations/mappingExampleGithub.png)

<br />

<br />

### Configuration structure[â](#configuration-structure "Direct link to Configuration structure")

This section will explain each part of the configuration YAML.<br /><!-- -->Some of the keys use [JQ queries](https://jqlang.github.io/jq/manual/) to filter the data ingested from the tool's API.

* The `resources` key is the root of the YAML configuration:

  ```
  resources:
    - kind: repository
      ...
  ```

  Processing order

  Resources are processed **sequentially from top to bottom**. This means:

  * The first `kind` in your configuration is fetched and ingested before the second one starts.
  * If you have relations between entities (e.g., pull requests â repositories), ensure the **target blueprint is listed first** so those entities exist before the relation is created.
  * For large datasets, the order can affect sync duration since each kind must complete before the next begins.

<br />

* The `kind` key is a specifier for the object you wish to map from the tool's API (in this example, a Github repository).<br /><!-- -->To see which `kinds` are available for mapping, refer to the integration's documentation. In this example, the available kinds are listed in the [Github integration page](/build-your-software-catalog/sync-data-to-catalog/git/github/.md#port-app-configyml-structure).

  ```
    resources:
      - kind: repository
        selector:
        ...
  ```

<br />

* The `selector` and the `query` keys let you filter exactly which objects of the specified `kind` will be ingested into Port:

  ```
  resources:
    - kind: repository
      selector:
        query: "true" # JQ boolean query. If evaluated to false - skip syncing the object.
      port:
  ```

  Using a JQ query, you can define your desired conditions. For example, to ingest only repositories that have a name starting with `"service"`, use the `query` key like this:

  ```
  query: .name | startswith("service")
  ```

<br />

* The `port.entity.mappings` key contains the section used to map the object fields to Port entities.<br /><!-- -->Here you can specify the `blueprint` in Port to which the data should be mapped, and which API object will be ingested to each of its properties. To map properties, specify the property identifier as the key inside the `properties` object.

  ```
  resources:
    - kind: repository
      selector:
        query: "true"
      port:
        entity:
          mappings: # Mappings between one GitHub API object to a Port entity. Each value is a JQ query.
            identifier: ".name"
            title: ".name"
            blueprint: '"service"'
            properties:
              description: ".description"
              url: ".html_url"
              defaultBranch: ".default_branch"
  ```

  To create multiple mappings of the same kind, you can add another item to the `resources` array:

  ```
  resources:
    - kind: repository
      selector:
        query: "true"
      port:
        entity:
          mappings: # Mappings between one GitHub API object to a Port entity. Each value is a JQ query.
            identifier: ".name"
            title: ".name"
            blueprint: '"service"'
            properties:
              description: ".description"
              url: ".html_url"
              defaultBranch: ".default_branch"
    - kind: repository # In this instance repository is mapped again with a different filter
      selector:
        query: '.name == "MyRepositoryName"'
      port:
        entity:
          mappings: ...
  ```

JQ syntax for identifiers with hyphens

When using JQ to reference identifiers or property names that contain hyphens, you must wrap them in double quotes and use bracket notation.

For example, use `.["my-property"]` instead of `.my-property`, which JQ would interpret as subtraction.

This applies to secrets, properties, and any other identifiers containing hyphens:

* Secrets: `.secrets["zendesk-api-token"]`
* Properties: `.properties["my-custom-field"]`
* Relations: `.relations["parent-service"]`

### Additional options[â](#additional-options "Direct link to Additional options")

Several more advanced options are available in the mapping configuration:

* `createMissingRelatedEntities` - used to enable the creation of missing related entities in Port. This is useful when you want to create an entity and its related entities in one call, or if you want to create an entity whose related entity does not exist yet.

* `deleteDependentEntities` - used to enable deletion of dependent Port entities. This is useful when you have two blueprints with a required relation, and the target entity in the relation should be deleted. In this scenario, the delete operation will fail if this parameter is set to `false`. If set to `true`, the source entity will be deleted as well.

* `entityDeletionThreshold` - used to set the threshold for the number of entities to delete by an Ocean integration. Ocean integrations compare the third-party data against the data in Port and may delete entities accordingly. This parameter allows you to control this behavior and avoid unexpected interruptions. The parameter can be set from 0 to 1.0. For example, if the parameter is set to 0.5, it means that if the number of entities to delete is greater than 50% of the total number of entities, the deletion will be skipped.

To use these options, add them to the root of the mapping configuration:

```
createMissingRelatedEntities: true
deleteDependentEntities: true
entityDeletionThreshold: 0.5
resources:
  - kind: repository
    ...
```

Create Missing Related Entities flag in protected blueprints

Note that you cannot use the `createMissingRelatedEntities` flag to create entities in protected blueprints such as `_user` and `_team`.

### Test your mapping - JQ playground[â](#test-your-mapping---jq-playground "Direct link to Test your mapping - JQ playground")

The mapping configuration window contains a JQ playground that allows you to test your JQ queries against example responses from the API of the integrated tool. This is useful for validating your queries and ensuring they return the expected results.

For integrations based on the [Ocean framework](https://ocean.getport.io/integrations-library/), examples will be automatically generated for each resource `kind` in your mapping, based on real data ingested from the tool. You can disable this behavior by setting the `sendRawDataExamples` flag to `false` in the integration's configuration.

To test your mapping against the example data, click on the `Test mapping` button in the bottom-right panel.

#### Manually add test examples[â](#manually-add-test-examples "Direct link to Manually add test examples")

For each resource `kind` in your mapping (in the bottom-left panel), you can add an example in the `Test examples` section.<br /><!-- -->Click on the `Add kind` button to add an example:

![](/img/software-catalog/customize-integrations/addTestExample.png)

After adding your example, click on the `Test mapping` button in the bottom-right panel to test your mapping against the example data.

Port's JQ playground

In addition to the aforementioned JQ playground, Port provides a general [JQ playground](https://jq.getport.io/) where you can test any JSON snippet against JQ expressions with real-time filters and AI-powered assistance.

### Edit an integration's mapping[â](#edit-an-integrations-mapping "Direct link to Edit an integration's mapping")

Once you have configured an integration's mapping to your liking, click the `Resync` button in the bottom-right to save your changes.

To edit an integration's mapping using Port's API, you can use the [Patch integration](/api-reference/update-an-integration.md) route.

Resync via the API

To perform a simple resync of an integration via the API without changing its mapping, use the same `Patch integration` route with the integration identifier and an empty body.

## Mapping relations[â](#mapping-relations "Direct link to Mapping relations")

[YouTube video player](https://www.youtube.com/embed/ovV4bLtX78g)

<br />

In Port, [relations](/build-your-software-catalog/customize-integrations/configure-data-model/relate-blueprints/.md) define how [blueprints](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md) are connected to one another.<br /><!-- -->For instance, a `Service` blueprint can be related to a `PagerDuty service` blueprint.

After ingesting all of our Services and PagerDuty services, we want to connect each `Service` to its corresponding `PagerDuty service`.<br /><!-- -->To achieve this, we have two options:

1. **Assigning relations automatically using the mapping Configuration**

   You can define the relation in the mapping file of your data source (e.g. PagerDuty) so that relations are assigned automatically during ingestion.<br /><!-- -->Here's an example:

   * Go to your [data sources page](https://app.getport.io/settings/data-sources) and click on the PagerDuty exporter:

   * In the bottom left panel, edit the mapping YAML file, and add the following entry to it:

     ```
     - kind: services
       selector:
         query: "true"
       port:
         entity:
           mappings:
             identifier: .name
             blueprint: '"service"'
             properties: {}
             relations:
               pager_duty_service: .id
     ```

     In this mapping configuration, `pager_duty_service` is the name of the relation identifier, and `.id` is a JQ expression that extracts the identifier of the `PagerDuty service` from the ingested data.

     When the data is ingested:

     * If a `service` entity with the same identifier (`.name`) already exists in your catalog, Port will update it, adding the `pager_duty_service` relation and other associated data, such as the on-call property.
     * If no such `service` exists, Port will create a new `service` entity with that identifier and attach the related `PagerDuty service` and the on-call property.

     This configuration ensures your catalog stays up to date automatically. You can also customize the relation logic, for example, using search-based relations, depending on your naming conventions or data structure.

2. **Assigning relations manually in the UI**

   You can also assign relations manually using Port's UI.<br /><!-- -->For example:

   * Go to the [services page](https://app.getport.io/services) of your software catalog.
   * Choose a service you want to assign a PagerDuty service to. Hover over it, click on the `...` button on the right, and select `Edit`.
   * In the `PagerDuty service` field, select the relevant `PagerDuty service` from the dropdown list, then click `Update`.

### Mapping relations using search queries[â](#mapping-relations-using-search-queries "Direct link to Mapping relations using search queries")

In the example above we map a relation using a direct reference to the related entity's `identifier`.

Port also allows you to use a [search query rule](/search-and-query/structure-and-syntax.md#rules) to map relations based on a **property** of the related entity.<br /><!-- -->This is useful in cases where you don't have the identifier of the related entity, but you do have one of its properties.

For example, consider the following scenario:<br /><!-- -->Say we have a `service` blueprint that has a relation (named `service_owner`) to a `user` blueprint. The `user` blueprint has a property named `github_username`.

Now, we want to map the `service_owner` relation based on the `github_username` property of the `user` entity.<br /><!-- -->To achieve this, we can use the following mapping configuration:

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
          service_owner:
            combinator: '"and"'
            rules:
              - property: '"github_username"'
                operator: '"="'
                value: .owner.login
```

Instead of directly referencing the `user` entity's `identifier`, we use a search query rule to find the `user` entity whose `github_username` property matches the `.owner.login` value returned from GitHub's API.

When using a search query rule to map a relation, Port will query all entities of the related blueprint (in this case - `user`) and return the one/s that match the rule.

#### Limitations[â](#limitations "Direct link to Limitations")

* One or more entities can be returned by the search query rule. Note the relation's type when using this method:

  <!-- -->

  * A ["single type" relation](/build-your-software-catalog/customize-integrations/configure-data-model/relate-blueprints/.md#bust_in_silhouette-single) expects a single entity to be returned.
  * A ["many type" relation](/build-your-software-catalog/customize-integrations/configure-data-model/relate-blueprints/.md#-many) expects an array of entities to be returned.

* The maximum number of entities returned by the search query rule is 500.

* Calculation properties are currently not supported.

* Mirror properties are supported only for a single type relation and one level deep.

* Only the following operators are supported in the search query rule: `=`, `in`, and `contains`.

## Map by property[â](#map-by-property "Direct link to Map by property")

In some cases, we may not know the identifier of the entity we want to map to. If that entity has a property that we do know, we can use it to map the data.<br /><!-- -->This is especially useful when patching entities whose identifiers are not known in advance. Take the following example:

* Say we installed Port's PagerDuty integration, and we want to connect each `service` (Git repository) to the relevant `PagerDuty service`.
* We can create a property in our `service` blueprint named `pagerduty_service_id`, containing the identifier of the relevant PagerDuty service.
* Then, in the `PagerDuty` integration mapping, we can use this property to map each `PagerDuty service` to the relevant `service`.
* This way, we would not need to have a separate blueprint for `PagerDuty services`, since the integration maps directly to the `service` blueprint.

Mapping by property is done using a [search query rule](/search-and-query/structure-and-syntax.md#rules) in the following format:

```
resources:
  - kind: services
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier:
            combinator: '"and"'
            rules:
              - operator: '"="'
                property: '"pagerduty_service_id"'
                value: .id
          blueprint: '"service"'
          properties:
            oncall: .__oncall_user | sort_by(.escalation_level) | .[0].user.email
            ... # Any other properties you want to map
```

In the example above, we search for a `service` entity whose `pagerduty_service_id` property is equal to the `id` of the PagerDuty service, and map data from the PagerDuty service to it.

API usage

Searching by property can also be used when using Port's API to [create an entity](/api-reference/create-an-entity.md).

### Limitations[â](#limitations-1 "Direct link to Limitations")

* The search query must return **exactly one entity** (otherwise the entire request will fail).<br /><!-- -->To avoid failures from identical values of a property across different blueprints, include an additional rule with the `$blueprint` property in mapping search queries, to ensure that the search query is executed on the correct blueprint.<br /><!-- -->For example:

  ```
  combinator: "and"
  rules:
    - property: "$blueprint"
      operator: "="
      value: "service"
    # your other rules...
  ```

* If the search query returns no entities, a new entity **will not** be created.

* The query will be executed on the same blueprint from the requestâs url.

* Only the `=` and `in` operators is supported for the search query rule.

* `Calculation` and `mirror` properties are not supported.

## Create multiple entities from an array API object[â](#create-multiple-entities-from-an-array-api-object "Direct link to Create multiple entities from an array API object")

When an application's API returns an array of objects that you want to map to multiple entities in Port, you can use the `itemsToParse` configuration option. This allows you to iterate over an array and create a separate entity for each item.

### `itemsToParse`[â](#itemstoparse "Direct link to itemstoparse")

The `itemsToParse` key specifies a JQ query that returns an array. Port will iterate over each item in this array and create a separate entity for each one. Within your mapping properties, you can reference the current array item using `.item`.

**Example:**

```
- kind: issue
  selector:
    query: .issueType == 'Bug'
  port:
    itemsToParse: .fields.comments
    entity:
      mappings:
        identifier: .item.id
        blueprint: '"comment"'
        properties:
          text: .item.text
          author: .item.author.name
        relations:
          issue: .key
```

In this example, Port will iterate over each comment in the `comments` array and create a separate `comment` entity for each one. The `.item` reference allows you to access properties of the current comment being processed.

### `itemsToParseName`[â](#itemstoparsename "Direct link to itemstoparsename")

By default, Port uses `.item` to reference the current array item. However, if your API response already contains an `item` key at the top level, this can cause ambiguous access. The `itemsToParseName` key allows you to specify a custom name to reference array items instead of the default `.item`.

**Example:**

```
- kind: issue
  selector:
    query: .issueType == 'Bug'
  port:
    itemsToParse: .fields.comments
    itemsToParseName: 'comment'
    entity:
      mappings:
        identifier: .comment.id
        blueprint: '"comment"'
        properties:
          text: .comment.text
          author: .comment.author.name
        relations:
          issue: .key
```

In this example, we use `comment` instead of `item` to reference each array element, avoiding conflicts with any top-level `item` property in the API response.

### `itemsToParseTopLevelTransform`[â](#itemstoparsetopleveltransform "Direct link to itemstoparsetopleveltransform")

By default, Port removes the target array specified in `itemsToParse` from the original payload to improve parsing performance. The `itemsToParseTopLevelTransform` flag controls this behavior:

* When set to `true` (default): The target array is removed from the payload, and you can only access array items via `.item` (or your custom `itemsToParseName`).
* When set to `false`: The target array remains in the payload, allowing you to access both the original array and individual items.

**Example with `itemsToParseTopLevelTransform: true` (default):**

```
- kind: issue
  selector:
    query: .issueType == 'Bug'
  port:
    itemsToParse: .fields.comments
    itemsToParseTopLevelTransform: true
    entity:
      mappings:
        identifier: .item.id
        blueprint: '"comment"'
        properties:
          text: .item.text
          issueKey: .key  # Can access top-level properties
        relations:
          issue: .key
```

**Example with `itemsToParseTopLevelTransform: false`:**

```
- kind: issue
  selector:
    query: .issueType == 'Bug'
  port:
    itemsToParse: .fields.comments
    itemsToParseTopLevelTransform: false
    entity:
      mappings:
        identifier: .item.id
        blueprint: '"comment"'
        properties:
          text: .item.text
          totalComments: .fields.comments | length  # Can access the original array
          issueKey: .key
        relations:
          issue: .key
```

When `itemsToParseTopLevelTransform` is `false`, you can access the original array (e.g., `.fields.comments`) in addition to individual items via `.item`.

Limitations

* The `itemsToParseName` key is not supported in non-Ocean integrations: [Github app](/build-your-software-catalog/sync-data-to-catalog/git/github/.md), [Kubernetes](/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/.md) and [Webhook integrations](/build-your-software-catalog/custom-integration/webhook/.md).
* When `itemsToParseName` is enabled, you cannot use the "test mapping" option in Port's UI.

The object returned from Jira for which we would apply this mapping might look like this (note the `comments` array):

**Example Jira API response (click to expand)**

```
{
  "url": "https://example.com/issue/1",
  "status": "Open",
  "issueType": "Bug",
  "comments": [
    {
      "id": "123",
      "text": "This issue is not reproducing"
    },
    {
      "id": "456",
      "text": "Great issue!"
    }
  ],
  "assignee": "user1",
  "reporter": "user2",
  "creator": "user3",
  "priority": "High",
  "created": "2024-03-18T10:00:00Z",
  "updated": "2024-03-18T12:30:00Z",
  "key": "ISSUE-1"
}
```

## Follow-up video[â](#follow-up-video "Direct link to Follow-up video")

The following video follows up on the video at the top of this page.<br /><!-- -->It demonstrates how to add new properties to a blueprint and map data into them:

[YouTube video player](https://www.youtube.com/embed/YeNyq_WJsvY)

<br />
