# Source: https://docs.base44.com/developers/backend/resources/entities/user-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User Schema

> Extend the built-in User entity with additional fields for your app.

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

The User entity exists in every Base44 project by default and stores information about your app's users. You can add fields to store additional user data, then use those fields in [security rules](/developers/backend/resources/entities/security) to control data access or in your app to personalize the experience.

## Built-in fields

Every User entity includes a set of built-in fields by default.

| Field       | Type   | Description              |
| ----------- | ------ | ------------------------ |
| `full_name` | string | User's display name      |
| `email`     | string | User's email address     |
| `role`      | string | Either `admin` or `user` |

The User entity also has the [general built-in fields](/developers/backend/resources/entities/entity-schemas#built-in-fields) that exist on all entities , such as `id`, and `created_date`.

These fields are managed by the system and can't be redefined in your schema.

## Custom fields

To add custom fields, define a User schema containing only your additional fields. Trying to redefine any built-in fields will cause a validation error.

Create a `User.json` or `User.jsonc` file in your project's entities directory. By default this is `base44/entities/`, but you can customize the path in your [project configuration](/developers/backend/overview/project-structure#configjsonc).

```json entities/User.json theme={null}
{
  "type": "object",
  "properties": {
    "company": { "type": "string" },
    "phone": { "type": "string" },
    "job_title": { "type": "string" },
    "bio": { 
      "type": "string",
      "maxLength": 500
    }
  },
  "required": ["company"]
}
```

Then push your entities to Base44 using [`entities push`](/developers/references/cli/commands/entities-push) or [`deploy`](/developers/references/cli/commands/deploy).

## Complete example

Here's a complete User schema with various field types:

```json  theme={null}
{
  "type": "object",
  "properties": {
    "company": {
      "type": "string"
    },
    "phone": {
      "type": "string"
    },
    "job_title": {
      "type": "string",
      "maxLength": 100
    },
    "bio": {
      "type": "string",
      "maxLength": 500
    },
    "website": {
      "type": "string",
      "format": "uri"
    },
    "preferences": {
      "type": "object",
      "properties": {
        "theme": {
          "type": "string",
          "enum": ["light", "dark"],
          "default": "light"
        },
        "notifications": {
          "type": "boolean",
          "default": true
        }
      }
    }
  },
  "required": ["company"]
}
```

## Use your fields

Once you've defined and pushed your User schema, you can reference your fields in security rules and access them in your app code.

### In security rules

You can use user fields to control access to other entities. For example, you might restrict users to only see records that belong to their company.

To reference user fields in [security rules](/developers/backend/resources/entities/security), use the `{{user.data.*}}` template syntax:

```json  theme={null}
{
  "rls": {
    "read": {"data.company": "{{user.data.company}}"},
    "update": {"data.company": "{{user.data.company}}"}
  }
}
```

This rule ensures users can only read and update records where the record's `company` field matches their own.

### In code

Access user fields through the [SDK](/developers/references/sdk/getting-started/overview):

```typescript  theme={null}
// Get current user's fields
const currentUser = await base44.auth.me();
console.log(currentUser.company); // "Acme Inc"

// Update current user's fields
await base44.auth.updateMe({
  phone: "+1-555-0123",
  job_title: "Senior Developer"
});

// List all users with service role (backend functions only)
const allUsers = await base44.asServiceRole.entities.User.list();
```

<Info>
  This example uses a `base44` client. See [Setting up the client](/developers/references/sdk/getting-started/client) for setup instructions.
</Info>

## See also

* [Entities Overview](/developers/backend/resources/entities/overview): Learn about database schema configuration
* [Entity Schemas](/developers/backend/resources/entities/entity-schemas): Define your entity structure
* [Security](/developers/backend/resources/entities/security): Configure row-level security rules
* [Project Structure](/developers/backend/overview/project-structure): How entity schemas fit into your project


Built with [Mintlify](https://mintlify.com).