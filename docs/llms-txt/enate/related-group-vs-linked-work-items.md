# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items.md

# Related Group vs Linked Work Items

## Group of Related Work Items

Related work items are a tightly connected group of items which, while they behave according to their own specific configuration, do have an active impact on their 'parent' work item - specifically the parent work item will not complete until all of its 'children' have completed first.&#x20;

Communications will be shared automatically between work items in the related group so they are always visible, and when you reply to an email in one work item, the reply can be seen in all the other work items.

Additionally, files, links, defects, smart cards, and contacts are also shared automatically between all the work items in the group, so updating for example a file in one work item will update the file in all the other work items in the related group as well.

Groups of Related work items include:

* A Case and its Actions
* A Case and its Sub Case(s)
* The remaining Ticket and other 'resolved' Tickets if multiple Tickets have been merged
* A 'child' Case and its parent Ticket if a Ticket has been converted to a Case

{% hint style="info" %}
Note that for split Tickets, a snapshot of the files, links, defects, smart cards, and contacts of the parent are to its child Tickets, so updating for example a file in one work item will not update the file in all the other work items in the related group. However, the parent Ticket, which will have moved to a state of Waiting, will not complete until all of its 'child' Tickets have completed first. Also note that if the parent Ticket receives an incoming email, it will be copied to its child Tickets rather than shared.&#x20;
{% endhint %}

## Linked Work Items

When work items don't have an active impact on each other (i.e. they're not part of a Related Work Items group) but there's still a loose connection between them and you want to be able to quickly jump to one from another, you should use the **Linked Work Item** feature in Enate.

Work items with a 'Linked' relationship behave according to their own specific configuration and do not need to wait for the other to complete before they can complete themselves. You can easily link two or more work items together at any time and it's a very useful, flexible way of loosely connecting together items so people in e.g. different departments can stay easily up to date on how other work connected to the Ticket/Case they're working on is going.

Communications will also not be shared automatically between linked work items, but you can choose to copy a snapshot of the communications in one work item to a work item it is linked to. &#x20;

Note that you also have the option to share emails between linked work items - [see here for more information on how to share emails between linked work items.](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/sharing-emails-between-linked-work-items)

Additionally, the files, links, defects, custom data, and contacts will not be shared automatically when launching a new linked work item, but you can choose to copy a snapshot of them. Any updates made to these will not be reflected in the other linked work items.

Work items with a linked relationship will show in the ['Linked Work' tab](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/viewing-linked-work-items) in Cases and Tickets.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fp7AqSvlh87hWLQmsyNC9%2FClicking-on-links-tab.gif?alt=media&#x26;token=b72669b8-0e70-4ef3-a785-be36d3e08a5a" alt=""><figcaption></figcaption></figure>

Using this type of connection is useful if e.g. a Case’s due date is not dependent on some other piece of work being completed (e.g. by a different department), but it's still considered useful for people working on either one to remain aware of activity on the other and, importantly, to have a quick point of accessing the other.&#x20;

Work Items can be linked together in the following ways:

* A Case or a Ticket launched directly from within an existing Case or Ticket.
* Manually adding a link from a Case/Ticket to another existing Case or Ticket.
