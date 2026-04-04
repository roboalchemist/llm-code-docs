# Source: https://help.aikido.dev/ide-plugins/visual-studio-plugin.md

# Visual Studio IDE

Aikido automatically scans your projects for hardcoded secrets (API keys, tokens) and insecure code patterns (SQL injections, path traversal, ..) so you can catch issues early and keep your codebase safe.

Scans run automatically whenever you open a file or save changes, making it easy to catch issues early in development.

When security issues are found, they're highlighted directly in your code and listed in the Aikido window.

![C# code editor showing SQL query function, warnings, and security/code scan panels.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2152f3288de769bd80d8dd621b143e2c719adea5%2Fvisual-studio-plugin_336ff95d-dea0-4f72-bd63-520c4757d664.gif?alt=media)

## How to Install and Use <a href="#how-to-install-and-use" id="how-to-install-and-use"></a>

**Step 1.** Head over to the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=AikidoSecurity.aikido-visualstudio) and click **Install.** After installation, you will be asked to add your personal access token (step 2).

**Step 2.** In Aikido, go to the [Visual Studio Integration Screen](https://app.aikido.dev/settings/integrations/ide/visualstudio) and create your token.

![Visual Studio IDE Plugin page showing no registered tokens and option to generate a new PAT.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-11ad30448f5b71be41d1b0adfe861e0e346d8c19%2Fvisual-studio-plugin_a3d6e40c-39f7-44b5-bfea-94361c90384b.png?alt=media)

**Step 3.** Check out the examples in our docs on the [Visual Studio Marketplace to test](https://marketplace.visualstudio.com/items?itemName=AikidoSecurity.aikido-visualstudio)[](https://marketplace.visualstudio.com/items?itemName=AikidoSecurity.aikido)whether everything works well.

## Supported Visual Studio Versions <a href="#supported-visual-studio-versions" id="supported-visual-studio-versions"></a>

The Aikido Extension can be installed on Visual Studio Community Edition, Visual Studio Professional and Visual Studio Enterprise. It adheres to [Visual Studio’s support lifecycle](https://learn.microsoft.com/en-us/visualstudio/productinfo/vs-servicing), remaining compatible with officially supported versions.

## Troubleshooting

{% content-ref url="troubleshooting/visual-studio-information-for-support" %}
[visual-studio-information-for-support](https://help.aikido.dev/ide-plugins/troubleshooting/visual-studio-information-for-support)
{% endcontent-ref %}
