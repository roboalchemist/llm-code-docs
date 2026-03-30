# Source: https://docs.base44.com/developers/references/monitoring-api/get-started/overview.md

# Source: https://docs.base44.com/developers/references/cli/get-started/overview.md

# Source: https://docs.base44.com/developers/references/sdk/getting-started/overview.md

# Source: https://docs.base44.com/developers/backend/resources/backend-functions/overview.md

# Source: https://docs.base44.com/developers/backend/resources/entities/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Entities Overview

> Learn about Base44's entity system for defining data models with built-in CRUD operations, validation, and security.

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

Entities are the data models for your Base44 app. Each entity is a schema that defines the structure for documents in a collection, stored in Base44's NoSQL database. The database is MongoDB-compatible, so you can use MongoDB operators when querying through the SDK.

When you define an entity, you automatically get full CRUD operations through the [entities module](/developers/references/sdk/docs/type-aliases/entities) in the SDK.

Entities support:

* **Schema flexibility:** You can update your data model at any point without running migrations.
* **Realtime updates:** Subscribe to changes to receive updates when records are created, updated, or deleted.
* **Fine-grained security:** Row-level and field-level security rules control who can access which records and fields.

## Define entities

Define entities as JSON files in your project's entities directory. By default the entities directory is `base44/entities/`, but you can customize the path in your [project configuration](/developers/backend/overview/project-structure#configjsonc).

## Test locally

Test your entities locally with [`base44 dev`](/developers/references/cli/commands/dev). The dev server picks up schema changes automatically. See [Local development](/developers/backend/overview/local-dev/local-development-overview) for details.

## Deploy entities

Deploy entities with [`entities push`](/developers/references/cli/commands/entities-push) or [`deploy`](/developers/references/cli/commands/deploy) to push all project resources at once.

## Entity schemas

Entity schemas are JSON Schema definitions that specify the fields, types, and validation rules for your data. Learn more about [entity schemas](/developers/backend/resources/entities/entity-schemas).

## TypeScript types

Generate TypeScript types from your entity schemas to get full type safety and autocomplete in your SDK code. Learn more about [dynamic types](/developers/references/sdk/getting-started/dynamic-types).

## User schema

Every Base44 app includes a built-in User entity that stores information about your app's users. You can extend it with additional fields to store custom user data like company, phone number, or preferences. User fields can be referenced in security rules to control data access based on user attributes. Learn more about the [User schema](/developers/backend/resources/entities/user-schema).

## Security

Control access to your data with row-level and field-level security rules. Define who can create, read, update, and delete records based on user attributes. Learn more about [security rules](/developers/backend/resources/entities/security).


Built with [Mintlify](https://mintlify.com).