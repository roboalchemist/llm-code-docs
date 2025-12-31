# Source: https://docs.avaamo.com/user-guide/release-notes/v5.0-to-v5.8.x-releases/v5.1.x/release-notes-v5.1.md

# Release notes v5.1.0

This article summarizes new and enhanced features in the Avaamo Conversational AI Platform v5.1.0 release:

* **New features**:

  * [Introducing export and import of agents](#introducing-export-and-import-of-agents)
  * [Introducing separate channels for Android and iOS mobile users](#introducing-separate-channels-for-android-and-ios-mobile-users)
  * [Introducing dictionaries](#introducing-dictionaries)

* **Enhancements**: This release also includes enhancements related to SAML Azure, security policies, REST API, and conversation engine performance improvements. See [Enhancements](#enhancements), for more information.

## New features

### Introducing export and import of agents

In this release, you can create a backup copy of your agent in your local system using the **Backup & Export** option. Later, you can use the exported copy and **import** the same to any existing agent in any account.

{% hint style="info" %}
**Note**: Import and export work only in the same version of the platform. This implies that you cannot export your agent in 5.1.0 and import it in the 5.2.0 version.
{% endhint %}

When you export an agent an exact snapshot of the agent as available at that point in time is exported to a zip file. The following lists a few use-cases of this feature:

* Import to an existing agent within the same company
* Import to an existing agent of a different company&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M4wZkp-AIqDEwoNxhIH%2F-M4w_OzHjbdl1ixvUKsa%2Fagent-backup-export.png?alt=media\&token=c0145b08-2cbe-4d63-9edc-d7a54ab1ee91)

See [Export and import agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/export-and-import-agents), for more information.

### Introducing separate channels for Android and iOS mobile users

In this release, you can deploy your agents built on Avaamo Platform into your Android apps or iOS apps separately to facilitate easy communication with Android and iOS mobile users respectively. See deploying agents in [Android apps](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps) and [iOS apps](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps), for more information.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M5Q2DMIYzZPJ5iq7E0u%2F-M5QCxiiy0PNL2iJmgSw%2Fwhats-new-channels.png?alt=media\&token=f6f28f04-66a8-4f9a-97e1-2f94b8215244)

This helps to clearly distinguish and monitor the user interactions from Android and iOS apps channel separately. See [Channels in Analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics), for more information.

In the previous release, web channel was used to deploy for Android and iOS mobile users too, hence it was not possible to monitor and analyze the user interactions from Android and iOS apps channels separately.

### Introducing dictionaries

In this release, you can create dictionaries with a collection of words or phrases that holds a specific meaning to your business. **Example**: Consider that you are creating an HR agent regarding the employee bonus policies. Here, EB (Employee bonus), QEB (Quarterly Employee Bonus), and such terminologies can be added to the dictionary.

These words once added to the agent dictionary are considered differently when understanding user queries. One such consideration is the spelling correction. The system does not attempt spelling correction when it encounters these words in user queries.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M508wCWYM0EOIE62Oom%2F-M50EpeIee_4v9BLvehk%2Fwhatsnew-dic.png?alt=media\&token=a31801a5-fa38-4ca8-874b-218c48190ea5)

See [Add dictionaries](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-dictionaries), for more information.

## Enhancements&#x20;

This release also includes enhancements related to SAML Azure, security policies, REST API, and conversation engine performance improvements. The following table summarizes a few enhancements:

<table><thead><tr><th width="266.41256214512754">Enhancement</th><th width="496.74607791856795">Description</th></tr></thead><tbody><tr><td>SAML Azure enhancements</td><td>In this release, <strong>SAML support for MS Azure</strong> has been enhanced to incorporate the new addition of Unique identifier in the User attributes and claims. See <a href="../../../../how-to/manage-platform-settings/identity-providers/saml-support-ms-azure#user-attributes-and-claims">User attributes and claims</a>, for more information.</td></tr><tr><td>Sign request for SSO</td><td>In this release, a new flag <strong>Sign request</strong> has been added in the Identity providers. This can be used to send the Avaamo certificate and key in the SAML request if required. See <a href="../../../how-to/manage-platform-settings/identity-providers">Identity provider</a>, for more information.</td></tr><tr><td>Security policy</td><td>In this release, you can configure a list of domains in the <strong>Security policy</strong> page from where the resources are allowed to be loaded in the Avaamo platform. This feature is useful in agent development when you are using resources such as fonts, assets, web pages (web view) from an external source that is not whitelisted in the Avaamo Platform. See the <a href="../../../how-to/manage-platform-settings/security-policy">Security policy</a>, for more information.</td></tr><tr><td>Feedback API</td><td><p>In this release, Feedback API has been enhanced to support the following query parameters:</p><ul><li><strong>since_timetoken</strong>, <strong>timetoken</strong>: To get feedback entries within a specified period.</li><li><strong>response_type</strong>: You can specify response_type = detailed in the query parameter to get detailed feedback response with user feedback, user query, and user details for each feedback entry. See <a href="../../../../ref/avaamo-platform-api-documentation/feedback-api#get-feedback-details">Feedback API</a>, for more information.</li></ul></td></tr><tr><td>Custom Channel</td><td><p>In this release, a new parameter <strong>total_messages</strong> has been added in the outgoing request payload of a custom channel for asynchronous mode. </p><p></p><p>This is useful when multiple responses are received in the payload and since it is an asynchronous mode, the sequence of messages is not in a defined order. You can use total messages and sequence, to render the message back in proper order. See <a href="../../../../how-to/build-agents/configure-agents/deploy/custom-channel#outgoing-request">Outgoing request in Custom channe</a>l, for more information.</p></td></tr></tbody></table>
