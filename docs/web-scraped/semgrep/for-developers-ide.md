# Run IDE scans

Source: https://semgrep.dev/docs/for-developers/ide

- [](/docs/)- [For developers](/docs/for-developers/overview)- Run scans- Run IDE scans**On this page- [Developer education](/docs/tags/developer-education)- [Extensions](/docs/tags/extensions)Run IDE scans
Semgrep supports the following IDE extensions:

NameMarketplace linkDocumentationMicrosoft Visual Studio Code[** `semgrep-vscode`](https://marketplace.visualstudio.com/items?itemName=semgrep.semgrep)[Semgrep VS Code extension](/docs/extensions/semgrep-vs-code)IntelliJ Ultimate Ideaand many other IntelliJ products[** `semgrep-intellij`](https://plugins.jetbrains.com/plugin/22622-semgrep)[Semgrep IntelliJ extension](/docs/extensions/semgrep-intellij)Emacs[** `lsp-mode`](https://github.com/emacs-lsp/lsp-mode)See repository README
## Quickstart[​](#quickstart)
Select your IDE in the following tabs and follow the instructions to set up your first Semgrep IDE scan.

- Visual Studio Code (VS Code)- IntelliJFor Microsoft VS Code users:

- [Install the Semgrep extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-an-extension). If you&#x27;re unfamiliar with installing VS Code extensions, see the Extension Marketplace&#x27;s article [Install an Extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-an-extension).
- Use Ctrl+⇧Shift+P or ⌘Command+⇧Shift+P (macOS) to launch the Command Palette, and run the following to sign in to Semgrep AppSec Platform:
`Semgrep: Sign in`
You can use the extension without signing in, but doing so enables better results since you benefit from [Semgrep Code](/docs/semgrep-code/overview) and its [Pro rules](/docs/semgrep-code/pro-rules).
- Launch the Command Palette using Ctrl+⇧Shift+P or ⌘Command+⇧Shift+P (macOS), and scan your files by running:
```
Semgrep: Scan all files in workspace
```

- To see detailed vulnerability information, hover over the code underlined in yellow. You can also see the findings identified by Semgrep using ⇧Shift+Ctrl+M or ⌘Command+⇧Shift+M (macOS) and opening the **Problems** tab.
For JetBrains IntelliJ users:

- 
Install the Semgrep extension:

Visit [** Semgrep&#x27;s page on the JetBrains Marketplace](https://plugins.jetbrains.com/plugin/22622-semgrep).
- In IntelliJ: **Settings/Preferences &gt; Plugins &gt; Marketplace &gt; Search for `semgrep-intellij` &gt; Install**. You may need to restart IntelliJ for the Semgrep extension to be installed.

- 
Sign in: Press Ctrl+⇧Shift+A (Windows) or ⌘Command+⇧Shift+A (macOS) and sign in to Semgrep AppSec Platform by selecting the following command:

`Sign in with Semgrep`

- 
Test the extension by pressing Ctrl+⇧Shift+A (Windows) or ⌘Command+⇧Shift+A (macOS) and run the following command:

`Scan workspace with Semgrep`

- 
See Semgrep findings: Hold the pointer over the code that has the red underline.

Feature maturitySemgrep&#x27;s IntelliJ extensions are currently in beta. Currently, the IntelliJ extension only supports Semgrep Community Edition (CE) - it doesn&#x27;t support Semgrep Supply Chain, Secrets, Pro rules, or Pro Engine. Please join the [Semgrep community Slack workspace](https://go.semgrep.dev/slack) and let the Semgrep team know if you encounter any issues.

## Scan scope and limitations[​](#scan-scope-and-limitations)
Semgrep&#x27;s VS Code extension supports the use of Pro rules and cross-file analysis. Other IDE scans use Semgrep Community Edition (CE) for its speed, and these scans are limited to single-file analysis. As a result, you may encounter a higher rate of false positives.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Developer education](/docs/tags/developer-education)- [Extensions](/docs/tags/extensions)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/for-developers/ide.md)Last updated on **Jan 16, 2025**