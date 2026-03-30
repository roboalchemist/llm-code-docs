# Source: https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration/how-to-setup-a-connection-with-azure-devops-on-premise.md

# How to Setup a Connection with Azure DevOps On-Premise

Connecting your On-Premise infrastructure with Azure can significantly enhance your organization’s capabilities by leveraging cloud resources while maintaining control over your local environment. With this detailed article, you can establish a connection between your Azure DevOps On-Premise infrastructure and any of our supported tools.

### Requirements and Recommendations <a href="#requirements-and-recommendations" id="requirements-and-recommendations"></a>

Before you begin, ensure you have the following:

* Administrative access to your Azure on-premise environment and the other app you’re integrating.
* Necessary permissions to create and manage projects, types, and fields within the applications.
* Service accounts with the required privileges for integration. It is not recommended to use personal accounts to build your integration. Additionally, it is important to note that comments are added as the user you chose to create the connection. The original author will still appear in the comment footer, but it will be attributed to the user who established the connection.

### Establishing the Connection <a href="#establishing-the-connection" id="establishing-the-connection"></a>

1. Launch Getint and look for the **Azure DevOps** in the apps selection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdbIaiz12h2aQFXNje2hM%2FSelecting%20Azure%20DevOps%20as%20the%20tool%20for%20connection.png?alt=media&#x26;token=fcdadf81-4c24-4ea0-bd3b-9c376658d420" alt=""><figcaption></figcaption></figure>

1. Click **Create New Connection.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FRzRUDblWqVgV4R0Vc6Mz%2FCreate%20connection.png?alt=media&#x26;token=48c76d46-65ae-49d4-98d4-df4d4cf1457b" alt=""><figcaption></figcaption></figure>

1. Add the **URL** of your server/deployment. Please ensure you use only the main **URL** without any additional information, such as project destinations, and so on.
   * These are examples of how URLs should be entered:
     * `https://mytfs.internal.com`
     * `http://1.32.312.32`
     * `https://devops.local:8080/tfs`
     * `http://10.0.0.1:8080/tfs`
   * Please avoid entering URLs this way:
     * `https://devops.local:8080/tfs/Collection/Project`
     * `http://10.0.0.1:8080/tfs/tfs/DefaultCollection/Project`
     * `http://1.32.312.32/DefaultCollection/Project`
     * `https://mytfs.internal.com/SomeCollection/`

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtNsL51yURFldS9jCyTOR%2FURL%20for%20connection.png?alt=media&#x26;token=ee6a2941-4fbb-4d9d-9112-445fba3dde17" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
If the URLs are not entered correctly, the tool will display an error message, and the connection will not be established.
{% endhint %}

1. Enter the connection details such as the **Connection Name, Collection Name, Username, Password / Personal Access Token**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FccqQr6usvwRG6n2op6m9%2FConnection%20to%20Azure.png?alt=media&#x26;token=62b89b45-1927-464a-8db6-bc7a665ca303" alt=""><figcaption></figcaption></figure>

1. You can create your **Personal Access Token** by going to the **Security** settings in your Azure Server.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqQHJ23zcVnx2LJ78FOx8%2FPersonal%20Access%20Token%20creation.png?alt=media&#x26;token=5295b308-c730-4660-95d1-317a7d664311" alt=""><figcaption></figcaption></figure>

1. Navigate to **Personal access tokens** and click on **+** **New Token.** Then, name your token and authorize it for **Full access.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0f9Yj3S5RErZ2jBv098C%2FGuide%20to%20personal%20access%20token%20setting.png?alt=media&#x26;token=48d63a77-a3cf-4a6e-a1e0-2d38e043c991" alt=""><figcaption></figcaption></figure>

1. Return to the connection screen and paste your new token in the appropriate field. Finally, click **Add** at the bottom right to save this connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXUG2FvIlMluyR06PcVzy%2FEnter%20the%20connection%20details.png?alt=media&#x26;token=9ba331ec-cd95-4ff0-a69a-85b09d459c9c" alt=""><figcaption></figcaption></figure>

1. Your new connection will be available in the **Select Connection** dropdown list when integrating with Azure DevOps.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjJtPXH0Hzjh44JTLcdqB%2FAzure%20DevOps%20On-Premise%20(1).png?alt=media&#x26;token=594d7d36-38c6-4807-bc71-2dc759dd9482" alt=""><figcaption></figcaption></figure>

1. After selecting the connection, you will be prompted to choose the project you will be syncing. Now click **Connect,** and you’ll be ready to start syncing tasks/issues.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F15XI4jFUrRhg4V5zxlbE%2FSelecting%20the%20newly%20created%20connection%20(1).png?alt=media&#x26;token=29370274-9afe-4e8d-808d-0c01e3fd05f7" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you experience any issues establishing a connection or have any doubts, feel free to contact our support team [here.](https://getint.io/help-center)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
