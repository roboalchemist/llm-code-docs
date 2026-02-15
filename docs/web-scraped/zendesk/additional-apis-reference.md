# Source: https://developer.zendesk.com/api-reference/

# Zendesk Additional APIs - Complete Reference

Comprehensive coverage of supplementary Zendesk APIs for integration services, admin functions, webhooks, and more.

## Help Center API

### Overview

Manage Help Center knowledge base articles, sections, and categories programmatically.

### Core Resources

```bash
# Articles
GET /help_center/articles                    # List articles
POST /help_center/articles                   # Create article
GET /help_center/articles/{id}              # Get article
PUT /help_center/articles/{id}              # Update article
DELETE /help_center/articles/{id}           # Delete article

# Sections (Collections)
GET /help_center/sections                    # List sections
POST /help_center/sections                   # Create section
GET /help_center/sections/{id}              # Get section
PUT /help_center/sections/{id}              # Update section

# Categories
GET /help_center/categories                  # List categories
POST /help_center/categories                 # Create category
GET /help_center/categories/{id}            # Get category
PUT /help_center/categories/{id}            # Update category

# Translations
GET /help_center/articles/{id}/translations # Get translations
POST /help_center/articles/{id}/translations # Add translation
PUT /help_center/articles/{id}/translations/{lang}  # Update translation
```

### Article Properties

```json
{
  "article": {
    "id": 123,
    "title": "How to Reset Your Password",
    "body": "To reset your password, follow these steps...",
    "source_locale": "en-us",
    "draft": false,
    "promoted": true,
    "position": 1,
    "section_id": 456,
    "created_at": "2024-02-14T10:00:00Z",
    "updated_at": "2024-02-14T10:30:00Z"
  }
}
```

## Integration Services (ZIS) APIs

Zendesk Integration Services provides event-driven integration capabilities.

### Overview

- **ZIS Configs API** - Manage integration configurations
- **Connections API** - Setup external service connections
- **ZIS Inbound Webhooks API** - Receive external webhooks
- **ZIS Links API** - Create named links between objects
- **ZIS Registry API** - Manage custom registry data
- **Trigger Events Reference** - Available trigger events

### ZIS Configs

```bash
GET /zis/configs                            # List configurations
POST /zis/configs                           # Create configuration
GET /zis/configs/{id}                      # Get configuration
PUT /zis/configs/{id}                      # Update configuration
DELETE /zis/configs/{id}                   # Delete configuration

GET /zis/configs/{id}/test                 # Test configuration
POST /zis/configs/{id}/activate            # Activate configuration
POST /zis/configs/{id}/deactivate          # Deactivate configuration
```

### Connections API

```bash
GET /zis/connections                        # List connections
POST /zis/connections                       # Create connection
GET /zis/connections/{id}                  # Get connection
PUT /zis/connections/{id}                  # Update connection
DELETE /zis/connections/{id}               # Delete connection
```

**Connection Types:**
- HTTP/REST endpoints
- Database connections
- OAuth applications
- API credentials

### Webhooks

```bash
GET /zis/webhooks                           # List webhooks
POST /zis/webhooks                          # Create webhook
GET /zis/webhooks/{id}                     # Get webhook
PUT /zis/webhooks/{id}                     # Update webhook
DELETE /zis/webhooks/{id}                  # Delete webhook
```

### ZIS Links

Link custom data to Zendesk objects:

```bash
GET /zis/links                              # List links
POST /zis/links                             # Create link
DELETE /zis/links/{id}                     # Delete link
```

## Status API

Get system status and maintenance information.

```bash
GET /status                                 # Get overall status
GET /status/incidents                       # List incidents
GET /status/incidents/{id}                 # Get incident details
GET /status/maintenance                    # List maintenance windows
```

**Status Values:**
- `operational` - All systems normal
- `degraded_performance` - Slower than normal
- `partial_outage` - Some services unavailable
- `major_outage` - Most services unavailable

## Search API

Advanced search across Zendesk resources.

### Overview

Unified search interface for:
- Tickets
- Users
- Organizations
- Articles
- Custom objects

### Search Query Syntax

```bash
GET /search?query=status:open priority:high

# Complex queries
GET /search?query=created:>2024-02-01 assignee_id:123

# Full-text search
GET /search?query=payment issue

# Boolean operators
GET /search?query=(status:open OR status:pending) AND priority:high
```

### Search Operators

| Operator | Example | Description |
|----------|---------|-------------|
| `:` | `status:open` | Field equals value |
| `>` | `created:>2024-01-01` | Greater than |
| `<` | `created:<2024-03-01` | Less than |
| `>=` | `value:>=100` | Greater or equal |
| `<=` | `value:<=500` | Less or equal |
| `AND` | `status:open AND priority:high` | Both conditions |
| `OR` | `status:open OR status:pending` | Either condition |
| `-` | `-status:closed` | Not condition |
| `*` | `title:password*` | Wildcard search |
| `"exact"` | `"exact phrase"` | Exact phrase match |

### Common Search Fields

**Tickets:**
- `status`, `priority`, `type`
- `assignee_id`, `requester_id`
- `organization_id`, `group_id`
- `created`, `updated`
- `tags`, `custom_field_id`

**Users:**
- `email`, `name`
- `organization_id`, `role`
- `created`, `updated`

**Articles:**
- `title`, `body`, `status`
- `section_id`, `category_id`
- `created`, `updated`

## Omnichannel/Routing APIs

Route customer interactions across channels.

```bash
GET /routing/attributes                    # List routing attributes
POST /routing/attributes                   # Create attribute
GET /routing/attributes/{id}              # Get attribute
PUT /routing/attributes/{id}              # Update attribute
DELETE /routing/attributes/{id}           # Delete attribute

GET /routing/skills                        # List routing skills
POST /routing/skills                       # Create skill
GET /routing/skills/{id}                  # Get skill
PUT /routing/skills/{id}                  # Update skill
```

## Explore API

Analytics and reporting API.

```bash
GET /explore/reports                       # List reports
POST /explore/reports                      # Create custom report
GET /explore/reports/{id}                 # Get report
PUT /explore/reports/{id}                 # Update report
DELETE /explore/reports/{id}              # Delete report

GET /explore/reports/{id}/data            # Get report data
```

### Report Types

- Ticket metrics (volume, resolution time)
- Agent performance (ratings, efficiency)
- Channel analytics (chat, email, phone)
- Customer satisfaction (CSAT, NPS)
- Custom object reporting

## Mobile SDK APIs

Support for mobile applications.

### Android SDK

```bash
GET /channels/mobile/android              # Configuration
POST /channels/mobile/android/push        # Push notifications
```

### iOS SDK

```bash
GET /channels/mobile/ios                  # Configuration
POST /channels/mobile/ios/push            # Push notifications
```

### Unity SDK

```bash
GET /channels/mobile/unity                # Configuration
```

## Admin APIs

Administrative functions and account management.

### Account Settings

```bash
GET /account                               # Get account info
GET /account/account_features              # List features
GET /account/audit_logs                    # Audit logs
GET /account/custom_roles                  # Custom roles
GET /account/brands                        # Brands
```

### Audit Logs

Track all administrative changes:

```bash
GET /audit_logs                            # List audit logs
GET /audit_logs?action=create              # Filter by action
GET /audit_logs?actor_id=123               # Filter by actor
```

### Brands

```bash
GET /brands                                # List brands
POST /brands                               # Create brand
GET /brands/{id}                          # Get brand
PUT /brands/{id}                          # Update brand
DELETE /brands/{id}                       # Delete brand
```

### Roles & Permissions

```bash
GET /roles                                 # List roles
POST /roles                                # Create custom role
GET /roles/{id}                           # Get role
PUT /roles/{id}                           # Update role
DELETE /roles/{id}                        # Delete role

GET /roles/{id}/permissions               # Get permissions
```

## Webhooks API

Zendesk can send webhooks to your systems on events.

### Webhook Management

```bash
GET /webhooks                              # List webhooks
POST /webhooks                             # Create webhook
GET /webhooks/{id}                        # Get webhook
PUT /webhooks/{id}                        # Update webhook
DELETE /webhooks/{id}                     # Delete webhook

POST /webhooks/{id}/test                  # Test webhook
```

### Webhook Configuration

```json
{
  "webhook": {
    "name": "Ticket Created",
    "description": "Notify external system of new tickets",
    "endpoint": "https://example.com/webhooks/tickets",
    "event_types": [
      "ticket.created",
      "ticket.updated"
    ],
    "filter": {
      "all": [
        {"field": "status", "value": "open"}
      ]
    },
    "headers": {
      "X-Custom-Header": "value"
    },
    "active": true
  }
}
```

### Webhook Events

**Ticket Events:**
- `ticket.created`
- `ticket.updated`
- `ticket.solved`
- `ticket.deleted`
- `ticket_comment.created`

**User Events:**
- `user.created`
- `user.updated`
- `user.deleted`

**Organization Events:**
- `organization.created`
- `organization.updated`

**Chat Events:**
- `chat_conversation.started`
- `chat_conversation.ended`
- `chat_message.created`

### Webhook Payload

```json
{
  "id": "webhook-event-123",
  "timestamp": "2024-02-14T10:30:00Z",
  "event_type": "ticket.created",
  "data": {
    "ticket": {
      "id": 456,
      "subject": "Help needed",
      "status": "new"
    }
  }
}
```

### Webhook Security

**Signature Verification:**

```bash
# Webhook headers include:
X-Zendesk-Webhook-ID: webhook-123
X-Zendesk-Webhook-Timestamp: 1707902400
X-Zendesk-Webhook-Signature: sha256=abc123...

# Verify signature
calculated_signature = sha256(webhook_body + timestamp + webhook_secret)
if calculated_signature == provided_signature:
  # Valid webhook
```

## Sunshine Profiles API

Build customer profiles from external data.

```bash
GET /profiles                              # List profiles
POST /profiles                             # Create profile
GET /profiles/{id}                        # Get profile
PUT /profiles/{id}                        # Update profile
DELETE /profiles/{id}                     # Delete profile

# Link to Zendesk objects
POST /profiles/{id}/links                 # Create link
GET /profiles/{id}/links                  # Get links
DELETE /profiles/{id}/links/{id}          # Delete link
```

## Events API

Track and query customer events and interactions.

```bash
GET /events                                # List events
POST /events                               # Create event
GET /events/{id}                          # Get event

# Query events
GET /events?filter[object_type]=ticket&filter[date][gte]=2024-02-01
```

## Common Integration Patterns

### Ticket Creation Flow

```
1. Customer action (email, chat, form)
2. Webhook event triggered
3. External system receives webhook
4. External system makes API call if needed
5. Ticket created/updated in Zendesk
6. Status reflected in external system
```

### Multi-System Sync

```
1. Zendesk ticket created
2. ZIS trigger fires
3. Webhook sent to external system
4. External system updates its records
5. Webhook response confirms receipt
6. Zendesk logs integration result
```

### Custom Reporting

```
1. Query Search API for relevant records
2. Use Explore API for metrics
3. Process data in business intelligence tool
4. Generate reports and dashboards
5. Schedule recurring queries
```

## Best Practices

### API Usage
- Use webhooks for async events (not polling)
- Implement exponential backoff for retries
- Cache Search results when possible
- Batch operations to reduce API calls

### Security
- Verify webhook signatures
- Use OAuth for third-party apps
- Rotate API tokens regularly
- Encrypt sensitive data in transit

### Performance
- Use cursor pagination for large datasets
- Filter search queries for faster results
- Implement request throttling
- Monitor rate limits

### Reliability
- Implement retry logic with backoff
- Handle partial failures gracefully
- Log all integration activity
- Monitor webhook delivery

## Error Handling

Common HTTP Status Codes:

- `200 OK` - Success
- `201 Created` - Resource created
- `204 No Content` - Success, no response body
- `400 Bad Request` - Invalid parameters
- `401 Unauthorized` - Authentication failed
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `409 Conflict` - Data conflict
- `422 Unprocessable Entity` - Validation error
- `429 Too Many Requests` - Rate limited
- `500 Server Error` - Internal error

## Limits & Quotas

- **API Requests**: 200-600 per minute (varies by endpoint)
- **Webhook Retries**: Up to 3 attempts over 24 hours
- **Search Results**: Maximum 1000 records
- **Batch Size**: Up to 100 records per batch
- **Rate Limits**: Per endpoint, per user

## Resources

- [API Reference](https://developer.zendesk.com/api-reference/)
- [Help Center API](https://developer.zendesk.com/api-reference/help-center-api/)
- [Integration Services](https://developer.zendesk.com/api-reference/integration-services/)
- [Search API Guide](https://developer.zendesk.com/documentation/api-basics/using-the-search-api)
- [Webhooks Documentation](https://developer.zendesk.com/documentation/webhooks/)
