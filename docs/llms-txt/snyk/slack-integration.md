# Source: https://docs.snyk.io/integrations/jira-and-slack-integrations/slack-integration.md

# Slack integration

{% hint style="warning" %}
Snyk recommends that all customers use the [Slack App](https://docs.snyk.io/integrations/jira-and-slack-integrations/slack-app), as the Slack integration is outdated.
{% endhint %}

You can set up Slack to receive Snyk’s alerts about new vulnerabilities that affect your Projects and new upgrades or patches that have become available.

{% hint style="info" %}
Vulnerabilities detected on initial import of projects are not sent to Slack immediately.
{% endhint %}

## Slack notification types

You can get the following alerts in Slack:

A newly disclosed vulnerability:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-03136f44e5c6585fdd804e3192faa15de4bca883%2Fimage%20(23)%20(1).png?alt=media" alt="Newly disclosed vulnerability notification"><figcaption><p>Newly disclosed vulnerability notification</p></figcaption></figure>

A new upgrade or patch is available for a vulnerability that you previously ignored or patched.

## Set up the Slack integration

To set up the integration, you must generate a Slack webhook. You can do this either via the [Incoming WebHooks app](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks) or by [creating your own Slack app](https://api.slack.com/incoming-webhooks).

Once you have generated your Slack Webhook URL, go to your **Manage Organization** settings and enter the URL.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b797ba9af4f005c2b23e6b20e1f6af86d43f2dac%2Fimage%20(24).png?alt=media&#x26;token=b4c2c328-d6f1-488f-a4d4-a48768b9dd28" alt="Enter URL of the Slack webhook"><figcaption><p>Enter URL of the Slack webhook</p></figcaption></figure>

{% hint style="info" %}
Only webhooks created with Slack Apps are supported; webhooks created with Slack Workflows are not supported.
{% endhint %}
