# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/creating-new-work/creating-a-work-item-from-an-existing-email.md

# Creating a Work Item from an Existing Email

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTYzNDYwNg==>" %}

There are certain circumstances when clients may send in an email that should really be used to start a new work item but, because they've sent it as a response to an existing mail chain, it ends up being attached to an existing work item. A prime example of this is when a client responds to an email with the intention of starting a new ticket but it gets added to the work item of the email chain that they were replying to. In such circumstances, you can use the 'Create a new Work Item from this email' feature which allows incoming emails that get added to an existing work item like this, to now be reprocessed and used to create a new work item.

### When will you be able to create a Work item from an existing email?

You will have the option to create a Work Item from any email that is attached to an existing Work Item, so long as it is not the initial email that created a Work Item.&#x20;

### How does this work?

If you are working on a Work Item and realize that an email that has been attached to it should actually have started a new Work Item, you can use the 'Create a new Work Item' icon that will appear on the email attached to the Work item which you want to use to create new work.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F87zKtmQRCCVNYu652ix9%2FCreate%20Work%20Item%20Link.png?alt=media&#x26;token=da6392c0-638b-4e27-8cd0-625600c2fed4" alt=""><figcaption></figcaption></figure>

Clicking this link and then the following confirmation popup will result in the email being effectively sent back into Enate, but with an additional rule that it should not append itself to an existing work item. Once the email has successfully created a new work item, a confirmation message will appear.

Once the new work item has been created, a note will show at the top of that mail with a link to that new work item, and that original mail entry in the first work item will effectively be set to 'read only' (since it should no longer be used to process the request within that mail).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F92qaBELUeQKzrgu9YeCf%2FCreate%20Work%20Item%20Link2.png?alt=media&#x26;token=0ae49dfd-2e20-4e72-bf22-86ce6ceef05d" alt=""><figcaption></figcaption></figure>

Links between the original Work Item and the new Work Item will also be displayed on each of their respective 'Linked Items' tabs.

{% hint style="info" %}
It should be noted that this option will never appear on the initial email which creates a work item, only on subsequent incoming emails which *could* be inappropriately appending.
{% endhint %}
