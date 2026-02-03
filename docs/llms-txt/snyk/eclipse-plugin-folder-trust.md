# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/eclipse-plugin/eclipse-plugin-folder-trust.md

# Eclipse plugin folder trust

The Snyk plugin asks for folder trust before allowing scans to be run against new folders.

When scanning for vulnerabilities, Snyk may automatically execute code such as invoking the package manager to get dependency information. You should only scan folders you trust.

Note that invoking a package manager (pip, Gradle, Maven, Yarn, npm, and so on) on untrusted code that has malicious configurations may expose your system to malicious code execution and exploits.

If in doubt, select **Don't trust folders**.

After a trust is granted, Snyk will not ask for trust on the opened Project folder and its subfolders again. If you did not grant trust the first time, the plugin asks again the next time you restart your Eclipse instance.

To revoke an existing folder trust, you can navigate to the Snyk plugin preferences in Eclipse and edit the **Trusted Folders** setting to specify which paths are safe to scan.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0a6ffd95d5d82e31814398f6ac011540a92770a7%2FScreenshot%202025-01-09%20at%208.33.24%E2%80%AFAM.png?alt=media" alt="Snyk Eclipse plugin preferences Trusted Folders setting"><figcaption><p>Snyk Eclipse plugin preferences Trusted Folders setting</p></figcaption></figure>
