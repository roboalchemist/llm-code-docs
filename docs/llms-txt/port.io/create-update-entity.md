# Source: https://docs.port.io/actions-and-automations/setup-backend/create-update-entity.md

# Create/update entity

In some cases, we don't want to run complex logic via a workflow or pipeline, but rather want our backend to simply create or update an entity in our software catalog.<br /><!-- -->This backend type does exactly that, simplifying the process and avoiding unnecessary complexity.

## Define the backend[â](#define-the-backend "Direct link to Define the backend")

To use this backend type, you will need to define the following fields:

![](/img/self-service-actions/setup-backend/upsert-entity/upsertUiExample.png)

* The `blueprint` from which the entity will be created or updated.

* The mapping of the created/updated entity:

  ```
  {
    "identifier": "some_identifier",
    "title": "Some Title",
    "team": [],
    "icon": "DefaultBlueprint",
    "properties": {},
    "relations": {}
  }
  ```

  <br />

  The table below describes the fields in the JSON structure (fields in **bold** are required):

  | Field            | Description                                                                                                                                                                                                                  |
  | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **`identifier`** | Used to identify the entity in your software catalog. If it already exists, the entity will be **updated**, otherwise it will be **created**.                                                                                |
  | `title`          | The title of the entity.                                                                                                                                                                                                     |
  | `team`           | The team/s this entity will belong to.                                                                                                                                                                                       |
  | `icon`           | The icon of the entity.                                                                                                                                                                                                      |
  | `properties`     | The properties of the entity, in `"key":"value"` pairs where the key is the property's identifier, and the value is its value.                                                                                               |
  | `relations`      | The relations of the entity, in `"key":"value"` pairs where the key is the relation's identifier, and the value is the related entity's identifier (for single relations) or an array of identifiers (for "many" relations). |

### Use jq to map the entity[â](#use-jq-to-map-the-entity "Direct link to Use jq to map the entity")

All fields in the `mapping` object can be mapped using `jq` expressions, by wrapping the value in double curly braces `{{ }}`.

For example, say we want to assign the initiator of the action to a new entity when it is created, we can take his email from the action run object and assign it to a property named `assignee`:

```
{
  "identifier": "someTaskEntity",
  "title": "Some Task",
  "team": ["team1"],
  "icon": "DefaultBlueprint",
  "properties": { "assignee": "{{ .trigger.by.user.email }}" },
  "relations": {}
}
```

Test your mapping

You can use the `Test JQ` button in the bottom-left corner to test your mapping against the action's schema.

## Map entity relations[â](#map-entity-relations "Direct link to Map entity relations")

When creating or updating entities, you often need to establish relations with other entities. The mapping approach depends on whether you're dealing with single or multiple entity inputs.

* Single Entity
* Array Entity
* Flexible Mapping

For a single entity relation, map the entity identifier directly:

```
{
  "identifier": "myServiceEntity",
  "title": "My Service",
  "properties": {},
  "relations": {
    "domain": "{{ .inputs.domain }}"
  }
}
```

When your action accepts [array entity inputs](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/entity.md#array), you need to extract the identifiers from the array using the `map(.identifier)` pattern:

```
{
  "identifier": "myUserEntity", 
  "title": "My User",
  "properties": {},
  "relations": {
    "skills": "{{ .inputs.skills | map(.identifier) }}"
  }
}
```

Array entity inputs

When users select multiple entities from an [entity array input](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/entity.md#array), the input contains an array of entity objects. Each object includes both `identifier` and `title` properties, but relations can only reference entity identifiers.

For maximum flexibility, you can create a conditional mapping that handles both single entity and array entity inputs:

```
{
  "identifier": "myProjectEntity",
  "title": "My Project", 
  "properties": {},
  "relations": {
    "dependencies": "{{ .inputs.dependencies | if type == \"array\" then map(.identifier) else .identifier end }}"
  }
}
```

This pattern automatically:

* Extracts identifiers from arrays when multiple entities are selected
* Uses the identifier directly when a single entity is selected

### Common use cases[â](#common-use-cases "Direct link to Common use cases")

Here are some typical scenarios for mapping array relations:

**Mapping skills to a user:**

```
"relations": {
  "skills": "{{ .inputs.selectedSkills | map(.identifier) }}"
}
```

**Mapping team members to a project:**

```
"relations": {
  "members": "{{ .inputs.teamMembers | map(.identifier) }}"
}
```

**Mapping dependencies between services:**

```
"relations": {
  "dependsOn": "{{ .inputs.dependencies | map(.identifier) }}"
}
```

Entity titles in relations

Relations can only reference entity **identifiers**, not titles. Even though entity objects contain both `identifier` and `title` properties, you must always use `.identifier` when mapping to relations.

## Limitations[â](#limitations "Direct link to Limitations")

### Create missing related entities[â](#create-missing-related-entities "Direct link to Create missing related entities")

The `createMissingRelatedEntities` flag is not supported when using this backend type.

If you want to automatically create missing related entities, you can use the [webhook backend](/actions-and-automations/setup-backend/webhook/.md) instead, with an API call to the [create an entity](/api-reference/create-an-entity.md) endpoint. This way you can set the `createMissingRelatedEntities` flag to `true` in the API call.

Here is an example JSON definition of a self-service action that creates a new entity and its related entities:

**Example action JSON definition (click to expand)**

Create in Port

```
{
  "identifier": "create_entity_a",
  "title": "Create Entity A",
  "trigger": {
    "type": "self-service",
    "operation": "CREATE",
    "userInputs": {
      "properties": {},
      "required": [],
      "order": []
    }
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "https://api.port.io/v1/blueprints/<entity_a_identifier>/entities?create_missing_related_entities=true",
    "agent": false,
    "synchronized": true,
    "method": "POST",
    "headers": {
      "RUN_ID": "{{ .run.id }}",
      "Content-Type": "application/json"
    },
    "body": {
      "identifier": "my_new_entity",
      "title": "MyNewEntity",
      "icon": "Microservice",
      "team": [],
      "properties": {},
      "relations": {
        "<relation_identifier>": "<entity_b_identifier>"
      }
    }
  },
  "requiredApproval": false
}
```

**Note** that `synchronized` should be set to `true`.
