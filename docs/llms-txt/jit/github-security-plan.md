# Source: https://docs.jit.io/docs/github-security-plan.md

# GitHub Security Plan

# GitHub Misconfigurations

GitHub misconfigurations pose serious threats to both organizations and users. These threats include the potential exposure of sensitive data, theft of intellectual property and compromised systems. Therefore, to safeguard the security of their sensitive data and to prevent misconfigurations, it is crucial that organizations and GitHub users periodically review and monitor GitHub configurations.

Jit's GitHub Security Plan runs periodic scans for GitHub misconfigurations and communicates the findings on the Backlog page.

## Security Tools

Jit seamlessly integrates the following tools to provide comprehensive security coverage across your GitHub organization and repositories:\
**[Legitify](https://github.com/Legit-Labs/legitify), [chain-bench](https://github.com/aquasecurity/chain-bench), Jit's MFA & Branch Protection Checkers**.

## Required Permissions

Jit requires a **GitHub Personal Access Token** to activate the plan items in the GitHub Security Plan.

To generate a **Personal Access Token** click  ["Generate PAT"](https://github.com/settings/tokens/new?description=Jit-GH-Security-PAT\&scopes=repo,read:repo_hook,read:enterprise,read:packages,read:org) when integrating with GitHub Security.

The following permissions are required in the token:

* repo
* read:repo\_hook
* read:org
* read:enterprise
* read:packages

> ❗️ Organizations with Single Sign-On (SSO) must authorize the new token
>
> Right after generating the token in GitHub, copy it because you won't be able to see it again. Then click the "Configure SSO" button and in the pop-up, click "Authorize" next to your organization's name.

Providing a token with the required permissions allows you to activate the following plan items:

| Coverage          | Plan Item                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Security Controls              |
| :---------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Branch Protection | Protect code changes by properly setting branch protection     | Failure to correctly set branch protection rules exposes your repositories to unauthorized changes. This leaves sensitive code vulnerable to modification, removal and exposure by any member, including those with malicious intentions. Crucial safeguards include enforcing pull request reviews, requiring status checks and ensuring branches are up to date before merging. Additional crucial safeguards are protecting the default branch, preventing forceful modifications to branch history and collectively fortifying the security and integrity of your codebase. | Legitify                       |
| Access Management | Enable multi-factor authentication for members                 | Without multi-factor authentication, your organization's accounts are more vulnerable to attackers employing password spraying or phishing methods. Relying solely on single-factor authentication provides minimal security, posing a significant risk to your entire codebase if compromised. It's crucial to ensure that all organization members enable multi-factor authentication. This includes applying multi-factor authentication to access the package registry.                                                                                                     | Jit's MFA Checker, Chain Bench |
| External Exposure | Limit the creation of public repos                             | Allowing unrestricted creation of public repositories can result in accidental exposure of proprietary or sensitive code and data. This poses not only a data leak risk but also invites unauthorized access and tampering. Ensuring that only authorized users can create public repositories is a crucial step in protecting your organization's intellectual property and sensitive information.                                                                                                                                                                             | Legitify                       |
| Access Management | There are no dormant GitHub users                              | Failing to regularly review and remove inactive users can turn dormant accounts into security risks. These unmonitored accounts can be hijacked and used as entry points for unauthorized activities without immediate detection.                                                                                                                                                                                                                                                                                                                                               | Chain Bench                    |
| Access Management | Limit user permissions to follow the least privilege principle | Failing to adhere to POLP can severely compromise your environment's security posture. Overly permissive settings not only invite operational errors but also expose avenues for unauthorized or malicious activities. To minimize potential points of failure and reduce the risk of data breaches or other security incidents, limit member permissions to only what is absolutely necessary. For example, restricting default member permissions and disabling anonymous access to artifacts.                                                                                | Chain Bench, Legitify          |

#### Without a Personal Access Token

The following plan items are available without a **Personal Access Token**:

| Category          | Plan Item                                   | Description                                                                                                                                                                                                                                                                         | Security Controls               |
| :---------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| Branch Protection | Set desired branch protection configuration | Failure to configure branch protection rules leaves your repositories vulnerable to unauthorized alterations. Setting your own rules, like a minimum number of code reviewers and mandatory status checks, provides an added layer of security against flawed or malicious changes. | Jit's Branch Protection Checker |