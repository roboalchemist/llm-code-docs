# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/defects-card-and-recording-defects.md

# Defects Card and Recording Defects

## Overview

When you're working on a Ticket, Action or Case, operational issues can occur which have an effect on how you're able to deliver the process. It is important to record these as a way to highlight them for others who may view or work on the item, and to help with longer term efforts to improve process delivery.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQzOTYyNw==>" %}

The Defects section on your work item screens in Enate is there to help you record and manage incidents like this when they occur. If [defect categories have been configured in the service line for a Ticket in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen#b-creating-defect-categories), a Defects Card will show in that Ticket's screen in Work Manager that provides the functionality to record defects for the work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWs_UoZmWEu7HtnHRi9%2Fimage.png?alt=media\&token=89cadaa6-2154-4333-82a0-a124d04f4058)

Defects can occur for a wide variety of reasons, for example:

* A client is late supplying information you've requested
* A supplier has attached the wrong file
* Something's gone wrong as part of the service centre's handling of the activity.&#x20;

It is very important to record defects, for various reasons:&#x20;

* while the work item is still in progress, it gives other agents who might be viewing or working on the activity an instant heads-up of issues which have occurred or are still happening which they'll likely need to know about
* after a work item has been closed, it helps serve as an accurate record of what went on and what went wrong - which might be important if you're reviewing a specific item and need to be able to explicitly show for example when a client took longer responding with critical information.&#x20;
* in the longer term it's really useful as part of analysis to spot patterns in where issues are occurring and where improvements can be made - perhaps there's a repeated quality issue with information from an external party, or a given customer if consistently late supplying information at a certain point in process. If defects aren't recorded, it's likely otherwise resolvable issues will still continue to happen.&#x20;

{% hint style="info" %}
It is important to note that the defects feature isn't linked to the way the Enate system determines SLA information.&#x20;
{% endhint %}

## Adding/Editing a Defect

Recording a defect is simple - with a Ticket, Action or Case open, simply expand the Defects card and click to add a new record.&#x20;

Select the relevant category that the defect falls under.

{% hint style="info" %}
If you're finding that some options are missing from the category list, i.e. a type of issue is happening regularly but there isn't really a sensible category for it, feed this back to your business admins and request to get it added to the category list.&#x20;
{% endhint %}

Select the area of responsibility from the ‘Party at Fault’ drop-down - e.g. your organisation, a third party supplier, or the client themselves

Then add a relevant description.&#x20;

If your system is set up to do so, you can also add the number of affected records - an example of when this can be useful is if your were running a payroll process for 100 employees and a defect occurs affecting 20 payslips, you can add that extra detail in here, which can be useful for subsequent reporting.&#x20;

You can add as many defects as are needed if multiple issues occur.&#x20;

Once you have recorded a defect on a particular work item, it is shared with all related cases, tickets and actions in the same manner as contacts are.&#x20;

If a defect gets resolved while the work item is still open, you can go to the defect card and mark it as resolved.&#x20;

If a defect was applied to a work item by accident or the defect itself was recorded incorrectly, you can chose to delete it as long as the work item is still in progress.&#x20;

{% hint style="info" %}
Any user can add a defect and mark defects as resolved. However, be aware that if the ['Restrict Defect Modification' setting](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#restrict-defect-modification) in the System Settings section of Builder is enabled, only the agent who created the defect record can subsequently modify or delete a defect.&#x20;
{% endhint %}

Once you're happy with all the details for your new Defect record, or with your changes if you're editing an existing one, click 'Submit' to save your changes.&#x20;
