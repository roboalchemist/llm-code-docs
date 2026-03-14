# Source: https://docs.getint.io/getintio-platform/unsync-feature.md

# Unsync Feature

## Managing and Stopping Synchronization

This guide explains how to use the **Unsync** feature to break the connection between paired items, as well as alternative methods for managing synchronization scope.

{% hint style="info" %}
**Note**: The “Unsync” button directly breaks the link between paired work items. You can also stop synchronization by excluding items from the sync scope, deleting the items, or disabling the integration entirely.
{% endhint %}

### How to Unsync Items in Getint <a href="#how-to-unsync-items-in-getint" id="how-to-unsync-items-in-getint"></a>

1. First, enable the corresponding property to make the feature visible in the Getint UI. To do this, go to **Settings** (represented by a cog icon) and navigate to the **Custom Properties section**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEDOuQnXM7OPDUrhlphOy%2FWhere%20to%20find%20the%20custom%20properties.png?alt=media&#x26;token=c836c74b-6056-41a8-b1bd-e077a6c1aec1" alt=""><figcaption></figcaption></figure>

1. Click **Add New Property**, and two new fields will appear. Then, enter the following values in those fields as shown below:
   * `FF_BULK_SYNC_ENABLED`
   * `true`

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FkyUIu3ugVsa42PK8ijw7%2Fadd%20new%20property.png?alt=media&#x26;token=ca48da94-49bf-434c-9008-c3b827e60bcc" alt=""><figcaption></figcaption></figure>

1. Use the **Add** button to register the new property and click **Save** to apply the changes.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7BTT6qMJBgpAOJSvgZbN%2Fenabling%20the%20custom%20property.png?alt=media&#x26;token=38762232-0edf-4f7e-b8c5-082be27db067" alt=""><figcaption></figcaption></figure>

1. Now, if you go to **Reporting** > **Synced items**, you will see that the **Unsync** button is visible before the import feature.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FnhLqVH3nQUZB21FAp3NG%2FUnsync%20button.png?alt=media&#x26;token=b5e942a3-f940-42c2-86b8-61f25d0acd3b" alt=""><figcaption></figcaption></figure>

1. Disable your integration. Next, select the integration where you will unsync pairs, paste the IDs of the related items, and hit **Apply**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fq4yqW8j8EphIjCkEUuIH%2FUnsyncing%20items.png?alt=media&#x26;token=87bf37a1-6dcf-43e4-aede-3360b5c55879" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
We’re using Jira and ServiceNow as examples, but the same approach applies to any connector. Please make sure to respect the direction of the integration: if Jira is on the left side, paste the Jira IDs on the left and the counterpart application’s IDs on the right. If the sides are reversed, do the opposite.
{% endhint %}

1. Go back to your integration, and open the **Latest synced items** section. The latest run will say **!UNSYNC!**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSla2wjGrc5tnD4VAwAeE%2FChecking%20changes%20in%20latest%20synced%20items.png?alt=media&#x26;token=7e6f8d55-7c5b-4ef8-ad93-5db32a0eaf86" alt=""><figcaption></figcaption></figure>

1. You can then open the sync logs to see if the unpairing was successful.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9hMXXlnsHQ5vafgflNGZ%2FOpening%20the%20sync%20logs.png?alt=media&#x26;token=fb2a534a-b689-4c96-81b7-00e3384708cf" alt=""><figcaption></figcaption></figure>

### Final Steps and Verification <a href="#final-steps-and-verification" id="final-steps-and-verification"></a>

The logs will show whether the relationship between the selected items was successfully removed. After verification, you may re-enable the integration if needed, or continue managing your synchronization scope based on your requirements.

If you have questions about Unsync behavior, encounter unexpected results, or need help choosing the best approach for managing your synchronization, our team is here to help. Don’t hesitate to reach out to [Getint Support](https://getint.io/help-center) for guidance tailored to your integration setup and use case.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FDJ1yThyNC3Q2o96EkYmv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=d3229fa0-1281-459d-b681-7f78b855bcaf" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
