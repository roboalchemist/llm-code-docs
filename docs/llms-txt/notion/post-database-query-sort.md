# Notion API

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
- [Create a token](/reference/create-a-token) (POST)
- [Introspect token](/reference/introspect-token) (POST)
- [Revoke token](/reference/revoke-token) (POST)
- [Refresh a token](/reference/refresh-a-token) (POST)

### Blocks
- [Append block children](/reference/append-block-children) (PATCH)
- [Retrieve a block](/reference/retrieve-a-block) (GET)
- [Retrieve block children](/reference/retrieve-block-children) (GET)
- [Update a block](/reference/update-a-block) (PATCH)
- [Delete a block](/reference/delete-a-block) (DEL)

### Pages
- [Create a page](/reference/create-a-page) (POST)
- [Retrieve a page](/reference/retrieve-a-page) (GET)
- [Retrieve a page property item](/reference/retrieve-a-page-property) (GET)
- [Update page](/reference/update-page) (PATCH)
  - [Trash a page](/reference/trash-a-page)

### Databases
- [Create a database](/reference/create-database) (POST)
- [List databases](/reference/list-databases) (GET)
- [Delete a database](/reference/delete-database) (DEL)
```

# Post a Database Entry

[Post](https://docs.rapidapi.com/reference/post-database-query)

## Create a Database

[Create a database](https://docs.rapidapi.com/reference/create-a-database)

## Update a Database

[Update a database](https://docs.rapidapi.com/reference/update-a-database)

## Retrieve a Database

[Retrieve a database](https://docs.rapidapi.com/reference/retrieve-a-database)

## Data Sources

### Create a Data Source

[Create a data source](https://docs.rapidapi.com/reference/create-a-data-source)

### Update a Data Source

#### Update Data Source Properties

[Update data source properties](https://docs.rapidapi.com/reference/update-data-source-properties)

### Retrieve a Data Source

[Retrieve a data source](https://docs.rapidapi.com/reference/retrieve-a-data-source)

### Query a Data Source

#### Filter Data Source Entries

[Filter data source entries](https://docs.rapidapi.com/reference/filter-data-source-entries)

#### Sort Data Source Entries

[Sort data source entries](https://docs.rapidapi.com/reference/sort-data-source-entries)

### List Data Source Templates

[List data source templates](https://docs.rapidapi.com/reference/list-data-source-templates)

## Databases (Deprecated)

### Create a Database

[Create a database](https://docs.rapidapi.com/reference/create-a-database)

### Query a Database

#### Filter Database Entries

[Filter database entries](https://docs.rapidapi.com/reference/post-database-query-filter)

### Retrieve a Database

[Retrieve a database](https://docs.rapidapi.com/reference/retrieve-a-database)

### Update a Database

#### Update Database Properties

[Update database properties](https://docs.rapidapi.com/reference/update-property-schema-object)

### List Databases (Deprecated)

[List databases (deprecated)](https://docs.rapidapi.com/reference/get-databases)

## Comments

### Create Comment

[Create comment](https://docs.rapidapi.com/reference/create-a-comment)

### Retrieve a Comment

[Retrieve a comment](https://docs.rapidapi.com/reference/retrieve-comment)

### List Comments

[List comments](https://docs.rapidapi.com/reference/list-comments)

## File Uploads

### Create a File Upload

[Create a file upload](https://docs.rapidapi.com/reference/create-a-file-upload)

### Send a File Upload

[Send a file upload](https://docs.rapidapi.com/reference/send-a-file-upload)

### Complete a File Upload

[Complete a file upload](https://docs.rapidapi.com/reference/complete-a-file-upload)

### Retrieve a File Upload

[Retrieve a file upload](https://docs.rapidapi.com/reference/retrieve-a-file-upload)

### List File Uploads

[List file uploads](https://docs.rapidapi.com/reference/list-file-uploads)

## Search

[Search](https://docs.rapidapi.com/reference/post-search)
```

# Sort database entries

> ❗️Deprecated as of version 2025-09-03
> 
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/docs/upgrade-guide-2025-09-03).
> 
> Refer to the new page instead:
> 
> - [Sort data source entries](/reference/sort-data-source-entries)

A sort is a condition used to order the entries returned from a database query.

A [database query](/reference/post-database-query) can be sorted by a property and/or timestamp and in a given direction. For example, a library database can be sorted by the "Name of a book" (i.e., property) and in `ascending` (i.e., direction).

Here is an example of a sort on a database property.

```json
{
    "sorts": [
        {
            "property": "Name",
            "direction": "ascending"
        }
    ]
}
```

If you’re using the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js), you can apply this sorting property to your query like so:

```javascript
const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_API_KEY });
// replace with your own database ID
const databaseId = 'd9824bdc-8445-4327-be8b-5b47500af6ce';

const sortedRows = async () => {
  const response = await notion.databases.query({
    database_id: databaseId,
    sorts: [
      {
        property: "Name",
        direction: "ascending"
      }
    ],
  });
  return response;
}
```

Database queries can also be sorted by two or more properties, which is formally called a nested sort. The sort object listed first in the nested sort list takes precedence.

Here is an example of a nested sort.

```json
{
    "sorts": [
      {
        "property": "Food group",
        "direction": "descending"
      },
      {
        "property": "Name",
        "direction": "ascending"
      }
    ]
}
```

In this example, the database query will first be sorted by "Food group" and the set with the same food group is then sorted by "Name".

## Sort object

### Property value sort

This sort orders the database query by a particular property.

The sort object must contain the following properties:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `property` | `string` | The name of the property to sort against. | `"Ingredients"` |
| `direction` | `string` (enum) | The direction to sort. Possible values include `"ascending"` and `"descending"`. | `"descending"` |

### Entry timestamp sort

This sort orders the database query by the timestamp associated with a database entry.

The sort object must contain the following properties:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `timestamp` | `string` (enum) | The name of the timestamp to sort against. Possible values include `"created_time"` and `"last_edited_time"`. | `"last_edited_time"` |
| `direction` | `string` (enum) | The direction to sort. Possible values include `"ascending"` and `"descending"`. | `"descending"` |
```