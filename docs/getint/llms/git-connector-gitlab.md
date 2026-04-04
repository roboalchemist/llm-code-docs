# Source: https://docs.getint.io/guides/integration-synchronization/git-integrations/git-connector-gitlab.md

# Git Connector - GitLab

This article provides a comprehensive guide on how to sync GitLab repositories with Jira, allowing teams to track changes, manage issues, and collaborate more effectively.

We cover everything from setting up the integration to configuring OAuth credentials and ensuring smooth data synchronization. Learn how to link your GitLab repositories to Jira projects, enabling you to monitor branches, commits, and pull requests directly within Jira. By following this guide, you can leverage the combined power of GitLab and Jira to streamline your workflow, enhance visibility, and improve productivity.

You can access our Git integration app for Jira using the following link: [Git Connector.](https://marketplace.atlassian.com/apps/1236406/git-connector-for-jira-azure-devops-github-gitlab?hosting=cloud\&tab=overview)

{% hint style="warning" %}
The Git Connector app is not required if you're using the GitLab integration app.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjLPlqGF8Q02otsQFuMdd%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=f4dc12ae-55ac-4d9d-82dd-f1acdd231e01" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a><br></p></figcaption></figure>

### How to Build a Git Integration for GitLab <a href="#how-to-build-a-git-integration-for-gitlab" id="how-to-build-a-git-integration-for-gitlab"></a>

#### 1. Launch the Getint App: <a href="#id-1.-launch-the-getint-app" id="id-1.-launch-the-getint-app"></a>

* Go to **Apps**, open the Git Connector for Jira app, navigate to **Integrations**, click **Create Integration**, and choose **GIT**.
* If you’re using Getint On-Premise, simply open the app, click **Create Integration**, and choose **Sync GIT Repository**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FIMX1Zagem19zcQcdmnmI%2FGIT%20REPOSITORY%20OPTION.png?alt=media&#x26;token=59787ee9-ad10-479e-beee-43c8ed77f008" alt=""><figcaption></figcaption></figure>

#### 2. Create a Connection with GitLab: <a href="#id-2.-create-a-connection-with-gitlab" id="id-2.-create-a-connection-with-gitlab"></a>

* Click the **Connect App** button, and select **GitLab**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPx1OLCtYbT1beMx2rZuU%2FSelecting%20GitLab%20for%20Git%20Integration.png?alt=media&#x26;token=fee233b9-5040-48b8-bad7-c52d0260cb40" alt=""><figcaption></figcaption></figure>

* Create a connection or select an existing one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fq5ko2hye5X091CfboWub%2FCreate%20New%20Connection%20or%20Select%20an%20existing%20connection.png?alt=media&#x26;token=1c0c2cdb-dbbb-46c6-84e5-4ea58876166a" alt=""><figcaption></figcaption></figure>

* Tap on **Create a new connection** if you don’t have an existing one.
* Enter your instance URL, and click on **Connect**. Do NOT provide a URL if you are using GitLab Cloud.
* Name the connection, and paste the token generated (create the personal access token following the instructions in this guide: [Connections](https://docs.getint.io/guides/quickstart/connection#gitlab)). Then click **Add**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpiXSYswfv2pfzLgiCvNL%2FNaming%20your%20connection%20and%20adding%20access%20token.png?alt=media&#x26;token=6c023c8d-f767-4b23-a6a2-a11a99f1be8b" alt=""><figcaption></figcaption></figure>

* Once you've added your details, you'll find your new connection in the dropdown list of available connections. Please select it and click **Connect** to complete the process.

#### 3. Establish a Connection with Jira: <a href="#id-3.-establish-a-connection-with-jira" id="id-3.-establish-a-connection-with-jira"></a>

* Ensure that you are logged in with administrative rights, then click on **Connect App** and select **Jira**. Click on **Create New** to set up a new connection with your Jira instance and enter the URL of your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F95QXAP4ctPtxiVWVk9dU%2FAdd%20the%20URL%20of%20your%20Jira%20instance.png?alt=media&#x26;token=020e7e6b-d584-498c-bda9-f8a2031d36fa" alt=""><figcaption></figcaption></figure>

* Unlike **Continuous Syncs** or **Migrations**, GIT integrations require users to set up OAuth in your Jira instance. Please ensure you have admin permissions; otherwise, you will not be able to set up the OAuth credentials. Then, follow our guide to configure a Jira OAuth at the following: [Connection | Jira OAuth.](https://docs.getint.io/guides/quickstart/connection#jira-cloud-oauth)
* Enter the necessary details to establish the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4obVTbpw36olFtf5ymeF%2FCreating%20a%20connection%20with%20Jira%20for%20a%20GIT%20integration.png?alt=media&#x26;token=aaff0167-0bb8-4c58-a7d7-a8a29124b5a0" alt=""><figcaption></figcaption></figure>

* After entering your details, your new connection will appear in the dropdown list of available connections. Please select it and click **Connect** to finalize the setup.

#### 4. Building Your Integration: <a href="#id-4.-building-your-integration" id="id-4.-building-your-integration"></a>

* By default, the Git repositories will automatically synchronize with all projects in your Jira instance. However, if you disable this option, you can specify one or multiple projects where this information should be available.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FCJ4eMp5NuhwJXHvj0IVS%2FGitlab%20git%20repository%20integration.png?alt=media&#x26;token=e12c1e7d-41de-42c9-aaaa-85f0c785b328" alt=""><figcaption></figcaption></figure>

* For example, you can pick particular projects based on your company's needs. Next, identify the Git repositories you want to sync. Finally, name your integration and click **Create** in the top right corner of the screen to save it.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FN2yEQWPz3n1o7TrMcsgH%2FSelecting%20different%20Jira%20Projects%20for%20Git%20Integration.png?alt=media&#x26;token=f37bc00a-2190-453e-936b-bf9b047f1cc9" alt=""><figcaption></figcaption></figure>

* After creating your integration, it will be readily available in the Integrations section within Workflows, identified by a code icon.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrcGeRf1yMfNmFtEOZXr6%2FWhere%20to%20find%20the%20GIT%20integrations.png?alt=media&#x26;token=4363123a-ed21-4f57-8563-300fe9d18aff" alt=""><figcaption></figcaption></figure>

* If you did not install the Git Connector app as instructed at the beginning of the article, you will encounter an error like the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FFlVRS1y9icaE4XL8wRYb%2FSync%20error%20due%20to%20missing%20Git%20connector.png?alt=media&#x26;token=7054f8bd-cd0e-4b86-b29b-efbeab5c2ee3" alt=""><figcaption></figcaption></figure>

#### 5. Test the Integration and Sync Your Branches <a href="#id-5.-test-the-integration-and-sync-your-branches" id="id-5.-test-the-integration-and-sync-your-branches"></a>

* To start syncing branches, use the Jira task ID as a prefix for the branch, commit, and pull request names. For branch names, only underscores or dashes can be used instead of spaces. For example **ED-33**\_**feature\_user\_authentication**.
* For instance, if you are syncing an item with the Jira ID **ED-33**, your branch should be named **ED-33** followed by the branch name, as shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FU2ZOqlZ52EPEwhYQpXqG%2FGitLab%20repository%20integration.png?alt=media&#x26;token=0882d758-0e87-4652-8941-16bc791e2b09" alt=""><figcaption></figcaption></figure>

* If you fail to use the correct naming prefix for branches and commits, you will encounter an error similar to the one shown below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3IKnhL7xiBYLFci3xbkk%2FGit%20sync%20error.png?alt=media&#x26;token=a3e94d63-4c74-4a8f-ab12-a4de3d7c82fb" alt=""><figcaption></figcaption></figure>

* The GitLab repository details of your Jira items will be available in the Development field. Refresh the page if you don’t see any changes to this field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDXqZ6SM0Ns1pkmHVCOEn%2FDevelopment%20field%20for%20gitlab%20integration.png?alt=media&#x26;token=4b6b3cad-7381-4911-97f6-2c90985823d8" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Depending on your Project template, the Development field may not be visible. In such cases, you must either add the field by modifying the issue layout or switch to a different template.
{% endhint %}

* Clicking on this field allows you to effortlessly access all the information fetched from the GitLab Repository.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FrFzEFQjm9HpdfdWMl7A7%2FInside%20the%20Development%20field%20in%20Jira.png?alt=media&#x26;token=335edbdd-8243-42ab-aa4a-688c62d958c1" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Getint enables the synchronization of Repositories, Branches, Commits, and Pull Requests. However, please note that changes cannot be submitted from Jira to the Git repository. The synchronization of repository information is one-way from GitLab.
{% endhint %}

### Conclusion <a href="#conclusion" id="conclusion"></a>

With this comprehensive guide at your disposal, you can seamlessly integrate GitLab repositories with Jira and unlock the full potential of efficient repository management. If you need any help or have any questions along the way, don't hesitate to reach out to us here.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
