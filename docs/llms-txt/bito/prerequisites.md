# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/prerequisites.md

# Prerequisites

## Minimum System Requirements

A machine with the following minimum specifications is recommended for Docker image deployment and for obtaining optimal performance of the AI Code Review Agent.

| Requirement     | Minimum Specification |
| --------------- | --------------------- |
| CPU Cores       | 4                     |
| RAM             | 8 GB                  |
| Hard Disk Drive | 80 GB                 |

***

## Supported Operating Systems

* Windows
* Linux
* macOS

***

## OS Prerequisites

<table><thead><tr><th width="192" align="center">Operating System</th><th>Installation Steps</th></tr></thead><tbody><tr><td align="center"><strong>Linux</strong></td><td><p><strong>You will need:</strong></p><ol><li><p><strong>Bash</strong> (minimum version 4.x)</p><ul><li><p>For Debian and Ubuntu systems</p><p><code>sudo apt-get install bash</code></p></li></ul><p></p><ul><li><p>For CentOS and other RPM-based systems</p><p><code>sudo yum install bash</code></p></li></ul></li></ol><p> </p><ol start="2"><li><p><strong>Docker</strong> (minimum version 20.x)</p><ul><li><a href="https://docs.docker.com/engine/install/">View Guide</a></li></ul></li></ol><p> </p></td></tr><tr><td align="center"><strong>macOS</strong></td><td><p><strong>You will need:</strong></p><ol><li><p><strong>Bash</strong> (minimum version 4.x)</p><p><code>brew install bash</code></p></li></ol><p></p><ol start="2"><li><p><strong>Docker</strong> (minimum version 20.x)</p><ul><li><a href="https://docs.docker.com/engine/install/">View Guide</a></li></ul></li></ol><p> </p></td></tr><tr><td align="center"><strong>Windows</strong></td><td><p><strong>You will need:</strong></p><ol><li><p><strong>PowerShell</strong> (minimum version 5.x)</p><ul><li><a href="https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4">View Guide</a></li><li>Note: In PowerShell version 7.x, run <code>Set-ExecutionPolicy Unrestricted</code> command. It allows the execution of scripts without any constraints, which is essential for running scripts that are otherwise blocked by default security settings.</li></ul></li></ol><p></p><ol start="2"><li><p><strong>Docker</strong> (minimum version 20.x)</p><ul><li><a href="https://docs.docker.com/engine/install/">View Guide</a></li></ul></li></ol><p> </p></td></tr></tbody></table>

***

## Required Access Tokens

* **Bito Access Key:** Obtain your Bito Access Key. [**View Guide**](https://docs.bito.ai/help/account-and-settings/access-key)
* **GitHub Personal Access Token (Classic):** For GitHub PR code reviews, ensure you have a CLASSIC personal access token with repo access. We do not support fine-grained tokens currently. [**View Guide**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)  &#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBZH0vDwrPqYQPMIxIyNW%2Fimage.png?alt=media&#x26;token=a4c42d8d-61a5-4cdb-87a1-622c0ba8f1ae" alt=""><figcaption><p><strong>GitHub Personal Access Token (Classic)</strong></p></figcaption></figure>

* **GitLab Personal Access Token:** For GitLab PR code reviews, a token with API access is required. [**View Guide**](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FghbsjA3aafRQJBQGnksv%2Fimage%20(1).png?alt=media&#x26;token=6feb55f7-39b3-4d61-8e46-f6b233e64849" alt=""><figcaption><p><strong>GitLab Personal Access Token</strong></p></figcaption></figure>

* **Snyk API Token (Auth Token):** For Snyk vulnerability reports, obtain a Snyk API Token. [**View Guide**](https://docs.snyk.io/getting-started/how-to-obtain-and-authenticate-with-your-snyk-api-token)
