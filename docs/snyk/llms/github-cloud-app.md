# Source: https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations/github-cloud-app.md

# GitHub Cloud App

{% hint style="info" %}
**Feature availability**

If you are using Broker, see the [Universal Broker documentation](https://docs.snyk.io/implementation-and-setup/enterprise-setup/snyk-broker/universal-broker).

If you want to use your own GitHub App, reach out to your Snyk account team.

The GitHub Cloud App does not have pre-configured IP addresses that can be automatically added to your allowlist. Contact your Snyk account team to obtain the Snyk IPs for manual addition.
{% endhint %}

## Prerequisites for GitHub Cloud App

* Snyk Organization Admin user role.
* GitHub Organization Admin user role.
* A public, internal or private GitHub repository.
* The required app permissions. For more information, see [GitHub Cloud App permission requirements](https://docs.snyk.io/developer-tools/user-permissions-and-access-scopes#github-cloud-app-permission-requirements).

{% hint style="info" %}
Users can install the app on GitHub Organizations they are Repository Admins on through the GitHub UI.

The GitHub Cloud App integration is available at the Organization level within the Snyk Web UI.
{% endhint %}

## GitHub Cloud App benefits

The GitHub Cloud App improves on many features as compared to the current GitHub integration, including role-based, granular access control, increased API rate limits, and creation of an entry point for expanded and enhanced developer experiences.

* RBAC (Role-Based Access Control) Compliance: With the GitHub Cloud App, the access control mechanism is decoupled from individual user accounts. Instead, it is associated with the app entity itself. This separation allows for better management and enforcement of RBAC policies, as access control is handled at the application level rather than being tied to individual user accounts.
* Granular access control: The GitHub Cloud App allows for fine-grained control over access permissions at the repository level.
* Increased API rate limit: The GitHub Cloud App provides higher rate limits, allowing Snyk to make a larger number of API requests. This increased limit will assist in handling large-scale use cases, such as monorepos with a large number of Projects, GitHub organizations with a large number of repositories, and more.
* Enabler for an enhanced developer experience:
  * Pull request checks: The Checks tab experience in GitHub is exclusively accessible through the GitHub Cloud App, enabling an SCM native experience as part of potential future PR check workflow improvements.
  * Fix and upgrade pull requests: Pull requests initiated by Snyk are performed directly by the GitHub App rather than a service account.

## How to set up the GitHub Cloud App

{% hint style="warning" %}
When setting up the GitHub Cloud App, you can only implement one of the following scenarios:

* One GitHub organization connected to one Snyk Organization
* One GitHub organization connected to multiple Snyk Organizations
  {% endhint %}

Log in to your Snyk account and navigate to the Integrations section in the Snyk Organization where you would like to set up the GitHub Cloud App.

Select the **GitHub Cloud App** tile.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-979dd27b4fab4d47003090885d06e27070deb9cc%2Fimage.png?alt=media" alt=""><figcaption><p>GitHub Cloud App tile on the Integrations page</p></figcaption></figure>

In the confirmation modal, select **Configure GitHub Cloud App.**

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-040c247776b86b8a7cfa673bf6606fe9d07d73a0%2FScreenshot%202024-06-26%20at%2010.03.50.png?alt=media" alt="Configuration notice for the GitHub Cloud App" width="375"><figcaption><p>Configuration notice for the GitHub Cloud App</p></figcaption></figure>

You are then asked to authorize the app to act on your user’s behalf. The app uses this information to check which GitHub organizations you are authorized to install the app in.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0a5ef3a6e7f12f83cdab9368e2a94b016b94085e%2FScreenshot%202024-06-26%20at%2010.05.37.png?alt=media" alt="" width="375"><figcaption><p>User authorization for the app</p></figcaption></figure>

When the install screen in GitHub opens, you can select the GitHub organization where you wish to install the app.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-39cf9c4793294caa82cf3a3695448fc0a30c80c2%2FScreenshot%202024-06-26%20at%2010.06.25.png?alt=media" alt="Selection of the GitHub organization to install the app into" width="375"><figcaption><p>Selection of the GitHub organization to install the app into</p></figcaption></figure>

If the GitHub Cloud App is already installed in a GitHub organization, you can select that same GitHub organization during the integration process for a different Snyk Organization.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-7bd914e6be3562513823466010f3834d523046c4%2FScreenshot%202024-06-26%20at%2010.13.54.png?alt=media" alt="Connect another GitHub organization into a Snyk Organization" width="563"><figcaption><p>Connect another GitHub organization into a Snyk Organization</p></figcaption></figure>

Specify whether you wish to install the app in all of the repositories belonging to the selected GitHub organization, or you want to install the app in a select number of repositories belonging to a GitHub organization; then click **Install & Authorize**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d5b9f72b5cce9c3ecbccf445131fcbdadaada7d1%2Fpermissions-install-authorize-github-cloud-app.png?alt=media" alt="Install and Authorize settings for the GitHub organization you are installing the GitHub Cloud App into" width="375"><figcaption><p>Install and authorize settings for the GitHub organization you are installing the GitHub Cloud App into</p></figcaption></figure>

{% hint style="warning" %}
The GitHub Cloud App will lose access to Snyk if it is uninstalled from the GitHub organization or if the repositories to which the app instance has access are edited.
{% endhint %}

## How to migrate to the GitHub Cloud App

If you are an Enterprise plan customer, you can migrate Snyk Targets to the GitHub Cloud App using the [snyk-migrate-to-github-app](https://github.com/snyk-labs/snyk-migrate-to-github-app) tool in the [tool repository](https://github.com/snyk-labs/snyk-migrate-to-github-app).
