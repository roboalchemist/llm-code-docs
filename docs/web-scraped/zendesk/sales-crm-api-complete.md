# Zendesk Sell (Sales CRM) API - Complete Reference

Source: https://developer.zendesk.com/documentation/sales-crm/

Zendesk Sell is a sales force automation platform that helps sales teams manage leads, deals, and customer relationships. The Sell API provides programmatic access to sales data and workflows.

## Overview

Sell provides four complementary APIs for different use cases:

1. **Core API** - RESTful CRUD operations (all plans)
2. **Sync API** - Data synchronization (Growth+ only)
3. **Firehose API** - Real-time data streams (Growth+ only)
4. **Search API** - Advanced querying and analytics (Growth+ only)

## Core Concepts

### Leads

Prospective customers with contact information and sales pipeline status.

### Deals

Opportunities representing potential sales transactions with:

- Deal value and expected close date
- Sales stage and pipeline
- Associated contacts and organizations
- Custom fields and properties

### Contacts

Individual people in the sales pipeline with:

- Name, email, phone, address
- Associated deals and organizations
- Custom fields for lead scoring, source, etc.

### Organizations

Companies and accounts for grouping contacts and deals.

### Activities

Sales activities like calls, emails, meetings tracked to contacts/deals.

### Pipelines & Stages

Sales process definition with multiple stages for deal progression.

## Getting Started

### Authentication

**Token-Based Authentication:**

```bash
curl -X GET https://api.getbase.com/v3/contacts \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

**Base URL:** `https://api.getbase.com/v3/`

### Rate Limits

- API-based: 6000 requests per hour
- Per-user: 100 requests per minute per user
- Sync/Firehose: Custom limits based on plan

## Core API (v3)

### Leads Resource

```bash
GET /leads                    # List leads
POST /leads                   # Create lead
GET /leads/{id}              # Get lead details
PUT /leads/{id}              # Update lead
DELETE /leads/{id}           # Delete lead
GET /leads/{id}/activities   # Get lead activities
```

**Lead Properties:**

- `id` - Unique identifier
- `first_name`, `last_name` - Contact name
- `email`, `phone`, `mobile`, `fax` - Contact info
- `title` - Job title
- `organization_id` - Parent organization
- `status` - Lead status
- `custom_fields` - Custom data
- `owner_id` - Sales owner
- `created_at`, `updated_at` - Timestamps

### Deals Resource

```bash
GET /deals                    # List deals
POST /deals                   # Create deal
GET /deals/{id}              # Get deal details
PUT /deals/{id}              # Update deal
DELETE /deals/{id}           # Delete deal
GET /deals/{id}/activities   # Get associated activities
```

**Deal Properties:**

- `id` - Unique identifier
- `name` - Deal name
- `value` - Deal amount
- `currency` - Currency code
- `stage_id` - Sales stage
- `status` - Deal status
- `expected_close_date` - Forecast date
- `owner_id` - Sales owner
- `organization_id` - Associated organization
- `contact_ids` - Associated contacts
- `custom_fields` - Custom data

### Contacts Resource

```bash
GET /contacts                 # List contacts
POST /contacts                # Create contact
GET /contacts/{id}           # Get contact details
PUT /contacts/{id}           # Update contact
DELETE /contacts/{id}        # Delete contact
GET /contacts/{id}/deals     # Get related deals
GET /contacts/{id}/activities # Get activities
```

### Organizations Resource

```bash
GET /organizations            # List organizations
POST /organizations           # Create organization
GET /organizations/{id}      # Get organization
PUT /organizations/{id}      # Update organization
DELETE /organizations/{id}   # Delete organization
```

### Activities Resource

Track calls, emails, meetings, etc.

```bash
GET /activities              # List activities
POST /activities             # Create activity
GET /activities/{id}         # Get activity
PUT /activities/{id}         # Update activity
DELETE /activities/{id}      # Delete activity
```

**Activity Types:**

- Call
- Email
- Note
- Meeting

### Pipeline & Stages

```bash
GET /pipelines               # List pipelines
GET /pipelines/{id}          # Get pipeline details
GET /pipelines/{id}/stages   # Get pipeline stages
GET /stages/{id}             # Get stage details
```

### Custom Fields

```bash
GET /custom_fields           # List custom fields
POST /custom_fields          # Create custom field
PUT /custom_fields/{id}      # Update custom field
DELETE /custom_fields/{id}   # Delete custom field
```

## Sync API

Provides data synchronization similar to mobile device sync functionality.

### Key Features

- Synchronization layer for keeping local data current
- Incremental sync to reduce bandwidth
- Conflict resolution for offline edits
- Only available on Growth plans and higher

### Basic Sync Flow

1. **Initial Sync**: Download all data from server
2. **Track Changes**: Store sync state locally
3. **Incremental Sync**: Pull only changed records since last sync
4. **Conflict Resolution**: Handle merge conflicts if needed
5. **Upload**: Send local changes to server

### Sync Endpoints

```bash
POST /sync/init              # Initialize sync session
POST /sync/               # Get sync data since last checkpoint
POST /sync/ack              # Acknowledge sync receipt
```

## Firehose API

Real-time event streaming for high-volume integrations and event-driven workflows.

### Features

- Continuous data streams
- Near real-time updates (seconds latency)
- Event filtering and subscriptions
- Guaranteed delivery with exactly-once semantics
- Backpressure handling

### Event Types

- `lead.created`, `lead.updated`, `lead.deleted`
- `deal.created`, `deal.updated`, `deal.deleted`
- `contact.created`, `contact.updated`, `contact.deleted`
- `activity.created`, `activity.updated`, `activity.deleted`
- `organization.created`, `organization.updated`, `organization.deleted`

### Firehose Endpoints

```bash
GET /firehose                # List available firehose streams
POST /firehose/subscribe     # Subscribe to firehose
GET /firehose/{stream_id}    # Get stream updates
```

### Event Format

```json
{
  "id": "event-123",
  "type": "deal.updated",
  "timestamp": "2024-02-14T10:30:00Z",
  "data": {
    "deal": {
      "id": 456,
      "name": "Enterprise Deal",
      "value": 50000,
      "updated_at": "2024-02-14T10:30:00Z"
    }
  }
}
```

## Search API

Advanced querying for complex data retrieval and analytics.

### Interfaces

**JSON Search API** - Rich query language with filtering, sorting, aggregation

```bash
POST /search/deals
{
  "filter": {
    "value": {"$gt": 10000},
    "status": {"$in": ["won", "active"]}
  },
  "sort": {"value": -1},
  "limit": 50
}
```

**GraphQL API** - Query company hierarchy and relationships

```graphql
{
  organizations {
    id
    name
    contacts {
      id
      email
      deals {
        id
        value
      }
    }
  }
}
```

### Search Features

- Full-text search across text fields
- Complex filtering with operators
- Sorting and ordering
- Aggregations and grouping
- Pagination support

## Building Sell Apps

Create extensions for Sell using the Apps framework:

```bash
GET /apps                    # List installed apps
POST /apps                   # Install app
GET /apps/{id}              # Get app details
DELETE /apps/{id}           # Uninstall app
```

## Integration Patterns

### Two-Way Sync

- Sync Sell data with external CRM
- Maintain data currency in both systems
- Conflict resolution for concurrent edits

### Real-Time Webhooks

- Receive immediate notifications of data changes
- Trigger workflows in external systems
- Keep dashboards synchronized

### Analytics Exports

- Export deal and activity data for BI tools
- Search API for complex reporting queries
- Data warehouse integration

### Lead Scoring

- Use custom fields for scoring algorithms
- Activities trigger re-scoring
- Integrate with marketing automation

## Best Practices

### API Usage

- Use cursor pagination for large datasets
- Filter results to reduce data transfer
- Batch operations where possible
- Implement exponential backoff for retries

### Data Synchronization

- Use Sync API for mobile/offline scenarios
- Cache locally when sync not available
- Handle merge conflicts gracefully
- Clean up old sync checkpoints

### Firehose Integration

- Process events asynchronously
- Implement idempotent event handlers
- Monitor for stream lag and backpressure
- Log all event processing failures

### Security

- Validate all webhook signatures
- Encrypt sensitive data in transit
- Rotate API tokens regularly
- Use OAuth 2.0 for third-party apps

## Common Use Cases

### CRM Integration

Sync Sell leads and deals with enterprise CRM systems.

### Pipeline Analytics

Monitor deal progression and forecast accuracy using Search API.

### Activity Tracking

Create activities from email, calendar, call logs automatically.

### Lead Assignment

Implement custom lead routing based on territory or skill.

### Account-Based Marketing

Connect Sell accounts with marketing campaigns and track engagement.

## Limitations & Quotas

- **Request Rate**: 100 requests per minute per user
- **API Rate**: 6000 requests per hour
- **List Limit**: 10,000 records maximum per list
- **Sync**: Full sync every 7 days recommended
- **Firehose**: Up to 1MB/second stream throughput

## Error Handling

**Error Response Format:**

```json
{
  "error": {
    "code": 400,
    "message": "Invalid request parameters",
    "details": [
      {
        "field": "value",
        "message": "must be a positive number"
      }
    ]
  }
}
```

**Common Status Codes:**

- `400 Bad Request` - Invalid input
- `401 Unauthorized` - Authentication failure
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `409 Conflict` - Data conflict (sync)
- `429 Too Many Requests` - Rate limit exceeded
- `500 Server Error` - Internal error

## Client Libraries

SDKs available for:

- Python
- JavaScript/Node.js
- Ruby
- PHP
- Java

## Resources

- [Sell API Documentation](https://developer.zendesk.com/api-reference/sales-crm/)
- [Sync API Guide](https://developer.zendesk.com/documentation/sales-crm/sync/)
- [Firehose Guide](https://developer.zendesk.com/documentation/sales-crm/firehose/)
- [Search API Guide](https://developer.zendesk.com/documentation/sales-crm/search/)
- [Apps Framework](https://developer.zendesk.com/documentation/apps/)
