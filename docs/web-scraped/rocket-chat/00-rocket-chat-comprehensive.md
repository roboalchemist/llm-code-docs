# Rocket.Chat Documentation

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

curl -X POST https://rocket.example.com/hooks/abc123/xyz789 \
  -H "Content-Type: application/json" \
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
