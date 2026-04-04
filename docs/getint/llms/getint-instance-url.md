# Source: https://docs.getint.io/guides/integration-synchronization/jira-jira-integration/getint-instance-url.md

# Getint Instance URL

The **Getint instance URL** is a unique identifier for a Getint installation. It is used to establish secure connections between Jira instances, validate licenses, and expose important instance metadata. This article explains what the Getint instance URL is, where to find it, and how it’s used in cross-instance configurations.

### What Is the Getint Instance URL? <a href="#what-is-the-getint-instance-url" id="what-is-the-getint-instance-url"></a>

The Getint instance URL uniquely represents a Getint instance running within a Jira environment. It allows Getint to:

* Identify another Getint instance on the “other side” of a connection.
* Validate licensing without querying Jira directly.
* Exchange instance-level metadata, such as version and data residency.

From now on, the Getint instance URL is the **single source of truth** for instance identification and license checks.

### Obtain Your Getint Instance URL <a href="#obtain-your-getint-instance-url" id="obtain-your-getint-instance-url"></a>

Each Jira instance running Getint has its own Getint instance URL.

To find it:

1. Open the **Getint app** in your Jira instance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F6GI0XTsRJyg2VfloyI1J%2FOpening%20Getint.png?alt=media&#x26;token=aafe6cc9-49d5-4486-b19e-f2d83909e365" alt=""><figcaption></figcaption></figure>

1. Navigate to **Settings**, and open the **General** tab. Your **Getint instance URL** is displayed there.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FB9jS0exj1LMfnVGCzQWD%2FGetint%20Instance%20URL.png?alt=media&#x26;token=428a1786-eeec-41ca-9eaf-4f4d952aea46" alt=""><figcaption></figcaption></figure>

This URL is generated automatically and is specific to that Getint installation.

### Adding the Getint Instance URL to the Connection <a href="#adding-the-getint-instance-url-to-the-connection" id="adding-the-getint-instance-url-to-the-connection"></a>

When setting up a connection between two Jira instances, you must retrieve the URL from the **counterpart** (the Jira instance you are connecting to).

{% hint style="info" %}
You do not need to provide the Getint instance URL in the connection that is running the integration.

The only exception is when a single Getint instance connects to two different Jira instances, for example, one on the left and another on the right. In this scenario, each connected Jira instance must have its corresponding Getint instance URL specified in the connection configuration.
{% endhint %}

1. Go to the connection configuration (**Workflows > Connections**), locate the Jira connection you want to update, and click the **3-dot button** below “Actions.”

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FtB86uz1J6OCbni5yH37I%2FLocate%20the%20second%20jira%20connection.png?alt=media&#x26;token=7e3ef1fa-9069-436c-b485-cabe938accd6" alt=""><figcaption></figcaption></figure>

1. Click on **Edit** to modify the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FY3MjDZy2Zs0Ch95DZ6mb%2FOpening%20the%20actions%20for%20the%20connections%20tab.png?alt=media&#x26;token=4ddecb48-b9ec-4747-86c0-40bb0ef6d0d6" alt=""><figcaption></figcaption></figure>

1. Specify the **Getint instance URL of the partner** (Getint instance on the other side), and hit the **Update** button.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0uKavt3xNoEXBgSYiC8m%2FEntering%20the%20second%20Jira%20instance%20URL.png?alt=media&#x26;token=27ca6f84-1585-4466-a27e-4bcf172f03d8" alt=""><figcaption></figcaption></figure>

1. Now test your integration. This time, you shouldn’t experience any Jira licensing errors.

Once updated, the two Getint connections are linked, allowing for secure and accurate cross-instance communication.

### Licensing Behavior Using the Getint Instance URL <a href="#licensing-behavior-using-the-getint-instance-url" id="licensing-behavior-using-the-getint-instance-url"></a>

With Forge, licensing is now handled at the Getint level rather than through Jira directly.

* If **Jira 2 is licensed**, license validation is performed by querying the **Getint instance** identified by the provided instance URL.
* Getint no longer asks Jira whether a license exists.
* Instead, Getint asks the **other Getint instance**: “Is there an explicit license associated with this instance URL?”

### Summary <a href="#summary" id="summary"></a>

* Every Getint installation has a unique **Getint instance URL**.
* The instance URL is available in the **Getint app** > **Settings** > **General**.
* No need to specify an ID for your local Jira instance (the Jira that is running the integration), regardless of whether it is configured as the left or the right side of the connection. Just focus on grabbing the Getint URL for the counterpart instance.
* License validation is now performed via Getint using the instance URL, not Jira.
* Additional metadata, such as version and data residency, is tied to the instance URL.

Using the Getint instance URL ensures clear identification, accurate license validation, and a scalable foundation for cross-instance integrations.

### Need Assistance? <a href="#need-assistance" id="need-assistance"></a>

If you encounter any issues retrieving your Getint instance URL, configuring the connection, or validating licensing, please contact our [**Support Team**](https://getint.io/help-center) for assistance.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
