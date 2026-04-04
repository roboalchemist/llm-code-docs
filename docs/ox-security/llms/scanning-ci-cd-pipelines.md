# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines.md

# Scanning Code and Artifacts in CI/CD Pipelines

OX Security integrates with CI/CD pipelines to scan code and artifacts changes as they are introduced. This enables early detection of vulnerabilities and misconfigurations during development, before code is merged or deployed.

Pipeline scanning is one of several targeted scanning methods supported by OX and is designed to complement the full scan.

While a full scan provides broad visibility across all repositories on a scheduled basis, pipeline scans focus on a single repository and analyze only the changes introduced in a specific push or pull request.

Benefits of pipeline scans:

* **Speed**: Pipeline scans are faster because they only analyze modified files.
* **Immediate feedback**: Scans run as soon as code is pushed or a pull request is opened.
* **Focused results**: Helps developers quickly identify and resolve newly introduced issues like secrets or vulnerabilities.

### How pipeline scanning works in OX

A pipeline scan runs automatically when triggered by version control events such as pushes or pull requests.

The scan analyzes the affected files or artifacts and reports any security findings. This allows teams to block risky builds and enforce secure coding practices early in the development lifecycle.

OX Security supports the following types of pipeline scans:

* **Pull request event scans:** Scans only the files that were modified in the source branch before it is merged into the target branch.
* **Push event scans:** Scans only the files that were modified in commits pushed to the source branch after the last successful pipeline scan on that branch.

## Setting up pipeline scans

1. Before setting up pipeline scans, make sure the repository went through a full scan.

> **Note:**\
> Pipeline scans can run even if a full scan has not been completed. However, running a full scan first is recommended for accurate and complete results, because pipeline scans rely on the application and repository data collected during the full scan.

1. Go to the **Applications** page.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-410be629da7301cfdd5b0bbd08e1c5d532ec5033%2FApp_page.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select a repository for which you want to configure pipeline scanning and click the **Pipeline Settings** icon at the top.
2. In the [Pipeline Settings page, review the settings that define how the scan behaves](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/pipeline-scan-settings).

> **Note:** OX Security recommends using the default settings.

1. Configure the [trigger mechanism in your source control platform](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms).
2. Go to the [**Pipeline Workflows** page to define how OX reacts to findings](https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows).
3. Validate the integration.\
   Push a code change or open a pull request to verify that the pipeline scan runs and reacts as expected.
4. [View and analyze scan results.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/understanding-pipeline-scan-results)
