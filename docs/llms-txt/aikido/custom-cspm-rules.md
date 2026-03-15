# Source: https://help.aikido.dev/cloud-scanning/custom-cspm-rules.md

# Custom CSPM Rules

Aikido’s Custom CSPM Rules let you define cloud misconfiguration rules in natural language, generating new issues in the feed based on your cloud asset searches. All these issues follow the same functionality as other issues in the feed, e.g, **ignore, snooze, alert notifications**, **task creation**, **etc.**

### **Use cases**

* Extending the out-of-the-box Aikido cloud checks.
* Organization-specific requirements, such as data residency or tagging policies.
* Responding to zero-day cloud misconfigurations.

### **Create a Custom CSPM Rule**

**Step 1.** Go to the [**Cloud Assets**](https://app.aikido.dev/clouds/assets) page in Aikido.

**Step 2.** Click on **Custom CSPM Rules**

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FSi2hoUKwYzeMyJL3O4VX%2Fimage.png?alt=media&#x26;token=c4f6331b-9b37-44f9-9dcf-3df36192d15b" alt=""><figcaption></figcaption></figure>

**Step 3.** Click **Create custom rule** on the Custom Rules Page.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F91JAQuYd41DfiikMqCkB%2Fimage.png?alt=media&#x26;token=8bb2b41d-eb10-44d7-9c6d-8b033941238d" alt="" width="563"><figcaption></figcaption></figure>

**Step 4. Fill in the necessary details to create the rule**

* &#x20;Add a **related search query** to define the condition that triggers the issue (e.g. `buckets outside eu`).
* Issue title
* TL;DR
* How to fix
* Score (this impacts severity)

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FwSds18fI5YEqlTJ4u3D5%2Fcustom-rule-buckets-eu.png?alt=media&#x26;token=e4f687d9-7a5e-490f-b23f-c14c9567a8ae" alt="" width="563"><figcaption><p>Custom cloud rule example</p></figcaption></figure>

**Step 5**. Your rule will be added to the page. You can always edit or delete by clicking the action dropdown menu.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FfVLFZPChJzCj8H3oAWsN%2Fimage.png?alt=media&#x26;token=2f98905a-c6f1-4bbf-b6d2-89a74bccab1f" alt=""><figcaption></figcaption></figure>

**Step 6.** Trigger a new cloud scan manually to have matching results appear in the feed.

### **Important Notes**

* Custom CSPM rules are evaluated after they are created and with each cloud scan.
* These rules generate **cloud misconfiguration issues**, which support all standard issue features (severity adjustment, Slack integration, task creation, etc.).
* Custom CSPM rules are applied **across all connected cloud accounts**.

### Mapping to Compliance Reports

You can map custom CSPM rules to compliance reports by adding compliance tags when creating or editing a rule. Aikido uses these tags to automatically include the rule in all relevant compliance sections of the supported benchmarks. The custom CSPM rules will appear in the compliance reports right after you add the tags, and will behave like any other cloud rule/check.

For example, if you wish to map a rule to "ISO 27001:2022, A.8.13 - Backups", you add the `Backup` tag. Please reach out to us if you need support or aren't sure which tag to use.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FzMraEnLqePTPb8QXuQAr%2Fimage.png?alt=media&#x26;token=da431183-e54f-40ae-8f41-8a50031776dc" alt=""><figcaption></figcaption></figure>
