# Source: https://docs.sonarsource.com/sonarqube-cloud/appendices/frequently-asked-questions.md

# Frequently asked questions

### Does SonarQube Cloud require single sign on - SSO? <a href="#does-sonarcloud-require-single-sign-on-sso" id="does-sonarcloud-require-single-sign-on-sso"></a>

SonarQube Cloud does not require single sign-on (SSO), as authentication is performed on the DevOps platform side.

### Which identity providers does SonarQube Cloud support? <a href="#which-identity-providers-does-sonarcloud-support" id="which-identity-providers-does-sonarcloud-support"></a>

The following code repository platforms are supported as identity providers:

* * GitHub
  * Bitbucket Cloud
  * Azure DevOps Services
  * GitLab

You must have an account on one of these code repository platforms to log in to SonarQube Cloud.

### How do I get rid of issues that are false-positives? <a href="#how-do-i-get-rid-of-issues-that-are-false-positives" id="how-do-i-get-rid-of-issues-that-are-false-positives"></a>

#### False Positive and Accept <a href="#false-positive-and-accept" id="false-positive-and-accept"></a>

* You can mark individual issues as *false positive* or \*accepted \*through the issues interface. If you’re using short-lived branch and pull request analysis, issues marked as false positive or accepted will retain that status after merge. This is the preferred approach.

**Help us improve our detection of security issues**

When you mark a vulnerability as false positive or accepted, explain why in the comment box. This feedback and the vulnerability context (current file content, issue and rule details) are reviewed by our teams to make SonarQube Cloud better.

**//NOSONAR**

* Most language analyzers support the use of the generic mechanism: `//NOSONAR` at the end of the line of the issue. This will suppress all issues - now and in the future - that might be raised on the line.

### How do I find and remove projects that haven’t been analyzed in a while? <a href="#how-do-i-find-and-remove-projects-that-havent-been-analyzed-in-a-while" id="how-do-i-find-and-remove-projects-that-havent-been-analyzed-in-a-while"></a>

* In your organization: **Administration** > **Projects Management** you can search for **Last analysis before** to filter projects not analyzed since a specific date, and then use bulk **Delete** to remove the projects that match your filter.
* This can be automated using the corresponding Web API: `api/projects/bulk_delete?organization=ORG-KEY&analyzedBefore=YYYY-MM-DD`.

### What are the browsers supported by SonarQube Cloud? <a href="#what-are-the-browsers-supported-by-sonarcloud" id="what-are-the-browsers-supported-by-sonarcloud"></a>

* SonarQube Cloud supports the following browsers:
  * the last 3 Chrome versions
  * the last 3 Firefox versions
  * the last 3 Safari versions
  * the last 3 Edge versions

### What Java versions are supported by SonarQube Cloud? <a href="#what-java-versions-are-supported-by-sonarcloud" id="what-java-versions-are-supported-by-sonarcloud"></a>

#### Java Version of Scanner Environment <a href="#java-version-of-scanner-environment" id="java-version-of-scanner-environment"></a>

* If you are performing analysis in your local build environment through an installed scanner tool, then the Java runtime environment of the scanner (that is, the Java installed on your build machine) should be at least Java 17.
* Similarly, if you are analyzing in a CI service, you should configure the Java environment to at least Java 17.
* If you are exclusively using automatic analysis, that is, where the SonarQube Cloud service itself does the analysis, you do not have to do anything.

#### Java Version of Targeted Code <a href="#java-version-of-targeted-code" id="java-version-of-targeted-code"></a>

* Pre-Java-17 code (for example, Java 11 code) will continue to be analyzable. The version bump applies only to the environment within which the scanner is running, not the code that is being analyzed. See the [general-requirements](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/scanner-environment/general-requirements "mention") page for more details.
