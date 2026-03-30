# FreshRSS APIs - Quick Start Guide

FreshRSS provides two different APIs for programmatic access: the **Google Reader API** and the **Fever API**. This guide helps you choose the right one for your use case.

## API Comparison

| Feature | Google Reader API | Fever API |
|---------|-------------------|-----------|
| **Complexity** | More complex, feature-rich | Simpler, lightweight |
| **Best For** | Full-featured RSS clients | Mobile clients, simple integrations |
| **Authentication** | Token-based (ClientLogin) | MD5 hash-based |
| **Response Format** | JSON/XML configurable | JSON primarily |
| **Subscription Mgmt** | Add, remove, modify subscriptions | List only |
| **Feed Groups** | Full support | Yes |
| **Unread Items** | Per-feed and global | Per-feed and global |
| **Starred Items** | Yes (full support) | Yes |
| **Tag Management** | Full tag/label system | No custom tags |
| **Search** | Yes | No |
| **CSRF Token** | Available | N/A |

## Choosing Your API

### Use Google Reader API if

- You're building a **feature-complete RSS client**
- You need to **add/remove feeds programmatically**
- You require **tag/label management**
- You need **search functionality**
- You're targeting **desktop applications**
- Your client needs **advanced categorization**

### Use Fever API if

- You're building a **mobile RSS client**
- You want a **simple, lightweight** integration
- You primarily need to **read and sync** articles
- You want **minimal authentication overhead**
- You're implementing a **feed reader widget or app**
- You prioritize **performance over features**

## Quick Setup

### Prerequisites

Before using either API, you must:

1. **Enable API Access** in FreshRSS:

   - Log in to FreshRSS web interface
   - Go to Settings > API access
   - Enable API and set an API password

2. **Get Your API Address:**

   - Google Reader: `https://<your-instance>/api/greader.php`
   - Fever: `https://<your-instance>/api/fever.php`

## Google Reader API - Quick Start

### 1. Authenticate

```bash
curl -X POST 'https://freshrss.example.net/api/greader.php/accounts/ClientLogin' \
  -d 'Email=alice&Passwd=your_api_password'
```

**Response:**

```text
SID=alice/8e6845e089457af25303abc6f53356eb60bdb5f8
Auth=alice/8e6845e089457af25303abc6f53356eb60bdb5f8
```

### 2. Use the Auth Token

```bash
AUTH="alice/8e6845e089457af25303abc6f53356eb60bdb5f8"

# List subscriptions
curl -H "Authorization: GoogleLogin auth=$AUTH" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/list?output=json'

# Get unread items
curl -H "Authorization: GoogleLogin auth=$AUTH" \
  'https://freshrss.example.net/api/greader.php/reader/api/0/stream/contents/reading-list?output=json'

# Add subscription
curl -X POST \
  -H "Authorization: GoogleLogin auth=$AUTH" \
  -d 'ac=subscribe&s=feed/http://example.com/feed.xml' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/subscription/edit'

# Mark item as read
curl -X POST \
  -H "Authorization: GoogleLogin auth=$AUTH" \
  -d 'a=user/alice/state/com.google/read&i=tag:google.com,2005:entry/item-123' \
  'https://freshrss.example.net/api/greader.php/reader/api/0/edit-tag'
```

## Fever API - Quick Start

### 1. Calculate API Key

```bash
# Generate MD5 hash of "username:api_password"
api_key=$(echo -n "alice:your_api_password" | md5sum | cut -d' ' -f1)
echo $api_key
# Output: abc123def456...
```

### 2. Use the API Key

```bash
# Check API status
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?api'

# Get feeds
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?feeds'

# Get unread items
curl -s -F "api_key=$api_key" \
  'https://freshrss.example.net/api/fever.php?items&unread_item_ids'

# Mark item as read
curl -s -F "api_key=$api_key" -F "id=123" \
  'https://freshrss.example.net/api/fever.php?mark=item&as=read'
```

## Common Workflows

### Google Reader API Full Sync

```bash
#!/bin/bash

# Configuration
BASE_URL="https://freshrss.example.net/api/greader.php"
USERNAME="alice"
PASSWORD="your_api_password"

# 1. Authenticate
echo "Authenticating..."
AUTH=$(curl -s -X POST \
  -d "Email=$USERNAME&Passwd=$PASSWORD" \
  "$BASE_URL/accounts/ClientLogin" | grep "Auth=" | cut -d= -f2)

if [ -z "$AUTH" ]; then
  echo "Authentication failed"
  exit 1
fi

echo "Auth token: $AUTH"

# 2. Get subscriptions
echo "Fetching subscriptions..."
curl -s -H "Authorization: GoogleLogin auth=$AUTH" \
  "$BASE_URL/reader/api/0/subscription/list?output=json" | jq .

# 3. Get unread count
echo "Fetching unread count..."
curl -s -H "Authorization: GoogleLogin auth=$AUTH" \
  "$BASE_URL/reader/api/0/unread-count?output=json" | jq .

# 4. Get recent articles
echo "Fetching recent articles..."
curl -s -H "Authorization: GoogleLogin auth=$AUTH" \
  "$BASE_URL/reader/api/0/stream/contents/reading-list?output=json&n=20" | jq .
```

### Fever API Sync and Mark as Read

```bash
#!/bin/bash

# Configuration
BASE_URL="https://freshrss.example.net/api/fever.php"
USERNAME="alice"
PASSWORD="your_api_password"

# 1. Generate API key
api_key=$(echo -n "$USERNAME:$PASSWORD" | md5sum | cut -d' ' -f1)
echo "API Key: $api_key"

# 2. Check API status
echo "Checking API status..."
curl -s -F "api_key=$api_key" "$BASE_URL?api" | jq .

# 3. Get feeds
echo "Fetching feeds..."
curl -s -F "api_key=$api_key" "$BASE_URL?feeds" | jq .

# 4. Get unread items
echo "Fetching unread items..."
unread_response=$(curl -s -F "api_key=$api_key" "$BASE_URL?unread_item_ids")
echo "$unread_response" | jq .

# Extract unread IDs
unread_ids=$(echo "$unread_response" | jq -r '.unread_item_ids' | tr ',' '\n')

# 5. Mark first 5 items as read
count=0
for id in $unread_ids; do
  if [ $count -ge 5 ]; then break; fi
  echo "Marking item $id as read..."
  curl -s -F "api_key=$api_key" -F "id=$id" "$BASE_URL?mark=item&as=read"
  ((count++))
done
```

## Detailed Documentation

For comprehensive documentation on each API, see:

- **[Google Reader API - Complete Reference](./API_REFERENCE_GoogleReader.md)**
  - Authentication, subscription management, stream contents, tags, items, search
  - All endpoints with parameters and response formats
  - Example workflows and best practices

- **[Fever API - Complete Reference](./API_REFERENCE_Fever.md)**
  - API key generation, feeds, groups, items, marking operations
  - All endpoints with parameters and response formats
  - Efficient sync strategies and debugging

## Mobile Access Setup

Both APIs require enabling Mobile API access in FreshRSS:

1. Log in to FreshRSS web interface
2. Go to **Settings** (gear icon)
3. Click **Mobile access** or **API access** (varies by version)
4. Enable API and set a unique **API password**
5. Save settings
6. Your API address will be displayed

Note: The API password is different from your login password and should be kept secret.

## Testing Your API

### Using cURL

```bash
# Test Google Reader API
curl -s 'https://freshrss.example.net/api/greader.php/accounts/ClientLogin' \
  -d 'Email=alice&Passwd=password' | head -5

# Test Fever API
api_key=$(echo -n "alice:password" | md5sum | cut -d' ' -f1)
curl -s -F "api_key=$api_key" 'https://freshrss.example.net/api/fever.php?api'
```

### Using Postman

**For Google Reader API:**

1. Create POST request to `/accounts/ClientLogin`
2. Body: form-data with `Email` and `Passwd`
3. Extract `Auth` token from response
4. Use Authorization header: `GoogleLogin auth=<token>`

**For Fever API:**

1. Create POST request to `?api`
2. Body: form-data with `api_key` field
3. Send and verify `"auth": 1` in response

### Using Python

```python
import hashlib
import requests

# Fever API
username = "alice"
password = "your_api_password"
api_key = hashlib.md5(f"{username}:{password}".encode()).hexdigest()

response = requests.post(
    "https://freshrss.example.net/api/fever.php?feeds",
    data={"api_key": api_key}
)
print(response.json())

# Google Reader API
auth_response = requests.post(
    "https://freshrss.example.net/api/greader.php/accounts/ClientLogin",
    data={"Email": username, "Passwd": password}
)
auth_token = auth_response.text.split("Auth=")[1].strip()

headers = {"Authorization": f"GoogleLogin auth={auth_token}"}
response = requests.get(
    "https://freshrss.example.net/api/greader.php/reader/api/0/subscription/list?output=json",
    headers=headers
)
print(response.json())
```

## Rate Limiting and Best Practices

### Rate Limiting

- FreshRSS may implement rate limits depending on configuration
- Recommended: 1 request per second for heavy operations
- Cache responses locally to minimize API calls

### Best Practices

1. **Sync Strategy:**

   - Use incremental sync with timestamps
   - Don't fetch all data on every sync
   - Implement exponential backoff for retries

2. **API Key Management:**

   - Never hardcode API keys in applications
   - Use encrypted storage for sensitive data
   - Regenerate keys if compromised

3. **Error Handling:**

   - Implement retry logic
   - Handle authentication failures gracefully
   - Log API errors for debugging

4. **Performance:**

   - Batch operations when possible
   - Use appropriate page sizes
   - Cache metadata locally

## Troubleshooting

### Authentication Fails

**Google Reader API:**

- Verify Email and Passwd parameters
- Check API password is set in FreshRSS settings
- Ensure API access is enabled

**Fever API:**

- Verify MD5 hash calculation: `echo -n "user:pass" | md5sum`
- Check API key is correctly passed
- Ensure API access is enabled

### No Items Returned

- Verify you have subscriptions in FreshRSS
- Check feed update status in web interface
- Try fetching specific feed instead of reading-list
- Check logs for feed update errors

### Slow Response

- Reduce number of items requested with `n` parameter
- Use pagination with continuation tokens
- Cache results locally
- Implement incremental sync

## Resources

- [FreshRSS GitHub Repository](https://github.com/FreshRSS/FreshRSS)
- [FreshRSS Documentation](https://github.com/FreshRSS/FreshRSS/tree/edge/docs/en)
- [Compatible Clients](https://github.com/FreshRSS/FreshRSS#apis--native-apps)
- [Google Reader API (Archived)](https://web.archive.org/web/20130710044440/http://undoc.in/api.html)
- [Fever API](https://feedafever.com/api)
