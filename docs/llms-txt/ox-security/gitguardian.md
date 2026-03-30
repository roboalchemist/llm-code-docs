# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/secret-pii-scan/gitguardian.md

# GitGuardian

GitGuardian is a leading provider of automated secrets detection and remediation solutions, helping organizations protect sensitive information across their codebases and development workflows.

GitGuardian enables continuous monitoring of public and private repositories to detect exposed secrets like API keys, credentials, and other sensitive data, providing real-time alerts to minimize security risks.

GitGuardian’s platform offers actionable insights and collaboration tools to facilitate swift remediation and ensure compliance with security policies.

By integrating with OX Security, GitGuardian enhances the ability of security teams to correlate detected secrets with broader security issues identified within the OX Security platform.

This integration provides:

* unified visibility into code-related vulnerabilities and secrets exposure, allowing teams to manage and prioritize risks more effectively
* automated detection
* centralized data analysis
* efficient response workflows
* security operations streamline
* stronger control over sensitive data throughout the development lifecycle

The integration process includes the following steps:\
1\. [Generate a GitGuardian token.](#generating-a-gitguardian-token)\
2\. [Connect the OX platform to GitGuardian.](#connecting-to-gitguardian)

## Prerequisites

GitGuardian account with read access.

## Generating a GitGuardian Token

1. Log in to GitGuardian at [dashboard.gitguardian.com](http://dashboard.gitguardian.com/).
2. In the left sidebar, click on **Settings**.
3. Navigate to the **API** section.
4. Click **Create a token**.
5. Enter a name for the token and configure the necessary permissions.
6. Click **Generate**.
7. Copy the token to a secure location. You will not be able to view it again after closing the dialog.

## Connecting to GitGuardian

1. In the **OX app**, go to **Connectors** and search for GitGuardian.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c1634e3f50e5b299e3f9378732e9969cb8651a4c%2FGitGuardian_icon.png?alt=media" alt="" width="124"><figcaption></figcaption></figure>

1. Select **GitGuardian** and set the following parameters in the **Configure your GitGuardian credentials** dialog.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6d4a33b62935141b295e7d25952d4050297a79c0%2FGitGuardian_Connect.png?alt=media" alt="" width="539"><figcaption></figcaption></figure>

| Parameter                | Description                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GitGuardian Host URL** | <p>Add your GitGuardian organization account URL.<br>- Use the default account: <a href="https://api.gitguardian.com/"><https://api.gitguardian.com></a>,<br>- Or use your org account.</p> |
| **Token**                | Paste the GitGuardian token you have generated.                                                                                                                                             |

1. Select **CONNECT**. The success message appears.
