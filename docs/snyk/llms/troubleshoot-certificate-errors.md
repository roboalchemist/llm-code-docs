# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/troubleshooting-ides/troubleshoot-certificate-errors.md

# Troubleshoot certificate errors

## Problem <a href="#problem" id="problem"></a>

Error message **Unable to get local issuer certificate** or something with certificate path.

## Solution <a href="#solution" id="solution"></a>

* Add all certificates in the correct chain to the operating system, the environment (JDK), or both that the certificate is running on.
* Set **Allow unknown certificate authority** in the IDE or
* Pass the `--insecure` argument to the Snyk CLI executable using settings, **This does not solve Download, API access, and Snyk Code communication.**

## Custom Certificate Authorities <a href="#custom-certificate-authorities" id="custom-certificate-authorities"></a>

### Java <a href="#java.1" id="java.1"></a>

The CA and intermediate certificates must be added to the certificate store of each JDK used.

See [Import the Certificate as a Trusted Certificate (The Java™ Tutorials > Security Features in Java SE > Signing Code and Granting It Permissions)](https://docs.oracle.com/javase/tutorial/security/toolsign/rstep2.html).

### Eclipse <a href="#eclipse" id="eclipse"></a>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a09d60def41e4676fab7883d7c8f3b9df6b6ee1d%2Fimage.png?alt=media" alt="Allow unknown certificate authorities"><figcaption><p>Allow unknown certificate authorities</p></figcaption></figure>

* Update the JDK used by Snyk scans to add unknown certificates.
* Update to the latest CLI and pugin version.
* CLI download can be re-triggered by deleting the CLI. The path is shown in the Snyk Preferences.

### IntelliJ <a href="#intellij" id="intellij"></a>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ecb106727816a2d9af4c91d5a575d7db1441a29b%2Fimage%20(174).png?alt=media" alt="IntelliJ setting"><figcaption><p>IntelliJ setting</p></figcaption></figure>

* See [Trusted root certificates | IntelliJ IDEA](https://www.jetbrains.com/help/idea/ssl-certificates.html).
* Updating the Jetbrains certificate handling only will most likely not be sufficient, as the CLI does not use Jetbrains settings, but JAVA\_HOME and PATH to determine a JDK. This JDKs certificate store must be updated.

### VSCode <a href="#vscode" id="vscode"></a>

Try using the`win-ca` extension to make Trusted Root Certificates available to the extension.

See [win-c](https://marketplace.visualstudio.com/items?itemName=ukoloff.win-ca)a.

Another option is using environment variables; see [How to add custom certificate authority (CA) to nodejs](https://stackoverflow.com/questions/29283040/how-to-add-custom-certificate-authority-ca-to-nodejs) .

The last resort is to disable Certificate checks. Add `--insecure` to additional arguments to disable checks in the CLI, and **uncheck** the setting to use a strict proxy (`http.proxyStrictSSL`) in VSCode to disable certificate checks in `https` calls.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-66d21a663b178ffdc91c3e4502285382641c87e2%2Fimage.png?alt=media" alt="--inseucure argument"><figcaption><p>--inseucure argument</p></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c83a7109d82dd32d63ea859b1d6e9fdffbc55f9d%2Fimage.png?alt=media" alt="Proxy settings"><figcaption><p>Proxy settings</p></figcaption></figure>
