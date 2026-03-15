# Source: https://docs.firehydrant.com/docs/heartbeat-monitoring.md

# Heartbeat Monitoring

Heartbeat monitoring allows you to ensure your services and scheduled jobs are running as expected. By configuring heartbeat endpoints in FireHydrant, your services can "check in" at regular intervals. If a service fails to check in within the expected timeframe, FireHydrant automatically creates an alert to notify your team.

Heartbeats support both HTTP and email-based check-ins, giving you flexibility in how your services communicate their health status.

## Create a Heartbeat

### Creating a Heartbeat

Navigate to **Signals > Sources > Heartbeats** and then click **"+ New Heartbeat"** in the top right.

You'll be guided through a multi-step form to configure your heartbeat endpoint:

### Step 1: Basic Information

Configure the fundamental settings for your heartbeat:

**Slug** (required) - A unique identifier used in the endpoint URL. Use alphanumeric characters and hyphens only. For example: `my-service-heartbeat` or `daily-backup-job`.

**Enabled** - Toggle to enable or disable this heartbeat endpoint. Disabled heartbeats will not monitor for check-ins or generate alerts.

**Description** (optional) - Provide additional context about what this heartbeat monitors, such as "Monitors the daily backup job that runs at 2 AM UTC."

### Step 2: Heartbeat Configuration

Configure how the heartbeat behaves and what incoming requests it accepts.

**Expected Interval** (required) - Specify how long to wait after the last check-in before considering the service offline and generating an alert. The interval must be between 5 minutes and 24 hours. Choose an interval that gives your service enough time between check-ins with some buffer for normal variance.

**Kind** (required) - Select whether this heartbeat creates an HTTP or email endpoint:

**HTTP** - Your service will send HTTP requests to a unique URL
**Email** - Your service will send emails to a unique email address

#### HTTP-Specific Configuration

When you select HTTP as the kind, you'll configure:

**Allowed HTTP Methods** - Select which HTTP methods can be used to ping this heartbeat endpoint. Common choices include GET, POST, PUT, PATCH, and DELETE. POST is the default selection, but if you don't specify methods, all methods are allowed.

**User-Agent Substring** (optional) - If specified, the User-Agent header of incoming requests must contain this substring. This provides an additional layer of validation to ensure requests are coming from your service. For example, enter `my-service-client` to only accept requests with that string in the User-Agent header.

#### Email-Specific Configuration

When you select Email as the kind, you'll configure:

**Allowed Email Senders** (optional) - A comma-separated list of email addresses that are allowed to trigger a check-in. Emails from other senders will be ignored. You can use domain patterns by prefixing with `@`, such as `@example.com` to allow all emails from that domain. Leave blank to allow emails from any sender.

Example: `monitoring@example.com, @monitoring-service.io`

### Step 3: Signal Template

Configure the signal that will be generated when the heartbeat is missed. This template defines what the alert will look like when your service fails to check in.

**Body** (optional) - The main message text for the alert. This should provide clear context about what failed to check in. The body supports markdown formatting.

Example: `The daily backup job has not checked in within the expected interval. This may indicate the job failed to run or completed with errors.`

**Tags** (optional) - Add key-value pairs to categorize and filter alerts. Tags appear as `key:value` in the alert.

Example tags:

* `service:api`
* `priority:high`
* `component:data-pipeline`

**Annotations** (optional) - Add additional metadata as key-value pairs. Keys can only contain alphanumeric characters, hyphens, and underscores. Annotations provide structured data that can be used for filtering and automation.

Example annotations:

* `environment:production`
* `runbook_url:https://wiki.example.com/backup-runbook`

**Links** (optional) - Add relevant URLs with descriptive text. These appear as clickable links in the alert.

Example links:

* Text: "Service Dashboard" / URL: `https://dashboard.example.com/backup-service`
* Text: "Runbook Documentation" / URL: `https://docs.example.com/runbooks/backup`

### Step 4: Rule Creation

Select the team that should be notified when this heartbeat generates an alert. The alert will be routed according to the team's escalation policies and notification preferences.

When you're finished configuring all steps, click **"Create Heartbeat"** to save your configuration.

## Using Your Heartbeat

Once created, you'll need to configure your service to check in with the heartbeat endpoint.

### For HTTP Heartbeats

After creating an HTTP heartbeat, you'll see the unique URL on the heartbeat detail page. Configure your service to send HTTP requests to this URL at regular intervals (more frequently than your configured expected interval).

Example using curl:

```bash
curl -X POST https://signals.firehydrant.io/v1/heartbeat/my-service-heartbeat
```

You can use any of the allowed HTTP methods you configured. Successful check-ins receive a 200 OK response. As long as FireHydrant receives a request within the expected interval, your heartbeat will remain "Online" and no alerts will be generated.

### For Email Heartbeats

After creating an email heartbeat, you'll see the unique email address on the heartbeat detail page. Configure your service to send emails to this address at regular intervals.

The email address will be in the format:

```
heartbeat.your-slug.organization-id@signals.email
```

The subject and body of the email don't matter—any email sent to this address from an allowed sender will count as a check-in. Configure your scheduled jobs or monitoring tools to send emails to this address when they complete successfully.

### Testing Your Heartbeat

After configuration, test your heartbeat by manually triggering a check-in from your service. You should see the "Last Received" timestamp update on the heartbeat detail page, and the status should show as "Online."

## Monitoring Heartbeat Status

View all your heartbeats by navigating to **Signals > Sources > Heartbeats**. The list shows each heartbeat's status and timing information.

### Status Indicators

**Online** (green) - The service has checked in recently and is operating normally. FireHydrant received a check-in within the expected interval.

**Offline** (red) - The service has not checked in within the expected interval. An alert has been generated using your configured signal template.

### Timing Information

**Last Received** - The timestamp of the most recent successful check-in from your service.

**Overdue At** - The calculated time when the heartbeat will be (or became) overdue. This is computed as the last received time plus the expected interval.

Click on any heartbeat to view detailed information, edit its configuration, or retrieve the endpoint URL or email address.

## What Happens When a Heartbeat is Missed

When a service fails to check in within the expected interval, FireHydrant automatically:

1. Changes the heartbeat status to "Offline"
2. Creates a new alert using the signal template you configured
3. Routes the alert to the specified team according to their escalation policy
4. Sends notifications to on-call team members based on their notification preferences

The generated alert will contain:

* The body text from your template
* All configured tags
* All configured annotations
* All configured links
* A reference to the heartbeat that triggered it
* Timing information about when the last check-in was received and when it became overdue

Once your service resumes checking in, the heartbeat status will automatically return to "Online." The alert created during the outage will remain open until manually resolved by your team.

## Best Practices

**Choose appropriate intervals** - Set your expected interval based on how frequently your service checks in, plus a reasonable buffer. For a job that runs every hour, consider an interval of 75-90 minutes to allow for normal variance in execution time.

**Use descriptive slugs** - Choose slugs that clearly identify the service or job being monitored, such as `api-health-check` or `nightly-backup-job` rather than generic names like `heartbeat-1`.

**Provide context in signal templates** - Write signal body text that helps responders understand what failed and where to start investigating. Include relevant service names, expected timing, and impact.

**Test after creation** - Always test your heartbeat after configuration to ensure your service can successfully check in and that the URL or email address is correct.

**Organize with tags** - Use consistent tagging schemes across your heartbeats to make filtering and searching easier. Common tags include service name, priority level, and component.

**Include runbook links** - Add links to relevant runbooks, dashboards, or documentation in your signal template so responders have immediate access to troubleshooting resources.

**Use domain patterns for email heartbeats** - If multiple services or email addresses might send check-ins, use the `@domain.com` pattern to allow all emails from your monitoring infrastructure's domain.

**Set realistic intervals for jobs** - For scheduled jobs (like backups or batch processes), set the expected interval to be at least twice the normal execution time to avoid false alerts due to longer-than-usual runs.

## Permissions

Users with the **manage\_event\_sources** permission can create, edit, and delete heartbeat endpoints.

Users with **Member** permissions can configure heartbeats within their teams. Users with **Owner** permissions can configure heartbeats for all teams regardless of membership.

For more information about permissions, visit Role-Based Access Controls.