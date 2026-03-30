# Source: https://help.aikido.dev/ide-plugins/kiro-ide.md

# Kiro IDE

Aikido automatically scans your projects for hardcoded secrets (API keys, tokens) and insecure code patterns (SQL injections, path traversal, ..) so you can catch issues early and keep your codebase safe.

Scans run automatically whenever you open a file or save changes, making it easy to catch issues early in development.

When security issues are found, they're highlighted directly in your code and listed in the Aikido window.

## Installation and Authentication

{% stepper %}
{% step %}

### Open Extensions and Install "Aikido Security"

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FMiDuSkvKznSEUFHz6GdM%2FScreenshot%202025-11-25%20at%2014.33.47.png?alt=media&#x26;token=5e037693-8ebc-4998-9d16-f3dd94d77d80" alt=""><figcaption></figcaption></figure>

Alternatively use these links to go to the Marketplaces

* [VS Code](https://marketplace.visualstudio.com/items?itemName=AikidoSecurity.aikido)
* [Windsurf](https://open-vsx.org/extension/AikidoSecurity/aikido) / [Cursor](https://open-vsx.org/extension/AikidoSecurity/aikido) / [Kiro](https://open-vsx.org/extension/AikidoSecurity/aikido) / [Google Antigravity](https://open-vsx.org/extension/AikidoSecurity/aikido)
  {% endstep %}

{% step %}

### Authenticate with Aikido&#x20;

<img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FWvVCcNOzIF0MjVfKvOKd%2FScreenshot%202025-11-25%20at%2014.52.14.png?alt=media&#x26;token=a6832d73-7ce0-48a8-adc5-f3d7728ca338" alt="" data-size="line"> Open the Aikido plugin by clicking on the sidebar icon and click on "Connect to Aikido" to authenticate with Aikido platform.&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FnmwcXgOx2EuTzPv2xtO3%2FScreenshot%202026-01-07%20at%2013.50.27.png?alt=media&#x26;token=eff2f367-86ba-4ae4-8ad1-fd899150d374" alt=""><figcaption></figcaption></figure>

Alternatively you can open up the Command Palette and run `Aikido: Log In`&#x20;

If the automated authentication does not work you can manually create a personal access within Aikido by going to the [Integrations page and following the instructions](https://app.aikido.dev/settings/integrations?section=ide).
{% endstep %}

{% step %}

### Try out our examples

Below you can find an example `index.js` file that can be used to verify if the extension is working correctly, it should detect one SAST issue (SQL injection) and one exposed secret (SQL Server connection string).

```javascript
const app = {}

app.get("/user", (req, res) => {
    const connStr = "Server=tcp:myserver.database.windows.net,1433;Initial Catalog=mydb;Persist Security Info=False;User ID=myuser;Password=$uperSecret123!@#";
    const username = req.query.username
    const unsafeQuery = `SELECT * FROM users WHERE username = '${username}'`
    sql.connect(connStr).query(unsafeQuery, (err, result) => {
        res.status(200).send(result)
    })
})
```

{% endstep %}

{% step %}

### Turn on Additional Security Tooling

Extend Aikido in your IDE with Expansion Packs like [MCP for AI agents](https://help.aikido.dev/mcp/aikido-mcp), [pre-commit hooks](https://help.aikido.dev/code-scanning/local-code-scanning/aikido-secrets-pre-commit-hook), and [Safe Chain](https://help.aikido.dev/code-scanning/aikido-malware-scanning). For more details, see the documentation below.

{% content-ref url="features/aikido-expansion-packs" %}
[aikido-expansion-packs](https://help.aikido.dev/ide-plugins/features/aikido-expansion-packs)
{% endcontent-ref %}
{% endstep %}
{% endstepper %}

## What to explore next

Now that the plugin is installed, you can dive into the features that help you spot security issues while you work:

{% content-ref url="features/real-time-code-scanning-in-ide" %}
[real-time-code-scanning-in-ide](https://help.aikido.dev/ide-plugins/features/real-time-code-scanning-in-ide)
{% endcontent-ref %}

{% content-ref url="broken-reference" %}
[Broken link](https://help.aikido.dev/ide-plugins/broken-reference)
{% endcontent-ref %}

{% content-ref url="features/open-source-dependency-scanning-sca-in-ide" %}
[open-source-dependency-scanning-sca-in-ide](https://help.aikido.dev/ide-plugins/features/open-source-dependency-scanning-sca-in-ide)
{% endcontent-ref %}

{% content-ref url="features/full-workspace-scan-in-ide" %}
[full-workspace-scan-in-ide](https://help.aikido.dev/ide-plugins/features/full-workspace-scan-in-ide)
{% endcontent-ref %}

{% content-ref url="features/aikido-ai-in-ide" %}
[aikido-ai-in-ide](https://help.aikido.dev/ide-plugins/features/aikido-ai-in-ide)
{% endcontent-ref %}

## Troubleshooting

{% content-ref url="troubleshooting/vs-code-extension-keeps-disconnecting" %}
[vs-code-extension-keeps-disconnecting](https://help.aikido.dev/ide-plugins/troubleshooting/vs-code-extension-keeps-disconnecting)
{% endcontent-ref %}
