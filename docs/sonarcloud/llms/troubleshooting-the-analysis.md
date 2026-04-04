# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/troubleshooting-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/troubleshooting-the-analysis.md

# Troubleshooting the analysis

See also the Troubleshooting section on the corresponding Scanner and CI tool page.

To find the scanner logs, see this [Community guide](https://community.sonarsource.com/t/how-to-find-logs-about-importing-code-coverage/73317).

### Viewing the analysis progress status <a href="#viewing-progress" id="viewing-progress"></a>

During analysis, data is requested from the server, the files provided to the analysis are processed, and the resulting data is sent back to the server in the form of a report, which is then analyzed asynchronously on the server side.

Analysis reports are queued and processed sequentially, so it is quite possible that for a brief period after your analysis log shows completion, the updated values are not visible in your SonarQube Server project. However, you will be able to tell what’s going on because an icon will be added on the project overview page, to the right of the project name. Mouse over it for more information. The icon goes away once the analysis processing is complete. However, if there are issues with the analysis, a warning message appears. Click on the **see details** link to reveal a list of analysis issues.

<figure><img src="https://583449977-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLWhbesChsC4Yd1BbhHhS%2Fuploads%2FIl56NTypV0r5x86npI3m%2Fanalysis-warnings.png?alt=media&#x26;token=23750110-2050-4839-88bd-8c8e32276c21" alt="Analysis warnings on the project overview page"><figcaption></figcaption></figure>

### Out of memory error <a href="#out-of-memory" id="out-of-memory"></a>

If your analysis errors out with `java.lang.OutOfMemoryError: GC overhead limit exceeded` then it means that your project is too large or too intricate for the scanner to analyze with the default memory allocation. To fix this you’ll want to allocate a larger heap (using `-Xmx[numeric value here]`) to the process running the analysis. Some CI engines may give you an input to specify the necessary values, for instance if you’re using a Maven Build Step in a Jenkins job to run analysis. Otherwise, use Java Options to set a higher value. Note that details of setting Java Options are omitted here because they vary depending on the environment.

You can also add an exclusion to manage the files and folders you don’t need to analyze by limiting your [analysis scope](https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope). Additionally, using a Solid-state drive or something similar will help speed up the analysis process and thus use less memory, especially for small file access.

### PKIX path building failed <a href="#pkix-path-building-failed" id="pkix-path-building-failed"></a>

If your analysis errors out with `PKIX path building failed` then it means that your SonarQube Server is configured with HTTPS and a self-signed SSL certificate (see [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy "mention")). However, the certificate is not correctly configured in the scanner machine’s JVM. This configuration is outside of SonarQube Server scope. The server certificate is unknown and could not be validated with the provided truststore. To solve the issue, you need to import the SonarQube Server certificate to the Java truststore (see [manage-tls-certificates](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/manage-tls-certificates "mention")). See also [Oracle’s documentation](https://docs.oracle.com/cd/E19830-01/819-4712/ablqw/index.html) for more information.

### No response from server <a href="#analysis-not-running" id="analysis-not-running"></a>

If, for example, after a PostgreSQL database upgrade, the CPU usage has increased drastically in SonarQube Server and your build process is blocked at the code scanning step (no response from SonarQube Server), try reindexing the following database tables: issues, rules, and components.

### Various error messages <a href="#various" id="various"></a>

#### The format of the analysis property sonar.token= is invalid <a href="#the-format-of-the-analysis-property-sonartoken-is-invalid" id="the-format-of-the-analysis-property-sonartoken-is-invalid"></a>

You may encounter this issue when using SONAR\_TOKEN as a secret in a calling workflow in GitHub Actions in case the called workflow doesn’t manage to read it as a secret. In that case, make sure that the secret is inherited from the calling workflow (you may use the `secrets: inherit` keyword). See [GitHub documentation](https://docs.github.com/en/actions/sharing-automations/reusing-workflows#using-inputs-and-secrets-in-a-reusable-workflow) for more information.

#### The maximum number of open files was reached <a href="#the-maximum-number-of-open-files-was-reached" id="the-maximum-number-of-open-files-was-reached"></a>

On a Linux system, see **Configuring the maximum number of open files and other limits** in [linux](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/linux "mention").

On a MacOS system, see **Configuring the maximum number of open files** in [macos](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/macos "mention").

#### Error when analyzing files with non-ASCII characters in the name <a href="#error-when-analyzing-files-with-nonascii-characters-in-the-name" id="error-when-analyzing-files-with-nonascii-characters-in-the-name"></a>

When analyzing files with non-ASCII characters in the name, if the `Malformed input or input contains unmappable characters` error is raised then you should make sure that the environment variables `LC_ALL` and `LANG` are properly set before running the analysis as shown below.

```css-79elbk
export LC_ALL="en_US.UTF-8"
export LANG="en_US.UTF-8"
```

#### No coverage data in pull request analysis report with AWS CodeBuild <a href="#no-coverage-data-in-pull-request-analysis-report-with-aws-codebuild" id="no-coverage-data-in-pull-request-analysis-report-with-aws-codebuild"></a>

Verify that AWS CodeBuild `LOCAL_SOURCE_CACHE` feature is disabled.

#### Failed to upload analysis report on cloud platform <a href="#failed-to-upload-analysis-report-on-cloud-platform" id="failed-to-upload-analysis-report-on-cloud-platform"></a>

If you encounter the "SonarQubeAnalyze fails at upload report - error POST 403 - Failed to upload: You’re not authorized" error and you’re running SonarQube Server on a cloud platform, check that the cloud environment’s firewall (WAF) configuration allows the upload. WAF rules can potentially block SonarQube Server APIs, including the report submission.

#### Self-signed certificate error <a href="#selfsigned-certificate-error" id="selfsigned-certificate-error"></a>

See [manage-tls-certificates](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/manage-tls-certificates "mention").

#### Analysis stops with an error on Windows <a href="#analysis-stops-with-an-error-on-windows" id="analysis-stops-with-an-error-on-windows"></a>

If your username on Windows ends with a special character, for example `C:\Users\myUser!\`, the analysis will fail. Either change the username or, if that’s not possible, use the `sonar.userHome` parameter and set a path that doesn’t include any special characters. See [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention") for more information about `sonar.userHome.`

#### Missing blame information or Could not find ref error <a href="#missing-blame-info-error" id="missing-blame-info-error"></a>

The errors "*Missing blame information…*" and "*Could not find ref…*" can be caused by checking out with a partial or shallow clone, or when using Git submodules. You should disable git shallow clone to make sure the scanner has access to all of your history when running analysis. See [verifying-code-checkout-step](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step "mention").

### Debugging the analysis <a href="#debugging-analysis" id="debugging-analysis"></a>

For debugging purposes, you can use the `sonar.scanner.internal.dumpToFile` parameter to output to a specific file a full list of properties retrieved by the scanners (CLI, Gradle, Maven, and NPM). The properties include user properties passed through command line arguments, configuration files, environmental variables, and other properties relevant to the specific scanners.

**Possible value**: path to the output file name.

Deprecated: `sonar.scanner.dumpToFile`

**Note**: The equivalent output is available in ***Your Project*** > **Project Settings** > **Background Tasks** > **3-dots menu** > **Show SonarScanner Context**. If the analysis report fails, the list is not generated in Show SonarScanner Context.
