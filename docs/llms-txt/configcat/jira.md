# Source: https://configcat.com/docs/integrations/jira.md

# Jira Cloud Plugin - Manage feature flags from Jira

The [ConfigCat Feature Flags Jira Cloud Plugin](https://marketplace.atlassian.com/1222421) allows you to connect your Jira Issues and feature flags. Create or link existing flags to your Jira issues without leaving your Jira instance.

Turn features On/Off right from a linked Issue on your Jira board. You can also easily modify the linked flags to edit or add new Targeting or Percentage Rules.

This guide will help you with the plugin installation and familiarise you with the plugin usage.

info

This integration is for Jira Cloud. It does not work on Jira Data Center or Jira Server instances.

## Installation[​](#installation "Direct link to Installation")

1. Add [ConfigCat Feature Flags](https://marketplace.atlassian.com/1222421) to your Jira Cloud instance.
2. Select **Configure**.
3. Copy your ConfigCat Public API credentials to the inputs. Read more about [ConfigCat Public API credentials here](https://app.configcat.com/my-account/public-api-credentials).
4. Click **Authorize**.

info

Every Jira user must authorize ConfigCat in Jira who wants to use the ConfigCat Feature Flags Plugin.

Your browser does not support the video tag.

## Usage[​](#usage "Direct link to Usage")

### Linking existing feature flags[​](#linking-existing-feature-flags "Direct link to Linking existing feature flags")

1. Navigate to any Issue on your Jira board.
2. Open the **ConfigCat Feature Flag** issue context.
3. On the **Link existing** tab, select a ConfigCat Product, Config, Environment, and Feature Flag to be linked to your Issue.
4. When linked, you can manage the selected feature flag from this Issue.

Your browser does not support the video tag.

### Creating new feature flags[​](#creating-new-feature-flags "Direct link to Creating new feature flags")

1. Navigate to any Issue on your Jira board.
2. Open the **ConfigCat Feature Flag** issue context.
3. On the **Create and Link** tab, select a ConfigCat Product and Config where you want to create the feature flag.
4. Set up your feature flag.
5. Select which environment you would like to link to this item.
6. When linked, you can manage the selected feature flag from this Issue.

Your browser does not support the video tag.

### View and Edit linked feature flags[​](#view-and-edit-linked-feature-flags "Direct link to View and Edit linked feature flags")

1. Open an Issue on your Jira board with a linked feature flag.
2. See the linked feature flags in the **Feature Flag (ConfigCat)** issue section.
3. You can manage the selected feature flag from this Issue.
4. You can add new Targeting Rules or Percentage Options to Feature Flags.
5. You can add new Targeting Rules with User, Segment or Prerequisite Conditions with a large selection of Comparators. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md)
6. You can remove Targeting Rules as well.

Your browser does not support the video tag.

### Remove linked feature flags[​](#remove-linked-feature-flags "Direct link to Remove linked feature flags")

1. Open an Issue on your Jira board with a linked feature flag.
2. Remove the linked feature flag by opening the **More menu** and selecting the **Remove from Issue** option.

Your browser does not support the video tag.

### View flag status in Releases[​](#view-flag-status-in-releases "Direct link to View flag status in Releases")

1. Open an Issue on your Jira board with a linked feature flag.
2. Check the **Releases** field values in the issue **Details** section to see the linked feature flags status in the Issue.
3. Click it for a more detailed dialog.

Your browser does not support the video tag.

1. Open a version in the Jira project's Release Hub page to see the related issues feature flag status.
2. Click it for a more detailed dialog.

Your browser does not support the video tag.

info

This plugin doesn't implement the **Releases - Create/Connect feature flag** action. Instead, you can create or link feature flags from the ConfigCat Feature Flags section below the Details section of the Issue.

### View linked issues in ConfigCat[​](#view-linked-issues-in-configcat "Direct link to View linked issues in ConfigCat")

1. View linked issues next to your Feature Flags in ConfigCat and jump to the Jira Issue directly.

Your browser does not support the video tag.
