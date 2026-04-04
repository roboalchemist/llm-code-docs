# Source: https://configcat.com/docs/integrations/intellij.md

# JetBrains/IntelliJ Plugin - Manage your feature flags from JetBrains/IntelliJ IDEs

Copy page

[ConfigCat's JetBrains/IntelliJ IDE plugin](https://plugins.jetbrains.com/plugin/26096-configcat-feature-flags) to manage feature flags from IDEs.

Connect your ConfigCat Product and Config to your JetBrains/IntelliJ IDE. Find your Feature Flag's usages in your code easily.

This guide will help you install the JetBrains/IntelliJ IDE Plugin and familiarize you with its usage.

## Feature overview[​](#feature-overview "Direct link to Feature overview")

* View your Feature Flags within the IDE.
* Create Feature Flags within the IDE.
* Open a Feature Flag on the ConfigCat Dashboard.
* Find Feature Flag usages in your code.
* Copy a Feature Flag's key to the clipboard.
* View your Products & Configs.
* Create Configs within the IDE.
* Open a Config on ConfigCat Dashboard.

Your browser does not support the video tag.

## Install plugin[​](#install-plugin "Direct link to Install plugin")

### Install within the IDE from Marketplace[​](#install-within-the-ide-from-marketplace "Direct link to Install within the IDE from Marketplace")

1. In your IDE, open the **File** > **Settings/Preferences** menu.
2. Go to the **Plugin** page and select the **Marketplace** tab.
3. Search for **ConfigCat Feature Flags**.
4. **Install** the plugin.
5. Configure the plugin ([see below](#configure-extension)).

### Install manually within the IDE[​](#install-manually-within-the-ide "Direct link to Install manually within the IDE")

1. Download the latest release from [GitHub](https://github.com/configcat/intellij-plugin/releases/latest) or from [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/26096-configcat-feature-flags).
2. In your IDE, open the **File** > **Settings/Preferences** menu.
3. Go to the **Plugin** page and open the **Gear Icon** menu.
4. Select the **Install plugin from disk...** option.
5. Configure the plugin ([see below](#configure-extension)).

### Compatible IDEs[​](#compatible-ides "Direct link to Compatible IDEs")

The plugin is compatible with the following IDEs. Check the plugin [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/26096-configcat-feature-flags) page for the full, detailed compatibility list.

* Android Studio
* Aqua
* CLion
* DataGrip
* DataSpell
* GoLand
* IntelliJ IDEA (Community & Ultimate)
* MPS
* PhpStorm
* PyCharm (Community & Professional)
* Rider
* RubyMine
* RustRover
* WebStorm
* Writerside

## Configure extension[​](#configure-extension "Direct link to Configure extension")

### Authentication[​](#authentication "Direct link to Authentication")

1. Get your API credentials for [ConfigCat Public Management API](https://app.configcat.com/my-account/public-api-credentials).
2. In your IDE, open the **File** > **Settings/Preferences** menu.
3. Search for **ConfigCat Feature Flags** page.
4. Fill out the **Basic auth user name** and **Basic auth password** inputs.

Your browser does not support the video tag.

### Advanced[​](#advanced "Direct link to Advanced")

This section is for you if you use a dedicated hosted/[on-premise](https://configcat.com/on-premise/) ConfigCat instance. In that case, you can specify your custom ConfigCat URLs in the IDE.

1. In your IDE, open the **File** > **Settings/Preferences** menu.
2. Search for **ConfigCat Feature Flags** page.
3. Fill out the **Public Api Base URL** and **Dashboard Base URL** inputs.

* `Public Api Base URL`: the base URL for the ConfigCat Public Management API. Defaults to: <https://api.configcat.com>.
* `Dashboard Base URL`: the base URL for ConfigCat Dashboard. Defaults to: <https://app.configcat.com>.

## Usage of ConfigCat Feature Flags Plugin[​](#usage-of-configcat-feature-flags-plugin "Direct link to Usage of ConfigCat Feature Flags Plugin")

The ConfigCat Feature Flags Tool Window can be opened by clicking the ConfigCat Feature Flags icon on the side of the IDE main window.

### Feature Flags & Settings tab[​](#feature-flags--settings-tab "Direct link to Feature Flags & Settings tab")

After you successfully configured your ConfigCat account in the **Settings**, you can use the **Feature Flags & Settings** tab and:

* View all of your Products, Configs and Feature Flags.
* Create new Configs and Feature Flags.
* Open your Configs and Feature Flags on the ConfigCat Dashboard.
* Copy a Feature Flag's key to the clipboard.
* Find your Feature Flag's usages in your code.

Your browser does not support the video tag.

#### Create a new Feature Flag[​](#create-a-new-feature-flag "Direct link to Create a new Feature Flag")

1. Select the Config in the tree where you want to create your new flag.
2. Click the **+** button on the action bar to open the **Create Flag** dialog.
3. Select the setting type.
4. Enter the new Feature Flag name.
5. Enter the new Feature Flag key.
6. Add a hint to your Feature Flag (optional).
7. Select **OK** to confirm the Flag creation.

#### Copy a Feature Flag's key to the clipboard[​](#copy-a-feature-flags-key-to-the-clipboard "Direct link to Copy a Feature Flag's key to the clipboard")

1. Select the Feature Flag in the tree whose key you want to copy.
2. Click the **Copy** button on the action bar to copy the key to the clipboard.

#### Open your Feature Flags on the ConfigCat Dashboard[​](#open-your-feature-flags-on-the-configcat-dashboard "Direct link to Open your Feature Flags on the ConfigCat Dashboard")

1. In the tree, select the Feature Flag you want to open in the Dashboard.
2. Click the **Open Config in ConfigCat Dashboard** button on the action bar to open the Feature Flag in the Dashboard.

#### Find your Feature Flag's usages in your code[​](#find-your-feature-flags-usages-in-your-code "Direct link to Find your Feature Flag's usages in your code")

1. Select the Feature Flag in the tree you want to search.
2. Click the **Find Usage** button on the action bar.
3. See the search results in the opened dialog.

#### Create a new Config under a product[​](#create-a-new-config-under-a-product "Direct link to Create a new Config under a product")

1. Select the Products in the tree where you want to create your new config.
2. Click the **+** button on the action bar to open the **Create Config** dialog.
3. Enter a name for the new config.
4. Add a hint to your config (optional).
5. Select **OK** to confirm the Config creation.

#### Open your Configs on the ConfigCat Dashboard[​](#open-your-configs-on-the-configcat-dashboard "Direct link to Open your Configs on the ConfigCat Dashboard")

1. Select the Config which you want to open in the Dashboard.
2. Click the **Open Config in ConfigCat Dashboard** button on the action bar to open the Config in the Dashboard.

info

The actions are available by right click menu as well.

### Help & Feedback Tab[​](#help--feedback-tab "Direct link to Help & Feedback Tab")

The Help & Feedback tab provides quick links to open ConfigCat's Documentation and Dashboard and allows you to report issues.
