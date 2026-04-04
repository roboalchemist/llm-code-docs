# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/jira-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/jira-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/jira-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/jira-integration.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/jira-integration.md

# Jira Cloud integration

This integration is available in the [Team and Enterprise plans](https://www.sonarsource.com/plans-and-pricing/sonarcloud/).

Before you can create Jira work items in SonarQube Cloud, you need to set up your Jira Cloud integration on the organization and project levels, and have the right permissions.

### Permissions <a href="#permissions" id="permissions"></a>

1. To set up your Jira Cloud integration for your SonarQube organization you need the **Administer Organization** permissions. Go to *Your Organization* > **Administration** > **Permissions** and select the **Administer Organization** checkbox for specific users or groups.
2. To connect your SonarQube project with a Jira Cloud project you need the **Administer** project permissions. Go to *Your Project* > **Administration** > **Permissions** and select the **Administer** checkbox for specific users and groups.

### Binding your organization with Jira Cloud <a href="#binding-your-organization-with-jira" id="binding-your-organization-with-jira"></a>

First, you have to bind Jira Cloud to your organization before you can bind it to individual projects

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-08f139a6b050fc1942daac45a4773015611de122%2Faffecf0866cd0f7ea88e92997f8f8d1a3b57a38a.png?alt=media" alt="Select the Connect button to connect your SonarQube Cloud organization with a Jira instance."><figcaption></figcaption></figure></div>

1. Go to *Your Organization* > **Administration** > **Organization settings** > **Jira**
2. Click **Connect.** You will be redirected to the Atlassian authorization page for 3rd party vendors. Follow the instructions and if you have multiple Jira Cloud instances, make sure to select the right instance.
3. Click **Accept** to authorize the connection.
4. Once you are redirected back to SonarQube Cloud you will see a **Connected** badge displayed next to **Jira** along with information about when the connection was established and with options to **Reauthorize** and **delete** the connection.

{% hint style="info" %}
The administrator who connects a SonarQube organization to a Jira Cloud instance becomes the default reporter for all Jira work items created from this organization.
{% endhint %}

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-7e2b76ba94b6f611a684c34e9238c942d5484b51%2F5a2574f98aa40a171e683099b86f0be4d0afa38d.png?alt=media" alt="To complete the SonarQube -to- Jira connection, select Accept in the SonarQube Jira Authenticator window." width="563"><figcaption></figcaption></figure></div>

{% hint style="warning" %}
After the connection is established, all Jira operations, including project binding and Jira work item creation, utilize the Sonar organization admin token. This means that some Sonar users might see Jira projects and create Jira work items in projects where they lack permissions in Jira Cloud.
{% endhint %}

You can now bind your SonarQube projects with Jira Cloud projects. See [#binding-your-project-with-jira](#binding-your-project-with-jira "mention") for more information.

#### Reauthorizing the connection with Jira Cloud

Reauthorizing your organization is non-destructive, which means that connections to all projects and issues will remain intact.

{% hint style="info" %}
When reauthorizing, always ensure you select the same Jira Cloud instance on the Atlassian authorization page to avoid potential errors. See [#troubleshooting](#troubleshooting "mention") for more information.
{% endhint %}

In the unlikely event that your organization doesn’t use any features of the Jira Cloud integration for three months (for example, if there are no projects connected for a given organization), the connection to Jira will expire and will need to be reauthenticated by the organization’s administrator.

#### Deleting the connection with Jira Cloud

Deleting your organization’s connection with Jira removes all binding between SonarQube and Jira Cloud, as well as related data in SonarQube Cloud. To completely remove the connection, you must revoke relevant token permissions in the [Atlassian account](https://id.atlassian.com/manage-profile/apps).

By deleting the SonarQube to Jira Cloud connection, you will:

* Lose access to all Jira features in this SonarQube Cloud organization.
* Delete this organization’s project to Jira Cloud project connections.
* Disconnect all SonarQube issues from Jira work items.

{% hint style="warning" %}
You will not be able to restore this data after reconnecting the organization.
{% endhint %}

### Binding your project with Jira Cloud <a href="#binding-your-project-with-jira" id="binding-your-project-with-jira"></a>

After connecting your SonarQube organization with your Jira Cloud instance you are now ready to connect your SonarQube project with a Jira project.

To bind your SonarQube project with Jira Cloud at a project level, go to *Your Project* > **Administration** > **General Settings** > **Jira.** You can only bind one SonarQube project to one Jira project.

1. Click **Connect** to open the connection modal.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-2779f10aae555a75b5b42cac5f9919338d088ac2%2F441080e8bf3d9cb6cfdddb9145c6838248302dad.png?alt=media" alt="Your SonarQube Cloud project must be bound with Jira Cloud project. The Jira binding modal lets you choose which work types can be pushed from SonarQube to Jira." width="367"><figcaption></figcaption></figure></div>

2. In the modal, select a Jira project from a dropdown list. A maximum of 1,000 items is available. Use the search option to quickly find a specific project.
3. Choose the work types that you can push from SonarQube to Jira Cloud.
4. Click **Connect**. Your connection is now saved and you should see the confirmation on the page.

Once your binding between SonarQube project and Jira project is created you will see the connection details along with options to edit or delete the project binding.

#### Mandatory fields without a default value

The configuration might not support all of your Jira project’s mandatory fields. The following is a list of supported mandatory fields:

* Summary
* Description
* Reporter

Jira work types that have other mandatory fields associated with them, and have no default value, are not supported and are disabled in SonarQube. You can either remove these mandatory fields in Jira or choose a supported work type in SonarQube. At least one supported Jira work type is required to save the configuration.

#### Editing your project binding with Jira Cloud

By clicking on **Edit**, you can change the binding of your SonarQube project by connecting it with another Jira project. Editing the binding is non destructive, meaning that all SonarQube-to-Jira connections will remain intact. To completely reset your project, you must unbind the SonarQube project with Jira by clicking the delete button.

#### Unbinding your project from Jira Cloud

Deleting the project binding removes all of your connections and links in the Jira project. This is a complete reset between your SonarQube project and Jira.

### Jira Cloud release widget <a href="#jira-release-widget" id="jira-release-widget"></a>

Once you bind your SonarQube project with a Jira Cloud project, a Jira widget appears on the Main Branch Summary page.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-4bc972bc3590dd7bccfdbd573fbc35b2eca64b20%2F0f3fdb51504481482b062b119d0c0ebd2e4ce247.png?alt=media" alt="The Jira widget in SonarQube Cloud will show you how many open Jira issues you have."><figcaption></figcaption></figure></div>

If you operate with version-based releases in Jira Cloud, the widget will surface any open Jira work items you have associated with the earliest release.

The widget shows the following information:

* The number of open Jira work items for a given version, regardless of whether those items are associated with SonarQube issues or not. Click on the issue count to view them in Jira Cloud.
* Release date
* Release version

The widget retrieves only open Jira work items from the earliest unreleased Jira version. If two or more unreleased versions have the same date or have no assigned date, the widget will select the version with the lowest release ID, which is the release that was created first.

### Creating a Jira work item from a single SonarQube issue

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-abac562ae15cd5a588bd99d6989b87fa4e77714f%2Fd9d40bd3e5777ad2870bd764008c2d705babe58d.png?alt=media" alt="Creating a Jira work item from SonarQube Cloud is as simple as selecting Push to Jira, then choosing a work type."><figcaption></figcaption></figure></div>

You can create a Jira work item from a SonarQube issue or from the Issues page:

1. Click the **Push to Jira** button and choose a Jira work type, if more than two work types are available. The list of Jira work types depends on your Jira Cloud integration configuration and is configured by the project administrator.
2. When the process is complete the button displays a Jira work item ID along with the status label.
3. A new Jira work item will be created in your Jira Cloud project and it will open in a new tab.
4. Click on the Jira work item ID to open it on the Jira’s website.

{% hint style="info" %}
If you are not seeing the **Push to Jira** button after properly setting your Jira Cloud integration, it might be due to unsupported mandatory fields present on all of the Jira work types. Check this in project-level Jira configuration settings in SonarQube Cloud.
{% endhint %}

On rare occasions, two or more concurrent Jira creation events might be triggered by multiple users simultaneously, resulting in two or more Jira work items being created at the same time.

#### Contents of the Jira work item <a href="#contents-of-the-jira-work-item" id="contents-of-the-jira-work-item"></a>

When you create a Jira work item, it includes the following information:

* Title of the SonarQube issues .
* SonarQube issue link.
* Location of the issues.
  * File path.
  * Code lines.
  * Commit hash.
  * Date the issue was introduced.
* Information about why this is an issue and how to fix it with the rule name and link.
* Impact on software quality and severity.
* The reporter for the Jira work item is the default reporter set in SonarQube organization’s Jira Cloud integration.

### Disconnecting a Jira work item <a href="#disconnecting-jira-work-item" id="disconnecting-jira-work-item"></a>

You cannot delete a Jira work item from within SonarQube Cloud, but you can disconnect it by clicking on the close icon of the Jira button either within the SonarQube issue or on the Issues page. The connection with the Jira work item will be removed but the item will still exist in Jira Cloud.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e79d835b63f8e252f8152af81b60910792fa9248%2F0d21bfa8779909fb7b915056e8457de656d29220.png?alt=media" alt="When removing a connection to a Jira work item, select the X on right side of the Jira botton."><figcaption></figcaption></figure></div>

{% hint style="info" %}
You cannot push a SonarQube issue to an existing Jira work item, which means you can only create new Jira work items from SonarQube issues.
{% endhint %}

### Creating a Jira work item from multiple SonarQube issues

You can push multiple SonarQube issues into a single Jira work item from the project’s issues page in SonarQube.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-44ea5116c0a2fdb687c6aface56c89880e06398a%2FJira-create-many-to-single-work-item.png?alt=media" alt="View of creating a Jira work item from multiple SonarQube Cloud issues."><figcaption></figcaption></figure></div>

1. Select the issues you want to include in the Jira work item.
2. Click **Push to Jira** at the top of the issues page to open a modal.
3. In the modal, select the work type that you want to apply to the Jira work item.

SonarQube creates a Jira work item with issues that have not been previously connected to Jira. If you have selected issues that currently have a Jira connection and you want to include them in this Jira work item, you will have to disconnect them from Jira first. See [#disconnecting-jira-work-item](#disconnecting-jira-work-item "mention") for more information.

{% hint style="info" %}
A maximum of 500 SonarQube issues can be included in a Jira work item.
{% endhint %}

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

The following are the typical errors that might prompt you to troubleshoot the connection with Jira:

* The administrator who set up the connection has left the company and the Atlassian token has been removed.\
  **Solution**: The new administrator has to reauthorize the Jira connection at the organizational level. See [#reauthorizing-the-connection-with-jira-cloud](#reauthorizing-the-connection-with-jira-cloud "mention") for more information.
* The connection has been reauthorized with a wrong Jira instance.\
  **Solution**: Make sure to select the correct Jira instance on the Atlassian authorization page when reauthorizing the Jira connection at the organization level. SonarQube remembers previous issue-to-Jira work item connections on the project levels, but the organization has to be reauthorized to the original Jira instance for these connections to be available again. See [#reauthorizing-the-connection-with-jira-cloud](#reauthorizing-the-connection-with-jira-cloud "mention") for more information.
* Some Jira work types cannot be selected on the project settings page for Jira.\
  **Solution**: Jira work types that have other mandatory fields associated with them are not supported and are disabled in SonarQube. You can either remove these mandatory fields in Jira or choose a supported work type in SonarQube.

Other issues:

* The **Push to Jira** button is not visible on the SonarQube issue page.\
  **Solution**: After connecting your organization to a Jira instance you need to bind individual SonarQube projects to Jira projects. See [#binding-your-project-with-jira](#binding-your-project-with-jira "mention") for more information.
* The Jira release widget does not show any insights, even though your team is operating under a version-based release cycle.\
  **Solution:** Ensure you have releases and versions enabled in your Jira project. See more on [Atlassian’s webpage](https://support.atlassian.com/jira-software-cloud/docs/enable-releases-and-versions/).

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions "mention")
* [organization-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions "mention")
