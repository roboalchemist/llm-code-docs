# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/unprocessed-emails/creating-new-email-routes-from-unhandled-emails.md

# Creating New Email Routes from Unhandled Emails

As part of dealing with Unhandled emails, agent users can create email routing directly within Work Manager. Creating these rules helps stop equivalent future emails from landing as Unhandled emails, ensuring that a Ticket or Case gets created for them. This reduces future Unhandled email volumes and makes sure work can start on these items more quickly. To provide an element of control, the ability of Work Manager users to create new email routes is an option which can be turned off/on in via User Roles in Builder.

Once these rules are created in Work Manager they're instantly live and working, however Admin users in Builder are notified of any new routing rules created in this way, and these remain marked for their attention until the Admin acknowledges them. Admins still have the ability to adjust or even turn off such rules after assessing them.

### Granting Access to Work Manager users to create new Email Routes

Feature Access to be able to create new Email Routes in Work Manager is controlled via Enate's User Role system, with a new option being added to the Email View Options section.

{% hint style="info" %}
Note: This 'Create Email Routes' access will be set to **ON** for the Standard Team Member role
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyNkwH8IE8SSXY3zcPIXK%2Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_1JbSS8D8arRxmWau5EPQ_image.webp?alt=media&#x26;token=9234507a-2226-4f34-94ec-4f9428481e66" alt=""><figcaption></figcaption></figure>

### How to create a new Email Route in Unhandled Emails

While dealing with an unhandled email in the Unhandled emails section of the Email Inbox page, if you choose to have the email processed into a Ticket / Case (by clicking 'New Work Item' option), you'll be met with the following popup:&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FrvRXtoAG2LyFHMOwizyT%2FCreate%20Route1.png?alt=media&#x26;token=dbf82db2-f0db-46da-abe8-eb4d540dfafb" alt=""><figcaption></figcaption></figure>

You can search by email route (which will auto-populate the Customer/Contract/Service/Process fields based on suggestions for the mailbox address selected), or can manually select. Clicking Create at this point will create the specific Ticket or Case from the email, as normal.

However, if you *also* wish to have the same thing happen automatically ongoing, you can click on the 'Apply to other emails' link at the foot of the popup before you hit 'Create'. If you've selected this option, when you hit 'Create' two things will happen:

* A small confirmation message shows confirming that a new work item has been created.
* A further popup screen to 'Create New Email Routing Rule' is then shown where you can fill in the remaining routing rule details before confirming its creation.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FA5EHkoxNFPiLWZRJoNVx%2Fimage.png?alt=media&#x26;token=85345a14-0474-4d5e-b75f-f5fc449f1748" alt=""><figcaption></figcaption></figure>

You can decide if the route is going to be a 'To' or 'From' type of route, i.e.&#x20;

* 'treat all emails FROM this address in the same way', OR
* 'Treat all email TO *this* address in the same way'&#x20;

and then which email address is to be used in conjunction with this. Enate will automatically fill the email address with the relevant email address associated with the unprocessed email you were working on.

{% hint style="info" %}
Within the 'Tips' section of this pop-up, there is a link that will take users to the Unhandled Emails page of the Enate online help, should users require any more information.
{% endhint %}

### Applying the Rule to Existing Email (Run Retrospectively)

In addition to setting a rule which will deal with all future emails that match this pattern, you can also choose to have the rule run against all/some of the existing Unhandled emails which match this rule. If you wish this to happen, select the 'Auto-apply' toggle and this foot of this popup.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqO47hIs4kOOPFQBJfdfM%2Fimage.png?alt=media&#x26;token=e2525eb0-5a76-4b71-ba0e-6f6ecc731b47" alt=""><figcaption></figcaption></figure>

The system will show you how many of the current backlog of Unhandled emails match this rule, i.e. how many would be reprocessed.

#### Choosing a time range to select which existing Unhandled emails to reprocess.

Selecting this option will bring up a time filter allowing you to select a subset of these existing emails to run the rule for (if, for example, you only want to run this for emails up to a week/month old etc.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fn2eBkAxBuSNOIqf7KJtc%2Fimage.png?alt=media&#x26;token=ff0b2bb8-59b2-4df1-b485-e8dd9dbfca9b" alt=""><figcaption></figcaption></figure>

You can use the slider to set different date ranges, including setting specific dates. As you change this setting, the system will update to reflect how many emails this would run the rule for.

When you're happy with your selection, you can hit Create - the rule will be re-run and emails will start to be re-processed into the type of Case or Ticket you specified.

{% hint style="info" %}
Important Note: Once you create a new email routing rule in this way via Work manager, it will instantly go live and start to run against any subsequent incoming emails.
{% endhint %}

### Admin Visibility of New Email Routing Rules in Builder

If any new email routes have been created in Unhandled Emails in Work Manager, Admin users will be made aware of this in Builder by a red dot on the Email icon section.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOCbHGjSKXK8K3BXQeE8U%2Fimage.png?alt=media&#x26;token=50ad60d5-23d6-4297-8582-050b2225df18" alt=""><figcaption></figcaption></figure>

Throughout any subsequent navigation sections and screens as they drill down to the Email Routes page, there will be continued signposting down the new Routing rules that they should be aware of.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJCXHPvZ5wEdho7smifBp%2Fimage.png?alt=media&#x26;token=32123ad9-aa86-4006-b971-836341ec7707" alt=""><figcaption></figcaption></figure>

Once on the Routes page, users will see a banner notifying them of new email routes to be aware of, as well as how many there are. A link will allow them to filter the routes down to just those new ones that they need to be aware of.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fl8VwMLkswDUnG5UA75sv%2FAdminBeAware.png?alt=media&#x26;token=9b87a49a-e13c-4402-a327-76044c2c011d" alt=""><figcaption></figcaption></figure>

Within the routes table itself, users will be alerted to these new routes to be aware of.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fp2hWdi9wYE195t19WGP6%2FAdminBeAware2.png?alt=media&#x26;token=c9babbfc-327b-4550-9076-6bf588707295" alt=""><figcaption></figcaption></figure>

Admin users are encouraged to review these new routing rules (and speak to the agent who created them\*) to make sure they're happy with how they are running in conjunction with the various other rules. They can choose to unset them from live, make any adjustments and even delete them if they feel necessary.&#x20;

If they're hapy with the rule they shoud unmark the 'be adjusted, They can use the 'Clear review filter' link in the header to return to the normal view.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0rpGLXp51E0SByACl6lt%2Fimage.png?alt=media&#x26;token=b780afeb-2af3-45ba-8234-69ba1d3a2f98" alt=""><figcaption></figcaption></figure>

\*You can view who created an email routing rule from the 'Show Activity' icon in the top of the rule details popup.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fw1F9yvhhNVNxt2nS17wH%2FAdminBeAware3.png?alt=media&#x26;token=72939c51-d690-4e09-9457-388374f4ca91" alt=""><figcaption></figcaption></figure>

Clicking on this will show the audit trail of who created and updated this rule.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUXIQugqD0R0gE64poKAD%2FAdminBeAware4.png?alt=media&#x26;token=31d7b1d7-4294-456b-a90c-8863c417dde6" alt=""><figcaption></figcaption></figure>
