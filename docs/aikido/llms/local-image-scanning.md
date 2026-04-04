# Source: https://help.aikido.dev/container-image-scanning/local-image-scanning.md

# Local Image Scanning

Local image scanning lets you analyze container images on your own machines without sending any code or images to Aikido. It is useful when you want to test builds during development, debug issues in isolated environments, or keep sensitive images fully local.

{% hint style="success" %}
For day to day workflows we recommend using a [cloud provider integration](https://help.aikido.dev/container-image-scanning/cloud-provider-registries) or the [standalone registries](https://help.aikido.dev/container-image-scanning/standalone-registries) since both give faster results and better coverage.
{% endhint %}

If you are looking for [source code scanning instead, check the code scanning docs](https://help.aikido.dev/code-scanning/local-code-scanning).

## General

{% content-ref url="local-image-scanning/setting-up-image-scanning-with-local-scanner" %}
[setting-up-image-scanning-with-local-scanner](https://help.aikido.dev/container-image-scanning/local-image-scanning/setting-up-image-scanning-with-local-scanner)
{% endcontent-ref %}

{% content-ref url="local-image-scanning/pr-gating-for-container-images-using-local-image-scanner" %}
[pr-gating-for-container-images-using-local-image-scanner](https://help.aikido.dev/container-image-scanning/local-image-scanning/pr-gating-for-container-images-using-local-image-scanner)
{% endcontent-ref %}

## CI/CD Integrations

{% content-ref url="local-image-scanning/azure-devops-server-setup-for-local-image-scanning" %}
[azure-devops-server-setup-for-local-image-scanning](https://help.aikido.dev/container-image-scanning/local-image-scanning/azure-devops-server-setup-for-local-image-scanning)
{% endcontent-ref %}

{% content-ref url="local-image-scanning/bitbucket-pipeline-setup-for-local-image-scanning" %}
[bitbucket-pipeline-setup-for-local-image-scanning](https://help.aikido.dev/container-image-scanning/local-image-scanning/bitbucket-pipeline-setup-for-local-image-scanning)
{% endcontent-ref %}

{% content-ref url="local-image-scanning/circleci-setup-for-local-image-scanning" %}
[circleci-setup-for-local-image-scanning](https://help.aikido.dev/container-image-scanning/local-image-scanning/circleci-setup-for-local-image-scanning)
{% endcontent-ref %}

{% content-ref url="local-image-scanning/github-action-setup-for-local-image-scanning" %}
[github-action-setup-for-local-image-scanning](https://help.aikido.dev/container-image-scanning/local-image-scanning/github-action-setup-for-local-image-scanning)
{% endcontent-ref %}

{% content-ref url="local-image-scanning/gitlab-setup-for-local-image-scanning" %}
[gitlab-setup-for-local-image-scanning](https://help.aikido.dev/container-image-scanning/local-image-scanning/gitlab-setup-for-local-image-scanning)
{% endcontent-ref %}

{% content-ref url="local-image-scanning/jenkins-setup-for-local-image-scanning" %}
[jenkins-setup-for-local-image-scanning](https://help.aikido.dev/container-image-scanning/local-image-scanning/jenkins-setup-for-local-image-scanning)
{% endcontent-ref %}

## Other

{% content-ref url="local-image-scanning/setting-up-kaniko-image-scanning-with-local-scanner" %}
[setting-up-kaniko-image-scanning-with-local-scanner](https://help.aikido.dev/container-image-scanning/local-image-scanning/setting-up-kaniko-image-scanning-with-local-scanner)
{% endcontent-ref %}
