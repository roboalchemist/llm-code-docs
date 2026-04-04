# Source: https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/fix-vulnerabilities-using-the-snyk-cli.md

# Fix vulnerabilities using the Snyk CLI

The Snyk CLI provides support for fixing vulnerabilities found by using the `snyk test` command. For information about fixes in the Web UI, see [Fix your vulnerabilities](https://docs.snyk.io/scan-with-snyk/snyk-open-source/manage-vulnerabilities/fix-your-vulnerabilities). For general information about patches, see [Snyk patches to fix vulnerabilities](https://docs.snyk.io/scan-with-snyk/snyk-open-source/manage-vulnerabilities/snyk-patches-to-fix-vulnerabilities).

If you are using `snyk container test`, see [Understanding Snyk Container CLI results](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-container/understand-snyk-container-cli-results) for information about resolving vulnerabilities found in a scan. If you are using `snyk code test`, see [View Snyk Code CLI results](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code/view-snyk-code-cli-results). If you are using `snyk iac test`, see [Understanding the IaC CLI test results](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac/understand-the-iac-cli-test-results).

## Upgrade and patch results from the CLI

From the CLI, for each list (upgrade and patch), results are displayed in groups based on the packages Snyk recommends that you fix. The results include the following:

* details for all vulnerabilities introduced per package; to view all dependency paths affected, use `--show-vulnerable-paths=all` when running `snyk test` or `snyk monitor`
* links to full descriptions of each vulnerability

Upgrade and patch results appear similar to the following:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b6747c94f599365ca4d3eeff91dfe9e61bb49bea%2Fimage%20(17).png?alt=media&#x26;token=b75fd8b7-5fee-4bf3-9c2d-5e0d93f6d387" alt="Upgrade results in the CLI"><figcaption><p>Upgrade results in the CLI</p></figcaption></figure>

Patch recommendations appear similar to the following:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-da5d4849da199ee58ef0274397cf9211c73aa81c%2Fuuid-1afca091-a9a5-d42c-40b6-f48aa0e72584-en.png?alt=media&#x26;token=ed3e4598-93cd-45e4-b49f-8e7f55113943" alt="Patch results in the CLI"><figcaption><p>Patch results in the CLI</p></figcaption></figure>

## Snyk patches to fix vulnerabilities using the CLI

The `protect` command was replaced by `@snyk/protect`: <https://github.com/snyk/snyk/tree/master/packages/snyk-protect>; [npm package for `snyk-protect` command](https://www.npmjs.com/package/@snyk/protect). These pages have instructions for using the package and migrating from `snyk protect`.
