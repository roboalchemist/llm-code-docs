# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/getting-new-work.md

# Getting New Work

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc3MQ==>" %}

Clicking on the 'Pull from Queue' button in the Work Inbox grid header will assign you a new piece of work, if any is available for your to do.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWqMXrK_ZvY1cj8JBqs%2F-MWqRv4hiUBVt6rGJXr3%2Fimage.png?alt=media\&token=0ae54aa3-e15a-4bc0-afd5-26dc5ed9119f)

### **Pull from Queue Allocation Rules**

**How does the system determine which work item to give a user when they click the “Pull from Queue” button on their Work Inbox?**

The system works by looking at all unassigned work items from all of the Queues the user is linked to, and has permissions on, and assigns one new work item, prioritising items as follows:

1. Any currently OVERDUE work item (most overdue item first). If none found, then
2. Any work item which has been rejected by a Robot. If none found, then
3. Any work item (item due soonest selected first).

{% hint style="info" %}
Note: Queues set to ‘strict mode’ are there to allocate work strictly to robots. Any human users linked to such queues are there only as a fall back for rejected robot work items, and aren’t auto-allocated the normal, unrejected work items from them when hitting “Pull from Queue”.
{% endhint %}
