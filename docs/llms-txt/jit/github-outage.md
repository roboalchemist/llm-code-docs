# Source: https://docs.jit.io/docs/github-outage.md

# GitHub has an Outage

## Overview

During a GitHub outage, our security checks are temporarily affected, preventing the scanning and detection of findings in your CI/CD environment. Here are the steps Jit takes to handle the GitHub outage and important information you should know.

### During an outage

* We actively monitor the GitHub outage and resume running our security checks as soon as the issue is resolved. We will provide updates on Slack and in the Jit UI to keep you informed.
* With branch protection (Jit Security): If you have configured branch protection for Jit Security, developers will be unable to merge their pull requests until the GitHub outage is resolved. Please note that GitHub admins have the ability to modify this configuration if necessary. However, we do not recommend that you make changes during the outage.
* Without branch protection: In the absence of branch protection, developers may still merge their pull requests during the GitHub outage, potentially including security findings.

### Post-outage full scan

* Regardless of branch protection settings, Jit collects all repositories where pull requests were merged during the GitHub outage. Once the issue is resolved, we perform a full scan to check if any new findings were introduced. You will be able to view these findings on your backlog page or receive Slack notifications if enabled.

### Important to know

Please note that while some GitHub services might still be running, our scans and checks are temporarily unavailable. We recommend checking the current status of GitHub [here](https://www.githubstatus.com/) and the GitHub Incident History [here](https://www.githubstatus.com/history?page=1) for updates on the outage (please note that there may be delays in reporting new incidents).

We apologize for any inconvenience caused and appreciate your understanding and cooperation during this time.