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
- [Data source properties](/reference/data-source)

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
- [Update page](/reference/update-page)
  - [Trash a page](/reference/trash-a-page)

```

# RESTful API Reference

## Database Operations

- [Create a database](https://docs.apimatic.io/reference/database-create)
- [Update a database](https://docs.apimatic.io/reference/database-update)
- [Retrieve a database](https://docs.apimatic.io/reference/database-retrieve)

## Data Sources

### Create a Data Source

- [Create a data source](https://docs.apimatic.io/reference/create-a-data-source)
- [Update a data source](https://docs.apimatic.io/reference/update-a-data-source)
  - [Update data source properties](https://docs.apimatic.io/reference/update-data-source-properties)
- [Retrieve a data source](https://docs.apimatic.io/reference/retrieve-a-data-source)
- [Query a data source](https://docs.apimatic.io/reference/query-a-data-source)
  - [Filter data source entries](https://docs.apimatic.io/reference/filter-data-source-entries)
  - [Sort data source entries](https://docs.apimatic.io/reference/sort-data-source-entries)
- [List data source templates](https://docs.apimatic.io/reference/list-data-source-templates)

### Databases (deprecated)

#### Create a Database

- [Create a database](https://docs.apimatic.io/reference/create-a-database)
- [Query a database](https://docs.apimatic.io/reference/post-database-query)
  - [Filter database entries](https://docs.apimatic.io/reference/post-database-query-filter)
  - [Sort database entries](https://docs.apimatic.io/reference/post-database-query-sort)
- [Retrieve a database](https://docs.apimatic.io/reference/retrieve-a-database)
- [Update a database](https://docs.apimatic.io/reference/update-a-database)
  - [Update database properties](https://docs.apimatic.io/reference/update-property-schema-object)
- [List databases (deprecated)](https://docs.apimatic.io/reference/get-databases)

### Comments

- [Create comment](https://docs.apimatic.io/reference/create-a-comment)
- [Retrieve a comment](https://docs.apimatic.io/reference/retrieve-comment)
- [List comments](https://docs.apimatic.io/reference/list-comments)

### File Uploads

- [Create a file upload](https://docs.apimatic.io/reference/create-a-file-upload)
- [Send a file upload](https://docs.apimatic.io/reference/send-a-file-upload)
- [Complete a file upload](https://docs.apimatic.io/reference/complete-a-file-upload)
- [Retrieve a file upload](https://docs.apimatic.io/reference/retrieve-a-file-upload)
- [List file uploads](https://docs.apimatic.io/reference/list-file-uploads)

### Search

- [Search](https://docs.apimatic.io/reference/post-search)
```

# Create a page

Use this API to create a new [page](/reference/page) as a child of an existing page or [data source](/reference/data-source).

## Use cases

### Choosing a parent

In most cases, provide a `page_id` or `data_source` under the `parent` parameter to create a page under an existing [page](/reference/page), or [data source](/reference/data-source), respectively.

There is a 3rd option, available only for bots of [public integrations](/docs/getting-started#internal-vs-public-integrations): creating a private page at the workspace level. To do this, omit the `parent` parameter, or provide `parent[workspace]=true`. This can be useful for quickly creating pages that can then be organized manually in the Notion app later, helping you get to your life's work faster.

For internal integrations, a page or data source parent is currently required in the API, because there is no one specific Notion user associated with them that could be used as the "owner" of the new private page.

### Setting up page properties

If the new page is a child of an existing page, `title` is the only valid property in the `properties` body parameter.

If the new page is a child of an existing [data source](/reference/data-source), the keys of the `properties` object body param must match the parent [data source's properties](/reference/property-object).

### Setting up page content

This endpoint can be used to create a new page with or without content using the `children` option. To add content to a page after creating it, use the [Append block children](/reference/patch-block-children) endpoint.

**Templates**: As an alternative to building up page content manually, the `template` body parameter can be used to specify an existing data source template to be used to populate the content and properties of the new page.

When omitted, the default is `template[type]=none`, which means no template is applied. The other options for `template[type]` are:

- `default`: Apply the data source's default template.
  - This is only allowed for pages created under a data source that has a default template configured in the Notion app.
- `template_id`: Provide a specific `template_id` to use as the blueprint for your page.
  - The API bot must have access to the template page, and it must be within the same workspace.
  - Although any valid page ID can be used as the `template[template_id]`, we recommend only using pages that are configured as actual [database templates](https://www.notion.com/help/database-templates) under the same data source as the parent of your new page to make sure that page properties can get merged in correctly.

When applying a template, the `children` parameter is **not** allowed. The page is returned as blank initially in the API response, and then Notion's systems apply the template asynchronously after the API request finishes. For more information, see our full guide on [creating pages from templates](/docs/creating-pages-from-templates).

## General behavior

Returns a new [page object](/reference/page).

> **Some page `properties` are not supported via the API.**
> 
> A request body that includes `rollup`, `created_by`, `created_time`, `last_edited_by`, or `last_edited_time` values in the properties object returns an error. These Notion-generated values cannot be created or updated via the API. If the `parent` contains any of these properties, then the new page’s corresponding values are automatically created.

> **Requirements**
> 
> Your integration must have [Insert Content capabilities](/reference/capabilities#content-capabilities) on the target parent page or database in order to call this endpoint. To update your integrations capabilities, navigation to the [My integrations](https://www.notion.so/my-integrations) dashboard, select your integration, go to the **Capabilities** tab, and update your settings as needed.
> 
> Attempting a query without update content capabilities returns an HTTP response with a 403 status code.

## Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
```