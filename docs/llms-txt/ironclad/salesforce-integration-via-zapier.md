# Source: https://clickwrap-developer.ironcladapp.com/docs/salesforce-integration-via-zapier.md

# Salesforce Integration (via Zapier)

## Overview

This guide provides a framework for integrating Ironclad Clickwrap and Salesforce, utilizing Zapier as a middleware tool.

This guide will walk through how to write Ironclad Clickwrap data back to Salesforce once a Contract has been signed or agreed to. This option will use Zapier's connectors with [Ironclad Clickwrap's Webhooks](https://clickwrap-developer.ironcladapp.com/docs/working-with-pactsafe-webhooks) and Salesforce.

## Requirements

### Ironclad Requirement

* **Ironclad Clickwrap Account:** Add a template to a group and publish the group. The acceptance of this contract will trigger a new Salesforce record.
* **Webhook Access:** Webhooks will be created on the Ironclad Clickwrap Site [integrations page](https://app.pactsafe.com/settings/integrations).
* **Reference:** Please see [Ironclad Clickwrap's Webhooks](https://clickwrap-developer.ironcladapp.com/docs/working-with-pactsafe-webhooks) documentation for the most up-to-date details on webhooks.

### Zapier Requirement

* Premium Apps are required. Visit Zapier's [documentation for Salesforce integration](https://help.zapier.com/hc/en-us/articles/8496020790925-How-to-Get-Started-with-Salesforce-on-Zapier).

### Salesforce Requirement

* A Salesforce account is required along with a user with the correct read/write permissions on the desired Object.

## Setup

## Zapier Setup

### Create a new Zap

To get started on building integration with Ironclad Clickwrap and Salesforce, start within Zapier and follow the steps below:

1. Create a new Zap and select "Webhooks by Zapier" as your Trigger.

<Image title="Screen Shot 2022-11-09 at 8.36.58 AM.png" alt={2566} width="80%" src="https://files.readme.io/0f85e3a-Screen_Shot_2022-11-09_at_8.36.58_AM.png" />

2. Select "Catch Hook" and press "Continue"

<Image title="Screen Shot 2022-11-09 at 8.43.04 AM.png" alt={1820} width="80%" src="https://files.readme.io/08bb87b-Screen_Shot_2022-11-09_at_8.43.04_AM.png" />

3. Click "Continue" again (there's no child key)
4. Copy the webhook URL to your clipboard!

## Ironclad Setup

Now that you have a webhook URL, you'll be able to start creating a Webhook within Ironclad. You can get to Webhooks in Ironclad Clickwrap by going to [Settings > Integrations](https://app.pactsafe.com/settings/integrations).

**For this example, we're going to set up a Webhook for when any contract is agreed upon.**

1. Click "Add Webhook" in Integrations

<Image title="Screen Shot 2022-11-09 at 8.46.07 AM.png" alt={1430} width="80%" src="https://files.readme.io/0a5da9c-Screen_Shot_2022-11-09_at_8.46.07_AM.png" />

2. Paste in the URL you copied to your clipboard from Zapier
3. Use HTTP "POST" when setting up your webhook
4. Select the toggle for "Activity - Agreed"

<Image title="Screen Shot 2022-11-09 at 8.47.35 AM.png" alt={2646} width="80%" src="https://files.readme.io/906fe96-Screen_Shot_2022-11-09_at_8.47.35_AM.png" />

To test the Webhook with the data, press "Save" and "Test Webhook". You will now see a test notification under "Test Notifications" on the left panel. This will send a test event to Zapier and the Zap that was created.

## Test Webhook in Zapier

After you've sent a test from Ironclad, you can go back to Zapier and click "Test trigger" and you should see the green checkbox confirming the Webhook successfully triggered in Zapier.

## Create a Filter in Zapier (Optional)

You can create additional actions like filters prior to connecting to Salesforce. Creating a filter step will allow you to set up criteria to use a specific set of Clickwrap agreements.

For example, you can filter a specific Clickwrap Group so that only Order Forms will create a record with Salesforce and regular Sign Up Clickwraps will not create a record.

1. Add a new Action and select "Filter"

<Image title="Screen Shot 2022-11-09 at 8.52.51 AM.png" alt={1820} width="80%" src="https://files.readme.io/891fb89-Screen_Shot_2022-11-09_at_8.52.51_AM.png" />

2. To create a criteria, select a data field like "Groups".
3. Choose "(Text) exactly matches" for condition.
4. Then input the Group number.
5. Press "Continue".

<Image title="Screen Shot 2022-11-09 at 9.31.47 AM.png" alt={1804} width="80%" src="https://files.readme.io/f51119c-Screen_Shot_2022-11-09_at_9.31.47_AM.png" />

Only clickwraps agreed with the criteria will move forward to the next step in Salesforce.

## Create a Salesforce Action in Zapier

The final step is to create a Salesforce Action in Zapier which will create a new lead for each Agreed Clickwrap.

Here's a quick example of how you can create a new Lead when for an "agreed" Clickwrap event:

1. Create a new Action
2. Search and select "Salesforce"
3. Select "Create Record" for the event
4. Press "Continue"

<Image title="Screen Shot 2022-11-09 at 2.28.58 PM.png" alt={1804} width="80%" src="https://files.readme.io/5d177b2-Screen_Shot_2022-11-09_at_2.28.58_PM.png" />

For the next step, log into your Salesforce account and ensure your profile has the right read/write permissions.

After connecting Salesforce, you will be able to select a specific Object.

Under Salesforce Object, pick "Lead" to create new records under the Lead Object. You can also use another Object if necessary.

Zapier will automatically pull all the fields under the "Lead" Object. All required fields will need a value or a field mapped over.

You can map over a field from the Ironclad webhook with the following steps:

1. Click into the empty box for each field
2. Select "1. Catch Hook in Webhooks by Zapier"
3. Select the available data options from the webhook.

<Image title="Screen Shot 2022-11-09 at 4.26.27 PM.png" alt={1808} width="80%" src="https://files.readme.io/1f25e13-Screen_Shot_2022-11-09_at_4.26.27_PM.png" />

Repeat the mapping exercise for all the required fields.

Finally, press "Continue" and Test the Action.

The test will automatically create a fake Lead in Salesforce and you can now Publish your Zap.