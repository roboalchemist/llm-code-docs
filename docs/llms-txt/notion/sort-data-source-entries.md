# Source: https://developers.notion.com/reference/sort-data-source-entries.md

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

# Sort data source entries

## Main Content

### Table of Contents

- [Create a database](/reference/database-create)
- [Update a database](/reference/database-update)
- [Retrieve a database](/reference/database-retrieve)

### Data Sources

#### Create a data source
- [Create a data source](/reference/create-a-data-source)

#### Update a data source
- [Update a data source](/reference/update-a-data-source)
  - [Update data source properties](/reference/update-data-source-properties)

#### Retrieve a data source
- [Retrieve a data source](/reference/retrieve-a-data-source)

#### Query a data source
- [Query a data source](/reference/query-a-data-source)
  - [Filter data source entries](/reference/filter-data-source-entries)
  - [Sort data source entries](/reference/sort-data-source-entries)
- [List data source templates](/reference/list-data-source-templates)

#### Databases (deprecated)
- [Databases (deprecated)](/reference/create-a-database)
  - [Create a database](/reference/create-a-database)
  - [Query a database](/reference/post-database-query)
    - [Filter database entries](/reference/post-database-query-filter)
    - [Sort database entries](/reference/post-database-query-sort)
  - [Retrieve a database](/reference/retrieve-a-database)
  - [Update a database](/reference/update-a-database)
    - [Update database properties](/reference/update-property-schema-object)
  - [List databases (deprecated)](/reference/get-databases)

#### Comments
- [Comments](/reference/create-a-comment)
  - [Create comment](/reference/create-a-comment)
  - [Retrieve a comment](/reference/retrieve-comment)
  - [List comments](/reference/list-comments)

#### File Uploads
- [File Uploads](/reference/create-a-file-upload)
  - [Create a file upload](/reference/create-a-file-upload)
  - [Send a file upload](/reference/send-a-file-upload)
  - [Complete a file upload](/reference/complete-a-file-upload)
  - [Retrieve a file upload](/reference/retrieve-a-file-upload)
  - [List file uploads](/reference/list-file-uploads)

#### Search
- [Search](/reference/post-search)
```

# Sort data source entries

A sort is a condition used to order the entries returned from a data source query.

A [data source query](/reference/query-a-data-source) can be sorted by a property and/or timestamp and in a given direction. For example, a library data source can be sorted by the "Name of a book" (i.e., property) and in `ascending` (i.e., direction).

Here is an example of a sort on a data source property.

```json
{
  "sorts": [
    {
      "property": "created_time",
      "direction": "ascending"
    }
  ]
}
```

If you’re using the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js), you can apply this sorting property to your query like so:

```javascript
const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_API_KEY });
// replace with your own data source ID
const dataSourceId = 'd9824bdc-8445-4327-be8b-5b47500af6ce';

const sortedRows = async () => {
  const response = await notion.dataSources.query({
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

Data source queries can also be sorted by two or more properties, which is formally called a nested sort. The sort object listed first in the nested sort list takes precedence.

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

In this example, the data source query will first be sorted by "Food group" and the set with the same food group is then sorted by "Name".

## Sort object

### Property value sort

This sort orders the data source query by a particular property.

The sort object must contain the following properties:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `property` | `string` | The name of the property to sort against. | `"Ingredients"` |
| `direction` | `string` (enum) | The direction to sort. Possible values include `"ascending"` and `"descending"`. | `"descending"` |

### Entry timestamp sort

This sort orders the data source query by the timestamp associated with a data source entry.

The sort object must contain the following properties:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `timestamp` | `string` (enum) | The name of the timestamp to sort against. Possible values include `"created_time"` and `"last_edited_time"`. | `"last_edited_time"` |
| `direction` | `string` (enum) | The direction to sort. Possible values include `"ascending"` and `"descending"`. | `"descending"` |
```