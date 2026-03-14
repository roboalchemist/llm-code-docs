# Source: https://docs.gitguardian.com/platform/configure-alerting/notifiers-integrations/pagerduty.md

# PagerDuty

> Configure PagerDuty integration to receive GitGuardian incident alerts through PagerDuty's Events API.

PagerDuty is an incident management platform that provides notifications, automatic escalations, on-call scheduling, and other functionality to help teams detect and fix infrastructure problems quickly. GitGuardian is natively integrated with PagerDuty so all alerts sent by GitGuardian can be disseminated through PagerDuty flows.

### PagerDuty + GitGuardian integration benefits

- Receive PagerDuty notifications for GitGuardian alerts
- GitGuardian groups occurrences of the same secret under one single secret incident. Set the frequency of your notifications: either all occurrences of each secret incident, or only at the first occurrence (only when the incident is newly created).

### How it works

When GitGuardian detects a secret in your source code, GitGuardian will send an event to a service in PagerDuty. Events from GitGuardian will trigger a new incident on the corresponding PagerDuty service, or group as alerts logs into an existing incident.

![GG PagerDuty incident](/img/platform/configure-alerting/notifiers-integrations/pagerduty/Pagerduty_occurences.png)

### Requirements

PagerDuty integrations require Admin rights on the PagerDuty service you want to receive notifications on (to create routing integration key needed for the integration on GitGuardian side). If it is not your case, please reach out to a PagerDuty Admin of your service to configure the integration.

### Integration walkthrough

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/u2rJQgFo4LY?controls=0&modestbranding=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

#### In PagerDuty

**Integrating with a PagerDuty service**

1. From the Configuration menu, select Services.
2. There are two ways to add an integration to a service:
   - **If you are adding your integration to an existing service**: click the name of the service you want to add the integration to. Then, select the **Integrations** tab and click the **New Integration** button.
   - If you are creating a new service for your integration: Please read PagerDuty documentation in section [Configuring Services and Integrations](https://support.pagerduty.com/docs/services-and-integrations#section-configuring-services-and-integrations) and follow the steps outlined in the [Create a New Service](https://support.pagerduty.com/docs/services-and-integrations#section-create-a-new-service) section, selecting GitGuardian as the Integration Type. Continue with the In GitGuardian section (below) once you have finished these steps.
3. Select GitGuardian from the Integration Type menu (if you cannot find GitGuardian, please fallback on "Events API v2" type).
4. Click the **Add Integration** button to save your new integration. You will be redirected to the Integrations tab for your service.
5. An **Integration Key** will be generated on this screen. Keep this key saved in a safe place, as it will be used when you configure the integration with GitGuardian in the next section.

<!-- TODO: Add screenshot of PagerDuty when GitGuardian integration available -->

#### In GitGuardian

1. Navigate to Settings > Integrations > Destinations > [PagerDuty](https://dashboard.gitguardian.com/settings/integrations/pagerduty)
2. Provide your newly created integration key
3. Select the frequency of notifications
4. Submit

For business workspace, the PagerDuty integration configuration is done per team. You can either create a single configuration within the `All-incidents` team to send all GitGuardian incidents to the same PagerDuty project or create separate configurations for each team to send their incidents to specific projects.
![GG PagerDuty integration form](/img/platform/configure-alerting/notifiers-integrations/pagerduty/new_integration_form.png)

### How to uninstall

1. Navigate to Settings > Integrations > Destinations > [PagerDuty](https://dashboard.gitguardian.com/settings/integrations/pagerduty)
2. Delete your integration key on GitGuardian
3. Revoke your key on PagerDuty

![PagerDuty integration keys table](/img/platform/configure-alerting/notifiers-integrations/pagerduty/integration_keys_table.png)
