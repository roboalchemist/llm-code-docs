# Source: https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code.md

# Snyk CLI for Snyk Code

The [Snyk Command Line Interface](https://docs.snyk.io/developer-tools/snyk-cli) (CLI) enables you to bring the functionality of Snyk Code into your development workflow. Using the Snyk CLI, you can run Snyk Code tests locally or incorporate them into your CI/CD pipeline to scan your source code for security vulnerabilities.

## Prerequisites for using the Snyk CLI with Snyk Code

Before using the Snyk CLI for testing your source code with Snyk Code, verify you have the following prerequisites:

* A Snyk account.
* Repositories with code in [supported languages and frameworks](https://docs.snyk.io/supported-languages/supported-languages-package-managers-and-frameworks).
* The **Snyk Code** option [enabled in your Snyk Org settings](https://docs.snyk.io/scan-with-snyk/snyk-code/configure-snyk-code).
* The Snyk CLI installed and authenticated.
  * For instructions, see [Install or update the Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli/install-or-update-the-snyk-cli) and [Authenticate the Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli/authenticate-to-use-the-cli).
  * The minimum Snyk CLI version for Snyk Code, version 1.716.0. Snyk recommends using the latest version of the CLI.

## Using the Snyk CLI for Snyk Code tests

To test your repository code using the Snyk CLI, use the [`snyk code test`](https://docs.snyk.io/developer-tools/snyk-cli/commands/code-test) command.\
For more information, see [Scan source code with Snyk Code using the CLI](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code/scan-source-code-with-snyk-code-using-the-cli).

Before running Snyk Code tests with the CLI, you may want to do the following:

* [Update your Snyk CLI version](https://docs.snyk.io/developer-tools/snyk-cli/install-or-update-the-snyk-cli).
* [Set the Organization for the CLI tests](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code/set-the-snyk-organization-for-the-cli-tests).
* [Exclude directories and files from the Snyk Code test](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code/exclude-directories-and-files-from-snyk-code-cli-tests).

For information about using the snyk code test command and the results, see the pages in this section of the documentation and [snyk-to-html](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/cli-tools/snyk-to-html).
