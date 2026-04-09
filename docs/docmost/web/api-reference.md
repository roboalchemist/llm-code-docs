# Docmost API Reference

## Overview

The Docmost API provides programmatic access to documents, spaces, users, and more. All endpoints require authentication via JWT token.

## Authentication

Include JWT token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## Base URL

```
https://your-docmost-instance.com/api
```

## Response Format

All responses are JSON:

```json
{
  "data": {},
  "error": null,
  "success": true
}
```

## Core Endpoints

### Documents

#### List Documents in Space

```
GET /spaces/:spaceId/documents
```

Query parameters:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20)

#### Get Document

```
GET /documents/:documentId
```

#### Create Document

```
POST /documents
```

Body:
```json
{
  "title": "My Document",
  "spaceId": "space_id",
  "content": "Document content"
}
```

#### Update Document

```
PUT /documents/:documentId
```

Body:
```json
{
  "title": "Updated Title",
  "content": "Updated content"
}
```

#### Delete Document

```
DELETE /documents/:documentId
```

### Spaces

#### List All Spaces

```
GET /spaces
```

#### Get Space

```
GET /spaces/:spaceId
```

#### Create Space

```
POST /spaces
```

Body:
```json
{
  "name": "Engineering",
  "description": "Engineering documentation"
}
```

#### Update Space

```
PUT /spaces/:spaceId
```

#### Delete Space

```
DELETE /spaces/:spaceId
```

### Users and Permissions

#### Get Current User

```
GET /users/me
```

#### List Space Members

```
GET /spaces/:spaceId/members
```

#### Invite User to Space

```
POST /spaces/:spaceId/members/invite
```

Body:
```json
{
  "email": "user@example.com",
  "role": "editor"
}
```

Roles: owner, editor, commenter, viewer

#### Update Member Role

```
PUT /spaces/:spaceId/members/:userId
```

Body:
```json
{
  "role": "editor"
}
```

#### Remove Member

```
DELETE /spaces/:spaceId/members/:userId
```

### Comments

#### Get Document Comments

```
GET /documents/:documentId/comments
```

#### Create Comment

```
POST /documents/:documentId/comments
```

Body:
```json
{
  "content": "This needs clarification",
  "range": {
    "start": 0,
    "end": 50
  }
}
```

#### Delete Comment

```
DELETE /comments/:commentId
```

### Search

#### Full-Text Search

```
GET /search
```

Query parameters:
- `q`: Search query (required)
- `spaceId`: Filter by space (optional)

Response:
```json
{
  "results": [
    {
      "id": "doc_123",
      "title": "Document Title",
      "excerpt": "...matching excerpt...",
      "spaceId": "space_123"
    }
  ]
}
```

## Rate Limiting

API requests are rate limited:
- 100 requests per minute for authenticated users
- 10 requests per minute for anonymous access

## Error Handling

Errors include appropriate HTTP status codes:

```json
{
  "error": "Document not found",
  "message": "The requested document does not exist",
  "status": 404
}
```

Common status codes:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 429: Too Many Requests
- 500: Internal Server Error

## Webhooks

Docmost supports webhooks for real-time event notifications.

### Event Types

- `document.created`
- `document.updated`
- `document.deleted`
- `comment.created`
- `comment.deleted`
- `space.created`
- `space.updated`
- `user.invited`

### Registering Webhooks

```
POST /webhooks
```

Body:
```json
{
  "url": "https://your-service.com/webhook",
  "events": ["document.updated", "comment.created"]
}
```

## Examples

### Create a Document

```bash
curl -X POST https://your-instance.com/api/documents \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "API Example",
    "spaceId": "space_123",
    "content": "This is created via API"
  }'
```

### Search Documents

```bash
curl "https://your-instance.com/api/search?q=getting+started" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### List Space Members

```bash
curl https://your-instance.com/api/spaces/space_123/members \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## SDK and Client Libraries

Docmost provides official TypeScript/JavaScript SDK:

```typescript
import { DocmostClient } from '@docmost/sdk';

const client = new DocmostClient({
  baseUrl: 'https://your-instance.com',
  token: 'your_jwt_token'
});

// Get document
const doc = await client.documents.get('doc_123');

// List spaces
const spaces = await client.spaces.list();

// Search
const results = await client.search({ q: 'query' });
```
