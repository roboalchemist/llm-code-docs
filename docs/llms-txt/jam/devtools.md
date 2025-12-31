# Source: https://jam.dev/docs/debug-a-jam/devtools.md

# DevTools

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FoOIz3cIMwGy61fgsrpaN%2Fnetwork.gif?alt=media&#x26;token=b5350984-eade-439d-8577-de5cb9053523" alt=""><figcaption></figcaption></figure>

### Overview

Every Jam capture automatically includes comprehensive developer information to help engineers debug faster. Get instant access to console logs, network data, and environment details without switching between tools or losing context.<br>

### Core Features

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Visual Context</strong></td><td>Screenshots and screen recordings with annotation tools</td><td><a href="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F2C8XJjmnhphIRSuLo104%2FVisual%20Context.png?alt=media&#x26;token=4d565926-49c1-4d51-b56a-2fe756a4ab12">Visual Context.png</a></td><td></td></tr><tr><td><strong>Metadata</strong> <code>Customizable</code></td><td>URL, timestamp, device info, browser version, OS, and more</td><td><a href="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FW0QFlGjEJjFqF7AwmrV0%2FDevice%20Info.png?alt=media&#x26;token=d5842034-5dbf-4204-8c12-888eabf5beba">Device Info.png</a></td><td><a href="devtools/jam.metadata">jam.metadata</a></td></tr><tr><td><strong>Developer Logs</strong></td><td>Console logs and complete network request details and more</td><td><a href="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FjSSvP2nbPkxa8KeEu2Rh%2FDev%20Logs.png?alt=media&#x26;token=87e2d9c9-b8c1-4956-a60a-865903bd52a4">Dev Logs.png</a></td><td><a href="devtools">devtools</a></td></tr><tr><td><strong>User Events</strong></td><td>User clicks, navigation events and more</td><td><a href="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FlNN7M1tQm5XPUeZUfyUo%2FUser%20Events.png?alt=media&#x26;token=31e6ffa4-c7f0-4d4d-8654-4ba3e6605873">User Events.png</a></td><td></td></tr></tbody></table>

#### Customization

#### **Layouts**

Switch between side and bottom layout to fit your workflow. The DevTools panel adapts to your preferred layout.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FoOIz3cIMwGy61fgsrpaN%2Fnetwork.gif?alt=media&#x26;token=b5350984-eade-439d-8577-de5cb9053523" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Side Dock" %}
DevTools appear on the right side in the properties panel for wide-screen debugging. Ideal when you need to see both the captured page and technical details simultaneously.
{% endtab %}

{% tab title="Bottom Dock" %}
DevTools expand across the bottom for detailed network analysis. Perfect for inspecting multiple requests or long console outputs.
{% endtab %}
{% endtabs %}

#### Keyboard Shortcuts

Use familiar Chrome DevTools shortcuts for faster navigation:

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F2bHsEGGVfdDLWiodMfST%2FJam%20Shortcuts.gif?alt=media&#x26;token=0bf034b2-2a08-4443-ab3f-a1fc8133c010" alt=""><figcaption></figcaption></figure>

| Action                            | Shortcut                                       |
| --------------------------------- | ---------------------------------------------- |
| Change layout                     | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>D</kbd> |
| Navigate through network requests | <kbd>↑↓</kbd>                                  |
| Open network request details      | <kbd>⏎</kbd> Return                            |
| Close network request details     | <kbd>Esc</kbd>                                 |

<br>

### FAQs

<details>

<summary>Do I need to enable DevTools manually?</summary>

No. DevTools data is automatically captured with every Jam. No setup or configuration required. You can capture additional meta data with [jam.metadata](https://jam.dev/docs/debug-a-jam/devtools/jam.metadata "mention").

</details>

<details>

<summary>Can I filter console logs by severity?</summary>

Yes. Use the severity filter to show only errors, warnings, or specific log levels that matter for debugging.

</details>

<details>

<summary>How detailed is the network timing data?</summary>

You get complete timing breakdowns including DNS lookup, connection time, and response duration – just like Chrome DevTools.

</details>
