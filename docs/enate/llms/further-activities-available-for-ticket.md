# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/further-activities-available-for-ticket.md

# Merging a Ticket into another Ticket/Case/Action

## Overview

The 'Merge' functionality in Enate lets you merge existing work items together so that queries which arrived separately - but should in fact be processed together - can be processed as one work item.

This is useful when, for example, an incoming email relating to an existing request inadvertently creates a new Ticket instead of auto-appending itself to an already existing request. This can sometimes happen if the incoming email isn't a direct reply to a previously sent Enate email or if the reference number of the initial Ticket isn't part of the email.

Watch this video to find out more about how to use the merge feature or continue reading below.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgzNg==>" %}

## How to Merge

There are two ways you can merge Tickets in Enate:

* [Close THIS Ticket (and merge it into an existing Ticket / Case / Action in the system)](#option-1-close-this-ticket-merge-it-into-another-work-item)
* [Keep this Ticket open (and merge other existing Tickets into this one)](#option-2-keep-this-ticket-open-merge-other-tickets-into-it)

### **Close this Ticket, merge it into another work item**

To merge a Ticket into another work item, click on the 'merge' tab and select the option to close 'This work item'. Then from the accompanying search field select the work item you want to merge the Ticket into from the Search bar. You can search by title, reference number or the name of the customer, contract or service that the work item belongs to.

{% hint style="info" %}
Please note: when choosing to close THIS Ticket and merge other work items into it, select a Ticket, Case or Action to merge the Ticket into, but note that the work item selected must be running. Additionally, if your search returns more than 50 results, only the most relevant top 50 will be displayed. If your desired work item does not appear in the top 50 results, add more search criteria to narrow down the results.
{% endhint %}

Select the Merge button from the Info card to confirm.

The Ticket tab will close and be marked as 'Closed' with a resolution method of 'Merged'.&#x20;

If you click view this ‘closed’ Ticket again, you will see its status, who it was resolved by, when it was resolved and its resolution method (i.e. 'Merged'). Additionally, the Info card will display a link to the work item it was merged into.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyPYLcHobt6ZfvcbEeP6K%2F12A%20Merge-Close-this-work-item.gif?alt=media&#x26;token=f8611f3d-8c92-4a51-993b-6a7e4701e156" alt=""><figcaption></figcaption></figure>

Communications from the now closed Ticket will now display in the timeline of the remaining work item, marked with a green dot to show they are new to this work item and the reference number of the Ticket they originate from. The markers will clear when a user sets the new information icon as read.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoPAyRiS2k1IK1aBQDRdG%2F12A%20View-Merged-Comms-Action.gif?alt=media&#x26;token=2841fa0d-122e-4949-ba57-d7fc0ca1574f" alt=""><figcaption></figcaption></figure>

### **Keep this Ticket open, merge other Tickets into it**

To keep this Ticket open and merge other existing Tickets into it, click on the 'merge' tab and select the option to close ‘Other work Items’. Then select for the desired Ticket(s) to merge the Ticket into from the Search bar. You can search by title, reference number or the name of the customer, contract or service that the work item belongs to.

{% hint style="info" %}
Please note: when choosing to close OTHER work items, you can only select Tickets, but you can select multiple Tickets at one time. If your search returns more than 50 results, only the most relevant top 50 will be displayed. If your desired work item does not appear in the top 50 results, add more search criteria to narrow down the results.
{% endhint %}

Select the Merge button from the Info card to confirm.

The other Ticket(s) will be set to ‘Closed' with a Resolution method of 'Merged' and a link to the Ticket they were merged into. If you click view the ‘closed’ Ticket(s), you will see its status, who it was resolved by, when it was resolved and its resolution method (i.e. 'Merged'). Additionally, the Info card will display a link to the work item it was merged into.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1kWjpGfZJJKuZncqheSg%2Fimage.png?alt=media&#x26;token=1e7919b5-b87f-4c1c-a776-bda06f33941c" alt=""><figcaption></figcaption></figure>

Communications from the now closed Ticket will now display in the timeline of the remaining Ticket, marked with a green dot to show they are new to this work item and the reference number of the Ticket they originate from. The markers will clear when a user sets the new information icon as read.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoPAyRiS2k1IK1aBQDRdG%2F12A%20View-Merged-Comms-Action.gif?alt=media&#x26;token=2841fa0d-122e-4949-ba57-d7fc0ca1574f" alt=""><figcaption></figcaption></figure>

### Due Dates & Merging

When merging a Ticket or Tickets into another work item, **the Due Date of that remaining work item is the single relevant Due Date for any ongoing work**. It is not recalculated as part of the merging, and similarly the due dates of any of the previously running work items (now set to Closed) are not recalculated before their status is set to Closed. Examples:&#x20;

* If an overdue ticket is merged into an on-time work item, the Due Date of the remaining work item stays unaffected - it is not classed as now being Overdue.
* If an on-time ticket is merged into an overdue work item, the Due Date of the remaining work item stays unaffected - it is not classed as now being 'on time'.
