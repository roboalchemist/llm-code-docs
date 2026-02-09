# Source: https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/cli-tools/snyk-scm-contributors-count/scripts-for-scm-contributors-count/bitbucket-cloud.md

# Source: https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations/bitbucket-cloud.md

# Bitbucket Cloud

{% hint style="info" %}
Snyk recommends installing or migrating to the [Bitbucket Cloud Application](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations/bitbucket-cloud-app) for smoother integration and to ensure long-term support.
{% endhint %}

The Bitbucket Cloud API token integration lets you:

* Continuously perform security scanning across all the integrated repositories
* Detect vulnerabilities in your open-source components
* Provide automated fixes and upgrades

### How to set up the Bitbucket Cloud Integration

{% hint style="info" %}
Admin permissions are required; however, Snyk's access is ultimately limited by the [permissions assigned to the API Token](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/).\
\
To improve security, the use of app passwords in Bitbucket Cloud is transitioning to API tokens. Existing integrations that use app passwords will continue to function temporarily until 9 June 2026.\
To ensure continued support and functionality, update your Bitbucket Cloud integration in Snyk to use an API token.
{% endhint %}

1. To give Snyk access to your Bitbucket account, set up a dedicated service account in Bitbucket with admin permissions. See the [Bitbucket documentation ](https://support.atlassian.com/bitbucket-cloud/docs/grant-access-to-a-workspace/)to learn more about adding users to a workspace.\
   The newly created user must have **Admin** permissions to all the repositories you need to monitor with Snyk.
2. In Snyk, go to the **Integrations** page, open the **Bitbucket Cloud** card, and configure the **Account credentials**.
3. In BitBucket, under the Personal settings, select **Atlassian account settings** > **Security** > **Create and manage API tokens**.
4. Follow the Bitbucket procedure to set up an account with the following permissions:

   * read:user:bitbucket
   * read:workspace:bitbucket
   * read:repository:bitbucket

   See the [Bitbucket documentation ](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/)for more details about the procedure.
5. Enter the email and the [API key for the Bitbucket account](https://developer.atlassian.com/cloud/bitbucket/rest/intro/#api-tokens) you created, and **save** your changes.\
   You can find your email under the Bitbucket **Personal settings.**\
   Snyk connects to your Bitbucket Cloud account. When the connection succeeds, the confirmation message **Bitbucket Cloud settings successfully updated** appears.

### How to add Bitbucket repositories to Snyk

After you connect Snyk to your Bitbucket Cloud account, you can select repositories for Snyk to monitor.

1. In Snyk, go to **Integrations** > **Bitbucket Cloud** card, and click **Add your Bitbucket Cloud repositories to Snyk** to start importing repositories to Snyk.
2. Choose the repositories you want to import to Snyk and click **Add selected repositories**.

After you add the selected repositories, Snyk scans them for dependency files in the entire directory tree, that is, `package.json`, `pom.xml`, and so on, and imports them to Snyk as Projects.

The imported projects appear on your **Projects** page and are continuously checked for vulnerabilities.

### Bitbucket integration features

After the integration is in place, you will be able to use capabilities such as:

* [Project-level security reports](#project-level-security-reports)
* [Project monitoring and automatic fix pull requests](#project-monitoring-and-automatic-fix-pull-requests)
* [Pull request testing](#pull-request-tests)

#### Project-level security reports

Snyk produces advanced [security reports](https://docs.snyk.io/manage-risk/reporting/legacy-reports/legacy-reports-overview) that let you explore the vulnerabilities found in your repositories and fix them immediately by opening a fix pull request directly to your repository, with the required upgrades or patches.

The example that follows shows a Project-level security report.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-364fedf32558182f221772681a893bdeac169ca2%2Fbbc_project-sec-rpt_21sept2022.png?alt=media" alt="An example of a Project-level security report"><figcaption><p>An example of a Project-level security report</p></figcaption></figure>

#### Project monitoring and automatic fix Pull Requests

Snyk scans your Projects on either a daily or a weekly basis. When new vulnerabilities are found, Snyk notifies you by email and by opening [automated pull requests](https://docs.snyk.io/scan-with-snyk/pull-requests/snyk-pull-or-merge-requests/create-automatic-prs-for-new-fixes-fix-prs) with fixes for your repositories.

The example that follows shows a fix Pull Request opened by Snyk.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-75e931440a18474405675a41635c15c4feb15660%2F666.png?alt=media&#x26;token=233293e0-cd37-43e9-bee0-624a12ab05ec" alt="Example of an automatic fix Pull Request opened by Snyk"><figcaption><p>Example of an automatic fix Pull Request opened by Snyk</p></figcaption></figure>

To review and adjust the automatic fix pull request settings:

1. In Snyk, go to **Organization settings** > **Integrations** > **Source control** > **Bitbucket Cloud**, and click **Edit Settings**.
2. Scroll to the **Automatic fix PRs** section and configure the relevant options.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-7f0c95f209e66a9553a316d04b5fd8375ffb6d50%2FScreenshot%202023-05-03%20at%2014.49.59.png?alt=media" alt="Configure Automatic fix PRs"><figcaption><p>Configure Automatic fix PRs</p></figcaption></figure>

{% hint style="info" %}
Unlike manual pull requests opened from the Bitbucket interface, Snyk pull requests are *not* automatically assigned to the default reviewer set in your Bitbucket Cloud account.

For more information, see [Snyk automated pull requests](https://docs.snyk.io/scan-with-snyk/pull-requests/snyk-pull-or-merge-requests/create-automatic-prs-for-new-fixes-fix-prs).
{% endhint %}

#### Pull request tests

Snyk tests any newly-created pull request in your repositories for security vulnerabilities and sends a build check to Bitbucket Cloud. You can see directly from Bitbucket Cloud whether or not the pull request introduces new security issues.

The example that follows shows a Snyk pull request build check on the Bitbucket Cloud **Pull Request** page.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-7efaff20ca4845d9372135ac75b746bf46ecebb8%2F888.png?alt=media&#x26;token=0fabda9d-b182-4c7d-9548-7275d120eaf8" alt="Example of a Snyk pull request build check on the Bitbucket Cloud Pull Request page"><figcaption><p>Example of a Snyk pull request build check on the Bitbucket Cloud <strong>Pull Request</strong> page</p></figcaption></figure>

To review and adjust the pull request tests settings:

1. In Snyk, go to **Organization settings** > **Integrations > Source control** > **Bitbucket Cloud**, and click **Edit Settings**.
2. Scroll to **Default Snyk test for pull requests** > **Open Source Security & Licenses**, and configure the relevant options.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-51630c7bb2dd83e96a8d498d9ff806e45fa4ecb7%2FScreenshot%202022-03-16%20at%2010.07.50.png?alt=media&#x26;token=64278851-ae68-4560-8469-99096cfca820" alt="Configuring the options for pull request Open Source Security &#x26; Licenses"><figcaption><p>Configuring the options for pull request Open Source Security &#x26; Licenses</p></figcaption></figure>

### Required permission scope for the Bitbucket Cloud integration

{% hint style="warning" %}
Bitbucket Cloud has replaced App Passwords with API tokens\
Existing credentials will continue to work normally until completely deprecated by Bitbucket Cloud [details here](https://www.atlassian.com/blog/bitbucket/bitbucket-cloud-transitions-to-api-tokens-enhancing-security-with-app-password-deprecation).\
New integrations will now use API tokens.
{% endhint %}

All the operations, whether triggered manually or automatically, are performed for a Bitbucket Cloud [service account](https://docs.snyk.io/implementation-and-setup/enterprise-setup/service-accounts) that has its token (API Token) configured in the **Integration settings**.

For Snyk to perform the required operations on monitored repositories, such as reading manifest files on a frequent basis and opening fix or upgrade PRs, the integrated Bitbucket Cloud service account needs **Admin** permissions on the imported repositories.

For detailed information on the permission scopes required, see [Bitbucket permission requirements](https://docs.snyk.io/developer-tools/user-permissions-and-access-scopes#bitbucket-cloud-and-bitbucket-data-center-server-scopes).

### How to disconnect Snyk from Bitbucket Cloud

{% hint style="warning" %}
When you disconnect Snyk from your repository Projects, your credentials are removed from Snyk, and any integration-specific Projects that Snyk is monitoring are deactivated in Snyk.\
If you choose to re-enable this integration, you must re-enter your credentials and activate your Projects.
{% endhint %}

To disconnect this integration, in **Organization settings** > **Integrations:**

1. In your list of integrations, select the Bitbucket integration you want to deactivate and click **Edit settings** to open a page with the current status of your integration.\
   \
   The page includes sections that are specific to each integration, where you can manage your credentials, API key, Service Principal, or connection details.
2. Scroll to the relevant section and click **Disconnect.**

### Migrate to the Bitbucket Cloud App

This section describes how to migrate your existing [Bitbucket Cloud API token integration](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations/bitbucket-cloud), displayed in Snyk as Bitbucket Cloud, to the [Bitbucket Cloud App](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations/bitbucket-cloud-app) integration.

To migrate to the new app integration, you must remove all the previously imported Projects from Snyk, delete the API token and its Projects, set up the new app integration, and reimport your Projects to Snyk from the new integration.

{% hint style="info" %}
Before going through the migration process, you should note that the following Project-level information will not persist:

* Historic Project-related data, including trend numbers for fixing vulnerabilities
* Project-related metadata: ignores and tags
  {% endhint %}

### Migration process

The migration process includes the following steps:

1. [Deleting the existing Projects](#delete-existing-projects) that are connected to the Bitbucket Cloud API token integration in Snyk.
2. [Disconnecting the PAT integration](#disconnect-the-pat-integration) in Snyk.
3. Removing the first-party extension for the PAT integration in Bitbucket (optional). This step is explained in the [Disconnect the PAT integration](#disconnect-the-pat-integration) section.
4. [Connecting the Bitbucket Cloud App](#set-up-the-bitbucket-cloud-app-integration) and importing Projects.

#### Delete existing Projects

Delete all the existing Projects in Snyk that were previously imported from the Legacy integration. To use the bulk delete action on the Projects page, change the grouping filter to **Group by none**. You can now select multiple Projects in the list individually or by selecting the checkbox at the top to **Select all visible projects**. To delete a Project, select the trash icon, **Delete selected projects**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-30b3dcca75abd695675ecb665df5e07a26b304b6%2F2023-11-20_14-29-35.png?alt=media" alt="Change the Projects filter to Group by none"><figcaption><p>Change the Projects filter to <strong>Group by none</strong></p></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8b4bf3c2094c54017fa9b16ad77d756e1886858a%2F2023-11-20_14-41-16.png?alt=media" alt="Bulk delete the selected Projects" width="375"><figcaption><p>Bulk delete the selected Projects</p></figcaption></figure>

#### Disconnect the PAT integration

To disconnect the Bitbucket Cloud PAT integration, navigate to the settings page of Bitbucket Cloud integration, scroll to the relevant section, and click **Disconnect.**

Remove the Snyk tab for the PAT integration in Bitbucket Cloud (optional)

The Bitbucket Cloud integration has an optional first-party interface app.

This app can be installed on your Bitbucket Cloud workspace to enrich the PAT integration with a first-party interface as the Snyk tab)

If you have used this app, before setting up the Snyk Bitbucket Cloud App in the next step, remove the previous interface app in Bitbucket Cloud.\
This functionality is supported out-of-the-box in the Snyk App integration.\
\
Go to your **Workspace settings** page in **Bitbucket.org** > **Manage installed apps**, expand the **Snyk Security for Bitbucket Cloud** app, and click **Remove.**

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5c212b38d75babf4df8577b00309a1c9d6d6f6e5%2Fremove_snyk-security-bbc_11oct2022.png?alt=media" alt="Remove the first-party Snyk Legacy interface app in Bitbucket"><figcaption><p>Remove the first-party Snyk Legacy interface app in Bitbucket</p></figcaption></figure>

#### Set up the Bitbucket Cloud App integration

See the [Bitbucket Cloud App integration](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations/bitbucket-cloud-app) topic for instructions.
