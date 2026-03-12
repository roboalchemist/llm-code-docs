# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/local-development-for-apps/deploy-changes-from-local-app-to-make-app.md

# Deploy changes to Make

You can partially deploy changes in components or new components to Make or the whole app can be deployed.

{% tabs %}
{% tab title="Deploy a code file" %}
To deploy only a specific code file in a component to Make, right-click the code file and select **Deploy to Make (beta)**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-ddc0e38f09cdd9b384d423b9a2423fd46eeb4db6%2FScreenshot%202024-05-10%20at%2014.29.43.png?alt=media" alt="" width="386"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Deploy a component directory" %}
To deploy a component to Make, right-click the component directory and select **Deploy to Make (beta)**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-79c1479c7907ee5c76b46a6d0f06f4f444427c63%2FScreenshot%202024-05-10%20at%2014.33.39.png?alt=media" alt=""><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Deploy an app" %}
To deploy the whole app to Make, right-click the **makecomapp.json** file and select **Deploy to Make (beta)**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-3e851a48aebba9d3f4182b9191833d08bde58885%2FScreenshot%202024-05-10%20at%2014.35.49.png?alt=media" alt="" width="545"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

In the dialog, select the origin where the changes should be deployed.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-32b3323550b6184ea63ac9d43dca8e5942149661%2FScreenshot%202024-05-10%20at%2015.23.39.png?alt=media" alt="" width="462"><figcaption></figcaption></figure></div>

The changes or new components are now available in the Make app.

The new app version can be tested in Scenario Builder. If you use testing and production apps, you can deploy the changes or new components to the production after the testing app passes the testing phase.
