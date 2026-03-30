# Source: https://docs.port.io/guides/all/nudge-pr-reviewers.md

# Nudge Pull Request Reviewers

In the following guide, we are going to create a self-service action in Port that uses `Send Slack message` backend to nudge PR reviewers with a kind message.

Available Github Integrations

This guide includes one or more steps that require integration with GitHub.<br /><!-- -->Port supports two GitHub integrations:

* **GitHub (Legacy)** - uses a GitHub app, which is soon to be deprecated.
* **GitHub (Ocean)** - uses the [Ocean framework](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md), recommended for new integrations.

Both integration options are present in this guide via tabs, choose the one that fits your needs.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Faster Merges**: Remind reviewers of open PRs to reduce delays.
* **Better Code**: Encourage timely reviews for quicker feedback.
* **Smoother Workflow**: Prevent bottlenecks that hinder development progress.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* GitHub (Legacy)
* GitHub (Ocean)

1. Install Port's GitHub app by clicking [here](https://github.com/apps/getport-io/installations/new).

1) Install [GitHub ocean](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md).

2. Set up a slack app:

   <!-- -->

   * Go to your [slack apps page](https://api.slack.com/apps).
   * Create a new app or use an existing one.
   * Enable Incoming Webhooks and create a new webhook.
   * Choose the target Slack channel for notifications.
   * Copy the generated webhook URL for use as the `SLACK_WEBHOOK_URL`.

## Port configuration[â](#port-configuration "Direct link to Port configuration")

1. To create the Port action, go to the [self-service page](https://app.getport.io/self-serve):

   <!-- -->

   * Click on the `+ New Action` button.
   * Click on the `{...} Edit JSON` button.
   * Copy and paste the following JSON configuration into the editor.
   * Click `Save`

Port Action: Nudge Pull Request Reviewers

tip

* `<SLACK_WEBHOOK_URL>` - The webhook URL obtained from slack

Create in Port

```
{
  "identifier": "nudge_reviewers",
  "title": "Nudge Reviewers",
  "icon": "Slack",
  "description": "Remind reviewers about PR",
  "trigger": {
    "type": "self-service",
    "operation": "DAY-2",
    "userInputs": {
      "properties": {},
      "required": []
    },
    "blueprintIdentifier": "githubPullRequest"
  },
  "invocationMethod": {
    "type": "SLACK",
    "url": "<SLACK_WEBHOOK_URL>",
    "agent": false,
    "synchronized": true,
    "method": "POST",
    "headers": {},
    "body": {
      "text": "\n*Reminder: Pending Pull Request Review*\nThis PR needs your attention!\n\n*PR:* <{{ .entity.properties.link }}|{{ .entity.title }}>\n*Reviewers:* {{ .entity.properties.reviewers }}\nReview PR: {{ .entity.properties.link }}"
    }
  },
  "requiredApproval": false
}
```

## Let's test it\![â](#lets-test-it "Direct link to Let's test it!")

Trigger the action from the [self-service](https://app.getport.io/self-serve) page of your Port application.

![](/img/self-service-actions/setup-backend/slack-message/nudgeSlack.png)

<br />

<br />

Done! ð You can now send a reminder to PR reviewers.
