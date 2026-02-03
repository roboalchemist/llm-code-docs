# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-extension/run-an-analysis-with-visual-studio-extension.md

# Run an analysis with Visual Studio extension

Open your solution and click **Run scan**. Depending on the size of your solution and the time needed to build a dependency graph, it takes less than one or two minutes to get the vulnerabilities.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-690fb5a33ffe527e2eaf0ce5434e94940855ee0b%2Frunscan.png?alt=media" alt=""><figcaption><p>Run a scan</p></figcaption></figure>

The extension provides two kinds of results:

* Open Source vulnerabilities
* Snyk Code issues

## Open Source vulnerabilities

Note that your solution must be built successfully in order to allow the CLI to pick up the dependencies and find the vulnerabilities.

If you see only npm vulnerabilities or vulnerabilities that are not related to your C#/.NET Projects, your Project may not have been built successfully and thus not detected by the CLI. If you have difficulty or questions, submit a request to [Snyk Support](https://support.snyk.io).

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b73878fa633ca9e23e4cd574d6a4a95ea68291eb%2Fossec.png?alt=media" alt=""><figcaption><p>Open Source vulnerabilities</p></figcaption></figure>

## Snyk Code issues

Snyk Code analysis shows a list of security vulnerabilities and code issues found in the application code. For more details and examples of how others fixed the issue, select a security vulnerability or a code security issue and examine the suggestions that Snyk provides.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3882115786a73181166c8292a04c24fceea4cd29%2Fcodesec.png?alt=media" alt=""><figcaption><p>Snyk suggestion panel</p></figcaption></figure>

The suggestions from Snyk include the recommendation of the Snyk engine using, for example, variable names in your code and the line numbers in red. You can also see:

* Links to external resources that explain the bug pattern in more detail.
* Tags that were assigned by Snyk, such as Security (the issue found is a security issue), Database (the issue is related to database interaction), or In Test (the issue is within the test code).
* Code from open-source repositories that can be of help to see how others have fixed the issue.
