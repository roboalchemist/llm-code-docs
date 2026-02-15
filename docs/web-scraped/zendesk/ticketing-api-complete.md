# Source: https://developer.zendesk.com/documentation/ticketing/

# Zendesk Ticketing API - Complete Reference

The Zendesk Ticketing API enables programmatic access to create, read, update, and delete support tickets and related data. Built on REST principles with JSON responses.

## Core Concepts

### Tickets
Tickets represent customer support requests. Each ticket contains:
- Subject and description
- Status (new, open, pending, hold, solved, closed)
- Priority (urgent, high, normal, low)
- Type (problem, incident, question, task)
- Requester (customer who opened the ticket)
- Assignee (support agent)
- Tags for categorization
- Custom fields for extended data
- Attachments for file support

### Users
Represents both customers and agents in the system:
- End users (customers)
- Agents (support staff)
- Admin users
- Organizations for grouping users

### Organizations
Groups of users for:
- Account management
- Bulk user operations
- Organization-level custom fields
- SLA policy assignment

### Groups
Collections of agents for ticket routing and assignment.

### Automation & Workflow
- **Triggers**: Automated responses to ticket events
- **Automations**: Time-based rule execution
- **Macros**: Bulk ticket operations
- **Views**: Saved ticket searches with conditions
- **SLA Policies**: Service level agreements with breach handling

## Getting Started

### Authentication
Two methods supported:
- **API Token**: Set via Basic Auth in Authorization header
- **OAuth 2.0**: For third-party applications and integrations

```bash
# API Token example
curl -H "Authorization: Bearer YOUR_API_TOKEN" \
  https://yoursubdomain.zendesk.com/api/v2/tickets
```

### Making API Requests

**Base URL:** `https://{subdomain}.zendesk.com/api/v2/`

**Methods:** Standard REST (GET, POST, PUT, DELETE)

**Rate Limiting:**
- 200 requests per minute for most endpoints
- Search requests: 60 per minute
- Batch operations: Custom limits

### Response Format

All responses are JSON:
```json
{
  "ticket": {
    "id": 35436,
    "url": "https://yoursubdomain.zendesk.com/api/v2/tickets/35436.json",
    "subject": "Help with my account",
    "status": "open"
  }
}
```

## Main API Resources

### Tickets
- List tickets with filtering and pagination
- Create single or batch tickets
- Update ticket properties
- Delete tickets
- Add comments to tickets
- Manage ticket attachments
- Extract CSAT survey responses
- Bulk ticket operations (update many, delete many)

**Key Endpoints:**
- `GET /tickets` - List all tickets
- `POST /tickets` - Create ticket
- `GET /tickets/{id}` - Get specific ticket
- `PUT /tickets/{id}` - Update ticket
- `DELETE /tickets/{id}` - Delete ticket
- `GET /tickets/{id}/comments` - Get comments
- `POST /tickets/{id}/comments` - Add comment

### Users
- List, create, update, delete users
- Manage user fields and custom data
- Assign users to organizations
- Search users by email or name
- Bulk user operations
- Export user data

**Key Endpoints:**
- `GET /users` - List users
- `POST /users` - Create user
- `GET /users/{id}` - Get user
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

### Organizations
- Create and manage organization records
- Assign users to organizations
- Set organization-specific custom fields
- Organization search and filtering

**Key Endpoints:**
- `GET /organizations` - List organizations
- `POST /organizations` - Create organization
- `GET /organizations/{id}` - Get organization
- `PUT /organizations/{id}` - Update organization
- `DELETE /organizations/{id}` - Delete organization

### Groups
- List agent groups
- Create and manage groups
- Assign agents to groups
- Define group routing rules

**Key Endpoints:**
- `GET /groups` - List groups
- `POST /groups` - Create group
- `GET /groups/{id}` - Get group
- `PUT /groups/{id}` - Update group
- `DELETE /groups/{id}` - Delete group

### Views
- Create custom ticket views (saved searches)
- Apply conditions and filters
- Access preview data
- Execute view queries

**Key Endpoints:**
- `GET /views` - List views
- `POST /views` - Create view
- `GET /views/{id}` - Get view details
- `GET /views/{id}/tickets` - Get tickets in view
- `PUT /views/{id}` - Update view
- `DELETE /views/{id}` - Delete view

### Macros
- Create reusable ticket operations
- Bulk ticket updates via macros
- Macro execution tracking
- Category management

**Key Endpoints:**
- `GET /macros` - List macros
- `POST /macros` - Create macro
- `POST /macros/{id}/apply` - Execute macro
- `PUT /macros/{id}` - Update macro
- `DELETE /macros/{id}` - Delete macro

### Triggers
- Automated responses based on ticket conditions
- Event-based execution
- Action definitions (email, webhook, field updates)

**Key Endpoints:**
- `GET /triggers` - List triggers
- `POST /triggers` - Create trigger
- `PUT /triggers/{id}` - Update trigger
- `DELETE /triggers/{id}` - Delete trigger

### Automations
- Time-based rule execution
- Conditions and actions
- Stale ticket handling
- Priority escalation

**Key Endpoints:**
- `GET /automations` - List automations
- `POST /automations` - Create automation
- `PUT /automations/{id}` - Update automation
- `DELETE /automations/{id}` - Delete automation

### SLA Policies
- Define service level agreements
- Priority and condition matching
- Response and resolution times
- Breach tracking and notifications

**Key Endpoints:**
- `GET /sla_policies` - List SLA policies
- `POST /sla_policies` - Create SLA policy
- `PUT /sla_policies/{id}` - Update SLA policy
- `DELETE /sla_policies/{id}` - Delete SLA policy

### Custom Fields
- Define custom field schemas
- Apply custom fields to tickets
- Field validation and types

**Key Endpoints:**
- `GET /ticket_fields` - List custom fields
- `POST /ticket_fields` - Create custom field
- `PUT /ticket_fields/{id}` - Update custom field

## Common Tasks

### Creating a Ticket

```bash
curl -X POST https://yoursubdomain.zendesk.com/api/v2/tickets \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "ticket": {
      "subject": "My printer is on fire!",
      "description": "The coffee is pouring out of my printer!",
      "priority": "urgent"
    }
  }'
```

### Updating Multiple Tickets

```bash
curl -X PUT https://yoursubdomain.zendesk.com/api/v2/tickets/update_many \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tickets": [
      {"id": 123, "status": "solved"},
      {"id": 124, "status": "solved"}
    ]
  }'
```

### Searching Tickets

Use the Search API for complex queries:

```bash
curl https://yoursubdomain.zendesk.com/api/v2/search \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -G --data-urlencode 'query=status:open priority:high'
```

### Adding Comments

```bash
curl -X POST https://yoursubdomain.zendesk.com/api/v2/tickets/35436/comments \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "comment": {
      "body": "This is a comment",
      "public": true
    }
  }'
```

## Pagination

### Offset Pagination
- Use `page` and `per_page` parameters
- Limited to 1000 records per page
- Best for small datasets

```bash
/api/v2/tickets?page=2&per_page=50
```

### Cursor Pagination
- Use `cursor` parameter for large datasets
- More efficient for pagination
- Returns `after_cursor` for next page

## Error Handling

**Error Response Format:**
```json
{
  "error": "Invalid request body",
  "description": "Could not parse JSON"
}
```

**Common Status Codes:**
- `400 Bad Request` - Invalid parameters
- `401 Unauthorized` - Authentication failure
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation error
- `429 Too Many Requests` - Rate limit exceeded

## Best Practices

### Asynchronous Operations
- Create tickets asynchronously for better performance
- Use job status API to poll for completion
- Reduces response time in high-volume scenarios

### Batch Operations
- Use batch endpoints for bulk updates
- Maximum 100 items per batch
- More efficient than individual requests

### Field Validation
- Use custom fields API to get field definitions
- Validate enum values before submission
- Handle date/time formats correctly

### Search Optimization
- Use cursor pagination for large result sets
- Filter by date ranges to reduce result size
- Leverage indexed fields for faster queries

### Error Recovery
- Implement exponential backoff for retries
- Handle 429 (rate limit) responses gracefully
- Log all API errors for debugging

## Integration Patterns

### Webhook Integration
- Receive real-time ticket events
- Update external systems on ticket changes
- Trigger external workflows

### Chat Integration
- Create tickets from chat conversations
- Link tickets to chat transcripts
- Escalate chat to tickets

### Email Integration
- Create tickets from email
- Reply to tickets via email
- Forward ticket comments via email

### Side Conversations
- Create private conversations on tickets
- Include external email addresses
- Collaborate without customer visibility

## Advanced Topics

### Custom Objects Integration
- Link custom objects to tickets
- Enrich ticket data with custom object context
- Query related custom object data

### JIRA Integration
- Sync JIRA issues to Zendesk tickets
- Two-way issue synchronization
- Custom field mapping

### On-Behalf-Of Operations
- Create/update tickets on behalf of end users
- Maintains proper requester attribution
- OAuth requirement

### CORS (Cross-Origin Requests)
- Client-side API requests from web widgets
- Restricted endpoints for browser security
- CORS headers configuration

## Client Libraries

Official SDKs available for:
- Python
- JavaScript/Node.js
- Java
- Ruby
- PHP
- Go
- C#

See SDK documentation for language-specific examples and patterns.

## Resources

- [Zendesk Support API reference](https://developer.zendesk.com/api-reference/ticketing-api/)
- [API quickstart guide](https://developer.zendesk.com/documentation/ticketing-api/getting-started-with-the-ticketing-api/zendesk-api-quick-start/)
- [Search API documentation](https://developer.zendesk.com/documentation/api-basics/using-the-search-api)
- [REST API glossary](https://developer.zendesk.com/documentation/api-basics/getting-started-with-zendesk-apis/rest-api-glossary)
