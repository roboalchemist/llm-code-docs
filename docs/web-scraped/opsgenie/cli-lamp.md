# OpsGenie Command Line Interface (Lamp)

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
lamp alert create \
  --message "Database Error" \
  --priority P1 \
  --responders-team "platform-team"

# With tags and details
lamp alert create \
  --message "High CPU Usage" \
  --tags "production,monitoring" \
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
lamp incident create \
  --title "API Service Down" \
  --description "REST API returning 500 errors" \
  --priority P1 \
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
lamp incident add-timeline \
  --id INCIDENT_ID \
  --message "Identified root cause: database query timeout"
```

### Create Postmortem

```bash
lamp incident create-postmortem \
  --id INCIDENT_ID \
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
lamp heartbeat create \
  --name "health-check" \
  --interval 5 \
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
  lamp alert create \
    --message "API Health Check Failed" \
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
