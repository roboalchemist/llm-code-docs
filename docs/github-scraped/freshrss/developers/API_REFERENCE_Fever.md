# FreshRSS Fever API Implementation - Complete Reference

## Overview

FreshRSS implements the Fever API, a simpler but effective API for RSS clients. The Fever API is ideal for mobile clients seeking a lightweight integration point with fewer operations than the Google Reader API.

## Base URL and Endpoints

All Fever API endpoints are accessed via:

```text
https://<freshrss-instance>/api/fever.php
```

Example:

```text
https://freshrss.example.net/api/fever.php
```

## Authentication

### API Key Generation

The Fever API uses MD5 hash-based authentication.

**Generate API Key:**

```text
MD5("username:api_password")
```

**Example:**

For user `kevin` with API password `freshrss`:

```bash
api_key=$(echo -n "kevin:freshrss" | md5sum | cut -d' ' -f1)
echo $api_key
# Output: abc123def456...
```

### Authentication Methods

#### Method 1: Form Data (Recommended)

```bash
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?api'
```

#### Method 2: Query Parameter

```bash
curl -s 'https://freshrss.example.net/api/fever.php?api&api_key=$api_key'
```

### Initial API Check

Test basic API access without authentication:

```bash
curl -s -F "api_key=" 'https://freshrss.example.net/api/fever.php?api'
```

**Response (Unauthenticated):**

```json
{
  "api_version": 3,
  "auth": 0
}
```

### Authenticated Request

```bash
api_key=$(echo -n "kevin:freshrss" | md5sum | cut -d' ' -f1)
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?api'
```

**Response (Authenticated):**

```json
{
  "api_version": 3,
  "auth": 1,
  "last_refreshed_on_time": "1520013061"
}
```text

**Fields:**

- `api_version`: API version number
- `auth`: Authentication status (0 = failed, 1 = success)
- `last_refreshed_on_time`: Unix timestamp of last feed refresh

## Core API Endpoints

### Information

#### Get API Status

**Endpoint:**

```text
POST /api/fever.php?api
```text

**Form Parameters:**

```text
api_key=<api_key>
```

**Example:**

```bash
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?api'
```

**Response:**

```json
{
  "api_version": 3,
  "auth": 1,
  "last_refreshed_on_time": "1520013061"
}
```text

### Feeds and Groups

#### Get Feeds

Returns all feeds subscribed by the user.

**Endpoint:**

```text
POST /api/fever.php?feeds
```

**Example:**

```bash
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?feeds'
```

**Response:**

```json
{
  "feeds": [
    {
      "id": 1,
      "favicon_id": 0,
      "title": "Example Blog",
      "url": "http://example.com/feed.xml",
      "site_url": "http://example.com",
      "is_spark": 0,
      "last_updated_on_time": 1234567890
    },
    {
      "id": 2,
      "favicon_id": 1,
      "title": "Tech News",
      "url": "http://technews.com/feed.xml",
      "site_url": "http://technews.com",
      "is_spark": 0,
      "last_updated_on_time": 1234567890
    }
  ],
  "feeds_groups": [
    {
      "feed_ids": "1,2",
      "group_id": 1
    }
  ]
}
```text

**Feed Fields:**

- `id`: Feed ID (numeric)
- `favicon_id`: Favicon identifier for custom icon
- `title`: Feed title
- `url`: Feed URL
- `site_url`: Website URL
- `is_spark`: Spark status (not typically used)
- `last_updated_on_time`: Unix timestamp

**Feeds Groups:**

- `feed_ids`: Comma-separated list of feed IDs
- `group_id`: Group/category ID

#### Get Groups

Returns all feed groups/categories.

**Endpoint:**

```text
POST /api/fever.php?groups
```

**Example:**

```bash
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?groups'
```

**Response:**

```json
{
  "groups": [
    {
      "id": 1,
      "title": "Technology",
      "parent_id": 0
    },
    {
      "id": 2,
      "title": "News",
      "parent_id": 0
    }
  ]
}
```text

**Group Fields:**

- `id`: Group ID
- `title`: Group/category name
- `parent_id`: Parent group ID (0 for root)

### Unread Status

#### Get Unread Item IDs

Returns IDs of all unread items.

**Endpoint:**

```text
POST /api/fever.php?unread_item_ids
```

**Parameters:**

- `since_id=<timestamp>`: Items newer than timestamp

**Example:**

```bash
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?unread_item_ids'
```

**Response:**

```json
{
  "unread_item_ids": "1,2,3,5,8,13,21,34",
  "max": 1234567890
}
```text

**Fields:**

- `unread_item_ids`: Comma-separated list of unread item IDs
- `max`: Unix timestamp (used for next sync)

### Saved/Starred Items

#### Get Saved Item IDs

Returns IDs of all starred/saved items.

**Endpoint:**

```text
POST /api/fever.php?saved_item_ids
```

**Parameters:**

- `since_id=<timestamp>`: Items starred after timestamp

**Example:**

```bash
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?saved_item_ids'
```

**Response:**

```json
{
  "saved_item_ids": "100,150,200",
  "max": 1234567890
}
```text

### Items (Articles)

#### Get All Items

Returns feed items/articles.

**Endpoint:**

```text
POST /api/fever.php?items
```

**Parameters:**

- `since_id=<timestamp>`: Items modified after timestamp
- `max_id=<item-id>`: Get items before this ID
- `with_ids=<id-list>`: Get specific items (comma-separated IDs)

**Example - Get Recent Items:**

```bash
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?items'
```

**Example - Get Items Since Timestamp:**

```bash
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?items&since_id=1234567890'
```

**Example - Get Specific Items:**

```bash
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?items&with_ids=1,2,3,5,8'
```

**Response:**

```json
{
  "items": [
    {
      "id": 1,
      "feed_id": 1,
      "title": "Article Title",
      "author": "Article Author",
      "html": "<p>Article content here</p>",
      "summary": "Article summary",
      "links": [
        {
          "href": "http://example.com/article",
          "rel": "alternate",
          "type": "text/html"
        }
      ],
      "origin": {
        "stream_id": "feed/1",
        "title": "Example Blog",
        "htmlUrl": "http://example.com"
      },
      "created_on_time": 1234567890,
      "updated_on_time": 1234567890
    }
  ],
  "total_items": 1,
  "max": 1234567890
}
```text

**Item Fields:**

- `id`: Item ID
- `feed_id`: Feed ID
- `title`: Article title
- `author`: Article author
- `html`: Full HTML content
- `summary`: Article summary/description
- `links`: Array of article links
- `origin`: Feed information
- `created_on_time`: Unix timestamp when created
- `updated_on_time`: Unix timestamp when updated

#### Mark Item as Read

**Endpoint:**

```text
POST /api/fever.php?mark=item&as=read
```text

**Parameters:**

```text
id=<item-id>
```

**Example:**

```bash
curl -s -F "api_key=$api_key" \
  -F "id=123" \
  'https://freshrss.example.net/api/fever.php?mark=item&as=read'
```text

#### Mark Item as Unread

**Endpoint:**

```text
POST /api/fever.php?mark=item&as=unread
```text

**Parameters:**

```text
id=<item-id>
```

**Example:**

```bash
curl -s -F "api_key=$api_key" \
  -F "id=123" \
  'https://freshrss.example.net/api/fever.php?mark=item&as=unread'
```text

#### Mark Item as Saved/Starred

**Endpoint:**

```text
POST /api/fever.php?mark=item&as=saved
```text

**Parameters:**

```text
id=<item-id>
```

**Example:**

```bash
curl -s -F "api_key=$api_key" \
  -F "id=123" \
  'https://freshrss.example.net/api/fever.php?mark=item&as=saved'
```text

#### Mark Item as Unsaved

**Endpoint:**

```text
POST /api/fever.php?mark=item&as=unsaved
```text

**Parameters:**

```text
id=<item-id>
```

**Example:**

```bash
curl -s -F "api_key=$api_key" \
  -F "id=123" \
  'https://freshrss.example.net/api/fever.php?mark=item&as=unsaved'
```text

### Feed Operations

#### Mark Feed as Read

**Endpoint:**

```text
POST /api/fever.php?mark=feed&as=read
```text

**Parameters:**

```text
id=<feed-id>
before=<timestamp>   [optional - mark items before this timestamp]
```

**Example:**

```bash
curl -s -F "api_key=$api_key" \
  -F "id=1" \
  'https://freshrss.example.net/api/fever.php?mark=feed&as=read'
```text

#### Mark Group as Read

**Endpoint:**

```text
POST /api/fever.php?mark=group&as=read
```text

**Parameters:**

```text
id=<group-id>
before=<timestamp>   [optional]
```

**Example:**

```bash
curl -s -F "api_key=$api_key" \
  -F "id=1" \
  'https://freshrss.example.net/api/fever.php?mark=group&as=read'
```text

### Favicons

#### Get Favicon

Returns favicon for a feed.

**Endpoint:**

```text
GET /api/fever.php?favicons
```

**Parameters:**

- `id=<feed-id>`: Feed ID

**Example:**

```bash
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?favicons&id=1'
```

**Response:**

```json
{
  "favicons": [
    {
      "id": 1,
      "data": "base64-encoded-image-data"
    }
  ]
}
```

## Query Parameters Reference

### Mark Operations

| Query | Purpose |
|-------|---------|
| `?mark=item&as=read&id=<id>` | Mark item as read |
| `?mark=item&as=unread&id=<id>` | Mark item as unread |
| `?mark=item&as=saved&id=<id>` | Mark item as saved/starred |
| `?mark=item&as=unsaved&id=<id>` | Mark item as unsaved |
| `?mark=feed&as=read&id=<id>` | Mark feed as read |
| `?mark=group&as=read&id=<id>` | Mark group as read |

### Information Queries

| Query | Purpose |
|-------|---------|
| `?api` | Get API status |
| `?feeds` | Get all feeds |
| `?groups` | Get all groups |
| `?unread_item_ids` | Get unread item IDs |
| `?saved_item_ids` | Get saved item IDs |
| `?items` | Get items |
| `?favicons` | Get favicons |

## Supported Features

The following features are implemented in FreshRSS:

### Implemented Features

- Fetching categories/groups
- Fetching feeds
- Fetching RSS items (new, favorites, unread, by_id, by_feed, by_category, since)
- Fetching favicons
- Setting read marker for item(s)
- Setting starred marker for item(s)
- Setting read marker for feed
- Setting read marker for category
- Supports FreshRSS extensions using the `entry_before_display` hook

### Not Implemented

- **Hot Links** aka **hot** - No equivalent functionality in FreshRSS exists to simulate this feature

## Pagination and Sync Strategy

### Efficient Synchronization

1. **Initial Sync:**

   - Get all feeds with `?feeds`
   - Get all groups with `?groups`
   - Get all unread item IDs with `?unread_item_ids`
   - Fetch items with `?items`

2. **Incremental Sync:**

   - Use `max` timestamp from previous response
   - Query with `?items&since_id=<max-timestamp>`
   - Update local unread counts

3. **Fetch Items:**

   - Use `?items&with_ids=<id-list>` to get specific items
   - Store `max` value for next sync

### Example Sync Flow

```bash
# Step 1: Get current state
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?api'

# Step 2: Get feed list
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?feeds'

# Step 3: Get unread IDs
unread=$(curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?unread_item_ids')
max=$(echo $unread | grep -o '"max":"[^"]*' | cut -d'"' -f4)

# Step 4: Get unread items
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?items&since_id='$max

# Step 5: Mark items as read
for id in 1 2 3; do
  curl -s -F "api_key=$api_key" -F "id=$id" \
    'https://freshrss.example.net/api/fever.php?mark=item&as=read'
done
```

## Error Responses

### Unauthorized

```json
{
  "api_version": 3,
  "auth": 0
}
```

Check your API key and ensure the user's API password is set correctly.

### Invalid Request

```json
{
  "error": "Invalid parameter"
}
```

Verify query parameters and form data are correctly formatted.

## Testing and Debugging

### Manual Testing with cURL

```bash
# Calculate API key
api_key=$(echo -n "username:password" | md5sum | cut -d' ' -f1)

# Test API access
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?api'

# Get feeds
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?feeds'

# Get unread items
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?items'
```

### Enable API Logging

Add logging to `/api/fever.php` to debug client interactions:

```php
file_put_contents(__DIR__ . '/fever.log',
  $_SERVER['HTTP_USER_AGENT'] . ': ' . json_encode($_REQUEST) . PHP_EOL,
  FILE_APPEND
);
```

Then check the log file for client requests:

```bash
tail -f /path/to/freshrss/api/fever.log
```

### Testing with Postman

1. Create a new POST request
2. URL: `https://freshrss.example.net/api/fever.php?api`
3. Body tab > form-data
4. Add key `api_key` with your API key value
5. Send request

## Compatible Clients

| Application | Platform | Type |
|-------------|----------|------|
| Fluent Reader | Windows, Linux, macOS | Desktop |
| Fluent Reader Lite | Android, iOS | Mobile |
| Read You | Android | Mobile |
| Fiery Feeds | iOS | Mobile |
| Newsflash | Linux | Desktop |
| Unread | iOS | Mobile |
| Reeder Classic | iOS, macOS | Mobile/Desktop |
| ReadKit | macOS | Desktop |
| FreshRSS Python Client | Python | Library |

## Best Practices

### 1. API Key Management

- Generate unique API passwords per device/client
- Don't hardcode API keys in applications
- Store API keys securely (encrypted storage)
- Regenerate keys if compromised

### 2. Request Optimization

- Batch requests when possible
- Cache feed/group metadata
- Use `since_id` parameter for incremental syncs
- Minimize number of API calls

### 3. Error Handling

- Implement retry logic for failed requests
- Handle authentication failures gracefully
- Log API errors for troubleshooting
- Provide user feedback for sync issues

### 4. Performance

- Reduce sync frequency (not every minute)
- Cache responses locally
- Use appropriate timeouts
- Implement background sync

## References

- [Original Fever API Documentation](https://feedafever.com/api)
- [FreshRSS API Implementation](https://github.com/FreshRSS/FreshRSS/blob/edge/p/api/fever.php)
- [FreshRSS Mobile Access Configuration](https://github.com/FreshRSS/FreshRSS/blob/edge/docs/en/users/06_Mobile_access.md)
- [Compatible Clients](https://github.com/FreshRSS/FreshRSS#apis--native-apps)
