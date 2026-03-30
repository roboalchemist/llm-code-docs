# Source: https://docs.mailtrap.io/email-api-smtp/deliverability/suppressions-list.md

# Suppressions List

When hard bounce, unsubscribe, and spam complaints events occur, Mailtrap adds the email address to a suppression list. The suppression list contains all the addresses you cannot send emails to.

You'll find all the addresses on suppression lists in the **Suppressions** menu to the left.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-54ff880c7eb4f2239d3d64571d8db844c01286d2%2Fsuppressions-list-table.png?alt=media" alt="" width="563"></div>

The menu contains the data for all your domains. If an email address was suppressed for more than one domain, it appears multiple times on the list.

You can export the whole Suppressions list.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-79c14346a568c54f29866b1c1b4cc618f98e5b49%2Fsuppressions-list-export.png?alt=media" alt="" width="563"></div>

### How to remove an email from a suppression list

If you believe an email landed on a suppression list by accident, you can remove it by clicking the **Reactivate** button to the right.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-778cb990d609d58d2b11031f26dda68a336f7975%2Fsuppressions-list-reactivate-button.png?alt=media" alt="" width="563"></div>

However, we advise you not to misuse the feature.

If someone decided to report your message as spam or leave your email list, you really don’t want to be emailing them again (unless they explicitly told you they had done it by mistake). Any further attempts will probably result in the same outcome, immediately hurting your email deliverability.

### Suppression list filters

You can filter the suppression list for:

* Specific email address
* Sending domain
* Type of suppression
* Reason for suppression

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-fea06a2896ed471c4392f1b27beec65d103c7d0f%2Fsuppressions-list-filters.png?alt=media" alt="" height="129" width="624"></div>

### How to add recipients to the suppression list

Mailtrap allows you to add recipients manually or by uploading a CSV file.

#### Manual method

Select **Insert manually**. Then, under **Add to stream**, choose Bulk, Transactional, or Any. Under **Add to domain**, choose all or one of your domains.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-08174b267885270e2ad47ec0b037a05ccb1f41fd%2Fsuppressions-add-manual-modal.png?alt=media" alt="" width="375"></div>

After you select the domain and stream, type or copy-paste the email addresses you want to suppress into the designated box. Then, click the **Add To Suppressions** button to complete the action.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-cf3549453be1014e877b0159f83fef9ef43f4a65%2Fsuppressions-add-manual-form.png?alt=media" alt="" width="375"></div>

You can add only one email address per line and up to 1,000 emails per selected domain.

Note that there's also the **Add New/Import** button at the top right of the screen in the Suppressions main dashboard. It allows you to access the **Add recipients to suppression list** menu quickly.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-06baa355f9a91da163aa531479c542f878020337%2Fsuppressions-add-new-import-button.png?alt=media" alt="" height="92" width="624"></div>

#### Upload CSV

Before you upload CSV to Mailtrap, you first need to export the document from your current sending provider. See how to do it with SendGrid, Postmark, and Mailgun.

### Exporting suppressions

#### Sendgrid

Navigate to Suppression Management - this is where you’ll find the list of all your Unsubscribe Groups. You’ll see the default groups and the ones you created.

To export the CSV file, you need to click the Settings button (the gear icon) next to each group, then choose **Export**.

#### Mailgun

Mailgun keeps three suppression lists (complaints, bounces, and unsubscribes) for each of your sending domains. There's no global, account-level suppression list, so you need to export separate lists for each domain you transfer to Mailtrap.

To get the list in CSV format, make sure you choose the correct domain and use the Mailgun dashboard to export the lists.

#### Postmark

There’s an Export button in the Postmark dashboard. This allows you to export up to 500 records in a JSON file. For more records, you need to use Postmark’s Messages API.

Many online services offer services for converting JSON to CSV. [Postmark’s help page](https://postmarkapp.com/support/article/881-can-i-export-a-list-of-all-bounces) provides more information.

### Importing to Mailtrap

Select **Upload CSV**, then choose the stream and the domain.

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FLVGZ3DkmdXORBHZ1UMpe%2FScreenshot%202026-01-02%20at%2011.25.25.png?alt=media&#x26;token=059c58bd-3e4d-4433-afec-61f8e6061153" alt=""><figcaption></figcaption></figure></div>

Click **Browse file** to select the CSV file from your computer or drag and drop it into the **Select file** box.

To complete the action, click **Add To Suppressions** and you’re done. If you wish, you can also download our CSV template by clicking on the corresponding option.

**Hint:** You can suppress sending of transactional and marketing emails separately or do both at once by selecting 'Any'. For example, if a user X unsubscribes from marketing emails and they're now on the suppression list, this doesn't stop you from sending them transactional emails. However, if they unsubscribe from those too, they won't receive any emails.
