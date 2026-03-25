# Source: https://docs.port.io/customize-pages-dashboards-and-plugins/page/entity-page.md

# Entity page

Each [entity](/build-your-software-catalog/sync-data-to-catalog/.md#entity-json-structure) has a dedicated page that contains 4 tabs (by default):

* [Overview](#overview)
* [Related entities](#related-entities)
* [Runs](#runs)
* [Audit log](#audit-log)

## Overview[â](#overview "Direct link to Overview")

The overview tab is a dashboard, used to display [widgets](/customize-pages-dashboards-and-plugins/dashboards/overview.md) related to the entity.

By default, each entity will have a `Details` widget, which displays the entity's properties and their values, and other metadata.

### Manage properties[â](#manage-properties "Direct link to Manage properties")

In the top right corner of the details widget, you can find the ![](/img/guides/icons/ManageProperties.svg)![](/img/guides/icons/dark/ManageProperties.svg) button that opens the "manage properties" modal, which allows you to:

* Show/hide empty values - properties with empty values will be hidden if the toggle is off.
* Show/hide specific properties in the widget.

Additional widgets can be added by clicking on the `+ Widget` button in the top right corner of the dashboard.

## Related entities[â](#related-entities "Direct link to Related entities")

By default, all related entities in the same direction will automatically appear in this table. This is true for both forward-related and backward-related entities. Indirectly-related entities will not appear but can be added manually, check out the [indirect relations](#indirect-relation) section on how to add indirectly related entities.

For example:

`Workflow Run` has a forward-relation to `Deployment Workflow`, which has a forward-relation to `Service`, which has a **backward**-relation to `Deployment`.<br /><!-- -->Since we changed direction midway, this relation is **indirect**:

![](/img/software-catalog/pages/builderRelationsExample.png)

When looking at the entity page of a certain `Workflow Run`, the related entities `Deployment Workflow` and `Service` automatically appear, but `Deployment` does not, since its relation is in the other direction.

### Add a Related entities tab[â](#add-a-related-entities-tab "Direct link to Add a Related entities tab")

1. Click the `+` button above the table to add a custom tab.

   ![](/img/software-catalog/pages/relatedEntitieNewTab.png)

   <br />

2. Fill in the form:

   ![](/img/software-catalog/pages/relatedEntitiesDetails.png)

   * Set the tab's `Name` and optional `Description`.

   * Choose the `Related blueprint` you want to display.

   * Pick a `Relation path`:

     * **All paths** â includes all available paths from the current blueprint to the target blueprint.
     * **Specific path** â choose the specific relation chain.

   * (Optional) Add `Additional filters` to restrict the result set.

Relation path options

The relation path dropdown displays straightforward, acyclic paths. For complex scenarios involving circular relationships, advanced path configurations, multiple self-relations, or maxHops, use [JSON mode](#filters-and-edit-json).

Using "All paths" is less performant than selecting a specific path, as it requires the system to evaluate multiple relationship paths.

#### Additional filters[â](#additional-filters "Direct link to Additional filters")

![](/img/software-catalog/pages/jsonTogglerAddTab.png)

<br />

<br />

Selecting `Filters` opens a dialog where you can build conditions using form controls (property, operator, value).<br /><!-- -->You can switch to a JSON editor using the `Edit JSON` button to define the dataset directly.

The filters visual editor doesn't support nested queries so in the case of nested queries, use the JSON editor to define the dataset.

The dataset follows this structure based on the [search and query syntax](https://docs.port.io/search-and-query/overview):

```
{
  "combinator": "and",
  "rules": [
    {
      "property": "$title",
      "operator": "contains",
      "value": "awesome-package"
    }
  ]
}
```

Use the JSON editor when you need to copy/paste filter sets, keep them in source control, or express conditions that are faster to author as JSON. You can toggle back to the form at any time.

#### Define the tab in JSON mode

You can also toggle `Json Mode` in the "Add tab" dialog to author the entire tab as JSON. An example:

```
{
  "dataset": {
    "combinator": "and",
    "rules": [
      {
        "property": "$title",
        "operator": "contains",
        "value": "awesome-package"
      }
    ]
  },
  "title": "custom path package",
  "targetBlueprint": "Package",
  "relationPath": {
    "path": ["service_in_env", "package"],
    "fromBlueprint": "service_in_env_deployments"
  }
}
```

This JSON corresponds to a tab named `custom path package` that targets the `Package` blueprint, follows a specific path from `service_in_env_deployments` via `service_in_env` to `package`, and filters results to titles containing the letter `awesome-package`.

#### Show/hide columns[â](#showhide-columns "Direct link to Show/hide columns")

By default, the related entities table will display the following columns for each entity:<br />`Title`, `Last update time`, and `Creation time`.<br /><!-- -->Other properties will be hidden by default.

You can always customize the table to [hide/show columns](/customize-pages-dashboards-and-plugins/page/catalog-page.md?create-page=ui#hideshow-columns).

#### Indirect relations[â](#indirect-relations "Direct link to Indirect relations")

In some scenarios, you may want to display entities that are not directly related but connected through a common blueprint. This is useful when you have multiple services that share relationships with a common entity.

For example, consider this relationship structure:

![](/img/software-catalog/pages/relatedEntitiesIndirectRelations.png)

<br />

<br />

From the diagram, we can see that:

* **Deployment Workflow** has a relation to **Microservice**
* **Deployment** has relations to **Microservice** (including `relation_1` and `relation_2`)
* **Deployment Workflow** and **Deployment** are not directly related, but connected through **Microservice**

When you're on the entity page of a **Deployment Workflow**, the related entity **Microservice** automatically appears, but **Deployment** does not, since its relation is in the other direction. However, you can create a custom tab to show **Deployment** entities by leveraging the indirect relationship through **Microservice**.

#### Add a tab for an indirectly related blueprint

1. Click the `+` button above the Related Entities table.

2. Set the tab name and description.

3. Choose **Deployment** as the `Related blueprint`.

4. For the `Relation or property`, select the specific relation from **Deployment Workflow** to **Microservice** that you want to traverse.

![](/img/software-catalog/pages/relatedEntitiesIndirectRelations2.png)

This approach allows you to display indirectly related entities while maintaining control over the specific relationship path used for the connection.

Multiple relations scenario

If **Deployment Workflow** has multiple relations to **Microservice** (e.g., `deployment_target` and `monitoring_target`), you can choose which specific relation path to use for more refined and filtered results.

Additionally, when you have an existing relation between blueprints, Port automatically creates a mirror property relation that allows you to traverse the relationship in both directions. This mirror relation will appear as an option in the relation dropdown, enabling you to explore connections from either side of the relationship.

#### Self-relation[â](#self-relation "Direct link to Self-relation")

A self-relation allows a blueprint to establish a relationship with itself. This is useful when you want entities of the same blueprint to be related to other entities within that same blueprint.

For example, consider a **Team** blueprint where:

* Organizations contain teams.
* Teams can belong to other organizational entities (like groups).

All entities share the same blueprint but have hierarchical relationships.

When defining a self-relation, you can specify how many "hops" to traverse in the relationship chain.<br /><!-- -->Hops represent the number of jumps you want to make upstream or downstream through the self-relation.

Create a self-relation

Before performing the following steps, make sure the desired blueprint has a relation to itself.

**Add self-relation (click to exapnd)**

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.
2. Choose the relevant blueprint.
3. Click the `+ New relation` button.
4. Give the property a `title`, choose the same blueprint in the `Related to` field.
5. Choose the entity limit and whether its required.
6. Click `Save`.

**Set up self-relations tab**

To add a self-relation tab to the related entities:

1. Click the `+` button in the **Related Entities** table.

2. Choose your blueprint as the **Related blueprint**.

3. Select the self-relation path from the available paths.

4. If you want to traverse more than one hop, switch to `Json mode`.

   In JSON mode you can:

   * Specify multiple self-relation identifiers (for fixed hops).

     ```
      "relationPath": {
      "path": [
        "self_relation",
        "self_relation"
        ]
      }
     ```

   * Use maxHops (for variable hops).

     ```
      "relationPath": {
        {
          "relation": "<SELF_RELATION_IDENTIFIER>",
          "maxHops": <number between 1 and 15>
        }
      }
     ```

   * Combine fixed hops with maxHops for mixed control.

     ```
     "relationPath": {
       "path": [
         "self_relation",
         {
           "relation": "<SELF_RELATION_IDENTIFIER>",
           "maxHops": <number between 1 and 15>
         }
       ]
     }
     ```

     `maxHops` limitation

     The `maxHops` parameter can only be applied **once** per path, and it accepts values from **1 to 15**.

5. Click on `Save` to save the tab.

Self-relation identifier

Note that `self_relation` in these examples represents the identifier of the self-relation you created in your blueprint. Replace it with your actual self-relation identifier.

**Examples**

Let's take a look at some examples using the concept of Teams.

![](/img/software-catalog/pages/relatedEntitiesTeamExample.png)

<br />

<br />

**Basic self-relation with multiple self-relations:**

If you want **exactly 2 hops**, specify the relation twice:

```
{
  "dataset": {
    "combinator": "and",
    "rules": []
  },
  "title": "Team Hierarchy",
  "targetBlueprint": "Team",
  "relationPath": {
    "path": [
      "self_relation",
      "self_relation"
    ],
    "fromBlueprint": "Team"
  }
}
```

In this case, the added tab under the `Unit` entity should show the `Group` entity.

**Self-relation with maxHops for variable hops:**

If you want a variable number of hops (between 1 and 15), use maxHops:

```
{
  "dataset": {
    "combinator": "and",
    "rules": []
  },
  "title": "Team Hierarchy",
  "targetBlueprint": "Team",
  "relationPath": {
    "path": [
      {
        "relation": "team_self_relation",
        "maxHops": 4
      }
    ],
    "fromBlueprint": "Team"
  }
}
```

In this case, the added tab under the `Unit` entity should show the `Basic Team`, `Group` and `Office` entities.

**Mixed approach example:**

You can also mix fixed hops with variable hops. For example, if you specify `self_relation` twice followed by a `maxHops` object, the system will start traversing from the 2 hops already made and continue with the additional hops specified in `maxHops`.

```
{
  "title": "Team Hierarchy",
  "targetBlueprint": "Team",
  "dataset": {
    "combinator": "and",
    "rules": []
  },
  "relationPath": {
    "path": [
      "self_relation",    // 1st hop: Unit -> Basic Team
      "self_relation",    // 2nd hop: Basic Team -> Group  
      {
        "relation": "team_self_relation",
        "maxHops": 3      // Continues from Group, adding up to 3 more hops (Group -> Office -> etc.)
      }
    ],
    "fromBlueprint": "Team"
  }
}
```

In this example, the system will traverse 2 fixed hops (`Unit` â `Basic Team` â `Group`) and then continue with up to 3 additional hops using the `team_self_relation`, starting from where the fixed hops left off. This could represent a complete organizational hierarchy from Unit all the way up to higher-level organizational structures.

In this case, the added tab under the `Unit`entity should show the `Group` and `Office` entities.

**Simple relation path example:**

You can also use regular relations (not self-relations) in your paths:

```
{
  "dataset": {
    "combinator": "and",
    "rules": []
  },
  "title": "Developer",
  "targetBlueprint": "developer",
  "relationPath": {
    "path": [
      "member_of"
    ]
  }
}
```

The fromBlueprint property

The `fromBlueprint` property is only needed when the path starts from the current page's blueprint and ends with the entities listed in the tab. For more information about relation paths see the [Relation operators](https://docs.port.io/search-and-query/operators/relation-operators) documentation.

## Runs[â](#runs "Direct link to Runs")

If the entity's blueprint has any [actions](/actions-and-automations/create-self-service-experiences/.md) configured, the `Runs` tab will display their history log, results, log streams, and more.

## Audit log[â](#audit-log "Direct link to Audit log")

This tab displays all actions (including CRUD) that caused any change to the entity's configuration.<br /><!-- -->For each change, useful metadata will be shown such as the initiator, diff before and after the change, relevant blueprint, and more.

## Additional tabs[â](#additional-tabs "Direct link to Additional tabs")

### Visual properties[â](#visual-properties "Direct link to Visual properties")

Some of the [available property types](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md#supported-properties) are visual by nature. When defining one of these properties in a blueprint, an additional tab will be automatically created in each entity page related to this blueprint, displaying the property's content in the relevant visual format.

The following property types are supported:

* [Markdown](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/markdown.md)
* [Embedded URL](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/embedded-url/.md)
* [Swagger UI](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/swagger.md)

### Scorecards[â](#scorecards "Direct link to Scorecards")

If the entity's blueprint has any [scorecards](/scorecards/overview.md) configured, a `Scorecards` tab will be automatically created in the entity page.

The tab will display the entity's compliance status with each of its scorecards.

### Dashboard tabs[â](#dashboard-tabs "Direct link to Dashboard tabs")

You can add additional, customizable dashboard tabs to an entity page by clicking the `+` button.<br /><!-- -->Each dashboard tab name can be customized and edited.

#### Limitations[â](#limitations "Direct link to Limitations")

* You can add up to 5 dashboard tabs per entity page.
* Dashboard tab names must be unique and are limited to 30 characters.

## Dashboard filters[â](#dashboard-filters "Direct link to Dashboard filters")

Dashboard filters allow you to apply selected filters **across all supported widgets** within a dashboard at once.<br /><!-- -->This makes it easier to explore data consistently, without having to filter each widget individually.

### Supported widgets[â](#supported-widgets "Direct link to Supported widgets")

Dashboard filters currently apply to the following widgets:

* [Number chart](/customize-pages-dashboards-and-plugins/dashboards/data-widgets.md#number-chart)
* [Pie chart](/customize-pages-dashboards-and-plugins/dashboards/data-widgets.md#pie-chart)
* [Line chart](/customize-pages-dashboards-and-plugins/dashboards/data-widgets.md#line-chart)
* [Table](/customize-pages-dashboards-and-plugins/dashboards/data-widgets.md#table)

### Supported filter types[â](#supported-filter-types "Direct link to Supported filter types")

When creating a dashboard filter, you can choose between:

* **Basic properties** - Meta properties that apply across all blueprints in the dashboard.
* **Blueprint-specific properties** - Properties from a specific blueprint that is selected in one or more widgets in the dashboard.

The blueprint dropdown will only show blueprints that are used in widgets within the dashboard. For example, if a widget uses the `microservice` blueprint, `microservice` will appear as an option in the filter dropdown.

![](/img/software-catalog/pages/dashboardFilterBlueprintServiceExample.png)

<br />

<br />

Filter scope

Filters applied to a specific blueprint will only affect widgets that are relevant to that blueprint in the dashboard.<br /><!-- -->Filters applied to basic properties will affect all supported widgets across all blueprints.

**Basic properties**

When selecting **Basic properties**, you can filter on the following meta properties:

* **Owning teams:**

  * Filter entities based on selected team(s).
  * Use the `My Teams` option to dynamically filter entities relevant to the current user.
  * Applies only to blueprints that include an `Owning Team` property.

* **Title:** Filter entities by their entity title using different [string operators](/search-and-query/operators/comparison-operators.md).

* **Identifier:** Filter entities by their identifier using different [string operators](/search-and-query/structure-and-syntax.md).

**Blueprint properties**

When selecting a specific blueprint (e.g., `service`), you can filter on any property defined for that blueprint, including:

* **Owning teams:** Filter entities of that specific blueprint based on selected team(s). This differs from filtering on owning team using basic properties, which applies across all blueprints.
* **Any other blueprint property:** Filter on any property defined in the selected blueprint using the appropriate [comparison operators](/search-and-query/operators/comparison-operators.md) for that property type.

For example, you can filter on owning team across all dashboard blueprints by selecting **Basic properties â Owning teams**, or you can filter on owning team only for the `service` blueprint by selecting **Service â Owning teams**.

Below is an example dashboard with **two types of filters applied**:

1. A **Blueprint properties** filter on the `microservice` blueprint that excludes entities where `language = Ruby`. This filter only affects widgets that display `microservice` data.
2. A **Basic properties** filter on **Owning teams**, which applies to *all* supported widgets in the dashboard, regardless of blueprint.

In the example, the **Services by language** widget reflects the blueprint filter by omitting microservices with `language = Ruby`, while every widget is narrowed by the **Owning teams** filter to show only entities associated with the selected team(s).

![](/img/software-catalog/pages/dashboardFiltersExample.png)

### Permissions[â](#permissions "Direct link to Permissions")

**Admin role:** As an admin (or a member with edit permissions for the dashboard), you can add, edit, or remove filters from the dashboard page. Then, save the view to apply it for other users.

**Member role:** As a member, you can view, add, edit, or remove filters on the page (unless the page is locked). The changes apply only to your own view.

![](/img/software-catalog/pages/dashboardFiltersMemberEdit.png)
