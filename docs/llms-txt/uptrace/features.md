# Source: https://uptrace.dev/raw/features.md

# Uptrace Features

> Explore Uptrace features: alerting, dashboards, querying, service graphs, SSO, Grafana integration, and more.

This page provides an overview of Uptrace features and documentation to help you get the most out of your observability data.

## Querying and Analysis

Query and analyze your telemetry data using a powerful query language.

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/features/querying/spans">
        Querying spans and logs
      </a>
    </td>
    
    <td>
      Filter, group, and aggregate traces and logs using UQL (Uptrace Query Language).
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/features/querying/metrics">
        Querying metrics
      </a>
    </td>
    
    <td>
      Write PromQL-inspired queries with aliases, joins, and expressions for metrics.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/features/querying/searching">
        Searching
      </a>
    </td>
    
    <td>
      Use a simple search syntax to find spans and logs quickly.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/features/querying/promql-compat">
        PromQL compatibility
      </a>
    </td>
    
    <td>
      Use existing Prometheus queries with Uptrace's PromQL-compatible engine.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/features/querying/grouping">
        Span grouping
      </a>
    </td>
    
    <td>
      Understand how Uptrace groups similar spans together for analysis.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/features/querying/semconv">
        Semantic conventions
      </a>
    </td>
    
    <td>
      Learn about indexed OpenTelemetry attributes for optimized queries.
    </td>
  </tr>
</tbody>
</table>

## Visualization

Build dashboards and visualize your application's behavior.

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/features/dashboards">
        Dashboards
      </a>
    </td>
    
    <td>
      Build custom dashboards from spans, events, logs, and metrics using UI or YAML.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/features/service-graph">
        Service graph
      </a>
    </td>
    
    <td>
      Get a visual representation of service interactions, dependencies, and performance.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/features/annotations">
        Chart annotations
      </a>
    </td>
    
    <td>
      Annotate charts with deployment markers, incidents, and notes for context.
    </td>
  </tr>
</tbody>
</table>

## Monitoring and Alerting

Set up monitors and receive notifications when issues occur.

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/features/alerting">
        Alerts and notifications
      </a>
    </td>
    
    <td>
      Create metric and error monitors with notifications via email, Slack, PagerDuty, and more.
    </td>
  </tr>
</tbody>
</table>

## Data Processing

Transform and process telemetry data before it reaches Uptrace.

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/features/transformations">
        Transformations
      </a>
    </td>
    
    <td>
      Rename, delete, or parse attributes using YAML-based rules. Drop or sample spans.
    </td>
  </tr>
</tbody>
</table>

## Integrations

Connect Uptrace with other tools in your observability stack.

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/features/grafana">
        Grafana integration
      </a>
    </td>
    
    <td>
      Use Uptrace as a Prometheus and Tempo data source in Grafana.
    </td>
  </tr>
</tbody>
</table>

## Single Sign-On (SSO)

Configure SSO to manage user access through your identity provider.

<table>
<thead>
  <tr>
    <th>
      Provider
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/features/sso/google">
        Google Cloud Auth
      </a>
    </td>
    
    <td>
      Use Google as an OIDC provider for Uptrace authentication.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/features/sso/okta">
        Okta
      </a>
    </td>
    
    <td>
      Configure Okta SAML or OIDC for enterprise SSO.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/features/sso/keycloak">
        Keycloak
      </a>
    </td>
    
    <td>
      Set up Keycloak as your identity provider.
    </td>
  </tr>
</tbody>
</table>

## Administration

Manage users, organizations, and projects.

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/features/fixtures">
        Data fixtures
      </a>
    </td>
    
    <td>
      Seed users, organizations, and projects using YAML or JSON configuration.
    </td>
  </tr>
</tbody>
</table>

## What's Next?

<table>
<thead>
  <tr>
    <th>
      I want to...
    </th>
    
    <th>
      Read this
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Send data to Uptrace
    </td>
    
    <td>
      <a href="/get">
        Getting started
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Learn about OpenTelemetry
    </td>
    
    <td>
      <a href="/opentelemetry">
        OpenTelemetry documentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Set up host monitoring
    </td>
    
    <td>
      <a href="/opentelemetry/collector/host-metrics">
        OpenTelemetry Collector host metrics
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Monitor a database
    </td>
    
    <td>
      <a href="/guides/opentelemetry-postgresql">
        PostgreSQL
      </a>
      
       or <a href="/guides/opentelemetry-mysql">
        MySQL
      </a>
      
       guides
    </td>
  </tr>
</tbody>
</table>
