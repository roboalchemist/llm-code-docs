# Source: https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/applications.md

# Applications

{% hint style="success" %}
**At a glance:** Review a list of all applications by business priority. Get an overview of each application's highest severity issues and drill down into all the details. Perform application-related actions and export comprehensive application information.
{% endhint %}

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9244a81c00a288ed2d2637dd9943a40b775bdb2e%2Fapplications.png?alt=media" alt=""><figcaption></figcaption></figure>

## Summary table

The **Applications** page summary table shows the tags assigned to each application, the highest-severity issues identified during the last scan, and a color-coded representation of the highest-severity issue found at each scanning stage along the software supply chain. Applications are listed in business-priority order.

{% hint style="info" %}
**What is business priority?**

The **business priority** of an application indicates its criticality to your business. It is not related to the application's security state; rather, it allows us to prioritize the issue risk in business-critical applications over those that are not.

Business priority calculation is based on these 3 factors:

* **Development effort:** The number of developers involved, code commits, frequent changes, etc. The more development effort, the higher the priority
* **Cloud usage:** Applications deployed to the cloud receive a higher score. The higher the usage, the higher the priority.
* **Internal characteristics of the application:** Use of PII or financial data, for example, will increase business priority.

You can [adjust the business priority](#set-priority) of any application.
{% endhint %}

## Application details

Click on any application in the table to view its details.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-08c3a34cb869ef56158a80ec742aae4161b62e7c%2Fapplication%20detail.png?alt=media" alt=""><figcaption></figcaption></figure>

The application details pane provides extensive information about the app. Switch among tabs to navigate the types of detailed information available.

## Application actions

The actions available from the buttons at the top of the page give you full control over an application's treatment in OX. You can apply these actions to one application at a time or select multiple applications to apply actions in bulk.

### Assign owners

Click **Assign owners** to give the people you select appropriate roles with respect to an application.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-30f8437f24c6a72ce02f0906ca4d3f4457b7f843%2Fassign_application_owners.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

You can assign one or more owners to a number of different roles:

* Dev owner
* Business owner
* Security owner
* Watcher

You can also add a new owner in the system by adding their name and email.

### Set priority

The **Set priority** dropdown allows you to:

* Adjust the OX-assigned business priority of an app.
* Designate an app as irrelevant.
  * Once an app is marked as irrelevant, it will be moved to the **Irrelevant applications** and [**Exclusions**](https://docs.ox.security/exclusions-and-sla/scope-policy-and-sla-compliance/exclusions) pages and won't be scanned in future scans.
  * If you decide to make the app relevant again, you can do so from the **Irrelevant applications** or [**Exclusions**](https://docs.ox.security/exclusions-and-sla/scope-policy-and-sla-compliance/exclusions) page.

## Export

You can export numerous types of data from the **Applications** page in various formats.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3b8455a58046d904d39c3bca4982e74b05b08c67%2Fapplication_export.png?alt=media" alt="" width="329"><figcaption></figcaption></figure></div>
