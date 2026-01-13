# Using the Datadog API

## Overview

The Datadog HTTP API enables programmatic access to the platform for sending data, building visualizations, and managing accounts.

## Send Data to Datadog

### Integration Endpoints

Available integrations for data submission:

- AWS Integration
- AWS Logs Integration
- Azure Integration
- Google Cloud Integration
- Slack Integration
- PagerDuty Integration
- Webhooks Integration

### Platform Endpoints

**Metrics**: Post metrics data for dashboard graphing and query historical metric periods.

**Events**: Submit and retrieve events through the Datadog event explorer.

**Synthetic Monitoring**: Create, manage, and monitor Synthetic tests with result tracking.

**Tracing Agent API**: Forward trace data to Datadog Agent for processing.

**LLM Observability Export API**: Access LLM data for external evaluations and offline storage of spans.

## Visualize Your Data

Once data reaches Datadog, use the API to programmatically construct visualizations:

- **Dashboards & Lists**: Build and manage dashboard collections
- **Host Management**: Organize and tag infrastructure hosts
- **Embeddable Graphs**: Create shareable graph visualizations
- **Snapshots**: Capture point-in-time graph states
- **Service Dependencies**: Map APM service relationships
- **Monitors**: Establish alert conditions and thresholds
- **Service Checks**: Post status data for monitor integration
- **Logs Management**: Create, configure, and manage log resources
- **Host Information**: Retrieve organizational infrastructure details
- **SLOs**: Define and track Service Level Objectives
- **Security Signals**: Generate security monitoring alerts

## Manage Your Account

Administrative operations available through the API:

- **User Management**: Create and modify user accounts
- **Role Management**: Configure access control roles
- **Organization Settings**: Manage organization configuration
- **Authentication**: Validate API and application credentials
- **Logs Access Control**: Restrict log visibility with query rules
- **Key Management**: Administer API and application keys
- **Usage Metering**: Track consumption across Datadog services
- **IP Ranges**: Access Datadog infrastructure IP prefixes

## Support

For questions or assistance, contact Datadog's solutions engineering team through the Help section.
