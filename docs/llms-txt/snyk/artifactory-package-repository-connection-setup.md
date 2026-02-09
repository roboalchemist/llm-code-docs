# Source: https://docs.snyk.io/scan-with-snyk/snyk-open-source/package-repository-integrations/artifactory-package-repository-connection-setup.md

# Artifactory package repository connection setup

{% hint style="info" %}
**Feature availability**\
Package repository integrations are available only with Enterprise plans. For more information, see [plans and pricing](https://snyk.io/plans/).

**Supported projects**\
The Artifactory Package Repository integration supports [Node.js](https://docs.snyk.io/supported-languages/supported-languages-list/javascript#supported-package-managers-and-package-registries) (npm and Yarn) and [Maven](https://docs.snyk.io/supported-languages/supported-languages-list/java-and-kotlin#supported-package-managers-and-package-registries) Projects. For [Improved Gradle SCM scanning](https://docs.snyk.io/supported-languages/supported-languages-list/java-and-kotlin/git-repositories-with-maven-and-gradle#improved-gradle-scm-scanning), use the Maven settings.
{% endhint %}

Connecting a custom Artifactory Package Repository enables Snyk to resolve all direct and transitive dependencies of packages hosted on the custom registry and calculate a more complete, accurate dependency graph and related vulnerabilities.

You can configure these types of Artifactory Package Repository:

* Publicly accessible instances protected by basic authentication
* Instances on a private network by using Snyk Broker (with or without basic authentication).

These instructions apply to configuring publicly accessible instances. For instructions on configuring a brokered instance, see the [setup instructions for Snyk Broker with Artifactory Repository](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/classic-broker/install-and-configure-snyk-broker/artifactory-repository-install-and-configure-broker).

The steps to set up Artifactory Repository Manager follow.

1. Navigate to **Settings** > **Integrations** > **Package Repositories** > **Artifactory**.
2. Enter the URL of your Artifactory instance; this must end with `/artifactory`.
3. Enter your username and password.
4. Select **Save**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3d4114d95e16097627b994eb23a578966960b8f9%2Fscreenshot_2020-04-17_at_14.38.12.png?alt=media&#x26;token=0e04ad73-fc10-4cb1-b0a6-e339d4704023" alt="Artifactory repository setup"><figcaption><p>Artifactory repository setup</p></figcaption></figure>
