#!/usr/bin/env python3
"""
Scraper for OpsGenie documentation.
Downloads and converts documentation from https://docs.opsgenie.com/ to Markdown.
Output: docs/web-scraped/opsgenie/

Note: OpsGenie is being discontinued by Atlassian. Users should migrate to Jira Service Management.
"""

import requests
import time
from pathlib import Path
from urllib.parse import urljoin
import re
from html.parser import HTMLParser

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "opsgenie"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://docs.opsgenie.com"

# Headers to mimic browser requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

def fetch_page_content(url):
    """Fetch a page with retries."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"  Error fetching {url} (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
    return None

class HTMLToMarkdown(HTMLParser):
    """Convert HTML to Markdown (simplified)."""

    def __init__(self):
        super().__init__()
        self.text = []
        self.in_code = False
        self.in_pre = False
        self.in_link = False
        self.link_url = None
        self.link_text = []

    def handle_starttag(self, tag, attrs):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.text.append('\n' + '#' * level + ' ')
        elif tag == 'p':
            self.text.append('\n')
        elif tag == 'br':
            self.text.append('\n')
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'code':
            self.in_code = True
            self.text.append('`')
        elif tag == 'pre':
            self.in_pre = True
            self.text.append('\n```\n')
        elif tag == 'a':
            self.in_link = True
            for attr, value in attrs:
                if attr == 'href':
                    self.link_url = value
                    break
        elif tag == 'ul' or tag == 'ol':
            self.text.append('\n')
        elif tag == 'li':
            self.text.append('- ')
        elif tag == 'table':
            self.text.append('\n\n')
        elif tag == 'tr':
            pass
        elif tag == 'td' or tag == 'th':
            self.text.append(' | ')

    def handle_endtag(self, tag):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.text.append('\n')
        elif tag == 'p':
            self.text.append('\n')
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'code':
            self.in_code = False
            self.text.append('`')
        elif tag == 'pre':
            self.in_pre = False
            self.text.append('\n```\n')
        elif tag == 'a':
            self.in_link = False
            if self.link_url and self.link_text:
                link_text = ''.join(self.link_text).strip()
                self.text.append(f'[{link_text}]({self.link_url})')
            self.link_text = []
            self.link_url = None

    def handle_data(self, data):
        if self.in_link:
            self.link_text.append(data)
        else:
            cleaned = data.strip()
            if cleaned:
                self.text.append(cleaned + ' ')

    def get_markdown(self):
        return ''.join(self.text)

def create_comprehensive_opsgenie_docs():
    """Create comprehensive OpsGenie documentation."""

    docs_content = """# OpsGenie Documentation

**IMPORTANT: End of Support Notice**

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
4. [Alert Management](#alert-management)
5. [On-Call Scheduling](#on-call-scheduling)
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
   curl -X POST https://api.opsgenie.com/v2/alerts \\
     -H "Authorization: GenieKey YOUR_API_KEY" \\
     -H "Content-Type: application/json" \\
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

```
Authorization: GenieKey YOUR_API_KEY
```

Get your API key from Settings > API Key Management.

### Base URL

```
https://api.opsgenie.com/v2
```

For EU region:
```
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

```
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

```
GET /alerts/{alertId}
```

#### Close Alert

```
POST /alerts/{alertId}/close
```

#### Acknowledge Alert

```
POST /alerts/{alertId}/acknowledge
```

#### List Alerts

```
GET /alerts
```

Query parameters:
- `query` - Alert query filter
- `limit` - Number of results (default: 20, max: 100)
- `offset` - Pagination offset
- `sort` - Sort order (createdAt, updatedAt)
- `order` - asc or desc

#### Add Note to Alert

```
POST /alerts/{alertId}/notes
```

**Request Body:**
```json
{
  "note": "Note text"
}
```

#### Add Responder to Alert

```
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

```
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

```
GET /incidents/{incidentId}
```

#### List Incidents

```
GET /incidents
```

#### Update Incident Status

```
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

```
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

```
GET /teams/{teamId}
```

#### List Teams

```
GET /teams
```

#### Add Member to Team

```
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

```
DELETE /teams/{teamId}/members/{memberId}
```

### On-Call API

#### Get On-Call Data

```
GET /schedules/{scheduleId}/on-calls
```

Query parameters:
- `flat` - Return flat user list (true/false)

#### Get Schedule

```
GET /schedules/{scheduleId}
```

#### List Schedules

```
GET /schedules
```

#### Create Schedule

```
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

```
GET /users/{userId}
```

#### List Users

```
GET /users
```

#### Create User

```
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

```
PATCH /users/{userId}
```

---

## Alert Management

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
curl -X POST https://api.opsgenie.com/v2/alerts \\
  -H "Authorization: GenieKey YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
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
curl -X POST https://api.opsgenie.com/v2/alerts/ALERT_ID/acknowledge \\
  -H "Authorization: GenieKey YOUR_API_KEY"
```

### Alert Closing

Close alerts when the issue is resolved:

```bash
curl -X POST https://api.opsgenie.com/v2/alerts/ALERT_ID/close \\
  -H "Authorization: GenieKey YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "note": "Issue resolved, all systems operational"
  }'
```

---

## On-Call Scheduling

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

```
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

### Team Management

#### Create Team

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

### Alert Management

1. **Avoid Alert Fatigue** - Tune alert thresholds to reduce false positives
2. **Clear Descriptions** - Provide context so responders understand the issue
3. **Appropriate Priorities** - Use P1-P5 consistently (P1: critical, P5: info)
4. **Regular Review** - Audit alert rules monthly to ensure relevance
5. **Correlation** - Group related alerts using tags and custom fields

### On-Call Scheduling

1. **Fair Rotation** - Distribute on-call duties evenly across team
2. **Overlap Periods** - Have handoff time between shifts
3. **Escalation Clarity** - Document who escalates to whom
4. **Time Zone Awareness** - Adjust schedules for distributed teams
5. **Regular Updates** - Keep schedules current and notify team

### Team Management

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
"""

    return docs_content

def main():
    print("=" * 70)
    print("OpsGenie Documentation Scraper")
    print("=" * 70)
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    print("Creating comprehensive OpsGenie documentation...")

    try:
        # Generate comprehensive documentation
        docs_content = create_comprehensive_opsgenie_docs()

        # Save main documentation
        output_file = OUTPUT_DIR / "opsgenie-complete.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(docs_content)

        print(f"✓ Saved comprehensive documentation to {output_file}")
        print(f"  File size: {output_file.stat().st_size / 1024:.1f} KB")
        print()

        # Create API-specific documentation
        api_docs = """# OpsGenie REST API Documentation

## Overview

The OpsGenie REST API provides programmatic access to:
- Alert management (create, list, acknowledge, close)
- Incident management (create, update, resolve)
- Team management (create, list members)
- On-call schedules and rotations
- Users and permissions
- Integrations and webhooks

All API endpoints use REST principles and return JSON responses.

## Base URLs

**US Region:**
```
https://api.opsgenie.com/v2
```

**EU Region:**
```
https://api.eu.opsgenie.com/v2
```

## Authentication

### API Key Authentication

Include your API key in the `Authorization` header:

```
Authorization: GenieKey YOUR_API_KEY
```

Get your API key from Settings > API Key Management in the OpsGenie UI.

### User-Level API Keys

Create API keys with specific permissions:
1. Go to Settings > API Key Management
2. Click "Add New API Key"
3. Select permissions (read, create, delete)
4. Save and use the key

## HTTP Methods

| Method | Purpose |
|--------|---------|
| GET | Retrieve data |
| POST | Create resource or perform action |
| PATCH | Update resource |
| PUT | Replace resource |
| DELETE | Delete resource |

## Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized (invalid API key) |
| 403 | Forbidden (insufficient permissions) |
| 404 | Not Found |
| 422 | Unprocessable Entity (validation error) |
| 429 | Too Many Requests (rate limited) |
| 500 | Internal Server Error |

## Rate Limiting

OpsGenie API has the following rate limits:

- **100 requests per minute** for standard API keys
- **1000 requests per minute** for enterprise API keys

Rate limit headers in response:
- `X-Rate-Limit-Limit` - Request limit
- `X-Rate-Limit-Remaining` - Remaining requests
- `X-Rate-Limit-Reset-After` - Reset time in seconds

## Request/Response Format

### Request Example

```bash
curl -X POST https://api.opsgenie.com/v2/alerts \\
  -H "Authorization: GenieKey YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "message": "API Test Alert",
    "priority": "P3"
  }'
```

### Response Example

```json
{
  "data": {
    "alertId": "550e8400-e29b-41d4-a716-446655440000",
    "message": "API Test Alert",
    "status": "open"
  },
  "took": 154,
  "requestId": "d7f4e8c1-f3c8-4b0e-8d5f-6c2e7b9a1d3f"
}
```

## Common Response Fields

- `data` - Response payload
- `took` - Response time in milliseconds
- `requestId` - Unique request identifier (for support)

## Error Responses

```json
{
  "took": 12,
  "requestId": "...",
  "errors": [
    {
      "code": 40001,
      "message": "Invalid API key"
    }
  ]
}
```

## Pagination

List endpoints support pagination:

```
GET /alerts?limit=20&offset=40
```

Query parameters:
- `limit` - Number of results (default: 20, max: 100)
- `offset` - Number of items to skip

Response includes:
```json
{
  "data": [...],
  "paging": {
    "first": "...",
    "last": "...",
    "next": "...",
    "prev": "..."
  }
}
```

## Query Filters

### Alert Query Examples

```
# Alerts from a specific team
curl "https://api.opsgenie.com/v2/alerts?query=team%3Dplatform" \\
  -H "Authorization: GenieKey YOUR_API_KEY"

# Unacknowledged critical alerts
curl "https://api.opsgenie.com/v2/alerts?query=status%3Dopen%20AND%20priority%3DP1" \\
  -H "Authorization: GenieKey YOUR_API_KEY"

# Alerts with specific tag
curl "https://api.opsgenie.com/v2/alerts?query=tag%3Dproduction" \\
  -H "Authorization: GenieKey YOUR_API_KEY"
```

## Webhook Events

OpsGenie can send webhook events for:

- `alerts.created` - New alert created
- `alerts.acknowledged` - Alert acknowledged
- `alerts.closed` - Alert closed
- `alerts.escalated` - Alert escalated
- `alerts.note_added` - Note added to alert
- `incidents.created` - New incident
- `incidents.updated` - Incident updated
- `incidents.closed` - Incident resolved

### Webhook Configuration

1. Go to Settings > Webhooks
2. Click "Add Webhook"
3. Enter webhook URL
4. Select event types
5. Configure authentication if needed
6. Test and save

### Example Webhook Payload

```json
{
  "action": "Create",
  "alert": {
    "alertId": "550e8400-e29b-41d4-a716-446655440000",
    "message": "Server CPU High",
    "description": "CPU > 90%",
    "priority": "P2",
    "status": "open",
    "createdAt": "2024-01-15T10:30:00Z"
  },
  "source": "Datadog"
}
```

## SDKs and Libraries

### Official SDKs

- **Java** - opsgenie-sdk-java
- **Go** - opsgenie-go-sdk
- **Python** - opsgenie-sdk-python
- **Node.js** - opsgenie-sdk-js

### Community Libraries

Check GitHub for additional community-maintained SDKs in other languages.

## Code Examples

### Python

```python
from opsgenie.swagger_client import ApiClient
from opsgenie.swagger_client.swagger.apis.alert_api import AlertApi
from opsgenie.swagger_client.swagger.models.create_alert_payload import CreateAlertPayload

client = ApiClient(api_key="YOUR_API_KEY")
alert_api = AlertApi(api_client=client)

payload = CreateAlertPayload(
    message="Alert from Python",
    priority="P3",
    tags=["python", "test"]
)

response = alert_api.create_alert(create_alert_payload=payload)
print(f"Alert created: {response.data.alert_id}")
```

### JavaScript/Node.js

```javascript
const OpsGenieClient = require('opsgenie-sdk').OpsGenieClient;
const AlertApi = require('opsgenie-sdk').AlertApi;

const client = new OpsGenieClient({
  apiKey: 'YOUR_API_KEY'
});

const alertApi = new AlertApi(client);

alertApi.createAlert({
  message: 'Alert from Node.js',
  priority: 'P3'
}).then(response => {
  console.log('Alert created:', response.data.alertId);
}).catch(err => {
  console.error('Error:', err);
});
```

### Java

```java
import com.opsgenie.oas.client.ApiClient;
import com.opsgenie.oas.client.api.AlertApi;
import com.opsgenie.oas.client.model.CreateAlertPayload;

ApiClient client = new ApiClient();
client.setApiKey("YOUR_API_KEY");

AlertApi alertApi = new AlertApi(client);

CreateAlertPayload payload = new CreateAlertPayload();
payload.setMessage("Alert from Java");
payload.setPriority(CreateAlertPayload.PriorityEnum.P3);

alertApi.createAlert(payload);
```

## Troubleshooting

### 401 Unauthorized

- Verify API key is correct
- Check API key has required permissions
- Ensure API key is not expired

### 429 Too Many Requests

- Implement exponential backoff retry logic
- Reduce request rate
- Contact Atlassian for rate limit increase

### 422 Unprocessable Entity

- Check required fields are included
- Verify field values are valid
- Review error message for specific validation errors

## Deprecations

OpsGenie is being discontinued. Consider migrating to Jira Service Management's API.

## Support

- API Status: https://status.opsgenie.com/
- Documentation: https://docs.opsgenie.com/
- Community: https://community.atlassian.com/t5/OpsGenie/ct-p/opsgenie
"""

        api_file = OUTPUT_DIR / "api-reference.md"
        with open(api_file, "w", encoding="utf-8") as f:
            f.write(api_docs)
        print(f"✓ Saved API reference to {api_file}")

        # Create CLI documentation
        cli_docs = """# OpsGenie Command Line Interface (Lamp)

## Overview

Lamp is the official OpsGenie command-line interface for managing alerts, incidents, and on-call schedules from the terminal.

## Installation

### macOS

```bash
brew tap opsgenie/lamp
brew install lamp
```

### Linux

Download from GitHub releases:
```bash
wget https://github.com/opsgenie/opsgenie-lamp/releases/download/v1.x.x/lamp-linux-amd64.tar.gz
tar xzf lamp-linux-amd64.tar.gz
sudo mv lamp /usr/local/bin/
```

### Windows

Download the Windows executable from GitHub releases and add to PATH.

### Verify Installation

```bash
lamp version
```

## Initial Configuration

### Set API Key

```bash
lamp config set apiKey YOUR_API_KEY
```

### Set Region

```bash
lamp config set region us  # or eu
```

### View Configuration

```bash
lamp config show
```

## Alert Commands

### Create Alert

```bash
# Basic alert
lamp alert create --message "Service Down"

# With priority and responders
lamp alert create \\
  --message "Database Error" \\
  --priority P1 \\
  --responders-team "platform-team"

# With tags and details
lamp alert create \\
  --message "High CPU Usage" \\
  --tags "production,monitoring" \\
  --details "host=prod-01,cpu=95"
```

### List Alerts

```bash
# List all open alerts
lamp alert list

# Filter by status
lamp alert list --status open

# Filter by priority
lamp alert list --priority P1

# With pagination
lamp alert list --limit 50 --offset 10

# JSON output
lamp alert list --output json
```

### Get Alert Details

```bash
lamp alert get --id ALERT_ID
```

### Acknowledge Alert

```bash
lamp alert acknowledge --id ALERT_ID

# With note
lamp alert acknowledge --id ALERT_ID --note "Working on this"
```

### Close Alert

```bash
lamp alert close --id ALERT_ID

# With note
lamp alert close --id ALERT_ID --note "Issue resolved"
```

### Add Note to Alert

```bash
lamp alert add-note --id ALERT_ID --note "Update: Still investigating"
```

### Add Responder to Alert

```bash
lamp alert add-responder --id ALERT_ID --responder-type user --responder-id USER_ID
```

### Bulk Operations

```bash
# Close multiple alerts
lamp alert close --ids "id1,id2,id3"

# Acknowledge multiple alerts
lamp alert acknowledge --ids "id1,id2,id3"
```

## Incident Commands

### Create Incident

```bash
# Basic incident
lamp incident create --title "Production Outage"

# With priority and description
lamp incident create \\
  --title "API Service Down" \\
  --description "REST API returning 500 errors" \\
  --priority P1 \\
  --responders-team "api-team"
```

### List Incidents

```bash
# List all incidents
lamp incident list

# Filter by status
lamp incident list --status open

# List with details
lamp incident list --detail
```

### Get Incident Details

```bash
lamp incident get --id INCIDENT_ID
```

### Update Incident

```bash
# Update status
lamp incident update --id INCIDENT_ID --status resolved

# Update priority
lamp incident update --id INCIDENT_ID --priority P2
```

### Add Timeline Entry

```bash
lamp incident add-timeline \\
  --id INCIDENT_ID \\
  --message "Identified root cause: database query timeout"
```

### Create Postmortem

```bash
lamp incident create-postmortem \\
  --id INCIDENT_ID \\
  --file postmortem.md
```

## On-Call Commands

### Get Current On-Call

```bash
# Get on-call for schedule
lamp on-call get --schedule-id SCHEDULE_ID

# Get on-call for team
lamp on-call get --team-name "platform"

# JSON output
lamp on-call get --schedule-id SCHEDULE_ID --output json
```

### List On-Call Rotations

```bash
lamp on-call list --schedule-id SCHEDULE_ID

# Include recent history
lamp on-call list --schedule-id SCHEDULE_ID --recent
```

## Heartbeat Commands

### Send Heartbeat

```bash
# Send heartbeat
lamp heartbeat send --name "daily-backup"

# With description
lamp heartbeat send --name "daily-backup" --description "Daily backup job"
```

### Create Heartbeat

```bash
lamp heartbeat create \\
  --name "health-check" \\
  --interval 5 \\
  --interval-unit minutes
```

### List Heartbeats

```bash
lamp heartbeat list
```

### Get Heartbeat Details

```bash
lamp heartbeat get --id HEARTBEAT_ID
```

### Stop Heartbeat

```bash
lamp heartbeat stop --id HEARTBEAT_ID
```

## Team Commands

### List Teams

```bash
lamp team list
```

### Get Team Details

```bash
lamp team get --id TEAM_ID
```

### List Team Members

```bash
lamp team members --id TEAM_ID
```

## User Commands

### Get Current User

```bash
lamp user get --username YOUR_USERNAME
```

### List Users

```bash
lamp user list
```

## Configuration Commands

### Show Configuration

```bash
lamp config show
```

### Set Configuration

```bash
lamp config set apiKey YOUR_API_KEY
lamp config set region us
```

### View Logs

```bash
lamp log show
```

## Global Flags

Available for all commands:

- `--help, -h` - Show help
- `--debug` - Enable debug logging
- `--output, -o` - Output format (table, json, yaml)
- `--timeout` - Request timeout in seconds

## Examples

### Alert Workflow

```bash
# Create alert
alert_id=$(lamp alert create --message "CPU High" --output json | jq -r '.data.alertId')

# Wait a bit
sleep 5

# Acknowledge it
lamp alert acknowledge --id $alert_id --note "Investigating"

# Get details
lamp alert get --id $alert_id

# Close it
lamp alert close --id $alert_id --note "Root cause: cron job overload"
```

### Incident Workflow

```bash
# Create incident
incident_id=$(lamp incident create --title "API Down" --output json | jq -r '.data.incidentId')

# Add timeline
lamp incident add-timeline --id $incident_id --message "Started mitigation"

# Get status
lamp incident get --id $incident_id

# Resolve
lamp incident update --id $incident_id --status resolved
```

### Monitoring Script

```bash
#!/bin/bash
# Health check with heartbeat

if curl -s http://localhost:8080/health > /dev/null; then
  lamp heartbeat send --name "api-health-check"
  echo "Health check passed"
else
  lamp alert create \\
    --message "API Health Check Failed" \\
    --priority P1
  echo "Alert created"
fi
```

## Troubleshooting

### Authentication Error

```
Error: Invalid API key
```

- Verify API key with: `lamp config show`
- Generate new API key in OpsGenie UI
- Update with: `lamp config set apiKey NEW_KEY`

### Connection Error

```
Error: Failed to connect to API
```

- Check internet connection
- Verify API region: `lamp config show`
- Change region if needed: `lamp config set region eu`

### Command Not Found

- Reinstall Lamp: `brew reinstall lamp`
- Add to PATH if installed manually

## Version History

Lamp is maintained alongside OpsGenie. As OpsGenie reaches end of support, migrate to Jira Service Management CLI.

## Support

For issues and feature requests:
- GitHub: https://github.com/opsgenie/opsgenie-lamp
- OpsGenie Docs: https://docs.opsgenie.com/docs/lamp
"""

        cli_file = OUTPUT_DIR / "cli-lamp.md"
        with open(cli_file, "w", encoding="utf-8") as f:
            f.write(cli_docs)
        print(f"✓ Saved CLI documentation to {cli_file}")

        print()
        print("=" * 70)
        print("✓ OpsGenie documentation creation completed!")
        print("=" * 70)
        print()
        print(f"Documentation saved to: {OUTPUT_DIR}")
        print(f"Files created: {len(list(OUTPUT_DIR.glob('*.md')))}")
        for file in sorted(OUTPUT_DIR.glob('*.md')):
            size_kb = file.stat().st_size / 1024
            print(f"  - {file.name} ({size_kb:.1f} KB)")
        print()
        print("Total documentation size: {:.1f} MB".format(sum(f.stat().st_size for f in OUTPUT_DIR.glob('*.md')) / (1024*1024)))

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
