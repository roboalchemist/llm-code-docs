# Source: https://docs.port.io/guides/all/notify-users-upon-approval-of-action.md

# Notify users upon approval of self-service actions

This guide shows how to build an automation in Port that sends Slack notifications to users when their self-service actions are **approved** or **declined**. This workflow ensures transparency and closes the feedback loop after a team member submits a request.

## Use cases[â](#use-cases "Direct link to Use cases")

* Automatically inform users when their actions are approved or rejected.
* Reduce manual follow-ups and delays by streamlining communication.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* Complete the [onboarding process](/getting-started/overview.md).
* You have access to Slack developers page and have created a Slack webhook URL. Follow the steps in the [Slack Incoming Webhooks Guide](https://api.slack.com/messaging/webhooks) to create a webhook URL.

## Set up action[â](#set-up-action "Direct link to Set up action")

In this guide, we will use the `Service` blueprint that is created by default during the onboarding process.

Here is an example action that locks service deployment environments â useful during maintenance or peak traffic periods. To introduce approvals, we will modify the action to require approval before execution.

This action can be reused from our [Lock and Unlock Service guide](https://docs.port.io/guides/all/lock-and-unlock-services-in-port/).

**Updated lock service action (Click to expand)**

Create in Port

```
{
  "identifier": "lock_service",
  "title": "Lock Service",
  "icon": "Lock",
  "description": "Lock service in Port",
  "trigger": {
    "type": "self-service",
    "operation": "DAY-2",
    "userInputs": {
      "properties": {
        "reason": {
          "type": "string",
          "title": "Reason"
        },
        "environment": {
          "type": "string",
          "title": "Environment",
          "enum": [
            "Production",
            "Staging",
            "Development"
          ],
          "enumColors": {
            "Production": "green",
            "Staging": "orange",
            "Development": "blue"
          }
        }
      },
      "required": [],
      "order": [
        "reason"
      ]
    },
    "blueprintIdentifier": "service"
  },
  "invocationMethod": {
    "type": "UPSERT_ENTITY",
    "blueprintIdentifier": "service",
    "mapping": {
      "identifier": "{{ .entity.identifier }}",
      "title": "{{ .entity.title }}",
      "properties": {
        "{{ if .inputs.environment == 'Production' then 'locked_in_prod' else 'locked_in_test' end }}": true,
        "{{ if .inputs.environment == 'Production' then 'locked_reason_prod' else 'locked_reason_test' end }}": "{{ .inputs.reason }}",
        "trigger_type": "Locked",
        "triggered_environment": "{{ .inputs.environment }}"
      }
    }
  },
  "requiredApproval": true
}
```

## Set up automation[â](#set-up-automation "Direct link to Set up automation")

Now let us create an automation that sends a Slack message when the status of the self-service action changes from `WAITING_FOR_APPROVAL` to either `IN_PROGRESS` (approved) or `DECLINED` (declined).

Follow the steps below to configure the automation:

1. Head to the [automation](https://app.getport.io/settings/automations) page.

2. Click on the `+ Automation` button.

3. Copy and paste the following JSON configuration into the editor:

   **Self service approval notification automation (Click to expand)**

   Configure your Slack environment

   Replace `<SLACK_WEBHOOK_URL>` with your actual Slack webhook URL.

   Create in Port

   ```
   {
     "identifier": "approval_notification",
     "title": "Notify on Action Approval/Decline",
     "description": "Sends Slack notifications when a self-service action is approved or declined",
     "trigger": {
         "type": "automation",
         "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "test_approval"
         },
         "condition": {
         "type": "JQ",
         "expressions": [
             ".diff.before.status == \"WAITING_FOR_APPROVAL\"",
             ".diff.after.status | IN(\"DECLINED\", \"IN_PROGRESS\")"
         ],
         "combinator": "and"
         }
     },
     "invocationMethod": {
         "type": "WEBHOOK",
         "url": "<SLACK_WEBHOOK_URL>",
         "agent": false,
         "synchronized": true,
         "method": "POST",
         "headers": {},
         "body": {
         "text": "{{ if .event.diff.after.status == \"DECLINED\" then \":x: *Your self-service request was declined.*\\n\\n*Action:* \" + .event.context.action.title + \"\\n*Status:* `\" + .event.diff.after.status + \"`\\n*Comment:* _\" + .event.diff.after.approval.description + \"_\\n\\n<https://app.getport.io/organization/run?runId=\" + .event.diff.after.id + \"|View in Port>\" else \":white_check_mark: *Your self-service request was approved!*\\n\\n*Action:* \" + .event.context.action.title + \"\\n*Status:* `\" + .event.diff.after.status + \"`\\n\\n<https://app.getport.io/organization/run?runId=\" + .event.diff.after.id + \"|View in Port>\" end }}"
         }
     },
     "publish": true
   }
   ```

4. Click `Save`.

When a user submits a self-service action and it is reviewed, the automation sends them a Slack message indicating whether it was **approved** or **declined**:

![](/img/guides/slackNotificationForApproval.png)
