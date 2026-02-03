# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/view-analysis-results-from-visual-studio-code-extension/analysis-results-snyk-iac-configuration.md

# Analysis results: Snyk IaC configuration

Snyk IaC configuration analysis shows issues in your Terraform, Kubernetes, AWS CloudFormation, and Azure Resource Manager (ARM) code with every scan. Based on the Snyk CLI, the scan is fast and friendly for local development. The scan runs in the background and is enabled by default.

## Snyk IaC configuration issues window

The configuration issues window shows information about issues. By clicking on an issue, you can learn more about it:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1efd72ae2468d5b8520096dfc984699e41f37f29%2FScreenshot%202023-03-16%20at%2015.14.16.png?alt=media&#x26;token=f00fc467-68cf-4f75-8d22-79c932285560" alt="Snyk IaC configuration issues window"><figcaption><p>Snyk IaC configuration issues window</p></figcaption></figure>

The following information is shown:

* Issue description
* Issue impact
* Issue path
* Remediation details
* Links to references

In the **Problems** tab of the Visual Studio Code configuration issues screen, you can see all configuration issues found in your Project.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e07749f16e1ec38cc68936387ec52d8a70602bcc%2FScreenshot%202023-03-16%20at%2014.32.48.png?alt=media&#x26;token=baa36856-9f74-45f6-9ce6-02a668b720e2" alt="Problems tab" width="563"><figcaption><p>Problems tab</p></figcaption></figure>

## Snyk IaC configuration editor window

The issues are visible within the editor, with the detailed information available on hover.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5882bd1c2ef785497a5e3454ef26f9bf646000f9%2FScreenshot%202023-03-16%20at%2015.21.10.png?alt=media&#x26;token=78a45583-af84-4d50-96eb-24717849851f" alt="Snyk IaC configuration issue" width="563"><figcaption><p>Snyk IaC configuration issue</p></figcaption></figure>

Choose **Quick Fix** to open the details panel for an issue using Code Action.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-645a82c8371dd7c83d8509a2250f61533e25173f%2FScreenshot%202023-03-16%20at%2015.17.50.png?alt=media&#x26;token=e36cfdfc-7d11-4d96-af74-04f42af481e6" alt="Quick Fix" width="563"><figcaption><p>Quick Fix</p></figcaption></figure>

The details panel shows the issue name with the **Description**, **Impact** statement, **Path** by which the issue was introduced, and suggested **Remediation**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-2cb1a6272bf6cd75aac42670e20579fe47e9d1a2%2FScreenshot%202023-03-16%20at%2014.32.23.png?alt=media&#x26;token=3c8651e0-1ed5-4714-81fd-aa6128042970" alt="Details panel for a Snyk IaC configuration issue" width="375"><figcaption><p>Details panel for a Snyk IaC configuration issue</p></figcaption></figure>
