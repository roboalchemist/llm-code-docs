# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/creating-new-work.md

# Creating New Work

Work can be created by users from within Work Manager in two ways:

1. **From Create New Work Item.** This is a dropdown available from the toolbar, the agent selects a Case or Ticket to start under a specific business context
2. **From the Contact Activity page**, often also referred to as the Call Handling Page. From this page, the service agent would first search for and find a person (often someone calling in to the service centre), and then start a piece of work directly for them, i.e. a Ticket or a Case

## Creating New Work Item from the ‘Create New Work Item’ dropdown <a href="#a-creating-new-work-item-from-the-create-new-work-item-dropdown" id="a-creating-new-work-item-from-the-create-new-work-item-dropdown"></a>

You can create work by clicking on the ‘Create’ link in the header bar (cube image). This will produce a dropdown screen section allowing you to start a new work item. The hierarchy displayed in the dropdown goes Company, Contract, Service, Process Group (if Configured) followed by the Cases that can be created.

Input links automatically appear here for Tickets and Cases when you have created a Ticket or Case process in Builder and set it to Live. Clicking on a link will create the new work item in a separate tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEhH-dnBbM95bUBf0z%2F-MYEk7maY3OWhZPPG154%2FCreate-Work-Item.gif?alt=media\&token=1d97d13f-88ec-4b2f-b505-dd88d3156538)

{% hint style="info" %}
Note: When running in Test Mode, processes which are in a state of ‘validated draft’ will be displayed here
{% endhint %}

## Creating New Work Item from the Contact Activity page <a href="#b-creating-new-work-item-from-the-contact-activity-page" id="b-creating-new-work-item-from-the-contact-activity-page"></a>

You can create work by clicking on the 'Start New Activity' dropdown on the [Contact Activity page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEkWZ6buBtuWBZ8N3r%2F-MYEmC7zXzcavCD1pAwt%2FCreate-work-from-contact-activit.gif?alt=media\&token=c4cd6836-a55a-47fb-b302-d94716f09670)

If you are on a contact page for someone under a known company (i.e. scoped at customer level), the Customer information will not display in this link name. A free text search will allow you to filter this list of links. Administrators can control whether you wish to see the Input link for a given Ticket / Case process via settings in Builder

Creating a work item from the contact activity page will automatically assign the contact as the primary contact of the work item.
