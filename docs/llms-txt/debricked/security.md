# Source: https://docs.debricked.com/product/project-health/security.md

# Security

The security of a repository is crucial in many aspects of open source, as the security of a project determines the security of your product. This metric measures both indicators of vulnerability entry risk, and past vulnerability response performance.\
Between each layer, there are weights that determine the impact of any given feature on a practice, and of any given practice on the [metric](https://docs.debricked.com/product/project-health/..#what-is-a-health-metric). You can find the data model illustrated below:

### Vulnerability response

This practice describes how fast vulnerabilities are being handled in a repository. A high score means that maintainers and contributors solve vulnerability risks in a timely manner.

The following features of Vulnerability Response are measured:

* Vulnerability Disclosure to Patch - The median number of days it takes for a vulnerability disclosed by a CNA to be patched from its disclosure. This can be inverted if the patch was released before the disclosure date.
* Vulnerability Entry to Disclosure - The number of days it takes for a vulnerability disclosed by a CNA to be discovered from when the vulnerable code was committed.
* Security Activity over Time - The security activity in a project per month for the past year (whether it is a stable activity or comes in bursts).
* Dead Issue Rate - The rate of stale or dead issues, defined as having been open for 52 weeks without being closed.
* Maintainer Responsiveness - Indicates whether maintainers (contributors with merge rights) are responding to issues in the project. If they’re not responding to any recent issues, it may indicate that the project is going “stale”.

### Vulnerability risk

This practice looks into the nature of reported vulnerabilities in the project. The following features of Vulnerability Risk are measured:

* Commits per Vulnerability - How frequently vulnerabilities are reported in relation to the project's size in commits. A higher number means vulnerabilities are less frequent.
* Vulnerability Severity - How serious the reported vulnerabilities are.
* CWE Diversity - The types of vulnerabilities being reported. Multiple vulnerabilities of the same type may indicate that the project's contributors are not learning from previous mistakes.

### Coding best practices

This practice describes how well the project contributors adhere to best practices that boost code quality, which correlates with the risk of exposure to vulnerabilities.

The following features of Coding Best Practices are measured:

* Review Comments per Pull-request - The average number of review comments a pull request has, indicating how much feedback is provided by the reviewers.
* Reviewers per Pull-request - The average number of reviewers per pull request before merge.
* Pull-request Size - The average pull request size, measured in lines of code changed in the pull requests submitted during the past 52 weeks.
* Seniority of Reviewers - How experienced the reviewers of pull requests are. Seniority is calculated as the average number of pull requests that a reviewer has on GitHub.

### Bug reporting

This practice describes the rate of bug reports in the project. The following features of Bug Reporting are measured:

* Issue Bug Saturation - The percentage of issues that are bug reports.
* Commits per Bug - The frequency of bug issues per commit made.
