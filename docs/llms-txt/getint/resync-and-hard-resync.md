# Source: https://docs.getint.io/getintio-platform/resync-and-hard-resync.md

# Resync and Hard Resync

Sometimes overlooked, **Resync** and **Hard Resync** are great options to prompt Getint to sync your tasks again. If you’ve made changes to your integration and want to sync your issues without updating them manually within each app, the resync options are your best bet, depending on your recent modifications.

{% hint style="warning" %}
Please note that a hard resync will not work if the tasks fail to create a counterpart on the other side.
{% endhint %}

### Data synchronization: Resync and Hard Resync <a href="#data-synchronization-resync-and-hard-resync" id="data-synchronization-resync-and-hard-resync"></a>

Resync/Hard Resync will always put an item for the earliest integration execution and process it.

1. **Resync**:
   * **Resync** refers to marking an item for resynchronization. When synchronization is executed, Getint compares the item data fetched from the app with the internal database field data and syncs only those that have changed.
   * In the context of Getint, **Resync** typically involves updating specific fields (such as Assignee, Status, and/or Description, to name a few) for synced items.
   * For example, it can be useful when changes occur in the source system (i.e., an issue’s status changes in Jira), and you want those updates reflected in Getint, but the issue failed to sync during the first run.
2. **Hard Resync**:
   * A **Hard resync** is a more comprehensive synchronization process as it involves re-evaluating all data and applying any necessary updates, even if there haven’t been explicit changes.
   * **Hard resyncs** will mark an item for resynchronization, when sync is executed, Getint treats all fields as modified which forces their resync.

{% hint style="info" %}
Comments & Attachments - only those that were not yet synced in both cases will be synchronized.
{% endhint %}

### How to apply resyncs to existing tasks <a href="#how-to-apply-resyncs-to-existing-tasks" id="how-to-apply-resyncs-to-existing-tasks"></a>

* Open your integration and go to **Latest synced items.**

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2GUQ2hxXjKetylpZ5KKo%2F3ae74758a7b60bd08ec18c6ec79725f9%20(1).png?alt=media&#x26;token=f1b3248d-5451-46e6-8947-b165583d3b99" alt=""><figcaption></figcaption></figure>

* Locate the item you want to resync and click the **3-dot button** on the right.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUXv7pIxoVjFaV4VBgyn6%2F7af215309e3bca61a8f865ecc2760758%20(1).png?alt=media&#x26;token=6bc9dafd-4bef-4173-94df-298663feb668" alt=""><figcaption></figcaption></figure>

* Select **Resync** or **Hard Resync** depending on the changes made to the task, and wait for the integration to trigger a synchronization run. If you applied the necessary changes to either the integration or the app that was causing the failed sync, the item should now properly sync.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fs8NtBVBjecgATN4haZeI%2F6a9128bfcf206ea926b047f708799e6b%20(2).png?alt=media&#x26;token=2540a257-8687-45bb-8aea-db6b954e7477" alt=""><figcaption></figcaption></figure>

Initially, the sync failed due to an inappropriate mapping for statuses. However, after addressing this issue and initiating a resync, the task now transfers correctly to the other side, as evident in the image above.

{% hint style="info" %}
To ensure proper synchronization when using this feature, it’s crucial to make adjustments to your integration and instances based on the errors encountered.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
