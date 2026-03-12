# Source: https://docs.port.io/scorecards/examples/automation-use-cases.md

# Automation use-cases

This page provides examples of automations that trigger when scorecard rule results are updated. These examples demonstrate how to notify teams via Slack or Microsoft Teams when rule results change, and how to automatically create GitHub issues when rule results degrade from `Passed` to `Not passed`.

## Notify on scorecard rule result updates[â](#notify-on-scorecard-rule-result-updates "Direct link to Notify on scorecard rule result updates")

### Automation definition[â](#automation-definition "Direct link to Automation definition")

By using the `ENTITY_UPDATED` trigger type, we can run custom logic whenever an entity of a specific type is updated.

The following configuration will cause a message to be sent whenever a scorecard rule result is updated:

**Automation configuration (click to expand)**

**Remember to change `github-org-name` and `github-repo-name` to your GitHub organization name and repository in the highlighted lines.**

Create in Port

```
{
"identifier": "ruleResultUpdated",
"title": "Rule result updated",
"trigger": {
    "type": "automation",
    "event": {
    "type": "ENTITY_UPDATED",
    "blueprintIdentifier": "_rule_result"
    }
},
"invocationMethod": {
    "type": "GITHUB",
    "org": "github-org-name",
    "repo": "github-repo-name",
    "workflow": "notify-rule-result-updated.yaml",
    "workflowInputs": {
    "rule_result_name": "{{ .event.context.entityIdentifier }}",
    "entity_link": "{{ .event.diff.after.properties.entity_link }}"
    },
    "reportWorkflowStatus": true
},
"publish": true
}
```

* `invocationMethod.workflowInputs` is the payload to be passed to the GitHub workflow upon every execution. In this example, we pass the rule result's identifier and the link to the evaluated entity.

* `invocationMethod.reportWorkflowStatus` is set to `true` to automatically update the action run in Port with the status of the GitHub workflow.

### Backend - GitHub workflow[â](#backend---github-workflow "Direct link to Backend - GitHub workflow")

The `notify-rule-result-updated.yaml` workflow will contain the logic to send a Slack/Teams message.

#### Prerequisite - set up webhooks

The workflow requires a Slack webhook URL and/or a Microsoft Teams webhook URL to send the message.

Slack:

1. To set up a Slack webhook, follow the instructions [here](https://api.slack.com/messaging/webhooks).
2. Once you have the webhook URL, add it as a secret in your GitHub repository named `SLACK_WEBHOOK_URL`.

Microsoft Teams:

1. To set up a Microsoft Teams webhook, follow the instructions [here](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook).
2. Once you have the webhook URL, add it as a secret in your GitHub repository named `TEAMS_WEBHOOK_URL`.

**GitHub workflow (click to expand)**

This workflow includes steps to send a message via **Slack** and **Microsoft Teams**.<br />**Use only the step(s) that apply to your use case.**

notify-rule-result-updated.yaml

```
name: Notify when rule result is updated

on:
  workflow_dispatch:
    inputs:
      # Note that the inputs are the same as the payload (workflowInputs) defined in the automation
      rule_result_name:
        description: "The rule result's name"
        required: true
        type: string
      entity_link:
        description: "A link to the evaluated entity"
        required: true
        type: string

jobs:
  send_message:
    runs-on: ubuntu-latest
    steps:
      - name: Send message to Slack
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
        run: |
          curl -X POST -H 'Content-type: application/json' --data '{"text":"The rule result ${{ inputs.rule_result_name }} has been updated. See evaluated entity: https://app.port.io${{ inputs.entity_link }}"}' $SLACK_WEBHOOK_URL
      
      - name: Send message to Microsoft Teams
        env:
          TEAMS_WEBHOOK_URL: ${{ secrets.TEAMS_WEBHOOK_URL }}
        run: |
          curl -H 'Content-Type: application/json' -d '{"text":"The rule result ${{ inputs.rule_result_name }} has been updated. See evaluated entity: https://app.port.io${{ inputs.entity_link }}"}' $TEAMS_WEBHOOK_URL
```

<br />

***

<br />

## Create a GitHub issue whenever a scorecard rule result is degraded[â](#create-a-github-issue-whenever-a-scorecard-rule-result-is-degraded "Direct link to Create a GitHub issue whenever a scorecard rule result is degraded")

### Automation definition[â](#automation-definition-1 "Direct link to Automation definition")

By using the `ENTITY_UPDATED` trigger type, we can run custom logic whenever an entity of a specific type is updated.

The following configuration will create a GitHub issue whenever a scorecard rule result's `Result` property changes from `Passed` to `Not passed`:

**Automation configuration (click to expand)**

**Remember to change `github-org-name` and `github-repo-name` to your GitHub organization name and repository in the highlighted lines.**

Create in Port

```
{
  "identifier": "ruleResultDegraded",
  "title": "Rule result degraded",
  "trigger": {
    "type": "automation",
    "event": {
      "type": "ENTITY_UPDATED",
      "blueprintIdentifier": "_rule_result"
    },
    "condition": {
      "type": "JQ",
      "expressions": [
        ".diff.before.properties.result == \"Passed\"",
        ".diff.after.properties.result == \"Not passed\""
      ],
      "combinator": "and"
    }
  },
  "invocationMethod": {
    "type": "GITHUB",
    "org": "github-org-name",
    "repo": "github-repo-name",
    "workflow": "create-issue-on-rule-degradation.yaml",
    "workflowInputs": {
      "rule_result_name": "{{ .event.context.entityIdentifier }}",
      "entity_link": "{{ .event.diff.after.properties.entity_link }}"
    },
    "reportWorkflowStatus": true
  },
  "publish": true
}
```

* `trigger.condition` checks the rule result's `Result` property before and after the update. The automation will only run for rule results that have been degraded.

* `invocationMethod.workflowInputs` is the payload to be passed to the GitHub workflow upon every execution. In this example, we pass the rule result's identifier and the link to the evaluated entity.

* `invocationMethod.reportWorkflowStatus` is set to `true` to automatically update the action run in Port with the status of the GitHub workflow.

### Backend - GitHub workflow[â](#backend---github-workflow-1 "Direct link to Backend - GitHub workflow")

The `create-issue-on-rule-degradation.yaml` workflow will contain the logic to create a GitHub issue.

**GitHub workflow (click to expand)**

create-issue-on-rule-degradation.yaml

```
name: Create issue when rule is degraded

on:
  workflow_dispatch:
    inputs:
      # Note that the inputs are the same as the payload (workflowInputs) defined in the automation
      rule_result_name:
        description: 'The rule result name'
        required: true
        type: string
      entity_link:
        description: 'A link to the evaluated entity'
        required: true
        type: string

# Grant write access to issues so the workflow can create them
permissions:
  contents: read
  issues: write

jobs:
  send_message:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: create an issue
      uses: dacbd/create-issue-action@main
      with:
        token: ${{ github.token }}
        # By default, the issue will be created in the same repository as the workflow
        repo: ${{ github.context.repo.repo}}
        title: '${{ inputs.rule_result_name }} - degraded rule result'
        body: |
          The rule result ${{ inputs.rule_result_name }} has been degraded.
          See evaluated entity: https://app.port.io${{ inputs.entity_link }}
```
