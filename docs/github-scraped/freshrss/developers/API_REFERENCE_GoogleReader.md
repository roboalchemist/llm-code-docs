# FreshRSS Google Reader Compatible API - Complete Reference

## Overview

FreshRSS implements a Google Reader compatible API that allows mobile clients and other RSS applications to interact with FreshRSS programmatically. This API is feature-rich and suitable for advanced RSS clients that need comprehensive access to subscription data, articles, and user interactions.

## Base URL and Endpoints

All Google Reader API endpoints are accessed via:

```
https://<freshrss-instance>/api/greader.php/
```

Example:
```
https://freshrss.example.net/api/greader.php/
```

## Authentication

### 1. Client Login (Initial Authentication)

Obtain authentication credentials using the ClientLogin endpoint.

**Endpoint:**
```
POST /accounts/ClientLogin
```

**Parameters:**
```
Email=<username>
Passwd=<api-password>
```

**Example:**
```bash
curl -X POST 'https://freshrss.example.net/api/greader.php/accounts/ClientLogin' \
  -d 'Email=alice&Passwd=Abcdef123456'
```

**Response:**
```
SID=alice/8e6845e089457af25303abc6f53356eb60bdb5f8
Auth=alice/8e6845e089457af25303abc6f53356eb60bdb5f8
```

**Fields:**
- `SID`: Session ID (Session Identifier)
- `Auth`: Authentication token used in subsequent requests

### 2. Authorization Header

Use the `Auth` token in subsequent requests with the Authorization header:

```
Authorization: GoogleLogin auth=<auth-token>
```

**Example:**
```bash
curl -H "Authorization: GoogleLogin auth=alice/8e6845e089457af25303abc6f53356eb60bdb5f8" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/list?output=json'
```

## Core API Endpoints

### Subscription Management

#### List All Subscriptions

**Endpoint:**
```
GET /reader/api/0/subscription/list
```

**Parameters:**
- `output=json` (or xml): Response format

**Response (JSON):**
```json
{
  "subscriptions": [
    {
      "id": "feed/http://example.com/feed.xml",
      "title": "Example Blog",
      "categories": [
        {
          "id": "user/alice/label/Technology",
          "label": "Technology"
        }
      ],
      "sortid": "0",
      "firstitemmsec": "1234567890000",
      "htmlUrl": "http://example.com",
      "iconUrl": ""
    }
  ]
}
```

**Fields:**
- `id`: Feed identifier (format: `feed/<feed-url>`)
- `title`: Feed title
- `categories`: Array of labels/categories assigned to this feed
- `sortid`: Sort order ID
- `firstitemmsec`: Timestamp of first article (milliseconds)
- `htmlUrl`: Website URL for the feed
- `iconUrl`: Feed favicon URL

#### Add Subscription

**Endpoint:**
```
POST /reader/api/0/subscription/edit
```

**Parameters:**
```
ac=subscribe
s=feed/<feed-url>
t=<optional-title>
```

**Example:**
```bash
curl -X POST \
  -H "Authorization: GoogleLogin auth=<auth-token>" \
  -d 'ac=subscribe&s=feed/http://example.com/feed.xml&t=Example%20Blog' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/edit'
```

#### Unsubscribe

**Endpoint:**
```
POST /reader/api/0/subscription/edit
```

**Parameters:**
```
ac=unsubscribe
s=feed/<feed-id>
```

**Example:**
```bash
curl -X POST \
  -H "Authorization: GoogleLogin auth=<auth-token>" \
  -d 'ac=unsubscribe&s=feed/52' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/edit'
```

#### Update Subscription Metadata

**Endpoint:**
```
POST /reader/api/0/subscription/edit
```

**Parameters:**
```
ac=edit
s=feed/<feed-id>
t=<new-title>
r=<new-category-id>   [optional]
```

**Example:**
```bash
curl -X POST \
  -H "Authorization: GoogleLogin auth=<auth-token>" \
  -d 'ac=edit&s=feed/52&t=New%20Title&r=user/alice/label/News' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/edit'
```

### Stream Contents (Articles)

#### Get Stream Contents

Retrieve articles from a specific stream (feed, category, or reading list).

**Endpoint:**
```
GET /reader/api/0/stream/contents/<stream-id>
```

**Stream IDs:**
- `reading-list`: All articles
- `starred`: Starred/saved articles
- `feed/<feed-id>`: Specific feed
- `user/<user-id>/label/<label-name>`: Category/label

**Parameters:**
- `output=json` (or xml): Response format
- `n=<number>`: Max items to return (default: 20)
- `xt=<exclude-tag>`: Exclude items with tag
- `c=<continuation-token>`: For pagination

**Example:**
```bash
curl -s -H "Authorization: GoogleLogin auth=<auth-token>" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/stream/contents/reading-list?output=json&n=20'
```

**Response (JSON):**
```json
{
  "direction": "ltr",
  "id": "user/alice/state/com.google/reading-list",
  "title": "Reading list",
  "description": "",
  "self": [
    {
      "href": "https://freshrss.example.net/api/greader.php/reader/api/0/stream/contents/user/alice/state/com.google/reading-list"
    }
  ],
  "updated": 1234567890,
  "items": [
    {
      "id": "tag:google.com,2005:entry/item-id",
      "categories": [
        "user/alice/state/com.google/read",
        "user/alice/state/com.google/starred"
      ],
      "title": "Article Title",
      "content": {
        "direction": "ltr",
        "content": "<p>Article content here</p>"
      },
      "summary": {
        "direction": "ltr",
        "content": "Article summary"
      },
      "author": "Article Author",
      "published": 1234567890,
      "updated": 1234567890,
      "alternate": [
        {
          "href": "http://example.com/article",
          "type": "text/html"
        }
      ],
      "canonical": [
        {
          "href": "http://example.com/article"
        }
      ],
      "origin": {
        "streamId": "feed/http://example.com/feed.xml",
        "title": "Example Blog",
        "htmlUrl": "http://example.com"
      }
    }
  ],
  "continuation": "pagination-token-here"
}
```

**Item Fields:**
- `id`: Unique item identifier
- `categories`: Array of tags/states (e.g., read, starred)
- `title`: Article title
- `content`: Full article content
- `summary`: Article summary/description
- `author`: Article author
- `published`: Publication timestamp (seconds)
- `updated`: Last update timestamp (seconds)
- `alternate`: Links to original article
- `origin`: Feed information
- `continuation`: Token for next page of results

#### Get Unread Count

**Endpoint:**
```
GET /reader/api/0/unread-count?output=json
```

**Response (JSON):**
```json
{
  "max": 1234567890,
  "unreadcounts": [
    {
      "id": "feed/http://example.com/feed.xml",
      "count": 5,
      "newestItemTimestampUsec": "1234567890000"
    },
    {
      "id": "user/alice/label/Technology",
      "count": 12,
      "newestItemTimestampUsec": "1234567890000"
    }
  ]
}
```

### Tags and Labels

#### List All Tags

**Endpoint:**
```
GET /reader/api/0/tag/list?output=json
```

**Response (JSON):**
```json
{
  "tags": [
    {
      "id": "user/alice/label/Technology",
      "sortid": "0"
    },
    {
      "id": "user/alice/label/News",
      "sortid": "1"
    }
  ]
}
```

#### Add Tag to Item

**Endpoint:**
```
POST /reader/api/0/edit-tag
```

**Parameters:**
```
a=<tag-id>     [Add tag]
r=<tag-id>     [Remove tag]
i=<item-id>
```

**Example:**
```bash
curl -X POST \
  -H "Authorization: GoogleLogin auth=<auth-token>" \
  -d 'a=user/alice/label/Important&i=tag:google.com,2005:entry/item-123' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/edit-tag'
```

#### Remove Tag from Item

**Endpoint:**
```
POST /reader/api/0/edit-tag
```

**Parameters:**
```
r=<tag-id>
i=<item-id>
```

**Example:**
```bash
curl -X POST \
  -H "Authorization: GoogleLogin auth=<auth-token>" \
  -d 'r=user/alice/label/Technology&i=tag:google.com,2005:entry/item-123' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/edit-tag'
```

### Item Actions

#### Mark Item as Read/Unread

**Endpoint:**
```
POST /reader/api/0/edit-tag
```

**Read Tag IDs:**
- Read: `user/<user-id>/state/com.google/read`
- Unread: `user/<user-id>/state/com.google/kept-unread`

**Example - Mark as Read:**
```bash
curl -X POST \
  -H "Authorization: GoogleLogin auth=<auth-token>" \
  -d 'a=user/alice/state/com.google/read&i=tag:google.com,2005:entry/item-123' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/edit-tag'
```

**Example - Mark as Unread:**
```bash
curl -X POST \
  -H "Authorization: GoogleLogin auth=<auth-token>" \
  -d 'a=user/alice/state/com.google/kept-unread&i=tag:google.com,2005:entry/item-123' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/edit-tag'
```

#### Star/Save Items

**Endpoint:**
```
POST /reader/api/0/edit-tag
```

**Parameters:**
```
a=user/alice/state/com.google/starred
i=<item-id>
```

**Example:**
```bash
curl -X POST \
  -H "Authorization: GoogleLogin auth=<auth-token>" \
  -d 'a=user/alice/state/com.google/starred&i=tag:google.com,2005:entry/item-123' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/edit-tag'
```

#### Mark All Items in Feed as Read

**Endpoint:**
```
POST /reader/api/0/mark-all-as-read
```

**Parameters:**
```
s=<stream-id>
ts=<timestamp>   [optional - mark items before this timestamp]
```

**Example:**
```bash
curl -X POST \
  -H "Authorization: GoogleLogin auth=<auth-token>" \
  -d 's=feed/http://example.com/feed.xml' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/mark-all-as-read'
```

### Token Generation

#### Get CSRF Token

Required for state-changing operations in some contexts.

**Endpoint:**
```
GET /reader/api/0/token
```

**Response:**
```
8e6845e089457af25303abc6f53356eb60bdb5f8ZZZZZZZZZZZZZZZZZ
```

### Search

#### Search Items

**Endpoint:**
```
GET /reader/api/0/search/items?q=<query>&output=json
```

**Parameters:**
- `q=<search-query>`: Search terms
- `output=json`: Response format
- `n=<number>`: Results per page

**Example:**
```bash
curl -s -H "Authorization: GoogleLogin auth=<auth-token>" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/search/items?q=technology&output=json'
```

## Pagination

The API uses continuation tokens for pagination.

**Getting Next Page:**

```bash
curl -s -H "Authorization: GoogleLogin auth=<auth-token>" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/stream/contents/reading-list?output=json&c=<continuation-token>'
```

The `c` parameter contains the token from the previous response's `continuation` field.

## Response Formats

### JSON Format

Use `?output=json` to get JSON responses.

```bash
curl 'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/list?output=json'
```

### XML Format

Use `?output=xml` or omit the output parameter for XML (default).

```bash
curl 'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/list?output=xml'
```

## Common Tag IDs

| Tag | Purpose |
|-----|---------|
| `user/<user-id>/state/com.google/read` | Mark as read |
| `user/<user-id>/state/com.google/kept-unread` | Keep/mark as unread |
| `user/<user-id>/state/com.google/starred` | Mark as starred/saved |
| `user/<user-id>/label/<label-name>` | User-defined label/category |
| `user/<user-id>/state/com.google/reading-list` | Reading list (all items) |
| `user/<user-id>/state/com.google/broadcast` | Shared/broadcast items |

## Stream IDs

| Stream | Description |
|--------|-------------|
| `reading-list` | All articles |
| `starred` | Starred articles |
| `feed/<feed-url>` | Specific feed |
| `user/<user-id>/label/<label-name>` | Specific label/category |

## Error Handling

### Unauthorized (401)

```json
{
  "error": "Unauthorized"
}
```

Ensure your auth token is valid and hasn't expired.

### Not Found (404)

```json
{
  "error": "Not found"
}
```

Check that the feed ID or item ID is correct.

### Server Error (500)

```json
{
  "error": "Internal server error"
}
```

Check FreshRSS server logs for details.

## Best Practices

### 1. Efficient Synchronization

- Use unread counts to detect changes
- Store local timestamps to minimize data transfer
- Use continuation tokens for paginated results
- Don't re-fetch all items on every sync

### 2. Token Management

- Cache authentication tokens locally
- Regenerate tokens periodically (not on every request)
- Handle token expiration gracefully

### 3. Error Handling

- Implement retry logic for network errors
- Respect rate limits if implemented
- Log API errors for debugging

### 4. Performance

- Batch operations when possible
- Use reasonable page sizes (n parameter)
- Cache feed metadata locally

## Example Workflows

### Complete Sync Workflow

```bash
# 1. Authenticate
AUTH=$(curl -s -X POST \
  -d 'Email=alice&Passwd=password' \
  'https://freshrss.example.net/api/greader.php/accounts/ClientLogin' | grep Auth | cut -d= -f2)

# 2. Get subscriptions
curl -s -H "Authorization: GoogleLogin auth=$AUTH" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/list?output=json'

# 3. Get unread counts
curl -s -H "Authorization: GoogleLogin auth=$AUTH" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/unread-count?output=json'

# 4. Fetch new articles
curl -s -H "Authorization: GoogleLogin auth=$AUTH" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/stream/contents/reading-list?output=json&n=100'

# 5. Mark items as read
curl -X POST \
  -H "Authorization: GoogleLogin auth=$AUTH" \
  -d 'a=user/alice/state/com.google/read&i=tag:google.com,2005:entry/123' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/edit-tag'
```

### Add Feed and Get Articles

```bash
# 1. Add subscription
curl -X POST \
  -H "Authorization: GoogleLogin auth=$AUTH" \
  -d 'ac=subscribe&s=feed/http://example.com/feed.xml' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/edit'

# 2. Get articles from that feed
curl -s -H "Authorization: GoogleLogin auth=$AUTH" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/stream/contents/feed/http://example.com/feed.xml?output=json'
```

## References

- [Original Google Reader API Documentation (archived)](https://web.archive.org/web/20130710044440/http://undoc.in/api.html)
- [FreshRSS Implementation](https://github.com/FreshRSS/FreshRSS/blob/edge/p/api/greader.php)
- [Compatible Clients](https://github.com/FreshRSS/FreshRSS#apis--native-apps)
- [Other Compatible Servers](https://github.com/theoldreader/api)
