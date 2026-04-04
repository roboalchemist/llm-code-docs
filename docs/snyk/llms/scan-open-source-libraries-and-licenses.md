# Source: https://docs.snyk.io/scan-with-snyk/snyk-open-source/scan-open-source-libraries-and-licenses.md

# Scan open-source libraries and licenses

You can scan your open-source libraries using Snyk Open Source:

* In the Snyk Web UI
* With your [IDE](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions)
* With a [CI/CD integration](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations)
* Through the [Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-open-source)
* Through the [Snyk API](https://docs.snyk.io/snyk-api/reference/test-v1)

## View vulnerabilities in your open-source libraries

You can view vulnerability results for imported Projects. The **Projects** page appears by default after import, showing vulnerability information for the Snyk Projects you have imported, grouped into **Targets**, that is, the repositories you have scanned.

You can expand a **Target** to see vulnerability information for Projects, including the number of issues found, grouped by severity level:

Click a Project to open the issues page for that Project, where, for supported environments, you can see the dependency cards, showing all of your dependencies, the versions where each associated issue was introduced, how to fix them, and more details about the individual vulnerabilities.

For unsupported environments, you can see a list of individual vulnerabilities. For more details, see [View Project information](https://docs.snyk.io/snyk-platform-administration/snyk-projects/project-information).

## Fix vulnerabilities in your open-source libraries

For some languages, Snyk can fix vulnerabilities using fix pull/merge requests. For more information, see [Automatic and manual PRs with Snyk Open Source](https://docs.snyk.io/scan-with-snyk/pull-requests/snyk-pull-or-merge-requests).

Navigate to the **Issues** card for a Project.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-85c4bd2101eacf582b333bbf10c5a62997c63173%2FOS-issues-tab-in-os-project.png?alt=media" alt=""><figcaption><p>Issues tab in an Open Source Project</p></figcaption></figure>

To fix vulnerabilities:

1. Click **Upgrade to X.X.X** to open a fix PR for this dependency. Click **Fix these vulnerabilities** at the top of the page to fix multiple issues.
2. The **Open a Fix PR** screen opens, displaying the selected vulnerabilities.
3. Check or uncheck the issues you want to fix or remove from this fix.
4. Scroll to the bottom of the screen and click **Open a Fix PR**.
5. Snyk acts on the PR and displays a results screen.
6. Optionally, select the **Files changed** tab to see details of the changes made.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ecf44f1f35b7ae1ec194b46453a6c8e0fe2a40b2%2Fscreenshot_2021-04-09_at_17.46.22.png?alt=media&#x26;token=faa76615-ba5a-4221-bc3e-6168597270b0" alt=".Files changed tab in GitHub after triggering Fix PR for an open source project"><figcaption><p>Files changed tab in GitHub after triggering Fix PR for an open source project</p></figcaption></figure>

For more details, see [Fix your vulnerabilities](https://docs.snyk.io/scan-with-snyk/snyk-open-source/manage-vulnerabilities/fix-your-vulnerabilities).
