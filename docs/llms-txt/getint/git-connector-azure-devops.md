# Source: https://docs.getint.io/guides/integration-synchronization/git-integrations/git-connector-azure-devops.md

# Git Connector - Azure DevOps

With the integration of Git, repository management becomes highly practical and efficient. We currently support integration with Azure DevOps. Whether you're merging branches, tracking changes, or rolling back to previous versions, you can track all these changes seamlessly within your Jira instance. This integration lets you easily track **repositories**, **branches**, **commits**, and **pull requests**.

Our Git integration app for Jira is available at the following link: [Git Connector for Jira.](https://marketplace.atlassian.com/apps/1236406/git-connector-for-jira-azure-devops-github-gitlab?hosting=cloud\&tab=overview)

{% hint style="warning" %}
While it is possible to create a Git integration using the Azure DevOps integration app, it is mandatory to have the Git Connector app installed.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3wmXPrAwlaQk7K4jQcMo%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=412364ac-394b-4c84-bf60-e26925e07dcb" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

### How to Build a Git Integration for Azure DevOps <a href="#how-to-build-a-git-integration-for-azure-devops" id="how-to-build-a-git-integration-for-azure-devops"></a>

#### 1. Launch the Getint App: <a href="#id-1.-launch-the-getint-app" id="id-1.-launch-the-getint-app"></a>

* Navigate to **Apps**, launch the app **Git Connector for Jira**, go to **Integrations**, click **Create Integration**, and select **Sync GIT Repository**.
* If you’re using Getint On-Premise, simply launch the app, click **Create Integration**, and select **GIT**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLz79THZQV0fEbkSnlZUx%2FGIT%20REPOSITORY%20OPTION.png?alt=media&#x26;token=920487b3-4c18-45be-9a0d-2b9126678b13" alt=""><figcaption></figcaption></figure>

#### 2. Create a Connection with Azure DevOps: <a href="#id-2.-create-a-connection-with-azure-devops" id="id-2.-create-a-connection-with-azure-devops"></a>

* Click the **Connect App** button, and select **Azure DevOps**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ft6NEa2kCl4SoaSucmULK%2FSelect%20the%20app%20you%20want%20to%20integrate%20-%20DevOps.png?alt=media&#x26;token=6f03f2ad-f0da-4990-806a-5da260cd7f96" alt=""><figcaption></figcaption></figure>

* Create a connection or select an existing one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIMzxE2qfiB0LUgEZA2Ye%2FCreate%20New%20Connection%20or%20Select%20an%20existing%20connection.png?alt=media&#x26;token=ea5be1c6-94ae-4ea0-9de6-1721d3c33d05" alt=""><figcaption></figcaption></figure>

* Tap on **Create a new connection** if you don’t have an existing one.
* Enter your instance URL, and click on **Connect**.
* Name the connection, input your email, and paste the token generated (create the personal access token following the instructions in this guide: [Connections](https://docs.getint.io/guides/quickstart/connection#azure-devops)). Then click **Add**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGNsemYijaZscjjUX16Tv%2FCreating%20a%20connection%20with%20Azure%20DevOps.png?alt=media&#x26;token=c0296d9d-13b4-4014-9585-357c166f981d" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

{% hint style="warning" %}
For Git Azure DevOps integrations, it is important to set the scope **Code** to **Read**. Otherwise, you’ll get the following error:

*Unfortunately, your integration failed to save due to the following reason: Forbidden.*
{% endhint %}

#### 3. Establish a Connection with Jira: <a href="#id-3.-establish-a-connection-with-jira" id="id-3.-establish-a-connection-with-jira"></a>

* Ensure that you are logged in with administrative rights, then click on **Connect App** and select **Jira**. Click on **Create New** to set up a new connection with your Jira instance and enter the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqvVDf27e4wRmzgdIy6BL%2FAdd%20the%20URL%20of%20your%20Jira%20instance.png?alt=media&#x26;token=80cc6191-f359-4979-bec6-d9621aa00a8c" alt=""><figcaption></figcaption></figure>

* Unlike **Continuous Syncs** or **Migrations**, GIT integrations require users to set up OAuth in your Jira instance. Please ensure you have admin permissions; otherwise, you will not be able to set up the OAuth credentials. Then, follow our guide to configure a Jira OAuth at the following: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
* Enter the necessary details to establish the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9E20Mude7KWSaIM0KOvu%2FCreating%20a%20connection%20with%20Jira%20for%20a%20GIT%20integration.png?alt=media&#x26;token=3ec045f0-eb62-4e83-983d-45f576901960" alt=""><figcaption></figcaption></figure>

* After entering your details, your new connection will appear in the dropdown list of available connections. Please select it and click **Connect** to finalize the setup.

#### 4. Building Your Integration: <a href="#id-4.-building-your-integration" id="id-4.-building-your-integration"></a>

* By default, the Git repositories will synchronize with all projects in your Jira instance. However, if you uncheck this option, you can choose one or multiple projects where you want this information to be accessible.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FitkgLgg1BZkgx1qB4iiv%2FGit%20integration%20-%20Azure%20DevOps.png?alt=media&#x26;token=7c718d82-e968-4a2e-b018-79c9e429c2b3" alt=""><figcaption></figcaption></figure>

* For instance, you can choose specific projects according to your company's requirements. Then, select the Git repositories you wish to synchronize. Lastly, give your integration a name and click **Create** at the top right corner of the screen to save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpWQXyuvuywJdPvLD5nQP%2FAzure%20DevOps%20Git%20integration.png?alt=media&#x26;token=5dba6db7-432d-4709-8347-e547fe4f1602" alt=""><figcaption></figcaption></figure>

* After creating your integration, it will be readily available in the Integrations section within Workflows, identified by a code icon.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOMdLDE1ZYF6xe8PjFGEw%2FChecking%20Azure%20DevOps%20integration%20from%20Workflows%20section.png?alt=media&#x26;token=4836d789-5481-4155-97ef-863b38ce8b40" alt=""><figcaption></figcaption></figure>

* If you did not install the Git Connector app as instructed at the beginning of the article, you will encounter an error like the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6Pg0OECp7YyPZQOVys6W%2FSync%20error%20due%20to%20missing%20Git%20connector.png?alt=media&#x26;token=41050743-9eae-4562-ac5d-684c63216261" alt=""><figcaption></figcaption></figure>

#### 5. Test the Integration and Sync Your Branches <a href="#id-5.-test-the-integration-and-sync-your-branches" id="id-5.-test-the-integration-and-sync-your-branches"></a>

* To start syncing branches, use the Jira task ID as a prefix for the branch, commit, and pull request names. For branch names, only underscores or dashes can be used instead of spaces. For example **ED-32\_Energy\_Dot**.
* For instance, if you are syncing an item with the Jira ID **ED-32**, your branch should be named **ED-32** followed by the branch name, as shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0dJWjqdDvgQu0Vx2gewY%2FAzure%20DevOps%20-%20Creating%20branches.png?alt=media&#x26;token=9e740c87-8ada-46ae-954c-e3499117f7d1" alt=""><figcaption><p>Example of proper branch naming for synchronization.</p></figcaption></figure>

* If you fail to use the correct naming prefix to sync your items, you will encounter an error similar to the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FziOt6DvRWjjyeQCvpDxE%2FGit%20sync%20error.png?alt=media&#x26;token=79304c6b-eece-4851-8d78-867bdbdcb569" alt=""><figcaption></figcaption></figure>

* The Git repository details of your Jira items will be available in the Development field. Refresh the page if you don’t see any changes to the Development field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIpjysDbkpfwNfGR9UliW%2FDevelopment%20field%20for%20Azure%20DevOps%20Git%20integration.png?alt=media&#x26;token=676e44c7-b9c8-4318-9a6a-f0de6acc61f0" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Depending on your Project template, the Development field may not be visible. In such cases, you must either add the field by modifying the issue layout or switch to a different template.
{% endhint %}

* Clicking on this field allows you to effortlessly access all the information being fetched from the repositories.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0TOuFjFYbBoICqOmZiRi%2FInside%20the%20Development%20field.png?alt=media&#x26;token=ebe8c9fe-baf3-4968-8dba-80b39fecf907" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Getint enables the synchronization of Repositories, Branches, Commits, and Pull Requests. However, please note that changes cannot be submitted from Jira to the Git repository. The synchronization of repository information is one-way from Azure DevOps.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

By following this detailed guide, you can effortlessly integrate Azure DevOps repositories with Jira and fully leverage efficient repository management. Should you need any assistance or have additional questions, please feel free to contact us here.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
