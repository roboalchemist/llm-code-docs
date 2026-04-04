# Source: https://docs.snyk.io/scan-with-snyk/snyk-open-source/package-repository-integrations/nexus-repository-manager-connection-setup/nexus-repository-manager-for-npm.md

# Nexus repository manager for npm

{% hint style="info" %}
**Feature availability**\
Package repository integrations are available only with Enterprise plans. For more information, see [plans and pricing](https://snyk.io/plans/).

This guide is relevant for Snyk Web UI integrations only; the Snyk CLI supports Yarn and npm Projects with private Nexus Repository Manager registries.
{% endhint %}

Snyk can use Nexus Repository Manager with npm and Yarn Projects imported from Git.

This enables Snyk to regenerate lockfiles with the correct URLs when creating Pull/Merge Requests.

You can add configuration to tell Snyk where your private Nexus Repository Manager Node.js packages are hosted and under what scope.

This is the same information you would normally add in your `.yarnrc` or `.npmrc`

## JavaScript language settings

Go to **Settings** > **Languages** > **JavaScript** and either the npm or Yarn settings, depending on your Project type.

If you have not previously connected to Nexus Repository Manager you will be asked to configure an integration first; see [Nexus Repository Manager connection setup](https://docs.snyk.io/scan-with-snyk/snyk-open-source/package-repository-integrations/nexus-repository-manager-connection-setup).

Follow the steps on the tabs below, according to your version of Nexus.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8aa783a5fbf2e0a504dde94e198e226c2e330549%2Fimage.png?alt=media" alt=""><figcaption><p>Configure Nexus registry</p></figcaption></figure>

{% tabs %}
{% tab title="Nexus 3" %}

1. Select **Add registry configuration.**
2. Select **Nexus** as the Package source.
3. If you want to configure this registry as the default registry url, leave the scope blank.
4. If you want to configure only scoped packages to use this registry, add a scope.
5. If you want to add a mix of the default registry url and scoped packages, add multiple configurations, one for the default and one per scope.
6. The **Repository** section should be set as whatever comes after `repository/` in the internal repository URL.\
   For example, if the URL is `http://nexus.company.io/repository/npm-group`, **Repository** should be set as `npm-group.`
7. When you have added all the registries and scopes you want, click **Update settings**.
   {% endtab %}

{% tab title="Nexus 2" %}

1. Select **Add registry configuration**.
2. Select **Nexus** as the **Package source**.
3. If you want to configure this registry as the **default registry url**, leave the **scope** blank.
4. If you want to configure **only scoped packages** to use this registry, add a **scope**.
5. If you want to add a mix of the **default registry url** and **scoped packages**, add multiple configurations, one for the default and one per scope.
6. The **Repository** section should be set as whatever comes after `nexus/content/` in the internal repository URL.\
   For example, if the URL is `http://nexus.company.io/nexus/content/groups/npm-group`, **Repository** should be set as `groups/npm-group` .\
   Or for `http://nexus.company.io/nexus/content/repositories/npm-hosted`, **Repository** should be set as `repositories/npm-hosted.`
7. When you have added all the registries and scopes you want, click **Update settings**.
   {% endtab %}
   {% endtabs %}

## Test it out

Open a Pull/Merge Request on a Project that contains private dependencies that are hosted in Nexus to see a lockfile updated and included in the Snyk Fix Pull Request with the correct URL to your repository.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-41044ea175c6c72384cfb0bea32e451a8f1cc22a%2FScreenshot%202022-07-15%20at%2014.22.59.png?alt=media" alt="Pull request to test Nexus integration"><figcaption><p>Pull request to test Nexus integration</p></figcaption></figure>
