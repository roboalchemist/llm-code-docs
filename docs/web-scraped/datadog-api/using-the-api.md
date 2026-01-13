# Using the Datadog API

## Overview

The Datadog HTTP API enables programmatic access to the platform for sending data, building visualizations, and managing accounts. The API supports multiple Datadog sites (US1, US3, US5, EU, AP1, AP2, US1-FED).

## Core API Capabilities

The Datadog API enables three primary functions:

### Data Ingestion

Use the API to send integrations data to Datadog. Organizations can transmit:
- Metrics data for dashboard graphing and historical queries
- Events to the event explorer
- Synthetic test results
- Logs and traces
- LLM Observability data

### Data Visualization

The platform supports programmatic creation of:
- Dashboards and Dashboard Lists
- Embeddable Graphs and snapshots
- Monitors and alerts
- Service dependencies and APM relationships
- Service-Level Objectives (SLOs)
- Security monitoring signals

### Account Management

Administrative functions include:
- User and role management
- Organization configuration
- API and application key management
- Logs access restrictions and configuration
- Usage metering across multiple billing dimensions
- IP range verification

## Send Data to Datadog

Use the API to begin sending integrations data to Datadog. With some additional setup of the Agent, you can also use the API to send Synthetic test data, Logs, and Traces to Datadog.

### Integration Endpoints

Available integrations endpoints:
- AWS Integration
- AWS Logs Integration
- Azure Integration
- Google Cloud Integration
- Slack Integration
- PagerDuty Integration
- Webhooks Integration

### Platform Data Endpoints

Use these endpoints to post and fetch data to and from other parts of the Datadog platform:

- **Metrics Endpoints**: Post metrics data so it can be graphed on Datadog's dashboards and query metrics from any time period
- **Events Endpoints**: Post and fetch events to and from the Datadog event explorer
- **Synthetic Monitoring**: Create, start, stop, and view Synthetic test results
- **Tracing Agent API**: Send traces to your Datadog Agent, which then forwards them to Datadog
- **LLM Observability Export API**: Access your LLM Observability data for running external evaluations and exporting spans for offline storage

## Visualize Your Data

Once you are sending data to Datadog, you can use the API to build data visualizations programmatically:

- **Dashboards**: Build and manage Dashboards and view Dashboard Lists
- **Host Tags**: Manage host tags for your infrastructure
- **Embeddable Graphs**: Create graphs that can be embedded in external applications
- **Graph Snapshots**: Take snapshots of your graphs
- **Service Dependencies**: See a list of your APM services and their dependencies
- **Monitors**: Create and manage monitors for alerting
- **Service Checks**: Post check statuses for use with monitors
- **Logs Configuration**: Create and manage Logs, Logs Indexes, and Logs Pipelines
- **Host Information**: Get host information for your organization
- **Service Level Objectives**: Create and manage SLOs
- **Security Monitoring**: Generate Security Monitoring signals

## Manage Your Account

You can also use the Datadog API to manage your account programmatically:

- **User Management**: Manage users in your organization
- **Role Management**: Manage roles and permissions
- **Organization Settings**: Configure your organization
- **Authentication**: Verify API and app keys with the Authentication endpoint
- **Logs Access Restrictions**: Grant specific logs access with the Logs Restriction Queries
- **Key Management**: Manage existing keys and create new ones
- **Usage Metering**: Get hourly, daily, and monthly usage across multiple facets of Datadog
- **IP Ranges**: See the list of IP prefixes belonging to Datadog

## Authentication

The Datadog API uses two primary authentication methods:

### API Keys and Application Keys

Manage your API and application keys through:
- The Key Management API endpoint for programmatic key management
- The Authentication endpoint to verify your credentials before making requests

### OAuth2

The platform offers OAuth2 authentication with:
- OAuth2 in Datadog for standard OAuth flows
- Authorization Endpoints for token exchange
- Authorization Scopes for granular permission control

## API Features

### Rate Limiting

The Datadog API implements rate limiting to maintain platform stability. Specific rate limits vary by endpoint category. Check the Rate Limits documentation for detailed threshold information.

### Request/Response Format

The API accepts and returns data in JSON format. Requests can be customized with:
- Query parameters for filtering and pagination
- Headers for authentication and content negotiation
- Request bodies in JSON for data submission

### Multiple Data Centers

The API supports requests to multiple Datadog sites:
- **US1**: US region (primary)
- **US3**: US region (alternative)
- **US5**: US region (alternative)
- **EU**: European Union region
- **AP1**: Asia Pacific region (alternative 1)
- **AP2**: Asia Pacific region (alternative 2)
- **US1-FED**: Federal region (US government)

## Key Integrations

The API integrates with major cloud providers:
- **AWS**: Including AWS integration, CloudTrail logs, and EC2 instances
- **Microsoft Azure**: Azure resources and diagnostics
- **Google Cloud Platform**: GCP resources and metrics
- **Oracle Cloud**: Oracle Cloud infrastructure

Additionally, notification services like Slack and PagerDuty can be configured programmatically.

## Data Types Supported

The platform accepts:
- **Custom Metrics**: Post custom metric data with tags
- **Distribution Points**: Send distribution data for percentile analysis
- **Service Checks**: Post service check results
- **Structured Logs**: JSON-formatted log entries
- **Events**: Custom events for timeline and alerting
- **Traces**: Application traces for APM

## Available Endpoints

The Datadog API provides over 100 endpoint categories covering:
- **Infrastructure**: Metrics, hosts, tags, and service checks
- **Observability**: Logs, events, traces, and APM
- **Monitoring**: Monitors, SLOs, and alerting
- **Security**: Security monitoring, findings, and signals
- **Testing**: Synthetic monitoring and CI/CD visibility
- **Data Visualization**: Dashboards, embeddable content, and snapshots
- **Account Management**: Users, roles, organizations, and usage
- **Real User Monitoring (RUM)**: Browser and mobile user session tracking
- **Cloud Integration**: AWS, Azure, GCP, and other cloud providers

## Best Practices

When using the Datadog API:

1. **Use the appropriate site URL** for your data center location
2. **Rotate API keys regularly** for security
3. **Use application keys** for third-party integrations
4. **Monitor rate limits** and implement backoff strategies
5. **Use OAuth2** for user-facing applications instead of static API keys
6. **Validate API responses** for error conditions
7. **Tag your data** for easier filtering and aggregation
8. **Use HTTPS** for all API requests (enforced)

## Authentication Endpoint

Before making API calls, you can verify your credentials using the Authentication endpoint to ensure your API and application keys are valid.

## Rate Limits

The documentation provides endpoint-specific rate limit details. Standard rate limiting applies based on your organization's Datadog plan. Implement exponential backoff for rate-limited responses (HTTP 429).

## Error Handling

The API returns standard HTTP status codes:
- **2xx**: Successful requests
- **4xx**: Client errors (invalid requests, authentication failures)
- **5xx**: Server errors (temporary issues)

Check the API response body for detailed error messages and resolution steps.

## Next Steps

For implementation details and specific endpoint documentation, refer to:
- API Reference guides for each endpoint category
- Authentication documentation for credential setup
- Rate Limits documentation for rate-specific details
- Integration guides for third-party service setup

---

**Source**: https://docs.datadoghq.com/api/latest/using-the-api/

This documentation was extracted from the official Datadog API documentation for use with AI and LLM applications.
