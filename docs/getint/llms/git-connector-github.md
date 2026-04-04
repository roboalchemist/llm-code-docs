# Source: https://docs.getint.io/guides/integration-synchronization/git-integrations/git-connector-github.md

# Git Connector - GitHub

Effortlessly sync your GitHub repositories with Jira using our in-depth guide. This comprehensive resource helps your team track changes, manage issues, and collaborate effectively.

We guide you through every step, from setting up the integration to configuring OAuth credentials and ensuring smooth data synchronization. As of now, we support syncing repositories, branches, commits, and pull requests. Discover how to link your GitHub repositories to Jira projects, enabling you to monitor branches, commits, and pull requests directly within Jira. This guide will show you how to combine the strengths of GitHub and Jira to optimize your workflow, boost visibility, and enhance productivity.

Access our Git integration app for Jira through this link: [Git Connector.](https://marketplace.atlassian.com/apps/1236406/git-connector-for-jira-azure-devops-github-gitlab?hosting=cloud\&tab=overview)

{% hint style="warning" %}
The Git Connector app is not required if you're using the GitHub integration app.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6TmPdBT0Gk3Tg0aM9rT8%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=29bc1de5-0133-41a6-bdaa-08db20302cf5" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a><br></p></figcaption></figure>

### How to Build a Git Integration for GitHub <a href="#how-to-build-a-git-integration-for-github" id="how-to-build-a-git-integration-for-github"></a>

#### 1. Launch the Getint App: <a href="#id-1.-launch-the-getint-app" id="id-1.-launch-the-getint-app"></a>

* Go to **Apps**, open the Git Connector for Jira app, navigate to **Integrations**, click **Create Integration**, and choose **Sync GIT Repository**.
* If you’re using Getint On-Premise, simply open the app, click **Create Integration**, and choose **Sync GIT Repository**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7kXR3sPFRHv0EgaEYbFX%2FGIT%20REPOSITORY%20OPTION.png?alt=media&#x26;token=369c2764-ffd7-4f43-9971-6727fdf110c4" alt=""><figcaption></figcaption></figure>

#### 2. Create a Connection with GitHub: <a href="#id-2.-create-a-connection-with-github" id="id-2.-create-a-connection-with-github"></a>

* Click the **Connect App** button, and select **GitHub**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FHTrUIwMDRpI3WLm5gk2R%2FSelecting%20GitHub%20for%20Git%20integration.png?alt=media&#x26;token=3afeefe7-6e22-40c4-aa68-2db5f10e77a1" alt=""><figcaption></figcaption></figure>

* Create a connection or select an existing one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FS6EWuoFdc9CENGKzDf4P%2FCreate%20New%20Connection%20or%20Select%20an%20existing%20connection.png?alt=media&#x26;token=5cccedb7-3891-4806-8b9b-185c5e50891b" alt=""><figcaption></figcaption></figure>

* Tap on **Create a new connection** if you don’t have an existing one.
* Name the connection, and paste the token generated (create the personal access token following the instructions in this guide: [Connections](https://docs.getint.io/guides/quickstart/connection#github)). Then click **Add**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtJqoAGaaUb7fTUsXYKnS%2FConnection%20to%20GitHub.png?alt=media&#x26;token=def5f2fc-f23d-484e-a3dc-8ad13dd71dd2" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

#### 3. Establish a Connection with Jira: <a href="#id-3.-establish-a-connection-with-jira" id="id-3.-establish-a-connection-with-jira"></a>

* Ensure that you are logged in with administrative rights, then click on **Connect App** and select **Jira**. Click on **Create New** to set up a new connection with your Jira instance and enter the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9jAABZyaQOrnhZdKPvg2%2FAdd%20the%20URL%20of%20your%20Jira%20instance.png?alt=media&#x26;token=331b1ea3-145b-4d6e-b91f-20e1d86aacb6" alt=""><figcaption></figcaption></figure>

* Unlike **Continuous Syncs** or **Migrations**, GIT integrations require users to set up OAuth in your Jira instance. Please ensure you have admin permissions; otherwise, you will not be able to set up the OAuth credentials. Then, follow our guide to configure a Jira OAuth at the following: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
* Enter the necessary details to establish the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6qeU2BobwaYJooJftR99%2FCreating%20a%20connection%20with%20Jira%20for%20a%20GIT%20integration.png?alt=media&#x26;token=98df4b79-20f0-48b0-b71f-2b636c5cda53" alt=""><figcaption></figcaption></figure>

* After entering your details, your new connection will appear in the dropdown list of available connections. Please select it and click **Connect** to finalize the setup.

#### 4. Building Your Integration: <a href="#id-4.-building-your-integration" id="id-4.-building-your-integration"></a>

* By default, the Git repositories will automatically synchronize with all projects in your Jira instance. However, if you disable this option, you can specify one or multiple projects where this information should be available.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTsST25NjptxPg2mGdJ4i%2FGitHub%20git%20repository%20integration.png?alt=media&#x26;token=4082aa1b-436a-4d92-91cc-55b65b28b39c" alt=""><figcaption></figcaption></figure>

* For example, you can pick particular projects based on your company's needs. Next, identify the Git repositories you want to sync. Finally, name your integration and click **Create** in the top right corner of the screen to save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSBTdluLaUsYkvGnRTquo%2FGitHub%20connector.png?alt=media&#x26;token=48d29b71-2daa-4bd8-afa6-5952b89cc345" alt=""><figcaption></figcaption></figure>

* After creating your integration, it will be readily available in the Integrations section within Workflows, identified by a code icon.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFJgdgT9pakrhoAsbjczB%2FCHecking%20the%20github%20integration.png?alt=media&#x26;token=6c12bbff-c115-4b3f-9f98-d7f6e83b4fb1" alt=""><figcaption></figcaption></figure>

* If you did not install the Git Connector app as instructed at the beginning of the article, you will encounter an error like the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8rWKCs35Bk6GLAN5o008%2FSync%20error%20due%20to%20missing%20Git%20connector.png?alt=media&#x26;token=acd8eae6-45b3-4a12-b8ba-269e314c314f" alt=""><figcaption></figcaption></figure>

#### 5. Test the Integration and Sync Your Branches <a href="#id-5.-test-the-integration-and-sync-your-branches" id="id-5.-test-the-integration-and-sync-your-branches"></a>

* To start syncing items, use the Jira task ID as a prefix for the branch, commit, and pull request names. For branch names, only underscores or dashes can be used instead of spaces. For example **ED-34**\_**New\_branch**.
* For instance, if you are syncing an item with the Jira ID **ED-34**, your branch should be named **ED-34** followed by the branch name, as shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F8QR8BFVIt2DOGvl3MGcl%2FCreating%20a%20branch%20in%20GitHub.png?alt=media&#x26;token=5c9fe8d0-614d-4f24-9eac-9900b3355127" alt=""><figcaption></figcaption></figure>

* If you fail to use the correct naming prefix for branches and commits, you will encounter an error similar to the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGGSQ6NbcFDxwFj9639Nj%2FGit%20sync%20error.png?alt=media&#x26;token=383290ba-70a0-4968-aaf7-e1d7d438d649" alt=""><figcaption></figcaption></figure>

* The Git repository details of your Jira items will be available in the Development field. Refresh the page if you don’t see any changes to the Development field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Foe9mmberMQWAoMD7fL9T%2FDevelopment%20field%20for%20GitHub%20integration.png?alt=media&#x26;token=cea5c9f5-cd85-42ba-b0be-8d3a60dee929" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Depending on your Project template, the Development field may not be visible. In such cases, you must either add the field by modifying the issue layout or switch to a different template.
{% endhint %}

* Clicking on this field allows you to effortlessly access all the information being fetched from the repositories.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEjdZmK9zUjJWnS2Z4YS6%2FInside%20the%20development%20field%20-%20Github.png?alt=media&#x26;token=119fb1e6-7ed9-4bda-8362-aa102f553b55" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Getint enables the synchronization of Repositories, Branches, Commits, and Pull Requests. However, please note that changes cannot be submitted from Jira to the Git repository. The synchronization of repository information is one-way from GitHub.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

With this comprehensive guide at your disposal, you can seamlessly integrate GitHub repositories with Jira and unlock the full potential of efficient repository management. If you need any help or have any questions along the way, don't hesitate to reach out to us here.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
