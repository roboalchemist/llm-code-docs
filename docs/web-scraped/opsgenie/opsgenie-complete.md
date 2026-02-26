# OpsGenie Documentation

## IMPORTANT: End of Support Notice

Atlassian has announced the discontinuation of OpsGenie. If you're using OpsGenie, you should plan your migration to:

- **Jira Service Management** - For incident management and alerting
- **Compass** - For service and dependency management

This documentation is provided for reference and to support existing OpsGenie deployments during the transition period.

**Source:** https://docs.opsgenie.com/

---

## Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [API Reference](#api-reference)
4. [Alert Management](#alert-management-overview)
5. [On-Call Scheduling](#on-call-scheduling-overview)
6. [Teams](#teams)
7. [CLI (Lamp)](#cli-lamp)
8. [Integrations](#integrations)
9. [Migration Guide](#migration-guide)

---

## Overview

OpsGenie is an alert and on-call management platform designed to help teams respond to incidents and operational alerts efficiently. It aggregates alerts from multiple sources, routes them intelligently, and coordinates on-call schedules to ensure the right person is notified at the right time.

### Key Features

- **Alert Aggregation** - Centralize alerts from monitoring systems, applications, and services
- **Smart Routing** - Route alerts to the right teams and individuals based on escalation policies
- **On-Call Management** - Schedule on-call shifts across teams with automatic escalations
- **Collaboration** - Built-in chat and communication features for incident resolution
- **Integrations** - Native integrations with 200+ tools including Datadog, PagerDuty, AWS, etc.
- **Mobile Apps** - iOS and Android apps for on-the-go alert management
- **API & CLI** - Programmatic access via REST API and command-line interface
- **Analytics** - Track alerting trends, incident response times, and team metrics

---

## Getting Started

### Account Setup

1. Create OpsGenie account at https://www.atlassian.com/software/opsgenie
2. Configure your organization details
3. Set up teams and add team members
4. Create notification rules
5. Integrate with your monitoring tools

### Navigation

The OpsGenie dashboard provides access to:

- **Dashboard** - Overview of current incidents and alerts
- **Alerts** - Searchable alert history and status
- **Incidents** - Incident management and tracking
- **On-Call** - Schedule management and on-call rotations
- **Teams** - Team management and configuration
- **Integrations** - Connected tools and data sources
- **Settings** - Account, user, and notification preferences

### First Alert

To test your setup:

1. Go to Settings > Team Settings
2. Create a test alert via API:

   ```bash
   curl -X POST https://api.opsgenie.com/v2/alerts \
     -H "Authorization: GenieKey YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Test Alert",
       "description": "This is a test alert",
       "priority": "P3"
     }'
   ```

3. Verify you receive the notification

---

## API Reference

### Authentication

All API requests require an API Key. Include it in the `Authorization` header:

```text
Authorization: GenieKey YOUR_API_KEY
```

Get your API key from Settings > API Key Management.

### Base URL

```text
https://api.opsgenie.com/v2
```

For EU region:

```text
https://api.eu.opsgenie.com/v2
```

### Common Response Format

All API responses follow this format:

```json
{
  "data": {
    "id": "...",
    "name": "..."
  },
  "took": 100,
  "requestId": "..."
}
```

### Alerts API

#### Create Alert

```text
POST /alerts
```

**Request Body:**

```json
{
  "message": "Alert Title",
  "description": "Alert description",
  "priority": "P1",
  "responders": [
    {
      "type": "user",
      "id": "user_id"
    }
  ],
  "tags": ["tag1", "tag2"],
  "details": {
    "custom_field": "value"
  }
}
```

**Response:**

```json
{
  "data": {
    "alertId": "4514d325-1e92-4ecd-a8d5-8f56892c9db1"
  },
  "took": 100,
  "requestId": "..."
}
```

#### Get Alert

```text
GET /alerts/{alertId}
```

#### Close Alert

```text
POST /alerts/{alertId}/close
```

#### Acknowledge Alert

```text
POST /alerts/{alertId}/acknowledge
```

#### List Alerts

```text
GET /alerts
```

Query parameters:

- `query` - Alert query filter
- `limit` - Number of results (default: 20, max: 100)
- `offset` - Pagination offset
- `sort` - Sort order (createdAt, updatedAt)
- `order` - asc or desc

#### Add Note to Alert

```text
POST /alerts/{alertId}/notes
```

**Request Body:**

```json
{
  "note": "Note text"
}
```

#### Add Responder to Alert

```text
POST /alerts/{alertId}/responders
```

**Request Body:**

```json
{
  "responder": {
    "type": "user",
    "id": "user_id"
  }
}
```

### Incidents API

#### Create Incident

```text
POST /incidents
```

**Request Body:**

```json
{
  "title": "Incident Title",
  "description": "Incident description",
  "priority": "P1",
  "responders": [
    {
      "type": "team",
      "id": "team_id"
    }
  ]
}
```

#### Get Incident

```text
GET /incidents/{incidentId}
```

#### List Incidents

```text
GET /incidents
```

#### Update Incident Status

```text
PATCH /incidents/{incidentId}
```

**Request Body:**

```json
{
  "status": "resolved",
  "statusPageVisibility": "public"
}
```

Valid status values:

- open
- acknowledged
- in_mitigation
- monitoring
- resolved
- resolved_with_mitigation
- closed
- declined

### Teams API

#### Create Team

```text
POST /teams
```

**Request Body:**

```json
{
  "name": "Team Name",
  "description": "Team description"
}
```

#### Get Team

```text
GET /teams/{teamId}
```

#### List Teams

```text
GET /teams
```

#### Add Member to Team

```text
POST /teams/{teamId}/members
```

**Request Body:**

```json
{
  "user": {
    "username": "user@example.com"
  }
}
```

#### Remove Member from Team

```text
DELETE /teams/{teamId}/members/{memberId}
```

### On-Call API

#### Get On-Call Data

```text
GET /schedules/{scheduleId}/on-calls
```

Query parameters:

- `flat` - Return flat user list (true/false)

#### Get Schedule

```text
GET /schedules/{scheduleId}
```

#### List Schedules

```text
GET /schedules
```

#### Create Schedule

```text
POST /schedules
```

**Request Body:**

```json
{
  "name": "On-Call Schedule",
  "timezone": "America/New_York",
  "description": "24x7 support rotation"
}
```

### Users API

#### Get User

```text
GET /users/{userId}
```

#### List Users

```text
GET /users
```

#### Create User

```text
POST /users
```

**Request Body:**

```json
{
  "username": "user@example.com",
  "fullName": "John Doe",
  "role": "user"
}
```

#### Update User

```text
PATCH /users/{userId}
```

---

## Alert Management (Overview)

### Creating Alerts

#### Via UI

1. Click "Create Alert" on the dashboard
2. Fill in the alert details:
   - Message (required)
   - Description
   - Priority (P1-P5)
   - Responders
   - Tags
   - Custom fields
3. Click "Create"

#### Via API

```bash
curl -X POST https://api.opsgenie.com/v2/alerts \
  -H "Authorization: GenieKey YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Service Down",
    "description": "Payment service is unavailable",
    "priority": "P1",
    "responders": [
      {
        "type": "team",
        "id": "platform-team-id"
      }
    ]
  }'
```

#### Via Integration

Most monitoring tools (Datadog, Prometheus, New Relic, etc.) have native OpsGenie integrations. Configure the integration webhook to send alerts automatically.

### Alert Routing

Alerts are routed based on:

1. **Team Assignment** - Alert specifies which team should respond
2. **On-Call Schedule** - Alert goes to team member who is on-call
3. **Escalation Policy** - If primary recipient doesn't acknowledge, escalate
4. **Notification Rules** - Customer notification preferences override routing

### Alert Acknowledgment

Team members acknowledge alerts to indicate they're working on the issue:

```bash
curl -X POST https://api.opsgenie.com/v2/alerts/ALERT_ID/acknowledge \
  -H "Authorization: GenieKey YOUR_API_KEY"
```

### Alert Closing

Close alerts when the issue is resolved:

```bash
curl -X POST https://api.opsgenie.com/v2/alerts/ALERT_ID/close \
  -H "Authorization: GenieKey YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "note": "Issue resolved, all systems operational"
  }'
```

---

## On-Call Scheduling (Overview)

### Creating Schedules

1. Go to On-Call > Schedules
2. Click "Create Schedule"
3. Configure:
   - Name and description
   - Timezone
   - Rotation type (daily, weekly, monthly)
   - Team members
   - Start date and rotation duration

### Rotation Types

- **Daily** - Changes every 24 hours
- **Weekly** - Changes on specific day each week
- **Bi-weekly** - Changes every 2 weeks
- **Monthly** - Changes on specific day each month
- **Custom** - Define custom rotation patterns

### Escalation Policies

Create escalation policies to handle unacknowledged alerts:

1. Go to Settings > Escalation
2. Click "Create Escalation Policy"
3. Define escalation rules:
   - First responder (on-call member)
   - Escalation delay (e.g., 5 minutes)
   - Second responder
   - Additional escalation steps

### Example Escalation Policy

```text
Alert created
    ↓
Notify primary on-call (5 min delay)
    ↓ (if unacknowledged)
Notify backup on-call (5 min delay)
    ↓ (if unacknowledged)
Notify team manager
```

---

## Teams

### Team Management (Teams Section)

#### Create Team via UI

1. Go to Teams
2. Click "Create Team"
3. Enter team details:
   - Team name
   - Description
   - Team members
4. Click "Create"

#### Team Settings

- **Notification Rules** - How team members receive alerts
- **Escalation Policy** - Default escalation for team alerts
- **Schedule** - Team's on-call schedule
- **Integration** - Team-specific integrations

### Team Members

#### Add Member

1. Go to Team > Members
2. Click "Add Member"
3. Select user and role:
   - Admin - Can manage team settings
   - User - Can view and manage alerts
4. Click "Add"

#### Member Roles

- **Admin** - Full team management access
- **User** - Can acknowledge and manage team alerts
- **Guest** - Read-only access

### Team Permissions

Teams can be granted permissions to:

- View specific alerts
- Create incidents
- Access integrations
- Manage on-call schedules
- Configure notification rules

---

## CLI (Lamp)

OpsGenie provides a command-line interface called Lamp for managing alerts and incidents from the terminal.

### Installation

#### macOS

```bash
brew tap opsgenie/lamp
brew install lamp
```

#### Linux

```bash
wget https://github.com/opsgenie/opsgenie-lamp/releases/download/v1.x.x/lamp-1.x.x-linux-amd64.tar.gz
tar xzf lamp-1.x.x-linux-amd64.tar.gz
sudo mv lamp /usr/local/bin/
```

#### Windows

Download the executable from GitHub releases and add to PATH.

### Configuration

1. Get your API key from OpsGenie UI
2. Configure Lamp:

```bash
lamp config set apiKey YOUR_API_KEY
lamp config set region us  # or eu
```

### Commands

#### Alert Commands

```bash
# Create alert
lamp alert create --message "Service Down" --priority P1

# List alerts
lamp alert list

# Close alert
lamp alert close --id ALERT_ID

# Acknowledge alert
lamp alert acknowledge --id ALERT_ID

# Add note
lamp alert add-note --id ALERT_ID --note "Update note"
```

#### Incident Commands

```bash
# Create incident
lamp incident create --title "Production Issue" --priority P1

# List incidents
lamp incident list

# Close incident
lamp incident close --id INCIDENT_ID

# Get incident details
lamp incident get --id INCIDENT_ID
```

#### On-Call Commands

```bash
# Get on-call user
lamp on-call get --schedule-id SCHEDULE_ID

# List on-call rotations
lamp on-call list --schedule-id SCHEDULE_ID
```

#### Heartbeat Commands

```bash
# Send heartbeat (for monitoring)
lamp heartbeat send --name heartbeat_name
```

---

## Integrations

OpsGenie integrates with 200+ tools and platforms:

### Monitoring & Observability

- **Datadog** - Send alerts from Datadog to OpsGenie
- **Prometheus** - AlertManager integration
- **New Relic** - Native integration
- **Grafana** - Send alerts to OpsGenie
- **AWS CloudWatch** - SNS to OpsGenie
- **Google Cloud Monitoring** - Pub/Sub integration
- **Azure Monitor** - Alert routing to OpsGenie

### Incident Management

- **PagerDuty** - Bidirectional integration
- **Jira** - Create incidents from alerts
- **ServiceNow** - Alert routing and ticketing
- **Linear** - Issue creation from alerts

### Communication

- **Slack** - Slash commands, incoming webhooks
- **Microsoft Teams** - Alert notifications
- **Discord** - Alert routing
- **Webhooks** - Custom integrations

### Setting Up Integrations

1. Go to Settings > Integrations
2. Search for desired integration
3. Click "Add Integration"
4. Configure credentials and routing rules
5. Test the integration
6. Save and activate

---

## Migration Guide

### Migrating from OpsGenie

Since OpsGenie is being discontinued, plan your migration to Jira Service Management:

#### Step 1: Export Data

Export your OpsGenie data:

```bash
# Use OpsGenie API to extract:
# - Teams and members
# - On-call schedules
# - Integration configurations
# - Alert history (last 90 days)
```

#### Step 2: Assess Jira Service Management

Jira Service Management provides:

- Incident management (similar to OpsGenie incidents)
- On-call scheduling
- Alert integration
- Team collaboration
- Reporting and analytics

#### Step 3: Migrate Integrations

Update your monitoring tools to send alerts to Jira Service Management instead of OpsGenie:

- Update webhook URLs
- Reconfigure API keys
- Test alert routing
- Update notification rules

#### Step 4: Train Teams

- Document new OpsGenie to JSM feature mapping
- Conduct training sessions
- Test incident response workflows
- Update runbooks and procedures

#### Step 5: Decommission OpsGenie

Once migration is complete:

- Archive OpsGenie account
- Verify all integrations are working in JSM
- Update documentation
- Communicate timeline to teams

---

## Best Practices

### Best Practices - Alert Management

1. **Avoid Alert Fatigue** - Tune alert thresholds to reduce false positives
2. **Clear Descriptions** - Provide context so responders understand the issue
3. **Appropriate Priorities** - Use P1-P5 consistently (P1: critical, P5: info)
4. **Regular Review** - Audit alert rules monthly to ensure relevance
5. **Correlation** - Group related alerts using tags and custom fields

### Best Practices - On-Call Scheduling

1. **Fair Rotation** - Distribute on-call duties evenly across team
2. **Overlap Periods** - Have handoff time between shifts
3. **Escalation Clarity** - Document who escalates to whom
4. **Time Zone Awareness** - Adjust schedules for distributed teams
5. **Regular Updates** - Keep schedules current and notify team

### Best Practices - Team Management

1. **Clear Responsibilities** - Define what each team responds to
2. **Documentation** - Create runbooks for common incidents
3. **Regular Training** - Keep team current on OpsGenie/JSM features
4. **On-Call Support** - Provide resources during on-call shifts
5. **Post-Mortems** - Review major incidents and improve processes

---

## Support and Resources

- **Official Docs** - https://docs.opsgenie.com/
- **Community** - https://community.atlassian.com/t5/OpsGenie/ct-p/opsgenie
- **API Docs** - https://docs.opsgenie.com/docs/api-overview
- **Status Page** - https://status.opsgenie.com/
- **Blog** - https://www.atlassian.com/blog/opsgenie

### Getting Help

- Check documentation and community forums first
- For bugs, contact Atlassian Support
- Discuss migration timeline with your Atlassian representative
- Review Jira Service Management documentation for feature parity

---

## Changelog & Version History

OpsGenie has reached end of support. For feature updates and bug fixes, refer to Jira Service Management release notes.

This documentation is current as of February 2026 and reflects OpsGenie's final stable version.
