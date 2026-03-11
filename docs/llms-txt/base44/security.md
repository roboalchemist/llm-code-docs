# Source: https://docs.base44.com/developers/backend/resources/entities/security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Security

> Control access to your entity data with row level and field level security rules.

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

Entities support two levels of security:

* **Row Level Security (RLS)**: Controls which records users can access.
* **Field Level Security (FLS)**: Controls which fields within records users can access.

## Permission types

Each security level has different permissions you can set. For each permission, you define who is allowed to perform the action.

### Row Level Security (RLS)

* `create` - Add new records
* `read` - View records
* `update` - Modify records
* `delete` - Remove records

### Field Level Security (FLS)

* `read` - View the field
* `write` - Create or modify the field

## Permission values

Each permission accepts one of the following values:

* `true` - Allow all users
* `false` - Block all users
* `{<condition>}` - Allow users matching the condition

### Condition syntax

When using `{<condition>}` as a permission value, you can define rules that check user attributes or roles.

**1. Entity-to-user comparison**

Compare record fields to the current user's values.

Entity fields you can reference:

* `created_by` - Email of user who created the record
* `created_by_id` - ID of user who created the record
* `entity_name` - Name of the entity type
* `app_id` - App ID
* `environment` - Either `prod` or `dev`
* `is_sample` - Whether it's sample data
* `is_deleted` - Soft delete flag
* `deleted_date` - When it was deleted
* `data.*` - Any field from your entity schema's properties

Template variables for user values:

* `{{user.email}}` - User's email
* `{{user.id}}` - User's ID
* `{{user.role}}` - User's role
* `{{user.data.*}}` - Additional user fields you define

Example:

```json  theme={null}
{"created_by": "{{user.email}}"}
{"data.department": "{{user.data.department}}"}
{"data.status": "approved"}
```

**2. User condition check**

Check user properties directly using `user_condition`.

User fields you can check:

* `email` - User's email
* `id` - User's ID
* `role` - User's role
* `data.*` - Custom user fields

Example:

```json  theme={null}
{"user_condition": {"role": "admin"}}
{"user_condition": {"data.level": "senior"}}
```

**3. Complex conditions**

Combine multiple conditions using operators.

Supported operators: `$or`, `$and`, `$nor`, `$in`, `$nin`, `$all`

Example:

```json  theme={null}
{
  "$or": [
    {"created_by": "{{user.email}}"},
    {"user_condition": {"role": "admin"}}
  ]
}
```

## Row Level Security (RLS) example

Add `rls` at the entity level:

```json  theme={null}
{
  "name": "task",
  "type": "object",
  "properties": {...},
  "rls": {
    "create": true,
    "read": {"created_by": "{{user.email}}"},
    "update": {"created_by": "{{user.email}}"},
    "delete": {"user_condition": {"role": "admin"}}
  }
}
```

## Field Level Security (FLS) example

Add `rls` to individual field properties:

```json  theme={null}
{
  "properties": {
    "salary": {
      "type": "number",
      "rls": {
        "read": {"user_condition": {"role": "admin"}},
        "write": {"user_condition": {"role": "admin"}}
      }
    }
  }
}
```

## Complete example with security

Here's an entity schema with both RLS and FLS:

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
      "items": {"type": "string"}
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

## Deploying security rules

Security rules are part of your entity schema. After adding or updating security rules, deploy using [`entities push`](/developers/references/cli/commands/entities-push). Security rules are also deployed automatically when you run the [`deploy`](/developers/references/cli/commands/deploy) command to deploy your entire project.

## See also

* [Entities Overview](/developers/backend/resources/entities/overview): Learn about database schema configuration
* [Entity Schemas](/developers/backend/resources/entities/entity-schemas): Define your entity structure
* [User Schema](/developers/backend/resources/entities/user-schema): Special built-in entity for user authentication
* [Project Structure](/developers/backend/overview/project-structure): How entity schemas fit into your project


Built with [Mintlify](https://mintlify.com).