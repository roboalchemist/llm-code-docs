# Source: https://developers.notion.com/reference/capabilities.md

# Notion API

## Integration capabilities

- [Introduction](https://docs.notion.so/reference/intro)
- [Integration capabilities](https://docs.notion.so/reference/capabilities)
- [Webhooks](https://docs.notion.so/reference/webhooks)
  - [Event types & delivery](https://docs.notion.so/reference/webhooks-events-delivery)
- [Request limits](https://docs.notion.so/reference/request-limits)
- [Status codes](https://docs.notion.so/reference/status-codes)
- [Versioning](https://docs.notion.so/reference/versioning)
  - [Changes by version](https://docs.notion.so/reference/changes-by-version)

## Objects

### Block

- [Rich text](https://docs.notion.so/reference/rich-text)

### Page

- [Page properties](https://docs.notion.so/reference/page-property-values)
  - [Page property items](https://docs.notion.so/reference/property-item-object)

### Database

- [Database](https://docs.notion.so/reference/database)

### Data source

- [Data source properties](https://docs.notion.so/reference/data-source)

### Comment

- [Comment attachment](https://docs.notion.so/reference/comment-attachment)
- [Comment display name](https://docs.notion.so/reference/comment-display-name)

### File

- [File Upload](https://docs.notion.so/reference/file-upload)

### User

- [User](https://docs.notion.so/reference/user)

### Parent

- [Parent](https://docs.notion.so/reference/parent-object)

### Emoji

- [Emoji](https://docs.notion.so/reference/emoji-object)

### Unfurl attribute (Link Previews)

- [Unfurl attribute (Link Previews)](https://docs.notion.so/reference/unfurl-attribute-object)

## Endpoints

### Authentication

- [Create a token](https://docs.notion.so/reference/create-a-token) (post)
- [Introspect token](https://docs.notion.so/reference/introspect-token) (post)
- [Revoke token](https://docs.notion.so/reference/revoke-token) (post)
- [Refresh a token](https://docs.notion.so/reference/refresh-a-token) (post)

### Blocks

- [Append block children](https://docs.notion.so/reference/patch-block-children) (patch)
- [Retrieve a block](https://docs.notion.so/reference/retrieve-a-block) (get)
- [Retrieve block children](https://docs.notion.so/reference/get-block-children) (get)
- [Update a block](https://docs.notion.so/reference/update-a-block) (patch)
- [Delete a block](https://docs.notion.so/reference/delete-a-block) (del)

### Pages

- [Create a page](https://docs.notion.so/reference/post-page) (post)
- [Retrieve a page](https://docs.notion.so/reference/retrieve-a-page) (get)
- [Retrieve a page property item](https://docs.notion.so/reference/retrieve-a-page-property) (get)
- [Update page](https://docs.notion.so/reference/patch-page)
  - [Trash a page](https://docs.notion.so/reference/archive-a-page)

### Databases

- [Create a database](https://docs.notion.so/reference/database-create)
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

# Integration capabilities

All integrations have associated capabilities which enforce what an integration can do and see in a Notion workspace. These capabilities when put together enforce which API endpoints an integration can call, and what content and user related information they are able to see. To set your integration's capabilities see the [Authorization](/docs/authorization) guide or navigate to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations).

![A screenshot of the capability configuration screen.](https://files.readme.io/06dcfeb-Screen_Shot_2022-07-15_at_11.48.40_AM.png)

## 📘 If an integration is added to a page, then the integration can access the page’s children

When an integration receives access to a Notion page or database, it can read and write to both that resource and its children.

---

## Content capabilities

Content capabilities affect how an integration can interact with [database objects](/reference/database), [page objects](/reference/page), and [block objects](/reference/block) via the API. Additionally, these capabilities affect what information is exposed to an integration in API responses. To verify which capabilities are needed for an endpoint's desired behavior, please use the API references.

- **Read content**: This capability gives an integration access to read existing content in a Notion workspace. For example, an integration with only this capability is able to call [Retrieve a database](/reference/retrieve-a-database), but not [Update database](/reference/update-a-database).
- **Update content**: This capability gives an integration permission to update existing content in a Notion workspace. For example, an integration with only this capability is able to call the [Update page](/reference/patch-page) endpoint, but is not able to create new pages.
- **Insert content**: This capability gives an integration permission to create new content in a Notion workspace. This capability does not give the integration access to read full objects.  
  For example, an integration with only this capability is able to [Create a page](/reference/post-page) but is not able to update existing pages.

_It is possible for an integration to have any combination of these content capabilities._

---

## Comment capabilities

Comment capabilities dictate how an integration can interact with the [comments](/reference/comment-object) on a page or block.

- **Read comments**: This capability gives the integration permission to [read comments](/reference/retrieve-a-comment) from a Notion page or block.
- **Insert comments**: This capability gives the integration permission to [insert comments](/reference/create-a-comment) in a page or in an existing discussion.

---

## User capabilities

An integration can request different levels of user capabilities, which affect how [user objects](/reference/user) are returned from the Notion API:

- **No user information**: Selecting this option prevents an integration from requesting any information about users. User objects will not include any information about the user, including name, profile image, or their email address.
- **User information without email addresses**: Selecting this option ensures that User objects will include all information about a user, including name and profile image, but omit the email address.
- **User information with email addresses**: Selecting this option ensures that User objects will include all information about the user, including name, profile image, and their email address.

---

## Capability Behaviors and Best Practices

An integration's capabilities will never supersede a user's. If a user loses edit access to the page where they have added an integration, that integration will now also only have read access, regardless of the capabilities the integration was created with.

For public integrations, users will need to re-authenticate with an integration if the capabilities are changed in the time since the user last authenticated with the integration.

To learn more about setting your integration's capabilities refer to the [Authorization](/docs/authorization) guide.

In general, you want to request minimum capabilities that your integration needs in order to function. The fewer capabilities you request, the more likely a workspace admin will be able to install your integration.

For example:
- If your integration is solely bringing data into Notion (creating new pages, or adding blocks), your integration only needs **Insert content** capabilities.
- If your integration is reading data to export it out of Notion, your integration will only need **Read content** capabilities.
- If your integration is simply updating a property on a page or an existing block, your integration will only need **Update content** capabilities.
```