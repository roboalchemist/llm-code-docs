# Source: https://configcat.com/docs/integrations/vscode.md

# Visual Studio Code - Manage your feature flags from VSCode

[ConfigCat's Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=ConfigCat.configcat-feature-flags) to manage feature flags from Visual Studio Code.

Connect your ConfigCat Product and Config to your Visual Studio Code Workspace. Find your Feature Flag's usages in your code easily. Turn features On/Off right from VSCode. You can also easily modify the linked flags to edit or add new Targeting or Percentage Rules.

This guide will help you with the Visual Studio Code Extensions installation and familiarize you with the Extensions usage.

## Feature overview[​](#feature-overview "Direct link to Feature overview")

* Turn features On / Off right from Visual Studio Code.
* Add Targeting or Percentage Rules from Visual Studio Code.
* Find Feature Flag usages in your code.
* Create Feature Flags within Visual Studio Code.
* Copy a Feature Flag's key to the clipboard.
* View your Products & Configs.
* Create Configs within Visual Studio Code.
* Connect a Config to your Workspace.
* Open a Config on ConfigCat Dashboard.

Your browser does not support the video tag.

## Install extension[​](#install-extension "Direct link to Install extension")

### Install from Visual Studio Code Marketplace[​](#install-from-visual-studio-code-marketplace "Direct link to Install from Visual Studio Code Marketplace")

1. In the Visual Studio Marketplace, open the [ConfigCat Feature Flags Extension](https://marketplace.visualstudio.com/items?itemName=ConfigCat.configcat-feature-flags).
2. Click on the **Install** button.
3. [Configure extension](#configure-extension).

### Install within Visual Studio Code[​](#install-within-visual-studio-code "Direct link to Install within Visual Studio Code")

1. In Visual Studio Code, open the Extensions page, and search for ConfigCat Feature Flags.
2. Click on the **Install** button.
3. [Configure extension](#configure-extension).

## Configure extension[​](#configure-extension "Direct link to Configure extension")

### Authentication[​](#authentication "Direct link to Authentication")

1. Get your API credentials for [ConfigCat Public Management API](https://app.configcat.com/my-account/public-api-credentials).

2. Authenticate ConfigCat in Visual Studio Code by

   <!-- -->

   * clicking on the ConfigCat Feature Flags icon on the Activity Bar and clicking on any of the **Authenticate** buttons.
   * or running the **ConfigCat - Log In** command from the Command Palette.

Your browser does not support the video tag.

### Advanced[​](#advanced "Direct link to Advanced")

This section is for you if you use a dedicated hosted/[on-premise](https://configcat.com/on-premise/) ConfigCat instance. In that case, you can specify your custom ConfigCat URLs in Visual Studio Code. You can do that by executing the `Preferences: Open Workspace Settings` command from the Command Palette and searching for `Extensions/ConfigCat` or clicking the manage button on the ConfigCat Feature Flags extension's page. Important settings:

* **Public Api Base URL**: the base URL for the ConfigCat Public Management API. Defaults to: <https://api.configcat.com>.
* **Dashboard Base URL**: the base URL for ConfigCat Dashboard. Defaults to: <https://app.configcat.com>.

## Usage of ConfigCat Feature Flags Views[​](#usage-of-configcat-feature-flags-views "Direct link to Usage of ConfigCat Feature Flags Views")

The ConfigCat Feature Flags Views can be opened by clicking the ConfigCat Feature Flags icon on the Visual Studio Code's Activity Bar. There are three different views.

### Feature Flags & Settings View[​](#feature-flags--settings-view "Direct link to Feature Flags & Settings View")

After you successfully connect your ConfigCat Config to your Visual Studio Code Workspace, open the Feature Flags & Settings View and:

* View the connected Config's Feature Flags.
* View or Update your Feature Flag's value.
* Create new Feature Flags.
* Copy a Feature Flag's key to the clipboard.
* Find your Feature Flag's usages in your code.

Your browser does not support the video tag.

#### View or Update your Feature Flag's value[​](#view-or-update-your-feature-flags-value "Direct link to View or Update your Feature Flag's value")

1. Open the **Feature Flags & Settings** view.
2. Find the Flag and click the **View or Update Feature Flag values** icon next to the Flag name.
3. Select the Environment.
4. See the Feature Flag in the opened tab.
5. You can turn your features On / Off right from the opened tab.
6. You can add new Targeting Rules with User, Segment or Prerequisite conditions with a large selection of Comparators. [Read more about Targeting.](https://configcat.com/docs/docs/targeting/targeting-overview/.md)
7. You can add new Percentage Options to Feature Flags or Targeting Rules

#### Create a new Feature Flag[​](#create-a-new-feature-flag "Direct link to Create a new Feature Flag")

1. Open the **Feature Flags & Settings** view.
2. Click the **+** in the view header.
3. Select the Setting type.
4. Enter the new Feature Flag name.
5. Enter the new Feature Flag key.
6. Add a hint to your Feature Flag (optional).
7. Select **Yes** to confirm the Flag creation.

#### Copy a Feature Flag's key to the clipboard[​](#copy-a-feature-flags-key-to-the-clipboard "Direct link to Copy a Feature Flag's key to the clipboard")

1. Open the **Feature Flags & Settings** View.
2. Find the Flag and click the **Copy Key to clipboard** icon next to the Flag name.

#### Find your Feature Flag's usages in your code[​](#find-your-feature-flags-usages-in-your-code "Direct link to Find your Feature Flag's usages in your code")

1. Open the **Feature Flags & Settings** view.
2. Find the Flag and click the **Find usage** icon next to the Flag name.
3. See the search results in the opened tab.

### Products & Configs View[​](#products--configs-view "Direct link to Products & Configs View")

Manage your products and configs on the **Products & Configs** view by performing the following actions:

* View all of your Products & Configs.
* Create Configs under a Product.
* Connect a Config to your current Workspace.
* Open your Configs on the ConfigCat Dashboard.

Your browser does not support the video tag.

#### Create a new Config under a product[​](#create-a-new-config-under-a-product "Direct link to Create a new Config under a product")

1. Open the **Products & Configs** view.
2. In the products list, click the **+** icon next to the product where you want to create the new config.
3. Enter a name for the new Config.
4. Add a description to your Config (optional).
5. Connect the new config to your current Workspace (optional).

#### Connect a Config to your current Workspace[​](#connect-a-config-to-your-current-workspace "Direct link to Connect a Config to your current Workspace")

1. Open the **Products & Configs** view.
2. Find the Config you want to connect to your current Workspace under your product list.
3. Click the **Connector** icon next to the Config in the list.
4. You can see the Config's Feature Flags in the **Feature Flags & Setting** view.

#### Open your Configs on the ConfigCat Dashboard[​](#open-your-configs-on-the-configcat-dashboard "Direct link to Open your Configs on the ConfigCat Dashboard")

1. Open the **Products & Configs** view.
2. Find the Config you want to connect to your current Workspace under your product list.
3. Click the **Open Config in ConfigCat Dashboard** icon next to the Config in the list.

### Help & Feedback View[​](#help--feedback-view "Direct link to Help & Feedback View")

The **Help & Feedback** view provides quick links to open ConfigCat's Documentation and Dashboard and allows you to report issues.
