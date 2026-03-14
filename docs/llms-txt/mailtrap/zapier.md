# Source: https://docs.mailtrap.io/guides/integrations/zapier.md

# Zapier

<a href="https://zapier.com/apps/mailtrap/integrations" class="button primary">View on Zapier Marketplace</a>

## Overview

Using the Mailtrap integration with Zapier, you can automate email sending by connecting Mailtrap to over 7,000 other applications without any coding. This guide shows you how to set up the integration, create automations, and manage your connections.

### Connecting Mailtrap to Zapier

{% stepper %}
{% step %}
Log in to your [Zapier account](https://zapier.com/sign-up) or create a new account.
{% endstep %}

{% step %}
Navigate to **Apps** in the left-hand side menu.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-c715329cf912cfa9c52f45e1c02fc5660042171f%2Fmailtrap-integration-with-zapier-1.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Click **Add connection**.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-4932c1ff9f9db6fd172b7685999acaf26b253866%2Fmailtrap-integration-with-zapier-2.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Type *Mailtrap* in the **App name** search bar.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-d237e54aa700a201a49f384d9ef595cca07da594%2Fmailtrap-integration-with-zapier-3.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Enter your Mailtrap API key to allow Zapier to access your account.&#x20;

**Note**: This should be the token for the domain you've added and verified in Mailtrap. You'll find it in the **Settings** → **API Tokens** menu.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-f835167a9374a4b528e45d748b9e98045a2f37b1%2Fmailtrap-integration-with-zapier-4.png?alt=media" alt="" width="375"></div>
{% endstep %}
{% endstepper %}

### Creating an automation

To set up trigger-based email sending via Mailtrap in Zapier, you need to create a Zap.

A Zap is a workflow connecting multiple apps that consists of a trigger (an event that starts a Zap) and one or more actions (events the Zap performs).

#### Using Copilot

{% stepper %}
{% step %}
Describe the workflow you want to create to Copilot.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-cb3f48ff6428b18a80bbf6945a03e9f9ca721664%2Fmailtrap-integration-with-zapier-5.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Add some or all the steps created by Copilot to the Zap or continue to prompt the chatbot to add or replace steps.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-7883d46847787e437ab2b871b7db208bbbc1374c%2Fmailtrap-integration-with-zapier-6.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Configure the required fields for sending an email. The from email should contain the same sending domain you added and verified in Mailtrap.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-6e292ab9e6ffd8f632920ecfe62f96d3b2fa3f30%2Fmailtrap-integration-with-zapier-7.png?alt=media" alt="" width="188"></div>
{% endstep %}

{% step %}
Send a test email to Mailtrap (optional).

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-75ff7727272f2cacfee7b8eceb623f146f5d25b9%2Fmailtrap-integration-with-zapier-8.png?alt=media" alt="" width="188"></div>
{% endstep %}

{% step %}
Publish the Zap.
{% endstep %}
{% endstepper %}

#### Manually

{% stepper %}
{% step %}
Select an event (trigger) to start your Zap.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-70c8501e09c3048a42efc669c4697d782482da00%2Fmailtrap-integration-with-zapier-9.png?alt=media" alt="" width="375"></div>

Zapier's app directory contains 7,000+ apps with triggers and actions available for each.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-dc9ec52039e60da7b768bd8e68fbd69a58aa531f%2Fmailtrap-integration-with-zapier-10.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Search for and select **Mailtrap** as the action for your Zap to run.
{% endstep %}

{% step %}
Select **Send Email** as the action event.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-7ddfe0296c4fe8149de5007c0a7d8c106c2fb4fe%2Fmailtrap-integration-with-zapier-12.png?alt=media" alt="" width="188"></div>
{% endstep %}

{% step %}
Configure the required fields for sending an email.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-6e292ab9e6ffd8f632920ecfe62f96d3b2fa3f30%2Fmailtrap-integration-with-zapier-7.png?alt=media" alt="" width="188"></div>
{% endstep %}

{% step %}
Send a test email to Mailtrap (optional).

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-75ff7727272f2cacfee7b8eceb623f146f5d25b9%2Fmailtrap-integration-with-zapier-8.png?alt=media" alt="" width="188"></div>
{% endstep %}

{% step %}
Publish the Zap.
{% endstep %}
{% endstepper %}

### Removing Mailtrap credentials from Zapier

{% stepper %}
{% step %}
Navigate to **Apps** in the left-hand side menu.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-c715329cf912cfa9c52f45e1c02fc5660042171f%2Fmailtrap-integration-with-zapier-1.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Click on your Mailtrap connection.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-06e2db50e8446bdc078d9c32aa7ca6b37dc4364e%2Fmailtrap-integration-with-zapier-16.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Click the three-dot menu and then **Delete** in the dropdown menu. Using the same menu, you can edit the connection name, reconnect, test the connection, and view Zaps created using the connection.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-8c1a6c84de3c03bbf9d2b2e845f861af302b852c%2Fmailtrap-integration-with-zapier-17.png?alt=media" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

## Next steps

After setting up your Mailtrap and Zapier integration, you can create unlimited Zaps to automate your email workflows and connect your favorite apps seamlessly.
