# Source: https://docs.snyk.io/manage-risk/policies/assets-policies/use-cases-for-policies/notification-policy.md

# Notification policy

You can use the **Send Email** and **Send Slack Message** actions to notify you about changes that take place on your assets.

This use case demonstrates how to set up and receive a notification every time a new class A asset does not have Snyk security coverage.

To follow this example, you need to create four filters that find:

* **Filter 1**: Assets that are of type Repository.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-313c6f62040b084f2a1e8ea02bcf7299f2bfe1fe%2Fimage%20(139).png?alt=media" alt="Filter configuration for asset type" width="352"><figcaption><p>Filter configuration for asset type</p></figcaption></figure>

* **Filter 2**: assets that are Class A.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-88132300f8d636aaaf24e95b8842bc78c9d517f7%2Fimage.png?alt=media" alt="Filter configuration for asset class" width="354"><figcaption><p>Filter configuration for asset class</p></figcaption></figure>

* **Filter 3**: tags that include relevant programming languages (like Apex, ASP, C, C#, C++, CMake, Go, HTML, Java, JavaScript, Kotlin, PHP, Python, Ruby, Scala, Swift, TypeScript, VisualBasic, Handlebars, Makefile, Objective-C).

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4a8fa7f9059122df9b2c12d3dc5a08ebb5852914%2Fimage.png?alt=media" alt="Filter configuration for tags" width="349"><figcaption><p>Filter configuration for tags</p></figcaption></figure>

* **Filter 4**: Do not have Snyk Open Code or Snyk Open Source scan coverage.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-9147ac1776d7ed704abe6940bff67c632e85483d%2FCoverage%20filter.png?alt=media" alt="Filter configuration for coverage control" width="353"><figcaption><p>Filter configuration for coverage control</p></figcaption></figure>

After setting up the filter conditions, you need to choose the **Send Email** action.

{% hint style="info" %}
If you want to set a **Send Slack Message** action, then you can generate the Slack webhook by using the [Incoming WebHooks app](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks) or by [creating your own Slack app](https://api.slack.com/incoming-webhooks).
{% endhint %}

Customize the Send Email action to notify you with a link to the assets impacted by the set policy. You can do this by typing "/" inside the **Body** field of the **Send Email** action and selecting **Link to Assets**. After you save the policy, every notification received will list all the assets impacted by the policy.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fe0e174a0fd9f3385bfb04d4eca58a7467190698%2Fimage.png?alt=media" alt="Snyk AppRisk - Set up the Links to Assets option from the Send Email action"><figcaption><p>Assets Policy - Set up the Links to Assets option from the Send Email action</p></figcaption></figure>

This is how your policy should look after all filters and actions are set.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-957b75a02b3df5245c1eaf28c580f4d76a7efd04%2Fimage.png?alt=media" alt="Snyk AppRisk - Setting up a Notification policy"><figcaption><p>Assets Policy - Setting up a notification policy</p></figcaption></figure>

You will receive an email notification after including the **Link to Assets** option in the Body field. You can access the assets from the notification individually, or view them in an aggregated form by clicking the **Click Here** link. The list of assets displayed in the email notification is automatically generated.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2FC634Vveii9umquWbBNmm%2Fimage.png?alt=media&#x26;token=34af10b5-24f0-43eb-8e24-b52122e5e7ef" alt="" width="375"><figcaption><p>Assets Policy - notification example from the Send Email action</p></figcaption></figure>

{% hint style="info" %}
After an email notification policy is created, it is run in a maximum of 3 hours after creation, then once every 3 hours.

If your policy is set to run daily, then the policy is run in a maximum of 3 hours after the 24-hour period ends. You can always manually run a policy by using the Run button.
{% endhint %}
