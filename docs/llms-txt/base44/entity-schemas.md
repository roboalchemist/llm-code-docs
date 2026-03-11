# Source: https://docs.base44.com/developers/backend/resources/entities/entity-schemas.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Entity Schemas

> Define custom data structures using a JSON Schema with validation rules and field types

<div className="dev-docs-banner">
  <div className="dev-docs-banner-content">
    <div className="dev-docs-banner-title">
      You're viewing developer documentation
    </div>

    <div className="dev-docs-banner-text">
      This documentation is for developers working with the Base44 developer platform. For information about managing your app data using the app editor, see <a href="/Building-your-app/Managing-your-app-data">Managing app data</a>.
    </div>
  </div>
</div>

Entities are defined using a JSON Schema that describes the data structure and validation rules.

## Basic schema structure

Entity schemas are defined in JSON files in your project's entities directory. By default, this is `base44/entities/`, but you can customize the path in your [project configuration](/developers/backend/overview/project-structure#config-jsonc). The filename determines the entity name. For example, `Task.json` creates a `Task` entity.

Here's an entity schema template:

```json  theme={null}
{
  "name": "my_entity",
  "type": "object",
  "title": "My Entity",
  "description": "Description of what this entity represents",
  "properties": {
    "<field_name>": {
      "type": "<field_type>",
      "<option>": "<value>"
    }
  },
  "required": ["<field_name>"]
}
```

## Built-in fields

Every entity record automatically includes the following fields. Don't define fields with these names in your schema.

| Field                     | Type     | Description                              |
| ------------------------- | -------- | ---------------------------------------- |
| `id`                      | string   | Unique identifier for the record         |
| `created_date`            | datetime | When the record was created              |
| `updated_date`            | datetime | When the record was last updated         |
| `created_by`              | string   | Email of the user who created the record |
| `created_by_id`           | string   | ID of the user who created the record    |
| `is_deleted` (internal)   | boolean  | Soft delete flag                         |
| `deleted_date` (internal) | datetime | When the record was deleted              |
| `is_sample` (internal)    | boolean  | Whether the record is sample data        |
| `entity_name` (internal)  | string   | Name of the entity type                  |
| `app_id` (internal)       | string   | App ID                                   |
| `environment` (internal)  | string   | Either `prod` or `dev`                   |

Internal fields aren't returned in API responses but can be referenced in [security rules](/developers/backend/resources/entities/security).

## Schema fields

<ResponseField name="name" type="string">
  String identifier for the entity.
</ResponseField>

<ResponseField name="type" type="string" required>
  Must be `"object"`.
</ResponseField>

<ResponseField name="title" type="string">
  User-friendly display name.
</ResponseField>

<ResponseField name="description" type="string">
  Description of what the entity represents.
</ResponseField>

<ResponseField name="properties" type="object" required>
  Object containing your field definitions. Each field has a `type` and optional
  validation rules.
</ResponseField>

## Field types

Entities support various field types to define different kinds of data you can store: `string`, `integer`, `number`, `boolean`, `array`, and `object`.
Each field inside `properties` requires a `type`. Based on the type, you can add validation options.

### String fields

String fields support these options:

* **`minLength`** / **`maxLength`**: Control minimum and maximum character count.
* **`pattern`**: Regular expression for custom validation.
* **`format`**: Predefined formats. Supported values:
  * `"date"`
  * `"date-time"`
  * `"time"`
  * `"email"`
  * `"uri"`
  * `"hostname"`
  * `"ipv4"`
  * `"ipv6"`
  * `"uuid"`
* **`enum`**: Restrict to specific allowed values. Define as an array: `["value1", "value2", "value3"]`.
* **`default`**: Default value if none provided.

### Integer fields

Integer fields support these options:

* **`minimum`** / **`maximum`**: Set inclusive lower/upper bounds.
* **`default`**: Default value if none provided.

### Number fields

Number fields support these options:

* **`minimum`** / **`maximum`**: Set inclusive lower/upper bounds.
* **`default`**: Default value if none provided.

### Boolean fields

Boolean fields support these options:

* **`default`**: Default value if none provided.

### Array fields

Array fields support these options:

* **`items`**: Define the type/schema for array elements.
* **`default`**: Default array value if none provided.

### Object fields

Object fields support these options:

* **`properties`**: Define the fields within the object.
* **`required`**: List of required property names.

## Required fields

Specify which fields must be provided:

```json  theme={null}
{
  "required": ["title", "email"]
}
```

## Complete example

Here's a complete entity schema:

```json  theme={null}
{
  "name": "Task",
  "type": "object",
  "title": "Task",
  "description": "A task item with priority, due date, and completion status",
  "properties": {
    "title": {
      "type": "string",
      "minLength": 1,
      "maxLength": 200
    },
    "description": {
      "type": "string",
      "maxLength": 1000
    },
    "priority": {
      "type": "string",
      "enum": ["low", "medium", "high"],
      "default": "medium"
    },
    "completed": {
      "type": "boolean",
      "default": false
    },
    "due_date": {
      "type": "string",
      "format": "date"
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" }
    },
    "internal_notes": {
      "type": "string",
      "rls": {
        "read": {"user_condition": {"role": "admin"}},
        "write": {"user_condition": {"role": "admin"}}
      }
    }
  },
  "required": ["title"],
  "rls": {
    "create": true,
    "read": {"created_by": "{{user.email}}"},
    "update": {"created_by": "{{user.email}}"},
    "delete": {"created_by": "{{user.email}}"}
  }
}
```

## Deploying entities

After defining your entity schema, deploy it to Base44 using [`entities push`](/developers/references/cli/commands/entities-push). Entities are also deployed automatically when you run the [`deploy`](/developers/references/cli/commands/deploy) command to deploy your entire project.

Once deployed, you can interact with your entities using the [SDK's `entities` module](/developers/references/sdk/docs/type-aliases/entities). The entity name in your schema must match exactly how you access it in the SDK, including capitalization. For example, if your schema has `"name": "Task"`, you must access it as `base44.entities.Task.list()`.

Deployed entity schemas can be viewed in the dashboard in the **Data** section.

## See also

* [User Schema](/developers/backend/resources/entities/user-schema): Special built-in entity for user authentication
* [Security](/developers/backend/resources/entities/security): Configure row-level security rules for entities
* [Project Structure](/developers/backend/overview/project-structure): How entity schemas fit into your project


Built with [Mintlify](https://mintlify.com).