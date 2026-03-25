# Source: https://docs.getint.io/getintio-platform/workflows/syncing-attachments.md

# Syncing Attachments

Attachments are important for managing tasks, and syncing them across different apps can make your work smoother. Getint is a handy solution for syncing attachments between tools, whether they are Jira integrations or non-Jira integrations. In this article, we’ll explore the steps to achieve error-free attachment synchronization.

### How to Enable Attachments <a href="#how-to-enable-attachments" id="how-to-enable-attachments"></a>

By default, this option is activated for most type mappings. However, it’s crucial to ensure that this feature is enabled before syncing issues. Otherwise, Getint will simply skip attachments during synchronization runs.

* To activate attachments, launch Getint, and open a type mapping (for example, **Epic-Epic**). Then, navigate to the **Comments & Attachments** section and enable the option.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F4C5gv1wqgLAEZwi1iOVK%2Ff9e4a350114217f819d6c6c3ce4ffaf6.png?alt=media&#x26;token=79c5b339-cda2-4a6f-b9bd-2cc39f599b37" alt=""><figcaption></figcaption></figure>

* Determine the sync direction for attachments, as well as customize how attachments are populated between apps. Attachments sync can go both ways or only to the right/only to the left side. Remember to click **Apply** to save your changes.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FpKpIUaOmGM9MQeg8oKS6%2Fae00539051566b37feb61a511d3097c4%20(1).png?alt=media&#x26;token=2dc048a0-1db7-4537-94e1-96402fb50182" alt=""><figcaption></figcaption></figure>

### Attachments Limitations <a href="#attachments-limitations" id="attachments-limitations"></a>

Depending on the app you’re integrating, the attachments could have different rules, or there might be considerations to make, such as:

* Monday doesn’t support inline images. Therefore, this option won’t be available when enabling the Attachments feature. However, it is available for other integrations, such as Azure DevOps, as you can see in the above picture.
* The maximum number of attachments to sync per integration run is limited to 10 for Saas (Cloud) customers. However, Jira Data Center apps and On-Premise customers can sync unlimited attachments per run.

{% hint style="danger" %}
When using the **Comments & Attachments** tab, please be aware that if attachments are not supported by the app (such as HubSpot or Airtable), the tab will be labeled simply as **Comments**.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdFNpRBjRnQouKqmlnwRV%2Fb91fc6ecdce9052dd707b8bdfb88ffb5%20(1).png?alt=media&#x26;token=0c898270-d5a5-47b8-afa1-2ae375de5331" alt=""><figcaption><p>Jira Airtable integration. As attachments aren’t supported for Airtable, there’s no indication about them.</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
