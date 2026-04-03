# Gazelle API Documentation

**Orpheus Development Papers #7 - JSON API**
Version 1 | Author: unknown | Date: unknown

## Overview

This is the API documentation for a Gazelle-based private tracker site.
The API provides programmatic access to site features.

## Authentication

- Cookie-based login via `/login.php`
- API tokens via the `Authorization` header
- Rate limit: 5 requests per 10 seconds

## Request Format

All requests go through `ajax.php?action=<ACTION>`. Responses are JSON with:

- `status` — success/failure indicator
- `response` — the actual data
- `info` — optional informational message

## Core Endpoints

### index

Returns user info, notifications, and stats.

### user

Fetch user details by ID.

### inbox

View inbox, sentbox, and conversations.

### browse

Search and browse torrents.

### torrentgroup

Get torrent group details.

### torrent

Get individual torrent details.

### upload

Upload torrents (requires authentication).

### requests

Browse request posts.

### request_fill

Fill a request.

### forum

View forum categories, forums, and threads.

### bookmarks

View bookmarked torrents.

### subscriptions

View subscribed content.

### collages

View and manage collages.

## Response Formats

Each endpoint returns structured JSON tailored to its function. See the
full documentation in the source repository for detailed response schemas.

## Unofficial Clients

This API is used by unofficial clients in Python, Java, Ruby, JavaScript,
C#, PHP, Go, and Scala.
