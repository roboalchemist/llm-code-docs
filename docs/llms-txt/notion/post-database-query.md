# Source: https://developers.notion.com/reference/post-database-query.md

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
- [Delete a database](/reference/delete-database) (del)
```

# Post a Database Query

[Post a database query](https://docs.rapidapi.com/reference/post-database-query)

## Request Method
- **Method**: `POST`
- **URL**: `/database/{id}/query`
- **Path Parameters**:
  - `{id}`: The ID of the database to query.

## Response Example

### Sample Response

```json
{
  "result": [
    {
      "id": 1,
      "name": "Database 1",
      "created_at": "2023-01-01T12:00:00Z"
    },
    {
      "id": 2,
      "name": "Database 2",
      "created_at": "2023-01-02T12:00:00Z"
    }
  ]
}
```

### Error Response

```json
{
  "error": "DB_ERROR",
  "message": "An error occurred while executing the query.",
  "details": "Please check the query parameters and try again."
}
```

## Notes

- This endpoint is used to execute a search query on a database.
- The response includes a list of entries that match the query criteria.
- If no matches are found, an empty array will be returned with a corresponding error message.
- You can filter the results using query parameters.
- You can sort the results using query parameters.
- You can specify the number of entries to return using query parameters.
- You can retrieve the schema of the database using the `/database/{id}/schema` endpoint.
- You can create a new entry using the `/database/{id}/add` endpoint.
- You can update an existing entry using the `/database/{id}/update` endpoint.
- You can delete an existing entry using the `/database/{id}/delete` endpoint.
- You can list all entries in the database using the `/database/{id}/list` endpoint.
- You can retrieve a specific entry using the `/database/{id}/entry/{id}` endpoint.
- You can retrieve the schema of an entry using the `/database/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/database/{id}/comment` endpoint.
- You can retrieve a comment using the `/database/{id}/comment/{id}` endpoint.
- You can list comments using the `/database/{id}/comments` endpoint.
- You can complete a file upload using the `/database/{id}/file/upload` endpoint.
- You can retrieve a file upload using the `/database/{id}/file/upload/{id}` endpoint.
- You can list all file uploads using the `/database/{id}/file/uploads` endpoint.
- You can send a file upload using the `/database/{id}/file/upload` endpoint.
- You can retrieve a file upload using the `/database/{id}/file/upload/{id}` endpoint.
- You can list all file uploads using the `/database/{id}/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/database/{id}/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new comment using the `/comment` endpoint.
- You can retrieve a comment using the `/comment/{id}` endpoint.
- You can list comments using the `/comments` endpoint.
- You can complete a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can send a file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can retrieve the schema of a file upload using the `/file/upload/{id}/schema` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You can delete a search using the `/search/{id}/delete` endpoint.
- You can list searches using the `/search` endpoint.
- You can retrieve a specific search result using the `/search/{id}/entry/{id}` endpoint.
- You can retrieve the schema of a search result using the `/search/{id}/entry/{id}/schema` endpoint.
- You can create a new file upload using the `/file/upload` endpoint.
- You can retrieve a file upload using the `/file/upload/{id}` endpoint.
- You can list all file uploads using the `/file/uploads` endpoint.
- You can create a new search using the `/search` endpoint.
- You can retrieve search results using the `/search` endpoint.
- You

# Query a database

> ❗️Deprecated as of version 2025-09-03
> 
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/docs/upgrade-guide-2025-09-03).
> 
> Refer to the new APIs instead:
> 
> - [Query a data source](/reference/query-a-data-source)

Gets a list of [Pages](/reference/page) and/or [Databases](/reference/database) contained in the database, filtered and ordered according to the filter conditions and sort criteria provided in the request. The response may contain fewer than `page_size` of results. If the response includes a `next_cursor` value, refer to the [pagination reference](/reference/intro#pagination) for details about how to use a cursor to iterate through the list.

> 📘[Wiki](https://www.notion.so/help/wikis-and-verified-pages) databases can contain both pages and databases as children.

[**Filters**](/reference/post-database-query-filter) are similar to the [filters provided in the Notion UI](https://www.notion.so/help/views-filters-and-sorts) where the set of filters and filter groups chained by "And" in the UI is equivalent to having each filter in the array of the compound `"and"` filter. Similar a set of filters chained by "Or" in the UI would be represented as filters in the array of the `"or"` compound filter.  
Filters operate on database properties and can be combined. If no filter is provided, all the pages in the database will be returned with pagination.

![1340](https://files.readme.io/6fe4a44-Screen_Shot_2021-12-23_at_11.46.21_AM.png)

The above filters in the UI can be represented as the following filter object

```json
{
  "and": [
    {
      "property": "Done",
      "checkbox": {
        "equals": true
      }
    },
    {
      "or": [
        {
          "property": "Tags",
          "contains": "A"
        },
        {
          "property": "Tags",
          "contains": "B"
        }
      ]
    }
  ]
}
```

In addition to chained filters, databases can be queried with single filters.

```json
{
    "property": "Done",
    "checkbox": {
        "equals": true
    }
}
```

[**Sorts**](/reference/post-database-query-sort) are similar to the [sorts provided in the Notion UI](https://notion.so/notion/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e#0eb303043b1742468e5aff2f3f670505). Sorts operate on database properties or page timestamps and can be combined. The order of the sorts in the request matter, with earlier sorts taking precedence over later ones.

The properties of the database schema returned in the response body can be filtered with the `filter_properties` query parameter.

```http
https://api.notion.com/v1/databases/[database_id]/query?filter_properties=[property_id_1]
```

Multiple filter properties can be provided by chaining the `filter_properties` query param.

```http
https://api.notion.com/v1/databases/[database_id]/query?filter_properties=[property_id_1]&filter_properties=[property_id_2]
```

Property IDs can be determined with the [Retrieve a database](/reference/retrieve-a-database) endpoint.

If you are using the [Notion JavaScript SDK](https://github.com/makenotion/notion-sdk-js), the `filter_properties` endpoint expects an array of property ID strings.

```javascript
notion.databases.query({
    database_id: id,
    filter_properties: ["propertyID1", "propertyID2"]
})
```

> 📘Permissions
> 
> Before an integration can query a database, the database must be shared with the integration. Attempting to query a database that has not been shared will return an HTTP response with a 404 status code.
> 
> To share a database with an integration, click the ••• menu at the top right of a database page, scroll to `Add connections`, and use the search bar to find and select the integration from the dropdown list.

> 📘Integration capabilities
> 
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

> 📘To display the page titles of related pages rather than just the ID:
> 
> 1. Add a rollup property to the database which uses a formula to get the related page's title. This works well if you have access to updating the database's schema.
> 2. Otherwise, [retrieve the individual related pages](/reference/retrieve-a-page) using each page ID.

> 🚧Formula and Rollup Limitation
> 
> - If a formula depends on a page property that is a relation, and that relation has more than 25 references, only 25 will be evaluated as part of the formula.
> - Rollups and formulas that depend on multiple layers of relations may not return correct results.

### Errors

Returns a 404 HTTP response if the database doesn't exist, or if the integration doesn't have access to the database.

Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

_Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information._
```