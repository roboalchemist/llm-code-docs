# Source: https://configcat.com/docs/integrations/zapier.md

# Zapier Zap - Build feature flag workflows

## Connect ConfigCat to hundreds of other apps with Zapier[​](#connect-configcat-to-hundreds-of-other-apps-with-zapier "Direct link to Connect ConfigCat to hundreds of other apps with Zapier")

[ConfigCat's Zap](https://zapier.com/apps/configcat/integrations) lets you connect ConfigCat to 8,000+ other web services. Automated connections called Zaps, set up in minutes with no coding, can automate your day-to-day tasks and build workflows between apps that otherwise wouldn't be possible.

Each Zap has one app as the **Trigger**, where your information comes from and which causes one or more **Actions** in other apps, where your data gets sent automatically.

[ConfigCat's Zap](https://zapier.com/apps/configcat/integrations) can notify you about feature flag and setting changes, so you can easily set up workflows in Zapier (e.g. Send out a Slack message or e-mail when somebody updated a flag).

## Setup[​](#setup "Direct link to Setup")

### Connect ConfigCat[​](#connect-configcat "Direct link to Connect ConfigCat")

1. Log in to your [Zapier account](https://zapier.com/sign-up) or create a new account.
2. Navigate to **App Connections** from the side menu.
3. Click the **Add connection** button and search for **ConfigCat** in the **Add new connection** dialog.
4. Click the **Add connection** button to connect ConfigCat.
5. Get your API credentials for [ConfigCat Public Management API](https://app.configcat.com/my-account/public-api-credentials).
6. Use the generated **Basic auth user name** and **Basic auth password** to connect your ConfigCat account to Zapier.

![zapier\_auth](/docs/assets/zapier_auth.png)

## Usage[​](#usage "Direct link to Usage")

Once ConfigCat is connected, you can start creating an automation! Use a pre-made Zap or create your own with the Zap Editor. Creating a Zap requires no coding knowledge and you'll be walked step-by-step through the setup. Need inspiration? See everything that's possible with [ConfigCat and Zapier](https://zapier.com/apps/configcat/integrations).

### Setup ConfigCat Trigger[​](#setup-configcat-trigger "Direct link to Setup ConfigCat Trigger")

1. Create a new Trigger.
2. Select **ConfigCat** app, **Feature Flag & Setting value changed** as Trigger event and the connected account.
3. Select the Product for which you want to receive notifications about Feature Flag or Setting changes.
4. For more specific notifications, select a Config and/or Environment.

![zapier\_customize](/docs/assets/zapier_customize.png)

### ConfigCat fields[​](#configcat-fields "Direct link to ConfigCat fields")

ConfigCat provide the following fields to include in your flow:

* **When**: When the change happened
* **Who (email), Who (full name)**: Who made the change
* **Where**: To which Config and Environment the change belongs to
* **What**: The exact values that changed

## Example Slack notification setup[​](#example-slack-notification-setup "Direct link to Example Slack notification setup")

### Configuration in Zapier[​](#configuration-in-zapier "Direct link to Configuration in Zapier")

![zapier\_config](/docs/assets/zapier_config.png)

### Result in Slack[​](#result-in-slack "Direct link to Result in Slack")

![zapier\_slack](/docs/assets/zapier_slack.png)

## Need help?[​](#need-help "Direct link to Need help?")

[Contact us](https://configcat.com/support/) if you need any help or you have any awesome improvement ideas for this Zap.
