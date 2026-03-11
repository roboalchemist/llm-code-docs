# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/home-page/home-page-bar-chart-and-grid.md

# Bar Chart and Grid

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTYzNw==>" %}

## Due Date Totals

Work items are classified into their respective due states:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdbqOhT7XiA8kQvosed%2F-MdbqVS56q-mM2DUX-x7%2Fimage.png?alt=media\&token=a125c9d6-b2fa-4999-98c6-817e90e57cb1)

* Green – on target, not yet overdue
* Amber – due today (but not yet overdue)
* Red – work items which are now overdue (including items where the due date is today, but the due *time* has now passed).
* Grey – work items are classified into a state of 'Not Set' when the due date is not currently known. This can be in the following situations:
  * When the work item has just been started (manually) but has not yet been submitted
  * When the work item is in a state of ‘Wait for more Information’ AND is set to add the wait time on the due date

If you click on one of the due dates, the grid will be filtered down to work items with just that due date:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvMJwEWwCpg6vwuKNFhJb%2F3-Click-on-Due-Date.gif?alt=media\&token=0ddf747d-b95b-49e5-9fe1-f19420befcdf)

## Bar Chart

Bar Chart information is displayed in a Pareto format, i.e. with highest volumes shown first. A maximum of ten bars are displayed. The top nine groups are displayed uniquely, with all remaining items shown combined in the final bar.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWqMXrK_ZvY1cj8JBqs%2F-MWqQxBGcx5FnmgWVNoW%2Fimage.png?alt=media\&token=384518e9-9c27-4eb1-80c5-59143b31ac22)

### Bar Chart ‘Display By’ Options

The ‘Display By’ choice for the bar chart is also accessed via the grid settings link. This will bring up the 'Display and Column Settings’ popup. The ‘Display By’ options for the bar chart can be found at the top. You can select a standard a standard system information column to display the bar chart by.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FE4CKcpVkGDAPsENXu1kE%2F3-Bar-Chart-Standard-Data.gif?alt=media\&token=96f172c2-0f6c-40e2-b99f-bb9e69c33ee8)

The standard system information by which you can display the bar chart display is as follows:

1. **Action Type** – this shows the Action type, either as send email or as a manual Action.
2. **Assigned To** – this shows who the Action has been assigned to.
3. **Contract Name** – this shows the name of the contract.
4. **Last Updated By** – human/digital worker who last updated this item.
5. **Last Updated On** – datetime when this item was last updated by a human/digital worker. The datetime on which custom data field values are updated is stored in the Enate database and can be used for subsequent reporting.
6. **Owned By** – name of the user who currently has ultimate responsibility for the work item.
7. **Parent Process Name** – if this an Action, this shows the parent Case.
8. **Process Name** – the business process the work item is part of, e.g. ‘Maternity Request Process’.
9. **Queue** – the work Queue which Cases/Tickets/Actions get sent to based on their routing rule.
10. **Service Line** – the overall area of the business this work item runs under, e.g. ‘Payroll’.
11. **Service Provider** – the company delivering service for this work item, usually *your* company.
12. **Started By** – this shows who the Action was started by.
13. **Started By Method** – how the work began, e.g. incoming email, automatic schedule, manually, etc.
14. **State** – current state of the work item e.g. Running, Waiting for more Information, Resolved etc.
15. **Work Item Type** – i.e. Case, Action or Ticket.

#### Displaying by Custom Data Fields

If your system has been configured with them, you can also choose to select a custom data column to display the bar chart by.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fod7STW5rcZX5NIGr4whQ%2F3-Bar-Chart-Custom-Data.gif?alt=media\&token=29516b25-8cab-4713-827f-3d4d67594e4f)

Custom Data fields of the following types can be used to display information in the bar chart:

* Short Text
* List (simple list only)
* Checkbox

{% hint style="info" %}
Note: When you choose to display information in the bar chart by a certain item (standard system property or custom data field), that item will be added to the main grid display as an additional column.&#x20;
{% endhint %}

You can return to the system defaults by selecting 'Revert to Defaults' in the 'Display and Column Settings’ popup.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8hHqQwM05M2IdXr4QpzH%2F3-Revert-to-Default.gif?alt=media\&token=97fa8952-6bd9-4fcf-92a0-2a77bf6f205a)

Clicking on a bar name within the chart filters the grid to those results.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSDbPcZVyB1dAYpTVDnvZ%2F3-Click-on-Bar-in-Bar-Chart.gif?alt=media\&token=ec29df25-75f8-4cb6-b756-bd2da855b9c7)

Clicking on a specific R/A/G section within an individual bar filters the grid results down to the items in that state.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmvmixAU48ozxvBhVLSAR%2F3-Click-on-Bar-Section.gif?alt=media\&token=3c1d2f79-d2b8-42f6-9d1c-6172ee2bd53e)

## Grid

### Grid Icons

​Icons in the homepage grid let you know the state of the work item and give you high-level information about them. ​

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FhVOYA2ZutMrhxd7Ct8OO%2Fimage.png?alt=media\&token=2103e5fa-b8c3-46b8-9e78-73a80e307b72)

These icons also appear when you search for a work item in Quickfind.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MahRvmx8njS5t0lRKZA%2F-MahSAdtaLCqo34zt6HB%2Fimage.png?alt=media\&token=559c777f-d49f-40ed-ba52-edcf04952476)

They denote the following information:

| ![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fmxt8iUHIHKiwQKABG7HV%2Fimage.png?alt=media\&token=761537ca-f73e-4b1b-b65a-2e013d49ac3b)   | Task can be carried out by a Robot                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| ​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQul4DhnMDPYAEwjpg7ba%2Fimage.png?alt=media\&token=a1943362-6e7b-4c55-a485-c7d3cddbde22)​ | Robot Task – Needs Attention                                                                       |
| ​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fzi6ZCBn0GsC0x2El26MD%2Fimage.png?alt=media\&token=e1a88787-70ba-4b92-9e0b-3f75b4548db1)​ | New information has been received that hasn't been read yet.                                       |
| ​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDDvOxxSnvF22v4G9rZk0%2Fimage.png?alt=media\&token=85ea620f-189b-4c39-9d65-bb6d89ac1b66)​ | Case only : Case is in a problem State (i.e. needs attention)                                      |
| ​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fe31eDgel9pWOwcaRimw7%2Fimage.png?alt=media\&token=cbe8daff-d6de-4aad-88ad-5a123b76e685)​ | The Action is a Peer Review and it is in the "doing" stage.                                        |
| ​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQCMbQcmGnh5cLms0K1ZW%2Fimage.png?alt=media\&token=25ea1a1d-8c2b-42ae-923c-ade239d2f636)​ | The Action is a Peer Review and it is in either in the reviewing stage, or the review is complete. |

And they denote the following information about the status of the work item:

| ​​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvHf86QKzeyWwRXleXAH5%2Fimage.png?alt=media\&token=69ca1b27-61ea-43db-8364-fbfa4b64e2cb) | Work Item is in a state of **DRAFT**       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| ![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FLXIsvAcEmothnQf7vudQ%2Fimage.png?alt=media\&token=2af4bb3c-0076-466b-aa99-be582df365e1)​  | Work Item is in a state of **TO DO**       |
| ​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7hk1XGPpJ301ONMlC4LW%2Fimage.png?alt=media\&token=28361f06-6a9a-4fa1-ad17-bb133f78ede9)​ | Work Item is in a state of **IN PROGRESS** |
| ​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnehYSSj6FkTqSuJOetyg%2Fimage.png?alt=media\&token=ccb5fdda-059b-446a-8923-8927da23f9d6)​ | Work Item is in a state of **WAIT**        |
| ​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FF8Ws1IoNZDpIpE2E97L5%2Fimage.png?alt=media\&token=5862902e-2f90-4031-8f42-2e7b341d0018)​ | Work Item is in a state of **RESOLVED**    |
| ​![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpPGmqHGUy2siaJl8x1ld%2Fimage.png?alt=media\&token=783466c4-4f42-4c13-adf0-3e1102e300f3)​ | Work Item is in a state of **CLOSED**      |

You can find more information about the states a Ticket goes through [here](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/processing-a-ticket), the states of a Case [here ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case)and the states of an Action [here](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/processing-an-action).

### Grid Display Options

You are able to choose which work items you can see on the home page by selecting Work Inbox, Owned Work, Team Work Inbox, or Team Owned Work.&#x20;

Generally, if a work item is **assigned to you** or one of your team members, or it's in a state of **To Do or In Progress**, you'll see it in the **Inboxes**. **Everything else**, such as items in a Wait state, you'll find in the **Owned Work views**. The sections below go into this in a bit more detail.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MY5hE4PX__fQOXeN2My%2F-MY5hJWUHi5tHeXjzk2o%2FGrid-Inbox-Owned-Work-Views.gif?alt=media\&token=4ed8517c-2c51-43cb-ba49-c1b43c27b477)

{% hint style="info" %}
Note: The RAG volumes and bar charts are shown independently for each of these views, and so the displays of each will also change when you flip from one grid view to the other.
{% endhint %}

#### Work Inbox

The Work Inbox view shows you which work items are currently assigned to you.

#### Owned Work

The Owned Work view displays work items for which you are the Owner, rather than the current assignee.&#x20;

These are work items which may not necessarily be assigned to you (or anyone) right now, but for which you have longer-term responsibility for, e.g. Cases.&#x20;

Long term responsibility refers to the person responsible for the entire Case journey. This includes its Actions, the status changes of the Cases and its Actions, as well as the delivery of the Case.&#x20;

A Case can be owned by using Keep with me.

{% hint style="info" %}
Please note:

* Actions can only have an Owner if they are in a state of Pause e.g. states such as Wait for more information, Schedule for follow-up, etc.&#x20;
* There can be only one Owner of a Case at any one point
  {% endhint %}

#### Team Work Inbox

The Team Work Inbox view shows you all the work items which are assigned to you or one of your team members, or it's in a state of To Do or In Progress.

#### Team Owned Work

The Team Owned Work view shows you all work items that are owned by your Team i.e. Cases started by them, and Cases in states such as Wait for more information, Schedule for follow up, etc.

{% hint style="info" %}
Note: If you are a Team Member who prefers a focused view of your Inbox and you do not want to see the Peers and Queue work, then please ask your manager to switch off these views for you. Your view after login will then only show items in your Inbox / Owned Work.
{% endhint %}

See the table below for a more detailed breakout of scenarios:

| Work Item Context                                                                                                                                      | Where it displays                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| Any Case/Ticket/Action with an Assigned User                                                                                                           | <mark style="color:blue;">Inbox</mark>       |
| Any Case/Ticket/Action with the “More Information” flag set that is configured to use Queues                                                           | <mark style="color:blue;">Inbox</mark>       |
| Case with the “Problem” flags set that is configured to use Queues                                                                                     | <mark style="color:blue;">Inbox</mark>       |
| Any Action in a To do / In Progress state that is configured to use Queues                                                                             | <mark style="color:blue;">Inbox</mark>       |
| Any Ticket in a To do / In Progress state that is configured to use Queues                                                                             | <mark style="color:blue;">Inbox</mark>       |
| Any Case in a To do / In Progress state with an Owner that does not have the “More Information” or “Problem” flag set that is configured to use Queues | <mark style="color:green;">Owned Work</mark> |
| Any Case/Ticket/Action in a Wait State with an Owner where Queues are configured                                                                       | <mark style="color:green;">Owned Work</mark> |
| Any Case/Ticket/Action in a Wait State with an Owner where Queues are not configured                                                                   | <mark style="color:green;">Owned Work</mark> |
| Any Case/Ticket/Action in a Wait State without an Owner where Queues are configured                                                                    | <mark style="color:green;">Owned Work</mark> |
| Any Case/Ticket/Action in a Wait State without an Owner where Queues are not configured                                                                | Not displayed                                |
| Tickets placed in a Wait State at the same time as changing the Category where Queues are configured                                                   | <mark style="color:green;">Owned Work</mark> |
| Tickets placed in a Wait State at the same time as changing the Category where Queues are not configured                                               | Not displayed                                |
| Tickets already in a Wait State when the Category is changed where Queues are configured                                                               | <mark style="color:green;">Owned Work</mark> |
| Tickets already in a Wait State when the Category is changed where Queues are not configured                                                           | Not displayed                                |
| Cases automatically created by Schedule that no User has ever updated where Queues are configured                                                      | <mark style="color:green;">Owned Work</mark> |
| Cases automatically created by Schedule that no User has ever updated where Queues are not configured                                                  | Not displayed                                |
| Case/Ticket/Action without an Assigned User or Owner where Queues are not configured                                                                   | Not displayed                                |

### Grid Column Options

You can reorder the columns in the home page grid according to your preference. This column order will persist when doing multiple searches, as well as when you log out and log back in.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MY5hE4PX__fQOXeN2My%2F-MY5jvZLFaR-cJU80G3j%2FReordering-Columns.gif?alt=media\&token=fdf9ecb2-544c-47dd-8e4e-af30274a6451)

Column widths can be manually adjusted, and data can be sorted by a a particular column by clicking on the name in column header. Click it again to cycle though ascending, descending and no sort.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MY5hE4PX__fQOXeN2My%2F-MY5m0Cdm_Nw0euhiDSV%2FOrdering-column-data.gif?alt=media\&token=78449443-39d5-4e87-88fd-ed92c0661366)

#### Displaying Additional Grid Columns

You can display additional columns in the grid by selecting them from the standard columns section in the left hand side of the 'Display and Column Settings’ popup. The mandatory columns are shown in grey.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MY5m8Xg938bcciI2SiY%2F-MY5o7QJNEU4iEsBQ7hk%2FAdding-Standard-Columns.gif?alt=media\&token=6fe50027-e4b3-4a7b-a1aa-06583bc88364)

The list of standard system attributes you can display as grid columns which are available in the home page grids include :

1. **Action Type** – this shows the Action type, either as a send email or as a manual Action-type.
2. **Assigned To** – this shows who the Action has been assigned to.
3. **Contract Name** – this shows the name of the contract.
4. **Customer** – this shows the name of the customer.
5. **Due** – this shows when the Action is due.
6. **Has Been Reopened** - this shows if a work item has been reopened or not.&#x20;
7. **Initial Request On** - this shows the start date of the original request. This is particularly useful in situations where a further work item has been created from the original request (when a Sub Case is created, when a Ticket is converted into a Case, when a Case or Action gets reworked, when an Action is created via the 'Start Action' option or when a new linked work item is created), as it allows you to see the entire length of time it is taking to complete a request, as opposed to just the length of time an individual work item has been being worked on.
8. **Is Overdue** - this shows if a work item is overdue
9. **Last Email Received** - the date and time the last email of a work item was received
10. **Last Email Sender** - the details of the last person who sent an email relating to a work item. If the user is already in the system, this column will display their name, otherwise this column will display their email address.
11. **Last Reopened By** - if a work item has been reopened, this shows the person who last reopened the work item.
12. **Last Reopened On** - if a work item has been reopened, this shows the date when the work items was last reopened.
13. **Last Updated By** – human/digital worker who updated this item last time.
14. **Last Updated On** – datetime when this item was last updated by a human/digital worker. The datetime on which custom data field values are updated is stored in the Enate database and can be used for subsequent reporting.
15. **Original Requester Email** – the email address of the original requester of a work item, i.e. the person who initially raised the request.
16. **Original Requester Name** – the name of the original requester of a work item, i.e. the person who initially raised the request.
17. **Owned By** – name of the user who currently has ultimate responsibility for the work item.
18. **Overdue By Days** - this shows the number of days a work item is overdue by.&#x20;
19. **Parent Process Name** – if this an Action, this shows the parent Case.
20. **Parent Reference** – reference number of the work item which started this one, e.g. parent Case.
21. **Primary Contact Email** - the email address of the primary contact of a work item
22. **Primary Contact Name** - the name of the primary contact of a work item
23. **Process Name** – the business process the work item is part of, e.g. ‘Maternity Request Process’.
24. **Queue** – the work Queue which Cases/Tickets/Actions get sent to based on their routing rule.
25. **Reference** – the unique reference number e.g. 101342-T.
26. **Requester Email** - the email address of the requester of a work item
27. **Requester Name** - the name of the requester of a work item
28. **Resolution Method** - this shows how a work item was Resolved e.g. if has been done successfully, if it was resolved by a Case being launched, if it was resolved by Tickets being merged etc.
29. **Service Line** – the overall area of the business this work item runs under, e.g. ‘Payroll’.
30. **Service Name** – the service instance the work item runs under, e.g. ACME French Payroll.
31. **Service Provider** – the company delivering service for this work item, usually *your* company.
32. **Started** – this shows when the Action was started.
33. **Started By** – this shows who the Action was started by.
34. **Started By Method** – how the work began, e.g. incoming email, automatic schedule, manually.
35. **Status** - the current state of the work item e.g. In Progress, Waiting, Resolved etc.
36. **Status Reason** - this shows the reason the work item's status was updated e.g. if it was updated by a resource, if it was updated by Enate, if it has newly been created etc.
37. **Subject Email** - the email address of the subject of a work item
38. **Subject Name** - the name of the subject of a work item
39. **Ticket Category Level 1** – high-level categorisation of type of Ticket e.g. ‘Healthcare Request’.
40. **Ticket Category Level 2** – next level categorisation of type of Ticket e.g. ‘International Travel Coverage’.
41. **Ticket Category Level 3** – most detailed-level categorisation of type of Ticket e.g. ‘Eligibility Query’.
42. **Time Remaining When Paused** – the amount of time left before the due date at the point the item was placed into a paused state.
43. **Title** – a brief text description of the work item, often the subject of the original email.
44. **Wait Type** - if a work item is in a state of Waiting, this column will show the type of Waiting the work item is in e.g. Wait for more information, Wait Until, etc.
45. **Work Item Type** – i.e. Case, Action or Ticket.

You can also revert the column settings to default if you wish by selecting 'Revert to Defaults'.

#### Custom Data Columns

You can display additional custom columns in the Home page grid by selecting them from Custom Data Columns section in the right-hand side of the 'Display and Column Settings’ popup. Custom Data Columns are created in Builder, see [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration)for more information.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzZd6uppj0WZb0Sjc0ExS%2F3-Adding-Custom-Data-Columns.gif?alt=media\&token=fefc0a1d-fe03-4e40-924d-ffa4e33cd8e3)

### Grid Filtering

The number total at the top right of the grid show the total number of items in the grid and, when filtering, the number of filtered items from that total.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWqMXrK_ZvY1cj8JBqs%2F-MWqQeDBolIz3RczZGnP%2Fimage.png?alt=media\&token=e38adb97-d1e9-41c7-b616-95ef8e3b7310)

**In-grid filtering**

You can apply filters to all the standard and custom data columns on the grid by clicking on the filter icon next to the desired column title.

Your applied filters will remain when switching between your Work Inbox, your Team Work Inbox, your Owned Work and your Team Owned Work, as well as after the you log out and log back in.

You can clear the applied filters by clicking on the 'clear filter' icon, and all work items will be displayed again.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fr646hFImTu4Y4mudrZyN%2F3-Adding-multiple-filters-to-gri.gif?alt=media\&token=d6d10c02-408e-4be8-aad5-a659c7a16468)

You can also apply multiple filters to all the standard and custom data columns on your bot farm grid. The applied filters will remain when switching back to your Team Work Inbox.

### Searching the grid

You can also search the grid by using the free text search function.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6Win108NzG2LxggoUOpU%2F3-Text-Search-Grid.gif?alt=media\&token=47045051-7197-4329-9ae6-d0e3e3d0c91a)

### Copy/Paste into Excel

You can copy and paste information from the grid into an Excel spreadsheet by selecting the information you want to copy and using Ctrl C and Ctrl V.&#x20;

The information that is copied and pasted includes any applied filters. The column titles will automatically be copied and pasted as well.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXqQR7rLByurw2aS3mJ%2F-MXqScSUM-S7yJ_-RceP%2FCopy-Home-grid-to-Excel.gif?alt=media\&token=9dee0765-f48d-42d5-b68d-6c181b90a633)

You are also able to copy and paste all of the information in the grid by using Ctr&#x6C;**-**&#x41;.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXqQR7rLByurw2aS3mJ%2F-MXqT3gPj1DFd4W-3syY%2FHome-grid-ctrl-A.gif?alt=media\&token=e4be70d1-0f00-4377-b974-98f9c35d54dc)
