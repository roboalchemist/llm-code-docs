# Source: https://help.aikido.dev/code-scanning/local-code-scanning.md

# Local Code Scanning

Local code scanning lets you analyze your source code directly on your own machines without sending any code to Aikido. It is useful when you want to test changes during development, work in isolated environments, or keep sensitive repositories fully local.

{% hint style="success" %}
For most workflows we still recommend using the [standard Aikido integrations](https://help.aikido.dev/code-scanning/connect-your-source-code) as they give faster results and better coverage.
{% endhint %}

Before you start, make sure you have an Aikido account/workspace that supports local scanning. Follow [Account Creation for Local Scanning](https://help.aikido.dev/code-scanning/local-code-scanning/account-creation-for-local-scanning-on-aikido).

If you are looking to scan container images instead, check the [container image scanning docs](https://help.aikido.dev/container-image-scanning/local-image-scanning).

## General

{% content-ref url="local-code-scanning/account-creation-for-local-scanning-on-aikido" %}
[account-creation-for-local-scanning-on-aikido](https://help.aikido.dev/code-scanning/local-code-scanning/account-creation-for-local-scanning-on-aikido)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/pr-gating-for-code-using-local-scanner" %}
[pr-gating-for-code-using-local-scanner](https://help.aikido.dev/code-scanning/local-code-scanning/pr-gating-for-code-using-local-scanner)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/release-gating-for-code-using-local-scanner" %}
[release-gating-for-code-using-local-scanner](https://help.aikido.dev/code-scanning/local-code-scanning/release-gating-for-code-using-local-scanner)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/performing-nightly-scans-using-the-aikido-local-scanner" %}
[performing-nightly-scans-using-the-aikido-local-scanner](https://help.aikido.dev/code-scanning/local-code-scanning/performing-nightly-scans-using-the-aikido-local-scanner)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/cli-options-for-local-scanner" %}
[cli-options-for-local-scanner](https://help.aikido.dev/code-scanning/local-code-scanning/cli-options-for-local-scanner)
{% endcontent-ref %}

## CI/CD Integrations

{% content-ref url="local-code-scanning/azure-devops-server-setup-for-local-code-scanning" %}
[azure-devops-server-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/azure-devops-server-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/bitbucket-pipeline-setup-for-local-code-scanning" %}
[bitbucket-pipeline-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/bitbucket-pipeline-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/bamboo-setup-for-local-code-scanning" %}
[bamboo-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/bamboo-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/circleci-setup-for-local-code-scanning" %}
[circleci-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/circleci-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/github-action-setup-for-local-code-scanning" %}
[github-action-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/github-action-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/gitlab-self-managed-setup-for-local-code-scanning" %}
[gitlab-self-managed-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/gitlab-self-managed-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/jenkins-setup-for-local-code-scanning" %}
[jenkins-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/jenkins-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/teamcity-pipeline-setup-for-local-code-scanning" %}
[teamcity-pipeline-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/teamcity-pipeline-setup-for-local-code-scanning)
{% endcontent-ref %}

## Operating Systems

{% content-ref url="local-code-scanning/linux-setup-for-local-code-scanning" %}
[linux-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/linux-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/mac-setup-for-local-code-scanning" %}
[mac-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/mac-setup-for-local-code-scanning)
{% endcontent-ref %}

{% content-ref url="local-code-scanning/windows-setup-for-local-code-scanning" %}
[windows-setup-for-local-code-scanning](https://help.aikido.dev/code-scanning/local-code-scanning/windows-setup-for-local-code-scanning)
{% endcontent-ref %}

## Other

{% content-ref url="local-code-scanning/local-scanning-in-existing-scm-integrated-workspaces" %}
[local-scanning-in-existing-scm-integrated-workspaces](https://help.aikido.dev/code-scanning/local-code-scanning/local-scanning-in-existing-scm-integrated-workspaces)
{% endcontent-ref %}
