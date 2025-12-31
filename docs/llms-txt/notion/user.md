# Source: https://developers.notion.com/reference/user.md

# User

## Objects

### Block

- [Rich text](/reference/rich-text)

### Page

- [Page properties](/reference/page-property-values)
  - [Page property items](/reference/property-item-object)

### Database

- [Database](/reference/database)

### Data source

- [Data source properties](/reference/property-object)

### Comment

- [Comment attachment](/reference/comment-attachment)
- [Comment display name](/reference/comment-display-name)

### File

- [File Upload](/reference/file-upload)

### User

- [User](/reference/user)

### Parent

- [Parent](/reference/parent-object)

### Emoji

- [Emoji](/reference/emoji-object)

### Unfurl attribute (Link Previews)

- [Unfurl attribute (Link Previews)](/reference/unfurl-attribute-object)

## Endpoints

### Authentication

- [Create a token](/reference/create-a-token) (post)
- [Introspect token](/reference/introspect-token) (post)
- [Revoke token](/reference/revoke-token) (post)
- [Refresh a token](/reference/refresh-a-token) (post)

### Blocks

- [Append block children](/reference/append-block-children) (patch)
- [Retrieve a block](/reference/retrieve-a-block) (get)
- [Retrieve block children](/reference/retrieve-block-children) (get)
- [Update a block](/reference/update-a-block) (patch)
- [Delete a block](/reference/delete-a-block) (del)

### Pages

- [Create a page](/reference/create-a-page) (post)
- [Retrieve a page](/reference/retrieve-a-page) (get)
- [Retrieve a page property item](/reference/retrieve-a-page-property) (get)
- [Update page](/reference/update-page)
  - [Trash a page](/reference/trash-a-page)

### Databases

- [Create a database](/reference/create-database) (post)
- [List databases](/reference/list-databases) (get)
- [Get database properties](/reference/get-database-properties) (get)
- [Update database](/reference/update-database)
```

# API Reference

## Database Operations

- [Create a database](https://docs.nestbase.com/reference/database-create)
- [Update a database](https://docs.nestbase.com/reference/database-update)
- [Retrieve a database](https://docs.nestbase.com/reference/database-retrieve)

## Data Sources

### Create a Data Source

- [Create a data source](https://docs.nestbase.com/reference/create-a-data-source)
- [Update a data source](https://docs.nestbase.com/reference/update-a-data-source)
  - [Update data source properties](https://docs.nestbase.com/reference/update-data-source-properties)
- [Retrieve a data source](https://docs.nestbase.com/reference/retrieve-a-data-source)
- [Query a data source](https://docs.nestbase.com/reference/query-a-data-source)
  - [Filter data source entries](https://docs.nestbase.com/reference/filter-data-source-entries)
  - [Sort data source entries](https://docs.nestbase.com/reference/sort-data-source-entries)
- [List data source templates](https://docs.nestbase.com/reference/list-data-source-templates)

### Databases (deprecated)

#### Create a Database

- [Create a database](https://docs.nestbase.com/reference/create-a-database)
- [Query a database](https://docs.nestbase.com/reference/post-database-query)
  - [Filter database entries](https://docs.nestbase.com/reference/post-database-query-filter)
  - [Sort database entries](https://docs.nestbase.com/reference/post-database-query-sort)
- [Retrieve a database](https://docs.nestbase.com/reference/retrieve-a-database)
- [Update a database](https://docs.nestbase.com/reference/update-a-database)
  - [Update database properties](https://docs.nestbase.com/reference/update-property-schema-object)
- [List databases (deprecated)](https://docs.nestbase.com/reference/get-databases)

### Comments

- [Create comment](https://docs.nestbase.com/reference/create-a-comment)
- [Retrieve a comment](https://docs.nestbase.com/reference/retrieve-comment)
- [List comments](https://docs.nestbase.com/reference/list-comments)

### File Uploads

- [Create a file upload](https://docs.nestbase.com/reference/create-a-file-upload)
- [Send a file upload](https://docs.nestbase.com/reference/send-a-file-upload)
- [Complete a file upload](https://docs.nestbase.com/reference/complete-a-file-upload)
- [Retrieve a file upload](https://docs.nestbase.com/reference/retrieve-a-file-upload)
- [List file uploads](https://docs.nestbase.com/reference/list-file-uploads)

### Search

- [Search](https://docs.nestbase.com/reference/post-search)
```

# User

The User object represents a user in a Notion workspace. Users include full workspace members, guests, and integrations. You can find more information about members and guests in [this guide](https://www.notion.so/help/add-members-admins-guests-and-groups).

> **📘 Provisioning users and groups using SCIM**
> 
> The SCIM API is available for workspaces in Notion's Enterprise Plan. Learn more about [using SCIM with Notion](https://www.notion.so/help/provision-users-and-groups-with-scim).

> **📘 Setting up single sign-on (SSO) with Notion**
> 
> Single sign-on (SSO) can be configured for workspaces in Notion's Enterprise Plan. [Learn more about SSO with Notion](https://www.notion.so/help/saml-sso-configuration).

## Where user objects appear in the API

User objects appear in nearly all objects returned by the API, including:

- [Block object](/reference/block) under `created_by` and `last_edited_by`.
- [Page object](/reference/page) under `created_by` and `last_edited_by` and in `people` property items.
- [Database object](/reference/database) under `created_by` and `last_edited_by`.
- [Rich text object](/reference/rich-text), as user mentions.
- [Property object](/reference/property-object) when the property is a `people` property.

User objects will **always** contain `object` and `id` keys, as described below. The remaining properties may appear if the user is being rendered in a rich text or page property context, and the bot has the correct capabilities to access those properties. For more about capabilities, see the [Capabilities guide](/reference/capabilities) and the [Authorization guide](/docs/authorization).

## All users

These fields are shared by all users, including people and bots. Fields marked with \* are always present.

| Property | Updatable | Type | Description | Example value |
| --- | --- | --- | --- | --- |
| `object`\* | Display-only | `"user"` | Always "user" | `"user"` |
| `id`\* | Display-only | `string` (UUID) | Unique identifier for this user. | `"e79a0b74-3aba-4149-9f74-0bb5791a6ee6"` |
| `type` | Display-only | `string` (optional, enum) | Type of the user. Possible values are `"person"` and `"bot"`. | `"person"` |
| `name` | Display-only | `string` (optional) | User's name, as displayed in Notion. | `"Avocado Lovelace"` |
| `avatar_url` | Display-only | `string` (optional) | Chosen avatar image. | `"https://secure.notion-static.com/e6a352a8-8381-44d0-a1dc-9ed80e62b53d.jpg"` |

## People

User objects that represent people have the `type` property set to `"person"`. These objects also have the following properties:

| Property | Updatable | Type | Description | Example value |
| --- | --- | --- | --- | --- |
| `person` | Display-only | `object` | Properties only present for non-bot users. |  |
| `person.email` | Display-only | `string` | Email address of person. This is only present if an integration has user capabilities that allow access to email addresses. | `"[email protected]"` |

## Bots

A user object's `type` property is `"bot"` when the user object represents a bot. A bot user object has the following properties:

| Property | Updatable | Type | Description | Example value |
| --- | --- | --- | --- | --- |
| `bot` | Display-only | `object` | If you're using `GET /v1/users/me` or `GET /v1/users/{{your_bot_id}}`, then this field returns data about the bot, including `owner`, `owner.type`, and `workspace_name`. These properties are detailed below. | ```
{     "object": "user",     "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf",     "name": "Test Integration",     "avatar_url": null,     "type": "bot",     "bot": {         "owner": {         "type": "workspace",         "workspace": true         },  "workspace_name": "Ada Lovelace’s Notion"     } }
``` |
| `owner` | Display-only | `object` | Information about who owns this bot. | ```
{     "type": "workspace",     "workspace": true }
``` |
| `owner.type` | Display-only | `string` enum | The type of owner, either `"workspace"` or `"user"`. | `"workspace"` |
| `workspace_name` | Display-only | `string` enum | If the `owner.type` is `"workspace"`, then `workspace.name` identifies the name of the workspace that owns the bot. If the `owner.type` is `"user"`, then `workspace.name` is `null`. | `"Ada Lovelace’s Notion"` |
| `workspace_id` | Display-only |  |  |  |

```

# Bot User Objects

## Table of Contents

- [Where user objects appear in the API](#where-user-objects-appear-in-the-api)
- [All users](#all-users)
- [People](#people)
- [Bots](#bots)

## Where user objects appear in the API

Bot user objects are available in the following locations:

| Location | Description |
| --- | --- |
| `requests.get('https://api.readdle.com/v1/workspace/{workspace_id}/users')` | Fetches a list of all users in the specified workspace. |
| `requests.get('https://api.readdle.com/v1/users')` | Fetches a list of all users across all workspaces. |

## All users

### People

- **id**: Unique identifier for the user.
- **name**: The user's name.
- **avatar_url**: URL of the user's avatar.
- **profile_picture_url**: URL of the user's profile picture.
- **public_bio**: A brief bio published by the user, if available.
- **created_at**: Date when the user was created.

### Bots

- **id**: Unique identifier for the bot.
- **name**: The bot's name.
- **description**: A brief description of the bot.
- **avatar_url**: URL of the bot's avatar.
- **profile_picture_url**: URL of the bot's profile picture.
- **public_bio**: A brief bio published by the bot, if available.
- **created_at**: Date when the bot was created.

## Bot User Objects

| Property | Type | Description |
| --- | --- | --- |
| id | string | ID of the bot's workspace. |
| workspace_limits | object | Information about the limits and restrictions that apply to the bot's workspace. |
| workspace_limits.max_file_upload_size_in_bytes | integer | The maximum allowable size of a file upload, in bytes. |

## Example

```json
{
  "id": "17ab3186-873d-418f-b899-c3f6a43f68de",
  "workspace_limits": {
    "max_file_upload_size_in_bytes": 5242880
  },
  "users": [
    {
      "id": "4e2c3b0f-0089-4f4b-a96b-f7c18387531d",
      "name": "John Doe",
      "avatar_url": "https://example.com/avatar.jpg",
      "profile_picture_url": null,
      "public_bio": "Hello, I'm John Doe!",
      "created_at": "2023-03-12T14:56:00Z"
    }
  ]
}
```