# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/relate-blueprints.md

# Relate Blueprints

[YouTube video player](https://www.youtube.com/embed/McUWOC4gcu4)

<br />

Relations define connections between [blueprints](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md), consequently connecting the [entities](/build-your-software-catalog/sync-data-to-catalog/.md#entities) based on these blueprints.<br /><!-- -->This provides logical context to the software catalog.

## Common relations[â](#common-relations "Direct link to Common relations")

Relations can be used to represent the logical connections between assets in your software catalog, for example:

* The **packages** that a **microservice** uses.
* The **run** history of a **CI job**.
* The **Kubernetes clusters** that exist in a **cloud account**.

In this [live demo](https://demo.port.io/settings) example, we can see the DevPortal Builder page with all of the blueprints and their relations. ð¬

## Relation schema structure[â](#relation-schema-structure "Direct link to Relation schema structure")

The basic structure of a relation object:

```
{
  "myRelation": {
    "title": "My title",
    "target": "My target blueprint",
    "required": true,
    "many": false
  }
}
```

relation declaration

A relation exists under the `relations` key in the [Blueprint JSON schema](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md#blueprint-schema-structure).

## Structure table[â](#structure-table "Direct link to Structure table")

| Field        | Description                                                                                            | Notes                                                                                                                                                                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifier` | Unique identifier (Maximum 100 characters)                                                             | The identifier is used for API calls, programmatic access and distinguishing between different relations.<br /><br />The identifier is the key of the relation schema object, in the [schema structure](#relation-schema-structure) above, the identifier is `myRelation` |
| `title`      | Relation name that will be shown in the UI                                                             | Human-readable name for the relation                                                                                                                                                                                                                                      |
| `target`     | Target blueprint identifier                                                                            | The target blueprint has to exist when defining the relation                                                                                                                                                                                                              |
| `required`   | Boolean flag to define whether the target must be provided when creating a new entity of the blueprint |                                                                                                                                                                                                                                                                           |
| `many`       | Boolean flag to define whether multiple target entities can be mapped to the Relation                  | For more information refer to [many relation](#many)                                                                                                                                                                                                                      |

## Types of relations[â](#types-of-relations "Direct link to Types of relations")

### ð¤<!-- --> Single[â](#bust_in_silhouette-single "Direct link to bust_in_silhouette-single")

A single type relation is used to map a single target entity to the source.

#### ð¡ Common Single Relations[â](#-common-single-relations "Direct link to ð¡ Common Single Relations")

* Map a **Deployment** to the **Running Service** that it deployed.
* Map a **package version** to the **package**.
* Map a **K8s cluster** to the **cloud account** it is provisioned in.

In this [live demo](https://demo.port.io/githubWorkflowEntity?identifier=wish_list_build_185674921\&activeTab=3) example, we can see a specific Deployment Workflow and its related Service. ð¬

#### Single Relation Structure[â](#single-relation-structure "Direct link to Single Relation Structure")

A single type relation is distinguished by the `many: false` configuration:

* API
* Terraform

```
{
  "myRelation": {
    "title": "My title",
    "target": "myTargetBlueprint",
    "required": false,
    "many": false
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  # ...user-defined properties
  relations {
    identifier = "myRelation"
    title      = "My relation"
    target     = "myTargetBlueprint"
    required   = false
    many       = false
  }
}
```

### ð¥ Many[â](#-many "Direct link to ð¥ Many")

A many type relation is used to map multiple target entities to the source.

#### ð¡ Common Many Relations[â](#-common-many-relations "Direct link to ð¡ Common Many Relations")

* Map dependencies between services.
* Map the **packages** used by a **service**.
* Map the **cloud resources** used by a **service**.
* Map the **services deployed** in a **developer environment**.

In this [live demo](https://demo.port.io/jiraIssueEntity?identifier=WISH-789\&activeTab=1) example, we can see a specific Jira issue and its related Services. ð¬

#### Many Relation Structure[â](#many-relation-structure "Direct link to Many Relation Structure")

A many type relation is distinguished by the `many: true` configuration:

* API
* Terraform

```
{
  "myRelation": {
    "title": "My title",
    "target": "myTargetBlueprint",
    "required": false,
    "many": true
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  # ...user-defined properties
  relations {
    identifier = "myRelation"
    title      = "My relation"
    target     = "myTargetBlueprint"
    required   = false
    many       = true
  }
}
```

Relation Configuration Restriction

A Relation can't be configured with both `many` and `required` set to `true`.

## Configure relations in Port[â](#configure-relations-in-port "Direct link to Configure relations in Port")

Relations are part of the structure of a [blueprint](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md#blueprint-structure).

* UI
* API
* Terraform

1. Go to the [Builder page](https://app.getport.io/settings) of your portal.

2. Expand the blueprint from which you would like to create a relation.

3. Click on the `+ New relation` button:

   ![](/img/software-catalog/customize-integrations/createRelation.png)

4. Fill in the form with your desired values, then click `Create`.

Create in Port

```
{
  "identifier": "myIdentifier",
  "title": "My title",
  "description": "My description",
  "icon": "My icon",
  "calculationProperties": {},
  "schema": {
    "properties": {},
    "required": []
  },
  "relations": {
    "myRelation": {
      "title": "My title",
      "target": "My target blueprint",
      "required": true,
      "many": false
    }
  }
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

```
resource "port_blueprint" "myBlueprint" {
  # ...blueprint properties
  # ...user-defined properties
  relations = {
    "myRelation" = {
      title    = "My title"
      target   = "My target blueprint"
      required = true
      many     = false
    }
  }
}
```
