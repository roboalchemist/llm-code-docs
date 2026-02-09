# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/use-snyk-code-in-the-ci-cd-pipeline.md

# Snyk Code in the CI/CD pipeline

You can use CI/CD integration to test your code for vulnerabilities and ensure your changes do not introduce new vulnerabilities, keeping your applications secure.

* Snyk Code may not be supported by a Snyk CI/CD plugin, such as the Snyk Jenkins plugin. If this is the case, you can integrate [Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code) with your CI server.
* You can filter the results by severity, for example, fail jobs only when high-severity vulnerabilities are introduced. See [Filter results by Severity](https://docs.snyk.io/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code/view-snyk-code-cli-results#filter-results-by-severity-level).
* You can export the CLI output to JSON or SARIF standard formats. See [Output test results](https://docs.snyk.io/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code/view-snyk-code-cli-results#export-test-results).
* You can generate more visual results using the Snyk-to-HTML tool. See [`snyk-to-html`](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/cli-tools/snyk-to-html).
