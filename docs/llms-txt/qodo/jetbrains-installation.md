# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/getting-started/setup-and-installation/jetbrains-installation.md

# JetBrains Installation

### Install Qodo <a href="#install-qodo-gen" id="install-qodo-gen"></a>

Visit [Qodo's page on Jetbrains Marketplace](https://plugins.jetbrains.com/plugin/21206-qodo-gen-formerly-codiumate-) to install Qodo IDE Plugin.

Alternatively, follow these steps to install the plugin from within your Jetbrains IDE:

1. Open the settings menu in your Jetbrains IDE by clicking the cog wheel on the top right.
2. Select **Plugins**.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2F4BxJOkPxBBFf8raLOY0M%2FScreenshot%202025-03-05%20at%2011.29.59.png?alt=media&#x26;token=9e93188c-b6c1-4cd4-9583-7d81d6df436e" alt="" width="219"><figcaption></figcaption></figure>

3. Type **Qodo** in the search bar.
4. Click the Install button.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FNCBdBT6SresNwZAVko1u%2FScreenshot%202025-03-05%20at%2011.31.31.png?alt=media&#x26;token=b11cd821-c79f-4e13-b60a-7a2269311602" alt="" width="321"><figcaption></figcaption></figure>

### Activate Qodo IDE Plugin

1. Following installation, restart your IDE to activate Qodo IDE Plugin.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FK2XYG2ToAHIjbsVdvrQm%2FScreenshot%202025-03-05%20at%2011.35.01.png?alt=media&#x26;token=44297a0e-0bf9-4d6f-ba64-1bc764aeaf3f" alt="" width="421"><figcaption></figcaption></figure>

2. After restarting, the Qodo icon should appear in the IDE's sidebar on the left side.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FcVfanZ6Wk9IxgFyZ6EGI%2FScreenshot%202025-02-23%20at%2012.22.31.png?alt=media&#x26;token=20b693cf-02ac-4c3e-884e-0923c318a25b" alt="" width="317"><figcaption></figcaption></figure>

### Android Studio support JCEF <a href="#android-studio-support-jcef" id="android-studio-support-jcef"></a>

Qodo Plugin uses JCEF (Java Chromium Embedded Framework) to create a webview component in the plugin's tool window. By default, most IntelliJ-based IDEs come with a boot runtime that includes JCEF. However, Android Studio (and some other versions of IntelliJ-based IDEs) utilize a boot runtime lacking JCEF, which prevents the plugin from loading in these environments.

Also in some cases JCEF could persist but not been initialised.

To address this issue:

1. Navigate to the "Help" -> "Find Action..." and find(type) "Registry". Here disable `ide.browser.jcef.sandbox.enable` option.
2. Navigate to the "Help" -> "Find Action..." and find(type) "Choose Boot Runtime for the IDE" dialog. Here, you can select a boot runtime equipped with JCEF.
3. Restart the IDE.

If the issue persist, please open an issue in our [GitHub issue tracker](https://github.com/Codium-ai/codiumai-jetbrains-release/issues) or [contact support](https://docs.qodo.ai/qodo-documentation/support-and-developers-community).
