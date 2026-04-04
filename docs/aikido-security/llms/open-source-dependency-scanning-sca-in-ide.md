# Source: https://help.aikido.dev/ide-plugins/features/open-source-dependency-scanning-sca-in-ide.md

# Open-Source Dependency Scanning (SCA) in IDE

Aikido’s IDE extension helps you find and fix vulnerabilities in your open-source dependencies without leaving your editor. It scans your project’s manifests and lockfiles to detect outdated or insecure packages, highlight affected versions, and suggest safe upgrades.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FrRt7WwaKJSP0Qkzw1ORj%2Fsca_autofix.gif?alt=media&#x26;token=09f50dcc-94c8-4f7f-873e-54e98e153945" alt=""><figcaption></figcaption></figure>

### How it works

* Aikido reads your dependency manifests and lockfiles to build an accurate list of packages and versions.
* Results include known CVEs, severity, affected versions, and safe upgrade ranges.
* After you run a manual SCA scan once, the extension watches your workspace for lockfile changes and refreshes results automatically.

### Run a manual SCA scan

1. Open the Aikido sidebar in VS Code.
2. Go to Open-source dependencies.
3. Click Start scanning.
4. When results appear, select a package to view details, advisories, and fix guidance.
5. Each finding shows the minimum safe version or version ranges that resolve the issue.
6. For supported ecosystems, [AI AutoFix](https://help.aikido.dev/ide-plugins/features/aikido-ai-in-ide) can update the manifest or suggest a safe version bump that you can apply from the IDE.
