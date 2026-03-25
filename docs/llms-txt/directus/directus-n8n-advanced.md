# Source: https://directus.io/docs/raw/guides/integrations/n8n/directus-n8n-advanced.md

# Advanced

> Advanced guide for using Directus raw CRUD operations in n8n, including raw JSON operations, complex filters, relational queries, and query parameters.

This guide covers advanced Directus features in n8n using raw CRUD operations, which give you full access to Directus's native filter syntax, query parameters, and complex query capabilities.

**← Back to Directus + n8n Overview**

## Raw CRUD Operations

The Directus node provides raw versions of all CRUD operations that allow you to use Directus's native JSON syntax for filters, query parameters, and data manipulation. These operations give you full control over the API request.

## Available Raw Operations

Quick reference of all available raw operations organized by resource type:

<table>
<thead>
  <tr>
    <th>
      Resource
    </th>
    
    <th>
      Operation
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Items
      </strong>
    </td>
    
    <td>
      Create (Raw JSON)
    </td>
    
    <td>
      Create items with full JSON control
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Items
      </strong>
    </td>
    
    <td>
      Get (Raw JSON)
    </td>
    
    <td>
      Retrieve a single item with custom query parameters
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Items
      </strong>
    </td>
    
    <td>
      Get Many (Raw JSON)
    </td>
    
    <td>
      Retrieve multiple items with advanced filters and query parameters
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Items
      </strong>
    </td>
    
    <td>
      Update (Raw JSON)
    </td>
    
    <td>
      Update items with complex data structures
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Users
      </strong>
    </td>
    
    <td>
      Get (Raw JSON)
    </td>
    
    <td>
      Retrieve a single user with custom query parameters
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Users
      </strong>
    </td>
    
    <td>
      Get Many (Raw JSON)
    </td>
    
    <td>
      Retrieve multiple users with advanced filters and query parameters
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Users
      </strong>
    </td>
    
    <td>
      Update (Raw JSON)
    </td>
    
    <td>
      Update users with complex data structures
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Files
      </strong>
    </td>
    
    <td>
      Get (Raw JSON)
    </td>
    
    <td>
      Retrieve a single file with custom query parameters
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Files
      </strong>
    </td>
    
    <td>
      Get Many (Raw JSON)
    </td>
    
    <td>
      Retrieve multiple files with advanced filters and query parameters
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Files
      </strong>
    </td>
    
    <td>
      Update (Raw JSON)
    </td>
    
    <td>
      Update files with complex data structures
    </td>
  </tr>
</tbody>
</table>

---

<callout icon="heroicons-outline:light-bulb">

**When to Use Raw Operations**
Use raw operations when you need complex filters with logical operators (`_and`, `_or`), relational field filtering, advanced query parameters (aggregation, search, etc.), or full control over the JSON payload structure.

</callout>

## Using Raw Operations

Raw operations work similarly to their standard counterparts, but instead of using the node's form fields, you provide all data in the **JSON Data** field as a JSON object.

### Setting Up a Raw Operation

1. Add a **Directus** node to your workflow
2. Set **Resource** to Item, User, or File
3. Select a **Raw JSON** operation (e.g., "Get Many (Raw JSON)", "Create (Raw JSON)")
4. For Items operations, select the **Collection**
5. Enter your JSON data in the **JSON Data** field
6. For Get and Update operations, provide the **Item ID** if needed

<callout icon="material-symbols:warning-rounded" color="warning">

**Token Permissions**
Ensure your Directus API token has the correct permissions for the resource and operations you're using. Raw operations require the same permissions as their standard counterparts.

</callout>

### Get Many (Raw JSON)

Retrieve items with advanced filtering and query parameters:

```json
{
  "filter": {
    "status": {"_eq": "published"},
    "views": {"_gt": 1000}
  },
  "fields": "title,author.name,views",
  "sort": "-date_created",
  "limit": 10
}
```

### Get (Raw JSON)

Retrieve a single item with custom query parameters:

```json
{
  "fields": "title,content,author.name,author.email,comments.text"
}
```

### Create (Raw JSON)

Create items with full control over the JSON structure:

```json
{
  "title": "My New Post",
  "content": "Post content here",
  "status": "published",
  "author": "author-uuid-here",
  "categories": ["category-uuid-1", "category-uuid-2"]
}
```

### Update (Raw JSON)

Update items with complex data structures:

```json
{
  "title": "Updated Title",
  "status": "archived",
  "metadata": {
    "tags": ["updated", "archived"],
    "notes": "Item has been archived"
  }
}
```

## Using Filters with Raw Operations

Raw operations allow you to use Directus's complete filter syntax. Specify filters in the `filter` parameter of your **JSON Data** field.

<callout icon="material-symbols:info-outline">

**Filter Documentation**
For complete filter syntax, operators, and examples, see the [Directus Filter Rules documentation](https://directus.io/docs/guides/connect/filter-rules).

</callout>

**Example: Complex filter with logical operators**

```json
{
  "filter": {
    "_and": [
      {"status": {"_eq": "published"}},
      {
        "_or": [
          {"category": {"_eq": "tutorial"}},
          {"category": {"_eq": "guide"}}
        ]
      },
      {"views": {"_gt": 100}}
    ]
  }
}
```

**Example: Relational filtering**

```json
{
  "filter": {
    "author": {
      "name": {"_eq": "John Doe"}
    },
    "comments": {
      "_some": {
        "status": {"_eq": "approved"}
      }
    }
  }
}
```

## Query Parameters

Raw operations support all Directus query parameters. Include them in your JSON Data alongside filters:

**Common query parameters:**

```json
{
  "fields": "title,author.name,views",
  "sort": "-date_created",
  "limit": 10,
  "offset": 0
}
```

**Search:**

```json
{
  "search": "directus tutorial"
}
```

**Aggregation:**

```json
{
  "aggregate": {
    "count": "id",
    "sum": "views",
    "avg": "rating"
  },
  "groupBy": "category"
}
```

<callout icon="material-symbols:info-outline">

**Query Parameters Documentation**
For complete query parameter documentation, see the [Directus Query Parameters documentation](https://directus.io/docs/guides/connect/query-parameters).

</callout>

## Working with Relations

When using **Create (Raw JSON)** or **Update (Raw JSON)**, you can include related data directly in your JSON:

```json
{
  "title": "My Post",
  "author": "author-uuid-here",
  "categories": ["category-uuid-1", "category-uuid-2"],
  "comments": [
    {"text": "Great post!", "user": "user-uuid-here"}
  ]
}
```

## Using Expressions in Raw Operations

You can use n8n expressions in your raw JSON data for dynamic queries:

```json
{
  "filter": {
    "status": {"_eq": "{{ $json.status }}"},
    "views": {"_gt": {{ $json.min_views }}}
  },
  "fields": "{{ $json.requested_fields }}",
  "sort": "-{{ $json.sort_field }}",
  "limit": {{ $json.limit }}
}
```

## Performance Tips

- **Select only needed fields**: Use the `fields` parameter to reduce data transfer
- **Use pagination**: Use `limit` and `offset`/`page` for large datasets, process in batches with n8n's **Split In Batches** node
- **Filter in Directus**: Always use the `filter` parameter rather than processing all data in n8n

**Example:**

```json
{
  "fields": "id,title,status",
  "filter": {
    "status": {"_eq": "published"},
    "date_created": {"_gte": "$NOW(-30 days)"}
  },
  "limit": 100
}
```

---

## Next Steps

- **← Back to Overview** Return to the integration overview
- **Learn about Directus Actions →** Basic operations guide
- **Learn about Directus Triggers →** Automation workflows
