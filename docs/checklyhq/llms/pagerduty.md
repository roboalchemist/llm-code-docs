# Source: https://checklyhq.com/docs/integrations/incident-management/pagerduty.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Alerts to PagerDuty

> Learn how Checkly integrates seamlessly with PagerDuty, delivering real-time failure and recovery alerts to your PagerDuty account

Checkly integrates with [Pagerduty](https://pagerduty.com) and can deliver all failure and recovery events
to your Pagerduty account. After setting up the integration, Checkly will:

1. Trigger alerts in Pagerduty when a check fails.
2. Resolve alerts when a check recovers.

Setup is as simple as following the three-step Pagerduty connect process. You can add as many Pagerduty channels as
you wish.

1. Navigate to the **alert settings** tab on the account screen and click the 'Add channels' button.
   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/pagerduty_step1.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=d3ec5e6da191d640e8362aedd8e67b99" alt="setup checkly pagerduty integration step 1" width="989" height="91" data-path="images/docs/images/integrations/pagerduty_step1.png" />

2. Clicking the **Alert with Pagerduty** button will take you to a Pagerduty Connect screen. Provide your credentials and click
   **Sign In** to allow Checkly to connect with Pagerduty.
   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/pagerduty_step2.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=023c2c8e992dc2e0744f6e01d0dd826a" alt="set up checkly pagerduty integration step 2" width="1237" height="993" data-path="images/docs/images/integrations/pagerduty_step2.png" />

3. On the next screen you can hook up Checkly to one or more existing services. If you select multiple services, we will
   create multiple dedicated channels so you have more flexibility of muting, editing and managing the channels.
   Click **Connect** to save your settings and redirect you back to Checkly.
   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/pagerduty_step3.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=d0f1a7bfd11ff877caf0112ead8137eb" alt="set up checkly pagerduty integration step 3" width="1193" height="949" data-path="images/docs/images/integrations/pagerduty_step3.png" />

4. Back in Checkly, you should see your Pagerduty **integration credentials** reflected in the alert settings. Don't forget
   to hit **Save Pagerduty channel**.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/pagerduty_step4.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=a33155a96c1013e9c41d5b226f299b43" alt="set up checkly pagerduty integration step 4" width="1169" height="420" data-path="images/docs/images/integrations/pagerduty_step4.png" />

5. Checkly will trigger an incident in Pagerduty when checks fail and also mark them as resolved when the checks are passing again.
   <img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/pagerduty_step5.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=e0b9daac467fa90585d18ffeaac931fa" alt="set up checkly pagerduty integration step 5" width="1392" height="552" data-path="images/docs/images/integrations/pagerduty_step5.png" />

## Advanced PagerDuty Configuration

### PagerDuty Alert Mapping

Configure how Checkly alerts map to PagerDuty incidents:

```yaml  theme={null}
PagerDuty Configuration:
  Service: Production Monitoring
  Integration Type: Events API v2
  
Alert Mapping:
  ALERT_FAILURE → Critical Incident
  ALERT_DEGRADED → Warning Incident  
  ALERT_RECOVERY → Resolve Incident
  
Incident Details:
  Title: "{{ALERT_TITLE}}"
  Description: "Check {{CHECK_NAME}} from {{RUN_LOCATION}}"
  Severity: Based on check tags and alert type
  Component: Derived from check name or group
  Custom Fields:
    - Response Time: {{RESPONSE_TIME}}ms
    - Check ID: {{CHECK_ID}}
    - Location: {{RUN_LOCATION}}
```

### Advanced PagerDuty Features

Leverage PagerDuty's advanced incident management capabilities:

```json  theme={null}
{
  "incident": {
    "type": "incident", 
    "title": "{{ALERT_TITLE}}",
    "service": {
      "id": "P123ABC",
      "type": "service_reference"
    },
    "priority": {
      "id": "{{#contains TAGS 'critical'}}P1{{else}}P2{{/contains}}",
      "type": "priority_reference"
    },
    "body": {
      "type": "incident_body",
      "details": "Check {{CHECK_NAME}} failed from {{RUN_LOCATION}}.\n\nResponse Time: {{RESPONSE_TIME}}ms\nError: {{CHECK_ERROR_MESSAGE}}\n\nView details: {{RESULT_LINK}}"
    },
    "escalation_policy": {
      "id": "{{#contains CHECK_NAME 'payment'}}P456DEF{{else}}P789GHI{{/contains}}",
      "type": "escalation_policy_reference"
    }
  }
}
```

### PagerDuty Best Practices

* **Service Organization**: Create separate PagerDuty services for different applications or teams
* **Escalation Policies**: Set up appropriate escalation chains based on check criticality
* **Priority Mapping**: Use check tags to automatically assign appropriate incident priorities
* **Integration Keys**: Use different integration keys for different environments (production, staging)
* **Custom Fields**: Include relevant context like response times, error messages, and check locations


Built with [Mintlify](https://mintlify.com).