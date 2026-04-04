# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/run-an-analysis-with-visual-studio-code-extension.md

# Run an analysis with Visual Studio Code extension

{% hint style="info" %}
Ensure the Snyk extension is [configured](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/visual-studio-code-extension-configuration-environment-variables-and-proxy), [authenticated](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/view-analysis-results-from-visual-studio-code-extension), and [trusted](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/visual-studio-code-workspace-trust) for your Project.
{% endhint %}

You can trigger `snyk test` by using one of these methods:

* automatic (default)
* manual

Snyk Code and IaC configuration scans are triggered automatically when you open your Project and when you save any supported files. This behavior can be turned off in [user experience configuration](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension-configuration-environment-variables-and-proxy#user-experience).

Snyk Open Source, by default, does not automatically run on save, but you can enable auto-scan in the configuration settings.

When the scan happens automatically, observe that the extension picks up the files and uploads them for analysis as soon as you open your Project or save any supported files.

Snyk Open Source requires the Snyk CLI, so it is downloaded in the background.

Snyk Code analysis runs quickly without the CLI, so results may be available quickly. If there is a delay, you see in-progress messages for each type of scan while Snyk scans your workspace for vulnerabilities and issues:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-942cbdb806d7a3e1b99d1c6802bb3825caf2c5ec%2FScreenshot%202025-06-04%20at%209.46.14%E2%80%AFAM.png?alt=media" alt=""><figcaption><p>Snyk scan in progress</p></figcaption></figure>

{% hint style="info" %}
Ensure your files are saved before manually running an analysis.
{% endhint %}

To trigger `snyk test` manually:

1. Click the **Snyk icon** in the sidebar to open the Snyk panel.
2. Click the **Rescan** (play) button at the top of the extension panel.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3704845199a9c17ec66405b31f8bf2b2c96f0e03%2FSCR-20241024-qqsi.png?alt=media" alt="" width="355"><figcaption><p>Manually trigger a Snyk analysis</p></figcaption></figure>
