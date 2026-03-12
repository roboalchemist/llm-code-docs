# Source: https://docs.getint.io/getting-started-with-the-platform/about-getint-concepts/how-integrations-are-executed-by-getint.md

# How Integrations are Executed by Getint

## Integration Execution: The Basics

In Getint, each integration runs sequentially, meaning one integration execution must finish before the next one can start. This concept is crucial to understand as it directly impacts the frequency of integration runs.

For instance, Jira Cloud users can only set a run interval of a minimum of 3 minutes, and Data Center customers have run intervals of a minimum of 60-120 seconds (mostly 120 seconds). However, On-Premise users can have run intervals of >= 0 seconds.

When users set an interval for integration (such as every 15 seconds), it’s important to understand that this doesn’t guarantee the integration will occur exactly every 15 seconds. The actual frequency of execution depends on various factors, including the total number of integrations and the duration each integration requires to complete.

### The Impact of Multiple Integrations

If a user has a large number of integrations, it can significantly impact the sync time of changes. For instance, if an item is set to be synced by an integration that is 10th in a queue, and each preceding integration takes 15 minutes (due to the large amount of data they sync), the user may experience a 2-3 hour delay between the change and its propagation.

In a scenario where there are 50 integrations, a 60-second interval won’t be effective because each integration needs to be completed before the next one can start. Therefore, the interval time does not always dictate the frequency of integration runs.

### Boost your Performance with Getint On-Premise

For customers seeking improved performance and parallel integration execution, Getint’s On-Premise solution stands out as a robust choice. This solution allows customers to run multiple threads and assign integrations to them, thereby significantly enhancing performance. Also, On-Premise operates entirely behind your firewall, providing a secure environment aligned with your company requirements.

The benefits of using our On-Premise solution include, but aren’t excluded to:

* Modifying run intervals to your system needs
* Supports multithreading and multi-tenancy
* Saving your data is configurable, which differs from Cloud users who can only retain their data for a maximum of 1 month
* Freedom to perform your own server maintenance and software updates

### Optimizing Integration Settings

To optimize the performance of Getint, users should consider the number of integrations they have and the interval they set for each integration. If there are more than a certain number of integrations, users might need to adjust the intervals to ensure efficient data syncing.

Understanding these nuances can help users make the most of Getint’s powerful integration capabilities and ensure smooth and timely data syncing across platforms. Remember, the key is to find the right balance between the number of integrations and the intervals set for each one.

{% hint style="info" %}
If you have any questions or need assistance with your integration, don’t hesitate to contact our [Support Center.](https://getint.io/help-center)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
