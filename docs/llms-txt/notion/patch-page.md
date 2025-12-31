# Source: https://developers.notion.com/reference/patch-page.md

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
- [Get database properties](/reference/get-database-properties) (GET)
- [Update database properties](/reference/update-database-properties) (PATCH)
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

# Update page

Use this API to modify attributes of a Notion page, such as its properties, icon, or cover.

## Use cases

### Updating properties

To change the `properties` of a page in a data source, use the `properties` body parameter. This parameter can only be used if the page's parent is a [data source](/reference/data-source), aside from updating the `title` of a page outside of a data source.

The page’s `properties` schema must match the parent [data source's properties](/reference/property-object).

### Setting the icon, cover, or "in trash" status

This endpoint can be used to update any page `icon` or `cover`, and can be used to [archive](/reference/archive-a-page) or restore any page.

### Locking and unlocking a page

Use the `is_locked` boolean parameter to lock or unlock the page from being further edited in the Notion app UI. Note that this setting doesn't affect the ability to update the page using the API.

### Applying a page template

Use the `template` body parameter object to apply a [template](/reference/creating-pages-from-templates) to an existing page. This can either be the parent data source's default template (`type=default`), or a specific template (`type=template_id`).

After the API request finishes, Notion's systems merge the content and properties from your chosen template into the current page.

For more information, visit our related guide: [Creating pages from templates](/docs/creating-pages-from-templates).

### Erasing content from a page

Use the `erase_content` flag to delete all block children of the current page. **Use caution** with this parameter, since this is a destructive action that **cannot** be reversed using the API.

The main use case is for applying a [template](/reference/creating-pages-from-templates) in scenarios where it makes sense to clear all of the existing page content and replace it with the template page's content, instead of appending the template content to what's already on the page.

### Adding content to a page

To add content, use the [append block children](/reference/patch-block-children) API instead. The `page_id` can be passed as the `block_id` when adding block children to the page.

## General behavior

Returns the updated [page object](/reference/page).

> 📘 Requirements
> Your integration must have [update content capabilities](/reference/capabilities#content-capabilities) on the target page in order to call this endpoint. To update your integrations capabilities, navigation to the [My integrations](https://www.notion.so/my-integrations) dashboard, select your integration, go to the **Capabilities** tab, and update your settings as needed.
> 
> Attempting a query without update content capabilities returns an HTTP response with a 403 status code.
> 
> 🚧 Limitations
> - Updating [rollup property values](/reference/property-value-object#rollup-property-values) is not supported.
> - A page’s `parent` cannot be changed.

## Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
```