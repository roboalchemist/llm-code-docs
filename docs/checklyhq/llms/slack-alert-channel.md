# Source: https://checklyhq.com/docs/constructs/slack-alert-channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SlackAlertChannel Construct

> Learn how to configure Slack alert channels with the Checkly CLI.

<Tip>
  Learn more about Slack alerts in [the Slack Alerts documentation](/integrations/alerts/slack).
</Tip>

Use Slack Alert Channels to send notifications to Slack channels when checks fail or recover. The examples below show how to configure Slack alerting for different scenarios.

<CodeGroup>
  ```ts Basic Example theme={null}
  import { SlackAlertChannel } from "checkly/constructs"

  const slackChannel = new SlackAlertChannel("slack-channel-1", {
    url: new URL(
      "https://hooks.slack.com/services/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"
    ),
    channel: "#ops",
  })
  ```

  ```ts Advanced Example theme={null}
  import { SlackAlertChannel } from "checkly/constructs"

  const slackChannel = new SlackAlertChannel("team-slack-channel", {
    url: new URL(
      "https://hooks.slack.com/services/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"
    ),
    channel: "#monitoring-alerts",
    sendRecovery: true,
    sendFailure: true,
    sendDegraded: true,
    sslExpiry: true,
    sslExpiryThreshold: 30,
  })
  ```
</CodeGroup>

## Configuration

<Tabs>
  <Tab title="Slack Alert Channel">
    Configure Slack-specific settings:

    | Parameter | Type     | Required | Default | Description                                  |
    | --------- | -------- | -------- | ------- | -------------------------------------------- |
    | `url`     | `URL`    | ✅        | -       | Slack webhook URL for incoming messages      |
    | `channel` | `string` | ❌        | -       | Target Slack channel (e.g., '#ops', '@user') |
  </Tab>

  <Tab title="General Alert Channel">
    Configure common alert channel properties:

    | Property             | Type      | Required | Default | Description                                              |
    | -------------------- | --------- | -------- | ------- | -------------------------------------------------------- |
    | `sendRecovery`       | `boolean` | ❌        | `true`  | Send notifications when checks recover                   |
    | `sendFailure`        | `boolean` | ❌        | `true`  | Send notifications when checks fail                      |
    | `sendDegrade`        | `boolean` | ❌        | `false` | Send notifications when checks degrade (API checks only) |
    | `sslExpiry`          | `boolean` | ❌        | `false` | Send notifications for SSL certificate expiry            |
    | `sslExpiryThreshold` | `number`  | ❌        | `30`    | Days before SSL expiry to send notification              |
  </Tab>
</Tabs>

### Slack Alert Channel Options

<ResponseField name="url" type="URL" required>
  Slack webhook URL for incoming messages. This is the endpoint where Checkly will send alert notifications.

  **Usage:**

  ```ts highlight={2-4} theme={null}
  new SlackAlertChannel("slack-channel", {
    url: new URL(
      "https://hooks.slack.com/services/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"
    ),
    channel: "#alerts",
  })
  ```

  Examples:

  <CodeGroup>
    ```ts Direct URL theme={null}
    const slackChannel = new SlackAlertChannel("direct-slack", {
      url: new URL(
        "https://hooks.slack.com/services/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"
      ),
      channel: "#monitoring",
    })
    ```

    ```ts Environment Variable theme={null}
    const secureSlack = new SlackAlertChannel("secure-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!), // Store securely
      channel: "#alerts",
    })
    ```

    ```ts Multiple Teams theme={null}
    // Different webhook URLs for different teams
    const devSlack = new SlackAlertChannel("dev-slack", {
      url: new URL(process.env.DEV_SLACK_WEBHOOK_URL!),
      channel: "#dev-alerts",
    })

    const opsSlack = new SlackAlertChannel("ops-slack", {
      url: new URL(process.env.OPS_SLACK_WEBHOOK_URL!),
      channel: "#ops-alerts",
    })
    ```
  </CodeGroup>

  **Use cases**: Team notifications, webhook integration, secure credential storage, multi-team alerting.
</ResponseField>

<ResponseField name="channel" type="string">
  Target Slack channel or user for notifications. Can override the default channel configured in the webhook.

  **Usage:**

  ```ts highlight={3} theme={null}
  new SlackAlertChannel("channel-slack", {
    url: new URL(process.env.SLACK_WEBHOOK_URL!),
    channel: "#ops", // Send to #ops channel
  })
  ```

  **Examples:**

  <CodeGroup>
    ```ts Channel Notifications theme={null}
    const channelSlack = new SlackAlertChannel("channel-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#monitoring-alerts", // Public channel
    })
    ```

    ```ts Direct Messages theme={null}
    const dmSlack = new SlackAlertChannel("dm-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "@john.doe", // Direct message to user
    })
    ```

    ```ts Different Channels for Different Purposes theme={null}
    const criticalSlack = new SlackAlertChannel("critical-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#critical-alerts",
    })

    const performanceSlack = new SlackAlertChannel("performance-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#performance-monitoring",
    })

    const securitySlack = new SlackAlertChannel("security-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#security-alerts",
    })
    ```
  </CodeGroup>

  **Use cases**: Team-specific alerts, direct notifications, alert categorization, noise management.
</ResponseField>

### General Alert Channel Options

<ResponseField name="sendRecovery" type="boolean">
  Whether to send notifications when checks recover from failure or degraded state.

  **Usage:**

  ```ts highlight={4} theme={null}
  new SlackAlertChannel("recovery-slack", {
    url: new URL(process.env.SLACK_WEBHOOK_URL!),
    channel: "#alerts",
    sendRecovery: true, // Send recovery notifications
  })
  ```

  **Examples:**

  <CodeGroup>
    ```ts Recovery Notifications theme={null}
    const opsSlack = new SlackAlertChannel("ops-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#ops",
      sendRecovery: true, // Get notified when issues are resolved
      sendFailure: true,
    })
    ```

    ```ts Failure Only theme={null}
    const alertsSlack = new SlackAlertChannel("alerts-only", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#critical-alerts",
      sendRecovery: false, // Only failures, no recovery notifications
      sendFailure: true,
      sendDegraded: false,
    })
    ```
  </CodeGroup>

  **Use cases**: Recovery confirmation, operational awareness, noise reduction.
</ResponseField>

<ResponseField name="sendFailure" type="boolean">
  Whether to send notifications when checks fail.

  **Usage:**

  ```ts highlight={4} theme={null}
  const slackAlert = new SlackAlertChannel("failure-slack", {
    url: new URL(process.env.SLACK_WEBHOOK_URL!),
    channel: "#alerts",
    sendFailure: true, // Send failure notifications
  })
  ```

  **Examples:**

  <CodeGroup>
    ```ts Critical Failures Only theme={null}
    const criticalSlack = new SlackAlertChannel("critical-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#critical-alerts",
      sendFailure: true, // Critical failures
      sendRecovery: true,
      sendDegraded: false, // No degraded alerts
    })
    ```

    ```ts All Notifications theme={null}
    const comprehensiveSlack = new SlackAlertChannel("all-notifications", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#monitoring",
      sendFailure: true, // All failures
      sendRecovery: true,
      sendDegraded: true,
    })
    ```
  </CodeGroup>

  **Use cases**: Incident response, failure monitoring, operational alerting.
</ResponseField>

<ResponseField name="sendDegraded" type="boolean">
  Whether to send notifications when API checks degrade (performance thresholds exceeded but not failed).

  **Usage:**

  ```ts highlight={4} theme={null}
  new SlackAlertChannel("performance-slack", {
    url: new URL(process.env.SLACK_WEBHOOK_URL!),
    channel: "#performance",
    sendDegraded: true, // Send degraded performance notifications
  })
  ```

  **Examples:**

  <CodeGroup>
    ```ts Performance Monitoring theme={null}
    const performanceSlack = new SlackAlertChannel("performance-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#performance",
      sendRecovery: true,
      sendFailure: true,
      sendDegraded: true, // Alert on degraded performance
    })

    new ApiCheck("performance-check", {
      name: "API Performance Check",
      maxResponseTime: 3000,
      degradedResponseTime: 1500, // Triggers degrade alerts
      alertChannels: [performanceSlack],
      request: {
        method: "GET",
        url: "https://api.example.com/slow-endpoint",
      },
    })
    ```

    ```ts Critical Only theme={null}
    const criticalOnlySlack = new SlackAlertChannel("critical-only", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#critical-alerts",
      sendFailure: true,
      sendRecovery: true,
      sendDegraded: false, // Only complete failures, not performance issues
    })
    ```
  </CodeGroup>

  **Use cases**: Performance monitoring, early warning systems, SLA tracking.
</ResponseField>

<ResponseField name="sslExpiry" type="boolean">
  Whether to send notifications for SSL certificate expiry warnings.

  **Usage:**

  ```ts highlight={4} theme={null}
  new SlackAlertChannel("security-slack", {
    url: new URL(process.env.SLACK_WEBHOOK_URL!),
    channel: "#security",
    sslExpiry: true,
    sslExpiryThreshold: 30, // Alert 30 days before expiry
  })
  ```

  **Examples:**

  <CodeGroup>
    ```ts Security Team Alerts theme={null}
    const securitySlack = new SlackAlertChannel("security-slack", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#security",
      sendRecovery: false,
      sendFailure: true,
      sslExpiry: true,
      sslExpiryThreshold: 7, // Alert 7 days before expiry
    })

    new ApiCheck("ssl-cert-check", {
      name: "SSL Certificate Check",
      alertChannels: [securitySlack],
      request: {
        method: "GET",
        url: "https://secure.example.com",
      },
    })
    ```

    ```ts Early Warning System theme={null}
    const earlyWarningSlack = new SlackAlertChannel("ssl-early-warning", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#devops",
      sslExpiry: true,
      sslExpiryThreshold: 60, // Alert 60 days before expiry for planning
    })
    ```
  </CodeGroup>

  **Use cases**: Certificate management, security compliance, proactive maintenance.
</ResponseField>

<ResponseField name="sslExpiryThreshold" type="number">
  Number of days before SSL certificate expiry to send notifications. Only relevant when `sslExpiry` is enabled.

  **Usage:**

  ```ts highlight={5} theme={null}
  new SlackAlertChannel('ssl-monitoring', {
    url: new URL(process.env.SLACK_WEBHOOK_URL!),
    channel: '#devops',
    sslExpiry: true,
    sslExpiryThreshold: 30 // Alert 30 days before expiry
  })
  ```

  Examples:

  <CodeGroup>
    ```ts Last Minute Alert theme={null}
    // Alert close to expiry for urgent action
    new SlackAlertChannel("ssl-urgent", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#security",
      sslExpiry: true,
      sslExpiryThreshold: 7, // 7 days notice
    })
    ```

    ```ts Multiple Thresholds theme={null}
    // Create multiple channels with different thresholds
    const earlyWarning = new SlackAlertChannel("ssl-early", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#planning",
      sslExpiry: true,
      sslExpiryThreshold: 90, // Planning notification
    })

    const urgentWarning = new SlackAlertChannel("ssl-urgent", {
      url: new URL(process.env.SLACK_WEBHOOK_URL!),
      channel: "#oncall",
      sslExpiry: true,
      sslExpiryThreshold: 7, // Urgent notification
    })
    ```
  </CodeGroup>

  **Use cases**: Certificate renewal planning, compliance management, operational scheduling.
</ResponseField>

## Examples

<CodeGroup>
  ```ts Team Channel Alerts theme={null}
      import { SlackAlertChannel, ApiCheck } from "checkly/constructs"

      const teamSlack = new SlackAlertChannel("team-slack", {
        url: new URL("https://hooks.slack.com/services/YOUR/WEBHOOK/URL"),
        channel: "#dev-team",
      })

      new ApiCheck("api-health-check", {
        name: "API Health Check",
        alertChannels: [teamSlack],
        request: {
          method: "GET",
          url: "https://api.acme.com/health",
        },
      })
  ```

  ```ts Critical Alerts Channel theme={null}
      import { ApiCheck, SlackAlertChannel } from "checkly/constructs"

      const criticalSlack = new SlackAlertChannel("critical-slack", {
        url: new URL("https://hooks.slack.com/services/YOUR/WEBHOOK/URL"),
        channel: "#critical-alerts",
        sendRecovery: true,
        sendFailure: true,
        sendDegraded: false, // Only failures for critical alerts
      })

      new ApiCheck("payment-api-check", {
        name: "Payment API Check",
        alertChannels: [criticalSlack],
        tags: ["critical", "payment"],
        request: {
          method: "GET",
          url: "https://api.acme.com/payments/health",
        },
      })
  ```

  ```ts Direct Message Alerts theme={null}
      import { ApiCheck, SlackAlertChannel } from "checkly/constructs"

      const dmSlack = new SlackAlertChannel("dm-slack", {
        url: new URL("https://hooks.slack.com/services/YOUR/WEBHOOK/URL"),
        channel: "@john.doe", // Direct message to user
        sendFailure: true,
        sendRecovery: false, // Only notify on failures
      })

      new ApiCheck("personal-project-check", {
        name: "Personal Project Check",
        alertChannels: [dmSlack],
        request: {
          method: "GET",
          url: "https://personal-project.example.com",
        },
      })
  ```

  ```ts SSL Certificate Monitoring theme={null}
      import { ApiCheck, SlackAlertChannel } from "checkly/constructs"

      const securitySlack = new SlackAlertChannel("security-slack", {
        url: new URL("https://hooks.slack.com/services/YOUR/WEBHOOK/URL"),
        channel: "#security",
        sendFailure: true,
        sendRecovery: false,
        sslExpiry: true,
        sslExpiryThreshold: 7, // Alert 7 days before SSL expires
      })

      new ApiCheck("ssl-cert-check", {
        name: "SSL Certificate Check",
        alertChannels: [securitySlack],
        request: {
          method: "GET",
          url: "https://secure.acme.com",
        },
      })
  ```

  ```ts Multiple Channels theme={null}
      import { ApiCheck, SlackAlertChannel } from "checkly/constructs"

      const devSlack = new SlackAlertChannel("dev-slack", {
        url: new URL("https://hooks.slack.com/services/YOUR/WEBHOOK/URL"),
        channel: "#development",
        sendDegraded: true,
      })

      const opsSlack = new SlackAlertChannel("ops-slack", {
        url: new URL("https://hooks.slack.com/services/YOUR/WEBHOOK/URL"),
        channel: "#operations",
        sendFailure: true,
        sendRecovery: true,
      })

      new ApiCheck("multi-channel-check", {
        name: "Multi-Channel Notifications",
        alertChannels: [devSlack, opsSlack],
        request: {
          method: "GET",
          url: "https://api.acme.com/important",
        },
      })
  ```
</CodeGroup>

## Setting Up Slack Webhooks

Find more information on how to set up a new Slack webhook in [the Slack alert channel documentation](/integrations/alerts/slack).

## Environment Variables

Store your Slack webhook URL securely using environment variables:

```ts  theme={null}
const slackChannel = new SlackAlertChannel("slack-channel", {
  url: new URL(process.env.SLACK_WEBHOOK_URL!),
  channel: "#monitoring",
})
```

```bash  theme={null}
# .env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

<Warning>
  **Webhook Security**: Keep your Slack webhook URLs secure. Anyone with access to the URL can send messages to your Slack channels.
</Warning>

<Info>
  **Channel Override**: The `channel` parameter can override the default channel configured in your Slack webhook. Use `#channel-name` for channels or `@username` for direct messages.
</Info>


Built with [Mintlify](https://mintlify.com).