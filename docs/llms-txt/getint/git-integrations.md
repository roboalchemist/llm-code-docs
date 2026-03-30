# Source: https://docs.getint.io/guides/integration-synchronization/git-integrations.md

# Git Repository integration

With the integration of Git, repository management becomes highly practical and efficient. We currently support integration with Azure DevOps, GitLab, and GitHub. Whether you're merging branches, tracking changes, or rolling back to previous versions, you can track all these changes seamlessly within your Jira instance. This integration allows you to easily track **repositories**, **branches**, **commits**, and **pull requests**.

Our Git integration app for Jira is available at the following link: [Git Connector for Jira.](https://marketplace.atlassian.com/apps/1236406/git-connector-for-jira-azure-devops-github-gitlab?hosting=cloud\&tab=overview)

{% hint style="warning" %}
While it is possible to create a Git integration using other integration apps, it is mandatory to have the Git Connector app installed.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F16CHi6P2piPZwusJr8af%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=703e3f94-c326-4b4e-a684-baaf294c1bdd" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

### How to Build a Git Integration <a href="#how-to-build-a-git-integration" id="how-to-build-a-git-integration"></a>

#### 1. Launch the Getint App: <a href="#id-1.-launch-the-getint-app" id="id-1.-launch-the-getint-app"></a>

* Navigate to **Apps**, launch the app **Git Connector for Jira**, go to **Integrations**, click **Create Integration**, and select **Sync GIT Repository**.
* If you’re using Getint On-Premise, simply launch the app, click **Create Integration**, and select **GIT**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDC3rn331vJYbArTMksN6%2FGIT%20REPOSITORY%20OPTION.png?alt=media&#x26;token=13e3f588-1880-4da0-acec-034f2b42cd4e" alt=""><figcaption></figcaption></figure>

#### 2. Create a Connection for the App Containing the Git Repository: <a href="#id-2.-create-a-connection-for-the-app-containing-the-git-repository" id="id-2.-create-a-connection-for-the-app-containing-the-git-repository"></a>

* Select the app you want to integrate by clicking the **Connect App** button.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fcaqysp7JfGO8CwRb4jR5%2FSelect%20the%20app%20you%20want%20to%20integrate.png?alt=media&#x26;token=6cba9594-f34d-4031-8cd7-ce2f11718fc8" alt=""><figcaption></figcaption></figure>

* Create a connection or select an existing one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTzsC9ZxCUT8GR19kP8k6%2FCreate%20New%20Connection%20or%20Select%20an%20existing%20connection.png?alt=media&#x26;token=b4a3c649-eaff-4a73-a002-57f1db94a9aa" alt=""><figcaption></figcaption></figure>

* Follow the next steps depending on the app you selected. We’re taking GitLab as an example, but the process is the same for the rest of the connectors.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FyPsJDKMX12njsLT91lf5%2FNaming%20your%20connection%20and%20adding%20access%20token.png?alt=media&#x26;token=4b7b51ec-a0f1-4e54-b0ce-7f2f03717c28" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

{% hint style="info" %}
For detailed instructions on creating a connection and generating an access token, please refer to our comprehensive guide: [Connections | Tokens and Requirements](https://docs.getint.io/guides/quickstart/connection).
{% endhint %}

#### 3. Establish a Connection with Jira: <a href="#id-3.-establish-a-connection-with-jira" id="id-3.-establish-a-connection-with-jira"></a>

* Make sure you are logged in with admin rights, then click on **Connect App** and select **Jira**. Choose **Create New** to establish a fresh connection with your Jira instance and enter the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FViEmoRAVjRwNaM4c9uxV%2FAdd%20the%20URL%20of%20your%20Jira%20instance.png?alt=media&#x26;token=0c2fb255-2c54-4bcd-8d17-388e502d99a7" alt=""><figcaption></figcaption></figure>

* Unlike **Continuous Syncs** or **Migrations**, GIT integrations require users to set up OAuth in their Jira instance. Please ensure you have admin permissions; otherwise, you will not be able to set up the OAuth credentials. Then, follow our guide to configure a Jira OAuth at the following: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
* Enter the necessary details to establish the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fk4fwjhgAACAHG2j3KhyJ%2FCreating%20a%20connection%20with%20Jira%20for%20a%20GIT%20integration.png?alt=media&#x26;token=dfaf9b91-4170-429a-884e-4c775a27eb4d" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

#### 4. Building Your Integration: <a href="#id-4.-building-your-integration" id="id-4.-building-your-integration"></a>

* By default, the Git repositories will sync with all projects in your Jira instance. However, unchecking this option allows you to select one or multiple projects where you want this information to be available.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fcrp2zQWC4JhlGxHx7hxV%2Fjira%20git%20connector.png?alt=media&#x26;token=799b7b94-e002-445b-a5ae-9f14b3c64337" alt=""><figcaption></figcaption></figure>

* For example, you can select specific projects based on your company’s needs. Next, choose the Git repositories you want to sync. Finally, name your integration and click **Create** at the top right corner of the screen to save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeD7VNdkrMmWb2cjsz95N%2FSelect%20the%20Git%20Repositories%20and%20Jira%20projects.png?alt=media&#x26;token=59923863-c07b-46f3-992a-db2efa062421" alt=""><figcaption></figcaption></figure>

* Once you've created your integration, it will be easily accessible in the **Integrations** section within Workflows, and it is marked with a code icon.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fy05P9ZUj2IfTsCL4Expx%2FGit%20Repositories.png?alt=media&#x26;token=3144ac2c-3963-4289-afd6-376280050299" alt=""><figcaption></figcaption></figure>

* If you did not install the Git Connector app as instructed at the beginning of the article, you will encounter an error like the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fl14thAOIsUVU9ucwK4Nr%2FSync%20error%20due%20to%20missing%20Git%20connector.png?alt=media&#x26;token=9d566c5c-567a-4c1e-8ed7-a06deb5c98f5" alt=""><figcaption></figcaption></figure>

#### 5. Test the Integration and Sync Your Branches <a href="#id-5.-test-the-integration-and-sync-your-branches" id="id-5.-test-the-integration-and-sync-your-branches"></a>

* To start syncing branches, ensure that you use the ID of the Jira task as a prefix for the branch names. For branch names, only underscores or dashes can be used instead of spaces. For example **ED-23-resolve-support-ticket-9843-migrate**.
* For example, if you’re syncing an item with the Jira ID **ED-23**, your branch should be named **ED-23 + branch name**, as shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXVyMeraVnPrUOLQ8FcYd%2Fnaming%20new%20branches.png?alt=media&#x26;token=c61d5086-b52d-4c5d-acf9-2464e3e97350" alt=""><figcaption><p>Example of proper branch naming for synchronization. Using GitHub as an example, the same principle applies to the other connectors.</p></figcaption></figure>

* If the correct naming prefix is not used to sync your items, an error like the one below will occur:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdRqi0bfxOuT4KJikt6vN%2FGit%20sync%20error.png?alt=media&#x26;token=4a8ffa76-97c9-4ad0-9a55-724924060cb0" alt=""><figcaption></figcaption></figure>

* The Git repository details of your Jira items will be available in the Development field. Refresh the page if you don’t see any changes to the Development field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FyZjqactZD1plsWifSHPp%2FChecking%20how%20changes%20are%20being%20integrated%20to%20Jira.png?alt=media&#x26;token=30df93ba-ee71-467f-baa5-12a8dc792489" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Depending on your Project template, the Development field may not be visible. In such cases, you must either add the field by modifying the issue layout or switch to a different template.
{% endhint %}

* By clicking on this field, you can easily access all the information that is being collected from the repositories.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fgx4778nNEoaJzUXAViCm%2FDevelopment%20field%20for%20git%20integration.png?alt=media&#x26;token=ce1a88c4-ecd4-4055-8f28-61eec798f166" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Getint enables the synchronization of Repositories, Branches, Commits, and Pull Requests. However, please note that changes cannot be submitted from Jira to the Git repository. The synchronization of repository information is one-way from the Git connector.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

With this comprehensive guide, you can seamlessly integrate Git with Jira and take full advantage of efficient repository management. If you require any assistance or have further questions, don't hesitate to contact us [here](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
