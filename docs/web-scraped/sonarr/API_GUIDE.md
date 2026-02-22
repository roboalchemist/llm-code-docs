# Sonarr API Guide

## Overview

Sonarr provides a comprehensive REST API for programmatic access to its functionality. The API allows you to:

- Query and manage your media library
- Automate episode downloading and management
- Integrate with other applications
- Build custom tools and workflows

## Authentication

Most API endpoints require an API key for authentication. You can find your API key in:
- **Settings > General > API Key**

Include the API key in all requests:
- **Header method:** `X-Api-Key: {api-key}`
- **Query parameter method:** `?apikey={api-key}`

## Base URL

```
http://localhost:8989/api/v3
```

Replace `localhost` with your Sonarr host and `8989` with your configured port.

## Common Endpoints

### Series Management
- `GET /series` - List all series
- `GET /series/{id}` - Get series details
- `POST /series` - Add a new series
- `PUT /series/{id}` - Update series
- `DELETE /series/{id}` - Delete series

### Episodes
- `GET /episode` - List episodes
- `GET /episode/{id}` - Get episode details
- `GET /episode/monitor` - Monitor status

### Release Search
- `GET /release` - Search for releases
- `GET /release/{id}` - Get release details

### Queue
- `GET /queue` - Get download queue
- `DELETE /queue/{id}` - Remove from queue

### System
- `GET /system/status` - System status
- `GET /health` - Health check
- `GET /system/logs` - Application logs

## Rate Limiting

No built-in rate limiting is enforced, but it's good practice to implement reasonable delays between requests.

## Response Format

All responses are returned as JSON. Success responses typically return HTTP 200, 201, or 204.

Error responses return appropriate HTTP status codes (400, 401, 403, 404, 500, etc.) with error details in the response body.

## Example Request

```bash
curl -X GET "http://localhost:8989/api/v3/series" \
  -H "X-Api-Key: YOUR_API_KEY" \
  -H "Accept: application/json"
```

## Documentation

For complete endpoint documentation, visit:
- [Sonarr API Docs](https://sonarr.tv/docs/api)
- [Wiki Documentation](https://wiki.servarr.com/Sonarr)
