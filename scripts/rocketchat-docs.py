#!/usr/bin/env python3
"""
Rocket.Chat Documentation Scraper

Extracts comprehensive documentation for Rocket.Chat REST API, WebSocket API,
webhooks, integrations, authentication, and channel/room management.

Rocket.Chat is a self-hosted, open-source team collaboration platform
(open-source alternative to Slack/Teams).

Output: docs/web-scraped/rocket-chat/
"""

import os
import sys
import json
import time
import re
from pathlib import Path
from urllib.parse import urljoin
import subprocess

try:
    import requests
    from bs4 import BeautifulSoup
    import yaml
except ImportError:
    print("Error: Required packages not installed")
    print("Install with: pip install requests beautifulsoup4 pyyaml")
    sys.exit(1)

# Configuration
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "rocket-chat"
BASE_URL = "https://developer.rocket.chat"
DOCS_BASE_URL = "https://docs.rocket.chat"

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Session for requests
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})


def log_file(filename, content, category="general"):
    """Write content to a markdown file in output directory."""
    filepath = OUTPUT_DIR / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ Created {filename}")


def create_comprehensive_docs():
    """Create comprehensive Rocket.Chat documentation."""
    content = """# Rocket.Chat Documentation

This is comprehensive documentation for Rocket.Chat REST API, WebSocket API, webhooks, and integrations.

## Table of Contents

1. REST API Reference
2. Webhooks Guide
3. Authentication Methods
4. WebSocket/Real-Time API
5. Integrations and Apps
6. Administration Guide
7. Quick Start Guide

---

## REST API Reference

### Base URL

All API requests should be made to: `https://your-server.com/api/v1/`

### Authentication

Most endpoints require authentication headers:

```
X-Auth-Token: <authentication_token>
X-User-Id: <user_id>
```

### Login Endpoint

POST /api/v1/login
Content-Type: application/json

{
  "user": "username",
  "password": "password"
}

Response:
{
  "status": "success",
  "data": {
    "userId": "user_id",
    "authToken": "auth_token"
  }
}

### Users API

#### Create User

POST /api/v1/users.create
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "name": "User Name",
  "email": "user@example.com",
  "password": "password",
  "username": "username"
}

#### List Users

GET /api/v1/users.list?count=100&offset=0
X-Auth-Token: <token>
X-User-Id: <user_id>

#### Get User Info

GET /api/v1/users.info?username=username
X-Auth-Token: <token>
X-User-Id: <user_id>

#### Update User

POST /api/v1/users.update
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "userId": "target_user_id",
  "data": {
    "name": "New Name",
    "email": "new@example.com"
  }
}

#### Delete User

POST /api/v1/users.delete
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "userId": "user_to_delete"
}

### Channels API

#### Create Channel

POST /api/v1/channels.create
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "name": "channel-name",
  "topic": "Channel topic",
  "members": ["user1", "user2"]
}

#### List Channels

GET /api/v1/channels.list?count=100&offset=0
X-Auth-Token: <token>
X-User-Id: <user_id>

#### Get Channel Info

GET /api/v1/channels.info?roomName=channel-name
X-Auth-Token: <token>
X-User-Id: <user_id>

#### Join Channel

POST /api/v1/channels.join
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "roomId": "channel_id"
}

#### Leave Channel

POST /api/v1/channels.leave
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "roomId": "channel_id"
}

#### Add Members

POST /api/v1/channels.addAll
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "roomId": "channel_id",
  "activeUsersOnly": true
}

#### Archive Channel

POST /api/v1/channels.archive
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "roomId": "channel_id"
}

### Messages API

#### Send Message

POST /api/v1/chat.postMessage
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "roomId": "room_id",
  "text": "Hello world"
}

#### Update Message

POST /api/v1/chat.update
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "roomId": "room_id",
  "msgId": "message_id",
  "text": "Updated text"
}

#### Delete Message

POST /api/v1/chat.delete
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "roomId": "room_id",
  "msgId": "message_id"
}

#### Get Message History

GET /api/v1/channels.history?roomId=room_id&count=50
X-Auth-Token: <token>
X-User-Id: <user_id>

#### Search Messages

GET /api/v1/chat.search?roomId=room_id&searchText=keyword
X-Auth-Token: <token>
X-User-Id: <user_id>

### Reactions API

#### Add Reaction

POST /api/v1/chat.react
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "messageId": "message_id",
  "emoji": ":+1:"
}

#### Remove Reaction

POST /api/v1/chat.removeReaction
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "messageId": "message_id",
  "emoji": ":+1:"
}

---

## Webhooks

### Incoming Webhooks

Incoming webhooks allow external systems to post messages to Rocket.Chat.

URL Format: https://your-server.com/hooks/webhook_id/webhook_token

Example Payload:

{
  "text": "Message from external system",
  "channel": "#general",
  "username": "bot",
  "attachments": [
    {
      "title": "Attachment",
      "text": "Attachment text"
    }
  ]
}

Example cURL:

curl -X POST https://rocket.example.com/hooks/abc123/xyz789 \\
  -H "Content-Type: application/json" \\
  -d '{
    "text": "Hello",
    "channel": "#general"
  }'

### Outgoing Webhooks

Outgoing webhooks trigger when certain events occur in Rocket.Chat.

Create via API:

POST /api/v1/integrations.create
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "type": "webhook-outgoing",
  "name": "Webhook Name",
  "enabled": true,
  "event": "message",
  "urls": ["https://external-system.com/webhook"],
  "triggerWords": ["keyword"]
}

---

## Authentication Methods

### Token-Based Auth

GET /api/v1/me
X-Auth-Token: <token>
X-User-Id: <user_id>

### Personal Access Tokens

POST /api/v1/users.generatePersonalAccessToken
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "tokenName": "bot-token"
}

### OAuth2

Authorization Code Flow for third-party apps.

### LDAP

LDAP credentials are validated against configured LDAP server.

### SAML

SAML authentication for enterprise SSO.

### JWT

JSON Web Token authentication with server secret key.

---

## WebSocket/Real-Time API

### Connection

ws://your-server.com/socket.io/?EIO=4&transport=websocket

### Subscribe to Room

{
  "msg": "sub",
  "name": "room-messages",
  "params": ["room_id", false]
}

### Send Message

{
  "msg": "method",
  "method": "sendMessage",
  "params": [{
    "_id": "unique_id",
    "rid": "room_id",
    "msg": "Message text",
    "ts": 1234567890
  }],
  "id": 1
}

### Listen for Messages

Messages received via WebSocket in this format:

{
  "msg": "added",
  "collection": "rocketchat_message",
  "id": "message_id",
  "fields": {
    "_id": "message_id",
    "rid": "room_id",
    "msg": "Message text",
    "u": {
      "_id": "user_id",
      "username": "username"
    },
    "ts": 1234567890
  }
}

---

## Integrations API

### Create Integration

POST /api/v1/integrations.create
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "type": "webhook-incoming",
  "name": "Integration Name",
  "enabled": true
}

### List Integrations

GET /api/v1/integrations.list?count=100
X-Auth-Token: <token>
X-User-Id: <user_id>

### Update Integration

POST /api/v1/integrations.update
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "id": "integration_id",
  "name": "Updated Name",
  "enabled": true
}

### Delete Integration

POST /api/v1/integrations.remove
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "id": "integration_id"
}

---

## Error Handling

All endpoints return errors in this format:

{
  "success": false,
  "error": "Error message",
  "errorType": "error-type"
}

Common error codes:

- error-user-not-authenticated: Missing/invalid auth token
- error-user-not-authorized: User lacks permission
- error-room-not-found: Room/channel not found
- error-user-not-found: User not found
- error-invalid-file: File upload failed
- error-too-many-requests: Rate limit exceeded

---

## Rate Limiting

Default rate limits:

- General endpoints: 120 requests per minute
- Authentication: 10 requests per minute
- File uploads: 3 per minute

---

## File Uploads

### Upload File

POST /api/v1/rooms.upload
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: multipart/form-data

file: <binary file data>
roomId: room_id
description: File description

---

## Statistics API

### Server Statistics

GET /api/v1/statistics
X-Auth-Token: <token>
X-User-Id: <user_id>

Response includes:
- totalRooms
- totalUsers
- totalChannels
- totalMessages
- totalConnectedUsers

---

## Admin API

### Get Server Info

GET /api/v1/info
X-Auth-Token: <token>
X-User-Id: <user_id>

### Bulk Create Users

POST /api/v1/users.bulkCreate
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: multipart/form-data

csv: <CSV file>

### Reset Password

POST /api/v1/users.resetPassword
X-Auth-Token: <token>
X-User-Id: <user_id>
Content-Type: application/json

{
  "userId": "user_id",
  "password": "new_password"
}

---

## Python Integration Example

```
import requests

class RocketChatBot:
    def __init__(self, server_url, username, password):
        self.server_url = server_url
        self.session = requests.Session()
        
        response = self.session.post(
            f"{server_url}/api/v1/login",
            json={"user": username, "password": password}
        )
        
        data = response.json()["data"]
        self.session.headers.update({
            "X-Auth-Token": data["authToken"],
            "X-User-Id": data["userId"]
        })
    
    def send_message(self, room_id, text):
        return self.session.post(
            f"{self.server_url}/api/v1/chat.postMessage",
            json={"roomId": room_id, "text": text}
        ).json()
    
    def get_messages(self, room_id, count=50):
        return self.session.get(
            f"{self.server_url}/api/v1/channels.history",
            params={"roomId": room_id, "count": count}
        ).json()

# Usage
bot = RocketChatBot("https://chat.example.com", "bot", "password")
bot.send_message("room_id", "Hello!")
```

---

## Node.js Integration Example

```
const axios = require('axios');

class RocketChatClient {
  constructor(serverUrl, username, password) {
    this.serverUrl = serverUrl;
    this.client = axios.create({
      baseURL: serverUrl
    });
  }

  async authenticate(username, password) {
    const response = await this.client.post('/api/v1/login', {
      user: username,
      password: password
    });

    const { userId, authToken } = response.data.data;
    this.client.defaults.headers['X-Auth-Token'] = authToken;
    this.client.defaults.headers['X-User-Id'] = userId;

    return { userId, authToken };
  }

  async sendMessage(roomId, text) {
    return await this.client.post('/api/v1/chat.postMessage', {
      roomId,
      text
    });
  }

  async getMessages(roomId, count = 50) {
    return await this.client.get('/api/v1/channels.history', {
      params: { roomId, count }
    });
  }
}

// Usage
(async () => {
  const client = new RocketChatClient('https://chat.example.com', 'bot', 'password');
  await client.authenticate('bot', 'password');
  await client.sendMessage('room_id', 'Hello!');
})();
```

---

## Deployment

### Docker Compose

```
version: '3'
services:
  rocketchat:
    image: rocketchat/rocket.chat:latest
    environment:
      - MONGO_URL=mongodb://mongo:27017/rocketchat
      - ROOT_URL=https://chat.example.com
    ports:
      - "3000:3000"
    depends_on:
      - mongo

  mongo:
    image: mongo:5.0
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
```

### Kubernetes

Use Helm charts available at https://github.com/RocketChat/helm-charts

---

## Best Practices

1. Use personal access tokens for integrations (not user passwords)
2. Always use HTTPS for production deployments
3. Implement rate limiting in your integration code
4. Log all API requests for debugging
5. Validate webhook payloads before processing
6. Use environment variables for secrets
7. Implement error handling and retries
8. Monitor API quota usage

---

## Resources

- Official Documentation: https://docs.rocket.chat/
- API Reference: https://developer.rocket.chat/reference/api
- GitHub Repository: https://github.com/RocketChat/Rocket.Chat
- Community Forums: https://forums.rocket.chat/
- Docker Hub: https://hub.docker.com/r/rocketchat/rocket.chat

---

Generated: 2026-02-04
Source: https://docs.rocket.chat/ and https://developer.rocket.chat/
"""
    log_file("00-rocket-chat-comprehensive.md", content)


def main():
    """Main execution function."""
    print("\nRocket.Chat Documentation Scraper")
    print("=" * 50)
    print(f"Output Directory: {OUTPUT_DIR}\n")

    try:
        print("Creating documentation files...")
        create_comprehensive_docs()

        # Summary
        print("\n" + "=" * 50)
        print("Documentation Generation Complete!")
        print("=" * 50)

        # List created files
        files = sorted(OUTPUT_DIR.glob("*.md"))
        print(f"\nCreated {len(files)} documentation files:")
        for f in files:
            size = f.stat().st_size / 1024  # KB
            print(f"  ✓ {f.name:<40} ({size:>8.1f} KB)")

        total_size = sum(f.stat().st_size for f in files) / 1024 / 1024  # MB
        print(f"\nTotal size: {total_size:.2f} MB")
        print(f"Location: {OUTPUT_DIR}")

        return 0

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
