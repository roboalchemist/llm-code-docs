# Zendesk Developer Documentation - Complete Index

**Source**: https://developer.zendesk.com/

**Last Updated**: February 2024

Zendesk is a comprehensive customer service and support platform offering integrated APIs and SDKs for building custom solutions and integrations.

## Platform Overview

Zendesk Sunshine is the open, flexible platform built on AWS enabling:

- Ticketing system (Support) for customer support
- Help Center for knowledge bases and communities
- Live Chat and messaging for conversational support
- Voice/Call center (Talk) for telephony integration
- Sales CRM (Sell) for sales pipeline management
- AI Agents for conversational automation
- Multi-channel messaging (Conversations) across web, mobile, social
- Custom data objects (Sunshine) for business-specific information
- Integration services for third-party system connections
- Apps framework for extending platform functionality

## API Categories

### Core Ticketing APIs

**Ticketing API** - Manage support tickets and related data

- Create, read, update, delete tickets
- User and organization management
- Group and queue management
- Views, macros, and ticket filtering
- Triggers and automations for workflows
- SLA policies and service levels
- Custom fields and ticket properties
- Comment and attachment management
- File: `ticketing-api-complete.md`

**Support API** (Same as Ticketing)

- Full REST API for all Support features
- Batch operations for bulk updates
- Ticket search and filtering
- Agent and customer user management

### Sales/CRM APIs

**Sell API** - Sales CRM and pipeline management

- **Core API** (v3) - RESTful CRUD operations
  - Leads, deals, contacts, organizations
  - Activities (calls, emails, meetings)
  - Custom fields and properties
  - Pipelines and sales stages
- **Sync API** - Data synchronization layer (Growth+ plans)
  - Mobile device sync support
  - Incremental sync capabilities
  - Offline data support
- **Firehose API** - Real-time event streaming (Growth+ plans)
  - Continuous data stream
  - Near real-time updates (seconds latency)
  - Event subscriptions and filtering
  - Guaranteed delivery semantics
- **Search API** - Advanced querying (Growth+ plans)
  - JSON search with complex filters
  - GraphQL interface for hierarchy
  - Aggregations and reporting
  - Full-text search capabilities
- File: `sales-crm-api-complete.md`

### Chat & Messaging APIs

**Chat API** - Live chat functionality

- Real-time chat conversations
- Agent availability management
- Visitor tracking and information
- Proactive chat engagement
- Chat routing and department assignment
- Conversation history and transcripts

**Real-Time Chat API** - WebSocket-based real-time messaging

- Bi-directional message streaming
- Typing indicators and presence
- Message read receipts
- Connection lifecycle management

**Chat Conversations API** - Agent-side operations

- Agent interaction management
- Chat transfers between agents
- Tag management for chats
- Agent invitation and participation

**Conversations API** (Unified Messaging) - Multi-channel support

- Unify messaging across channels
- Web chat, mobile, SMS, email, social
- Participant management
- Channel routing and switching
- Conversation lifecycle

**AI Agents API** - Conversational AI automation

- Natural language understanding
- Automated response generation
- Multi-turn conversations
- Knowledge base integration
- Handoff triggers to human agents
- Conversation analytics
- Confidence scoring
- Custom model configuration

**Answer Bot API** - Help Center suggestions

- Analyze customer inquiries
- Recommend relevant articles
- Track suggestion effectiveness
- Integration with chat/widgets

Files: `chat-ai-messaging-apis.md`

### Voice/Telephony API

**Voice API** (Talk API) - Call center integration

- Inbound and outbound call management
- Phone number provisioning
- Call recording and transcription
- Voicemail handling
- IVR (Interactive Voice Response) configuration
- Agent status management
- Call routing and queues
- Call-to-ticket creation
- Agent phone status tracking
- Call analytics and reporting
- Real-time call metrics
- Compliance and recording management
- Talk Partner Edition for custom integrations

File: `voice-api-complete.md`

### Help Center API

**Help Center API** - Knowledge base management

- Article creation and management
- Section and category organization
- Multi-language support (translations)
- Article publishing and versioning
- Draft and published states
- Search indexing
- Community features
- User segments for targeting
- Analytics on article usage

File: `additional-apis-reference.md` (Help Center section)

### Custom Data APIs

**Custom Objects API** - Store business-specific data

- Create custom object types with schemas
- Define relationships to Zendesk objects
- Link to tickets, users, organizations
- Field types: text, number, date, dropdown, multiselect, boolean, record
- Bulk record operations
- Custom object search and filtering
- Integration with triggers and automations
- Events and activity tracking
- Zendesk Explore analytics integration

**Profiles API** - Customer profile management

- Build unified customer views
- Link external data sources
- Create relationships with Zendesk objects
- Multi-source customer context

File: `custom-objects-api-complete.md`

### Integration & Automation APIs

**Webhooks API** - Event-driven integrations

- Subscribe to ticket, user, chat events
- Automatic webhook delivery
- Webhook signing and verification
- Retry logic with exponential backoff
- Webhook testing and monitoring
- Event filtering and conditions
- Custom headers support
- Event types: ticket, user, organization, chat, comment

**Integration Services (ZIS) APIs** - Event-driven automation

- **ZIS Configs API** - Integration configurations
- **Connections API** - External service connections
- **ZIS Inbound Webhooks API** - Receive external webhooks
- **ZIS Links API** - Named links between objects
- **ZIS Registry API** - Custom registry data storage
- **Trigger Events Reference** - Available integration events

**Amazon EventBridge** - AWS event streaming

- Route Zendesk events to AWS
- Integration with AWS services
- Cross-account event routing

File: `additional-apis-reference.md`

### Apps Framework

**Apps Core API** - App lifecycle and management

- App installation and configuration
- API access from app context
- Storage for app state
- Event subscriptions

**Apps Support API** - Support product integration

- Access to ticket, user, organization data
- UI component rendering
- Modal and notification support

**Apps Chat API** - Chat product integration

- Access to conversation data
- Visitor information access

**Apps Sell API** - Sell product integration

- Lead and deal access
- Activity management

File: `apps.md`

### Authentication & Security

**OAuth 2.0** - Third-party authorization

- Authorization Code flow (recommended)
- Implicit flow (legacy)
- PKCE support for mobile apps
- Token refresh capability
- Scope-based access control
- OAuth client management

**API Token Authentication** - Simple server-to-server

- Token creation and management
- Basic auth with email/token
- Token revocation and rotation

**Two-Factor Authentication (2FA)** - Additional security

- 2FA code requirement handling
- SSO integration support

File: `authentication-oauth-guide.md`

### Admin & Account APIs

**Status API** - System status and maintenance

- Overall system status
- Incident tracking
- Maintenance windows
- Component-level status

**Account Settings** - Account administration

- Account information and features
- Audit logs for all changes
- Custom roles and permissions
- Brand management

**Audit Logs** - Track all administrative actions

- Changes to configuration
- User access logs
- API usage tracking
- Administrative actions

File: `additional-apis-reference.md`

### Search & Analytics APIs

**Search API** - Powerful cross-resource search

- Unified search across objects
- Advanced query syntax (operators, filters)
- Full-text search capability
- Boolean operators (AND, OR, NOT)
- Date and numeric filtering
- Wildcard support
- Result sorting and pagination
- Search in tickets, users, organizations, articles

**Explore API** - Analytics and reporting

- Custom report creation
- Pre-built report templates
- Report scheduling
- Data export
- Metrics: tickets, agents, channels, CSAT
- Custom object reporting

File: `additional-apis-reference.md`

### Routing & Omnichannel

**Omnichannel Routing APIs** - Channel-aware routing

- Routing attributes configuration
- Skill-based routing
- Agent availability
- Channel-specific rules
- Queue management
- Priority routing

**Workforce Management (WFM)** - Agent scheduling

- Schedule management
- Shift planning
- Adherence tracking
- Forecast accuracy

File: `additional-apis-reference.md` (Omnichannel section)

### Mobile & Web SDKs

#### Web Widget APIs

- Web Widget (Messaging) API - Embedded messaging widget
- Web Widget (Classic) API - Legacy widget support
- Widget customization and theming
- Visitor identification
- Pre-chat forms
- Proactive messaging

#### Mobile SDKs

- **Android SDK** - Native Android support
- **iOS SDK** - Native iOS support
- **Unity SDK** - Game engine support
- Push notifications
- In-app messaging
- Offline support

## Documentation Files

### Core Reference Files

1. **ticketing-api-complete.md** - Complete Ticketing API reference
   - All ticket operations (CRUD)
   - User, organization, group management
   - Views, macros, triggers, automations
   - SLA policies and workflows
   - Best practices and examples
   - Error handling and limits

2. **sales-crm-api-complete.md** - Sell/CRM API reference
   - Core API (CRUD operations)
   - Sync API for data synchronization
   - Firehose API for real-time events
   - Search API for analytics
   - Two-way integration patterns
   - Lead scoring and pipeline management

3. **voice-api-complete.md** - Voice/Talk API reference
   - Call management and routing
   - Phone number provisioning
   - Call recording and transcription
   - Voicemail handling
   - IVR configuration
   - Agent status and availability
   - Call-to-ticket workflows
   - Compliance and recording management

4. **custom-objects-api-complete.md** - Custom Objects reference
   - Object type definition and schema
   - Record CRUD operations
   - Field types and validation
   - Relationships to Zendesk objects
   - Search and filtering
   - Integration with triggers/automation
   - Use cases and patterns

5. **chat-ai-messaging-apis.md** - Chat, messaging, and AI APIs
   - Chat API for live chat
   - Real-Time Chat API (WebSocket)
   - AI Agents API for automation
   - Conversations API (unified messaging)
   - Answer Bot API for suggestions
   - Multi-channel routing patterns
   - Handoff to human agents

6. **authentication-oauth-guide.md** - Security and auth reference
   - API Token creation and usage
   - OAuth 2.0 flows (Authorization Code, Implicit)
   - PKCE for mobile/desktop apps
   - Token management and rotation
   - 2FA handling
   - SSO integration
   - Security best practices

7. **additional-apis-reference.md** - Supplementary APIs
   - Help Center API
   - Integration Services (ZIS) APIs
   - Status API
   - Search API
   - Admin and Audit APIs
   - Omnichannel/Routing APIs
   - Explore API for analytics
   - Webhooks API
   - Sunshine Profiles API
   - Events API

### Existing Files (from previous coverage)

8. **api-basics.md** - API fundamentals
   - Getting started with Zendesk APIs
   - Authentication overview
   - REST API principles
   - Request/response formats
   - Pagination methods
   - Error handling

9. **ticketing.md** - Support product guide
   - Product overview
   - Ticket lifecycle
   - User management
   - Routing and assignment
   - CSAT and surveys

10. **help-center.md** - Knowledge base guide
    - Article management
    - Publishing workflow
    - Community features
    - Search optimization

11. **live-chat.md** - Chat product guide
    - Agent interface
    - Visitor management
    - Proactive engagement
    - Chat routing

12. **sales-crm.md** - Sales product guide
    - Pipeline management
    - Deal tracking
    - Activity logging
    - Sales automation

13. **custom-objects.md** - Custom data overview
    - Object creation basics
    - Relationship management
    - Use cases and patterns

14. **webhooks.md** - Webhook overview
    - Event subscriptions
    - Webhook security
    - Integration patterns

15. **integration-services.md** - ZIS overview
    - Integration configuration
    - Event flows
    - Trigger setup

16. **apps.md** - Apps framework guide
    - App development
    - Building extensions
    - Marketplace distribution

17. **web-widget-sdk.md** - Widget documentation
    - Widget deployment
    - Customization options
    - API configuration

18. **conversations-api.md** - Messaging API stub (brief)
    - Unified messaging overview

## Getting Started

### For Different Use Cases

**Building Support Integrations:**

1. Start with `api-basics.md` for fundamentals
2. Review `authentication-oauth-guide.md` for auth
3. Explore `ticketing-api-complete.md` for main API
4. Check `webhooks.md` for real-time events
5. See `additional-apis-reference.md` for Help Center

**Building Sales Integrations:**

1. Review `authentication-oauth-guide.md`
2. Study `sales-crm-api-complete.md` (Core API first)
3. For real-time: Use Firehose API
4. For sync: Consult Sync API documentation
5. For reporting: Check Search API section

**Building Chat/Messaging Solutions:**

1. Start with `chat-ai-messaging-apis.md`
2. Review `web-widget-sdk.md` for web embedding
3. Check mobile SDK guides for apps
4. Explore `webhooks.md` for events
5. Study AI Agents for automation

**Multi-Channel Integrations:**

1. Review `chat-ai-messaging-apis.md` (Conversations API)
2. Check `voice-api-complete.md` for phone
3. Explore `custom-objects-api-complete.md` for data
4. Study `webhooks.md` for synchronization
5. Reference `additional-apis-reference.md` for ZIS

### Authentication Steps

1. Create API token (Admin → APIs)
2. OR configure OAuth client (Admin → OAuth clients)
3. Choose token auth for simple integrations
4. Choose OAuth for third-party/user-delegation
5. Review `authentication-oauth-guide.md` for details

### First API Call

```bash
# With API Token
curl -H "Authorization: Bearer YOUR_API_TOKEN" \
  https://yoursubdomain.zendesk.com/api/v2/tickets

# With OAuth
# Complete flow in authentication-oauth-guide.md
```

## API Best Practices

### Performance

- Use cursor pagination for large datasets
- Implement request caching where appropriate
- Batch operations for bulk changes
- Monitor rate limits and implement backoff
- Use Search API filters to reduce results

### Reliability

- Implement exponential backoff for retries
- Handle all HTTP error codes gracefully
- Log all API interactions
- Monitor webhook delivery
- Set up alerts for rate limit approaches

### Security

- Use OAuth for third-party applications
- Rotate API tokens every 90 days
- Store credentials securely (no hardcoding)
- Verify webhook signatures
- Use HTTPS for all requests
- Implement proper CORS for browser apps

### Integration Patterns

- Use webhooks for async events (not polling)
- Design idempotent operations
- Handle partial failures gracefully
- Clean up resources on errors
- Document integration architecture

## Key Resources

### Official Documentation

- [Zendesk Developer Hub](https://developer.zendesk.com/)
- [API Reference](https://developer.zendesk.com/api-reference/)
- [Documentation Hub](https://developer.zendesk.com/documentation/)
- [Developer Community](https://support.zendesk.com/hc/en-us/community/topics)

### SDKs & Client Libraries

- JavaScript/Node.js SDK
- Python SDK
- Ruby SDK
- PHP SDK
- Java SDK
- Go SDK
- C# SDK

### Related Tools

- [Postman Collection](https://developer.zendesk.com/api-reference/) - Pre-built requests
- [Zendesk CLI](https://developer.zendesk.com/documentation/apps/getting-started/using-the-zendesk-cli/) - Development tool
- [Webhooks Tool](https://webhook.site/) - Test webhooks
- [cURL](https://curl.se/) - Command-line requests

## Rate Limits & Quotas

| Endpoint | Limit | Notes |
|----------|-------|-------|
| Most API endpoints | 200 req/min | Per user |
| Search API | 60 req/min | Per user |
| Incremental Exports | 40 req/min | Per user |
| Batch operations | 100 items max | Per request |
| Webhook retries | 3 attempts | 24 hour window |

## Frequently Needed Information

- [Creating API Tokens](authentication-oauth-guide.md#creating-an-api-token)
- [OAuth Flows](authentication-oauth-guide.md#oauth-20-authentication)
- [Search Syntax](additional-apis-reference.md#search-query-syntax)
- [Webhook Events](additional-apis-reference.md#webhook-events)
- [Error Codes](additional-apis-reference.md#error-handling)
- [Pagination Methods](api-basics.md#pagination)

## Latest Updates

### February 2024 Refresh

- Added comprehensive ticketing-api-complete.md
- Added complete sales-crm-api-complete.md
- Added voice-api-complete.md
- Added chat-ai-messaging-apis.md
- Added authentication-oauth-guide.md
- Added custom-objects-api-complete.md
- Added additional-apis-reference.md
- Expanded API coverage to include:
  - AI Agents API
  - Conversations/Unified Messaging
  - Help Center API
  - Integration Services (ZIS)
  - Status API
  - Search API
  - Webhooks reference
  - Admin APIs
  - Omnichannel routing
  - Explore analytics
  - Mobile SDKs
  - Full authentication guide

## Architecture & Design Patterns

### Zendesk Sunshine Platform

Built on AWS with:

- RESTful API design
- JSON request/response format
- Event-driven architecture
- Real-time capabilities (WebSockets, Firehose)
- Multi-tenancy support
- Global infrastructure

### Integration Approaches

1. **Polling** - Regular API queries (not recommended)
2. **Webhooks** - Event notifications (recommended)
3. **Sync API** - Bidirectional data sync
4. **Firehose** - Real-time event streams
5. **SDKs** - Language-specific libraries

## Support & Help

- [Zendesk Support](https://support.zendesk.com/)
- [Developer Forum](https://support.zendesk.com/hc/en-us/community/topics)
- [Status Page](https://status.zendesk.com/)
- [API Rate Limit Guide](https://developer.zendesk.com/documentation/api-basics/best-practices-for-avoiding-rate-limiting/)

---

**Complete API Coverage**: This index now covers all major Zendesk APIs including Ticketing, Sales/CRM, Chat, Voice, Custom Objects, AI Agents, Integration Services, and administrative APIs with detailed reference documentation for each.
