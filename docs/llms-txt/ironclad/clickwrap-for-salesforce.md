# Source: https://clickwrap-developer.ironcladapp.com/docs/clickwrap-for-salesforce.md

# Salesforce Integration

It may be needed for you to write Ironclad Clickwrap data back to Salesforce once an agreement has been accepted.

To integrate Clickwrap agreements back into Salesforce, see the options below on using Ironclad Webhooks to send data to Opportunities, Accounts, Contacts, and more.

## Send Ironclad Clickwrap Data to Salesforce

There are a couple of ways that can accomplish this.

1. Using Ironclad Clickwrap Webhooks in combination with a middleware service like Zapier.
2. Using Salesforce Apex code to retrieve data from the Ironclad Clickwrap Webhook.

### Webhooks with Zapier

Depending on the type of event you want to trigger the process (we normally see Agreed events), you'll need to make sure that you set this up in your Ironclad Clickwrap Site [integrations page](https://app.pactsafe.com/settings/integrations). Webhooks give you the ability to be notified when an acceptance has occurred and handle it as needed. For example, using a platform like Zapier allows you to hook into Ironclad Clickwrap webhooks and update data within your Salesforce account.

Webhooks are typically the easiest way to get data back to Salesforce when you may not have immediate Salesforce development resources. If you do have Salesforce help, the next section covers more advanced methods.

For more information on writing back data to Salesforce using Zapier, visit our [Integrating Ironclad Clickwrap with Zapier](https://clickwrap-developer.ironcladapp.com/docs/salesforce-integration-via-zapier) guide.

### Salesforce Apex

Salesforce Apex allows teams to build custom flow and transaction control statements on Salesforce. Teams can create complex business processes without middleware.

An Apex Class will be used to set up as a webhook event listener. The Apex Class will also be used to parse the body from the webhook and added to the Salesforce Object.

For more information on writing back data to Salesforce with Apex, visit our [Integrating Ironclad Clickwrap with Apex](https://clickwrap-developer.ironcladapp.com/docs/salesforce-integration-via-salesforce-apex) guide.