# Source: https://docs.port.io/guides/all/send-slack-message-to-user.md

# Send Slack messages using Port's Slack app and automations

This guide demonstrates how to set up automations to send Slack messages to users using Port's Slack app. In this guide, we will use the email addresses from Port integrations (such as GitHub, GitLab, Jira, etc.) to look up the corresponding Slack user IDs and send targeted messages to those users.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Pull request notifications**: Notify reviewers when PRs are assigned or merged.
* **Jira notifications**: Notify users when their Jira issues are assigned.
* **On-call handoffs**: Notify the next person on-call when their shift is starting.
* **Approval requests**: Notify approvers when their approval is needed for platform requests.
* **Deployment notifications**: Alert developers when their deployments complete or fail.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* A Port account with **admin** permissions.
* Port's [Slack app](/ai-interfaces/slack-app.md) installed in your workspace.
* Access to the Slack app bot token (automatically created as a system secret).

## Set up the automations[â](#set-up-the-automations "Direct link to Set up the automations")

This guide creates two automations that work together:

1. **Get Slack user ID by email** - Looks up a user's Slack ID using their email address.
2. **Send Slack message to user** - Sends a simple message to the user.

### Get Slack user ID automation[â](#get-slack-user-id-automation "Direct link to Get Slack user ID automation")

This automation uses Slack's `users.lookupByEmail` API to find a user's Slack ID from their email address.

1. Go to the [Automations page](https://app.getport.io/settings/automations) of your portal.

2. Click on `+ Automation`.

3. Click on the `Edit JSON` button in the top right corner.

4. Copy and paste the following JSON schema:

   **Get Slack user ID automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "get_slack_user_id",
     "title": "Get Slack user ID by email",
     "icon": "Slack",
     "description": "Looks up a user's Slack ID using their email address",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "event_type",
         // Only one of "blueprintIdentifier" or "actionIdentifier" should be present depending on the trigger type
         "blueprintIdentifier": "blueprint_id",
         // OR
         "actionIdentifier": "action_id"
       },
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/users.lookupByEmail?email={{ .event.diff.after.properties.email }}",
       "agent": false,
       "synchronized": true,
       "method": "GET",
       "headers": {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body":{}
     },
     "publish": true
   }
   ```

5. Click "Save" to create the automation.

### Send Slack message automation[â](#send-slack-message-automation "Direct link to Send Slack message automation")

This automation sends a simple message to a user's Slack DM using their user ID.

1. Go to the [Automations page](https://app.getport.io/settings/automations) of your portal.

2. Click on `+ Automation`.

3. Click on the `Edit JSON` button in the top right corner.

4. Copy and paste the following JSON schema:

   **Send Slack message automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "send_slack_message_to_user",
     "title": "Send Slack message to user",
     "icon": "Slack",
     "description": "Sends a simple Slack message to a user by their email",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "event_type",
         // Only one of "blueprintIdentifier" or "actionIdentifier" should be present depending on the trigger type
         "blueprintIdentifier": "blueprint_id",
         // OR
         "actionIdentifier": "action_id"
       },
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/chat.postMessage",
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Content-Type": "application/json; charset=utf-8",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {
         "channel": "{{ .event.diff.after.response.user.id }}",
         "text": "ð New notification: From port automation"
       }
     },
     "publish": true
   }
   ```

5. Click "Save" to create the automation.

Replace your Slack bot token

1. Click on the `...` button in the top right corner of your Port application
2. Select `Credentials` and then click on the `Secrets` tab
3. Look for a secret named `__SLACK_APP_BOT_TOKEN_T<team_id>` where `<team_id>` is your Slack workspace ID

## Use case examples[â](#use-case-examples "Direct link to Use case examples")

Below are specific examples of how to use these automations for different integrations:

### GitHub pull request notifications[â](#github-pull-request-notifications "Direct link to GitHub pull request notifications")

We can implement a use case where the creator of a pull request is notified when the pull request is merged.<br /><!-- -->Add the two automations below to your portal to set up the notifications.

1. **Look up the Slack user ID by email**

   **Look up the Slack user ID by email automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "get_slack_user_id_for_merged_pr",
     "title": "Get Slack user ID for merged PR",
     "icon": "Slack",
     "description": "Looks up a user's Slack ID using their email address when a PR is merged",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_UPDATED",
         "blueprintIdentifier": "githubPullRequest"
       },
       "condition": {
         "type": "JQ",
         "expressions": [
           ".diff.after.properties.status == \"merged\""
         ],
         "combinator": "and"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/users.lookupByEmail?email={{ .event.diff.after.relations.creator }}",
       "agent": false,
       "synchronized": true,
       "method": "GET",
       "headers": {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {}
     },
     "publish": true
   }
   ```

2. **Send Slack message to user**

   **Send Slack message to user automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "notify_user_on_pr_merged",
     "title": "Notify user when PR is merged",
     "icon": "Slack",
     "description": "Sends a Slack message to the PR creator or assignee when the PR is merged",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "get_slack_user_id_for_merged_pr"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/chat.postMessage",
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Content-Type": "application/json; charset=utf-8",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {
         "channel": "{{ .event.diff.after.response.user.id }}",
         "blocks": [
           {
             "type": "section",
             "text": {
               "type": "mrkdwn",
               "text": "Hi <@{{ .event.diff.after.response.user.real_name }}>,\n\nYour pull request *{{ .event.context.entity.title }}* has been merged! ð"
             }
           },
           {
             "type": "section",
             "fields": [
               {
                 "type": "mrkdwn",
                 "text": "*Repository:*\n{{ .event.diff.after.properties.relations.repository }}"
               },
               {
                 "type": "mrkdwn",
                 "text": "*Merged At:*\n{{ .event.diff.after.properties.mergedAt }}"
               }
             ]
           },
           {
             "type": "actions",
             "elements": [
               {
                 "type": "button",
                 "text": {
                   "type": "plain_text",
                   "text": "View PR"
                 },
                 "url": "{{ .event.diff.after.properties.link }}"
               }
             ]
           }
         ]
       }
     },
     "publish": true
   }
   ```

### Jira issue notifications[â](#jira-issue-notifications "Direct link to Jira issue notifications")

We can implement a use case where a user is notified when a Jira issue is assigned to them. Add the two automations below to your portal to set up the notifications.

1. **Look up the Slack user ID by email**

   **Look up the Slack user ID by email automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "get_slack_user_id_for_jira_assignee",
     "title": "Get Slack user ID for Jira assignee",
     "icon": "Slack",
     "description": "Looks up a user's Slack ID using their email address when a Jira issue is created",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_CREATED",
         "blueprintIdentifier": "jiraIssue"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/users.lookupByEmail?email={{ .event.diff.after.properties.assignee }}",
       "agent": false,
       "synchronized": true,
       "method": "GET",
       "headers": {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {}
     },
     "publish": true
   }   
   ```

2. **Send Slack message to user**

   **Send Slack message to user automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "notify_jira_assignee_on_assignment",
     "title": "Notify Jira assignee on assignment",
     "icon": "Slack",
     "description": "Sends a Slack message to the assignee when a Jira issue is assigned to them",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "get_slack_user_id_for_jira_assignee"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/chat.postMessage",
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Content-Type": "application/json; charset=utf-8",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {
         "channel": "{{ .event.diff.after.response.user.id }}",
         "text": "ð You have been assigned a Jira issue",
         "blocks": [
           {
             "type": "section",
             "text": {
               "type": "mrkdwn",
               "text": "Hi <@{{ .event.diff.after.response.user.real_name }}>,\n\nYou have been assigned to a Jira issue:"
             }
           },
           {
             "type": "section",
             "fields": [
               {
                 "type": "mrkdwn",
                 "text": "*Issue:*\n{{ .event.diff.after.properties.title }}"
               },
               {
                 "type": "mrkdwn",
                 "text": "*Status:*\n{{ .event.diff.after.properties.status }}"
               },
               {
                 "type": "mrkdwn",
                 "text": "*Priority:*\n{{ .event.diff.after.properties.priority }}"
               },
               {
                 "type": "mrkdwn",
                 "text": "*Assigned At:*\n{{ .event.diff.after.properties.updatedAt }}"
               }
             ]
           },
           {
             "type": "actions",
             "elements": [
               {
                 "type": "button",
                 "text": {
                   "type": "plain_text",
                   "text": "View Issue"
                 },
                 "url": "{{ .event.diff.after.properties.url }}"
               }
             ]
           }
         ]
       }
     },
     "publish": true
   }
   ```

### PagerDuty on-call notifications[â](#pagerduty-on-call-notifications "Direct link to PagerDuty on-call notifications")

We can implement a use case where an on-call user is notified when they are assigned to a PagerDuty incident.<br /><!-- -->Add the two automations below to your portal to set up the notifications.

1. **Look up the Slack user ID by email**

   **Look up the Slack user ID by email automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "get_slack_user_id_for_pagerduty_assignee",
     "title": "Get Slack user ID for PagerDuty assignee",
     "icon": "Slack",
     "description": "Looks up a user's Slack ID using their email address when a PagerDuty incident is assigned",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "ENTITY_CREATED",
         "blueprintIdentifier": "pagerdutyIncident"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/users.lookupByEmail?email={{ .event.diff.after.properties.assignee }}",
       "agent": false,
       "synchronized": true,
       "method": "GET",
       "headers": {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {}
     },
     "publish": true
   }
   ```

2. **Send Slack message to user**

   **Send Slack message to user automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "notify_pagerduty_assignee_on_incident",
     "title": "Notify PagerDuty assignee on incident assignment",
     "icon": "Slack",
     "description": "Sends a Slack message to the assignee when a PagerDuty incident is assigned",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "get_slack_user_id_for_pagerduty_assignee"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/chat.postMessage",
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Content-Type": "application/json; charset=utf-8",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {
         "channel": "{{ .event.diff.after.response.user.id }}",
         "text": "ð¨ You have been assigned a new PagerDuty incident!",
         "blocks": [
           {
             "type": "section",
             "text": {
               "type": "mrkdwn",
               "text": "Hi <@{{ .event.diff.after.response.user.real_name }}>,\n\nYou have been assigned to a new PagerDuty incident:\n*Incident:* {{ .event.diff.after.properties.title }}\n*Priority:* {{ .event.diff.after.properties.priority }}\n*Service:* {{ .event.diff.after.properties.service }}"
             }
           },
           {
             "type": "actions",
             "elements": [
               {
                 "type": "button",
                 "text": {
                   "type": "plain_text",
                   "text": "View Incident"
                 },
                 "url": "https://app.getport.io/pagerdutyIncident/{{ .event.diff.after.identifier }}"
               }
             ]
           }
         ]
       }
     },
     "publish": true
   }
   ```

### Approval requests notifications[â](#approval-requests-notifications "Direct link to Approval requests notifications")

We can implement a use case where an approver is notified when a platform request is created. Add the two automations below to your portal to set up the notifications.

1. **Look up the Slack user ID by email**

   **Look up the Slack user ID by email automation (Click to expand)**

   Create in Port

   ```
     {
       "identifier": "get_slack_user_id_for_approver",
       "title": "Get Slack user ID for platform request approver",
       "icon": "Slack",
       "description": "Looks up a user's Slack ID using their email address when a platform request is created",
       "trigger": {
         "type": "automation",
         "event": {
           "type": "ENTITY_CREATED",
           "blueprintIdentifier": "platformRequest"
         }
       },
       "invocationMethod": {
         "type": "WEBHOOK",
         "url": "https://slack.com/api/users.lookupByEmail?email={{ .event.diff.after.properties.approver }}",
         "agent": false,
         "synchronized": true,
         "method": "GET",
         "headers": {
           "Content-Type": "application/x-www-form-urlencoded",
           "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
         },
         "body": {}
       },
       "publish": true
     }
   ```

2. **Send Slack message to user**

   **Send Slack message to user automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "notify_approver_on_platform_request",
     "title": "Notify approver when approval is needed",
     "icon": "Slack",
     "description": "Sends a Slack message to the approver when a platform request requires approval",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "get_slack_user_id_for_approver"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/chat.postMessage",
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Content-Type": "application/json; charset=utf-8",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {
         "channel": "{{ .event.diff.after.response.user.id }}",
         "text": "â Approval request",
         "blocks": [
           {
             "type": "section",
             "text": {
               "type": "mrkdwn",
               "text": "Hi <@{{ .event.diff.after.response.user.real_name }}>,\n\nA new platform request requires your approval:"
             }
           },
           {
             "type": "section",
             "fields": [
               {
                 "type": "mrkdwn",
                 "text": "*Request:*\n{{ .event.diff.after.properties.title }}"
               },
               {
                 "type": "mrkdwn",
                 "text": "*Type:*\n{{ .event.diff.after.properties.requestType }}"
               },
               {
                 "type": "mrkdwn",
                 "text": "*Requester:*\n{{ .event.diff.after.properties.requester }}"
               },
               {
                 "type": "mrkdwn",
                 "text": "*Created:*\n{{ .event.diff.after.properties.createdAt }}"
               }
             ]
           },
           {
             "type": "actions",
             "elements": [
               {
                 "type": "button",
                 "text": {
                   "type": "plain_text",
                   "text": "Review Request"
                 },
                 "url": "https://app.getport.io/platformRequest/{{ .event.diff.after.identifier }}"
               }
             ]
           }
         ]
       }
     },
     "publish": true
   }
   ```

### Failed deployment notifications[â](#failed-deployment-notifications "Direct link to Failed deployment notifications")

We can implement a use case where a user is notified when a deployment fails. Add the two automations below to your portal to set up the notifications.

1. **Look up the Slack user ID by email**

   **Look up the Slack user ID by email automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "get_slack_user_id_for_failed_deployment",
     "title": "Get Slack user ID for failed deployment",
     "icon": "Slack",
     "description": "Looks up a user's Slack ID using their email address when a deployment fails",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "deploy_an_image"
       },
       "condition": {
         "type": "JQ",
         "expressions": [
           ".diff.before.status == \"IN_PROGRESS\"",
           ".diff.after.status == \"FAILURE\""
         ],
         "combinator": "and"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/users.lookupByEmail?email={{ .event.diff.after.properties.triggered_by_email }}",
       "agent": false,
       "synchronized": true,
       "method": "GET",
       "headers": {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {}
     },
     "publish": true
   }
   ```

2. **Send Slack message to user**

   **Send Slack message to user automation (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "notify_user_on_failed_deployment",
     "title": "Notify user on failed deployment",
     "icon": "Slack",
     "description": "Sends a Slack message to the user when their deployment fails",
     "trigger": {
       "type": "automation",
       "event": {
         "type": "RUN_UPDATED",
         "actionIdentifier": "get_slack_user_id_for_failed_deployment"
       }
     },
     "invocationMethod": {
       "type": "WEBHOOK",
       "url": "https://slack.com/api/chat.postMessage",
       "synchronized": true,
       "method": "POST",
       "headers": {
         "Content-Type": "application/json; charset=utf-8",
         "Authorization": "Bearer {{ .secrets.__SLACK_APP_BOT_TOKEN_T123 }}"
       },
       "body": {
         "channel": "{{ .event.diff.after.response.user.id }}",
         "text": "ð¨ Your deployment has failed.",
         "blocks": [
           {
             "type": "section",
             "text": {
               "type": "mrkdwn",
               "text": "Hi <@{{ .event.diff.after.response.user.real_name }}>,\n\nYour deployment of service *{{ .event.diff.after.properties.identifier }}* (image: {{ .event.diff.after.properties.image }}) to environment *{{ .event.diff.after.properties.environment }}* has failed.\n\n[View run details](https://app.getport.io/organization/run?runId={{ .event.diff.after.id }})"
             }
           }
         ]
       }
     },
     "publish": true
   }
   ```

## Let's test it[â](#lets-test-it "Direct link to Let's test it")

To test your automations:

1. Create a test entity that matches your trigger conditions.
2. Check the automation execution logs in the [Automations page](https://app.getport.io/settings/automations).
3. Verify that the Slack message was sent to the intended user.
4. Check for any error messages in the execution logs.
