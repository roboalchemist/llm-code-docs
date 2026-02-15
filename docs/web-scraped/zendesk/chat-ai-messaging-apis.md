# Zendesk Chat, AI Agents & Messaging APIs - Complete Reference

Source: https://developer.zendesk.com/api-reference/

Comprehensive coverage of Zendesk's chat, messaging, and AI agent APIs for building conversational experiences.

## Chat API

The Chat API enables live chat functionality and agent interactions.

### Overview

Provides:

- Real-time messaging between customers and agents
- Chat history and transcripts
- Agent availability management
- Visitor information and tracking
- Proactive engagement capabilities

### Authentication

```bash
curl -H "Authorization: Bearer YOUR_API_TOKEN" \
  https://yoursubdomain.zendesk.com/api/v2/channels/chat/...
```

### Key Endpoints

#### Chat Conversations

```bash
GET /chat/conversations                    # List conversations
POST /chat/conversations                   # Create conversation
GET /chat/conversations/{id}              # Get conversation
PUT /chat/conversations/{id}              # Update conversation
DELETE /chat/conversations/{id}           # Close conversation

GET /chat/conversations/{id}/messages     # Get messages
POST /chat/conversations/{id}/messages    # Send message
```

#### Agents

```bash
GET /chat/agents                          # List agents
GET /chat/agents/{id}                     # Get agent profile
PUT /chat/agents/{id}                     # Update agent status

GET /chat/agents/{id}/availability        # Get availability
POST /chat/agents/{id}/availability       # Update availability
```

#### Visitor Tracking

```bash
GET /chat/visitors                        # List active visitors
GET /chat/visitors/{id}                   # Get visitor info
POST /chat/visitors/{id}/track           # Track visitor activity

GET /chat/visitors/{id}/conversations     # Get visitor chats
```

#### Chat Accounts

```bash
GET /chat/accounts                        # Account information
POST /chat/accounts/proactive            # Proactive engagement
```

### Common Chat Operations

**Start Chat Session:**

```bash
POST /chat/conversations
{
  "conversation": {
    "visitor": {
      "name": "John Doe",
      "email": "john@example.com"
    },
    "department_id": 123
  }
}
```

**Send Message:**

```bash
POST /chat/conversations/abc123/messages
{
  "message": {
    "body": "How can I help you today?",
    "author": {
      "type": "agent",
      "id": "agent-456"
    }
  }
}
```

**Monitor Agent Status:**

```bash
GET /chat/agents/789/availability
{
  "availability": {
    "status": "online|offline|away",
    "max_chats": 10,
    "current_chats": 3
  }
}
```

## Real-Time Chat API

WebSocket-based real-time chat messaging.

### Features

- Bi-directional messaging
- Real-time presence
- Typing indicators
- Message read receipts
- Connection lifecycle management

### WebSocket Connection

```javascript
const ws = new WebSocket('wss://yoursubdomain.zendesk.com/api/v2/chat/stream');

ws.addEventListener('open', () => {
  ws.send(JSON.stringify({
    action: 'connect',
    token: 'YOUR_API_TOKEN'
  }));
});

ws.addEventListener('message', (event) => {
  const data = JSON.parse(event.data);
  console.log('Message:', data);
});
```

### Message Types

```json
{
  "type": "message",
  "conversation_id": "abc123",
  "author": "agent|visitor",
  "content": "Message text",
  "timestamp": "2024-02-14T10:30:00Z"
}

{
  "type": "typing_indicator",
  "conversation_id": "abc123",
  "author": "agent|visitor"
}

{
  "type": "presence",
  "user_id": "123",
  "status": "online|offline|away"
}

{
  "type": "read_receipt",
  "conversation_id": "abc123",
  "message_id": "msg-456"
}
```

## Chat Conversations API

Manage agent interactions with chat conversations.

```bash
GET /chat/conversations/{id}/agents      # Get agents in chat
POST /chat/conversations/{id}/transfer   # Transfer chat
POST /chat/conversations/{id}/invite     # Invite agent

GET /chat/conversations/{id}/tags        # Get tags
POST /chat/conversations/{id}/tags       # Add tags
DELETE /chat/conversations/{id}/tags/{tag}  # Remove tag
```

## AI Agents API

Zendesk AI Agents enable conversational AI and automation.

### AI Agents Overview

Features:

- Natural language understanding
- Automated response generation
- Multi-turn conversations
- Integration with ticketing
- Handoff to human agents
- Conversation analytics

### Agent Configuration

```bash
GET /ai_agents                            # List AI agents
POST /ai_agents                           # Create agent
GET /ai_agents/{id}                      # Get configuration
PUT /ai_agents/{id}                      # Update configuration
DELETE /ai_agents/{id}                   # Delete agent

GET /ai_agents/{id}/knowledge_base       # Get knowledge sources
POST /ai_agents/{id}/knowledge_base      # Add knowledge source
```

### Agent Properties

```json
{
  "ai_agent": {
    "id": "agent-123",
    "name": "Support Bot",
    "description": "Handles common support issues",
    "enabled": true,
    "model": "gpt-4|gpt-3.5",
    "temperature": 0.7,
    "max_tokens": 500,
    "system_prompt": "You are a helpful support agent...",
    "knowledge_sources": [
      {
        "type": "help_center",
        "id": "kb-articles"
      }
    ],
    "handoff_triggers": [
      "complex_issue",
      "payment_required",
      "user_requested"
    ]
  }
}
```

### Running Conversations

```bash
POST /ai_agents/{id}/conversations       # Start conversation
GET /ai_agents/{id}/conversations/{conv_id}  # Get conversation
POST /ai_agents/{id}/conversations/{conv_id}/messages  # Send message

GET /ai_agents/{id}/conversations/{conv_id}/messages  # Get messages
```

### Message Exchange

**User Message:**

```json
{
  "role": "user",
  "content": "How do I reset my password?"
}
```

**Agent Response:**

```json
{
  "role": "assistant",
  "content": "To reset your password, follow these steps...",
  "confidence": 0.95,
  "sources": ["help_article_123"]
}
```

### Knowledge Sources

Link AI agents to knowledge:

```bash
# Help Center integration
POST /ai_agents/123/knowledge_base
{
  "knowledge_source": {
    "type": "help_center",
    "include_sections": ["Getting Started", "Billing"],
    "exclude_articles": ["archived_1", "archived_2"]
  }
}

# Custom documents
POST /ai_agents/123/knowledge_base
{
  "knowledge_source": {
    "type": "document",
    "documents": [
      {
        "title": "Product Manual",
        "content": "...",
        "metadata": {"version": "2.0"}
      }
    ]
  }
}

# Web URLs
POST /ai_agents/123/knowledge_base
{
  "knowledge_source": {
    "type": "web",
    "urls": [
      "https://example.com/docs",
      "https://blog.example.com"
    ]
  }
}
```

### Handoff to Humans

Configure automatic escalation:

```bash
PUT /ai_agents/123
{
  "ai_agent": {
    "handoff_triggers": [
      {
        "type": "user_request",
        "action": "create_ticket"
      },
      {
        "type": "confidence_threshold",
        "threshold": 0.5,
        "action": "escalate"
      },
      {
        "type": "max_turns",
        "max_turns": 10,
        "action": "escalate"
      }
    ]
  }
}
```

### Analytics

```bash
GET /ai_agents/{id}/analytics
{
  "period": "2024-02-01/2024-02-14",
  "metrics": {
    "conversations": 1000,
    "avg_response_time": 2.3,
    "resolution_rate": 72.5,
    "handoff_rate": 27.5,
    "user_satisfaction": 4.2,
    "top_topics": ["password_reset", "billing", "features"]
  }
}
```

## Conversations API (Messaging)

Unified messaging API for multi-channel conversations.

### Messaging Overview

Combines messaging across:

- Web chat
- Mobile messaging
- Social media
- Email
- SMS

### Conversations

```bash
GET /conversations                        # List conversations
POST /conversations                       # Create conversation
GET /conversations/{id}                  # Get conversation
PUT /conversations/{id}                  # Update conversation
DELETE /conversations/{id}               # Delete conversation

GET /conversations/{id}/messages         # Get messages
POST /conversations/{id}/messages        # Send message
```

### Participants

```bash
GET /conversations/{id}/participants     # Get participants
POST /conversations/{id}/participants    # Add participant
DELETE /conversations/{id}/participants/{id}  # Remove participant
```

### Channels

```bash
GET /conversations/{id}/channels         # Get active channels
POST /conversations/{id}/channels        # Add channel
DELETE /conversations/{id}/channels/{channel_id}  # Remove channel
```

### Sample Conversation

```json
{
  "conversation": {
    "id": "conv-123",
    "subject": "Order Status Inquiry",
    "participants": [
      {"id": "cust-456", "type": "customer", "name": "John Doe"},
      {"id": "agent-789", "type": "agent", "name": "Sarah Agent"}
    ],
    "channels": ["web_chat", "sms"],
    "status": "open",
    "created_at": "2024-02-14T10:00:00Z"
  }
}
```

## Answer Bot API

Provides Help Center article suggestions.

### Answer Bot Overview

- Analyze customer inquiries
- Recommend relevant Help Center articles
- Track suggestion effectiveness
- Integration with chat/widgets

### Endpoints

```bash
POST /answer_bot/suggest                 # Get article suggestions
GET /answer_bot/feedback                 # Get feedback on suggestions
POST /answer_bot/feedback                # Submit feedback
```

### Getting Suggestions

```bash
POST /answer_bot/suggest
{
  "inquiry": "How do I reset my password?",
  "limit": 5,
  "confidence_threshold": 0.7
}

Response:
{
  "suggestions": [
    {
      "article_id": "123",
      "title": "Password Reset Guide",
      "excerpt": "To reset your password...",
      "url": "https://help.example.com/articles/123",
      "confidence": 0.95
    }
  ]
}
```

## Common Integration Patterns

### Chat to Ticket Escalation

```bash
# 1. Chat conversation occurs
POST /chat/conversations/abc/messages

# 2. Customer requests to escalate
# System detects escalation request

# 3. Create ticket from chat
POST /tickets
{
  "ticket": {
    "subject": "Chat escalation - Order issue",
    "description": "Chat transcript...",
    "chat_id": "abc",
    "requester_email": "customer@example.com"
  }
}

# 4. Close chat, link to ticket
PUT /chat/conversations/abc
{
  "linked_ticket_id": "ticket-456"
}
```

### AI Agent with Human Handoff

```bash
# 1. Customer starts conversation with AI
POST /ai_agents/123/conversations
{
  "initial_message": "I can't log in"
}

# 2. AI attempts resolution
# System evaluates confidence/complexity

# 3. If handoff needed, create ticket
POST /tickets
{
  "subject": "AI Agent Escalation",
  "conversation_id": "conv-456",
  "priority": "high"
}

# 4. Notify human agent
# Agent takes over conversation
```

### Multi-Channel Routing

```bash
# Message comes via SMS, chat, or email
# System unifies in single conversation

POST /conversations
{
  "conversation": {
    "channels": ["sms", "web"],
    "participant_phone": "+1-555-1234",
    "participant_email": "customer@example.com"
  }
}
```

## Best Practices

### Chat Performance

- Monitor response times
- Queue capacity management
- Agent workload balancing
- Proactive engagement timing

### AI Agent Quality

- Regular knowledge base updates
- Monitor handoff rates
- Analyze customer satisfaction
- Fine-tune system prompts
- Test with realistic queries

### Conversation Management

- Archive old conversations
- Implement search indexing
- Track conversation metrics
- Maintain transcript compliance

### Integration Security

- Validate webhook signatures
- Encrypt sensitive data
- Rate limit API calls
- Audit access logs

## Limits & Quotas

- **Chat**: 10K concurrent conversations
- **Messages**: 1000 per minute per account
- **AI Agents**: Up to 10 per account
- **API Rate**: 600 requests per minute
- **Message Size**: 4KB per message

## Error Codes

- `400 Bad Request` - Invalid parameters
- `401 Unauthorized` - Invalid credentials
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `429 Too Many Requests` - Rate limited
- `503 Service Unavailable` - Temporary outage

## Resources

- [Chat API Documentation](https://developer.zendesk.com/api-reference/live-chat-api/)
- [Real-Time Chat API](https://developer.zendesk.com/api-reference/real-time-chat-api/)
- [AI Agents API](https://developer.zendesk.com/api-reference/ai-agents/)
- [Conversations API](https://developer.zendesk.com/api-reference/conversations/)
- [Answer Bot API](https://developer.zendesk.com/api-reference/answer-bot/)
