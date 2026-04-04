# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/view-analysis-results-from-visual-studio-code-extension/analysis-results-snyk-code.md

# Analysis results: Snyk Code

Snyk Code analysis shows security vulnerabilities and quality issues in your code with every scan.

{% hint style="info" %}
Effective beginning on June 24, 2025, Snyk Code Quality issues will no longer be provided.
{% endhint %}

## Snyk Code vulnerability window

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-683f536680ec9cce60b4102e71889a11c3f0d02f%2FScreenshot%202023-03-17%20at%2012.25.28.png?alt=media&#x26;token=4b3c0d16-be7d-44df-9b5f-1cd642a88c81" alt="Snuk Code vulnerability window"><figcaption><p>Snyk Code vulnerability window</p></figcaption></figure>

The Snyk suggestion panel on the right of the results screen shows the Snyk Code Vulnerability name, the line it was found in, a suggestion for a fix, and an option to ignore, either in the entire file or a specific line.

On the **Problems** tab of the Visual Studio Code results screen, you can see all Code issues found in your Project.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-77b42fcdda4e48345064e03dff6370bbd633d0a7%2FScreenshot%202023-03-17%20at%2013.41.55.png?alt=media&#x26;token=6a16c3ed-2028-42b3-8077-6a82360e7bd4" alt="Visual Studio Code Problems tab"><figcaption><p>Visual Studio Code Problems tab</p></figcaption></figure>

Snyk also includes a feedback mechanism to report false positives so others do not see the same issue (bottom left).

## Snyk Code editor window

The vulnerabilities are visible within the editor, with the detailed information available on hover.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-788c25296dc9a128d61e440e89ef8ec1a6bb3910%2FScreenshot%202023-03-17%20at%2012.31.45.png?alt=media&#x26;token=9a3ff442-3691-41b9-8c08-fde618d7211c" alt="Snyk Code editor window"><figcaption><p>Snyk Code editor window</p></figcaption></figure>

Choose **Quick Fix** to open the details panel for an issue using Code Action.

You can also choose to ignore a suggestion, either a particular one or a recurring one in the current file, using **Quick Fix**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6061fbe4f0596357c96c2a56b33e73b76501f5fc%2FScreenshot%202023-03-17%20at%2016.34.21.png?alt=media&#x26;token=1880d79c-d88e-4fe5-b7c3-5103dee5cd90" alt="Quick Fix menu"><figcaption><p>Quick Fix menu</p></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-44a5c909570e6d4b5aee2d3f6421c6946d66a3e7%2FScreenshot%202023-03-17%20at%2012.32.22.png?alt=media&#x26;token=e2f7b6df-c81d-4b4c-9170-cbec85e87a70" alt="Ignore options with issue detail"><figcaption><p>Ignore options with issue detail</p></figcaption></figure>
