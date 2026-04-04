# Source: https://docs.getint.io/getintio-platform/connections/editing-connections-for-existing-integrations.md

# Editing Connections for Existing Integrations

Suppose you need to replace your current connections due to changes in your instance. In that case, the new "Change Connection" feature within the integration screen allows users to edit or select a new connection for existing integrations. This feature is particularly useful when transitioning from a private account (e.g., a user's personal account) to a Service Account or when replacing an expired token.

### How to Use the Change Connection Feature <a href="#how-to-use-the-change-connection-feature" id="how-to-use-the-change-connection-feature"></a>

1. Go to the integration editor and click on the connection you wish to modify.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuY0atGIqVX9vx11LWmDx%2Fe147d8c71ce019bd77d97cf13dbf3514.png?alt=media&#x26;token=beaae64b-2167-4b47-9553-8b69e760ccb4" alt=""><figcaption></figcaption></figure>

1. Click on **Change Connection** to select a different one.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0P42PNA0Te86uT5jcTmS%2Fec5600fbd710815e3180c77a790741d5%20(1).png?alt=media&#x26;token=48b14c70-fb9a-4e1c-8a27-1fb9d1684521" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
This feature is not intended for use with different instances or projects. Otherwise, it will cause data sync issues.
{% endhint %}

### Pros and Cons of Using this Feature <a href="#pros-and-cons-of-using-this-feature" id="pros-and-cons-of-using-this-feature"></a>

To prevent sync errors and ensure your integration works correctly, consider the following criteria:

#### Pros: <a href="#pros" id="pros"></a>

* The ability to edit your connection without starting a new integration
* This feature allows you to modify the connection if you’ve transitioned from a personal account to a service account
* You can edit the connection when the access token expires and needs to be changed
* If there are errors with the current connection, selecting a new connection can often resolve these issues
* If the connection is corrupted and Getint can’t update it, switching connections could solve the issue
* Similarly, if the URL of the destination app has changed, creating a new connection and switching to it may help.

#### Cons: <a href="#cons" id="cons"></a>

* For new users, ensure they have the same permissions and can access fields and issues already synchronized by the integration. Otherwise, they may encounter data sync errors.
* Don't use this feature to change projects or instances, as they might not be compatible

{% hint style="info" %}
This feature is designed for editing connections in existing integrations. Therefore, If you need to modify the connection at a more detailed level, you can do so from the **Connections** setting in **Workflows**. You’ll find comprehensive instructions here: [<img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Ficon%2FPRq8D5IBseUvQPEVFVwD%2FGitbook%20getint%20sygnet%20logo.png?alt=media&#x26;token=3353768c-d008-46f7-bc2d-fd71b5d48f14" alt="" data-size="line">Connections](https://docs.getint.io/getintio-platform/connections#understanding-access-permissions).
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
