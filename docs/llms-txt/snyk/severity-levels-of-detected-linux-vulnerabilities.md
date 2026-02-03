# Source: https://docs.snyk.io/scan-with-snyk/snyk-container/how-snyk-container-works/severity-levels-of-detected-linux-vulnerabilities.md

# Severity levels of detected Linux vulnerabilities

When determining the [severity level](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/severity-levels) of a Linux vulnerability (Low, Medium, High, Critical), Snyk Container considers multiple factors:

* Snyk internal analysis
* An assessment of the severity provided by the Linux distribution security maintainers
* The severity of the vulnerability, as assessed by the National Vulnerability Database (NVD).

In certain cases, NVD assigns a different CVSS vector and severity score from the security maintainers of a particular Linux distribution. When this occurs, Snyk prioritizes and uses the CVSS and severity determined by the Linux distribution maintainers, as asserted by the relative importance feature.

## Relative importance feature

Relative importance asserts a common severity for a vulnerability and shows the underlying detailed information for that severity based on multiple sources. This allows developers and analysts to view a common level of importance and exposes the underlying information that contributed to the asserted severity.

Snyk supports relative importance in Ubuntu, Debian, Red Hat Enterprise Linux (RHEL), CentOS, Amazon Linux, Oracle Linux, and SUSE Linux Enterprise Server (SLES).

## View relative importance

For each issue, information appears on the Project page, under **Security information**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e16740be4b29723affd8214e35ce57188b1bd3a6%2Fproject_page_security_information.png?alt=media" alt=""><figcaption><p>Security information on a Project page</p></figcaption></figure>

## External information sources for relative importance

To provide information for the distribution, Snyk uses the following external sources:

* [NVD Severity](https://nvd.nist.gov/vuln)
* [Debian Severity Levels](https://security-team.debian.org/security_tracker.html#severity-levels) and [no-dsa](https://security-team.debian.org/security_tracker.html#issues-not-warranting-a-security-advisory) issues
* [Ubuntu CVE Priority](https://people.canonical.com/~ubuntu-security/priority.html)
* [Red Hat Enterprise Linux Severity Rating](https://access.redhat.com/security/updates/classification)
* [SUSE Linux Enterprise Security Rating Overview](https://www.suse.com/support/security/rating/)
* [Amazon Linux](https://alas.aws.amazon.com/alas2.html)

## View NVD Score and Severity for Linux vulnerabilities

To create a report showing only NVD Score and Severity (without the Linux-maintainer rating), add the NVD Score and NVD Severity columns in the Issues Detail report.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0554c8e4a882fb148c9c82bf309c07173ee26bcf%2Fcontainer-NVD-report.png?alt=media" alt=""><figcaption><p>Example of a report with NVD Score and NVD Severity</p></figcaption></figure>
