# Source: https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac.md

# Snyk CLI for IaC

## Overview

To use the CLI, you must first [install](https://docs.snyk.io/developer-tools/snyk-cli/install-or-update-the-snyk-cli) it and then [authenticate](https://docs.snyk.io/developer-tools/snyk-cli/commands/auth).

With Snyk Infrastructure as Code, you can test your configuration files directly from the CLI. See the following pages for details:

* [Test your IaC files](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac/test-your-iac-files)
* [Share CLI results with the Snyk Web UI](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac/share-cli-results-with-the-snyk-web-ui)
* [IaC ignores using the `.snyk` policy file](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac/iac-ignores-using-the-.snyk-policy-file)
* [IaC exclusions using the command line](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac/iac-exclusions-using-the-command-line)
* [Understanding the IaC CLI test results](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac/understand-the-iac-cli-test-results) (has information about reports)

## Regularly testing IaC files

Snyk Infrastructure as Code has no equivalent command to `snyk monitor` because the CLI does not send IaC source files back to the platform for periodic testing.

For IaC CLI results to appear in the Snyk Web UI, use [`snyk iac test --report`](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac/share-cli-results-with-the-snyk-web-ui) to capture a one-time snapshot. Optionally, run the command on a recurring schedule to regularly test your IaC files.

Alternatively, you can add an [SCM integration](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations), and Snyk will monitor and test a given Git repository on a recurring basis.

## Using Snyk behind a proxy

If you are using a proxy, see [Proxy configuration for Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli/configure-the-snyk-cli/proxy-configuration-for-snyk-cli).

For IaC scans specifically, you must also whitelist the \*.snyk.io address, as explained on the page [How can we allowlist Snyk IP addresses](https://support.snyk.io/s/article/How-can-we-allowlist-Snyk-IP-addresses)?
