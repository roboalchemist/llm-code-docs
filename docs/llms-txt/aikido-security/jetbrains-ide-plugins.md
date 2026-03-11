# Source: https://help.aikido.dev/ide-plugins/jetbrains-ide-plugins.md

# JetBrains IDE

Aikido integrates with the majority of Jetbrains IDEs and scans your codebases for **secrets, API keys SAST** code issues and **SCA**. It runs scans whenever you open or save a file.

Every time you make and save changes in a file, a scan runs. If any issues are detected, they are highlighted in the editor and also displayed in the Problems panel. When you hover over a detected SAST issue, additional context about the problem is provided.

![Code editor highlighting security warnings in an Express.js application, including missing security headers.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a195d2c2a534d1a8c4d829e38e1b6db911dc64ce%2Fjetbrains-ide-plugins_530564ed-8698-4161-b13e-4aa301e00836.png?alt=media)

## Supported IDEs <a href="#supported-ides" id="supported-ides"></a>

We support the majority of Jetbrain IDEs

* IntelliJ IDEA (Java/Kotlin/Spring)
* GoLand (Go/JS/TS)
* PhpStorm (PHP/Laravel/Symfony)
* PyCharm (Python/Django)
* Rider (C#/.NET/ASP.NET)
* WebStorm (JS/TS/React)
* RubyMine (Ruby/Rails)
* RustRover (Rust)
* Android Studio (Android)

## How to Install and Test <a href="#how-to-install-and-test" id="how-to-install-and-test"></a>

> This plugin is only available on paid plans.

**Step 1.** Head over to the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/24993-aikido-security) and click **Get.** After installation, you will be asked to add your personal access token (step 2).

**Step 2.** In Aikido, go to the [JetBrains IDE Integration Screen](https://app.aikido.dev/settings/integrations/ide/jetbrains) and create your token.

![JetBrains IDE Plugin user access and activity log with token generation options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7e3828aa171c841f6bea936b588509c517d00e99%2Fjetbrains-ide-plugins_3fefe56c-0d6a-43b6-a61d-6bf47f6c7118.png?alt=media)

**Step 3.** Check out the examples in our docs on the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/24993-aikido-security) to test whether everything works well.

### Enabling Code Quality (BETA)

1. Open **Settings > Tools > Aikido Security**
2. Click **Enable Code Quality Scanning**.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FB4Ptk4zeoBDtPG2xCkjs%2Fimage.png?alt=media&#x26;token=b3e9f8e1-8887-4bb3-ab20-57d3969a6288" alt=""><figcaption></figcaption></figure>

This will add a Code Quality Issues section to the Current File Scan Results view in the Aikido Toolbar.

## Troubleshooting

{% content-ref url="troubleshooting/jetbrains-plugin-access-token-not-stored" %}
[jetbrains-plugin-access-token-not-stored](https://help.aikido.dev/ide-plugins/troubleshooting/jetbrains-plugin-access-token-not-stored)
{% endcontent-ref %}

{% content-ref url="troubleshooting/jetbrains-information-for-support" %}
[jetbrains-information-for-support](https://help.aikido.dev/ide-plugins/troubleshooting/jetbrains-information-for-support)
{% endcontent-ref %}
