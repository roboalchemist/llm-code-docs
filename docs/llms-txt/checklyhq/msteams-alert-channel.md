# Source: https://checklyhq.com/docs/constructs/msteams-alert-channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MSTeamsAlertChannel Construct

> Learn how to configure Microsoft Teams alert channels with the Checkly CLI.

<Tip>
  Learn more about Microsoft Teams alerts in [the Microsoft Teams Alerts documentation](/integrations/alerts/msteams).
</Tip>

Use Microsoft Teams Alert Channels to send notifications to Microsoft Teams channels when checks fail or recover. Teams alerts help keep your team informed and enable quick collaboration on issues.

<CodeGroup>
  ```ts Basic Example theme={null}
  import { MSTeamsAlertChannel } from "checkly/constructs"

  const teamsChannel = new MSTeamsAlertChannel("teams-channel-1", {
    name: "Dev Team Alerts",
    url: "https://prod-24.westus.logic.azure.com:443/workflows/xxxxx",
  })
  ```

  ```ts Advanced Example theme={null}
  import { MSTeamsAlertChannel } from "checkly/constructs"

  const teamsChannel = new MSTeamsAlertChannel("advanced-teams-channel", {
    name: "Production Monitoring Alerts",
    url: "https://prod-24.westus.logic.azure.com:443/workflows/xxxxx",
    sendRecovery: true,
    sendFailure: true,
    sendDegraded: true,
    sslExpiry: true,
    sslExpiryThreshold: 14,
  })
  ```
</CodeGroup>

## Configuration

<Tabs>
  <Tab title="Microsoft Teams Alert Channel">
    Configure Microsoft Teams-specific settings:

    | Parameter | Type     | Required | Default | Description                                         |
    | --------- | -------- | -------- | ------- | --------------------------------------------------- |
    | `url`     | `string` | ✅        | -       | Microsoft Teams webhook URL created by the Workflow |
    | `name`    | `string` | ❌        | -       | Friendly name to recognize the integration          |
    | `payload` | `string` | ❌        | -       | Custom payload for the alert message                |
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

## Examples

<Tabs>
  <Tab title="Development Team">
    ```ts  theme={null}
    import { MSTeamsAlertChannel, ApiCheck } from "checkly/constructs"

    const devTeamsAlert = new MSTeamsAlertChannel("dev-team-alerts", {
      name: "Development Team Alerts",
      url: "https://prod-24.westus.logic.azure.com:443/workflows/dev-team-webhook",
    })

    new ApiCheck("dev-api-check", {
      name: "Development API Health",
      alertChannels: [devTeamsAlert],
      tags: ["development", "api"],
      request: {
        method: "GET",
        url: "https://dev-api.example.com/health",
      },
    })
    ```
  </Tab>

  <Tab title="Operations Team">
    ```ts  theme={null}
    import { ApiCheck, MSTeamsAlertChannel } from "checkly/constructs"

    const opsTeamsAlert = new MSTeamsAlertChannel("ops-team-alerts", {
      name: "Operations Team Alerts",
      url: "https://prod-24.westus.logic.azure.com:443/workflows/ops-team-webhook",
      sendRecovery: true,
      sendFailure: true,
      sendDegraded: true, // Ops team wants to know about degraded performance
    })

    new ApiCheck("infrastructure-check", {
      name: "Infrastructure Health Check",
      alertChannels: [opsTeamsAlert],
      maxResponseTime: 5000,
      degradedResponseTime: 2000,
      tags: ["infrastructure", "operations"],
      request: {
        method: "GET",
        url: "https://infrastructure.example.com/health",
      },
    })
    ```
  </Tab>

  <Tab title="Multi-Team Notifications">
    ```ts  theme={null}
    import { ApiCheck, MSTeamsAlertChannel } from "checkly/constructs"

    const devTeams = new MSTeamsAlertChannel("dev-teams", {
      name: "Development Team",
      url: "https://prod-24.westus.logic.azure.com:443/workflows/dev-webhook",
    })

    const opsTeams = new MSTeamsAlertChannel("ops-teams", {
      name: "Operations Team",
      url: "https://prod-24.westus.logic.azure.com:443/workflows/ops-webhook",
    })

    const businessTeams = new MSTeamsAlertChannel("business-teams", {
      name: "Business Team",
      url: "https://prod-24.westus.logic.azure.com:443/workflows/business-webhook",
      sendFailure: true,
      sendRecovery: true,
      sendDegraded: false, // Business team only needs to know about failures
    })

    new ApiCheck("multi-team-check", {
      name: "Cross-Team Critical Service",
      alertChannels: [devTeams, opsTeams, businessTeams],
      tags: ["cross-team", "critical"],
      request: {
        method: "GET",
        url: "https://critical-service.example.com/health",
      },
    })
    ```
  </Tab>

  <Tab title="Environment-Specific">
    ```ts  theme={null}
    import { ApiCheck, MSTeamsAlertChannel } from "checkly/constructs"

    const prodTeams = new MSTeamsAlertChannel("prod-teams", {
      name: "Production Alerts",
      url: "https://prod-24.westus.logic.azure.com:443/workflows/prod-webhook",
    })

    const stagingTeams = new MSTeamsAlertChannel("staging-teams", {
      name: "Staging Environment Alerts",
      url: "https://prod-24.westus.logic.azure.com:443/workflows/staging-webhook",
      sendDegraded: true, // More tolerant for staging
    })

    // Production monitoring
    new ApiCheck("prod-api-check", {
      name: "Production API",
      alertChannels: [prodTeams],
      tags: ["production"],
      request: {
        method: "GET",
        url: "https://api.example.com/health",
      },
    })

    // Staging monitoring
    new ApiCheck("staging-api-check", {
      name: "Staging API",
      alertChannels: [stagingTeams],
      tags: ["staging"],
      maxResponseTime: 10000, // More lenient for staging
      degradedResponseTime: 5000,
      request: {
        method: "GET",
        url: "https://staging-api.example.com/health",
      },
    })
    ```
  </Tab>
</Tabs>

## Setting Up Microsoft Teams Webhooks

Find more information on how to set up a Microsoft Teams workflows in [the Microsoft Teams documentation](/integrations/alerts/msteams).

## Environment Variables

Store your Teams webhook URLs securely using environment variables:

```ts  theme={null}
const teamsChannel = new MSTeamsAlertChannel("teams-alerts", {
  name: "Team Notifications",
  url: process.env.TEAMS_WEBHOOK_URL!,
})
```

```bash  theme={null}
# .env
TEAMS_WEBHOOK_URL=https://prod-24.westus.logic.azure.com:443/workflows/xxxxx
```

## Best Practices

<Warning>
  **Webhook Security**: Keep your Teams webhook URLs secure. Anyone with access to the URL can send messages to your Teams channels.
</Warning>

<Info>
  **Channel Selection**: Choose appropriate Teams channels for different types of alerts. Consider creating dedicated monitoring channels to avoid noise in general discussion channels.
</Info>


Built with [Mintlify](https://mintlify.com).