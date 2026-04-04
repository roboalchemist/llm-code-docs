# Enate Documentation

Source: https://docs.enate.net/llms-full.txt

---

# Hi, welcome to Enate Help

This is your one stop shop for learning about how to use Enate - it's packed full of useful explainers and videos to help you cover everything you need to know.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTU5NzkyMA==>" %}

Here's a breakout of the various sections of Enate's online help and what you'll find in them..

### :computer: Work Manager - For End Users

Work Manager is Enate's operations environment where service agents, Team Leaders and Operations Managers go to manage and deliver service. In this section you'll find lots of explainers and videos teaching you how to use the software day-to-day.

Enate's Work Manager Help is available in 9 languages including [Spanish](https://docs.enate.net/enate-help/v/espanol/), [French](https://docs.enate.net/enate-help/v/francais/), [German](https://docs.enate.net/enate-help/v/deutsch/), [Brazilian Portuguese](https://docs.enate.net/enate-help/v/portugues/), [Russian](https://docs.enate.net/enate-help/v/pusskii/), [Polish](https://docs.enate.net/enate-help/v/polski/), [Hungarian ](https://docs.enate.net/enate-help/v/magyar/)& [Romanian](https://docs.enate.net/enate-help/v/romana/).

{% content-ref url="work-manager/work-manager-2021.1" %}
[work-manager-2021.1](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1)
{% endcontent-ref %}

### :tools: Builder - For Configurers and Business Analysts

Wanting to get up to speed with mapping and running your business processes in Enate? Check out the Builder help section here.&#x20;

{% content-ref url="builder/builder-2021.1" %}
[builder-2021.1](https://docs.enate.net/enate-help/builder/builder-2021.1)
{% endcontent-ref %}

### :chart\_with\_upwards\_trend: For Analysts & BI Developers

Enate's Work Manager provides you with embedded reporting capabilities, driven by [Microsoft's Power BI reporting platform](https://learn.microsoft.com/en-us/power-bi/), which gives you lots of additional information at your disposal to gain new insights and support for your business operations. Check out this section to see the standard Reports available to you in the system.

{% content-ref url="work-manager/work-manager-2021.1/reports" %}
[reports](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/reports)
{% endcontent-ref %}

If you want to know more about the information available in the Data Warehouse for creating your own BI, check out this  Check out the BI section to view details of the Data Dictionary, with field data types and definition. This also highlights foreign and primary keys to join tables on.

{% content-ref url="enate-bi" %}
[enate-bi](https://docs.enate.net/enate-help/enate-bi)
{% endcontent-ref %}

&#x20;

### :zap: For Integrators

**Enate Integration Services** - Enate has teamed up with one of the leading iPaaS vendors [SnapLogic](https://www.snaplogic.com/) to offer iPaaS as part of the Enate platform for clients that do not already have their own iPaaS, or are seeking a more business user friendly solution.

{% content-ref url="integrations/enate-integration-services-powered-by-snaplogic" %}
[enate-integration-services-powered-by-snaplogic](https://docs.enate.net/enate-help/integrations/enate-integration-services-powered-by-snaplogic)
{% endcontent-ref %}

Additionally, Enate has an extensive library of APIs, Webhooks, and integration capabilities with RPA & OCR systems.  Check out the Enate Integrations section for information on this as well as Enate's extension points like Custom Card code.&#x20;

{% content-ref url="integrations/enate-integrations" %}
[enate-integrations](https://docs.enate.net/enate-help/integrations/enate-integrations)
{% endcontent-ref %}

### :rocket: For Implementers

Information for Enate implementation and Academy Training

{% content-ref url="implementation/enate-implementations-2" %}
[enate-implementations-2](https://docs.enate.net/enate-help/implementation/enate-implementations-2)
{% endcontent-ref %}


# Work Manager

In this section you'll ﬁnd lots of explainers and videos teaching you how to use Enate's Work Manager software to manage your business processes day-to-day.

## Work Manager Overview

Work Manager is a web-based, multi-page application used by members of the service delivery team to interact with Tickets, Cases and Actions running through managed business processes.

Users of Work Manager are service agents, team leaders, operations managers and executives. Work Manager provides a standard set of views for these users to carry out work.

Watch this video for a quick overview of Work Manager:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTYzMA==>" %}

### Browser Support

Work Manager is designed to support the following Browsers:

* Latest version of Chrome (at time of release)
* Latest version of Firefox (at time of release)
* Latest version of the Microsoft Edge, based on Chromium (at time of release).


# User Roles in Work Manager

Enate allows a granular level of granting access to people based on their role and business requirements. These settings are defined in the User Management section of Builder.

Every user has a Work Manager role assigned to them. The role has a number of access options configured for it which determine what they can see and do in Enate.

Enate provides two standard, pre-configured roles for Work Manager:

* **Team Member** - this is for Agent users who process Tickets, Actions & Cases and who report to a Team Leader. This role gives them access to work assigned to them, their team (people who report to the same Team Leader as they do) and work that is  in the Queues that they work out of, but has fewer levels of access than the Team Leader role.
* **Team Leader** - this is for senior members who manage a Team and oversee Queues. This role gives them access to set up and maintain their teams and Queues, to assign work to others, as well as to more advanced features such as creating customized reports.&#x20;

This article provides a full breakdown of access options for Team Member and Team Leader roles.&#x20;

If a standard role doesn't quite fit the bill, you can create custom roles that allow you to fine-tune levels of access to give users the exact combination of access levels they need.

Custom roles might be particularly useful in the following circumstances:&#x20;

* **Senior Team Members** - You may wish to create a custom role for your more senior team members which falls part-way between the standard 'Team Leader' and 'Team Member' roles, giving them access to some Team Leader-like features without needing to have them fulfil that role entirely.
* **Junior Team Members** - You may wish to create a custom role for your more junior team members which gives them access to some 'Team Member'-like features while hiding other aspects of the system until they gain more experience

You can also give some Work Manager users access to Enate's Builder application, for example so that they can view local processes. You do this by assigning them a Builder role, [see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-roles-and-feature-access).

Users are also able to view which roles their team members have in Work Manager - [clicking on a team member from the Team Bar](https://docs.enate.net/enate-help/work-manager/home-page/team-bar/team-bar-for-team-members#viewing-an-individual-user) will bring up their user profile which includes information such as their role title, its description (if one has been added), as well as a list showing which features that the user has access to.&#x20;

If you find yourself needing to change the levels of access for yourself or users in your team, speak to your system admin.


# Home Page

The Home page allows Team Leaders and Team Members to view the work for their area of business, i.e. Work Items sitting in their work Queues and with their Team Members (both human and robot).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mfs1xzVb6becGeegY9e%2F-Mfs21pgcyAbHsW6d0ci%2Fimage.png?alt=media\&token=47621cfd-6796-4b0c-8ce0-8c7e6132cc15)

On your Home page you will see:

* Work Items that are assigned to you
* Work Items that are assigned to your manager, i.e. the person you report to (if you have one)
* Work Items that are assigned to your peers (people managed by the same person as you)
* Work Items in a Queue that you are a member of / are a manager of

Additionally, as a Team Leader you will see:

* Work Items that are assigned to people you manage (i.e. people who report to you)
* Work Items that are assigned to people managed by people you manage (recursively down the hierarchy of manager relationships)
* Work Items in a Queue that you manage, even if you are not a member of it

Click [here ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/setting-teams-and-queues)to see how to set the users who report to you (i.e. your Team), and Queues which you manage.


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


# Team Bar - Viewing Your Team


# Team Bar for Team Members

On the right hand side of the [home page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/home-page) is the Team Bar.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY0Mg==>" %}

If you are a Team Member, the Team Bar shows you [your team](#my-team) and your [unassigned work](#unassigned-work).

## My Team

At the top of the Team Bar you can see the people in your team and, for each of them:

* The amount of work they have outstanding (number in centre of pie-chart)
* The due status of that work (i.e. Red/Amber/Green)
* Their current availability status (available or offline)

### My Team Display Options

#### Available / Offline Status for Team Members

You can see the availability status of your Team Members - so if they are online or offline.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MgfBV8LnrdZumBORMaw%2F-MgfFG1Te_-PwJ6QvY9g%2Fimage.png?alt=media\&token=0c8e2526-670b-42c0-93f8-7360588ee825)

The system tracks your active Enate browser session, and so is able to check if they are still logged into Enate.

{% hint style="info" %}
Note: if you do not log out properly, i.e. shut down the browser or machine directly without logging out of Enate, the system will display you as still online for the duration of the standard system timeout (usually 30 minutes).
{% endhint %}

An important point is that this available / offline status is for informational purposes only – it is not taken into account as part of any allocation rules - i.e. the ‘Who does it go to?’ settings.

You can filter the display of your team to show available / offline / all users.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FW0YAhiGG6Ak68PKX1VSa%2F4-Filter-team-members-by-availab.gif?alt=media\&token=5ffc7884-34f7-4e2a-9d3e-f9a7181454f1)

#### Sorting by work item status

You can sort your team members by work item status criteria including:

* Least / Most Work (Total)
* Least / Most Overdue (Amber)
* Least / Most Overdue (Red)
* Least / Most On Target (Green)
* You can use this to help identify resources which are stretched and other team member who you may be able to share work out among to help balance workloads.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7vBb1U5R3QsOslORRCYw%2F4-Sort-team-members-by-work-stat.gif?alt=media\&token=6d16c148-5211-4212-bc2f-b5f9550dbd37)

#### Searching for team members

Free text search also allows for you to search for individual users from the list.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fqg1p8a5iJJVK1TdjdnZ4%2F4-text-search-for-team-members.gif?alt=media\&token=bb11af2c-d8bb-4611-a654-177b7a7fd00c)

### Viewing an Individual User

Clicking on a team member from the Team Bar, will bring up their user profile. The grid filters down to show only work items currently assigned to that user.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FS3BxKRsngqHAeVKDEAuJ%2Fimage.png?alt=media&#x26;token=4b5bf704-0bec-4a8d-bd4f-30e4d12a9be4" alt=""><figcaption></figcaption></figure>

The homepage bar chart will be replaced to show the amount of work that is assigned to the user (the number in centre of pie-chart), as well as the due status of that work (i.e. Red/Amber/Green), You will also see the user's profile picture, their role title, its description (if one has been added), and if you click on the 'More about this role' link, you'll see a list showing which features that the user has access to.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpIK5wXGFjj7b12ab8KSu%2Fimage.png?alt=media&#x26;token=7e689989-6dd4-4c44-8284-69380dcba28e" alt=""><figcaption></figcaption></figure>

You can close the view and return to the standard bar chart view of all work items by clicking the 'X' icon.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjUMJMLkPu76w6eAkvKMf%2Fimage.png?alt=media&#x26;token=d86e8419-1ffc-40e6-93ed-e595be78da89" alt=""><figcaption></figcaption></figure>

## **Unassigned Work**

At the foot of the Team Bar you can see the amount of work which is sitting unassigned in the Queues you manage, grouped by Queue. This includes information about the amount of work in each Queue that is unassigned (the number in centre of pie-chart), as well as the due status of that work (i.e. Red/Amber/Green).

If you have unassigned work which is overdue – i.e. any red items in this section – you should be looking to deal with that situation.


# Team Bar for Team Leaders

On the right hand side of the [home page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/home-page) is the Team Bar.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsNAL5R8UnTrTYGwHA%2F-MWsNNDggWYNunA2CwOk%2Fimage.png?alt=media\&token=23e80e5d-6a0a-4a82-b965-3721e499e17b)

If you are a Team Leader, the Team Bar shows you [your team](#my-team), your [bots ](#bots)and your [unassigned work](#unassigned-work).

## My Team

At the top of the Team Bar you can see the people in your team and, for each of them:

* The amount of work they have outstanding (number in centre of pie-chart)
* The due status of that work (i.e. Red/Amber/Green)
* Their current availability status (available or offline)

### My Team Display Options

#### Available / Offline Status for Team Members

You can see the availability status of your Team Members - so if they are online or offline.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MgfBV8LnrdZumBORMaw%2F-MgfFG1Te_-PwJ6QvY9g%2Fimage.png?alt=media\&token=0c8e2526-670b-42c0-93f8-7360588ee825)

The system tracks your active Enate browser session, and so is able to check if they are still logged into Enate.

{% hint style="info" %}
Note: if you do not log out properly, i.e. shut down the browser or machine directly without logging out of Enate, the system will display you as still online for the duration of the standard system timeout (usually 30 minutes).
{% endhint %}

An important point is that this available / offline status is for informational purposes only – it is not taken into account as part of any allocation rules - i.e. the ‘Who does it go to?’ settings.

You can filter the display of your team to show available / offline / all users.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FW0YAhiGG6Ak68PKX1VSa%2F4-Filter-team-members-by-availab.gif?alt=media\&token=5ffc7884-34f7-4e2a-9d3e-f9a7181454f1)

#### Sorting by work item status

You can sort your team members by work item status criteria including:

* Least / Most Work (Total)
* Least / Most Overdue (Amber)
* Least / Most Overdue (Red)
* Least / Most On Target (Green)
* You can use this to help identify resources which are stretched and other team member who you may be able to share work out among to help balance workloads.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7vBb1U5R3QsOslORRCYw%2F4-Sort-team-members-by-work-stat.gif?alt=media\&token=6d16c148-5211-4212-bc2f-b5f9550dbd37)

#### Searching for team members

Free text search also allows for you to search for individual users from the list.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fqg1p8a5iJJVK1TdjdnZ4%2F4-text-search-for-team-members.gif?alt=media\&token=bb11af2c-d8bb-4611-a654-177b7a7fd00c)

### Viewing an Individual User

Clicking on a team member from the Team Bar, will bring up their user profile. The grid filters down to show only work items currently assigned to that user.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fcr8WuzqJf1vlPbf6ECDo%2Fimage.png?alt=media&#x26;token=7b2b6008-e430-424e-ac62-bf491d032d4c" alt=""><figcaption></figcaption></figure>

The homepage bar chart will be replaced to show the amount of work that is assigned to the user (the number in centre of pie-chart), as well as the due status of that work (i.e. Red/Amber/Green), You will also see the user's profile picture, their role title, its description (if one has been added), and if you click on the 'More about this role' link, you'll see a list showing which features that the user has access to.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNAVSY61Qw6Dkeib5oeTs%2Fimage.png?alt=media&#x26;token=23c29656-45f6-49ab-b322-aae8edba221a" alt=""><figcaption></figcaption></figure>

You can close the view and return to the standard bar chart view of all work items by clicking the 'X' icon.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSuKSwGQrGfs0EI4Jhs6Y%2Fimage.png?alt=media&#x26;token=518a29f6-122c-4132-9371-6b6171b48583" alt=""><figcaption></figcaption></figure>

If you find yourself needing to change the levels of access for yourself or users in your team, speak to your system admin.

## Bots

If you are a Team Leader you will also be able to see your bots in the Team Bar. This shows you any Robots which are available to work on items you manage / work with, grouped by Robot farm.

Each row displays a different robot farm, along with their Technology (e.g. UiPath, Automation Anywhere, Blue Prism etc.).&#x20;

The number of ‘bottable’ work items lined up for the robot farm will be displayed, as well as the estimated amount of work left available for the robot farm in minutes.

If any of the Robots in the farm are offline or unresponsive, a warning icon will be displayed.

Additionally, it's possible that some of the bottable work items for these bots are outside of this user's permissions. If that is the case then a warning 'i' icon and message will be displayed informing the user of this.

### Viewing an Individual Bot Farm

Clicking on a Robot farm in the Bots section swaps out the bar chart main display to show that group of robots AND filters down the grid results to show ‘bottable’ work items.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsNAL5R8UnTrTYGwHA%2F-MWsO99B2D8hVp0Wrm9K%2Fimage.png?alt=media\&token=847c593f-a241-47b7-87ab-7326e03eea75)

In this view, Team Leaders can:

* See the status of individual robots within the robot farm:
  * Idle - the bot is available for work
  * Offline - if your bot uses deep integration, such as UiPath orchestration synchronisation, an offline status means that your IT system can't connect with the bot. In this situation you would reassign the bot's work items to other resources. If your bot does not use deep integration, such as Blue Prism, an offline status means that your IT system hasn't connected with the bot for a certain amount of time.
  * Suspended – the bot’s average work is not within standard deviation, so it has been paused
  * Busy Integrated – the bot is busy working on a task that is has been assigned to
  * Busy Independent- the bot is busy working on a task that it has not been assigned to
* View the work currently being done by individual robots
* Filter down the view to an individual robot
* See how much work is remaining for the bots to do (both in volume, e.g. 20 items, and in how many minutes worth of work is remaining, i.e. how long we think it will take to complete all of those 20 items).
* The system can make an estimate of the amount of work left in minutes because we have an ‘estimated duration’ value configured in Builder for different Actions. The system simply totals the value of these for the Actions currently available for the robots to do.

The grid will show projected start and end times for each piece of work, colour-coding the projected end date to show it if will breach the due datetime – this helps the Team Leader determine if they need to add further human / robot resources in order to meet SLAs.

The view can be closed to return to the standard bar chart view of all work items.

**How does the system determine which work item to give a ROBOT when they send in a “Get more work" request?**

The system works by looking at all unassigned Action work items from all of the Queues the robot is linked to and for which the robot's farm is set as the relevant farm in the 'General Settings' configured for that action (the equivalent of Robot permissions), then from this list determines the one due soonest, and assigns the Action to the Robot.

**Exception**: If a robot is already listed as working on an Action and yet sends in a "Get more work" request to Enate, the system will send back a response to the Robot of that same Action - effectively reiterating that the bot should carry out that Action. The system will do this a total of 3 times if the robot continues to send such requests while still supposedly 'occupied', and on the next such request will take the Action off the robot, mark it to be allocated to a human rather than a robot, and will then proceed with the normal logic of assigning the robot the soonest due Action from the list of ones it can perform.

## **Unassigned Work**

At the foot of the Team Bar you can see the amount of work which is sitting unassigned in the Queues you manage, grouped by Queue. This includes information about the amount of work in each Queue that is unassigned (the number in centre of pie-chart), as well as the due status of that work (i.e. Red/Amber/Green).

If you have unassigned work which is overdue – i.e. any red items in this section – you should be looking to deal with that situation.


# Setting Teams and Queues

## Overview

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY0NQ==>" %}

As a Team Leader (someone who has people reporting to them in Enate), the Home page needs to know *who* reports to you and what Queues you are in charge of. These settings can be adjusted in the Queues page, which you can open from the navigation section.

If you have no data set up yet, the page will open in Edit mode by default. Otherwise, it will show the Queues that you manage (along with the people who are working out of that Queue), and the list of people who report to you, i.e. your Team.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYAQ2lRoEw8Y_10P5lE%2F-MYAWlRKHQxOSGYoqeYp%2FClicking-on-Queues.gif?alt=media\&token=16119f46-9415-474b-8971-0daec0380f16)

## Editing Queues <a href="#b-editing-teams-and-queues" id="b-editing-teams-and-queues"></a>

You can Edit these settings as follows:

* Add a Queue. You are also able to add yourself as a manager to a Queue. This includes Queues which may already be managed by a different Team Leader (you will now both be managers of this Queue).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZDSPDnHoOUgdNJdorl%2F-MZDSUUs_zpbmWACYJ8G%2FAdding-to-Queue.gif?alt=media\&token=7566cd64-dee3-4880-ae59-5a29920e8e28)

* Remove a Queue, i.e. unset yourself as the manager of a Queue.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZDSPDnHoOUgdNJdorl%2F-MZDTplYoyMbKyJG0F7-%2FRemoving-Queue.gif?alt=media\&token=1785a231-bf3d-4c35-8df1-506f919f723b)

* Add / remove Team Members to one or more of your Queues.
* Add and remove Robots to your Queues. You can add/remove all the robots (or just those selected) in a farm to a Queue at one time.
* Set a mixed resource Queue to ‘Strict mode’ - In Queues where there is a mixture of human and robot resources, switching on 'Strict Mode' sets any human users in the Queue as fall-back resources only, only receiving work from here if its robots are for some reason currently unable to carry out the work in the Queue.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY1MA==>" %}

### Queues with multiple managers <a href="#queues-with-multiple-managers" id="queues-with-multiple-managers"></a>

Queues can be set to have more than one manager.

Example: Consider Manager 1 and Manager 2 as two team leads where Manager 1 needs visibility on the Queue of Manager 2. Manager 1 can simply add the Queue of Manager 2 to his Queues page to have the visibility of the same Queue.

Click on the edit option and add the specified Queue where it shows that the Queue is managed by Manager 2. This does not remove managerial responsibility from the current manager.

If a Queue is managed by multiple people then the users that report to you are filtered under 'Managed by me' and the other users who report to the other person are filtered under 'Managed by others'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZDYYkSyV4Y2yK0YH1x%2F-MZD_LDGwCY8EsK3ZIVF%2FMultiple-Managers.gif?alt=media\&token=f50f0816-ae4b-48e7-80d0-eb10c60ba962)

## Editing My Team

You can add and remove Users to 'My Team'. When you are adding users to your team, you do so by building up a list of the users who report to you.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZDYYkSyV4Y2yK0YH1x%2F-MZDbGq8_QubgOjYLtTj%2FEditing-My-Team.gif?alt=media\&token=9dd2eb1e-126b-448d-a86e-af76874decb3)

{% hint style="info" %}
**A user can only report to one Team Leader**, so when you add a user to a team, you may be resetting who they report to – if they previously reported to a different Team Leader that will now be wiped and reset to you. They will no longer have that user report to them, and will not have visibility of the user (unless they are still in Queues that the Team Leader manages).
{% endhint %}


# Quickfind

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY1NA==>" %}

You can use Quickfind to search for people, work items, communications and files.

By default, Quickfind will search against all four categories of people, work items, communications and files, but you can focus down to searching just one of these categories by selecting from the left-hand dropdown in the Quickfind header.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FEw7bjav0kH5Mk6lQbkbl%2F5-Quickfind-intro.gif?alt=media\&token=e2dbdfae-6333-4d39-a526-51528e21d5ef)

## Searching for Work Items

You can search for work items (i.e. Tickets. Cases and Actions) by entering key words relating to them into Quickfind.

If you have many results, then you can choose to filter your search down further by choosing to search by Ticket, Case or Action specifically.&#x20;

Work item search results will display the reference, title, process name, work item status, due date (with Red/Amber/Green colour-coding), plus the name of the person to whom the item is currently assigned.&#x20;

Additionally, you can filter the search by start date using the slider provided, from Today through to Past Year, plus specific date ranges.

Hovering over a work item row in Quick find will display a ‘Take It’ icon. Instantly assign this work item to yourself by clicking on this icon.

Clicking on the work item will open it in a new tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPoFSvToTM7OlHM5uORDM%2F5-Quickfind-Work-Item.gif?alt=media\&token=21fc945e-5a73-4271-909b-f8fdf31b0ff8)

## Searching for People

You can search for contacts by searching for first name, last name, company and email address.

Additionally, further people-extended properties can be added to the system and all text/string properties can be searchable within Quickfind.  For example, you might have a 3rd party contact with the attributes ‘Country Name’ etc. which will be searchable in the Quickfind.

The criteria which can be searched against, e.g. ‘Employee Number’, are displayed as the records are returned in the Quickfind results, in the line underneath the contact name.

If you have many results, then you could filter it by clicking on ‘Contact’ or ‘Agent’. When you click on contact, the system will only show contacts with search criteria.

Clicking on a person will open the [Contact Activity page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page) where you can view current and historic activity - work items related to that person - all their communications, and start new work for them.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYAbzgkYvkHuG6fVaCl%2F-MYAevFYyG2clcqvWwoE%2FSearching-Contact.gif?alt=media\&token=97156af4-a757-47c7-93f6-442c848625b7)

{% hint style="info" %}
Note: You will only be able to see the email addresses and the Contacts belonging to the companies that you have access to. These settings are configured in Builder, click [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#external-contact-scoping)for more information.
{% endhint %}

### **Creating a new Contact Record from Quickfind**

If you are searching for a new contact which does not currently exist in the system, you can create a new contact from Quickfind itself. Navigate to the people search function in Quickfind and click on ‘add a contact’.

When you click on ‘add a contact’, the system will decode and auto-populate the first name, last name and email address. Once you fill in all the information and click on create, you will be taken to  the [Contact Activity Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page) of the new contact.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MbH-BYuK4VLPdtNwqfT%2F-MbHBB9sVuyT_nCkaTfK%2FCreating-a-Contact-from-Quickfin.gif?alt=media\&token=fe49d4ff-b5be-4aee-bbd6-b5aeee0ff1f3)

{% hint style="info" %}
Note: The contact email address must be unique in the system.
{% endhint %}

## Searching for Communications

You can search communications (i.e. emails, notes and Self Service communications) by entering key words from the email subject, body text or contact details (To, From, Cc, Bc), or key words from the note or Self Service communication you are searching for.

You can choose to filter you results even further by selecting the communication type i.e. incoming email, outgoing email, note, self-service comment by clicking on top icons.&#x20;

You can also use the slider to filter by received/sent date (from Today through to Past Year, plus specific date ranges).

Search results will be sorted by the date that the email was sent/received, with the most recent at the top.

Email search results will include details such as the To/From address (depending on whether the email was sent or received), an icon to indicate if the email was sent or received (if the email was sent from you or your team the icon will be green and if the email was received by you or a member of your team the icon will be blue), the email subject  and the first few lines of the email body, as well as the email sent/received time.

Note search results display the writer of the note, the first few lines of the note and when the note was written.

Clicking on the communication will open the work item which it is linked to in a new tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTxw0TNgqNAWHGnuWBdPP%2F5-Quickfind-Communications.gif?alt=media\&token=91164874-cb46-4c53-8109-6c9b72346b8f)

## Searching Files

You can use Quickfind to search for individual files or to search for a work item by searching for one of its files. Searching for files in Quickfind will search for both files that are directly linked to the work item AND files that have been attached to communications for the work item.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY1Ng==>" %}

The search results will be sorted by the date that the file was last updated on or when the email was sent/received if the file is a communication attachment, with the most recent at the top.&#x20;

Search results will include details such as the type of file (i.e. whether it was attached to the work item or to a communication), when the work item was last updated if the file is attached to a work item or when the email was sent/received if the file is a communication attachment, the reference number and title of the work item(s) the file is attached to and the communication subject if the file is a communication attachment.&#x20;

Clicking on the file will download a copy of it and clicking on the work item reference will open the work item the file is attached to in a new tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FWvrylgS1DItjlnBRQzZg%2F5-Quickfind-Files.gif?alt=media\&token=5f7a11c6-d0e5-4609-b500-8cd7b9d321da)

{% hint style="info" %}
Note: You will only be able to see the files and work items that you have access to to based on the permissions you have. These settings are configured in Builder, click [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-groups)for more information. You will also not be able to search for files or communication attachments that have been deleted.

Additionally, to mitigate performance issues Quickfind will not return search results for:

* Communication attachments that start with 'Mime Attachment'
* Communication attachments that start with 'MIME-Attachment'

You can still search for the text mime attachment, but the only results will be from work item files. You can still search for 'mim' which may return other results.

Also note that the system uses 'start with' logic for searching for files where it adds a wildcard to the END of search texts. This means that if you are searching for a file called 'Invoice Processing.docx', searches for 'processing' would not find the file, but searches for 'invoice' would.
{% endhint %}


# Quickfind Searches with Custom Data Fields

You can search for work items and their emails using focussed ‘search this value in this field’ on the work item. This is achieved by prepending the search with predefined search code. Before typing anything into Quickfind, the dropdown displays all short codes available in the system, and the field they relate to.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsLjW1By6N--0f-8Eq%2F-MWsMRJGX8fmcXWOy7Cy%2Fimage.png?alt=media\&token=19356388-3d63-4af9-97d6-dca737040ef1)

To search against a field, enter the short code and the desired value e.g. hq:Laptop

This will return work item (Ticket/Case/Action) and communication results where this field has this value:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsLjW1By6N--0f-8Eq%2F-MWsMVtK6fjKs0HtjIsC%2Fimage.png?alt=media\&token=78049389-2913-4ef9-ad5d-88f7777ca23e)

### Using Quotes to search for entire phrases <a href="#using-quotes-to-search-for-entire-phrases" id="using-quotes-to-search-for-entire-phrases"></a>

You can put quote marks around your search value to search for an entire phrase as the field value you want to find e.g.:  bn:“entire phrase”

You can also use this approach to search for phrases with general free text searching, i.e. even when you are *not* searching against a custom field with a prepended short code.


# How Quickfind works - specifics

Some further explanation of how Quickfind works: There are three different kinds of searches going on in parallel when you are entering Quickfind search data:

**1) Specific search against reference number**. This is based upon recognizing a known format of the system’s refence number for work items and then returning results related to Tickets, Cases, Actions which have that reference. You can just type the reference, e.g. ‘40308-T’ and the system will recognize it as a reference. You don’t need to enter a leading short code.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjA3OoT2nCAxbsV8dQa%2F-MjA65fGB-pu1C0DIa9Z%2Fimage.png?alt=media\&token=8b85eab4-af1b-4fa3-bd0c-3e480f5e91c9)

Note: There's also support for certain formats of your own internal reference numbers. Specifically, Quickfind will recognize text  strings made up of a series of digits and a '.' decimal point marker, up to 10 digit characters, i.e. with the format 'NNNNN.NNNNN', no matter where the '.' character appears within this string.

**2) Custom Data Field** searches. As described above. The system will know to do this kind of search when you enter a known short code, e.g. ‘FN: ’. The search will be for a field which contains the specific value you enter. See further note below on Wildcards.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjA0xUKb944CbFdMH4z%2F-MjA36E-nGuNRGMyCEXG%2Fimage.png?alt=media\&token=d586e10b-2088-4540-9020-4efb777cc07c)

**3) Free text searching for work items, communications and people** against anything else you enter which doesn’t conform to the first two types of recognized data. The system free text searches the individual words against various system attributes of work items, communication and people, e.g. work item title, email subject and body.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjA0xUKb944CbFdMH4z%2F-MjA3Jbz3yVxTkjjN9uA%2Fimage.png?alt=media\&token=8ce6f61c-4dbb-4741-97c1-63b14de261e6)

**4) 'Start with' searching for files** - the system uses 'start with' logic for searching for files where it adds a wildcard to the END of search texts. This means that if you are searching for a file called 'Invoice Processing.docx', searches for 'processing' would not find the file, but searches for 'invoice' would.

## Wildcards for open searching <a href="#a-wildcards-for-open-searching" id="a-wildcards-for-open-searching"></a>

When searching, the system will add a wildcard to the END of search texts, but not the start.

For Custom Data Searches specifically, an example of behaviour would be:\
searching for e.g. “p:John Smi” would find items with the value “John Smith” in a field ‘person’ but searching just for “p:Smith” would NOT find it.

In short: With Custom Data Field searches, we’re searching for the precise value of the field, or the start of the value. Free text searches aren’t *quite* the same as this, since a free text search will try to match against each individual word within a text value to get a match, rather than the value as a whole.

Wildcards are added to the end of reference number searches also.

### **Running Wildcards while typing** <a href="#running-wildcards-while-typing" id="running-wildcards-while-typing"></a>

While you are typing in Quickfind, the system will wildcard search against the very last word, e.g. if you’re free text search typing: "John return prio", the system will wildcard the last word and would also bring back results with e.g. ‘priority’.

Once you’ve pressed the space bar the system will conclude you’ve finished typing that word and will search against it without a trailing wildcard.

## Other search terms ignored <a href="#b-other-search-terms-ignored" id="b-other-search-terms-ignored"></a>

In order to retain system performance, the following are ignored from searches:

* Words of 1 to 2 characters.
* Words in the system 'Stop List'. These are standard common words such as ‘and’ ‘the’, ‘me’ etc., which would otherwise return too many results. Please see here for the [full stop list of words which are ignored in searches](https://docs.enate.net/enate-help/work-manager/appendix/search-terms-ignored-further-details#stop-list) (in Quickfind and indeed in any other system searches).
* Specific characters which are set to be ignored, e.g. “\*”, “?”, “@” etc. in Quckfind specifically. Please see here for a [full list of the characters which are ignored](https://docs.enate.net/enate-help/work-manager/appendix/search-terms-ignored-further-details#characters-ignored-in-quickfind). This will mean for example that when searching for customer.com in Quickfind, the words 'customer' and 'com' would be searched for. As such, it’s recommended to place such word combinations in quotes to search for them as a specific phrase - i.e. searching for “customer.com” will likely bring back the results you are looking for.&#x20;

## Further things to note for Quickfind&#x20;

Quickfind is a text-driven search. Entering dates in the text strings may bring back inconsistent results. Use “quotes” where possible if such searching is necessary to help the search look for entire strings of characters such as "search for where this entire string occurs".&#x20;

Use the date sliders to search for results in specific date ranges.&#x20;

When searching for multiple words, the search will be using an ‘AND’ logic rather than ‘OR’, i.e. bring back items with 'Apple' AND 'Banana' AND 'Pear'.&#x20;

## Specifics of Searches against Work Items vs Emails&#x20;

It’s important to note that Quickfind performs three independent searches,&#x20;

* one for for work items (Cases, Actions, Tickets),&#x20;
* one for the Emails that may relate to them, and&#x20;
* one for people. &#x20;

An effect of this can be that if you are e.g. searching against a combination of three words, e.g. 'apple' and 'banana' and 'pear', Quickfind will return results of any work items where all three words occur, and separately any emails where all three words occur. Situations where two of the words appear in the work item, and the third only in an associated email, would NOT be brought back by either search.&#x20;

The specific attributes which the work item searches are performed against are as follows:&#x20;

* Work Item Reference&#x20;
* Title&#x20;
* Customer Name&#x20;
* Supplier Name&#x20;
* Contract Name&#x20;
* Service Name&#x20;
* Service Line Name&#x20;
* Process Type Name&#x20;

The specific attributes which the Communications searches are performed against are as follows:&#x20;

* Email Title&#x20;
* Email Body&#x20;
* Email Addresses (From, To, CC, BCC)&#x20;
* Internal Note Body (for notes added in Enate / Self Service).&#x20;


# Managing Contacts

There a numerous ways of creating and managing contacts in Enate. Watch this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY2MQ==>" %}

{% content-ref url="managing-contacts/adding-editing-and-deleting-contacts" %}
[adding-editing-and-deleting-contacts](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/adding-editing-and-deleting-contacts)
{% endcontent-ref %}

{% content-ref url="managing-contacts/contact-management-page" %}
[contact-management-page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page)
{% endcontent-ref %}

{% content-ref url="managing-contacts/contact-activity-page" %}
[contact-activity-page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page)
{% endcontent-ref %}

{% content-ref url="managing-contacts/contact-tags" %}
[contact-tags](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-tags)
{% endcontent-ref %}

{% content-ref url="managing-contacts/contacts-card" %}
[contacts-card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card)
{% endcontent-ref %}


# Adding, Editing and Deleting Contacts

## Adding Contacts

External contacts can be created in Enate in several ways.

### **1) Automatically from an incoming email**

The Enate system can be set to automatically create new external Contact records when incoming emails arrive which contain new email addresses if the ['Enable Automatic Contact Creation' setting is set to ON in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation).

The system will auto-populate the first name and last name of the contact based on the email display name. More specifics on this:&#x20;

* If there is a space in the email display name, anything before the first space will be used as the contact's first name and anything after the last space will be used as their last name. For example, if the email display name is 'John Smith' then the contact's first name will be auto-filled as 'John' and their last name will be auto-filled as 'Smith'.
* If there is a comma in the email display name, anything before the first comma will be used as the contact's last name and anything after the comma but before the space will be used as their first name. For example, if the email display name is 'Smith, John' then the contact's last name will be auto-filled as 'Smith' and their first name will be auto-filled as 'John'.
* If the system can't auto-fill the first name and last name with confidence, then the contact will be auto-created without a first and last name and the user will be prompted to fill this themselves when they submit the work item.

Additionally the [company set](#company-name-external-contact-scoping) to an auto-created contact will depend on the [contact scope setting in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#contact-scope). If it's set to 'Global', or 'Global and Local', the auto-created contact will have a Global scope, i.e. not linked to any specific company.  If it is set to 'Local', the auto-created contact will be created under the company that the related Work item exists under.

### **2) Adding an individual contact from the Contact Management page**&#x20;

You can add contacts from the [Contact Management page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page) by clicking on the Create Contact icon and filling out the details for the contact in the resulting popup.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FK62ZZNAWwA6Gs8trMXXj%2F7%20Adding-Contact-from-Contact-Mana.gif?alt=media&#x26;token=d4a08dc8-4439-4fbb-a257-a8e4a72fec07" alt=""><figcaption></figcaption></figure>

### **3) Importing contacts to the Contact Management page from an Excel template**

You can import a list of contacts from an Excel spreadsheet in the [Contact Management page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page). A template is provided and the template is supported in all of the languages that Enate offers.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtwXbX4m1KzyOayzQnRHh%2F7%20Bulk-Adding-Contacts.gif?alt=media&#x26;token=f67af277-5f68-49e3-8a46-a64fd9aacaa6" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
It is mandatory to fill in the email address when importing Contacts from an Excel template. If you don't specify a company, the contact will automatically be set to global. See here for more information about [company scoping](#company-name-external-contact-scoping).
{% endhint %}

### **4) Adding a contact from Quickfind**

If you are searching for a new contact which does not currently exist in the system, you can create a new contact from [Quickfind ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/quickfind)itself. Navigate to the people search function in Quickfind and click on ‘add a contact’.

When you click on ‘add a contact’, the system will decode and auto-populate the first name, last name and email address. Once you fill in all the information and click on create, you will be taken to  the [Contact Activity Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page) of the new contact.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MbH-BYuK4VLPdtNwqfT%2F-MbHBB9sVuyT_nCkaTfK%2FCreating-a-Contact-from-Quickfin.gif?alt=media\&token=fe49d4ff-b5be-4aee-bbd6-b5aeee0ff1f3)

{% hint style="info" %}
Note: The contact email address must be unique in the system.
{% endhint %}

### **5) Adding a contact from the Contacts Card of a Work Item**

You can also create a new contact from the [contacts card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card) a work item. When you search for a user in the contacts card that does not exist in the system, you can create a new contact by clicking on the ‘Create Contact’ option and filling in the contact's details.

If you have written the email address for the contact, the system will decode and auto-populate the first name and last name of the contact. Once you fill in all the information and click on create contact, the system will redirect you back to the work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0LlSloVJ3b9h0UndDyZ9%2F7-Create-Contact-from-Work-Item.gif?alt=media\&token=fe7d24c4-1b2b-4f38-a480-524d59f6e5fa)

{% hint style="info" %}
Please note that if you create a new contact in test mode, that contact will only be available for running test packets in the system.
{% endhint %}

## Automatic vs Manual Contact Creation

You can see if an external contact has been automatically created by the system or manually created by a user by looking at the 'Auto-Created' column in the [Contact Management Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/contact-management-page#b-configuring-grid-settings).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fe7d4RTbYmrBWAIk5QaEz%2Fimage.png?alt=media\&token=513bd818-d217-42d4-9c2d-8e6f29ccea4f)

{% hint style="info" %}
Please note that once a contact that auto-created has had edits made to it, it will no longer display as an auto-created contact in the 'Auto Created' column of the Contact Management Page.
{% endhint %}

## Company Name - External Contact Scoping

Depending upon how it has been configured in Builder, you will have various options when assigning a company to an external contact:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4e1NkPn732m2IQnJpK6P%2F7-Company-Scope.gif?alt=media\&token=58472a1a-c708-408d-b6ca-9041e4aa0b3a)

* **All Companies/Global**&#x20;
  * Setting the company to this means that external contact can create and access work items for all companies.
  * It also means that work manager users are able to search for other all external contacts on a work item.

{% hint style="info" %}
Please note that this setting is only available if the External Contact Scope has been set to 'Global' or 'Global and Local' in Builder. See [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#contact-scope)for more information.
{% endhint %}

* **A particular company (local)**
  * Setting the contact scope to a particular company means that external contact will only be able to create and access work items for that particular company that the external contact has been associated to.
  * Users will also only be able to add a Contact to a Packet API if the Contact is in the same Company (or is in an umbrella Company).

{% hint style="info" %}
Please note:&#x20;

1. It is only possible to change the associated company of an external contact from All Companies/Global to a particular company (local) if the external contact is not associated with work items from multiple different companies. You can change this by reassigning the Contact on a work item.&#x20;
2. To scope external contacts to Global/All Companies the Company column in Bulk Upload file should be left blank so by default the contacts will be scoped to Global.
3. The company set to an auto-created contact will depend on the contact scope setting you have set. If it's set to 'Global', or 'Global and Local', the auto-created contact will have a Global scope, i.e. not linked to any specific company.  If it is set to 'Local', the auto-created contact will be created under the company that the related Work item exists under.
   {% endhint %}

### Impact of Global / Local Scoping on linking Contacts to a Work Item

{% hint style="warning" %}
Please note that if an External Contact is scoped locally (i.e. is linked a specific Company), you cannot add them as a contact for a work item which exists within another company.  This is also true for Agent accounts (which must *always* exist under a specific Company). ONLY Globally scoped External accounts have the flexibility to be linked as contacts to work items in any Customer.
{% endhint %}

## Editing a Contact

To edit a contact, go to the [Contact Management page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page) and double click on the contact to bring up the Edit Contact popup.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5KzvJfKILnLTcBggLbMR%2F7-Editing-a-Conact-in-Contact-Ma.gif?alt=media\&token=96c83c98-057d-42f9-b311-93f2fdd41cf7)

You are also able to bulk edit the company, time zone, office location, preferred language and default tag of your contacts by selecting on the contacts' tick boxes - click on the Edit button which will appear to display the Bulk Edit popup. Set details as desired and hit Confirm to save bulk changes.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FxKdZIM6sgHA9p4VcRwN9%2F7-Bulk-Editing-Contacts-in-Conta.gif?alt=media\&token=7c70b227-0e28-48a7-8735-0644bd1e0123)

## Deleting a Contact

To delete a contact, go to the [Contact Management page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page) and click on the contact's tick box and the delete button will appear. You are able to delete multiple contacts at once.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4jCq5IAIW63mMiAcyeke%2F7-Deleting-Conacts-from-Contact.gif?alt=media\&token=9fad9700-bc29-4872-8f12-0b28e6f78c49)

## Contact Scope vs. Permissions

It is important to take your user permissions into account when understanding which Contact records you are able to see, depending on the Global / Local scope setting which has been made in Builder:

{% hint style="info" %}
**Please note:** \
**- Locally-scoped contacts are visible to you in if you have permissions specificallly on that contact's company, or parent companies. If you don't have such permissions, you will not be able to see the contact record.** \
**- Global contacts are visible to all users.**
{% endhint %}

## Creating Contacts in Test Mode

Enate supports the creation of separate Contact records in Test Mode, i.e. any contact records you create in Test mode will be accessible only to Test Mode users (and contacts created in live mode will be accessible only to Live mode users). This helps to ensure that emails from test work items are not accidentally sent to production users, and vice versa.

### Warning - Do Not Use Production Email Addresses when creating Test Contacts

{% hint style="warning" %}
**IMPORTANT:** Do NOT create Test Contact records using information (specifically email address) for people you will be using in normal production. **If you create a Contact record while you are in Test mode this will be created as a Test Contact, and ALL emails arriving into the system from that email address will create a Case/Ticket in Test Mode.** This would result in incoming production emails creating work test work items which would not be visible by production users.

If you have created a production Contact record as a Test Contract record in error, you should edit the Test contact by changing the email address, then switch back to normal production mode to create the desired normal Contact record.
{% endhint %}


# Contacts Page

## Overview

The Contacts Page is where you can view and manage all of your external contacts in one place.&#x20;

{% hint style="info" %}
Note: you will only be able to access the Contact Management Page if you have been set up with the relevant permissions in Enate Builder. See [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/service-agents)for more information.
{% endhint %}

You can access the Contact Management page from the Navigation link. Your contacts and their information will be displayed in a table.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FRT2L7FCObnAbFTbghgxd%2F7-Clicking-on-Contact-Management.gif?alt=media\&token=19cebc16-9cc1-44fe-a8c1-577bd2368ac1)

{% hint style="info" %}
Note: Access to this Contacts page is not switched on for standard Team Member and Team Leader Roles. To give users access to this feature, a [Custom Role](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-roles-and-feature-access) must be created via the User Management section of Builder, with the 'Contacts' option switched.
{% endhint %}

Clicking on the first name link will open the [Contact Activity page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDE53wG3bR5yR69h1nPBR%2F7-Clicking-on-Contact-Activity-P.gif?alt=media\&token=b56374f6-2fde-4742-a46b-b8dddb604ea3)

## Adding Contacts <a href="#b-configuring-grid-settings" id="b-configuring-grid-settings"></a>

### **Adding an individual contact**

You can add contacts from the Contact Management page by clicking on the Create Contact icon and filling out the details for the contact in the resulting popup.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fxu9D8Q0P7Pio9LhTtXhf%2FAdding-Contact-from-Contact-Mana.gif?alt=media\&token=0d4ba96f-dbe6-4be5-b4e5-d0dc24945a39)

### **Adding multiple contacts**

You can import a list of contacts from an Excel spreadsheet in the Contact Management page. A template is provided and the template is supported in all of the languages that Enate offers.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FYwUSYqvgFmw6H5LcK7Ml%2FBulk-Adding-Contacts.gif?alt=media\&token=3d5b741e-f066-4a20-a4b3-d31fe3a42cd9)

{% hint style="info" %}
It is mandatory to fill in the email address when importing Contacts from an Excel template. If you don't specify a company, the contact will automatically be set to global. See here for more information about [company scoping](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/adding-editing-and-deleting-contacts#company-name-external-contact-scoping).
{% endhint %}

## Editing a Contact

To edit a contact, go to the Contact Management page and double click on the contact to bring up the Edit Contact popup.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5KzvJfKILnLTcBggLbMR%2F7-Editing-a-Conact-in-Contact-Ma.gif?alt=media\&token=96c83c98-057d-42f9-b311-93f2fdd41cf7)

You are also able to bulk edit the company, time zone, office location, preferred language of your contacts by selecting on the contact's tick box and the edit button will appear.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FxKdZIM6sgHA9p4VcRwN9%2F7-Bulk-Editing-Contacts-in-Conta.gif?alt=media\&token=7c70b227-0e28-48a7-8735-0644bd1e0123)

## Deleting a Contact

To delete a contact, go to the Contact Management page and click on the contact's tick box and the delete button will appear. You are able to delete multiple contacts at once.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4jCq5IAIW63mMiAcyeke%2F7-Deleting-Conacts-from-Contact.gif?alt=media\&token=9fad9700-bc29-4872-8f12-0b28e6f78c49)

## Adjusting Grid Settings <a href="#b-configuring-grid-settings" id="b-configuring-grid-settings"></a>

You can choose which columns to see by by clicking on the cog icon and selecting from your list of Standard Columns.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSkexA7ZDE9RLF6IFhzLX%2Fimage.png?alt=media\&token=d1aa85d7-e634-4bb3-9162-f686f7c4d35d)

The Auto-created column option lets you see how external contacts have been created - if they have been created automatically or manually. Please note that once a contact that has been auto-created has had edits made to it, it will no longer display as an auto-created contact in the 'Auto Created' column of the Contact Management Page.

You can add custom columns to the grid by clicking on the cog icon and selecting from your list of Custom Data Columns. Custom Data Columns are created in Builder (click [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration)for more information). Fields of all data types can be created with the exception of Table fields and Long Text fields.

You can sort the table by alphabetical order for a column by clicking on that column's title, and you can go back to the original selection of columns by clicking 'Revert to Defaults'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZVCMoLu8X26i9vuvgkYA%2F7-Sorting-Contact-Management-Pag.gif?alt=media\&token=951e097b-1902-43da-8060-b2cdaec229c7)


# Contact Activity Page

The Contact Activity Page displays the activity details for an individual service recipient.&#x20;

You can navigate to the Contact Activity page via:

**1. Quickfind** – clicking on a user in [Quickfind](https://docs.enate.net/enate-help/work-manager/quickfind#searching-for-people)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEeZvyo3kK3CdIt5hu%2F-MYEg6F9sJEf7DZGHI3u%2FQuickfind-to-Contact-Activity-Pa.gif?alt=media\&token=b757bf9c-9ac1-4d31-8ef8-932354634fec)

**2. A Work Item** – clicking on a contact in the [contacts card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card) of a work item

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYEeZvyo3kK3CdIt5hu%2F-MYEh5SNyUu3ZxSzpsVL%2FWork-Item-to-Contact-Activity.gif?alt=media\&token=245c922f-6aa9-495e-bdf9-c896129e8358)

**3. The Contact Management Page** – clicking on the first name of a contact in the [Contact Management Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-management-page)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYAf86bhlx18jwx2Lze%2F-MYAirfF8i7EXaVMTFQZ%2FClicking-on-Contact-Activity-Pag.gif?alt=media\&token=173bcab8-e7f1-440c-ac3e-76834bdff5c8)

Once you are on the Contact Activity Page, you can see the contact's details on the right-hand side and update them as needed.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNZnz1TsbkpPn6sEQpHKA%2F7-CA-Edit-Contact-Details.gif?alt=media\&token=28c0e6ec-343c-493e-b26e-3e8a1bb61b77)

Clicking on the 'Work Items' tab lets you see all work items which relate to the contact. Each work item is shown as a card with data about it like reference, title of work item, due date, assignee, queue, and state. Work Items can be opened for further details by clicking on reference and title. Running items are displayed by default, completed work items can also be displayed.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F03xAWQB3Tq3w7kXCK6id%2F7-CA-Page-Work-Items-Tab.gif?alt=media\&token=b034fc8b-79d5-4d35-a892-2577465968aa)

Clicking on the 'Comms' tab lets you see communications (emails, notes) relating to the user and the work items relating to them. You can search for specific communications here too.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnxEVJoJuzV3xmGB0i3Iv%2F7-CA-Page-Comms-Tab.gif?alt=media\&token=430f507c-42fb-4825-bf01-5059bfac8b26)

You can also start a new piece of work for the contact from the Contact Activity Page. Starting a new work item from the Contact Activity Page will automatically assign the contact as the Primary Contact, Requester and Subject on the work item, and if they have a Default Tag set, they will be tagged as this as well on the work item. Note that when launching a Ticket, the 'Send Automated Emails' option is automatically set to off.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoGSKsPPuKtznH8MJa2iR%2F7-CA-Page-Start-New-Work-Item.gif?alt=media\&token=0f2fa703-a49b-4337-bed1-4a36ab95e544)

{% hint style="info" %}
The work items that you can start from here depends upon if the work items have been [configured to be startable from the Contact Activity Page in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/service-matrix-screen/adding-a-new-ticket-case-to-a-service#c-opening-editing-setting-a-ticket-or-case-live), which [company the contact has been scoped to](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/adding-editing-and-deleting-contacts#adding-contacts) when it was created in Work Manager, and which [company you as a user have been scoped to](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/service-agents) as well.
{% endhint %}

You are able to copy the user's name by clicking on the copy button on the tab:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsG1AJE9JavfmnfBfP%2F-MWsG9PZfYfiC5OZEi6Z%2Fimage.png?alt=media\&token=e0e01f23-fc2b-405d-930d-37f23915f1e9)


# Contact Tags

Contact tags are used to link contacts to work items.

## System-Default Tags

The system-default Contacts Tags that are available are:

* **Primary Contact** – the main person you are dealing with for this query. There can only ever be one Primary Contact for a work item. This is mandatory for a Ticket. Depending on Case configuration in Builder, this may or may not be mandatory for a Case (if set as mandatory for Case type, is also mandatory for that Case’s Actions).
* **Original Requester** - the person who initially raised the request. There can only ever be one Original Requester for a work item, and it is independent to the 'Requester' tag. The original requester will be either automatically set in the situation where a valid contact sent in the email that started the work item, or the first person who gets manually set as the ‘requester’ will be promoted to ‘original requester’. The Original Requester tag cannot be changed once it has been set and you cannot remove the contact tagged as the original requester from the work item.
* **Requester** – the person requesting the query. There can only ever be one Requester for a work item. This is mandatory for a Ticket. Depending on Case configuration in Builder, this may or may not be mandatory for a Case (if set as mandatory for Case type, is also mandatory for that Case’s Actions).
* **Subject** – who the work item is about (this may be neither of the above). There can only ever be one Subject for a work item.

Very often all three will be the same person. If you tag another contact as any of these system-default relationship types, the tag will be removed from the previous contact - as there can be only one holder of the system-default contacts in one work item.

When you manually add the first contact to a work item they will be set as the Primary Contact, Requester and Subject by default. You can manually reassign these tags to other users afterwards.

* CCs – any further contacts which can be copied on any correspondence. When a contact is tagged only as ‘CC’, it will be displayed in the separate CCs section (hidden until any CC-only contacts exist on the work item.

## Setting additional Default Tags on a Contact Record

In addition to the system-default Contact Tags (Primary Contact, Subject, CC, Requester), you can add a further default contact tag to a contact record to make using contact tags on work items faster and easier.&#x20;

Example: If you know that 'Jane Smith' is always going to be the Broker or any work item you add them to as a contact, you can give Jane's Contact record a default tag of 'Broker' so it gets auto-populated for her in the work item - rather than you having to manually set this tag value each time.

The Default Tags list available to choose from is set in Builder in the [General Settings >> Contact Tags](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags) section. &#x20;

You can set this Default Tag whenever you add a new contact into the system.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FcIJqqZIZBtMkAQf7AMzo%2Fimage.png?alt=media\&token=f611c6da-530a-4210-a855-2cb31d205937)

You can also add the tag to existing contacts and edit the Default Tag set to a contact via the Contacts page.

The Default Tag attribute is also available to edit in bulk, i.e. you can set this for multiple contacts at one time - simply select a number of contact records from the Contacts page grid and click on the Edit button to access the Bulk Edit popup.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1vGyg20nHkJq744dxTq2%2Fimage.png?alt=media\&token=e6094bcc-5d65-4af9-98a7-9f8c7c40785c)

### Default Contact Tag behaviour if set not to 'Allow Multiple'

If a specific tag value has not been set to 'Allow Multiple', only one contact in a Work Item is allowed to have the value. Example: it may be that there can be only a single 'Broker' contact for Ticket. This obviously impacts default tagging if two contacts with the same 'must be unique' Default Tag get added to a work item, either manually or automatically. In this scenario the system will allocate the Default Tag to only one contact (and therefore remove the Default Tag for the other contacts). The system will allocate to the Contact already tagged with an existing *other* tag value, in the following priority order.

* Primary Contact
* Requester
* Subject
* CC
* Any other contact on the work item

### **Additional notes about Supplier Company mismatches with Contact Tags:**&#x20;

* You will not be able to add a Default Tag to a contact if the company they are assigned to has a different Supplier Company to the Default Tag.&#x20;
* You will not be able to submit a work item with a contact whose Default Tag is set to a different Supplier Company than the work item.

## Auto-tagging of Contacts in Work Items <a href="#contacts-populated-from-initial-email" id="contacts-populated-from-initial-email"></a>

### Contacts populated from an initial email <a href="#contacts-populated-from-initial-email" id="contacts-populated-from-initial-email"></a>

#### Known Contacts

When an email arrives from an address which is associated with a contact that is already in the system and the contact:

* has a Global scope setting, or&#x20;
* they have a Local scope setting but belong to the same company that the work item will belong to based on email routing rules

then their details are automatically populated into the Contacts Card when the work item is created by the system and they will automatically be tagged as the Primary Contact, Original Requester and Requester of the work item. Additionally, if they have a default tag assigned to them, they will also be tagged as that. However do note that you can always go in and manually edit the tags yourself once the work item has been created.

When an email arrives from an address which is associated with a contact that is already in the system, but they have a Local scope setting and belong to a *different* company than the one the work item will belong to based on email routing rules, their details will NOT be automatically populated into the Contacts Card when the work item is created by the system, (and therefore they cannot be automatically tagged to the work item). Note that you can always go in and manually edit the contact and tags yourself once the work item has been created.

#### Unknown Contacts

*Default 'Global' or 'Global & Local' Scope*

When an email arrives from an unknown address and:

* &#x20;the ['Enable Automatic Contact Creation' setting is set to ON in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) and&#x20;
* your system has been configured to set the scope of your external contacts to '**Global**', or '**Global and Local**',&#x20;

then the contact will be auto-created, have a Global scope (i.e. the won't be  linked to any specific company) and their details will be automatically populated into the Contacts Card when the work item is created by the system. Additionally, they will automatically be tagged as the Primary Contact, Original Requester and Requester of the work item. As they were previously unknown to the system, they will have no default tag set. Note that you can always go in and manually edit the tags yourself once the work item has been created.

*Default 'Local' Scope*

When an email arrives from an unknown address and

* the ['Enable Automatic Contact Creation' setting is set to ON in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation) and&#x20;
* your system has been configured to set the scope of your external contacts to '**Local**',&#x20;

then the contact will be auto-created, have a Local scope (i.e. they will be  linked to a specific company) and they will be created under the company that the work item exists under. Their details will be automatically populated into the Contacts Card when the work item is created by the system and they will automatically be tagged as the Primary Contact, Original Requester and Requester of the work item. As they were previously unknown to the system, they will have no default tag set. Note that you can always go in and manually edit the tags yourself once the work item has been created.

*Automatic Contact Creation OFF*

When an email arrives from an unknown address and&#x20;

* the ['Enable Automatic Contact Creation' setting is set to OFF in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation),&#x20;

then the work item will be created based on the email routing rules, but the email sender's details will NOT be automatically populated into the Contacts Card when the work item is created by the system, (and therefore they cannot be automatically tagged to the work item). Note that you can always go in and manually edit the contacts and tags yourself once the work item has been created.

### Contact tags populated from the Contact Activity Page <a href="#contacts-populated-from-contact-activity-call-handling-page" id="contacts-populated-from-contact-activity-call-handling-page"></a>

When a work item is created from the 'Start work item' button on the [Contact Activity Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page) of a contact, that contact will be auto-tagged as the Original Requester, Requester, Subject and Primary Contact of the work item, and their Default Tag will be added too (if they have one).


# Contacts Card

## Overview

The contacts card in the side panel of Tickets, Cases and Actions is where you can specify the people who relate to the work item and set their contact tags.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKo1tFaeJtAvubGePJiUK%2Fimage.png?alt=media&#x26;token=f1f0eda1-5e98-4e8e-a532-07a4a72e5a1d" alt=""><figcaption></figcaption></figure>

Clicking on an individual record will display the contact detail's information in a new tab showing the [Contact Activity Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWsYxfm_0NfuJyJssZ6%2Fimage.png?alt=media\&token=82d9ec27-3ae9-47ff-833d-420ad8f359b0)

## Auto-population of the contacts card <a href="#contacts-populated-from-initial-email" id="contacts-populated-from-initial-email"></a>

#### Contacts populated from an initial email <a href="#contacts-populated-from-initial-email" id="contacts-populated-from-initial-email"></a>

When an email arrives from an address which is associated with a system user or an external contact which has been previously recorded in the system then their details are automatically populated on the contacts tab when the Ticket is created by the system. They will automatically be [tagged ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-tags)as the Original Requester Requester, Subject and Primary Contact. These tags can be removed.&#x20;

Optionally the first operator to assess the Ticket can also set them as the Primary Contact if deemed appropriated by their assessment. If you tag another contact as any of these relationship types, the tag will be removed from the previous contact.

#### Contacts populated from Contact Activity Page <a href="#contacts-populated-from-contact-activity-call-handling-page" id="contacts-populated-from-contact-activity-call-handling-page"></a>

Similarly, when a work item is created from the 'Start work item' button on the [Contact Activity Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-activity-page) of a contact, that contact will be [tagged](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-tags) as the Original Requester, Requester, Subject and Primary Contact of the work item.

## Manually adding contacts to the contacts card <a href="#searching-creating-contacts-manually" id="searching-creating-contacts-manually"></a>

You can also add contacts to the work item manually by searching for them in the contacts card.

{% hint style="info" %}
Note that you will only be able to view contacts from the same company as the work item.
{% endhint %}

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHaVmBb0E56_Q_jYnK%2F-MZHbC4BRt2U6cLKu08V%2FContact-Card-Search-for-Contact.gif?alt=media\&token=599a753b-246e-417c-af72-9df32a26189e)

If you search for a user in the contacts card that does not exist in the system, you can create a new contact by clicking on the ‘Create Contact’ option and filling in the contact's details.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHZHKfCwmT20z_i-95%2F-MZHa09WPZI3WlIY7Ea-%2FContact-Card-Create-Contact.gif?alt=media\&token=bd8d2355-15e2-4760-b594-6db9028823c3)

If you have written the email address for the contact, the system will decode and auto-populate the first name and last name of the contact. Once you fill in all the information and click on create contact, the system will redirect you back to the work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHNQAkYnfT4YfYPY7I%2F-MZHZ15Kudy6pBkdjKew%2FContact-Card-Email-Address.gif?alt=media\&token=971fe34f-7a7b-4a1b-a402-d0868d662d26)

When you manually add a contact for the first time, they will be [tagged ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contact-tags)as the Primary Contact, Original Requester, Requester and Subject by default. You can manually reassign the Primary Contact, Requester and Subject tags to other users afterwards, but note that the Original Requester tag cannot be changed once it has been set.


# Emails


# Composing Emails

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY2OQ==>" %}

You can write a new email from the Email tab of a work item.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUndPccUgucI68JhL8tll%2Fimage.png?alt=media\&token=ecdb684c-2074-411a-939b-56232fe8de98)

You can [save an email as a draft](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/saving-an-email-as-a-draft), [schedule when you want to send an email](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/scheduling-of-emails-and-the-outbox-page) and send an email straight away.

Note that you cannot send an email that [exceeds the size set in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#maximum-email-size).

Once the email has been sent, it will appear in the timeline, where you can see who composed the email, the content of the email if you expand it, when the email was composed and when it was sent. You will also have the option to reply to the email, forward the email, expand the email or print the email.

{% hint style="info" %}
You can write a brand new email without needing to have the work item assigned to you.
{% endhint %}

## Sending an email to a recipient not associated with a Work Item

To help safeguard sensitive information, should a recipients address that is not associated with a Work Item ever be entered in an email in a Work Item, a warning message will appear alerting you to the fact that an email address is not associated with the work item and giving you the option to remove any non-associated email addresses. If you still wish to send the email to the chosen email recipient simply click send.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbhMPszWTlfRFMCXQPTFx%2Fimage.png?alt=media&#x26;token=28299f9b-0cde-4769-8aeb-d89e818e48c2" alt=""><figcaption></figcaption></figure>

## Responding to emails from the timeline <a href="#f-responding-to-emails" id="f-responding-to-emails"></a>

You can also reply / forward emails from the timeline by clicking on the links available. These buttons will be enabled when you mouse over the email card.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjEJi2N6N-uLY5hw_8-%2F-MjEQNzl2Zg1nSwVSx_f%2FResponding-to-an-email-from-the.gif?alt=media&#x26;token=1affb6b1-936e-4944-8395-56ee720b6487" alt=""><figcaption></figcaption></figure>

## Rules for To, From, Cc, Bcc Addresses <a href="#h-rules-for-to-from-cc-bcc-addresses" id="h-rules-for-to-from-cc-bcc-addresses"></a>

System behaviour for entering email addresses is as follows:

* When sending a new email, the system will default the To address to that of the Primary Contact in the contacts section. Cc Address will also default to email addresses entered in the Ccs section.
* If more than one possible From email address is configured, the system will populate the default one (configured as default in Builder), and will display a dropdown to allow the alternate ones to be selected.
* These standard rules for default and suggested addresses can be overridden for To, Cc and Bcc for Cases and Actions in Builder configuration. Addresses set as default will auto-populate (more than one can be set in this way). Override addresses not set as default will be available for quick selection by clicking the To / Cc/ Bcc button address
* When searching for a contact in the To/CC/BCC fields, you will only be able to view contacts from the same company as the work item. However, you can manually enter the email address of a contact from a different company.&#x20;

{% hint style="info" %}
Note: The From address always displays in the email composition section when you are writing an email. This ensures that the sender will always have a view of the email address being used as the from when sending out emails from a particular work item.
{% endhint %}

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWsea8p01g1B2QlmpnT%2Fimage.png?alt=media\&token=caaf9daa-47b2-48b9-b534-0e6ea43a8ab1)

{% hint style="info" %}
Note: You will only be able to see the email addresses of contacts from companies that you have access to. However, you are able to manually enter any email address. These permissions can be configured in Builder, click [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#external-contact-scoping)for more information.
{% endhint %}

### Copy-paste of Email Addresses between To, Cc, Bcc

When composing emails, you can easily copy email addresses between the To/Cc/Bcc addresses via the ‘copy’ icon displayed when clicking into the relevant address field.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYp8XDI6leEQSQrhkBx%2F-MYpBEL1-NjkOuUl2hcl%2FCopy-Addresses.gif?alt=media\&token=88961724-2e4b-45a7-9ff2-9a894ba5ce86)

### External Contacts creation prompt for new email addresses

When you send out an email which contains new email addresses (i.e. not linked to existing contacts), the system will display a popup to allow you to create them as new contact records.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWsf08Vx5_v_1yk_7-P%2Fimage.png?alt=media\&token=7915f188-7699-406f-9519-d6797d50c40b)

If there are any email addresses for which you do not wish to create a new record, simply hover over the row and click the delete icon. Additionally, there is a ‘Do not show this again’ checkbox which when clicked will ensure you are not presented with this popup for subsequent new email addresses (this can be switched back on again in the [user profile section](https://docs.enate.net/enate-help/work-manager/user-settings#other-system-personalisation-options) where you can also find your email signature settings).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjEJi2N6N-uLY5hw_8-%2F-MjENAZm2Pl7V2yil7sF%2Fimage.png?alt=media\&token=59fd53f8-b060-479b-8eb7-716aea978990)

## Email toolbar <a href="#a-email-toolbar" id="a-email-toolbar"></a>

Via the email toolbar you can:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKcDigOh4e2YnA6Dxldkz%2Fimage.png?alt=media\&token=fb429cf6-8216-4bba-884d-926be50efebd)

* [Attach files](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/attaching-files-to-an-email) to the email
* Access the [email body formatting toolbar](#d-email-body-formatting-toolbar)
* Pin the email body formatting toolbar
* Insert a [Canned Text](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/canned-texts)
* Set the email importance as high

### Email Body Formatting Toolbar

Clicking on the email body formatting icon will formatting options for the main body of the email.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPzkTr3GNsQdkRTYE4j1V%2Fimage.png?alt=media\&token=bb700e72-7036-4b64-88a8-95b7d28eb402)

You also have the option to pin the email body formatting toolbar.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8aKINEpXy4c8tumGJTQD%2Fimage.png?alt=media\&token=edb497cd-3b96-4ae0-81a8-896f748ab39a)

The email body formatting toolbar gives you the options to:

* Select the font
* Select the font size
* Make the text Bold, Italic or Underlined
* Undo your previous changes (also available with Ctrl + Z)
* Redo your previous changes (also available with Ctrl + Shift + Z)
* Expand the email to full screen
* Select the background colour
* Select the text colour
* Choose how to align the text
* Add a numbered list
* Add a bullet list
* Text inline options - ability to increase or decrease the text indent
* Insert a horizontal line
* Adjust the line height
* Select an inline style
* Format the cell style
* Insert a strike through (also available by highlighting the text and Ctrl + S)
* Add a subscript or superscript
* Add special characters
* Insert a link
* Insert a table
* Insert an image
* You also have the option to view a list of keyboard shortcuts

#### Font Settings Saved

When you compose an email (either as an email template in Builder, or any form of new/response/forward email in Work Items in Work Manager) your font settings (i.e. your font style and size) the font type and font size most recently used will be saved  as the font for writing content so you don't need to set them again. &#x20;

These values are saved to the user profile so will persist between Builder and Work Manager usage.&#x20;

This only pertains to the front at the very top of the email being composed - if user clicks into any pre-existing content further down the mail, the font style and size already in use for that content will be used. See note for further details. As part of this change, inconsistencies in 'new empty lines' for emails has been resolved - when writing a new email, 2 blank lines will always be inserted that the top of the mail.

Note that the font for canned texts and templates will use the font settings when they were created.

The email font style and size being used when a user is composing a mail will depending on whether they are clicking on pre-existing content. The logic for which fonts will be used is as follows, and is impacted by the new auto-insertion of two blank lines at the beginning of every new email:

* 1st auto-inserted line: uses the user-saved font settings from their most - recent email.
* 2nd auto-inserted. This is always set as Arial - 10.

Subsequent email content after this may come from: -previous emails in the mail chain

* email template content
* email signature content font style and size in these sections will come from that already existing content, depending on where user clicks.

## Copy / Paste of Excel, Word and Web information <a href="#e-copy-paste-of-excel-word-and-web-information" id="e-copy-paste-of-excel-word-and-web-information"></a>

You can copy/paste information into emails from external documents, e.g. Excel tables and Word document content, as well as HTML information from webpages.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYjsnFTQ5VLGmtJzs44%2F-MYk2ggE9I7eFv0uuxbj%2FCopy-from-Excel-into-Email.gif?alt=media\&token=a8d43ce7-1392-41d6-bd61-530e4f0f64b3)

## Email Pop out <a href="#g-email-pop-out" id="g-email-pop-out"></a>

If you wish to dedicate more screen space to view emails, you can use the available pop out feature:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYjsnFTQ5VLGmtJzs44%2F-MYk4eYtpA-7DtwWQ7k-%2FEmail-Popout.gif?alt=media\&token=b3337661-da4d-4765-8373-4c9f5bea6ed5)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjERJfytdZskUYwP-2d%2F-MjESLF3srSji3R6O9GN%2FOpen-Email-Popout-from-Timeline.gif?alt=media\&token=f6e4c73e-a7cf-4374-9485-af5fc8b096c1)

## Undo Send Setting

The Undo Send setting lets you add a time delay to when your emails will be sent, giving you the opportunity to cancel sending an email, or reviewing an email before it gets sent.

You can set an Undo Send time in [User Settings](https://docs.enate.net/enate-help/work-manager/user-settings#undo-send).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7C5Oei3m1jS327X4DxI5%2F8-Cancel-Send-Setting.gif?alt=media\&token=be3fa04c-cbdd-4ac1-bb90-5eed13efa148)

When an Undo Send time is set, a popup will appear allowing you to cancel sending the email.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyQJOVV5jTRERBiCvABAD%2F8-Cancel-Sending-an-Email.gif?alt=media\&token=7286cbfc-f464-4616-9d3b-fbd32b8fef1e)

Additionally, when an Undo Send time is set, you will have the option of sending an email 'Now' in the Timeline which overrides the time delay from the Undo Send configuration and you will also have the option to cancel sending the email altogether.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-M_5gMeG-gAiOmge9mMj%2F-M_5hm6ySU30Ampha6ca%2Fimage.png?alt=media\&token=6649922f-bb14-4fa0-9ea5-d9ab727bbd66)

When an Undo Send time is set, emails will be shown in the Outbox page with a Send Status of Queue.

## Downloading an email

For all type of emails (inbound / outbound / cancelled / failed/ scheduled) you have the option to download the underlying .eml file. This is available from the various locations in the system where emails can be see, i.e. Work Item Comms & Timeline sections, Email Inbox, Sent Items views.

{% hint style="info" %}
Please note: If the email you are attempting to download contains an attachment file which has been explicitly manually deleted by an user (for e.g. reasons of data sensitivity), the .eml download option will be disabled for that email - the system will display a message explaining the reason for this disabling when download icon is clicked.
{% endhint %}

### How do I enable spell checker in Enate

You can easily check the spelling & grammar for everything you write in Enate (including your emails) by switching on spellchecker in your browser. For information on how to enable spell checker in the most popular internet browsers follow this link "[How to enable spell check in Enate"](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/appendix/how-to-enable-spell-check-in-enate).


# Canned Texts

Canned Texts are standard pre-configured texts which are created as part of system configuration.

When writing an email, you can insert a Canned Text by clicking on the Canned Texts icon at the bottom of a write an email screen. This will show you all canned texts available for the Service Line and you can use the free text search function to filter items by title.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYjsnFTQ5VLGmtJzs44%2F-MYjy3caUFanUcTY6gC9%2FCanned-Text.gif?alt=media\&token=a1699841-c028-47af-a3e8-84983c669a0e)

You can also use the ‘recently used’ option by clicking on the dropdown list, allowing you to quickly access a more relevant canned text. You can also manually modify canned texts after they have been inserted into your email.

{% hint style="info" %}
Note: Any files linked to the canned text section will also be attached at the same time.
{% endhint %}

**Show by Language**

You can also select a canned text in a different language by clicking on the language in the dropdown list.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWsahHPkfWL1L3aK4HM%2Fimage.png?alt=media\&token=8ac10efc-9c5e-424c-be4b-713d12eb03ea)

{% hint style="info" %}
Note: The system will show the canned text in your language by default.
{% endhint %}


# Email Attachments

## Attaching files to an email

Files can be attached to an email in various ways.&#x20;

1\) You can attach files when composing an email by clicking on the attach files option at the foot of the email section.&#x20;

Files that are already attached to the work item, and are therefore already in the [files tab](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/files-tab) (including files attached to previous existing emails within the work item) will be available for selection from here. You can use the search function to search for specific files if there are many to choose from.

You can also search for files from your PC to attach from here by clicking on the ‘Browse This PC’ icon.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfGpcbQZJQ2vfK8NS6Foc%2Fimage.png?alt=media\&token=616df6f8-c625-43e0-8a38-c7d4bc70a544)

2\) You can add links to an email by clicking on the attach links option at the foot of the email section. Links that have already been added to the work item (and are therefore already in the [files tab](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/files-tab)).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqPBOJJuK8eBkuwfE2EfV%2Fimage.png?alt=media\&token=9ee0ff90-50f6-454d-88c3-026612390793)

3\) You can drag and drop files from your desktop into the email section

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYjsnFTQ5VLGmtJzs44%2F-MYk0n5Fumnw-Y19cgwu%2FDrag-and-Drop-Files-Into-Email.gif?alt=media\&token=7bc10b5e-fe3b-4295-a2b0-f4abc08b503e)

4\) Files which have been linked to a standard Canned Text will automatically attach to the email when the canned text is selected.&#x20;

When emails are auto-generated and sent by the system, the email template used may be linked to one or more tags – the system will identify any files currently attached to the work item which have been tagged with this same value, and will auto-attach them to the email before sending.

## Viewing Attachments <a href="#preview-of-attachments" id="preview-of-attachments"></a>

### Previewing Attachments <a href="#preview-of-attachments" id="preview-of-attachments"></a>

You can view all the email attachments that have been added to the work item and other related/linked work items in the files tab.&#x20;

Attachments from incoming emails are denoted with a green email icon: ![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FgaZowGfYqSpWXd6DK7aI%2Fimage.png?alt=media\&token=0f53fe10-c592-4151-8d4f-4df32c979db4)

Attachments from outgoing emails are denoted with a blue email icon: <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FD1Up0VmIWPMPFZmNwl7k%2Fimage.png?alt=media&#x26;token=7ba2d037-20aa-4156-9ab6-a55b7b6f0f4a" alt="" data-size="line">

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJqsYwkhoAYLLMJeI2O0g%2Fimage.png?alt=media\&token=60f10264-646f-4056-9e64-0a926893198f)

You can see the name of the file, what type of file it is, its size and when and by who it was uploaded and the reference number of the work item it was uploaded to.

You can also see the [tags ](https://docs.enate.net/enate-help/work-manager/work-item-screens/files-tab#tagging-files)and [notes ](https://docs.enate.net/enate-help/work-manager/work-item-screens/files-tab#adding-notes-to-files)that have been added to the files.

### Downloading Email Attachments <a href="#download-multiple-attachments" id="download-multiple-attachments"></a>

#### From an Email

You can download files from an email by opening the email you have received and clicking to download the file attached.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKgnxPqfacTDkpJU7VpcB%2Fimage.png?alt=media\&token=e5c58404-ac7e-47b8-9eaf-66cfb5492213)

If multiple files have been attached, you have the option to download all the files individually or to download them as a zip file.

#### From the Comms/Timeline

It is possible to download multiple attachments with a single click from mails in the comms and timeline section. Clicking on the ‘Download all’ icon will download all attachments present in that Comms / Timeline section item.

#### From the Files Tab

You can download individual files by clicking on the the option in the menu on the right.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F04z5A8u0Jqa0ztTlCavF%2Fimage.png?alt=media\&token=19a9d7f7-c416-4756-9d97-ccec30f6cb15)

You can download multiple files at once by selecting the files you wish to download and selecting the option at the top of the screen.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FGFmsyBuXctvxKnpaRBTL%2Fimage.png?alt=media\&token=de3c6b03-4fd7-42b7-aec7-dd41f40dcfd5)

You can download multiple files in a zip file by selecting the files you wish to download and selecting the option at the top of the screen.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1Kdk3vUSgLqipOLp154O%2Fimage.png?alt=media\&token=7d8298eb-73bd-4748-9e45-13e2cefa65ca)

## Deleting Email Attachments

If your system has been set up to let you delete email attachments, you can delete attachments that originated from an email in the file card of a work item. This is useful when, for example, you are dealing with sensitive information in email attachments.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY3Nw==>" %}

The deleted attachment will also be deleted from other related work items such as other Actions in a Case, Sub Cases, child and parent Tickets if a Ticket has been merged, child Cases and parent Tickets if a Ticket has been converted to a Case.

But note that if you delete an email attachment from a Ticket that has been split or is the child Ticket of a split, the deleted file will not be deleted from the other child Ticket(s) or the parent Ticket.&#x20;

Note also that deleting an attachment from a linked work item will NOT delete the attachment from the work item(s) it is linked with.

Please also be aware that it is not possible to delete an email attachment from a work item that is Closed.

The attachment will be deleted from all parts of the system, so you won't be able to search for it in Quickfind, and it will not be available to attach to a new email relating to the work item.&#x20;

Any further activity on the work item will not resurrect the deleted attachment and creating a new linked work item will not resurrect the deleted attachment.

You will be notified in the timeline when an email attachment has been deleted, along with the file name of the email attachment that was deleted, the subject of the email it was attached to, who deleted it and when it was deleted.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7xfPPrM6vKG6rgknlD3t%2Fimage.png?alt=media\&token=643af32a-0fec-4723-b53b-0b15c178f826)


# Saving an Email as a Draft

## Overview

To make your email work more flexible we've added the ability to save your emails as drafts if you're not quite ready to send them. Now when you are writing an email in a work item, you can choose to save the email as a draft and come back to it later.&#x20;

When you are writing an email in a work item, you can choose to save the email as a draft and come back to it later. Drafts will be saved for a maximum of 90 days.

Note that you cannot save an email as a draft that exceeds the size set in Builder - [see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#maximum-email-size).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKAhUAwy1KfsJLBv2TFlj%2Fimage.png?alt=media\&token=5d2b623c-2565-4e28-b89d-5ba5c254b296)

## Viewing Draft Emails

If you have the Drafts filter in the comms/timeline tab switched on (note that this will be switched on automatically by default upon upgrade), you will see any saved draft emails for that work item in the comms/timeline.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3ASdgbBzddHpmOHa1qUi%2Fimage.png?alt=media\&token=3d4f970a-2fbf-4af5-b907-4ca6d56912ea)

You'll see who created the draft and when and the first few lines of the email.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyjNO6jUw3tdzR9NZnQmM%2Fimage.png?alt=media\&token=6b4d7579-6c4b-4eae-8da9-e63ef33d3e08)

If you click to expand the view, you'll also see the email address that the draft will be sent from, the address it will be sent to, any CC or BCC email addresses, the subject of the email, any attachments and the full email content if these have been added when the draft was saved.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ft1T4JbShO2Z3RJnqDaY1%2Fimage.png?alt=media\&token=d31779e5-cec5-4fb5-8227-6bc7b64b4e61)

You can edit a draft email from the timeline by clicking 'Update Draft'. This will open up the email editor where you can edit your draft. Note that you can only edit or delete a draft email from the work item it belongs to.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FAoxwPEtqoDMcFNhGzT8T%2Fimage.png?alt=media\&token=7282a521-04f2-4e65-9b91-bdeb030d6cca)

You also have the options to delete the draft, to open the email in a pop-out window or to print it.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FB4ZBXerywKYHuu1uDg6h%2Fimage.png?alt=media\&token=1716cdce-4b8e-46ae-8ec1-3ba79a69b05a)

Multiple users can work on the same draft, just not at the same time. A single work item can have multiple draft emails. These can all be seen and edited from the work item's comms/timeline.

When a draft already exists for a work item, the system will alert you to this when you start writing a new email so you can choose whether you want to continue writing your new email or whether you would like to edit the draft email instead.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjxVnJbiLcqMYxkFeZAb6%2Fimage.png?alt=media\&token=501c270b-305f-4c8d-9864-bfa14e942147)

If a work item has a draft email and you merge or convert a Ticket to a Case, you will be able to see the draft email in the comms/timeline or all work items in the related group as long as the 'Drafts' filter and the 'Include Related Work Items' filter are switched on.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FrN0c02NuaBR66FV9ZYVx%2Fimage.png?alt=media\&token=2f3b400c-3f17-4ac0-abf5-5d0d2fb1e238)

The draft email will show in the timeline with the reference number of the work item it belongs to.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHQrxmiGlCYELXAIWlLGp%2Fimage.png?alt=media\&token=88e215db-c3ba-48d9-af63-33406f39dab2)

Note that draft emails will not be copied across when copying communications to a new linked work item, even when the 'Copy communications' option is enabled.

## Attaching files to draft emails

An attachment icon in the draft email comms/timeline entry shows you if any files have been attached to the draft email.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7Cl7N5bDFVfXBIHboSqU%2Fimage.png?alt=media\&token=590a0487-4ed2-48b2-bd1f-b46b47fc555c)

Clicking to expand the comms/timeline view will show you the name of the attachment and give you the option to download it.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fe325z5wrnLmvmU6DLKln%2Fimage.png?alt=media\&token=b5eeca68-7bdf-4adb-ab97-e02e69342369)

Additionally, any files attached to draft emails will show in the files tab and be marked with a draft icon. You can view, download or delete files attached to draft emails from here. Note that you cannot add notes or tags to files attached to draft emails.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTicGP4p6uu8mrF8hN80V%2Fimage.png?alt=media\&token=f8886e0b-358c-4087-a2fb-4a19f054b1bc)


# Scheduling Emails

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY4Mw==>" %}

You can schedule the date and time of when an email will be sent by selecting the Schedule Send option.&#x20;

The scheduled email will appear in the Comms and Timeline tabs, along with who scheduled it and when it has been scheduled for. If the email has been scheduled to send more than 2 minutes later,  a 'Send Now' and 'Cancel' button will appear to let you send the scheduled email straight away if you have changed your mind or to cancel sending the scheduled email altogether.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOl7Tqy9a2lTG3lcvzOJu%2F8-Schedule-Sending-Email.gif?alt=media\&token=2870866d-4c88-4f3f-8838-60b25aa3fbc8)

Note that you cannot schedule an email that exceeds the size set in Builder - [see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#maximum-email-size). However, validation of the email size occurs as part of saving the email, not at the sent time. So if a 25MB email has been scheduled and then the maximum email size gets reduced in Builder to 10MB, the scheduled email will still be sent as it conformed to the size allowance configured when it was scheduled.


# Email Inbox View

## Overview

This shows emails related to in-progress Work Items in your business areas. There are various filtering options and ways to view different sets of data. Use this view to keep on top of incoming emails for the work items you and your team are dealing with.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPCF6Yv5maEZrCPrTrRWa%2Fimage.png?alt=media&#x26;token=fa2b426a-8b75-4a49-8981-7d93914898b6" alt=""><figcaption></figcaption></figure>

By default, emails received within the past 90 DAYS are displayed. Agents can use the Filter dropdown to select a different (e.g. older) date or date range to see emails older than this, but note that the date range specified can only span a maximum of 90 days.

## Sections in Email Inbox

In the collapsible folder pane on left-hand side of the Email Inbox, you can see links to various sections of your Email Inbox, divided into:

* **My Emails** - Emails for all work items that are currently in your Work Inbox (that you'd see in your Homepage)
* **My Team Emails** - Emails for all work items that are currently in the Work Inbox of your Team.\
  \&#xNAN;*This link is visible if you are a Team Leader or are able to see your peers and Queues.*
* **Unassigned Emails** - Emails for all unassigned work items sitting in Queues you work out of.\
  \&#xNAN;*This link is visible if you are a Team Leader or are able to see your peers and Queues.*
* **All emails** - in this section you will be able to view all emails belonging to work items, including closed items, in your business areas that you have permissions on. In this section you can also filter by the status of the work item that the email belongs to.

The numbers displayed show the number of unread emails in these different folders.&#x20;

* **Unhanded Emails** - here you'll be able to see any such unhandled emails for your area of the business, and decide on the what to do with them. The number next to this section shows you the total number of emails in the section. [See here for more information](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/unprocessed-emails).

There's also links to your [Sent Items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/sent-items-view) and your [Outbox ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/outbox-view)- all of which open in separate tabs.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F20c8dnK44HIEMA0kTIZs%2Fimage.png?alt=media&#x26;token=d541fed3-0681-4ec1-9c43-549adc05b1eb" alt=""><figcaption></figcaption></figure>

You can see a list of all the emails in your inbox as well as Self Service user comments, with the most recent at the top, showing who the email is from, when it was received, the subject of the email, a preview of the first line of the email body and which work item the email relates to. You will also be able to see if the email has any attachments and if the email was sent with high importance.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FE1pzS9ws9dgddVFLQcax%2Fimage.png?alt=media&#x26;token=0a86e78a-6cd3-40d7-b56c-8199096d597c" alt=""><figcaption></figcaption></figure>

Unread emails will appear in bold and you can filter to view just your unread emails by clicking on the 'Unread' option.

{% hint style="info" %}
Note that an email will be marked as read when a user opens an email.
{% endhint %}

## Filtering Options

You can filter your inbox by Customer, Contract, Service, Process, Queue, the 'from' email address, whether or not the email has attachments, and by email received date.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIOgJVmoEMtEYRvVOsojk%2Fimage.png?alt=media&#x26;token=e9ff8ad2-55fa-426c-ade3-befe7ba36e9d" alt=""><figcaption></figcaption></figure>

If you have access to the 'My Team Emails' view you'll also be able to filter by assigned user.

For the 'All Emails' section you can also filter by the status of the work item that the email belongs to.

## Switching between views and refreshing on new incoming mails

You can switch between viewing 'My Emails' which are the emails in your own inbox, 'My Team Emails' which will show you the emails in the inbox of your team members, 'Unassigned Emails' which will show you incoming emails for work items in your Queues which don't have an assignee, 'All emails' which shows you all emails related to work items, including closed items, in your business areas that you have permissions on and 'Unhandled Emails' which shows you any unprocessed emails for your area of the business so that you can decide what to do with them.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXk4INAWDhum60x9KOeOQ%2Fimage.png?alt=media&#x26;token=10fd70fb-bdc5-4767-b2e0-e69ec156c96e" alt=""><figcaption></figcaption></figure>

For My Emails, My Team Emails, Unassigned Emails and All Emails, when a new email comes in the 'unread' number will refresh and a mail icon will appear on the refresh button. You just need to click it to refresh your inbox and view the newly arrived emails.&#x20;

{% hint style="info" %}
You can mark individual emails as read/unread, but please note that this will NOT affect the new information flag on the work item that the email relates to, so marking an email as read will NOT switch off the new information icon in the work item.
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzGNjNp26QZi0RggxOdDn%2Fimage.png?alt=media&#x26;token=7c826769-7359-4877-a088-3db043091910" alt=""><figcaption></figcaption></figure>

For **Unhandled Emails**, the number next to this section shows you the total number of emails in the section. [See here for more information](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/unprocessed-emails).

The main section of the Email Inbox view displays the preview panel for whichever email you have selected. You can adjust the size of the email preview panel to suit your needs.

When you click on a email, you will be able to see the full email in the right-hand side of the screen. You can see the subject of the email, who it was sent from, who it was sent to, any CC recipients, a link to the work item that the email relates to, the due date of the work item and the full content of the email.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F9V8B4v2Q7quGQnYzJyMY%2Fimage.png?alt=media&#x26;token=c3669ba5-0d29-4cbb-9635-6aa65a36c7bf" alt=""><figcaption></figcaption></figure>

## Replying / forwarding emails

If you click on reply, reply all, or forward for an email, the system will open a new tab displaying the Work item in question and will take you to the email editor screen to start composing your email.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvW4tIzguNrPaVRPjTmEK%2Fimage.png?alt=media&#x26;token=faac0913-558d-4362-8647-caa845658442" alt=""><figcaption></figcaption></figure>

## Further options

Further options are also available from the ellipses next to the reply links. These will allow you to go directly to the work item that the email relates to (opening in a new tab), and to print the email directly.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FosuoYZUnUKS8kHUpeFTY%2Fimage.png?alt=media\&token=61385660-0c8d-4178-be36-53854af6f6ed)

You also have the option to download the underlying .eml file.

{% hint style="info" %}
Please note: If the email you are attempting to download contains an attachment file which has been explicitly manually deleted by a user (for e.g. reasons of data sensitivity), the .eml download option will be disabled for that email - the system will display a message explaining the reason for this disabling when download icon is clicked.
{% endhint %}

## Email Attachments

If an email has any attachments, you can see the name of the attachment, its size and the option to download it. If the email has multiple attachments, you have the additional options of downloading all of the attachments or downloading them all as a ZIP file.

## Full-screen option

You can also expand the email to full-screen mode, where the preview pane is hidden.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5oz6WhjL07E9UAIHCFEd%2Fimage.png?alt=media&#x26;token=cf5589f2-622b-4675-8819-0be7ffc1006e" alt=""><figcaption></figcaption></figure>


# Sent Items View

## Overview

Sent Items shows you all of the emails from your business area's work items that have been sent out.

You can see a preview list of all the emails that have been sent out, with the most recent at the top, showing who the email was sent to, when it was sent, the subject of the email, a preview of the first line of the email body and which work item the email relates to. You will also be able to see if the email has any attachments and if the email was sent with high importance.

You can adjust the size of the email preview panel to suit your needs.

When you click on an email, you will be able to see the full email in the right-hand side of the screen. You can see the subject of the email, who it was sent from, who it was sent to, any CC recipients, a link to the work item that the email relates to, the due date of the work item and the full content of the email.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmVqAUZ7UQFSuuzVD41cE%2Fimage.png?alt=media\&token=a3eb6477-7250-46e5-bb94-1eed25c4fb69)

You can also expand the email to full-screen mode, where the preview pane is hidden.

## Switching between views

You can switch between viewing 'My Emails' which are the emails that you have sent and 'My Team Emails' which will show you the emails that members of your team have sent.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTWqqKAAIjsKcpkkuZBFU%2Fimage.png?alt=media\&token=7ddf6ca2-2314-485d-8020-dedeb65a5bed)

## Replying / forwarding emails

You can also reply, reply all, or forward a sent email. When you click on one of these options, the system will open a new tab displaying the work item in question and will take you to the email editor screen to start composing your email.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjdV7aEA5p9Be977zh28M%2Fimage.png?alt=media\&token=64d22a13-c501-4a43-aee6-387c716cc1f7)

## Filtering Options

You can filter your sent emails by Customer, Contract, Service, Process, Queue, who the email was sent to, date range, the status of the work item that the email relates to, whether or not the email has attachments, and whether or not the email was system-generated.&#x20;

Note that when filtering by date you can only filter for a maximum timespan of 90 days.

If you have access to the 'My Team Emails' view you'll also be able to filter by assigned user and by who the email was sent by.&#x20;

## Further options

Further options are also available from the ellipses next to the reply links. These will allow you to go directly to the work item that the email relates to (opening in a new tab), and to print the email directly.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJqp35UUcE7pt1f3d0Yyn%2Fimage.png?alt=media\&token=e5f9230b-358b-4c18-97b4-00db9c8ab3c9)

You also have the option to download the underlying .eml file.

{% hint style="info" %}
Please note: If the email you are attempting to download contains an attachment file which has been explicitly manually deleted by a user (for e.g. reasons of data sensitivity), the .eml download option will be disabled for that email - the system will display a message explaining the reason for this disabling when download icon is clicked.
{% endhint %}

## Email Attachments

If an email has any [attachments](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/attaching-files-to-an-email), you can see the name of the attachment, its size and the option to download it. If the email has multiple attachments, you have the additional options of downloading all of the attachments or downloading them all as a ZIP file.


# Outbox View

## Overview

The Outbox Page is where you can find emails belonging to yourself or to your team that are scheduled be to sent at a later date, or have failed to send.

You can access the Outbox Page from the Emails section in the navigation link. The total number of emails in your Outbox will also be shown in the navigation link.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6zBPgzDCBQ7DugKl91bf%2Fimage.png?alt=media\&token=ac110c95-a933-425c-bd7f-26a0fe54da9a)

You can select how many emails will be shown from the option on the right.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FypvBw33Z3mOSWcawFlqm%2F8-Outbox-Page-Number-of-rows.gif?alt=media\&token=abe4fae4-3a3f-45a3-aadb-a22e6886b6aa)

## Outbox Grid Views

The first time a Team Leader logs in, they will land on the 'My Team Emails' view. The first time a Team Member logs in, they will land on the 'My Emails' view. You are able to change your view of the outbox page to show just your outbox emails, your team's, the system's or all outbox emails. This will be saved when you log out and log back in.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FK48xnoeWvjpoA9cgRbX0%2F8-outbox-page-filters.gif?alt=media\&token=7a54f2b6-516c-4ba8-89ab-5e0fe50e3270)

Selecting '**My Emails**' lets you see emails sent by you that are in your outbox.

'**My Team Emails**' shows you emails sent by your team that are in the outbox, as well as emails relating to work items that your team members are working on that are in the outbox.

Selecting '**System Emails**' lets you see emails that are sent automatically by the system e.g. because a Ticket has been split or merged.

'**All**' lets you see emails sent by you, your team, as well as emails from outside of your team for which you have access.

## Retry and Cancel Options

You are able to manually retry sending an email by clicking on the Retry icon. The email will now be in a state of **'**&#x50;ending Retry'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJkOzke4SSq4rYPj5bw54%2F8-retry-sending-email-from-outbo.gif?alt=media\&token=7c26d189-032c-4cd2-a5c8-75ce04c1454a)

You can also retry sending an email from the timeline of the work item itself.

Additionally, the system can automatically retry sending emails if your system has been set with an Automated Failure Retry Pattern ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern)). Once the system has retried sending an email the maximum number of times specified, it will no longer retry sending it automatically, but you can still retry sending the email manually, i.e. by clicking the 'Retry' icon.

You are also able to cancel sending an email by clicking on the Cancel icon. This will remove the email from the Outbox.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_RA0uUPIci_XLqD9Fs%2F-M_REKnN58uonsLTRux6%2Fimage.png?alt=media\&token=261065a7-6f73-4cad-83a7-4def7b4d7b23)

You are also able to retry or cancel sending emails in bulk.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNIX3WDn8E0lxUGCeZUAI%2F8-outbox-page-bulk-options.gif?alt=media\&token=9ae7e2e4-e9eb-4132-87e4-04efb3ceaeae)

{% hint style="info" %}
Please note that the system will not automatically retry sending emails that have been migrated from an older version (2020.1 or older). These can only be sent by retrying manually, i.e. clicking the 'Retry' icon.
{% endhint %}

## Viewing an Email

Double clicking on an email will open the email's details in a popup in read only form. You can see who the email is from, who it is to, etc. You are also able to retry and cancel sending the email from the popup.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fp0vnOV3tG7uXuFtATaxP%2F8-opening-email-in-outbox-page.gif?alt=media\&token=ab58437e-71c2-4016-b001-177289693b7a)

## Adjusting Grid Columns

You can adjust the grid columns by clicking on the settings cog. These will be saved when you log out and log back in. The 'To' and 'Subject' columns are mandatory.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY4Ng==>" %}

* **Email Connector** - the name of the email connector through which your system sends emails. This is configured in Builder, [see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-connectors-detail).
* **Importance** - the importance setting of the email i.e. high, normal, low.
* **System Generated** - if the email was automatically generated by the system (e.g. to notify a user when a Ticket has been split).
* **Last Attempt To Send** - when the last attempt to send the email was (automatically by the system or manually by a user)
* **Last Send Failure Message** - a message displaying the reason why the last attempt to send the email failure e.g. The Email connector is disabled. Please enable it and try again.
* **Logged** - the date and time recorded when the email first failed to send.&#x20;
* **Next Attempt To Send** - when the system will next try to send the email
* **Packet** - the work item reference that the email is from. Clicking on this will take you to the work item screen.
* **Packet Type** - if the email is related to a Ticket, Case or Action
* **Send Retry Count** - this will show the number of times the system has tried to send the email. You can set this number in Builder, [see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern).
* **Send Status** - this shows what status emails in the outbox are in in terms of sending. There are 4 states:
  * **Failed** - an email with this Send Status has failed to send. In order to send it, it must be manually 'retried'.&#x20;
  * **Connector Disabled** - if an email has this Send Status, it means that the Email Connector has been disabled in Builder. [Click here for more information about how to switch it on](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-connectors-detail).
  * **Pending Retry** - an email with this Send Status is awaiting automatic retry by the system.
  * **Queued** - an email with this Send Status is already scheduled to be sent. Emails send when an Undo Send option has been set will have this status too ([see here for more information about the Undo Send option](https://docs.enate.net/enate-help/work-manager/user-settings#undo-send)). When these emails will be sent depends on the Automated Failure Retry Pattern option which is set in Builder, [see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern).
* **Attachment Count** - how many (if any) files are attached to the email


# Unhandled Emails

## Overview&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTY1NDg2Mg==>" %}

All emails arriving into Enate get automatically processed into either Tickets or Cases based on business rules which look at things like where it's sent into, who it's from and what it's about. Occasionally though, emails arrive into Enate and do not get processed into a Case or a Ticket.

This can happen due to the following reasons:

1. None of the To and/or CC email addresses have a matching email route defined for them in Builder (that's the rules which say which kind of Ticket or Case an incoming email should generate).
2. There are only BCC email addresses in the email, no To or CC addresses.

If there any such emails in your area of the business, you'll see an icon in your header bar showing you how many.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7WMlw3jyaZMFGN9ofess%2FUnhandledicon.png?alt=media&#x26;token=64d171b4-7897-4448-b0d0-e6da7c00758b" alt=""><figcaption></figcaption></figure>

This will show the total number of currently unhandled emails and, if you click the link will also show a popup showing how many of these have arrived in the past 24 hours, plus a link to take you straight to the Unhandled emails section of your Email Inbox page (alternatively you can find it within your Email Inbox view).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMRIMKGthXFGmeKlycNS7%2FUnhandledpopup.png?alt=media&#x26;token=197b29cf-5181-43a9-82ce-05e6e839a112" alt=""><figcaption></figcaption></figure>

### The Unhandled Email section of Email Inbox view

The Unhandled Emails view in the Email Inbox section in Work Manager allows agent users to review these unhandled emails and take the appropriate steps. This option is visible to all users.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUlDRYN7wQnWvcmza3uUF%2FUnhandled2.png?alt=media&#x26;token=9c702381-db6a-4444-99b1-2932819601de" alt=""><figcaption></figcaption></figure>

## **What emails do I see?**&#x20;

You'll see emails that have failed to process into a Case or Ticket (i.e. they're unhandled) which have come into the mailbox that your area of the business works out of. Other unhandled emails which arrive into mailboxes that aren't linked to any of your business processes will be seen by agents in other areas of your business.&#x20;

More specifically, if you have permissions on a process connected to an email route, you'll see the unhandled emails for any email that comes into that email connector, even if its from a different route.

The number next to this section shows the total number of emails in the unhandled email view.

### Filter Options

You can filter the emails in this section by:

* Mailbox Address
* Mailbox Name (if you know it). Specifically, this is the email address of the mailbox which handles the incoming mails.
* Date, i.e. the date which the email arrived.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbUOpCmhCSQ94ygtMgbUe%2FUnhandledFilter.png?alt=media&#x26;token=3554865c-c1d2-40e5-a2de-e384bfcb5beb" alt=""><figcaption></figcaption></figure>

## **What options do I have?**&#x20;

The Unhandled Emails view will let you review the incoming email's content to help you determine where you should route.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyE2qLHJfQMX7gyDaiO0l%2FUnhandled1.png?alt=media&#x26;token=a351849f-7f04-4751-91aa-8531ecf36a3c" alt=""><figcaption></figcaption></figure>

Once you've determined where it should go, you've got a couple of options:

1\) **You can decide to create a work item from the email**, specifying a Customer, Contract & Service for it, before launching the work item. If you do this, the email will be changed to 'Processed' and will be removed from the Unhandled Emails view when you next click to refresh your email inbox.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVQJIGQlrrkwIcZ9iSR1T%2FUnhandledCreated.png?alt=media&#x26;token=155486dc-3d8a-432d-b964-6129b132cacd" alt=""><figcaption></figcaption></figure>

2\) **You can decide to delete the email if appropriate** (for example if it's a spam mail). If you do this, the email will be changed to 'Deleted' and will be removed from the Unhandled Emails view when you next click to refresh your email inbox.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fg9HNtNzOPt01Wn1GdrxC%2FUnhandledDeleted.png?alt=media&#x26;token=41d8d5f3-0e94-4345-a81c-cd3c6681947d" alt=""><figcaption></figcaption></figure>

### **Bulk Delete Option**

There's also an option to delete multiple emails in Bulk. Click on one or more boxes and a delete button will appear next to the filter, along with the number of emails selected.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtErZCW83f2fASBADAS48%2FUnhandledBulkDelete.png?alt=media&#x26;token=51f25138-2ca0-43a1-9005-1eb4ed8a7f39" alt=""><figcaption></figcaption></figure>

### Unhandled Emails - Additional Notes

{% hint style="info" %}
Note that it is not currently possible to append an unhandled email to an *existing* work item, only to create a new work item. However once you have done this, you can still use the [merge ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/further-activities-available-for-ticket)feature to merge it in with an existing work item.&#x20;
{% endhint %}

{% hint style="info" %}
Note: Users will be able to create a new work item from an unhandled email on this page even if they do not have the 'Can Create' permission set for them.
{% endhint %}

### **Patterns to look out for - resolve with new Routing Rules**

If you find yourself regularly having to pick up unhandled mails and route them into the same tickets or cases again and again, you've got a couple of options:

* You can speak with your Business Admin to see if a new [Email Route](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes) can be set in order to catch these emails and automatically create the relevant Work Item for them.
* Alternatively, **you can resolve the issue at source and create a simple Email Routing Rule yourself, from within the Unhandled Emails view**. See '[**Creating New Email Routes from Unhandled Emails**](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/unprocessed-emails/creating-new-email-routes-from-unhandled-emails)' for how to do this.

And, for more information about how Enate processes incoming emails, [**see this section**](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic).


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


# Viewing Deleted Emails

You can view the unhandled incoming emails which were deleted by you / your team as part of dealing with them with the 'Deletion Audit' section of Unhandled Emails. This helps with an auditing how incoming emails which were unhandled have been dealt with.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZEnkoxBSydh5QNG7GmSs%2FDeletion%20Audit.webp?alt=media&#x26;token=c4c58af7-5101-4fa8-a399-328284843af1" alt=""><figcaption></figcaption></figure>

Clicking on this 'Deletion Audit' link will bring up a view of all deleted unhandled emails within your area of the business. These are incoming unhandled emails where the decision was made to delete these mails rather than create a new Case or Ticket from them.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMWTg1M6hqycqHIqtLzub%2FDeletion2.png?alt=media&#x26;token=bd0d9ab9-fb2a-478e-80dd-af4b3c30f070" alt=""><figcaption></figcaption></figure>

All filters and paging options are available as for the other email views in this page, but the emails themselves are shown in read-only mode..

Clicking on a deleted unhandled email will display the email in detail in the main section of the screen, with any attachments that it may have had.&#x20;

**Additionally, the header bar above the mail shows who deleted the email and when.**

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFSYrfT5oW5k0xINWBgMb%2FDeletion3.png?alt=media&#x26;token=45e48be4-56d9-4c5a-974c-113d01afc00c" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: You cannot 'undelete' emails which have been deleted, however if you wish to copy body text information from them you can do this by simply selecting the desired text and copying / Ctrl-C.
{% endhint %}


# Unhandled Emails Further Specifics

### When do emails appear in the Unhandled Emails view?

Emails will appear in the Unhandled Emails view of your 'Email Inbox' view in Work Manager if they meet one of the following conditions:

1. None of the To and/or CC email addresses have a matching email route.
2. There are only BCC email addresses in an email, no To or CC addresses.

See the table below for further detailed information on how emails arriving into Enate are treated, depending on the combinations of Enate-relevant email addresses may appear in the TO, CC or BCC fields.

| **Scenario**                                                                                                 | **Number of work Items Created**   | **Will they appear in the Unhandled View**                                   |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------- | ---------------------------------------------------------------------------- |
| Email to just one email address in either the TO or CC field                                                 | 1                                  | <mark style="color:orange;">No</mark>                                        |
| Email to 2 or more email addresses in either TO or CC field                                                  | 2 or more                          | <mark style="color:orange;">No</mark>                                        |
| Email to 1 email address in TO, another in CC field, and one in BCC field                                    | 1 for each TO & CC address         | <mark style="color:orange;">No</mark>                                        |
| \*Email to 1 email address in TO and another in BCC field                                                    | 1 for TO field                     | <mark style="color:orange;">No</mark>                                        |
| Email to 1 or more email addresses in BCC only. Nothing in TO or CC fields.                                  | 0                                  | <mark style="color:green;">Yes - for the BCC email mailbox</mark>            |
| Email to just 1 email address that is not correctly configured in Enate                                      | 0                                  | <mark style="color:green;">Yes - for the non-configured email address</mark> |
| Email to 1 email address that is not configured correctly in Enate and one email address configured in Enate | 1 for the configured email address | <mark style="color:orange;">No</mark>                                        |


# Blocked Email Addresses

This is where you are able to easily add, edit and delete email addresses to be blocked.

**Disable auto-generated emails when creating a new Ticket from this address** - the system will allow Tickets to be created for emails arriving from this address but will not send any auto-generated emails out to the address.

**Disable auto-generated emails when creating a new Ticket/Case from this address** - the system will allow Tickets and/or Cases to be created for emails arriving from this address but will not send any auto-generated emails out to the address.

**Auto-reject emails from this address as spam** - the system will allow Tickets to be created for emails arriving from this address but once created, the Ticket will be automatically moved to a state of Closed with a resolution method of 'Rejected as Spam'. As Cases do not have a 'Rejected' status, any email from a blocked address will be automatically moved to your 'Unhandled email' section of your email page, rather than creating any work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FP92W0KmpcRwyAKNVjutP%2Fimage.png?alt=media\&token=05965d43-76f4-4323-a257-4993247579d8)


# Using Multiple Tabs

Enate's browser-based Work Manager uses a multi-browser page approach. You can control how you want the system to behave when you click on links to open new items, for example to open a Ticket or Action from your home page, or to open up your Email Inbox page.&#x20;

You can choose between links opening in a [new, dedicated browser tab](#multiple-browser-tabs) or in your [current browser tab](#single-browser-tab).

Watch this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ0OTgzNw==>" %}

## Single Browser Tab

As a default, when you click on a link the new content will show up in the same browser tab, replacing the previous content.&#x20;

If you want to return to the previous page, you can use the browser's 'back' button to navigate back there, and equally use the forward link again to return to the newer screen.&#x20;

Some other features which can be helpful when working with a single tab approach… The 'recently viewed' list from your navigation section is always a useful way re-find work that you've been looking at recently. You can click to open up a fresh Home page at any time… And, you can even use your focus list to put together a list of work items that you want to concentrate on, perhaps as part of a focused daily to-do list.

If you'd like to open a link in its own dedicated tab, you can right click on a link and select the 'open link in new tab' option from the subsequent menu.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCT7XhqT923AL4G481m3K%2Fimage.png?alt=media&#x26;token=7de68fdc-08ec-48e6-875e-852c304a890e" alt=""><figcaption></figcaption></figure>

Or you can hold down the 'control' or 'command' button on your keyboard when clicking the link.

This will open it in a new browser tab and leave the previous one as-is.

## Multiple Browser Tabs&#x20;

If you'd prefer that the links you click on to open in new, different browser tabs, every time you click on a link, you can do this by [changing your User Settings](#changing-your-preference-in-user-settings).

This means that you can view content in separate browser tabs and can have two sets of content open side by side, letting you, for example have your Email Inbox open at the same time as viewing a ticket or action, so you can read mails without swapping between screens. The browser tab will show information such as the work item reference and title.

Each tab has a dedicated URL which means you can easily share links to specific work items to other team members. Just copy the URL and send it to them - when they open the link it will take them straight to that work item.&#x20;

When you perform an update on a Work Item that would close the tab, you'll be returned to the page that launched it, for example your home page or Email inbox page.&#x20;

{% hint style="info" %}
If you're opening items from the Advanced Search page, save your search if you want to return to the page with the previous filters still set.&#x20;
{% endhint %}

## Changing your preference in User Settings

If you want to change how the system opens up links, you can go to your user settings page and change the tabs behaviour.&#x20;

You'll see the 'Open Links in New Browser tab' option. This lets you decide how you would like the links you click on in Enate Work Manager to open - either in a new, dedicated browser tab or in your current browser tab.&#x20;

By default, this option is set to OFF, meaning that when you click on a link the new content displays in your current browser tab. If you'd prefer that the links you click on open in new, different browser tabs, switch this option to ON and save your change. Now when you click on links, you'll see that a new dedicated browser tab will open up to show that content.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FD1cfkNbrU5D3QtOXrSXU%2Fimage.png?alt=media&#x26;token=1727669b-265a-49d2-aee4-efb9aad0c901" alt=""><figcaption></figcaption></figure>


# Focus List

The Focus List enables you to put together a list of work items that you want to concentrate on, perhaps as part of a focused daily to-do list, or as a handy shortcut to get to the items you're needing quick access to.

Watch this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM4NjYxOA==>" %}

You can add Tickets, Actions and Cases to the list, even ones which aren't assigned to you, up to a maximum of 50 items. You can get to your Focus List from anywhere in Work Manager by clicking on the Focus List icon in your header bar.&#x20;

Clicking on an item in your list will take you directly to that work item, either in a new browser tab or in the existing view if you're set to open up links that way.&#x20;

#### Adding Work Items to your Focus List

You can add items to your focus list in a few different ways:

* Firstly, you can add them from **within the Focus List itself** by clicking on the plus icon and then searching for either the title or reference number of the work item you're looking for. Select which work item or items you want to add from the search result and click to add.&#x20;
* Another way is to click on the 'Add to Focus List' icon from **within a Ticket, Action or Case**.&#x20;
* And you also can also add items to the list **from the homepage grid** by selecting one or multiple items and then clicking the 'Add to Focus List' option that appears in the grid header.&#x20;

Once they're added, work items can easily be arranged in your list, just drag and drop to relocate them.&#x20;

#### Removal of Work Items from Focus List

If you're accessing a Ticket, Case or Action which is already in your Focus List, you'll be shown that with the ticked Focus list icon. You can click on that link again to remove it from your list, or, alternatively they can easily be removed from with the list itself - select one or more, click the remove link and then confirm.&#x20;

One thing to note is that once a work item moves to a state of Resolved or Closed, it will automatically be removed from your focus list, freeing up space for other open items you want to focus on. However, users can still add items in either of these states into the Focus List if they want.&#x20;

#### Allowing Opening of Work Items from Focus List

Additionally, when a user tries to open multiple links in new tab from the Focus List, occasionally they might not be able to and will instead be shown a pop-up stating that multiple tabs have been blocked from being opened. Users simply need to click to allow pop-ups and redirects from Enate.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkLh7St1VvsKSiis0xMoT%2Fimage.png?alt=media&#x26;token=407311a1-2af8-49e9-87a8-2e99eaf37c9e" alt=""><figcaption></figcaption></figure>


# Notifications

## Overview

Enate's Notifications keep you up to date on what's happening with any Tickets, Actions and Cases you're interested in to keep you in the loop at all times. You've got lots of flexibility with how you receive notifications, in terms of which items you follow, what events you're notified about for them and how they're delivered to you.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY5Mg==>" %}

You've got various options at your disposal:

* Follow individual Work Items
* Follow all Work in your Work Inbox
* Follow all work in your Queues

## Getting notifications on Individual Work Items

### Following a Work Item

You can choose to get notifications about a particular work item - just open it in Work Manager and click the 'Follow' option in the header bar.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FReNNMiedA2BUxJdfrpvO%2Fimage.png?alt=media\&token=f8217fbe-d13d-4082-a6f0-6eda99502fe8)

While you're following a work item, you'll receive a notification whenever any of the [events you have selected in your Notification Settings](#when-and-how-to-notify-me) occur - things like changes in state, changes in its assignee, etc.. If you have [chosen to also be notified by browser pop-up and /or email](#when-and-how-to-notify-me), you will receive copies of your notifications via those channels too.

{% hint style="info" %}
Points to note:

* You can follow a work item in any state except Draft and Closed.&#x20;
* You can only follow work items that you have permissions on.
* You will never *automatically* be set to following an individual work item.&#x20;
* You can only follow an individual work item by manually clicking to follow it from its work item screen. The one exception to this rule is when you're following a Ticket and that Ticket is subsequently set to [split](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/splitting-a-ticket). In that circumstance you will automatically be set to follow all the Tickets that the original was split into.&#x20;
* When you click to follow a work item, you will only be set to following that work item and not work items that are related to it e.g. other Actions in a Case, or any[ linked work items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items).
* If you choose to follow an Action and that Action's parent Case gets reworked, you will not be notified when that Action automatically closes as part of the rework, and you will not automatically follow that Action when the new one is relaunched from the new Case. If you want to follow the Action again, you can select to do so manually.
  {% endhint %}

### Unfollowing a Work Item

You can 'Unfollow' a work item at any point by clicking 'Unfollow' from the work item screen.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVQ4CmptldU3l5tHuvR6O%2Fimage.png?alt=media\&token=780ed441-62f0-46f2-99c6-2961c0879bc2)

{% hint style="info" %}
You can only unfollow a work item by manually clicking to unfollow it or if the work item moves to a state of Closed. When a work item moves to Closed, all of the users who were following it will be set to unfollow.
{% endhint %}

## Customising Notifications

You can choose which notifications you want to receive and how by going to your [User Settings](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-settings) and clicking to view your [Notification Settings](#customising-notifications).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fw4PUNqSAnWGiUQwUGc2J%2Fimage.png?alt=media\&token=154d10f2-97ec-4e89-985a-02640d880bd3)

In addition to choosing to follow an individual work item, you can also use the notifications settings page to specify more generally which notifications you want to automatically receive. There are two parts to this:

* First, you specify which work items you want to receive, e.g. item's in your own Work Inbox.
* Further to this, you specify which *events* about those work items you want to be notified about.

See below for details ..&#x20;

### Which Items to notify me about - Scope

You can choose to receive notifications for work items in your [Work Inbox](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/home-page) and/or for work items in your [Queues](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/setting-teams-and-queues).&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfRlWd7Jk37ZjjiaYzuv5%2Fimage.png?alt=media\&token=b57de8f2-2e73-4157-a263-c02b20272092)

<table><thead><tr><th width="247.37282229965155">Work Item Type</th><th>Detail</th><th>Notes</th></tr></thead><tbody><tr><td>My Work Inbox</td><td>You will receive notifications for work items that are in your work inbox i.e. work items that are assigned to you. </td><td>This is switched on by default for all users.</td></tr><tr><td>My Queues</td><td>You will receive notifications for work items that are in Queues that you are in and/or manage. </td><td>This option is switched on by default for Team Leaders.</td></tr></tbody></table>

### Which Events to notify me about

In addition to this, you need to choose which events you want to be notified about for these Work Items.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fj8sTUxalIW8dmAFDcrW6%2Fimage.png?alt=media\&token=21b70c3b-f277-4835-80a5-3eacf181ec61)

The options are as follows:

<table><thead><tr><th>Type of Notification</th><th width="241.33333333333331">Detail</th><th>Notes</th></tr></thead><tbody><tr><td>New Information Received </td><td>A new email or Self Service Note has been received on the work item</td><td>Users subscribed to receive notifications for a work item in its related group to this (e.g. Case/Actions or the child/parent of a split Ticket) will also receive the notification.</td></tr><tr><td>Work Item Assigned to Me</td><td>Assigned user of a work item has changed to me</td><td>Only the person the work item is being assigned to will receive the notification.</td></tr><tr><td>New Work Item into Queue</td><td>Assigned Queue of a work item has changed to a Queue that I am in and/or manage</td><td></td></tr><tr><td>New File Added</td><td>A new file has been manually uploaded by an agent to the files tab of the work item</td><td>Users subscribed to receive notifications for a work item related to this (e.g. Case/Actions or the child/parent of a split Ticket) will also receive the notification.</td></tr><tr><td>Due Date 'At Risk' Reminder</td><td>Due date of the work item is deemed to be at risk. This is calculated by subtracting the expected time for the work item to take with an additional 30 minutes from the due date/time. </td><td><p>E.g. if the work item is due to be completed at 17.00 and the time expected to complete the work item is 1 hour, the Due Date 'At Risk' Reminder will be sent at 15.30. </p><p></p><p>Note that this notification will not be sent if:</p><ul><li>the work item is in a state of Draft</li><li>the work item is in a state of In Progress and assigned to a user</li><li>the work item is in a state of Waiting AND its due date has been configured with the option 'Add Wait Time To Due Date'</li></ul><p>Anyone subscribed to receive notifications for the parent of this work item (if there is one) will also receive this notification.</p></td></tr><tr><td>Work Item is Overdue</td><td>The due date of the work item has been missed and it is now overdue.</td><td>Anyone subscribed to receive notifications for the parent of this work item (if there is one) will also receive this notification.</td></tr><tr><td>Action Rejected</td><td>A robot has actively rejected an Action, or repeatedly failed to process it</td><td>Anyone subscribed to receive notifications for the parent Case of the Action will also receive this notification.</td></tr><tr><td>Case Needs Attention</td><td>A Case has encountered a problem and requires intervention before it can proceed. </td><td>Users subscribed to receive notifications for a work item Related to this (e.g. Case/Actions or the child/parent of a split Ticket) will also receive the notification. Note that the person who rejected the Action within the Case will not receive the notification.</td></tr><tr><td>Peer Review Changes</td><td>The peer review of an Action has been marked as 'Passed', 'Failed', or 'Unable to be Completed'.</td><td><p>Note that in order to receive this notification, users must:</p><ul><li>be in the Queue that this Action belongs to (or manage it), AND</li><li>be subscribed to receive notifications about this Action (being subscribed to the Case is not enough), AND</li><li>have the setting to receive notifications from 'My Queues' switched on.</li></ul><p>Additionally, the person who completed the peer review will not receive the notification.</p></td></tr></tbody></table>

{% hint style="info" %}
Note that you will only ever receive **one** notification about the same event for a work item.
{% endhint %}

### How to notify me - different types of Notifications&#x20;

For each event you subscribe to, you will automatically get notified in Work Manager in the [Notifications Centre](#notifications-centre) (via the Notifications icon in the header bar) - with a counter showing the number of unread notifications. However you can additionally choose if you also want to be notified by [email](#email-notifications) and/or by [browser pop-up](#browser-pop-up-notifications).&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8LhAwzOc2hh0CqnYWCh0%2Fimage.png?alt=media\&token=8eb36cda-a289-42d8-b07e-29b95e7898a2)

## Notifications Centre

The Notifications icon shows you how many unread notification messages you have.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqssJtvLu8cbokpO5orT6%2Fimage.png?alt=media\&token=8a30b07e-7647-42bb-beb9-cadbf2b2a9e0)

Clicking on the Notifications icon will display your Notifications Centre.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6U5zf2v4qnOpqBwjwtyi%2Fimage.png?alt=media\&token=58f46f43-7ab4-4e0a-8055-b116294d6348)

This will show the notification messages you have received (displaying the latest 100 notifications), sorted into 'All' and 'Unread'.

Clicking on the notification will take you to the work item it relates to.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FE6tiJvZ1d1bB16N5xBUh%2Fimage.png?alt=media\&token=ec662de8-21e6-4977-8ce3-c7697027078e)

You also have the option to mark individual and (from the ellipses menu) all notifications as read.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkYrNCPAnRUEvqh0AQuZt%2Fimage.png?alt=media\&token=d7277cc5-dfb8-474f-a765-9440049fdc19)

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdZ0II6txol8tZXV7zvc3%2Fimage.png?alt=media&#x26;token=3ad416dc-dc1f-4294-8e95-e38c774bcc28" alt=""><figcaption></figcaption></figure>

## Mute Notifications - Do Not Disturb

The Do Not Disturb option turns off all email and browser pop-up notifications. Note: you'll still continue to receive notifications in your Notifications Centre.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0YK7pFEqHwZfBbybq0iT%2Fimage.png?alt=media\&token=6bec4fb1-4bf7-4239-8a8c-f3926b49e560)

You can adjust your notification preferences by clicking on the 'Notification Settings' option or by going to you [User Settings](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-settings) and then clicking to view '[Notification Settings](https://docs.enate.net/enate-help/work-manager/user-settings#notification-settings)'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQygTdXD8opEnZZltLBvZ%2Fimage.png?alt=media\&token=f29cc663-7466-480b-be31-66a92e3bb627)

{% hint style="info" %}
Notifications will be sent in the user's preferred language. If a user switches to a different language, all previous notifications will remain in the previous language, but any new notifications will appear in the new preferred language.&#x20;
{% endhint %}

## Browser Pop-Up Notifications

If you have Browser pop-up notifications turned on, whenever a notification is generated they will appear on the bottom-right of your screen. Clicking on the link to the work item will take you direct to that work item.

Browser pop-up notifications will appear on any screen as long as you are logged into a Work Manager session.&#x20;

### Allowing Popup notifications in your Browser

You may need to adjust your browser settings in order for browser pop-up notifications to appear. If you need to do this, you will be alerted in the Notifications Centre.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJySNQVbdkmt5hX5zAOTJ%2Fimage.png?alt=media\&token=fca973f5-c4d1-43fd-b5c3-c6fe7e72eef8)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fxtcoc4A9MzJf5w35spFe%2Fimage.png?alt=media\&token=9070351f-5c53-40fb-969c-0a1b8fc55cb6)

To adjust your browser settings, go to Settings > Privacy and Security > Site Settings > Permissions > Notifications and adjust the settings to ensure that sites can send notifications to your browser.&#x20;

{% hint style="info" %}
Note that if Do Not Disturb is on, email notifications and browser pop-up notifications will be disabled and will no longer appear until Do Not Disturb has been switched off. Additionally, browser pop-up notifications will not appear when the browser is in incognito mode.
{% endhint %}

## Email Notifications

Email notifications will be sent to the email address that is [configured for users in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/service-agents).&#x20;

The address that the email will be sent from is [Unmonitored Email Address that has been configured in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#unmonitored-email-address).

Email notifications will contain a link to the work item they relate to. If a user is already logged in to Enate, clicking on the link will take them straight to that work item. If the user has logged out, clicking on the link will take them to the Enate log in screen. Once they have logged in, they will be taken straight to the work item.

{% hint style="info" %}
Note that if Do Not Disturb is on, email notifications and browser pop-up notifications will be disabled and will no longer appear until Do Not Disturb has been switched off.
{% endhint %}

## Desktop Notifications

### How to see Desktop Notifications

In addition to seeing your notifications within the Work Manager Notifications Centre, as browser popups and via email, you can also set to see your browser popups within various parts of your Desktop, e.g. in your windows start menu and on your machine's lock screen.

### Sounds for Desktop Notifications

Sounds can also be turned all turned on within your desktop's notifications settings to allow for sounds to play whenever a desktop notification shows.

## Turn off all Notifications

You can choose to turn off ALL notifications by selecting this option in your User Settings tab at the top of the Notifications Settings section.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fsbymj8ULsc5QtzBzvH9F%2Fimage.png?alt=media\&token=7120726f-8ba6-47e1-a644-ba1db54c8be8)

While this option is switch on, **no notifications will be generated for you**. Your preferences will have been saved for when you want to turn notifications back on.

{% hint style="info" %}
Note: If and when you choose to resume notifications, the system will begin to generate new notifications for you but any which would have been generated in the interim period will not be retrospectively created.
{% endhint %}


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


# Bulk Create Work Items

## Overview

The Bulk Create feature lets you create large numbers of Cases and/or Tickets via the uploading of data from Excel spreadsheets.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc3Nw==>" %}

You can find a link to the Bulk Create page in the ‘Bulk Create’ link in the ‘Create New Work Item’ dropdown.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FooJaBoamzT3URAqBjFqC%2F10%20Bulk%20Create.gif?alt=media&#x26;token=28fc19e2-4206-480b-bbec-418508ccb790" alt=""><figcaption></figcaption></figure>

This will bring up the Bulk Create screen in a new tab. From this screen select whether you want to bulk create Cases or Tickets. You can then download the relevant Excel template, populate it, then upload it to the page - making sure to fill in any [mandatory fields](#mandatory-fields) beforehand. &#x20;

You can download a template of the excel file. The excel templates available will conform to whichever language you currently have set in your Enate user preferences.

Once you have added the data into the excel file, save and close it, then on the Bulk Create screen click to select the file.

You can then choose if you want to allow work items with duplicate titles to be created by using the ‘Unique Title’ option. Leaving this option off allows work items with duplicate titles to be created. Switching this option on will ensure that any work item which is due to have the same title as another item in the upload file will [fail validation](#validation-errors).

Once you are happy, click on the ‘Upload’ button. This will upload your information about the Cases or Tickets from your file on-screen.

You will see the following information:

* **Total** – the total number of items contained in the uploaded file that will be created&#x20;
* **Created** – the number of items that have been created successfully (this will be zero before you start to create)
* **Issues** – the number of items with [validation issues](#validation-errors) (these need to be fixed before the items can be successfully created)
* **Not Started** – the number of items that are waiting to be created

Additionally, in the grid you will see that a 'Status' and 'Reference' column have been added - these will be filled in by the system when the items get created.

All you need to for now is to click ‘Create Items’ and the system will start creating your Cases/Tickets. The information displayed will update to show the number of items that have been successfully create and the reference numbers of the work items created.

{% hint style="info" %}
**It should be noted that excel uploads of up to 2000 rows are supported in bulk create. Sheets with more rows than this can lead to potential errors.**&#x20;
{% endhint %}

## Bulk Create Templates

If you are using version 2022.5 or above of Enate, please use the in-product templates from the bulk create page. If you are using version 2022.4 or below of Enate, please use the templates below

### Bulk Create Ticket Templates

You can download the excel file templates to bulk create Tickets from the following links:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOshXkiGInF7ld1YcvwfL%2Fbulk-create-ticket_en-gb.xlsx?alt=media&token=eff2aaba-c493-4292-b339-891254acccff>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVbsS5rlfK6s2lYXbLcV7%2Fbulk-create-ticket_en-us.xlsx?alt=media&token=a7cdc5e9-ddf6-4c97-926f-f9347de933d6>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNV5i9uYCcGGNyt5sDJXv%2Fbulk-create-ticket_fr-fr.xlsx?alt=media&token=29ce366d-7c3c-4b00-8d4d-0177a3b14171>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FznbcN7Fjl486dn5kIDhk%2Fbulk-create-ticket_de-de.xlsx?alt=media&token=e36ddc24-c4c3-4eef-a19b-99610b07c0fa>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FN4ZtAhlbNxSCwdGIBChf%2Fbulk-create-ticket_es-419.xlsx?alt=media&token=c006b1d5-152d-41cd-bbfb-49bf82c439af>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fk5dppQNgsYZIwO7N7wfX%2Fbulk-create-ticket_pt-br.xlsx?alt=media&token=4ceefdc8-042f-44ee-84a5-e67966bf07f0>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvhodJBF9Y6665GG6G0Kg%2Fbulk-create-ticket_pt-br%20(v23.1%20onwards).xlsx?alt=media&token=0f44a312-6d5c-4199-b884-7101650ab183>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeDbSxHuyu0MvTbcuO5Q0%2Fbulk-create-ticket_ro-ro.xlsx?alt=media&token=be0450e8-9545-4eac-ae3d-24e77fd53578>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ftu8Xamas8k8jDpMxFcRm%2Fbulk-create-ticket_pl-pl.xlsx?alt=media&token=3fe331db-7fd2-4851-8410-72fd87c2b8a0>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtlrMizq7KQSHQV5j1Wkw%2Fbulk-create-ticket_hu-hu.xlsx?alt=media&token=fdc5e705-d6a7-4305-ab55-8c1681a62a72>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5aFIJkdzGs4Pu9e3Jdc6%2Fbulk-create-ticket_ru-ru.xlsx?alt=media&token=b8d48fed-3968-4980-b468-c2bb8817ac4b>" %}

### Bulk Create Case Templates

You can download the excel file templates to bulk create Cases from the following links:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkzMyVMsyNx9EejJlH2VS%2Fbulk-create-case_en-gb.xlsx?alt=media&token=09fd10cc-9167-443e-85f2-bcc0c2b64391>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F392GDtfbliR1iyz0LcXD%2Fbulk-create-case_en-us.xlsx?alt=media&token=997ef861-490c-491a-a039-95dc5e2df6c8>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7zNyBDVYqR09aGqBxd2B%2Fbulk-create-case_fr-fr.xlsx?alt=media&token=c36f0624-5aba-4740-b4f2-251b3fad689b>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FxxZzicTJavcJV3BtJDlB%2Fbulk-create-case_de-de.xlsx?alt=media&token=6bd8b250-e2d6-4d31-82b1-f01f0cf910d8>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7ws0OtVe0m9ilVdFGy7E%2Fbulk-create-case_es-419.xlsx?alt=media&token=b9c9fd9e-951b-4a95-824e-3368fb9c773a>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCEFqplCDyZB455W05uJv%2Fbulk-create-case_pt-br.xlsx?alt=media&token=a6d36dd7-c8e0-4bb7-89c1-36c4e0510ddc>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FgvbslumrVcgIe1djeanh%2Fbulk-create-case_pt-br%20(v23.1%20onwards).xlsx?alt=media&token=c6e326a5-e9b6-480e-87cb-1b9c9866c3b6>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXq8Ic8OsvTS8jCahFSqe%2Fbulk-create-case_ro-ro.xlsx?alt=media&token=1f850df7-37d4-4ff4-935d-e51c3531600a>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBIxWuBnpQ5ZxGyyFgaDq%2Fbulk-create-case_pl-pl.xlsx?alt=media&token=2a366e7c-bf6a-495f-9def-5a625aa8a735>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzPfe1y7yaIqM46ejXVyg%2Fbulk-create-case_hu-hu.xlsx?alt=media&token=86a6f142-4e9d-46c1-bb04-4625033afedb>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fg2KhMWCygUeRlfbcV8AR%2Fbulk-create-case_ru-ru.xlsx?alt=media&token=67508a29-4f56-437d-9b38-ad5144583fab>" %}

## Mandatory Fields

The mandatory fields which must be filled in order to create a Case are:

* Customer
* Contract
* Service
* Case - the process name
* Title - the title for the individual Case work item.&#x20;

{% hint style="info" %}
Note that the Primary Contact and Requester fields are only mandatory for a Case when the '[Make Contacts Mandatory](https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen/creating-new-case-types-in-a-service-line#a-creating-a-new-type-of-case)' option is set to 'on' for the Case type you are bulk creating in the Service Lines screen in Builder. If you do want to fill these fields in, make sure to[ adhere to contact record requirements](#requirement-for-contact-records-within-your-bulk-upload-file).&#x20;
{% endhint %}

The mandatory fields which must be filled in order to create a Ticket are:

* Customer
* Contract
* Service
* Ticket - the process name
* Title - the title for the individual Ticket
* Ticket Description
* Ticket Category Level 1&#x20;
* Ticket Category Level 2&#x20;
* Ticket Category Level 3&#x20;
* Primary contact - the main contact you are dealing with for this query.  [See section about contact record requirements](#requirement-for-all-contact-records-within-your-bulk-upload-file).
* Requester - the contact that raised the initial request. [See section about contact record requirements](#requirement-for-all-contact-records-within-your-bulk-upload-file).

{% hint style="info" %}
Note that all data entered must match existing values in the system, otherwise [validation errors](#validation-errors) will be displayed.
{% endhint %}

### Requirement for contact records within your bulk upload file

Any contact records used in a bulk create file i.e. Primary Contact, Requester, Subject and CC contacts must adhere to the following rules:

* the email address of the contact must be used
* the contact must already exist in the system&#x20;
* the contact must be [scoped to the same customer](https://docs.enate.net/enate-help/work-manager/managing-contacts/adding-editing-and-deleting-contacts#company-name-external-contact-scoping) that the Case/Ticket will be created under

## Optional Fields

Optional fields that can be filled in for both Tickets and Cases are:

* Subject - the contact the work item is about. [See section about contact record requirements](#requirement-for-all-contact-records-within-your-bulk-upload-file).
* CC email address(es) - any further contacts which can be copied on any correspondence. [See section about contact record requirements](#requirement-for-all-contact-records-within-your-bulk-upload-file). Also note that when adding two or more CC email addresses, please make sure to separate the addresses with a semi colon (;) with no spaces either side e.g. <mark style="color:blue;"><user.one@example.net></mark>;<mark style="color:blue;"><user.two@example.net></mark>.
* Override Due Date - enter the new due date. [See date formatting section](#date-formatting).
* Do Not Send Automated Emails To Contacts - whether or not you want to send system-automated emails, such as request acknowledgement emails, to the contacts of the work item. Enter 'True' or 'False', this also applies for languages other than English.

### Date Formatting

Please be aware that any dates entered must have the following formatting:

DD-MM-YYYY HH:MM

Note that hours and minutes entered can either be in the 24 hour system format i.e. 23:00 or in the 12 hour system format with an AM/PM after it i.e. 11:00 AM.

Valid date format examples:

* 25-05-2022 23:25
* 25-05-2022 11:25 PM

If you choose not to enter hours or minutes, the system will set a default time of 00:00.

## Custom Data Fields

You can also pass custom data fields into the Cases/Tickets as they are being created. To do this, add a column name which precisely matches the data field name in Enate. If any of these bespoke fields are marked as mandatory in your Case process configuration, you MUST supply a value in this field’s column for every row in the upload file (otherwise that row will fail validation and a Case will not be created for it).

### **Supported Fields** <a href="#supported-fields" id="supported-fields"></a>

Bulk create supports below list of custom field type:

1. Check Box
2. Date Only - [see date formatting section](#date-formatting).
3. Date and Time - [see date formatting section](#date-formatting).
4. Decimal Number
5. Email Address
6. Hyperlink - note that hyperlinks with customised display text are not supported i.e. the text entered in a hyperlink field must be the entire URL of the hyperlink e.g. <https://www.enate.io/> and NOT [Enate Website](https://www.enate.io/)
7. List
8. Long Text
9. Multiple level list
10. Short Text
11. Whole Number

### **Unsupported Fields** <a href="#unsupported-fields" id="unsupported-fields"></a>

Bulk create does not support below custom field type:

1. Tables
2. Entity Relationship

Additionally, the following system property fields are not supported when bulk creating work:

1. Keep with me
2. Keep Action with me
3. Defects
4. Files

## Validation Errors

If you do have any validation errors, these will be highlighted in red and a ‘warning’ status icon will be displayed. If the input values are wrong throughout an entire column, validation errors will be displayed at the bottom of the grid e.g. if a field column is referenced in the upload file which does not exist in the system. If the input values are wrong for an individual row, a ‘warning’ status icon will be displayed at the start of the row and the individual validation errors will be highlighted in red. You will then need to modify the file, click to 'change file' and select to upload your updated file.

You can still proceed with creation of the valid Case items in your upload file. The system will skip over the invalid rows and confirm creation of the valid ones, but the invalid items will need to be resolved before they can be created. You can do this by modifying the file and then clicking to 'change file' and select to upload your updated file.

Click here to see the full list of potential validation errors for Bulk Create:

{% content-ref url="../appendix/potential-validation-errors-for-bulk-creation-of-work-items" %}
[potential-validation-errors-for-bulk-creation-of-work-items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/appendix/potential-validation-errors-for-bulk-creation-of-work-items)
{% endcontent-ref %}

## Multilingual Support

Bulk Create is also supported in all of the languages that Enate offers: French, German, Spanish, Portuguese Brazilian, Romanian, Polish, Hungarian and Russian.&#x20;

{% hint style="info" %}
Note: the bulk create template uploaded should be in the same language as the logged-in user’s preferred language. For example, if a Spanish user wants to upload a bulk create template, then the template they upload should be in Spanish.&#x20;

Additionally, the column header values in the bulk create template should match the values that are configured in Enate Builder in the [Localisations page](https://docs.enate.net/enate-help/builder/builder-2021.1/adding-localisations). If the translations for fields like Primary contact, Requester, CC, Subject or any Custom Data Fields have been modified in the Localisations page, then the column headings in the bulk create template need to match these values.
{% endhint %}


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


# Work Item Overview


# Overview of Work Item Types

There are three types of Work Item in Enate:

* [**Tickets** ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket)– Used for modelling single-part activities, e.g. queries. Tickets are standalone and are not part of a business process. Can be promoted to become a specific type of Case.
* [**Cases**](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case) – Used for modelling multi-part activities (i.e. business processes).
* [**Actions**](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action) – the constituent parts of a Case, i.e. a Case is made up of a flow of Actions. Contains a set of instructions, often a checklist of activities to track progress within the Action. These can be manual (can be carried out by humans and bots) or automatic Actions, e.g. auto sending an email.


# Adding a Note

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTYxMA==>" %}

Click the Note tab to add a note. Anyone can add an internal note to a Ticket, Case or Action – you don’t have to have it assigned to you, and adding a note won’t auto-assign the work to you. These are notes for internal use and the external contacts won’t ever see them.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MfX96dvqh9mJ9tApeXf%2F-MfXBKrOo_VJ8tN-SORW%2Fimage.png?alt=media\&token=6cc4f925-df89-40f1-8e05-9f4d9d62058d)

### Specifying note type

If desired, you can specify which kind of interaction resulted in the note, e.g. phone incoming / outgoing etc.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsVJ6OZCp08OfuY-xz%2F-MWsVcVjybKXFjoN_XRL%2Fimage.png?alt=media\&token=a9626d96-34d9-400a-b6bb-4237621b7a0f)

### Adding a note and resolving a Ticket

If we we are adding a note to a Ticket assigned to ourselves, we have the additional option of Adding a Note & Resolving the work item which will resolve the work item when we click on it.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MfX96dvqh9mJ9tApeXf%2F-MfXBUwt0-p7nKBWF9bz%2Fimage.png?alt=media\&token=b54c7ee6-8c48-4a47-be10-430441cd56d4)

After adding the note, the screen will refresh with the new note displayed on the timeline.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MfX96dvqh9mJ9tApeXf%2F-MfXBnp7N2MSHCSNGH00%2Fimage.png?alt=media\&token=3a17e1be-044f-4cef-88ec-46dc98db37d9)

### Closing an item with incomplete notes

If you have started to enter a note but have not saved it, the tab will display a ‘\*’ marker on the tab alerting you to this.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsVJ6OZCp08OfuY-xz%2F-MWsVhGYoZNhBtGo17rh%2Fimage.png?alt=media\&token=da2a8f44-af78-4451-8596-4f381119098c)

If you subsequently try to close the work item tab with this ‘in-progress’ items still unsaved, the system will alert you asking if you wish to proceed.


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


# Timeline and Comms

The timeline shows the history of activity that has taken place for a work item in a chronological list. It is divided into the [Comms Tab](#comms-tab) which shows the communications history for the work item and the [Timeline Tab](#timeline-tab) which shows all of the activity that has taken place for the work item. See the following video for more information.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc4NA==>" %}

### Timeline Icons

below you will find a full list of icons that can appear in a Work Items Timeline:

|                                                                                                                                                                                                                                                                      |                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKR5Cx3kKT8sxzHywBE1T%2Fimage.png?alt=media&#x26;token=caf06df7-aa25-4975-b70a-fddb87562077" alt="" data-size="original"> | This icon means **initial Ticket description**                                                                      |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHjGfyg1CtwIQ3XecxuS6%2Fimage.png?alt=media&#x26;token=7d68b413-fa40-42ca-b3f7-53fac7534b1c" alt="" data-size="original"> | This icon means the Work Item status was changed to **Resolved**                                                    |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fo1CdXmPEp8ym1CalXOaU%2Fimage.png?alt=media&#x26;token=827a095e-e39c-4f60-824e-10868f08a938" alt="" data-size="original"> | This icon means that the Work Item status was set to **Draft**                                                      |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FP6loEZECf3xjZThBfu4q%2Fimage.png?alt=media&#x26;token=245a3be4-4520-426e-a6d7-a5981fd7e86d" alt="" data-size="original"> | This icon means that the Work Item status was set to **To Do**                                                      |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FB0EiXoXZM4DNSAbwTmGD%2Fimage.png?alt=media&#x26;token=d86e04fe-5e1a-4bb6-a872-d20b0c506a35" alt="" data-size="original"> | This icon means that the Work Item status was set to **Wait**                                                       |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FiM0eAUl0bdii0TpWqRXh%2Fimage.png?alt=media&#x26;token=a8ec75ab-539c-471f-bdff-ad78082f0e0e" alt="" data-size="original"> | This icon means that the Work Item status was set to **In progress**                                                |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fm5DZK0z2PZSLGr35QiEC%2Fimage.png?alt=media&#x26;token=12f99e2e-4831-48dd-b6a1-2e8e05b829bb" alt="" data-size="original"> | This icon means a **note** was added to the Work Item                                                               |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fdmz98MyLpLGMLqFTVbpm%2Fimage.png?alt=media&#x26;token=96629177-30bb-46ba-a818-0c54130badfe" alt="" data-size="original"> | This icon means either the Work Item has been moved to a different **Queue** or **Reassigned** to a different user. |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fx8ctDkgABKXOaC2mWfS8%2Fimage.png?alt=media&#x26;token=444a09e7-d4b9-46bf-a0bb-da8fd573cbb8" alt="" data-size="original"> | This icon means that the Ticket Category was **set** / **changed**                                                  |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5WCEsqdkoSykMJpQ9Rez%2Fimage.png?alt=media&#x26;token=342b5d3c-c3bc-46ce-93ae-9fe7244a7f9b" alt="" data-size="original"> | This icon means that the Work Item was **re-opened**                                                                |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbBnWLR4opQKOTYcSOBUB%2Fimage.png?alt=media&#x26;token=f67979f3-f2b9-475d-bd9e-4aa9c7635640" alt="" data-size="original"> | This icon means that the Work Item was added to a **Queue**                                                         |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F9oZYd3UnXfdjjHC3cQAl%2Fimage.png?alt=media&#x26;token=d3548034-11ca-4097-bbee-f080679a90eb" alt="" data-size="original"> | This icon means the Work Item **due date was changed**                                                              |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F9r40YRLydKnaBCatUFiT%2Fimage.png?alt=media&#x26;token=6d9e24f7-6e3c-409e-afe5-a3c66e9d750d" alt="" data-size="original"> | This icon means **a email was sent out** from the Work Item                                                         |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FWZUjYWsNlNnChttyrVPs%2Fimage.png?alt=media&#x26;token=4e84a8b9-1f56-46c8-bd1c-9f83ceac106c" alt="" data-size="original"> | This icon means the Work Item **received an incoming email**                                                        |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FB2fgeRZSS4JsiMHgbVtZ%2Fimage.png?alt=media&#x26;token=b660277c-3333-402d-a727-59a830e7e769" alt="" data-size="original"> | This icon means that the Work Item's **due date was missed**                                                        |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpCAlECWUpL614JqMunj2%2Fimage.png?alt=media&#x26;token=d0ca33b6-f75f-4470-b4d2-40a1cd93aac6" alt="" data-size="original"> | This icon means **system generated** activity                                                                       |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqEv8KbSDbSzqj1ntNtbG%2Fimage.png?alt=media&#x26;token=2f210554-35d2-4ce5-971a-bf88b2c74b7f" alt="" data-size="original"> | This icon means the Work Item was **Reworked**                                                                      |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F2JfEzS8CoIIN0qmWFxS1%2Fimage.png?alt=media&#x26;token=edae1746-1c0d-4af7-a1f8-9393dffa9ff6" alt="" data-size="original"> | This icon means an **Action was completed on a Case**                                                               |
| <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FcnGvKywxL3CcQehVULlp%2Fimage.png?alt=media&#x26;token=500708e1-990a-453d-952c-7cdb997a0849" alt="" data-size="original"> | This icon means that a **Email Attachment was deleted**                                                             |

## Comms Tab

The Comms tab shows the communications history for a work item, such as emails, log activity and notes. For Tickets and Actions, the timeline section will display the Comms tab by default.&#x20;

The communications will be displayed in chronological order with the most recent at the top and the most recent email communication will be auto expanded by default. You can expand items to view them in more detail.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-MZNmcjxyLCUIqWpJlYS%2F-MZO3qL5G2XEkosNjGtc%2Fimage.png?alt=media\&token=726b0052-37c2-47fd-aed6-26c213081404)

Incoming communications which have arrived on the work item since it was last accessed by an agent will display on the timeline with a green dot to make you aware of the new communications. The green dots will clear after any manual update is made to the work item and you hit ‘Submit’. The system does not clear the green dots based purely on the work item being viewed, as it could be viewed by multiple parties. Instead, in order to ensure that the agent tasked with working on this item is aware of such recent updates an explicit update to the work item is needed before the green dot will clear.&#x20;

<div align="left"><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fujcxq4yuJNe9yq9MPOXE%2Fimage.png?alt=media&#x26;token=8ffb4cf1-cb05-42fd-9314-d148a1116042" alt=""></div>

Additionally, if another Ticket has been merged into the work item you are currently viewing, any communications from that now merged Ticket will initially display on the timeline highlighted with green dots to make you aware of the new relevant communications. These will again clear the next time the work item is manually updated.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7gfVvZuv78TGta8YFrz6%2Fimage.png?alt=media\&token=080955fa-dce2-4bc3-a6ab-f5c0467c7fac)

### Filtering the Comms Tab

You can choose which communications you wish to see on the comms timeline by clicking on the filter icon.&#x20;

The number next to the filter icon lets you know how many types of communications you are able to see out of the total number of types of communications available.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQBwuqMrDsg8MOCwELk65%2Fimage.png?alt=media\&token=b2c8fea3-2ce6-432d-b121-bddeb0c5e2f3)

You can choose to filter the Comms tab by the following communications:

#### **Email**&#x20;

* Cancelled - this shows emails that have been cancelled, when they were cancelled and who they were cancelled by

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0i0l9zlPJVjfG1ntKkJx%2Fimage.png?alt=media\&token=4ff6eee1-e14b-426d-819c-45b536c09409)

* Failed - this will shows emails that have failed to send and why they failed to send. Note that you can try to resend failed emails from the Timeline section by clicking the 'Retry' option.​

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDoc1pyuNUzaSoVblpqnJ%2Fimage.png?alt=media\&token=0bc2baa2-5efc-4d1b-85b7-f15266cccdb2)

* Incoming - this will shows emails coming in from a third party, when they arrived and who they were sent by

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FH5IhzbZbrEfkFrvmnDJY%2Fimage.png?alt=media\&token=a28b584c-4cfd-4897-804d-cdf37e0534cc)

* Outgoing - this will shows emails going out to a third party, when they were send and who they were sent by.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FK10dwABKHsGHGAZpyi0J%2Fimage.png?alt=media\&token=c073b800-6efb-40ea-ab02-060a49aeeca0)

* Scheduled - this will shows emails that are scheduled to send at a later date, when the emails are scheduled to send and who and who set the schedule. You also have the option to send the email now or to cancel the email from the Timeline. Additionally, when an Undo Send time is set, the option to send emails straight away or to cancel sending the email

  will appear in the Timeline during the Undo Send period ([see here for more information about the Undo Send option](https://docs.enate.net/enate-help/work-manager/user-settings#undo-send)) when scheduled emails are set to appear in the Timeline.​

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0nXE6YrdbWx8Wd8wsTOc%2Fimage.png?alt=media\&token=08844696-147a-43ac-bd7b-a79b79dd6e7f)

* **Log Activity**
  * Incoming and outgoing phone calls
  * Incoming and outgoing letters
* **Notes** - this shows the notes that have been added to the work item
* **Self Service** - this shows communications entered by self Service Users
* (If the work item is a Ticket) **Ticket Initial Description** - this shows the initial description under which a Ticket was submitted

### **Include related work items**&#x20;

When this is switched on, the comms tab will display communications not just from this work item, but for all related work items.

When a related work item appears on the timeline, its reference will be displayed in the timeline.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNYlJE2zatkvhDra19rnk%2Fimage.png?alt=media\&token=4bd1f0ec-56f0-41df-894e-8e1a2ddbdba7)

{% hint style="info" %}

* This setting is switched on by default for Cases so that when viewing a Case, you will also be able to see communications for all of its corresponding Actions.
* This option is switched off by default for Tickets and Actions, so they will default to only displaying communications from *this* work item.
  {% endhint %}

### **Include system generated items**

When switched on, system-generated communications such as auto-created submission confirmation emails which Enate sends out will be displayed. This option is off by default.

## Timeline Tab

The timeline tab shows the all of the activity history that has taken place for a work item, such as allocation changes, status changes and information about the quality of the work item, as well as all of the communications information that is also displayed in the comms tab.

The items will be displayed on the timeline in chronological order with the most recent at the top.

### Filtering the Timeline Tab <a href="#filtering-the-timeline-tab" id="filtering-the-timeline-tab"></a>

You can choose which activities you wish to see on the timeline by clicking on the filter icon.&#x20;

The number next to the filter icon lets you know how many types of communications you are able to see out of the total number of types of communications available.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F31is06IUjN3fEC4k5hL9%2Fimage.png?alt=media\&token=2704b031-6513-4bda-81d8-2a867064f2d3)

In addition to all the communication options, you can choose to filter the timeline tab by the following information:

**Allocations**

* Queues ​- when the work item has moved to a different Queue
* Reassignments - the shows when the work item has been reassigned to another user

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBnZbLcddhijjJihFoqtv%2Fimage.png?alt=media\&token=8bc7bece-3fb3-4d77-851f-f9101524751e)

**Ticket Description (Ticket Only)**

If a user has written an initial description of a Ticket, the timeline will display the written description.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F2IO9sZPhBQLkqBzAtkH7%2Fimage.png?alt=media&#x26;token=ee9ace2b-8e24-4dd0-8293-fa9afde4883d" alt=""><figcaption></figcaption></figure>

**Case Rework History (Cases Only)**

If a Case has been set to rework, the timeline will show who set the Case to rework, when it was set to rework, and the Step number and Action it was set to rework from.&#x20;

<div align="left"><figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnEGf3VLXnCEOpc45EtXl%2Fimage.png?alt=media&#x26;token=031d4d4a-1e88-465d-81f2-2e87e1c2af1e" alt=""><figcaption></figcaption></figure></div>

**Email Attachment Deletion**

This shows when an email attachment has been deleted. It includes the file name of the email attachment that was deleted, the subject of the email it was attached to, who deleted it and when it was deleted.&#x20;

<div align="left"><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fs4YhltV78zbXLxh2NhmB%2Fimage.png?alt=media&#x26;token=a563af17-8e52-484e-a1c0-9bd9f191c4d4" alt=""></div>

**Quality**

* Due Date Missed - this shows when the due date for the work item has been missed

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtZPmi1u6mEuhIpZ7fDy9%2Fimage.png?alt=media\&token=e5f75c8c-73c0-425d-a1a5-02cf77a30f2c)

* Due Date Changed - when the due date of the work item, the timeline will show when it has been changed to, who changed it and when they changed it

#### **Status Changes**

* this shows when the work item status was changed, what is was changed from and to (e.g. status changed from In Progress to Resolved), who it was changed by and the reason it was changed. The icon on the left will reflect the status the work item was changed to.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fpo3Z21zsfN2PngjfRfna%2Fimage.png?alt=media&#x26;token=067c7bc8-c47e-4ce4-83d8-1581db974b39" alt=""><figcaption></figcaption></figure>

* If the status has changed to Wait, the Timeline will also show the Wait type

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdL460uc7buzBSvpnrcd6%2Fimage.png?alt=media\&token=2bd09229-40c7-4dba-b0c5-c932135f5707)

* If the status has changed to Resolved, the Timeline will also show the Resolution Method
* when a Peer-Review Action is in the peer review stage
* If a Case has a problem

**Include Related Work Items**&#x20;

When this is switched on, the timeline will display information not just from this work item, but for all related work items.

When a related work item appears on the timeline, its reference will be displayed underneath the icon.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfmWIWTw0cFClaJoGIQbc%2Fimage.png?alt=media\&token=17cb4fba-73dd-48c7-8a1d-49274a179ef8)

{% hint style="info" %}

* This setting is switched on by default for Cases so that when viewing a Case, you will also be able to see information about all of its corresponding Actions.
* This option is switched off by default for Tickets and Actions, so they will default to only displaying information from *this* work item.
* The one exception is when merging a Ticket, any Tickets which were closed due to merging will default to display the information from the downstream related Ticket.
  {% endhint %}

#### **Include System-Generated Activities**

When switched on, system-generated timeline entries such as auto-created submission confirmation emails which Enate sends out will be displayed. This option is off by default.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCuTFtB2tUPSkxm33ARji%2Fimage.png?alt=media\&token=a8bbe693-28c2-456b-beb2-bc08618e76bd)

### Viewing Reopened Work Items

You can view when work items have been reopened from a resolved state in the timeline, as well as when it was reopened and by whom.

If a work item has been reopened as a result of an email, 'System' will be shown as who reopened the work item, so make sure that the ['Include System-Generated Activities'](#include-system-generated-items) option in the comms/timeline filter is enabled to see these timeline entries.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FApLxwLbtezkm6VpZ0Zwm%2Fimage.png?alt=media&#x26;token=1cbeb17c-217e-4251-a3a3-8ea9d6a2f106" alt=""><figcaption></figcaption></figure>

If a work item has been reopened by an agent, make sure the '[status changes](#status-changes)' option from the timeline filter is enabled to see these timeline entries.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fxxyuv0pdBHKI67yge3L8%2Fimage.png?alt=media&#x26;token=9e4b1ac5-a2bd-425f-9f14-713a24a31836" alt=""><figcaption></figcaption></figure>

The information about who last reopened it and when is also shown explicitly on the work item info card.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Foy5fsBvPEPTr1n8sm1bx%2Fimage.png?alt=media&#x26;token=8ef80a68-9bc3-4c83-9a46-f95b6cba76ad" alt=""><figcaption></figcaption></figure>


# Files Tab

## Overview

The files tab shows all of the files and links that have been added to that work item and its related work items, plus attachments for incoming and outgoing emails.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc5Nw==>" %}

Any files/links for the current work item which is open are displayed at the top of the files tab, and any for its related work items are shown in a separated section below this. Items are sorted by the date/time they were uploaded with the most recent at the top.&#x20;

You can see the name of the file, what type of file it is, its size, who uploaded it (and when), plus the reference number and of the work item it was uploaded to. You can also see the [tags ](#tagging-files)and [notes ](#adding-notes-to-files)that have been added to the files.

Various icons help you to identify further information:

* Standard file attachments are denoted with a paperclip icon: <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmYMqgKJ9DuXCL53PugFn%2Fimage.png?alt=media&#x26;token=310b578e-7a11-4891-85ab-3506eca6564e" alt="" data-size="line">
* Links are denoted with a links icon: ![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaccvZVAAP8tP9CW7xbLB%2Fimage.png?alt=media\&token=696ec6dd-46ed-452d-ab06-ecbea8c30808)
* Attachments from incoming emails are denoted with a green email icon: <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fvov9LZHMzNbi2WyLwjZk%2Fimage.png?alt=media&#x26;token=4815f405-f2b9-4b20-83b6-a7c2be842e46" alt="" data-size="line">
* Attachments from outgoing emails are denoted with a blue email icon: <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fn8qaklJ2nhsDejig2BF1%2Fimage.png?alt=media&#x26;token=b5758a1d-31c3-4521-ad4a-181bf7753c1a" alt="" data-size="line">

All files in the files tab are available to [add as attachments to any outgoing emails](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/attaching-files-to-an-email) and links are available to add to the email body.

{% hint style="info" %}
Please note that when upgrading from versions older than 2022.3, the files attached directly to a work item will all show in the 'Other work items' section without a reference number. Email attachments for this work item's emails *will* show in the 'Current' section however.
{% endhint %}

## Adding Files/Links to a Work Item

If the work item is assigned to you, you can add files and links to a work item in the Files tab. Multiple files can be uploaded at one time. Click the upload links at the top of the tab to upload.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5Jf2BwcDga3ug4ioTVd4%2Fimage.png?alt=media\&token=1db36f90-91ba-4ff7-9d8f-5c7324881e36)

You can also drag and drop files into the files tab to upload them.

{% hint style="info" %}
Note: The maximum size per file is 100.00 MB.&#x20;
{% endhint %}

### File Type restrictions <a href="#tagging-files" id="tagging-files"></a>

By default, all types of files can be uploaded, however filetypes *can* be restricted by specifying acceptable types in the [general settings](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#allowed-file-types) section of Builder.&#x20;

## Tagging Files and Links <a href="#tagging-files-and-links" id="tagging-files-and-links"></a>

Tags can be added to files and links. Tagging is very helpful to add more structure to your files information, and opens up features such as auto-attaching files with certain tags to emails being auto-sent by the system, and to canned responses in mails you're composing. They also allow external automation routines to know which specific files to pick up from a work item.&#x20;

Tagging files is also an important feature for processes which involve automation technology. Example: if a downstream automated Action needs to know which of the files you’ve attached to your Case is the ‘Invoice Confirmation’ file, you can tag the relevant files as such and, no matter the file name, the automation technology would know to select that file based on its tag. Such external automation technology can equally well supply tags as part of uploading documents into Work Items in Enate for further downstream manual / automated use.

The tag titles available to you are [set in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags). If you're regularly finding that a specific tag is not available to select, make sure to speak to your admin team about getting it added.

You can add a tag to a file by clicking on the '+' icon and then selecting a tag from the resulting list.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVXReQz9C20sb4udydhJF%2Fimage.png?alt=media&#x26;token=602fe6a4-3867-4b26-b40b-61bb28b2f19a" alt=""><figcaption></figcaption></figure>

You can also add tags to multiple files and links at once by selecting one or more items and using the icon which are then displayed in the Files tab header.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFg81XR81PsdWgsqxQ0SU%2Fimage.png?alt=media\&token=47b7cb6a-9956-441c-942e-1714a2abee5e)

Enate can also help with automated tagging of email attachments. Various options are available in the [Marketplace ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)section of Enate Builder to enable components (from Enate as well as third party ones) which analyse incoming mail content, including being able to suggest tags for email attachments based on their contents.&#x20;

If your admin has switched on an auto-tagging component, you'll see some extra bits of info in the file tag section, where automated suggestions of tag values for an attachment have been made.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7DjliBUjGYgVVsFAlsVK%2Fimage.png?alt=media&#x26;token=50ad2fe4-77b6-496e-8cb4-4fe37f7fc0b8" alt=""><figcaption></figcaption></figure>

If the technology you're using is confident enough about its tagging suggestion, the tag will appear in green. If you agree with the suggestion, you don't need to do anything, but if disagree with it, you can simply click to change it.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FhrGM2KnQWOm6hWEOWvmT%2Fimage.png?alt=media&#x26;token=8ca78e18-5e32-46ef-aa4e-b11d0247b8c1" alt=""><figcaption></figcaption></figure>

And if the technology was less confident in its tag suggestion, the tag will be highlighted in orange. If you agree with the suggested tag, make sure to confirm it, otherwise change it to your preference. Every time you do this, the technology will learn and get a little bit better at suggesting tags. If you notice that the technology is regularly getting its suggestions wrong, speak to your admin team about modifying the confidence threshold.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIMxyVCb2WYDXfK5CFCST%2Fimage.png?alt=media&#x26;token=b202cf44-61da-47bf-ae5c-989b964cedc1" alt=""><figcaption></figcaption></figure>

Once tags have been added, the files/links will become available for auto-adding to emails with matching tags, allowing you to ensure that all documents of a relevant type are included with specific emails / email body content.

When a [canned response](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/canned-texts) text is inserted into a manual email or when a new email is auto-created and sent in-process, the system will identify any tags linked to the canned text / email template and will then auto-attach all of that work item’s files which share the same tag. Tags are linked to the canned response / email content as part of system configuration by administrator users in Builder when creating [email templates](https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration).

{% hint style="info" %}
Note: If file tags are not [configured in your system](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags) then this ‘add file tag’ option will not be displayed.
{% endhint %}

## Adding Notes to Files

You can also add notes to files and links to provide a brief description of the content or to provide any other information that might be useful.&#x20;

You can also add notes to multiple files and links at once by selecting one or more items and using the icon which are then displayed in the Files tab header.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUXVe4me5Mn7AGqmEtmQa%2Fimage.png?alt=media\&token=7c06730b-d499-4828-bc7e-78d58984480a)

## Previewing Files

The menu on the right lets you preview an individual file. The preview will open in a new tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdTInKAI18Z8RKC4DDxsP%2Fimage.png?alt=media\&token=395d3020-5805-4e9b-a0e3-edd90351bd33)

{% hint style="info" %}
If the file is not previewable, a confirmation banner will pop up to explain this, and to offer an option to download the file. The file types supported for preview are as follows: **txt**, **pdf**, **jpg**, **jpeg**, **jpe**, **jif**, **jfif**, **jfi**, **png**, **gif**, **web**, **tiff**, **tif**, **heif**,**heic**, **svg**, **svgz**.
{% endhint %}

## Downloading Files

You can download individual files by clicking on the option in the menu on the right.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTcUK4hSDn8B2DFvlOTZD%2Fimage.png?alt=media\&token=262356ff-ade9-45a1-b5ea-75ad38d334a5)

You can download multiple files at once by selecting the files you wish to download and selecting the option at the top of the screen. These can be downloaded as multiple individual files or as a single compressed ZIP file via the ZIP download option here.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3TEpseIE3pJwc9suEBKD%2Fimage.png?alt=media\&token=217713a4-b82a-4cf6-8b41-c348b68b27e9)

## **Deleting Files/Links**

You can delete files or links individually by clicking on the menu on the right.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fwmg6Aj7ffpIiocroEfCq%2Fimage.png?alt=media\&token=2b22c488-83e1-407f-9134-5344c92a04a6)

You can also delete multiple files/links by selecting the files/links you wish to remove and selecting the delete option at the top of the screen.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FwSfryGedBt7Tlo1SUrWd%2Fimage.png?alt=media\&token=6271abc7-199c-4172-a737-e826760657b7)

## Filtering Files/Links <a href="#drag-and-drop-of-attachments-into-email-section" id="drag-and-drop-of-attachments-into-email-section"></a>

You can filter the files and links being displayed in the files tab by using the filter option at the top. You can filter by: Attachments, Outgoing Email Attachments, Incoming Email Attachments and Links.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzI5mpzWPSZIG7WKdTv1z%2Fimage.png?alt=media\&token=3f0c3b24-b17c-41a6-8725-734fa1534013)

### Freetext File Search

There's also a freetext search available to help you locate individual files or links. You can search based on the various text groups on display - Filename, Tag info and Notes texts.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPjawLOwhfaNmHFicxlnf%2Fimage.png?alt=media\&token=dd4647e9-3f81-4c61-bad1-32b704d4118a)


# Time Tracking

## Overview

To help you manage activity against your SLAs, Enate allows users to track the time it takes for work items to be completed, both as an overall total and broken out by the various resources who may have worked on it.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgwNw==>" %}

#### When is time tracked for a Work Item?

The time tracker records the time of each individual browser session that the item is worked on; time is tracked whenever a work item is open on-screen, regardless of whether it is assigned to the user or not and regardless of what state the work item is in. The time tracker runs for one single work item at a time within a browser session and will run for a work item tab when it gets browser tab focus. **It continues to run even if the browser is minimized, if the computer is in lock screen etc.**

#### Switching between tabs

In the scenario where work item A is open (with the timer running) and a further work item B tab gets opened, the timer will stop on item A and switch instead to item B. Flipping between these work item tabs would equally switch which one the time tracker is running for.&#x20;

Time tracking halts when the work item tab is closed and in the event of a browser/machine timing out.

**See here for more details about** [**when time is tracked or not tracked**](#when-is-time-tracked-not-tracked) **in the Time Tracker card.**

#### Work Item Time Tracking when accessing Email View

{% hint style="info" %}
Clicking directly on an email in any of the Email View tabs will start the time tracker running for that work item and would stop a time tracker running for any other work item tab it had been running on immediately prior to this.
{% endhint %}

## Time Tracker Card Information

The card displays the length of time of the current session, a combined total of the length of time of all previous sessions, the expected initial estimated effort time and - for Actions and Tickets - the estimated effort time which the service agent can alter, which is useful for Forecasting.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FAmE4Xc9J36r4b9lY6tiC%2Fimage.png?alt=media&#x26;token=d9558dcf-646f-45c3-ad24-1e5c4de92b6f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: You are able to pause and reset the time being recorded for the current session, regardless of whether or not you are the work item's assignee.
{% endhint %}

Additionally you can edit the time of the current *and your* previous recorded sessions, regardless of whether or not you are the work item's assignee. However please note that only Team Leaders are able to edit the time recorded by *other* members of their team, whereas Team Members are only able to edit the time recorded for their own sessions.

## Viewing Previous Recorded Sessions

Expanding the Time Tracker card displays the recorded time for previous sessions, as well as who was working on the work item during that session, how long the session lasted and if the session's recorded time has been edited.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFCzgQWsEOVRcw70mHmSQ%2Fimage.png?alt=media&#x26;token=c8c5bb9e-6d39-45e2-9172-c547fb91dc26" alt=""><figcaption></figcaption></figure>

Clicking on the information icon lets you see the date and time when the session was recorded and, if the work item is a Ticket, which category it was assigned to during that session.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPXptA7gjjJ0X6P5kOfHq%2Fimage.png?alt=media\&token=6bc977db-c457-4841-ad0f-42940070af8a)

## Editing Recorded Times <a href="#previously-recorded-times" id="previously-recorded-times"></a>

You can edit the time of the current and previous recorded sessions, regardless of whether or not you are the work item's assignee. However please note that only Team Leaders are able to edit the time recorded by other members of their team, whereas Team Members are only able to edit the time recorded for their own sessions.

Manually editing the current time-on-task will save that edited time **as a new row** in the history.&#x20;

You will be able to see further information including when an edit was made and who by when you open the card in full-screen mode.&#x20;

{% hint style="info" %}
Note that time tracker values for work performed by robots are read-only.&#x20;
{% endhint %}

### Viewing Edited Times

You can click the expand icon to open the card in full-screen mode. Here you can see the length of time of the current session, a combined total of the length of time of all previous sessions, and, for Actions and Tickets, the expected time required to complete the work item. You will also be able to see more detailed information about the individual session, as well as information about edits made to the recorded time:

| Column                        | Detail                                                                  |
| ----------------------------- | ----------------------------------------------------------------------- |
| User                          | Who was working on the work item                                        |
| Time                          | The start and end time and total length of time of the recorded session |
| Date                          | The date when the session was recorded                                  |
| Time Edited By                | Who last edited the session's recorded time                             |
| Time Edited To                | What the session's recorded time has been edited to                     |
| Date Edited                   | The date when the session's recorded time was edited                    |
| Ticket Category (Ticket Only) | The category that the Ticket was in when the time was edited            |

## 'Expected Time'

The expected time required to complete the work item can be configured in Builder for Cases, Actions and Tickets. Note that this information will only display if:

* An Initial Estimated Effort value has been entered for this Case, Action or the selected Ticket Category in Builder.
* The system-wide settings 'Show Time Tracker' and 'Display Expected Time in Time Tracker' are enabled.

***

## Ensuring Accurate Auto-Time Tracking - Recommendations

* If you only have one work item open in Enate and are currently working on a different business application, as long as you return to that tab before your Enate session expires your time will be tracked accurately.
* If you have multiple work items open in Enate and are currently working on a different business application, as long as you return to the most recently accessed tab before your Enate session expires your time will be tracked accurately. The other work items that were open but not accessed mostly recently will not have their times tracked.

### Helpful Hints and Tips (Dos and Don'ts)

In order to keep time tracking of your activities as accurate as possible, here are a few help 'Do's and Don'ts' that will optimise how the system can help while running in a web browser.&#x20;

Remember that you might have one single Enate Work item tab open, or perhaps multiple work items open in tabs in your browser.&#x20;

#### Recommended behaviour (Dos)

1. Always open the work item you want to track time against as the LAST activity in Enate before switching to another business application to work on your task.
2. Make sure to return to the Enate application at the point where you finish your task.&#x20;
3. If your activity is taking an extended period of time to complete, it's a good idea to come back to Enate from time to time, since your session may otherwise time out due to your browser timeout\*.

*\*Session timeout periods for browsers could be typically from 20 mins to several hours. If you're finding that that things are timing out like this, speak with your IT admin about how that settings can be extended to help avoid this.*

### Things that may lead to less accurate tracking (Don'ts)

1. Failing to return to Enate after finishing your work.
2. Returning to Enate too late, i.e. after a session timeout due to inactivity.
3. Logging in on a different device or browser rather than going back to the same tab you left.
4. Just clicking the 'X' on the Enate tab without having reopened it (i.e. without having clicked to display the tab content).
5. Restarting the browser before returning to the Enate tab.
6. Closing the entire browser.
7. Restarting your system.

***

## Details - Time Tracking in various scenarios <a href="#when-is-time-tracked-not-tracked" id="when-is-time-tracked-not-tracked"></a>

Time is tracked whenever a user has the Enate work item tab open either displayed or not displayed on screen. Time will not be tracked when the Time Tracker Card has been paused. \
\
You can find more detailed information about whether time is tracked or not in a particular scenario from the table below.

<table><thead><tr><th width="194">Tab Situation</th><th width="266">Scenario</th><th width="294">Running Counter Behaviour</th></tr></thead><tbody><tr><td>One Enate work item tab open</td><td><mark style="color:green;">Users performs work away from Enate, then returns to Enate before the session timeout</mark></td><td><mark style="color:green;">Time is tracked on the work item accurately. Most correct user behaviour.</mark></td></tr><tr><td>Multiple work item tabs open</td><td><mark style="color:green;">Users performs work away from Enate, then return to last focused tab before session timeout</mark></td><td><mark style="color:green;">Time is tracked on the most recently focused work item tab. Most correct user behaviour.</mark></td></tr><tr><td>Multiple work item tabs open</td><td><mark style="color:green;">Users performs work away from Enate, then returns to a different tab, not the last focused tab, before session timeout</mark></td><td><mark style="color:green;">Enate records time spent on the business application to the last focused tab, but subsequent time is added to the currently focused tab.</mark></td></tr><tr><td>Multiple work item tabs open</td><td><mark style="color:green;">Users performs work away from Enate, then clicks to switch the display of currently focussed work item tab to instead show Enate Home page</mark></td><td><mark style="color:green;">Enate stops recording time on that work item tab, and does not start automatically recording anything until another work item tab is clicked onto.</mark></td></tr><tr><td>Non-work item tab opened, no work item tabs</td><td><mark style="color:green;">Users performs work away from Enate, then returns to Enate before the session timeout</mark></td><td><mark style="color:green;">Time is not recorded as no work item tab was open. not ideal user behaviour from the time tracker feature pov.</mark></td></tr><tr><td>Non-work item tab opened, one work item tab open</td><td><mark style="color:green;">Users performs work away from Enate, then returns to Enate before the session timeout</mark></td><td><mark style="color:green;">Time is recorded accurately on the work item tab if the user visited/opened it.</mark></td></tr><tr><td>Work item tab open</td><td><mark style="color:red;">Users performs work away from Enate, then Enate Tab gets closed without reopening</mark></td><td><mark style="color:red;">Enate may not record this accurately.</mark></td></tr><tr><td>One or more Enate work item tabs open, browser minimized</td><td><mark style="color:green;">Users performs work away from Enate, then returns to Enate before the session timeout</mark></td><td><mark style="color:green;">Time is tracked on the most recently focused work item tab.</mark></td></tr><tr><td>One or more Enate work item tabs open</td><td><mark style="color:red;">Users performs work away from Enate,</mark><br><mark style="color:red;">User session times out (e.g., due to inactivity, browser closed, login in different device/browser)</mark></td><td><mark style="color:red;">Enate may not record this accurately.</mark></td></tr><tr><td>One or more Enate work item tabs open</td><td><mark style="color:green;">User navigates to Enate website and logs out successfully.</mark></td><td><mark style="color:green;">Enate accurately records time on the last focused tab.</mark></td></tr><tr><td>One or more Enate work item tabs open</td><td><mark style="color:green;">Internet connection lost, but then restored and user returns to Enate before session timeout.</mark></td><td><mark style="color:green;">Enate accurately record time on the last focused tab.</mark></td></tr><tr><td>One or more Enate work item tabs open</td><td><mark style="color:red;">System crash or unexpected shutdown. User restarts the system and returns to Enate</mark></td><td><mark style="color:red;">Time tracking may be incomplete or inaccurate due to the unexpected interruption.</mark></td></tr><tr><td>Work item tab open</td><td><mark style="color:green;">Users presses F5 / reloads the Enate tab</mark></td><td><mark style="color:green;">Time is recorded accurately on the work item tab.</mark></td></tr><tr><td>Work item tab open</td><td><mark style="color:green;">Computer is put to sleep and then resumed within User session timeout values (i.e. user wouldn't be re-asked to sign into Enate).</mark></td><td><mark style="color:green;">Time tracking will include the time the computer was asleep</mark></td></tr><tr><td>Work item tab open</td><td><mark style="color:red;">Computer is put to sleep and then resumed but </mark><em><mark style="color:red;">after</mark></em><mark style="color:red;"> the user session has timed out.</mark></td><td><mark style="color:red;">Enate may not record this accurately.</mark></td></tr></tbody></table>

## Additional Time Tracking Information

* The Enate system will always keep a record of the automatically recorded time (i.e. not manually edited). This is a record of the amount of time which the work item tab was displayed directly on screen. This data is not displayed to you but can be accessed for MI / reporting purposes. **Please note that the time tracker tracks ALL accessing of the work item, even&#x20;*****after*****&#x20;it is completed.**&#x20;
* Manually editing the current time-on-task will save that edited time as a new row in the history. The ‘time on task’ box will subsequently display the auto-running count of the time since you started the manual edit of the previously displayed value.


# Forecasting for Cases

### Overview <a href="#overview" id="overview"></a>

For users on v2024.1, they will be able to use the forecasting feature to provide more accurate estimated efforts for work items, enabling you to plan resource requirements more effectively.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTY5NTg1MQ==>" %}

In the long term, this data can be collated and fed back to admin users to adjust estimated effort timers and to provide more accurate forecasting for future work volumes.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvYu2IZLWf97qZhW7HKNF%2Fimage.png?alt=media&#x26;token=f2546618-a6fc-4dd1-a5bf-4404a2d37c53" alt=""><figcaption></figcaption></figure>

### How to use 'Forecasting' <a href="#how-to-use-forecasting" id="how-to-use-forecasting"></a>

Once the 'Forecasting' feature has been switched on, a new ‘Effort Estimation’ tab will appear in Cases in Work Manager.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F1296463846-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8xJkS0SKlesb8bmVBtGc%252Fuploads%252FLcrJP0VJlGg4kAY1Kh36%252Fimage.png%3Falt%3Dmedia%26token%3D1cc56faf-d835-4c13-ae54-761ca7ab600d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=a853b182&#x26;sv=1" alt=""><figcaption></figcaption></figure>

Here you'll see a summary of the estimated effort for the whole Case, a breakdown of the estimated effort for Actions or Sub Cases that make up the Case, and a breakdown of the estimated effort for Actions or Sub Cases that have not been created yet.

#### Case Effort Summary <a href="#case-effort-summary" id="case-effort-summary"></a>

The 'Case Effort Summary' section is where a user can change the estimated time for the Case. It also provides other useful metrics for the Case.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F076Y9o6GftPK7jbqjQOC%2Fimage.png?alt=media&#x26;token=ea15329e-c2b6-431a-aa06-04fdf2614ee8" alt=""><figcaption></figcaption></figure>

* 'Total Case Estimated Effort' effort shows the total estimated time that the Case is estimated to take. This can be updated by a user with a more accurate estimate.
  * It is the sum of the ‘Estimated’ effort of all the created work and the Actions (and Sub Case Actions) that make up the Case and the and the 'Effort for Work Not Yet Created' value
  * The field will will initially show the manual ‘[Initial Estimated Effort Per Record](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)’ value from Builder (if there is one) multiplied by the [record count](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
    * If the ‘Record Count’ gets updated, the ‘Estimated Effort’ for the Case that has not been updated by a Work Manager user will be updated to reflect the change in record count.
  * Once the Case is in a state of Resolved or Closed, its estimated effort can no longer be changed.
  * Note that increasing this value will increase the ‘Effort for Work Not Yet Created’ estimate and vice versa.
* ‘Total Case Actual Effort’ effort shows the amount of time that has been spent working on the Case Effort for Work Not Yet Created.
  * It is the sum of the 'Actual' effort for all the created Actions and Sub Cases that make up the Case, taken from their respective Time Trackers.
* ‘Total Case Remaining Effort’ shows the amount of time estimated to be left on the Case.
  * It is the sum of the 'Total Remaining Effort' effort for all the created Actions and Sub Cases that make up the Case AND the estimated remaining time for work that has yet to be created (therefore it might not always equal the 'Case Estimated' effort minus the 'Case Actual' effort).

Changing the 'Estimated' effort value for a Case has the following effects:

* Automatic update to the[ 'Effort for Work Not Yet Created' estimated value](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases#effort-for-work-not-yet-created). This is because the ‘Estimated Effort’ for the Case is a calculated value made up of the sum of the ‘Estimated’ effort of all the created work and the Actions (and Sub Case Actions) that make up the Case and the and the 'Effort for Work Not Yet Created' value.
  * Increasing the 'Estimated' effort for a Case increases the 'Effort for Work Not Yet Created' value by the same amount
  * Decreasing the 'Estimated' effort for a Case decreases the 'Effort for Work Not Yet Created' value by the same amount

#### Effort Breakdown for Created Work <a href="#effort-breakdown-for-created-work" id="effort-breakdown-for-created-work"></a>

The 'Effort Breakdown for Created Work' section is where a user can change the estimated time for the individual created Actions (and Sub Cases) that make up the Case. It also shows other useful metrics for each of the created Actions (and Sub Cases) that make up the Case.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F1296463846-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8xJkS0SKlesb8bmVBtGc%252Fuploads%252Fcnl0uwHUp7VMtMmKE9yY%252Fimage.png%3Falt%3Dmedia%26token%3D480399c4-1766-46b6-95c9-635bf60a6ad8&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=29471a23&#x26;sv=1" alt=""><figcaption></figcaption></figure>

Note that once an Action is in a state of Resolved or Closed, its estimated effort can no longer be changed.

As Actions (and Sub Cases) get created, the estimated effort for them will be taken from the Estimated effort value from the Work Not Yet Created section below.

**Action Breakdown**

For each Action, you'll see:

* A link to each Action
* 'Estimated' effort that shows the total estimated time that the Action is estimated to take. This can be updated by a user with a more accurate estimate.
  * The field will will initially show the manual ‘[Initial Estimated Effort Per Record](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)’ value from Builder multiplied by the [record count](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
    * If the ‘Record Count’ gets updated, the ‘Estimated Effort’ for any running Actions that have not been updated by a Work Manager user will be updated to reflect the change in record count.
  * Increasing this value will decrease the ‘Work Not Yet Created’ estimate and vice versa and therefore might affect the total 'Case Estimated' effort
  * Note that once an Action is in a state of Resolved or Closed, its estimated effort can no longer be changed.
* ‘Actual’ effort shows the amount of time that has so far been spent working on that Action
  * The value is taken from the Time Tracker of the Action.
* ‘Estimated Remaining’ shows the amount of time estimated to be left on the Action.
  * It is calculated by subtracting the 'Actual' effort for the Action from the 'Estimated' effort.
* The due date of the Action
  * You'll also see a 'Start By' value if the 'Actual' effort is currently zero. This value show when is the absolute latest that the Action can be started by in order to meet its due date.
* The status of the Action

Changing the 'Estimated' effort value for an Action has the following effects:

* Automatic update to the 'Effort for Work Not Yet Created' estimated value for the Case.
* Possible automatic update to the 'Estimated' effort for the whole Case

Details:

* Decreasing the 'Estimated' effort for an Action increases the 'Effort for Work Not Yet Created' value for the Case by the same amount (leaving the 'Estimated' effort for the whole Case the same).
* Increasing the 'Estimated' effort for an Action decreases the 'Effort for Work Not Yet Created' value for the Case by the same amount. This may or may not affect the 'Estimated' effort for the overall Case.
  * If the updated ‘Estimated Effort’ on an Action doesn't increase by enough to cause the ‘Effort for Work Not Yet Created’ value for the Case to go below 0, the 'Estimated' effort for the Case will not be affected
    * Example: let's say that the 'Estimated' effort for Action 1 is 2 hours, the estimated 'Effort for Work Not Yet Created' is 1 hour and the 'Estimated Effort' for the Case is 3. A user decides that Action 1 is going to take 1 hour more and so updated the 'Estimated' effort for Action 1 from 2 to 3 hours. 'Effort for Work Not Yet Created' will decrease from 1 hour to 0 and the 'Estimated' effort for the Case will not change - it will stay at 3 hours.
  * If the updated ‘Estimated Effort’ on an Action increases enough to cause the ‘Effort for Work Not Yet Created’ value for the Case to go below 0, the difference should be added to the ‘Estimated Effort’ of the overall Case.
    * Example: let's say that a Case only has one Action created for it called Action 1. The 'Estimated' effort for Action 1 is 2 hours, the estimated 'Effort for Work Not Yet Created' is 0 and therefore the 'Estimated Effort' for the whole Case is 2 hours. A user decides that Action 1 is going to take 1 hour more and so updates the 'Estimated' effort for Action 1 from 2 to 3 hours. Because 'Effort for Work Not Yet Created' is 0, the 'Estimated' effort for the overall Case is therefore going to increase by 1 hour from 2 to 3 hours.
    * Example 2: let's say that a Case only has one Action created for it called Action 1. The 'Estimated' effort for Action 1 is 2 hours, the estimated 'Effort for Work Not Yet Created' is 1 hour and therefore the 'Estimated Effort' for the whole Case is 3 hours. A user decides that Action 1 is going to take 2 more hours and so updates the 'Estimated' effort for Action 1 from 2 to 4 hours, causing the 'Effort for Work Not Yet Created' to decrease by 1 hour from 1 to 0 (decreasing as far as it can). The "remaining" 1 hour will effectively be added to the total 'Estimated' effort of the Case that will increase by 1 hour to from 3 to 4 hours.

**Sub Case Breakdown**

If a Sub Case gets created, you'll see:

* A link to the Sub Case if you have permission to access it (otherwise you'll just see the name and reference number of the Sub Case with no link)
* A Sub Case "total" row with the following:
  * 'Estimated' effort shows the total estimated time that the Sub Case is estimated to take. This can be updated by a user with a more accurate estimate.
    * It is the sum of the ‘Estimated’ effort of all the created and yet-to-be created Actions that make up the Sub Case.
    * The field will initially show the manual ‘[Initial Estimated Effort Per Record](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)’ value from Builder multiplied by the [record count](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
      * If the ‘Record Count’ gets updated, the ‘Estimated Effort’ for the Sub Case that has not been updated by a Work Manager user will be updated to reflect the change in record count.
    * Once a Sub Case is in a state of Resolved or Closed, its estimated effort can no longer be changed.
    * Note that increasing this value will increase the ‘Work Not Yet Created’ estimate for the Sub Case and vice versa.
  * ‘Actual’ effort shows the amount of time that has so far been spent working on the Sub Case.
    * It is the sum of the 'Actual' effort for all the created Actions that make up the Sub Case, taken from their respective Time Trackers.
  * ‘Estimated Remaining’ shows the amount of time estimated to be left on the Sub Case.
    * It is the sum of the 'Estimated Remaining' effort for all the created Actions that make up the Sub Case AND the estimated remaining time for work that has yet to be created for that Sub Case (therefore it might not always equal the 'Sub Case Estimated' effort minus the 'Sub Case Actual' effort)
    * The due date of the Sub Case
    * The status of the Sub Case
* A row for each Sub Case Action with the following:
  * 'Estimated' effort shows the total estimated time that the Sub Case Action is estimated to take. This can be updated by a user with a more accurate estimate.
    * The field will will initially show the manual ‘[Initial Estimated Effort Per Record](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)’ value from Builder multiplied by the [record count](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
      * If the ‘Record Count’ gets updated, the ‘Estimated Effort’ for any running Sub Case Actions that have not been updated by a Work Manager user will be updated to reflect the change in record count.
    * Increasing this value will decrease the ‘Work Not Yet Created’ Sub Case estimate and vice versa and therefore might affect the total 'Sub Case Estimated' effort
    * Once an Action is in a state of Resolved or Closed, its estimated effort can no longer be changed.
  * ‘Actual’ effort shows the amount of time that has so far been spent working on that Sub Case Action
    * The value is taken from the Time Tracker of the Sub Case Action.
  * ‘Estimated Remaining’ shows the amount of time estimated to be left on the Sub Case Action.
    * It is calculated by subtracting the 'Actual' effort for the Sub Case Action from the 'Estimated' effort.
  * The due date of the Sub Case Action
    * You'll also see a 'Start By' value if the 'Actual' effort is currently zero. This value show when is the absolute latest that the Sub Case Action can be started by in order to meet its due date.
  * The status of the Sub Case Action
* A row for 'Sub Case Work Note Yet Created' with the following:
  * 'Estimated' effort shows how much effort is estimated to be needed to complete the Sub Case Actions that have not yet been created for that Sub Case. This can be updated by a user with a more accurate estimate.
    * Changing this estimate will affect the total 'Sub Case Estimated' effort and might affect the effort estimate for the overall Case

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F1296463846-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8xJkS0SKlesb8bmVBtGc%252Fuploads%252F2WtIv48Khiu9x4nLa0vG%252Fimage.png%3Falt%3Dmedia%26token%3D07b13647-afaa-482c-bbf8-b0be5aa8761e&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6df3f1bd&#x26;sv=1" alt=""><figcaption></figcaption></figure>

Changing the 'Estimated' effort value for a Sub Case Action has the following effects:

* Automatic update to the 'Effort for Work Not Yet Created' estimated value for the Sub Case.
* Possible automatic update to the 'Estimated' effort for the whole Sub Case
* Possible automatic update to the 'Estimated' effort for the whole parent Case.

Details:

* Decreasing the 'Estimated' effort for a Sub Case Action increases the 'Effort for Work Not Yet Created' value for the Sub Case by the same amount (leaving the 'Estimated' effort for the whole Sub Case the same and therefore having no impact on the 'Estimated' effort for the whole parent Case).
* Increasing the 'Estimated' effort for a Sub Case Action decreases the 'Effort for Work Not Yet Created' value for the Sub Case by the same amount. This may or may not affect the 'Estimated' effort for the overall Case.
  * If the updated ‘Estimated Effort’ on a Sub Case Action doesn't increase by enough to cause the ‘Effort for Work Not Yet Created’ value for the Sub Case to go below 0, the 'Estimated' effort for the Sub Case will not be affected (and therefore the 'Estimated' effort for the whole parent Case will not be affected).
    * Example: let's say that a Sub Case only has one Action created for it called Sub Case Action 1. The 'Estimated' effort for Sub Case Action 1 is 2 hours and the estimated 'Effort for Work Not Yet Created' for the Sub Case is 1 hour, therefore the 'Estimated Effort' for the Sub Case is 3 hours. A user decides that Sub Case Action 1 is going to take 1 hour more and so updates the 'Estimated' effort for Sub Case Action 1 from 2 to 3 hours, causing the 'Effort for Work Not Yet Created' for the Sub Case to decrease from 1 hour to 0. The 'Estimated' effort for the Sub Case will not change - it will stay at 3 hours (and therefore the 'Estimated' effort for the whole parent Case will not be affected).
  * If the updated ‘Estimated Effort’ on a Sub Case Action increases enough to cause the ‘Effort for Work Not Yet Created’ value for the Sub Case to go below 0, the difference should be added to the ‘Estimated Effort’ of the overall Sub Case, (and therefore might impact the 'Estimated' effort for the whole parent Case).
    * Example: let's say that a Sub Case only has one Action created for it called Sub Case Action 1. The 'Estimated' effort for Sub Case Action 1 is 2 hours and the estimated 'Effort for Work Not Yet Created' for the Sub Case is 0, therefore the 'Estimated' effort for the overall Sub Case is 2 hours. A user decides that Sub Case Action 1 is going to take 1 more hour and so updates the 'Estimated' effort for Sub Case Action 1 from 2 to 3 hours. Because 'Effort for Work Not Yet Created' for the Sub Case is 0, the 'Estimated' effort for the Sub Case is going to increase by 1 hour from 2 to 3 hours.
      * If there is enough time in the 'Effort for Work Not Yet Created' of the parent Case, this 1 hour increase might be taken from there, therefore there will be no impact on the 'Estimated' effort for the whole parent Case.
      * If there is isn't enough time in the 'Effort for Work Not Yet Created' of the parent Case, this 1 hour increase will result in an increase in the the 'Estimated' effort for the whole parent Case.
    * Example 2: let's say that a Sub Case only has one Action created for it called Sub Case Action 1. The 'Estimated' effort for Sub Case Action 1 is 2 hours and the estimated 'Effort for Work Not Yet Created' for the Sub Case is 1 hour, therefore the 'Estimated' effort for the overall Sub Case is 3 hours. A user decides that Sub Case Action 1 is going to take 2 more hours and so updated the 'Estimated' effort for Sub Case Action 1 from 2 to 4 hours, causing the 'Effort for Work Not Yet Created' for the Sub Case to decrease as much as it can - here it will decrease by 1 hour to from 1 to 0. The "remaining" 1 hour will effectively be added to the total 'Estimated' effort of the Sub Case that will increase by 1 hour from 3 to 4 hours.
      * If there is enough time in the 'Effort for Work Not Yet Created' of the parent Case, this 1 hour increase might be taken from there, therefore there will be no impact on the 'Estimated' effort for the whole parent Case.
      * If there is isn't enough time in the 'Effort for Work Not Yet Created' of the parent Case, this 1 hour increase will result in an increase in the the 'Estimated' effort for the whole parent Case.

#### Effort for Work Not Yet Created <a href="#effort-for-work-not-yet-created" id="effort-for-work-not-yet-created"></a>

The 'Effort for Work Not Yet Created' section shows how much effort is estimated to be needed to complete Actions (and Sub Cases Actions) that have not yet been created for this Case.

It is calculated by subtracting the sum of the 'Estimated' effort for created work from the 'Estimated' effort for the Case. Therefore, increasing the 'Effort for Work Not Yet Created' will increase the effort estimate for the overall Case and vice versa.

As Actions (and Sub Cases) get created, the estimated effort for them will be taken from the 'Estimated Effort for Work Not Yet Created' value.

Once the Case is in a state of Resolved or Closed, the 'Effort for Work Not Yet Created' can no longer be changed.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F1296463846-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8xJkS0SKlesb8bmVBtGc%252Fuploads%252FZO0iZKS9meBe6c1Gddtg%252Fimage.png%3Falt%3Dmedia%26token%3D607ac07a-137e-48df-a68b-adaf65cf1176&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=46bdfea5&#x26;sv=1" alt=""><figcaption></figcaption></figure>


# Custom Cards

Custom Data can be added to Tickets, Cases and Actions to capture bespoke information on these work items as they run through process. The information is displayable via Custom Cards. Custom Cards can be set to display in the main section of the work item, and also as a section of the side panel on the right side of the screens.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWs_llTG6jXwcWVC3LM%2Fimage.png?alt=media\&token=0dead956-07cc-421f-addd-b0435b14d9f2)

Custom Cards can be designed (with HTML, Typescript and CSS) to surface almost any content, e.g. content from other systems.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWs_ob3QRZ_fu4GJfWP%2Fimage.png?alt=media\&token=e2d7c331-dacf-4a75-84e0-f4e8b503b5f3)

## Filling in Data Fields on Tickets, Cases and Actions <a href="#a-validation-in-smart-cards" id="a-validation-in-smart-cards"></a>

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ2MDgzNQ==>" %}

## Validation in Custom Cards <a href="#a-validation-in-smart-cards" id="a-validation-in-smart-cards"></a>

Custom Cards can be linked up to standard system validation in order to e.g. make filling in of certain data on a card a requirement before you can progress a work item.

## Custom Data Override Warning <a href="#b-custom-data-override-warning" id="b-custom-data-override-warning"></a>

If you have a work item open and are modifying custom data, Enate will check for any data conflict when you go to update the work item. Specifically, a check will be made to see if another user has accessed the work item and changed any of its custom data since you opened it. If so, a confirmation message box will be displayed to you asking whether you wish to proceed with your update (which will override their changes) or instead cancel and refresh your screen to see (and keep) those latest changes.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWs_yPpj2Ni3J3Es_sX%2Fimage.png?alt=media\&token=3272e5ac-e7e6-4ecc-8da6-bb99b4bbd1b4)


# Viewing Recently Accessed Work Items

If you wish to quickly re-access a work item (e.g. you wish to re-open a work item tab you’ve just closed down), open the ‘Recently Accessed’ link from the navigation dropdown.

This will display a list of the last 20 items which you have accessed (along with datetime the tab was closed), ordered by most recent first. Click an item to re-open the tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZDG_88DeXHfruPiq5v%2F-MZDKLQMt-j-_zOWRLmE%2FRecently-Accessed-Items.gif?alt=media\&token=60ba03ec-2ad0-46d1-982c-8eab5de3cfa9)


# Processing a Ticket


# The Ticket Screen

The Ticket screen has the same overall layout as the [Case ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/case-screen)and [Action ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/action-screen)screen, and the same basic features including [adding a note](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/adding-a-note) to a work item, [sending an email](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/composing-emails), viewing the [files and links attached](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/files-tab) and viewing the [comms/timeline](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/timeline), but it also contains some Ticket-specific features. Watch this video to find out more:&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgyMw==>" %}

## Ticket Title

At the top of the Ticket screen, you'll see the title of the Ticket.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqPpt6lcm8F6b1cQ9vKGI%2Fimage.png?alt=media\&token=b8a8c148-a32c-470b-a792-b250f397174a)

Depending on Builder settings, this may be editable throughout the duration of a Ticket.

The title of the Ticket that will appear at the top of the Ticket's tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fvwj7H3ocKKRu1DamSS3L%2Fimage.png?alt=media\&token=4c624d7c-917c-41ef-8a30-67afe1423ebc)

And the title will appear in the 'Title' column of the homepage grid for the Ticket.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F2lDOVhm5dUgiDCyVpZzf%2Fimage.png?alt=media\&token=c7f03ade-2b7d-4d93-99bc-5ab7af44072b)

You can copy the Ticket's reference and number by clicking on the copy icon in the tab:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqYmvbpA4lV9ua8CEKT4j%2Fimage.png?alt=media\&token=c31e4621-889f-4c00-8776-bd62cff205b1)

## Due Date <a href="#c-due-date" id="c-due-date"></a>

The Ticket's due date will display, colour-coded to show if the date is:

On schedule:&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoSF5hTTfJXBlLgyPxOk6%2Fimage.png?alt=media\&token=0f0922b3-f879-405a-b645-4609a58b6208)

Due today:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FGcZVxA8BPtbDFm2jMCio%2Fimage.png?alt=media\&token=6425fbf6-d706-4d8d-a85f-d0fff6049c99)

Late:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fe3h76q8sJOIIwUt34ZOM%2Fimage.png?alt=media\&token=e8f6f236-a8ce-4ad2-b970-724ffbea4308)

### Override Due Date

If a Ticket has been configured with an override due date option in Builder, then you will be able to override the due date of a Ticket by clicking on the due date in the header and changing the date in the popup.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNcmoTZkr3ag83Kcop7e3%2Fimage.png?alt=media\&token=aeb571fd-26ed-446f-a06c-6ed23942df78)

{% hint style="info" %}
Please note that if you change the category of the Ticket to a category that does *not* allow the option of overriding the due date, then the system will recalculate and use the due date that has been configured for that category in Builder.
{% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-Meyu8QEO5qWsp9liasq%2F-MeyuLfG7SAFjNFCFvUd%2Fimage.png?alt=media\&token=70e5d7cf-98b7-45d5-a97a-f7347a71dd51)

## Assignee

You can also see whether or not the Ticket has been assigned, and who to.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FR5JaAkNmWXiMd4CDKa7C%2Fimage.png?alt=media\&token=0f1d6290-acb8-475d-81e4-6b9b454c4e6d)

You are able to reassign and unassign an Ticket, or assign the Ticket to yourself if it has not been assigned to you already.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSgKbxV2MlZgaVuv82RTS%2Fimage.png?alt=media\&token=9c1a42b6-3746-4c77-8ef1-52f92bf4940c)

See here for more information about assigning work in Enate:

{% content-ref url="../assigning-reassigning-unassigning-work" %}
[assigning-reassigning-unassigning-work](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/assigning-reassigning-unassigning-work)
{% endcontent-ref %}

## Side Panel <a href="#item-access-vs-assignment-rules" id="item-access-vs-assignment-rules"></a>

### Viewing a Ticket's Status <a href="#item-access-vs-assignment-rules" id="item-access-vs-assignment-rules"></a>

In the Info Card you can see the status of the Ticket and change the status as needed.

The main label on the left side of the Info Card will display the status the Ticket is currently in. The dropdown button on the right side gives options for the states which you can move it into as part of processing.&#x20;

See here for more information about processing a Ticket:

{% content-ref url="processing-a-ticket" %}
[processing-a-ticket](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/processing-a-ticket)
{% endcontent-ref %}

{% hint style="info" %}
**Once you have selected the new status from the dropdown and filled in any further required information, click the button to confirm**.
{% endhint %}

The border of the Info Card highlights in a colour relating to the current status – once you have clicked the button to change status, the system will process the changes – the border colour and new status will change to confirm that the status update has occurred.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMzGoNhVD7NrPlJQg28C7%2Fimage.png?alt=media\&token=5d18e5c8-0eb2-48a8-8158-aabb64247c81)

When changing the status of a work item, if you are moving it to a state of 'In Progress', the work item tab will remain open upon confirming the new status. When changing to any other status, e.g. 'Wait' or 'Rejected', the tab will automatically close. A label under the Status will inform you of this in advance.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsWImGGXvpVMeCYg10%2F-MWsXAfURJOYJHxyrHjA%2Fimage.png?alt=media\&token=5a1b7150-e4a2-43a8-b066-7b9de745b561)

In addition to showing the Ticket's status, the following information is displayed directly underneath:

* Set by - who set the status
* Reason - the status change reason - i.e. why was it changed, this could be manual or as part of a process)
* Date - when the status was changed
* Last Updated By - who last changed some data on the Ticket
* Last Updated On - when some data  was last changed on the Ticket

{% hint style="info" %}
Note that not all of the above information will be displayed every time, the information that is shown depends on the status of the Ticket and how the Ticket has been configured in Builder.
{% endhint %}

### Viewing a Ticket's Settings

The Settings Card shows you detailed information about the Ticket, including:

* The name of the Ticket process
* The Ticket's context (Customer>Contract>Service>Ticket Process), plus the Ticket's category and sub categories. These can be modified by expanding the card

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FA9VNj5PZznC3Q8YoLjNH%2Fimage.png?alt=media&#x26;token=d37abbb4-c088-4fab-a6e7-648e1bfb4a4e" alt=""><figcaption></figcaption></figure>

Expanding the Settings Card will show you:

* The name of the Ticket process
* Editable versions of the Ticket's context (Customer>Contract>Service>Ticket Process), plus the Ticket's category and sub categories
* When, how and who created the Ticket
* If this Ticket was created from another work item, the initial request date shows the start date of the original request, allowing you to capture the entire length of time it has taken to complete a request.
* Keep with me - users who have this option selected will be auto assigned as the work item's owner or assignee. This can still be changed manually.
* Send Automated Emails - the option to send out automated emails e.g. Ticket acknowledgement emails to the Ticket's contacts.

Depending on if record count has been configured to be visible on a Ticket, users will also be able to see and interact with the record count on the Ticket Settings card.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ff3Z0brt10d9zVzkIeqS0%2Fimage.png?alt=media&#x26;token=a12088ba-18f0-4008-9aca-e298be3dbe30" alt=""><figcaption></figcaption></figure>

### Ticket's Contacts

The [Contacts Card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card) is where you can specify the people who relate to the Ticket.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWsYkhgFViAO0Oc0mj5%2Fimage.png?alt=media\&token=a7f14d2f-d032-49b9-bdcf-4e11fa778736)

By default, the available relationships are:

* Primary Contact – the main person you are dealing with for this Ticket. This is mandatory for Tickets.
* Requester – the person that raised the initial request. This is mandatory for Tickets.
* Subject – who the Ticket is about (this may be neither of the above).

Very often all three will be the same person.

* CCs – any further contacts which can be copied on any correspondence. When a contact is tagged only as ‘CC’, it will be displayed in the separate CCs section (hidden until any CC-only contacts exist on the work item.

{% hint style="info" %}
Note: it is possible to add further relationship types into the system. See here for more information on how to [add contact tags](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags).
{% endhint %}

#### Populating a Ticket's Contacts Card <a href="#contacts-populated-from-initial-email" id="contacts-populated-from-initial-email"></a>

*Auto-populating a Ticket's contacts*

When an email arrives from an address which is associated with a system user or an external contact which has been previously recorded in the system, then their details are automatically populated on the contacts tab when the Ticket is created by the system. They will automatically be tagged as the Requester, Subject and Primary Contact. These tags can be removed.&#x20;

Optionally the first operator to assess the Ticket can also set them as the Primary Contact if deemed appropriated by their assessment. If you tag another contact as any of these relationship types, the tag will be removed from the previous contact.

*Manually Populating a Ticket's Contact's*

A Ticket's contacts will usually be auto-populated from an initial email. However, if the Ticket's contacts are not auto-populated or if you want to add a different contact to the Ticket, you can add contacts to the Ticket manually by searching for them in the [Contacts Card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHaVmBb0E56_Q_jYnK%2F-MZHbC4BRt2U6cLKu08V%2FContact-Card-Search-for-Contact.gif?alt=media\&token=599a753b-246e-417c-af72-9df32a26189e)

If you search for a user in the Contacts Card that does not exist in the system, you can create a new contact by clicking on the ‘Create Contact’ option and filling in the contact's details.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHZHKfCwmT20z_i-95%2F-MZHa09WPZI3WlIY7Ea-%2FContact-Card-Create-Contact.gif?alt=media\&token=bd8d2355-15e2-4760-b594-6db9028823c3)

If you have written the email address for the contact, the system will decode and auto-populate the first name and last name of the contact. Once you fill in all the information and click on create contact, the system will redirect you back to the work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHNQAkYnfT4YfYPY7I%2F-MZHZ15Kudy6pBkdjKew%2FContact-Card-Email-Address.gif?alt=media\&token=971fe34f-7a7b-4a1b-a402-d0868d662d26)

When you manually add a contact they will be set as the Primary Contact, Requester and Subject by default. You can manually reassign these tags to other users afterwards.

### **Time Tracking**

To help you manage activity against your SLAs, Enate allows users to track the time it takes for work items to be completed, both as an overall total and broken out by the various resources who may have worked on it.

The Time Tracker Card in work items tracks the time of each individual browser session that the item is worked o&#x6E;**.**&#x20;

See here for more information about time trackin&#x67;**:**

{% content-ref url="../work-item-screens/time-tracker-card" %}
[time-tracker-card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/time-tracker-card)
{% endcontent-ref %}

### Custom Card

Additionally, a Custom Card can be configured to display custom data.

See here for more information:

{% content-ref url="../work-item-screens/smart-cards" %}
[smart-cards](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/smart-cards)
{% endcontent-ref %}

### Defects Card and Recording Defects

When you're working on a Ticket, Action or Case, operational issues can occur which have an effect on how you're able to deliver the process. It is important to record these as a way to highlight them for others who may view or work on the item, and to help with longer term efforts to improve process delivery.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWs_UoZmWEu7HtnHRi9%2Fimage.png?alt=media\&token=89cadaa6-2154-4333-82a0-a124d04f4058)

Watch this video to find out more about recording defects in Enate.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQzOTYyNw==>" %}

You can also go to the dedicated article to find out more:

{% content-ref url="../work-item-screens/defects-card-and-recording-defects" %}
[defects-card-and-recording-defects](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/defects-card-and-recording-defects)
{% endcontent-ref %}

## Activities Launched from the Ticket Screen

### Convert to a Case

If during processing of a Ticket query it becomes apparent that the request is better handled via a specific Case, you can support this by choosing to convert the Ticket into a Case. You can do this via the ‘Convert to Case’ option from the Ticket screen.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJR9n8Ygvvl3uQ8sRfsgD%2Fimage.png?alt=media&#x26;token=bf58bfc8-b68d-4124-8743-59c3ca8e5c44" alt=""><figcaption></figcaption></figure>

See here for more information:

{% content-ref url="convert-a-ticket-into-a-case" %}
[convert-a-ticket-into-a-case](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/convert-a-ticket-into-a-case)
{% endcontent-ref %}

### Merging a Ticket

If an incoming email creates a new Ticket instead of auto-appending itself to an already existing request, you can merge the Ticket into the other work item. You do this by selecting the 'Merge' option from the Ticket screen.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYK-BqBje8jiN_mSdIY%2F-MYK2LTO-yUjnp-axLPQ%2FMerging-Ticket-Close-This-Work-I.gif?alt=media\&token=a849a86f-d9b4-4f2d-8bc8-08299a075501)

See here for more information:

{% content-ref url="further-activities-available-for-ticket" %}
[further-activities-available-for-ticket](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/further-activities-available-for-ticket)
{% endcontent-ref %}

### Splitting a Ticket

If a Ticket contains multiple separate queries / questions which are better managed separately you can split the Ticket. You do this by clicking on the Split option from the Ticket screen.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fg99H3QhuGKsCYRu7tVk4%2Fimage.png?alt=media\&token=ab35fa19-dd74-4adc-b47f-af7a325c6b3d)

See here for more information:

{% content-ref url="splitting-a-ticket" %}
[splitting-a-ticket](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/splitting-a-ticket)
{% endcontent-ref %}

## Further Info on Ticket Screen

### New Information Received

When a new email or Self Service message has come in for a Ticket that hasn't been read yet, the New Information icon will be highlighted. Clicking on it shows you when the new information was received.&#x20;

You can choose to mark the new information as read which will set the New Information icon back to normal. You can also mark the information as unread by clicking on the 'Mark as New' option.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeDI4vt4cOwzwuhffQIOL%2FNew-Information-Icon.gif?alt=media\&token=4f358a7d-0d7f-4691-9338-aea89d4b6304)

### Standard Operating Procedure

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyijZShPp6uX9KN6ns1lN%2Fimage.png?alt=media\&token=9437dcbb-afc1-41a2-8c25-e59b49c27774)

This provides a link to the Standard Operating Procedure for the work item that has been set in Builder.&#x20;

## Customer Feedback <a href="#g-ticket-feedback-link" id="g-ticket-feedback-link"></a>

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_eBbjH3R7peUqxfS92%2F-M_e_fX_4MCjO0fPn2g5%2Fimage.png?alt=media\&token=84f0cce6-b608-450d-8664-b8c8a1953285)

If the ‘Allow Feedback’ setting is ticked in Builder (see [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen/creating-ticket-case-and-action-types-in-a-service-line#c-creating-a-new-type-of-ticket)for more information on how to do this), the Customer Feedback icon will appear in the Ticket's Header Ribbon.

It will show you your current feedback rating as well as recent customer feedback. See here for more information about [getting Customer Feedback](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/feedback-features).


# Processing a Ticket

## Initial Ticket Submission

When manually starting a Ticket directly in Enate it will sit in a state of 'Draft' until it has been submitted for the first time.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_W8pWTB-OnnGBhgDhY%2F-M_W9T5DhgK--i3rJoXK%2Fimage.png?alt=media\&token=3b57628c-856a-4bba-ba58-509f3021dfd7)

To submit a Ticket, you must:

* Add a Title
* Enter a Ticket description in the section provided (after submitting, this section will disappear and instead will show as the initial submission note).
* Set a Ticket Category in the Settings Tab - [see here for more information](#setting-a-ticket-category)
* Set a Primary Contact and a Requester in the Contacts section.

{% hint style="info" %}
Note: For manually created Tickets which have yet to have a title and description entered for them, if you send out an email prior to initial submitting (and saving) of the Ticket, the system will auto-populate the Ticket title and description from the email subject and description respectively. Upon sending an email, the email’s subject and body are copied into the Ticket’s title and description.
{% endhint %}

Then hit the ‘Submit’ button.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYJpcqcadDX115KcdK1%2F-MYJwuIT2AkgMqaH4Bpa%2FInitial-Ticket-Submission.gif?alt=media\&token=2beac51b-c929-4bce-a56a-a53699ba622b)

Once you have successfully submitted the Ticket, the Ticket will close and a confirmation pop-up will display showing that the Ticket has been submitted successfully and is now in a state of To Do.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FRb91inEPVMKXFTFpMEpb%2Fimage.png?alt=media&#x26;token=7c8ca309-d548-445a-a0fa-48ecfe7f653c" alt=""><figcaption></figcaption></figure>

You can click the Ticket reference link on this message to immediately re-open the Ticket (note that the Ticket may still be processing if you re-open the tab immediately). Alternatively, you can re-open using the ‘Recently Accessed’ link at the foot of the navigation dropdown.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fmp3bSUpBKbNrPFYwvgUl%2Fimage.png?alt=media&#x26;token=ba67e1ee-c73c-49ad-8631-26fd2ab3db02" alt=""><figcaption></figcaption></figure>

When you see a Ticket in a state of To Do, it means that it is not currently being progressed.

The Ticket will sit in a status of To Do until a resource has picked it up - this could be a human resource or a robot resource.&#x20;

Once you start updating a Ticket in a state of To Do, it will:

* automatically assign to you and&#x20;
* the status will change to ‘In progress’&#x20;

You can also choose to change the state yourself.&#x20;

When a Ticket is in a state of In Progress, this signifies that work is now underway. It will stay in that status until it’s resolved (unless it needs to be moved to a state of Wait).&#x20;

### Setting a Ticket Category

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgzMA==>" %}

You can change the category of the Ticket after it has been initially categorised and an entry will appear in the timeline showing who changed the Ticket category, when they changed it and what it has been changed to.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fn9iZlKhbBBKBiqUa0Vas%2Fimage.png?alt=media\&token=7a86dd13-9550-4c8c-879e-179034df4539)

Note that you will need to have selected the 'Ticket Category Changed' option from the [timeline filter](https://docs.enate.net/enate-help/work-manager/work-item-screens/timeline#filtering-the-timeline-tab) for this to show.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FuIVTRVTTRL7asqdTk5xg%2Fimage.png?alt=media\&token=f7330a62-5552-4f32-81d9-a6d3b503c222)

## Setting a Ticket back to 'To Do'

If you’ve picked up a Ticket in error, or if your reach the conclusion that it’s not a piece of work you’re going to be able to progress, you can unassign it from yourself, either to another resource or just back to its Queue. This could be after 10 seconds or half an hour, but when you do this the system will automatically set the status back to ‘To Do’ to let everyone know that it’s not going to be progressed until another resource picks it up. You can also just manually set the status back to ‘To Do’ if for example you started working on it in error and need to quickly undo the status change.&#x20;

Similarly, if a robot resource rejects a piece of work, its status will be set back to ‘To Do’ as part of handing it over for a human resource to carry out.

## Using 'Wait' for Tickets

If you’re working on a Ticket and you have to temporarily halt work on it because you’re waiting for some additional information or because of some other temporary blocker, you should choose the **‘Wait’** status.

When placing a Ticket into a state of 'Wait', you need to specify the type of wait. The options are:

* [Wait for more information](#wait-for-more-information)
* [Wait Until](#wait-until-specified-date)

### Wait for more information for Tickets

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgzMQ==>" %}

Impact on SLA clock: SLA clock PAUSES while a Ticket is in this state, IF the Ticket's Due Date rule (configured during process design) has  ['Add Wait Time To Due Date'](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours) set to ON. If it is set to OFF, the SLA clock CONTINUES while the Ticket is in this state.

If you’re working on a Ticket and you have to temporarily halt work on it because you’re waiting for some for some information from a third party or client, you should choose 'Wait for more information' and then add the number of days you want to wait for a response.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXD1u3AQB_NsYAgxnMk%2F-MXDPyuVAjh9G1UTKxNC%2Fimage.png?alt=media\&token=474e32cf-2605-4662-b2bf-77c183f38111)

Upon confirming the 'Wait for more information' status, the Ticket will move from your Work Inbox into your Owned Work list, as there is no active work to be carried out on it until a response is received.&#x20;

Once a response has been received, the Ticket will move back from your Owned Work list into your Work Inbox in a state of To Do, highlighted for you to progress.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8ycYPcePvj43upJd5z7p%2Fimage.png?alt=media\&token=c240f490-ac4c-468b-ac00-3f967dc49080)

Alternatively, if you have set the ‘Close if no response received’ to On, then upon reaching the number of days to wait if there has been no response received from the client, the Ticket will automatically close.

### Wait Until for Tickets

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgzMw==>" %}

Impact on SLA clock: SLA clock CONTINUES while Ticket is in this state.

If you’re working on a Ticket and you have to temporarily halt work on it until a specific future date/time, you should choose 'Wait Until'.

When you select 'Wait Until', you must specify the desired follow up date and time.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXD1u3AQB_NsYAgxnMk%2F-MXDPts0LDqsGQOvPhP6%2Fimage.png?alt=media\&token=33f79774-bfc6-481c-bb34-88c731ce21ea)

Upon confirming the 'Wait Until' status, the Ticket will move from your Work Inbox into your Owned Work list, as there is no active work to be carried out on it until the follow up date.&#x20;

When this date is reached, the Ticket will move back from your Owned Work list into your Work Inbox in a state of To Do, highlighted for you to progress.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8ycYPcePvj43upJd5z7p%2Fimage.png?alt=media\&token=c240f490-ac4c-468b-ac00-3f967dc49080)

### Set back to ‘In Progress’

Re-select this option if you wish to take the Ticket off **'**&#x57;ai&#x74;**'**.

## Resolving a Ticket

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2NjA5Mg==>" %}

You signify completing a Ticket by marking it as Resolved.&#x20;

In addition to marking the Ticket as resolved you can specify the 'Resolution Method', with the following options:

* With Customer Response
* No customer response
* Rejected
* Rejected as Spam

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MgjJQXJ7V9mjUsvhlCG%2F-MgjJoQr4gpWRHYVid4J%2Fimage.png?alt=media\&token=a45f24de-f417-480f-8e60-22c8407965ca)

The Ticket will then move to a state of Closed, unless a feedback window has been set for it, in which case it will move to a state of Resolved. See below for [more information](#feedback-window) on this.

### Resolution Email/Note

When you select to resolve a Ticket, if it has been configured this way in your system (see [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#email-or-note-required-on-ticket-in-order-to-resolve)for more information), you must either:

* Send a resolution email

or

* Add an internal resolution note

If you mark the Ticket as resolved and have not done either of these, the system will bring up a reminder message:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXByM2lAY6OkUjuloVU%2F-MXC3cmEqWWFUhkxoNiq%2Fimage.png?alt=media\&token=c6c9796a-0b69-43d4-a7dc-7981a131ed23)

If you then choose to send a resolution email, the system will show this with a green tick in the email or note:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXByM2lAY6OkUjuloVU%2F-MXC3PBDwOumD7ocllJ_%2Fimage.png?alt=media\&token=1454f093-14ca-477b-b877-5a96f5b10108)

You will then be able to mark the Ticket as resolved.

**If you have already added a resolution**

If you have just added a note or sent an email before marking as ‘resolved’, the system will automatically mark this accordingly, and will not ask you to add a further resolution confirmation.

**Subsequent Resolution Note / Email display in timeline.**

For resolved Tickets, you will be able to see the note / email which was tagged as the resolution highlighted in green with tick marker:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsfFXFZLxFZy1U7_IU%2F-MWsi5vo1W-jqmV3cEBj%2Fimage.png?alt=media\&token=8b0c92da-ce9b-455a-bbb5-808eaa7ab507)

**Quick Resolution**

For quick resolution, you can also send your resolving email and mark the Ticket as resolved in a single click. Just click the ‘Send and Resolve’ button at the foot of the email you are sending.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsfFXFZLxFZy1U7_IU%2F-MWsiBEGKGjqHSAePH37%2Fimage.png?alt=media\&token=8f6f27db-2bff-4506-9665-f73fd4c089ce)

{% hint style="info" %}
Note, this option is not available if you are sending an email from the pop-out screen. You need to come back to the main Ticket browser screen to confirm resolution of the Ticket.
{% endhint %}

### Feedback Window

After a Ticket has been resolved it may sit in that status for a brief period if a Feedback Window has been set for it - during this time period the service recipient may respond and the Ticket may be reopened, either manually using the 'Reopen' button or automatically upon receipt of a new incoming email or feedback within the time period.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MgjGfqTwBEq6S4IT-aZ%2F-MgjJOVHC8gAm76Z7RyN%2Fimage.png?alt=media\&token=c2cb74fa-7d57-4cf6-8fee-171cfb756142)

{% hint style="info" %}
Please note that when work items are reopened, the data stored for who resolved it and when it was resolved are persisted, and are not overwritten when the item is resolved for a second time.
{% endhint %}

After the feedback window has completed without any further response, the Ticket will move to a state of fully 'Closed'. Any subsequent mails received will launch a brand new work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MgjGfqTwBEq6S4IT-aZ%2F-MgjJGgYIKMF_GF9AY9J%2Fimage.png?alt=media\&token=04706672-6a3c-44fd-977e-f25a05039086)

{% hint style="info" %}
Note: You can easily move an item from draft straight through to resolved - a good example of this is a ticket query which gets resolved on first contact.
{% endhint %}


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


# Splitting a Ticket

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgzNw==>" %}

If a Ticket contains multiple separate queries / questions which are better managed separately you can split the Ticket. Click on the Split tab in the Activities tabs to start the split:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MgjfZWJIIAErBT3H87k%2F-Mgjh7sXrkAKn74mxMZX%2FSplit.png?alt=media\&token=f719bf09-042f-401f-9826-17d22e3fe829)

The screen will default split into two Tickets. You can manually add more splits if you wish by clicking on the '+' icon. The Title, Description and Context (Customer >> Ticket Category etc.) are copied from the current Ticket, but all can be modified. You can choose to keep each separate Ticket with you.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsfFXFZLxFZy1U7_IU%2F-MWsgFpxgLYjzMyloqUm%2Fimage.png?alt=media\&token=8429f65a-f633-477e-99b0-0b16898a9d1a)

Confirm the Ticket split by clicking the button in the Info card:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MgjfZWJIIAErBT3H87k%2F-Mgjg1x2qoZAG1bvt67h%2Fimage.png?alt=media\&token=725e7d80-41fb-40ad-be07-b83cf87c3610)

After splitting, the original Ticket will be set to ‘Wait– split Ticket’ with links to the new Tickets the original was split into.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MgjfZWJIIAErBT3H87k%2F-MgjhZXVqpQSVHQgeqP1%2Fimage.png?alt=media\&token=880a54c1-5623-4d32-9675-d972646e29e7)

Once the split Tickets are resolved and the feedback window if they have one has expired, this original Ticket will be set to fully complete.&#x20;

For SLA purposes the start date of the original Ticket is copied to each of the Resulting Tickets and the time when the original Ticket has been marked as Resolved is calculated as the time when the last Ticket it has been split into gets resolved.&#x20;

For example, if Ticket A has been split into Tickets B and C, and Ticket B is resolved at '2022-02-02 01:10:00' and Ticket C is resolved at '2022-02-03 02:00:00', the time marked for when Ticket A is Resolved will be '2022-02-03 02:00:00'.

You can cancel the splitting of a Ticket at any time by navigating away from the Split tab (the main Action button on the Ticket changes away from ‘Split’, so you can be sure you’re not splitting it).


# Converting a Ticket into a Case

If during the processing of a Ticket query it becomes apparent to you that the request is best handled as a Case, you may choose to convert the Ticket to a Case.'

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQyMDU5OA==>" %}

To convert a Ticket into a Case, expand the settings card of a Ticket, select 'Convert to Case' and then select the Case process you want to convert the Ticket into.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FC3wW9nkB0sBgPEd6V6rG%2F12A-Convert-Ticket-to-Case.gif?alt=media&#x26;token=7aa8a83c-9ef2-4e58-b0bf-e17a635abbfa" alt=""><figcaption></figcaption></figure>

The system will then bring up any relevant custom cards for that Case - just fill in any required data and then click on 'Start Case' in the info card.

If your system has be configured to allow you to override the due date upon Case creation, you can select a new due date here.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fes2gdiB3GRGVEVYOp0Q8%2Fimage.png?alt=media&#x26;token=e6720c7a-e9fd-42d2-891b-beb277e5071e" alt=""><figcaption></figcaption></figure>

If your system has been configured to set a schedule for a new Case upon creation in work manager, you can select a schedule here.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MhDyF3NIGJ_7AAw59ME%2F-MhDzsXyRto3IwCUlzuq%2Fimage.png?alt=media\&token=3e8a026f-8af6-4d4d-ab23-50b738650842)

You can choose to keep each separate Ticket with you by selecting 'Keep with me' in the settings card and you can choose to send an email to the primary contact for the Ticket informing them that the Ticket has been turned into a Case by selecting the 'Send Automated Emails' option.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FRgK7nx7Izii9jE4xeMNK%2Fimage.png?alt=media&#x26;token=28d8a784-4bce-4ea8-8f59-8081abbe4a56" alt=""><figcaption></figcaption></figure>

Confirm the Ticket promotion up to a Case by clicking the button in the Info card:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmHl4xeJWO1QlcxLS4Fsi%2Fimage.png?alt=media&#x26;token=c4b09315-5e96-4d1a-b337-53e101fde575" alt=""><figcaption></figcaption></figure>

You will see a confirmation messages informing you that the Ticket will be closed and replaced by a Case (with the same reference number, but a ‘-C’ ending).

The original Ticket does not form any further part of service delivery and will now be in a state of Waiting with a Resolution Method of 'Case Launched' with a link to that Case.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fi1h3P5C8NR7vbIGlSFMp%2Fimage.png?alt=media&#x26;token=db0ef38b-8d7d-466a-81e5-6678572adcd3" alt=""><figcaption></figcaption></figure>

The original Ticket will move to a state of Closed when the Case that has been launched is Closed.

The new Case launched will be in a state of To Do.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoMpqmcSPqZQnlSmB5EUa%2Fimage.png?alt=media&#x26;token=3bc41e1b-7037-42af-ab1f-80df3ea2eced" alt=""><figcaption></figcaption></figure>


# Processing a Case


# The Case Screen

The Case screen has the same overall layout as the [Ticket ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/ticket-screen)and [Action ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/action-screen)screen, and the same basic features including [adding a note](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/adding-a-note) to a work item, [sending an email](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/composing-emails), viewing the [files and links attached](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/files-tab) and viewing the [comms/timeline](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/timeline), but the Case screen also contains some Case-specific features.

## Case Title

At the top of the Case screen, you'll see the context of the Case, made up of:

Customer name - Contract name - Service name - Case Process Name

For example:&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMbplYGBxt5UkpgzCpqBv%2Fimage.png?alt=media\&token=77ea83c2-cb77-4efd-bfc7-a5df9222edfc)

The Case short description is shown on the right-hand side of the screen. If the ['Allow Title Change' option](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/case-info-section) has been selected in the Case Info tab in Builder, you will be able to edit the short description of the Case.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQmEMyo1vWZjpZN5Ujg0E%2Fimage.png?alt=media\&token=19e23d96-6120-4bdd-b335-81d207e29d39)

This is the title that will then appear at the top of the Case's tab.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmP1RCx6A1gXdsujGY7Qn%2Fimage.png?alt=media\&token=87e61ac8-e834-4583-8a92-03dfca3cccd8)

This is the title that will also appear in the 'Title' column of the homepage grid.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FEv0G2XkT48dHQxgwmZmF%2Fimage.png?alt=media\&token=d666858b-9c27-47fa-a019-b86f3bf0d84c)

You can copy the Case's reference number and title by clicking on the copy icon in the tab:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5dXDWL5q5mMy38NN4POA%2Fimage.png?alt=media\&token=f0aac113-85c5-4dea-a0a2-9165ade33733)

## Viewing the Actions of a Case

The Case screen display is laid out to emphasise visibility of the Actions which are run for it. To support this, an additional dedicated 'Actions' tab exists which allows you to quickly see the status of its Actions and to access them. This is the default displayed tab in this section for Cases.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FR2fuHSkgTGKv8Z9ZhNiC%2Fimage.png?alt=media\&token=534a7e02-5f68-43f0-b3f4-0df24191ff5c)

This tab shows the following information for any Actions under the Case:

* Current State icon
* Action reference number
* Action title and instructions
* Due Date, Assignee, Queue
* State in text form

Actions will be displayed in order of:

1. **Status**, with Actions in a status of Draft at the top, followed by Actions in a status of To Do, then In Progress, then Waiting, then Resolved, then Closed. If all the statuses are the same, then the Actions will be displayed in order of:
2. **Due date**, with the Actions due soonest at the top. If all the due dates are the same, then the Actions will be displayed in order of:
3. **Time remaining when paused**, with the Action with the least amount of time remaining when paused at the top. If the time remaining when paused is the same for all the Actions, then the Actions will be displayed in order of:
4. **Step number**, with the Action with the lowest step number at the top. If the step numbers are all the same, then the Actions will be displayed in order of:
5. **Start Date/Time**, with the Action with the most recent start date/time at the top. If the start date/time is the same for all the Actions, then the Actions will be displayed in order of:
6. **Reference number**

## Sub Cases

Sub Cases are created from an existing 'parent' Case that retain a link to their 'parent' Case will behave according to its own specific configuration, but its parent Case will not complete until all of its Sub Cases have completed.&#x20;

You can create Sub Cases by clicking on the ‘+ Work item’ link shown near the tabs section of a Case and the choose the 'Sub Case' option from the dropdown.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FRPVs2K1duEx1PUkyFffA%2Fimage.png?alt=media\&token=47113468-c47f-4597-bd60-aff2ae1ef721)

The Sub Cases tab will show the Sub Cases for that Case.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8o18I3JZ3nO3hyj0a%2FSub-Cases-Tab.gif?alt=media\&token=bd36ffad-fe23-4381-b5ff-2f74c03a9518)

See here for more information about Sub Cases:

{% content-ref url="sub-cases" %}
[sub-cases](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/sub-cases)
{% endcontent-ref %}

## Viewing Work Linked to a Case

Another feature of the Case screen is the option to launch a Case or Ticket from the Case to create a  'Linked' relationship between the work items.&#x20;

Items created in this way will retain a link to the original Case / Ticket and will show on a [Links tab](#viewing-linked-work-items-the-links-tab) within it, making it easy to track a group of work items which relate to each other.&#x20;

See here for more information:

{% content-ref url="../working-with-linked-work-items" %}
[working-with-linked-work-items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items)
{% endcontent-ref %}

## Due Date <a href="#c-due-date" id="c-due-date"></a>

The Case's due date will display, colour-coded to show if the date is:

On schedule:&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoSF5hTTfJXBlLgyPxOk6%2Fimage.png?alt=media\&token=0f0922b3-f879-405a-b645-4609a58b6208)

Due today:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FGcZVxA8BPtbDFm2jMCio%2Fimage.png?alt=media\&token=6425fbf6-d706-4d8d-a85f-d0fff6049c99)

Late:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fe3h76q8sJOIIwUt34ZOM%2Fimage.png?alt=media\&token=e8f6f236-a8ce-4ad2-b970-724ffbea4308)

### Override Due Date

If a Case has been configured with an override due date option in Builder, then you will be able to override the due date of a Case by clicking on the due date in the header and changing the date in the popup.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNcmoTZkr3ag83Kcop7e3%2Fimage.png?alt=media\&token=aeb571fd-26ed-446f-a06c-6ed23942df78)

## Assignee

You can also see whether or not the Case has been assigned, and who to.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FR5JaAkNmWXiMd4CDKa7C%2Fimage.png?alt=media\&token=0f1d6290-acb8-475d-81e4-6b9b454c4e6d)

You are able to reassign and unassign an Case, or assign the Case to yourself if it has not been assigned to you already.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSgKbxV2MlZgaVuv82RTS%2Fimage.png?alt=media\&token=9c1a42b6-3746-4c77-8ef1-52f92bf4940c)

See here for more information about assigning work in Enate:

{% content-ref url="../assigning-reassigning-unassigning-work" %}
[assigning-reassigning-unassigning-work](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/assigning-reassigning-unassigning-work)
{% endcontent-ref %}

### Case Assignment <a href="#item-access-vs-assignment-rules" id="item-access-vs-assignment-rules"></a>

Please note that Cases behave differently to Actions and Tickets in terms of assignment and how they appear in a user’s workload: **Cases do not automatically assign to users in the same way that Actions and Tickets do**, as the majority of operational work within a Case is carried out on its associated Actions. Cases will auto-assign to relevant users where work has been explicitly escalated or requires direct intervention by the Case Owner.&#x20;

As a result, **Cases do not typically populate a user’s Work Inbox**, which is reserved for actionable items requiring immediate user input. Instead, Cases are visible in the **Owned Work** section, allowing users to retain ownership and oversight of the Case while focusing their inbox on active Actions and Tickets. In short: if you see a Case item in your Work Inbox, it will most likely be because something has happened at the Action level which needs your input or new information has been received at the Case level that you can review such as the merging of a Ticket to the Case or the arrival of an inbound email.

## Side Panel <a href="#item-access-vs-assignment-rules" id="item-access-vs-assignment-rules"></a>

### Viewing the Status of a Case <a href="#item-access-vs-assignment-rules" id="item-access-vs-assignment-rules"></a>

In the Info Card you can see the status of the Case and change the status as needed.

The main label on the left side of the Info Card will display the status the Case is currently in. The dropdown button on the right side gives options for the states which you can move it into as part of processing.&#x20;

See here for more information about processing a Case:

{% content-ref url="processing-a-case" %}
[processing-a-case](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/processing-a-case)
{% endcontent-ref %}

{% hint style="info" %}
**Once you have selected the new status from the dropdown and filled in any further required information, click the button to confirm**.
{% endhint %}

The border of the Info Card highlights in a colour relating to the current status – once you have clicked the button to change status, the system will process the changes – the border colour and new status will change to confirm that the status update has occurred.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMzGoNhVD7NrPlJQg28C7%2Fimage.png?alt=media\&token=5d18e5c8-0eb2-48a8-8158-aabb64247c81)

When changing the status of a work item, if you are moving it to a state of 'In Progress', the work item tab will remain open upon confirming the new status. When changing to any other status, e.g. 'Wait' or 'Rejected', the tab will automatically close. A label under the Status will inform you of this in advance.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsWImGGXvpVMeCYg10%2F-MWsXAfURJOYJHxyrHjA%2Fimage.png?alt=media\&token=5a1b7150-e4a2-43a8-b066-7b9de745b561)

In addition to showing the Case's status, the following information is displayed directly underneath:

* Set by - who set the status
* Reason - the status change reason - i.e. why was it changed, this could be manual or as part of a process)
* Date - when the status was changed
* Last Updated By - who last changed some data on the Ticket
* Last Updated On - when some data  was last changed on the Ticket

{% hint style="info" %}
Note that not all of the above information will be displayed every time, the information that is shown depends on the status of the Ticket and how the Ticket has been configured in Builder.
{% endhint %}

### Viewing the Settings of a Case

The Settings Card shows you detailed information about the Case, including:

* The context of the Case (Customer>Contract>Service>Case Process).&#x20;
* When, how and who created the Case
* If this Case was created from another work item, the initial request date shows the start date of the original request, allowing you to capture the entire length of time it has taken to complete a request.
* Keep with me - a user who is the owner of a Case will be alerted and assigned to the Case when new developments such as the arrival of an inbound email or the merging with a Ticket occurs. Once the user acknowledges the new information, they will be automatically unassigned from the Case, however they will still remain as the owner of the Case.&#x20;
* Keep Action with me - all future Actions within a Case will automatically be assigned to the user who has the "Keep Action with me" option selected.
* Send Automated Emails - the option to send automated emails for the Case. At the moment, the only automated email available to send for cases is a Case creation acknowledgement email.&#x20;
* Record Count - depending on configuration for the Case in Builder, the record count may or may not be displayed here. If it is, the record count is editable.

### Case's Contacts

The [Contacts Card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card) is where you can specify the people who relate to the Case.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWsYkhgFViAO0Oc0mj5%2Fimage.png?alt=media\&token=a7f14d2f-d032-49b9-bdcf-4e11fa778736)

By default, the available relationships are:

* Primary Contact – the main person you are dealing with for this Case. This is may or may not be mandatory for Cases, depending upon Case configuration in Builder.
* Requester – the person that raised the initial request. This is may or may not be mandatory for Cases, depending upon Case configuration in Builder.
* Subject – who the Case is about.

Very often all three will be the same person.

* CCs – any further contacts which can be copied on any correspondence. When a contact is tagged only as ‘CC’, it will be displayed in the separate CCs section (hidden until any CC-only contacts exist on the work item.

{% hint style="info" %}
Note: it is possible to add further relationship types into the system. See here for more information on how to [add contact tags](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags).
{% endhint %}

A Case's Contacts Card will not usually be auto-populated, so you need to manually add a contact. You can do this by searching for a contact in the [Contacts Card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHaVmBb0E56_Q_jYnK%2F-MZHbC4BRt2U6cLKu08V%2FContact-Card-Search-for-Contact.gif?alt=media\&token=599a753b-246e-417c-af72-9df32a26189e)

If you search for a user in the Contacts Card that does not exist in the system, you can create a new contact by clicking on the ‘Create Contact’ option and filling in the contact's details.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHZHKfCwmT20z_i-95%2F-MZHa09WPZI3WlIY7Ea-%2FContact-Card-Create-Contact.gif?alt=media\&token=bd8d2355-15e2-4760-b594-6db9028823c3)

If you have written the email address for the contact, the system will decode and auto-populate the first name and last name of the contact. Once you fill in all the information and click on create contact, the system will redirect you back to the work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHNQAkYnfT4YfYPY7I%2F-MZHZ15Kudy6pBkdjKew%2FContact-Card-Email-Address.gif?alt=media\&token=971fe34f-7a7b-4a1b-a402-d0868d662d26)

When you manually add a contact they will be set as the Primary Contact, Requester and Subject by default. You can manually reassign these tags to other users afterwards.

### **Time Tracking**

To help you manage activity against your SLAs, Enate allows users to track the time it takes for work items to be completed, both as an overall total and broken out by the various resources who may have worked on it.

The Time Tracker Card in work items tracks the time of each individual browser session that the item is worked o&#x6E;**.**&#x20;

See here for more information about time tracking:

{% content-ref url="../work-item-screens/time-tracker-card" %}
[time-tracker-card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/time-tracker-card)
{% endcontent-ref %}

### Custom Card

Additionally, a Custom Card can be configured to display custom data..

See here for more information:

{% content-ref url="../work-item-screens/smart-cards" %}
[smart-cards](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/smart-cards)
{% endcontent-ref %}

### Defects Card and Recording Defects

When you're working on a Ticket, Action or Case, operational issues can occur which have an effect on how you're able to deliver the process. It is important to record these as a way to highlight them for others who may view or work on the item, and to help with longer term efforts to improve process delivery.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWs_UoZmWEu7HtnHRi9%2Fimage.png?alt=media\&token=89cadaa6-2154-4333-82a0-a124d04f4058)

Watch this video to find out more about recording defects in Enate.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQzOTYyNw==>" %}

You can also go to the dedicated article to find out more:

{% content-ref url="../work-item-screens/defects-card-and-recording-defects" %}
[defects-card-and-recording-defects](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/defects-card-and-recording-defects)
{% endcontent-ref %}

## Activities Launched from the Case screen&#x20;

### Reworking a Case

If issues have occurred during the running of a Case you may wish to rework the Case. You can do this from the Case by selecting the ‘Rework’ tab from the Case screen.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOgKd6o9jNbybVgWFwMGX%2Fimage.png?alt=media\&token=24f27c4f-7ed2-42c5-a3c8-0dfaf223c8cd)

See here to find out more about reworking a Case:

{% content-ref url="reworking-a-case" %}
[reworking-a-case](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/reworking-a-case)
{% endcontent-ref %}

### Starting an Action Manually

Most often the Actions in a Case are started automatically (either by process flow or based on schedules). However, if an Action has been configured to be manually startable, you can do this from the Case using the 'Start Action' feature.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCM2BplPeHi2ilI16Jaj3%2Fimage.png?alt=media\&token=b065dd5c-7f7b-4678-ab20-787614bf5444)

See here to find out more about manually launching an Action from a Case:

{% content-ref url="activities-available-for-case" %}
[activities-available-for-case](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/activities-available-for-case)
{% endcontent-ref %}

## Further info on the Case screen

### New Information Received

When a new email has come in for a Case that hasn't been read yet, the New Information icon will be highlighted. Clicking on it shows you when the new email was received.&#x20;

You can choose to mark the new information as read which will set the New Information icon back to normal. You can also mark the information as unread by clicking on the 'Mark as New' option.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeDI4vt4cOwzwuhffQIOL%2FNew-Information-Icon.gif?alt=media\&token=4f358a7d-0d7f-4691-9338-aea89d4b6304)

### Standard Operating Procedure

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyijZShPp6uX9KN6ns1lN%2Fimage.png?alt=media\&token=9437dcbb-afc1-41a2-8c25-e59b49c27774)

This provides a link to the Standard Operating Procedure for the work item that has been set in Builder.&#x20;


# Processing a Case

## Initial Case Submission

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTg1NA==>" %}

Cases can be started in the following ways:

* Via an incoming email (if the system is configured to do so for that email mailbox)
* By a ‘Start Case’ Action within another Case flow.
* Manually, from the ‘Create New Work Item’ link in the Work Manager toolbar
* Automatically started
* Via third party integrations

## How Cases move through the different states

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTg2NQ==>" %}

When manually starting a Case directly in Enate, it will sit in a state of 'Draft' until it has been submitted for the first time.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_W8pWTB-OnnGBhgDhY%2F-M_W9l3jTOTWjfELfwoZ%2Fimage.png?alt=media\&token=89ddbaf4-7ba7-4d3f-b35d-c27b86a80518)

When starting manually, you should fill in the ‘Case Short Description’.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsy10QGFwapNDi9Yhz%2F-MWszrIkYzS2Po4X-rzW%2Fimage.png?alt=media\&token=0b8a5884-45ac-469a-8086-2145cd2c25a0)

Once a Case has been submitted into Enate, it will then sit in a status of ‘To Do’ until a resource has picked it up - this could be a human resource or a robot resource. Once you start updating a Case sitting in this state, it will:

* automatically assign to you and&#x20;
* the status will change to ‘In progress’&#x20;

You can also choose to change the state yourself. This signifies that work is now underway and it will stay in that status until it’s resolved – assuming e.g. no waiting for further information.

## Setting an Item back to 'To Do'

If you’ve picked up a Case in error, or if your reach the conclusion that it’s not a piece of work you’re going to be able to progress you can unassign it from yourself, either to another resource or just back to its Queue. This could be after 10 seconds or half an hour, but when you do this the system will automatically set the status back to ‘To Do’ to let everyone know that it’s not going to be progressed until another resource picks it up. You can also just manually set the status back to ‘To Do’ if for example you started working on it in error and need to quickly undo the status change.&#x20;

Similarly if a robot resource rejects a piece of work, its status will be set back to ‘To Do’ as part of handing it over for a human resource to carry out.

### Needs Attention

Additionally, if there is a problem with a Case (usually be because of an issue with one of its Actions), the Case will be put back into a state of 'To Do'.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FLbHJAzTQ8GVVuv7m9qhD%2Fimage.png?alt=media\&token=393fa147-87e5-447e-97a5-3b4404bf331d)

Once the Case is in this state, the Case owner can see this along with the reason – i.e. often the problem Action in the Info Card. As Case Owner, you have various options available to you:

* Rework the Case from a previous step or from completed Actions within this step
* Place the Case on Wait - Pause
* Reset the Case to In Progress
* Manually launch / re-launch Actions

## Using 'Wait' state for a Case

If you’re working on a Case and you have to temporarily halt work on it because you’re waiting for some additional information or because of some other temporary blocker, you should choose the **‘Wait’** status.

When a Case is in a state of Waiting, no more new Actions for that Case will be launched until the Case moves back into a state of To Do or In Progress. Users can complete Actions that have already launched and are already running Actions, but once these Actions have been completed, no new Actions will get launched.

When placing a Case into a state of 'Wait' you need to specify the type of wait. The options are:

* [Wait for more information](#wait-for-more-information)
* [Wait Until](#wait-until-follow-up-date)
* [Pause](#pause)

### 'Wait for more information' for a Case

Impact on SLA clock: SLA clock PAUSES while Case is in this state, IF the Case's Due Date rule (configured during process design) has  ['Add Wait Time To Due Date'](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours) set to ON. If it is set to OFF, the SLA Clock CONTINUES while Case is in this state.

If you’re working on a Case and you have to temporarily halt work on it because you’re waiting for some information from a third party or client, you should choose 'Wait for more information'.

When a Case is in a state of Waiting, no more new Actions for that Case will be launched until the Case moves back into a state of To Do or In Progress. Users can complete Actions that have already launched and are already running Actions, but once these Actions have been completed, no new Actions will get launched.

When you click on 'Wait for more information', you must choose the reason for placing the Case in that state from the dropdown list.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXD1u3AQB_NsYAgxnMk%2F-MXDIonXyIdFG01Maek3%2Fimage.png?alt=media\&token=a5c5860c-a208-444c-b76c-b898c505c427)

Upon confirming the 'Wait for more information' status, the Case will move from your Work Inbox into your Owned Work list, as there is no active work to be carried out on it until a response is received.&#x20;

Once a response has been received, the Case will move back from your Owned Work list into your Work Inbox in a state of To Do, highlighted for you to progress.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvVFaKqLZmQ2fzOU5DwDQ%2Fimage.png?alt=media\&token=5bc9d2f5-2113-4513-b0e1-44d602d8caef)

#### What shows for Due Date when SLA Clock pauses on Cases in 'Waiting for more Information'

The Remaining Hours of SLA when a Case is set to 'Waiting for more Information' will be displayed. To explain..

If a Case is set to 'Waiting for more Information' and the option to ['Add Wait Time To Due Date'](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours) is set to ON in the Case's Due Date rule (defined during process design in Builder), then the system will PAUSE the SLA clock. In conjunction with this, the Due Date value normally displayed on the Case header bar will be hidden (because until the SLA clock starts again, we can't know it!). In its place, the system will show the remaining time which was left until the Case is due at the point where it was put into this state (or how long it was overdue at the point where it was put into this state, if it has already passed the due date).&#x20;

Example: If the Case is yet to pass the due date the the message will show as ‘**Due: Paused** x **h** y **m before due**’.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPd2E6BAyvid2l8AfJ0F7%2Fimage.png?alt=media\&token=24d642e7-a3fb-463f-b290-54a1e2b80369)

Example: If the work has passed the due date then the message will show as ‘**Due: Paused** x **h** y **m after overdue**’.

### 'Wait Until' for a Case

Impact on SLA Clock: SLA Clock CONTINUES while Case is in this state.

If you’re working on a Case and you have to temporarily halt work on it until a specific future date/time, you should choose 'Wait Until'.

When a Case is in this state, no more new Actions for that Case will be launched until the Follow Up Datetime has been reached. Users can complete Actions that have already launched and are already running Actions, but once these Actions have been completed, no new Actions will get launched.

When you click on 'Wait Until', you must specify the desired follow up date and time.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXCwVfR_igRXin3gGYz%2F-MXD1g0alYl0hhzBhlBP%2Fimage.png?alt=media\&token=705c1610-1357-4e43-ad9f-6990c5769321)

Upon confirming the 'Wait Until' status, the Case will move from your Work Inbox into your Owned Work list, as there is no active work to be carried out on it until the follow up date.&#x20;

When this date is reached, the Case will move back from your Owned Work list into your Work Inbox in a state of To Do, highlighted for you to progress.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvVFaKqLZmQ2fzOU5DwDQ%2Fimage.png?alt=media\&token=5bc9d2f5-2113-4513-b0e1-44d602d8caef)

### 'Pause' for a Case

Impact on SLA Clock: SLA Clock CONTINUES while Case is in this state.

If you’re working on a Case and you have to temporarily halt work on it, but you are not waiting for some information from a third party or client, or waiting until a specific future date/time, you should choose 'Pause'.

When a Case is in a state of Waiting, no more new Actions for that Case will be launched until  a user actively changes the status of the Case to To Do or In Progress. There is no automatic way of taking a Case out of a state of Pause, it can only be done manually. Users can complete Actions that have already launched and are already running Actions, but once these Actions have been completed, no new Actions will get launched.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXCwVfR_igRXin3gGYz%2F-MXD1rsCFBVbVyYpSUDc%2Fimage.png?alt=media\&token=7630cf52-70cb-45d9-b639-9f6c2ad1d02e)

Upon confirming the 'Pause' status, the Case will move from your Work Inbox into your Owned Work list, as there is no active work to be carried out on it by you until a user actively changes the status of the Case to To Do or In Progress.&#x20;

When this is done, the Case will move back from your Owned Work list into your Work Inbox in a state of To Do, highlighted for you to progress.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvVFaKqLZmQ2fzOU5DwDQ%2Fimage.png?alt=media\&token=5bc9d2f5-2113-4513-b0e1-44d602d8caef)

## Resolving a Case

When all the actions in a Case are completed, the system will move the Case into a state of 'Resolved' if the Case has been [configured with a feedback window](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/case-info-section#case-info-tab). It will sit in this status for a brief period during which the service recipient may respond and the Case may be reopened, either manually or automatically upon receipt of a new incoming email or feedback within the time period.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MfDZBGtUv2atxGtZJ45%2F-MfD_ek9lcl7RWfbWyiI%2Fimage.png?alt=media\&token=cb1d85af-16da-4a46-ad88-8d507e8d6851)

{% hint style="info" %}
Please note that when work items are reopened, the data stored for who resolved it and when it was resolved are persisted and are not overwritten when the item is resolved for a second time.
{% endhint %}

After the feedback window has completed without any further response, or if the Case does not have a feedback window, the Case will move to a state of fully 'Closed'. Any subsequent mails received will launch a brand new work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MfDZBGtUv2atxGtZJ45%2F-MfDaCTHDEAgfxe17rUS%2Fimage.png?alt=media\&token=51703655-11d9-4c63-be4d-e6685ec18a48)

### Cancelling/Aborting a Case

Selecting the 'Cancel' option and hitting the button to confirm will abort the Case. It will be completely closed and will no longer be available to process. If you re-open the tab for this item, system will confirm that the Case has been aborted.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MfDZBGtUv2atxGtZJ45%2F-MfDafSafJXPMq-moPjY%2Fimage.png?alt=media\&token=65dda021-429d-49a9-b06e-d4736eaa5bef)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_W8pWTB-OnnGBhgDhY%2F-M_WAaOEQ3Yl_vkQs7Wp%2Fimage.png?alt=media\&token=2093937f-61ca-49f1-b9c5-1b05c75feaa4)


# Manually Launching An Action

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTg2OQ==>" %}

Most often the Actions in a Case are started automatically (either by process flow or based on schedules). However, if an Action has been configured to be manually startable, you can do this from the Case.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsy10QGFwapNDi9Yhz%2F-MWsywf3_8k23skSkZYh%2Fimage.png?alt=media\&token=b3c6677f-99ac-414f-97ed-0deb79a9a2a2)

Select the ‘Start Action’ tab in the Activities section. In the resulting panel, choose the Action type to launch (must have been configured as manually startable in Builder), set a due date and specify how many of the Action you wish to launch. Specify the Action instructions if you wish these to be different from the default instructions displayed.

Hit ‘Start Action’ to confirm. The Action List will automatically refresh to display the new Action that you have just created and a confirmation message will be displayed.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FEPaybyI0V3aqyOGj9YAF%2Fimage.png?alt=media&#x26;token=0b1f6025-b1b6-4218-8fa0-69499577bf7e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note:

* You do not need to have the Case assigned to you in order to launch a new Action.
* This option is also available from any of the Actions within the Case.
  {% endhint %}

The tab will not close upon launching the new Action, as this is an additive activity which does not modify the current Case.


# Reworking a Case

If issues have occurred during the running of a Case you may wish to rework the Case.&#x20;

## From a Case

You can do this from the Case by selecting the ‘Rework’ tab. In the resulting panel, you need to choose where you want to restart the Case from. You can choose to rework the Case from a specific Step or from a specific Action. You can also select a schedule if your system has been configured to allow you to do so.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fnm23Kwd92k1Xy0Hqef18%2Fimage.png?alt=media\&token=b3721fc5-e06c-446f-8fb8-fa1a24e2ed39)

{% hint style="info" %}
Note: In order to re-evaluate the Case Conditions, rework must be started from the start of a step. Further specifics on this:

* You cannot rework from an Action which was started as an ad-hoc Action.
* Users are still limited to reworking from steps prior to the current one, and so are also limited to choosing Actions from within prior steps.
* If rework is performed multiple times then there may already be downstream steps that were previously completed - however they are not eligible for selection as restart point.
  {% endhint %}

Additionally, if the Case you are wanting to rework has any associated running Sub Cases or manually started Actions (Ad-hoc Actions), you can choose to terminate them as part of reworking the Case.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZD6CsnuzXc3xzj8VBUpg%2Fimage.png?alt=media\&token=6e2a5699-7c5a-4651-b2b3-501d15db4bdd)

Once you are happy, click the ‘Rework’ button in the info card to confirm and begin reworking the Case.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fx8lZpaxXEerX30TJ76CG%2Fimage.png?alt=media\&token=70caa7d8-96ba-4dc9-b2d1-cb5bb8f9d8c0)

The Case will move to a state of In Progress.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fm7PzW3prIjVaVKT2EpRi%2Fimage.png?alt=media\&token=f46d87da-f6b0-4ed2-9f95-e0a0cac54fcb)

All running Actions that are part of the Case will close when the Case is set to rework.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQPhiU7JVA2BnEZouR3SO%2FMicrosoftTeams-image%20(23).png?alt=media&#x26;token=8b1a3ae9-1518-45b4-a4f3-4200d2aef0fb" alt=""><figcaption></figcaption></figure>

Copies of these Actions will be created in the Case, all in a state of To Do.

An entry will also be added to the timeline showing who set the Case to rework, when it was set to rework, and the Step number and Action it was set to rework from. This will also appear in related work item timelines i.e. its Actions and any Sub Cases if you have selected the Case Rework History filter from the timeline filters options.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeGMlFXKOZLPM91ETsYVO%2Fimage.png?alt=media\&token=937d92c8-4f69-48f3-ad5f-0b91322a3877)

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F30cAhOefASMpAHwj9uGb%2FMicrosoftTeams-image%20(25).png?alt=media&#x26;token=d52d874f-e761-406d-b7ff-dd88efa33fa8" alt=""><figcaption></figcaption></figure>

## From an Action

You can do this from an Action by selecting the ‘Rework’ tab. In the resulting panel, you need to choose where you want to restart the Case from. You can choose to rework the Case from a specific Step or from a specific Action. You can also select a schedule if your system has been configured to allow you to do so.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3n1tnGjca85WaJZIIiKF%2Fimage.png?alt=media\&token=14a317b8-c882-4fd4-82eb-d33ca00447b6)

{% hint style="info" %}
Note: In order to re-evaluate the Case Conditions, rework must be started from the start of a step. Further specifics on this:

* You cannot rework from an Action which was started as an ad-hoc Action.
* Users are still limited to reworking from steps prior to the current one, and so are also limited to choosing Actions from within prior steps.
* If rework is performed multiple times then there may already be downstream steps that were previously completed - however they are not eligible for selection as restart point.
  {% endhint %}

Additionally, if the Case you are wanting to rework has any associated running Sub Cases or manually started Actions (Ad-hoc Actions), you can choose to terminate them as part of reworking the Case.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQKdSrVVIUUjLDUo3IHZx%2Fimage.png?alt=media\&token=d2a15333-0523-4140-88af-28d2e3540b00)

Once you are happy, click the ‘Rework’ button to confirm and begin reworking the Case.&#x20;

All running Actions that are part of the Case, including the Action you are currently in, will close when the Case is set to rework:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQPhiU7JVA2BnEZouR3SO%2FMicrosoftTeams-image%20(23).png?alt=media&#x26;token=8b1a3ae9-1518-45b4-a4f3-4200d2aef0fb" alt=""><figcaption></figcaption></figure>

And copies of these Actions will be created in the Case, all in a state of To Do.

An entry will also be added to the timeline showing who set the Case to rework, when it was set to rework, and the Step number and Action it was set to rework from. This will also appear in related work item timelines i.e. its Actions and any Sub Cases if you have selected the Case Rework History filter from the timeline filters options.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeGMlFXKOZLPM91ETsYVO%2Fimage.png?alt=media\&token=937d92c8-4f69-48f3-ad5f-0b91322a3877)

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F30cAhOefASMpAHwj9uGb%2FMicrosoftTeams-image%20(25).png?alt=media&#x26;token=d52d874f-e761-406d-b7ff-dd88efa33fa8" alt=""><figcaption></figcaption></figure>

## Auto-Assignment of Actions started while Case is in Rework <a href="#auto-assignment-of-actions-started-while-case-is-in-rework" id="auto-assignment-of-actions-started-while-case-is-in-rework"></a>

When an Action is started in a Case which is currently in rework, the Action will auto-assign to the same user who previously performed the same Action (either the user who completed the Action or, if it was not completed previously, then the last user it was assigned to).

{% hint style="info" %}
Note: If 'Keep Actions with Me' is selected on the Case, the ‘keep with’ logic will take precedence.
{% endhint %}


# Sub Cases

## Creating a Sub Case

A Sub Case will behave according to its own specific configuration, but its “parent” Case will not complete until all of its Sub Cases have completed.&#x20;

You can therefore only create a Sub Case from an existing Case.

To create a new Sub Case, click the ‘+ Work item’ link shown near the tabs section of a Case and the choose the 'Sub Case' option from the dropdown.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fjm8x5puRRfaMMvkEbftA%2Fimage.png?alt=media\&token=12a080a0-c104-4088-b4cb-e055b2e7c69f)

In the resulting pop up, you can filter to search for the new type of Sub Case process you want to create in two ways:

* by searching by email route - you can specify the mailbox address which people would normally send emails into to create work items. Often an email mailbox represent a certain part of the business within which you want to create your new work item.  As a useful shortcut we've added a feature here where you can search by mailbox and narrow down straight away the Sub Case processes that you can choose from. Selecting a mailbox will filter the dropdown options to only the processes linked to that mailbox.&#x20;
* by selecting a Customer, Contract, Service and a Sub Case process to launch (these will default in values if there is only one option to choose). Note that the Customer for a Sub Case will will be auto-filled as the same as its parent Case i.e. the Case you are creating it from.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHLUm3pLYbKcn4JsMReyc%2Fimage.png?alt=media\&token=c0b1961e-c3ac-4e5b-9f75-6c90c06df7b6)

{% hint style="info" %}
Please note that the Sub Cases available for you to launch will depend on the permissions settings in Builder. Additionally, you will also only be able to select a Sub Case process from an email route that has been enabled in Builder ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes)). You will also only be able to select a Sub Case process in [Test Mode](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/test-mode) if the email route for that Sub Case process has been [configured to run in Test Mode](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes).
{% endhint %}

You can then adjust the following settings for the Sub Case:

| Setting           | Detail                                                                                                                                                                                                                                                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Override Due Date | If your system has been configured this way ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours)), you can select to override the due date of the new Sub Case you are creating. |
| Description       | You can modify the description of the new Sub Case you are creatin                                                                                                                                                                                                             |
| Schedule          | If your system has been configured this way ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules)), you must select a schedule for the new Sub Case you are creating.        |
| Adding Contacts   | You can add multiple different contacts for the new Sub Case and divide the tags between them as you need.                                                                                                                                                                     |

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoplhBTgXtkBFSQxg4siA%2Fimage.png?alt=media\&token=1fce5840-3f34-49b1-83a3-3ac74efd9aa5)

{% hint style="info" %}
Please note that Defects, Files, Links & Custom Data will be automatically shared will be automatically shared from the parent Case to your new Sub Case. Communications from the parent Case, and its related work items, so its Action and Sub Cases (if it has any) will also be shared with the new Sub Case. However please note that emails will not be shared but you can easily see them by selecting the ['Include related work items' option in the timeline](https://docs.enate.net/enate-help/work-manager/work-item-screens/timeline#filtering-the-comms-tab). Also note that making updates to the Defects, Files, Links, Custom Data or Communications in the new Sub Case WILL update update them in the parent Case too.
{% endhint %}

A link to the new Sub Case will appear in the [Sub Cases tab](#sub-cases-tab) and NOT in the [Links tab](#viewing-linked-work-items-the-links-tab).

## Sub Cases Tab

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8o18I3JZ3nO3hyj0a%2FSub-Cases-Tab.gif?alt=media\&token=bd36ffad-fe23-4381-b5ff-2f74c03a9518)

The Sub Cases tab will show the following information for any Sub Cases under a Case:

* Current State icon
* Sub Case reference number and Case title
* Action Count – The count of Actions associated with this Sub-Case
* Owner– the Case owne&#x72;*(If defined)*
* Queue – the Cases Queue *(If defined)*
* Due Date – The Case due date
* Icon to expand the Sub Case to reveal its Actions

## Sub-Case Reference Number Logic

Reference numbers of Sub Cases can be broken down as follows:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzMwbwNchC5jzMFieVqwJ%2Fimage.png?alt=media\&token=9de85e6f-fe97-416b-9687-c07100c681da)


# Processing an Action


# The Action Screen

The Action screen has the same overall layout as the [Ticket ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-ticket/ticket-screen)and [Case ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/case-screen)screen, and the same basic features including [adding a note](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/adding-a-note) to a work item, [sending an email](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/composing-emails), viewing the [files and links attached](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/files-tab) and viewing the [comms/timeline](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/timeline), but the Action screen also contains some Action-specific features.

## Action Title

At the top of the Action screen, you'll see the title of the Action, made up of:

Customer name - Contract name - Service name - Case Process name - Action Process name

For example:&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnlK2Y4Xyz6pfnRsWxFRG%2Fimage.png?alt=media\&token=eadee018-42a7-4533-89c9-3e4cbae0c303)

{% hint style="info" %}
The title of an Action is automatically set and is not editable.
{% endhint %}

If the [short description of the Action's Case has been edited](https://docs.enate.net/enate-help/work-manager/processing-a-case/case-screen#case-title), the changes to Case Short Description will be reflected in the Actions Screens of all the Case's Actions (you may need to refresh your Action screen for this to take immediate effect) and the title of the Action will be made up of:

'**Action Reference** - **Case Short Description** - **Action Process Name**'\
'**10040-C-A1.1** - **Jack Jones new starter** - **HR Approval**'&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FcebEpVdRYFR5bU9DNKrg%2Fimage.png?alt=media\&token=9f05514d-688a-459e-ad24-dd332e5d9e2a)

{% hint style="info" %}
Note that the Case Short Description cannot be edited directly from an Action.
{% endhint %}

This is the name that will be shown in the Action tab:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXF31N4UuVvz0xaEc87a3%2Fimage.png?alt=media\&token=39331a19-022d-4d6e-a417-779bebfea9ad)

The Case's short description is also the title that will also appear in the 'Title' column of the homepage grid for the Action.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFGvZoFKR92U5NcavSMOe%2Fimage.png?alt=media\&token=cad8c295-5c3e-49ef-b2d7-935d9aec33c1)

You can copy the Action's reference and number by clicking on the copy icon in the tab:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQ2oeOx9UOCmBmW8WiRb3%2Fimage.png?alt=media\&token=02b81aaf-dc4f-4489-9f47-9559c25eaf90)

## Due Date <a href="#c-due-date" id="c-due-date"></a>

The Action's due date will display, colour-coded to show if the date is:

On schedule:&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoSF5hTTfJXBlLgyPxOk6%2Fimage.png?alt=media\&token=0f0922b3-f879-405a-b645-4609a58b6208)

Due today:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FGcZVxA8BPtbDFm2jMCio%2Fimage.png?alt=media\&token=6425fbf6-d706-4d8d-a85f-d0fff6049c99)

Late:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fe3h76q8sJOIIwUt34ZOM%2Fimage.png?alt=media\&token=e8f6f236-a8ce-4ad2-b970-724ffbea4308)

### Override Due Date

If an Action has been configured with an override due date option in Builder, then you will be able to override the due date of an Action by clicking on the due date in the header and changing the date in the popup.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNcmoTZkr3ag83Kcop7e3%2Fimage.png?alt=media\&token=aeb571fd-26ed-446f-a06c-6ed23942df78)

## Assignee

You can also see whether or not the Action has been assigned, and who to.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FR5JaAkNmWXiMd4CDKa7C%2Fimage.png?alt=media\&token=0f1d6290-acb8-475d-81e4-6b9b454c4e6d)

You are able to reassign and unassign an Action, or assign the Action to yourself if it has not been assigned to you already.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSgKbxV2MlZgaVuv82RTS%2Fimage.png?alt=media\&token=9c1a42b6-3746-4c77-8ef1-52f92bf4940c)

See here for more information about assigning work in Enate:

{% content-ref url="../assigning-reassigning-unassigning-work" %}
[assigning-reassigning-unassigning-work](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/assigning-reassigning-unassigning-work)
{% endcontent-ref %}

## Side Panel <a href="#item-access-vs-assignment-rules" id="item-access-vs-assignment-rules"></a>

### Viewing an Action's Status <a href="#item-access-vs-assignment-rules" id="item-access-vs-assignment-rules"></a>

In the Info Card you can see the status of the Action and change the status as needed.

The main label on the left side of the Info card will display the status the Action is currently in. The dropdown button on the right side gives options for the states which you can move it into as part of processing.&#x20;

See here for more information about processing an Action:

{% content-ref url="processing-an-action" %}
[processing-an-action](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/processing-an-action)
{% endcontent-ref %}

{% hint style="info" %}
**Once you have selected the new status from the dropdown and filled in any further required information, click the button to confirm**.
{% endhint %}

The border of the Info Card highlights in a colour relating to the current status – once you have clicked the button to change status, the system will process the changes – the border colour and new status will change to confirm that the status update has occurred.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMzGoNhVD7NrPlJQg28C7%2Fimage.png?alt=media\&token=5d18e5c8-0eb2-48a8-8158-aabb64247c81)

When changing the status of a work item, if you are moving it to a state of 'In Progress', the work item tab will remain open upon confirming the new status. When changing to any other status, e.g. 'Wait' or 'Rejected', the tab will automatically close. A label under the Status will inform you of this in advance.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsWImGGXvpVMeCYg10%2F-MWsXAfURJOYJHxyrHjA%2Fimage.png?alt=media\&token=5a1b7150-e4a2-43a8-b066-7b9de745b561)

In addition to showing the Action's status, the following information is displayed directly underneath:

* Set by - who set the status
* Reason - the status change reason - i.e. why was it changed, this could be manual or as part of a process)
* Date - when the status was changed
* Last Updated By - who last changed some data on the Action
* Last Updated On - when some data  was last changed on the Action.

{% hint style="info" %}
Note that not all of the above information will be displayed every time, the information that is shown depends on the status of the Action and how the Action has been configured in Builder.
{% endhint %}

### Viewing an Action's Settings

The Settings Card shows you detailed information about the Action, including:

* The Action's context (Customer>Contract>Service>Case Process). This cannot be modified.
* Action Instructions
* The Action's parent Case, a link to the parent Case and a symbol showing the state of the Case
* When the Action was created and who by
* If this Action was created from another work item, the initial request date shows the start date of the original request, allowing you to capture the entire length of time it has taken to complete a request.
* Keep with me - users who have this option selected will be auto assigned as the work item's owner or assignee. This can still be changed manually.
* Record Count - depending on configuration for the Action in Builder, the record count may or may not be displayed here. If it is, the record count is editable. If you update the record count for an Action, it will update the record count for future Actions but not previous Actions that have been closed.

### Action's Contacts

The [contacts card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card) is where you can specify the people who relate to the Action.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWsYkhgFViAO0Oc0mj5%2Fimage.png?alt=media\&token=a7f14d2f-d032-49b9-bdcf-4e11fa778736)

By default, the available relationships are:

* Primary Contact – the main person you are dealing with for this Action.
* Requester – the person that raised the initial request.
* Subject – who the Action is about (this may be neither of the above).

Very often all three will be the same person.

* CCs – any further contacts which can be copied on any correspondence. When a contact is tagged only as ‘CC’, it will be displayed in the separate CCs section (hidden until any CC-only contacts exist on the work item.

{% hint style="info" %}
Note: it is possible to add further relationship types into the system. See here for more information on how to [add contact tags](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags).
{% endhint %}

An Action's contacts will usually be auto-populated as the same as the contacts for the parent Case. However, if the Action's contacts are not auto-populated or if you want to add a different contact to the Action, you can add contacts to the Action manually by searching for them in the [Contacts Card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/managing-contacts/contacts-card). This change will also be reflected in the Case's contacts too.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHaVmBb0E56_Q_jYnK%2F-MZHbC4BRt2U6cLKu08V%2FContact-Card-Search-for-Contact.gif?alt=media\&token=599a753b-246e-417c-af72-9df32a26189e)

If you search for a user in the contacts card that does not exist in the system, you can create a new contact by clicking on the ‘Create Contact’ option and filling in the contact's details.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHZHKfCwmT20z_i-95%2F-MZHa09WPZI3WlIY7Ea-%2FContact-Card-Create-Contact.gif?alt=media\&token=bd8d2355-15e2-4760-b594-6db9028823c3)

If you have written the email address for the contact, the system will decode and auto-populate the first name and last name of the contact. Once you fill in all the information and click on create contact, the system will redirect you back to the work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHNQAkYnfT4YfYPY7I%2F-MZHZ15Kudy6pBkdjKew%2FContact-Card-Email-Address.gif?alt=media\&token=971fe34f-7a7b-4a1b-a402-d0868d662d26)

When you manually add a contact they will be set as the Primary Contact, Requester and Subject by default. You can manually reassign these tags to other users afterwards.

### **Time Tracking**

To help you manage activity against your SLAs, Enate allows users to track the time it takes for work items to be completed, both as an overall total and broken out by the various resources who may have worked on it.

The Time Tracker Card in work items tracks the time of each individual browser session that the item is worked o&#x6E;**.**&#x20;

See here for more information about time tracking:

{% content-ref url="../work-item-screens/time-tracker-card" %}
[time-tracker-card](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/time-tracker-card)
{% endcontent-ref %}

### Custom Card

Additionally, a Custom Card can be configured to display custom data..

See here for more information:

{% content-ref url="../work-item-screens/smart-cards" %}
[smart-cards](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/smart-cards)
{% endcontent-ref %}

### Defects Card and Recording Defects

When you're working on a Ticket, Action or Case, operational issues can occur which have an effect on how you're able to deliver the process. It is important to record these as a way to highlight them for others who may view or work on the item, and to help with longer term efforts to improve process delivery.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsY65S_d9Pto44HgLB%2F-MWs_UoZmWEu7HtnHRi9%2Fimage.png?alt=media\&token=89cadaa6-2154-4333-82a0-a124d04f4058)

Watch this video to find out more about recording defects in Enate.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQzOTYyNw==>" %}

You can also go to the dedicated article to find out more:

{% content-ref url="../work-item-screens/defects-card-and-recording-defects" %}
[defects-card-and-recording-defects](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/defects-card-and-recording-defects)
{% endcontent-ref %}

## Checklists

Some Actions have a checklist section. This shows the checks which are required for this Action - defined during its [configuration in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions#overview).

In order to mark an Action as complete, you must confirm for each item in the checklist whether you have completed it (the options are Yes, No, N/A) and you may need to add a note for each check.

You can also see the name of the person who last updated the item in the checklist and when this update was made.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FC5Tm9pNogHm9WEF3d536%2Fimage.png?alt=media&#x26;token=16424cd3-d368-4663-98ca-5779ad4258de" alt=""><figcaption></figcaption></figure>

## Activities Launched from the Action Screen

### Reworking a Case

If issues have occurred during the running of a Case you may wish to rework the Case. You can do this from an Action by selecting the ‘Rework’ tab from the Action screen.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHgMPMtp4UG01mo90wPSY%2Fimage.png?alt=media\&token=4de47c0d-a93c-4c0e-b084-09c395a1172a)

See here to find out more about reworking a Case from an Action:

{% content-ref url="../processing-a-case/reworking-a-case" %}
[reworking-a-case](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/reworking-a-case)
{% endcontent-ref %}

### Starting an Action Manually

Most often the Actions in a Case are started automatically (either by process flow or based on schedules). However, if an Action has been configured to be manually startable, you can do this from an Action using the 'Start Action' feature.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfArufbVRuGyuZioRMoGa%2Fimage.png?alt=media\&token=1cf9cc3b-9817-45fd-970c-7da50b37c92e)

See here to find out more about manually launching an Action from an Action:

{% content-ref url="../processing-a-case/activities-available-for-case" %}
[activities-available-for-case](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/activities-available-for-case)
{% endcontent-ref %}

## Further Info on Action Screen

### New Information Received

When a new email has come in for the Action that hasn't been read yet, the New Information icon will be highlighted. Clicking on it shows you when the new email was received.&#x20;

You can choose to mark the new information as read which will set the New Information icon back to normal. You can also mark the information as unread by clicking on the 'Mark as New' option.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeDI4vt4cOwzwuhffQIOL%2FNew-Information-Icon.gif?alt=media\&token=4f358a7d-0d7f-4691-9338-aea89d4b6304)

### Viewing Case Progress

You can view how the Case that the Action belongs to is progressing by clicking on the map icon. will bring up the Case progress popup. This displays the progress made on steps in the Case, showing completed steps in green, the current step in orange and future steps in grey.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTO8IPEq0YD4JNf2W3HBa%2Fimage.png?alt=media\&token=4ed77d97-18a3-4ce5-980c-1a9e9f672e80)

{% hint style="info" %}
If you do not want any percentages to show here, simply leave them blank when configuring the Case’s steps in Builder.
{% endhint %}

### Standard Operating Procedure

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyijZShPp6uX9KN6ns1lN%2Fimage.png?alt=media\&token=9437dcbb-afc1-41a2-8c25-e59b49c27774)

This provides a link to the Standard Operating Procedure for the work item that has been set in Builder.


# Processing an Action

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTg3Nw==>" %}

An Action in Enate will begin in a status of ‘To Do’ until a resource has picked it up - this could be a human resource or a robot resource.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXD1u3AQB_NsYAgxnMk%2F-MXDK9jbYtKU1PgqZFF2%2Fimage.png?alt=media\&token=db241192-a584-4691-bc8b-b537d916095c)

Once you start updating an Action sitting in this state, it will:

* automatically assign to you and&#x20;
* the status will change to ‘In progress’&#x20;

You can also choose to change the state yourself. This signifies that work is now underway and it will stay in 'In Progress' until it’s resolved – assuming e.g. no waiting for further information.

## Setting an Action back to 'To Do'

If you’ve picked up an Action in error, or if your reach the conclusion that it’s not a piece of work you’re going to be able to progress you can unassign it from yourself, either to another resource or just back to its Queue. This could be after 10 seconds or half an hour, but when you do this the system will automatically set the status back to ‘To Do’ to let everyone know that it’s not going to be progressed until another resource picks it up. You can also just manually set the status back to ‘To Do’ if for example you started working on it in error and need to quickly undo the status change.&#x20;

Similarly if a robot resource rejects a piece of work its status will be set back to ‘To Do’ as part of handing it over for a human resource to carry out.

## Using 'Wait' for Actions

If you’re working on an Action and you have to temporarily halt work on it because you’re waiting for some additional information or because of some other temporary blocker, you should choose the **‘Wait’** status.

When placing an Action into a state of 'Wait', you need to specify the type of wait. The options are:

* [Wait for more information](#wait-for-more-information)
* [Wait Until](#wait-until-follow-up-date)

### Wait for more information for Actions

Impact on SLA clock: IF the Action's due date rule (configured during process design) has  ['Add Wait Time To Due Date'](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours) set to ON, SLA clock PAUSES while an Action is in this state. If it is set to OFF, the SLA clock CONTINUES while the Action is in this state.

If you’re working on an Action and you have to temporarily halt work on it because you’re waiting for some for some information from a third party or client, you should choose 'Wait for more information'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXD1u3AQB_NsYAgxnMk%2F-MXDLMMUjSk7o-k6hiRW%2Fimage.png?alt=media\&token=32a7db18-7aa4-465a-a1e1-cb4d46d68526)

Upon confirming the 'Wait for more information' status, the Action will move from your Work Inbox into your Owned Work list, as there is no active work to be carried out on it until a response is received.&#x20;

Once a response has been received, the Action will move back from your Owned Work list into your Work Inbox in a state of To Do, highlighted for you to progress.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fyz6eyDiuxJ0Img0zOpJk%2Fimage.png?alt=media\&token=fad49311-f0a9-44ab-b725-3a5dde2c56cd)

### Wait Until for Actions

Impact on SLA clock: IF the Action's due date rule (configured during process design) has  ['Add Wait Time To Due Date'](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours) set to ON, SLA clock PAUSES while an Action is in this state. If it is set to OFF, the SLA clock CONTINUES while the Action is in this state.

If you’re working on an Action and you have to temporarily halt work on it until a specific future date/time, you should choose 'Wait Until'.

When you select 'Wait Until', you must specify the desired follow up date and time.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXD1u3AQB_NsYAgxnMk%2F-MXDLTWcSRoNFwvRgvD3%2Fimage.png?alt=media\&token=fcc923c4-a8d0-42b6-9939-8f4cf5368c2b)

Upon confirming the 'Wait Until' status, the Action will move from your Work Inbox into your Owned Work list, as there is no active work to be carried out on it until the follow up date.&#x20;

When this date is reached, the Action will move back from your Owned Work list into your Work Inbox in a state of To Do, highlighted for you to progress.

## Resolving an Action

You signify completing the Action by marking it as Resolved.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXD1u3AQB_NsYAgxnMk%2F-MXDLgr9gzTcJPQm3ITg%2Fimage.png?alt=media\&token=98c3b4df-21fa-4363-83bf-168914b9e352)

Along with this there are two options to specify how the Action was resolved:&#x20;

* Complete
* Unable to complete

### Unable to Complete

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTg5Mg==>" %}

Set this option if you cannot complete the required activity. Once you have confirmed this option, the Action will be closed and cannot be re-opened. The Case Owner will be notified of this and be asked to take the necessary steps to resolve at Case level. This may involve starting another copy of the Action, reworking the Case from a previous step, or moving on.

Enter the reason you are unable to complete the Action and hit the ‘can’t Complete’ button to confirm. The tab will close.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXD1u3AQB_NsYAgxnMk%2F-MXDLmv410mCfXwChph3%2Fimage.png?alt=media\&token=8229cbfa-dda4-4b14-bfb1-e461e0f13ac4)

### Resolved to Closed <a href="#resolved-to-closed" id="resolved-to-closed"></a>

After the Action has been resolved, it will move to a state of 'Closed'.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_W8pWTB-OnnGBhgDhY%2F-M_WBDyUv_PumvChBe4o%2Fimage.png?alt=media\&token=78649201-b5d8-483b-addc-92d5d3e25bc6)

Any subsequent mails received will launch a brand new work item. Once you have selected this, the Action will be closed and cannot be re-opened.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXD1u3AQB_NsYAgxnMk%2F-MXDMIENa-OdE1VU-Yfk%2Fimage.png?alt=media\&token=0c63ecdc-77d2-492d-8a90-7ba063995adc)

{% hint style="info" %}
&#x20;Note: You can easily move an item from 'To Do' straight through to resolved.
{% endhint %}


# 'Wait for Sub Cases to Complete' Actions

A ‘Wait for Sub Cases to Complete’ Action will wait for a specific Sub Case to reach completion before allowing the Case to move on to the next Action.

You can tell that an Action is a ‘Wait for Sub Cases to Complete’ Action because it will say 'Action is waiting for Sub Case to complete' in the Action's info card.

Once a ‘Wait for Sub Cases to Complete’ Action has been launched AND the Sub Case it has been set to wait for has been launched (either manually or through a 'Start Case' Action), the ‘Wait for Sub Cases to Complete’ Action will move into a state of 'Waiting'.&#x20;

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-Mahf7s_DMYD56EJBY03%2F-MahjL3C13RNC2jFgHiy%2Fimage.png?alt=media\&token=7d6c2eb3-78c8-4b0a-a6c5-6c79a272dbba)

Once the Sub Case is completed, the 'Wait for Sub Cases to Complete' Action will close automatically.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F2lWsvg9v2BZeS9KzHNTU%2Fimage.png?alt=media\&token=34c14e3e-b53d-45b7-9be2-b2ec7a456ecf)

You will be notified of this in the timeline as well.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKRXWFgDwBMN9znQAFTsC%2Fimage.png?alt=media\&token=27e8765e-75a2-443a-9e3f-8f1edbac5ea4)

If the Sub Case the 'Wait for Sub Cases to Complete’ Action is set to wait for it not available - either because it has not been launched or because it was resolved before the ‘Wait for Sub Cases to Complete’ Action was launched, the ‘Wait for Sub Cases to Complete’ Action will enter a state of 'To Do' and be assigned to a Queue where a user will pick it up and decide how to proceed.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-M_tt8kvvrs8MMHHKag6%2F-M_ttFIUdXov1PCb7v2Z%2Fimage.png?alt=media\&token=abd4dab3-54ef-4172-930a-09775d9106cd)

If you then try to set the 'Waiting for Sub Case to Complete' Action to 'Waiting', the Action will close as the Sub Case it is set to wait for hasn't been launched.

If the Action is not in a 'Wait for Sub Cases to Complete' state and the Sub Case for which it is waiting has been completed, a message will appear as 'Sub Case is completed' in the Info Card.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-Mahf7s_DMYD56EJBY03%2F-MahjJ5dRBh27P7pDi6T%2Fimage.png?alt=media\&token=cf9a40b1-9f4e-4195-ae20-6b17596a4c90)

If you manually Resolve a ‘Wait for Sub Case to Complete’ Action, the Action will be marked as Resolved without the Sub Case having completed.

{% hint style="info" %}
Please note that if your system has been configured to auto-close a 'Wait for Sub Case to complete' Action (see here for more information about how to do that) and the Sub Case the 'Wait for Sub Cases to Complete’ Action is set to wait for is not available - either because it has not been launched or because it was resolved before the ‘Wait for Sub Cases to Complete’ Action was launched, the ‘Wait for Sub Cases to Complete’ Action will automatically move to a state of Closed. You will be notified of this in the timeline.
{% endhint %}


# IDP: 'Document Extraction' Actions

## Overview

The Document Extraction component automatically extracts the relevant data from files attached to incoming emails so that this data can be used in further processing of the work item, saving your agents time and effort. This also means that documents such as PDFs can be scanned and used both to start Cases in Enate and to form part of the ongoing process's activities.&#x20;

When a Document Extraction Action runs for a Case, documents attached to the Case can be submitted to your desired technology for scanning and the processed output files will be returned and automatically attached to the Case.

If at any point the technology you're using is not confident enough of the results, based on a confidence threshold that you can set, Enate will instantly transfer the work to an agent in Work Manager to look over and verify, giving you that 'human in the loop' support.

This component can be switched on by your admin in the [Marketplace ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)section of Enate Builder.

Check out this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTgwNzUwMw==>" %}

## How it works at runtime

When the Case is run in Work Manager, relevant data from files attached to incoming emails for it will be automatically analyzed and extracted.

If the technology you're using is confident enough about its data extraction results, this Action won't even need to be seen by a human user, it will simply be completed automatically and the Case will move on to the next Action. The completed data extraction Action can still be viewed if you click on it, but it won't need to be handed over to a human user for involvement.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5x5hGES3lDv4IeonVeVS%2Fimage.png?alt=media&#x26;token=d780fad0-e13d-4f09-aab1-92d50045b3b3" alt=""><figcaption></figcaption></figure>

However, if the extraction technology is less confident in its data extraction results, the Action will be handed over to a human user when you next hit 'pull from Queue' in their home page, to pick up and look over. When an agent opens the Action, you'll see that it's been given to them because some further checks are required.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fy9Y9HDnAUp1iAZPBElZt%2Fimage.png?alt=media&#x26;token=2e5fe576-dd63-48da-88af-d5a26e72e880" alt=""><figcaption></figcaption></figure>

To view and validate each document, click on the icon to open, and scroll to the 'validation station' screen in the Action, which shows the scanned document image and the resulting extracted table of data values. This lets you see where those lower confidence levels are highlighted, review them and make any necessary corrections manually. This can viewed in-situ, or expanded out to a popup to display full screen.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FENjWUXcMkUCNFGf5gEq9%2Fimage.png?alt=media&#x26;token=ecc6a608-3dd1-41d1-9b48-a647a6b0f74c" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FEq2V55uyAAiyTKogXKvi%2Fimage.png?alt=media&#x26;token=06749f49-5a26-48fb-8cb8-9a6b4a4676cc" alt=""><figcaption></figcaption></figure>

On this validation screen the agent will be able to see a scanned copy of the file, which can be multiple pages, alongside two tabs showing extracted data.

* The **Extracted Data** tab shows the agent key value pairs of the extracted data along with the confidence level that EnateAI has given them. The values can be adjusted when necessary and are saved once the agent clicks the update button for that value. Doing so will set the confidence value to 100% for that Key.
* The **Tables** tab shows any repeating data that has been picked out as a table. You can use the delete button to delete any rows that you do not need.

#### **Checkbox Data**

**Checkboxes** are recorded within the validation fields. EnateAI for IDP can record complicated **checkbox** questions such as those with multiple answers. The number or letter of **checkbox** will be recorded in the data validation field as well as any text answer that comes with the **checkbox**. See the example below:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fi07bEs95sUCtOiAofGVm%2Fimage.png?alt=media&#x26;token=616a1331-6779-4e1a-a02f-5ca3d7418562" alt=""><figcaption></figcaption></figure>

#### Saving and Submitting

If the agent needs to leave the Validation Station screen at any time they can just click 'Save as Draft' to save their changes for a particular document. &#x20;

{% hint style="info" %}
Note: If an agent enters the validation screen on an Action that is not assigned to them, the data will be in read only mode and can not be edited. To be able to edit the data, the agent must first assign the Action to themselves.
{% endhint %}

Once an agent is happy with the data all they need to do to submit the updated data is to click the 'Submit' button. EnateAI will finish processing in the background, and will update the Action screen to confirm when it's finished. The background processing allows the agent to move on to any other documents which require verification.

Once 'Submit' has been clicked for the last document needing validation, the Action screen auto-closes. Again, EnateAI is finishing processing in the background and will mark the Action as Resolved after a short time, then moved to Closed.

*Note: Every time you review and update data items, EnateAI will learn and get a little bit better at its data extraction suggestions. If you notice that the technology is regularly getting its suggestions wrong, speak to your admin team about modifying the confidence threshold.*&#x20;

### Current Limitations

* Only one document can be viewed at a time.
* The maximum file size is 15 pages.


# 'Peer Review' Actions

## Overview

Peer Review Actions are a great way for different members of a team to crosscheck each other's work for key Actions within a Case.

Peer Review Actions involve two parts: the first part is completing the Action, done by one user. The second part involves reviewing the Action to check it was completed correctly, done by a different user.

Watch this video for a quick overview about how to use Peer Review Actions in Work Manager:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM1Mjg4Nw==>" %}

## Step 1: Completing the Action

The Peer Review Action will first appear in a state of 'To Do' to the user who is tasked with completing the Action.&#x20;

The peer review symbol will let you know if you are completing an Action that is then going to be reviewed by a peer:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fj7WUtPuRlJRZZHj2uXnw%2Fimage.png?alt=media&#x26;token=dc5c3819-9d47-4629-bf4a-4f88dc167acd" alt=""><figcaption></figcaption></figure>

The first user needs to complete the Action as normal and mark it as 'Resolved'.

## Step 2: Reviewing the Action

Once the Action has been completed and marked as 'Resolved', the Action is then assigned to a **different** user to review, back in a state of 'To Do'. &#x20;

{% hint style="info" %}
Note: The person who carried out the manual activity cannot also perform the peer review activity.
{% endhint %}

The peer review symbol will let you know if you are peer reviewing an Action that was completed by a colleague:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FlBKkG0Dez4281EY77Wai%2Fimage.png?alt=media&#x26;token=c4c18cb2-68dc-4bf6-aec9-ace958646878" alt=""><figcaption></figcaption></figure>

When you are on the screen of the Action which is being peer reviewed, you'll see a Peer Review text box along the top, allowing the reviewer to add any overall comments relating to reviewing how the Action was completed.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNkMXFA8h9ah6aY4Z1Iab%2Fimage.png?alt=media&#x26;token=431c44a0-f6ba-440f-8525-9c8051c24bbb" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The checklist is only available when the Action is in a state of 'To Do' and only the assigned reviewer is able to edit the checklist.
{% endhint %}

Once you have finished your review activity, switch the status of the Action to resolve and then choose if the review was a Pass, Fail or was Unable to be completed and then click to confirm.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FAufzEIHpPpUKBic06Dxp%2Fimage.png?alt=media&#x26;token=0121fc36-4b92-466b-849e-a627887967de" alt=""><figcaption></figcaption></figure>

### Passing the Review

If you're happy to approve the activity, selecting 'Pass' will mark it as such and will close the Action on-screen. You can add a comment, but it is not mandatory.&#x20;

If you then click to re-display the action, you'll see that next to Peer Review it now says Passed, and any comments entered can be read.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FxPX3CaKCBmKvvmUXcu4p%2Fimage.png?alt=media&#x26;token=255d4c98-0c24-455f-8048-27476d3229fe" alt=""><figcaption></figcaption></figure>

### Failing the Review

If the Action has not been done correctly, you should select 'Fail' and must add a comment in the Peer Review Comments section with the details of why.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FWydWa4XtJzoFRC6rT8nS%2Fimage.png?alt=media&#x26;token=502cb3a9-d5fc-4e16-9b21-0876aa6d0695" alt=""><figcaption></figcaption></figure>

Submitting the review will then return this Action back to the agent who carried out the original activity in a state of 'To Do'.&#x20;

When that original agent opens the Action, they'll see 'Failed' next to the peer review, and will be able to read all of the comments left by the reviewer.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoX7jefuiZ5dFcmEBDtdJ%2Fimage.png?alt=media&#x26;token=f5b1e029-087d-4b6d-8932-111908b778b8" alt=""><figcaption></figcaption></figure>

Their role now is obviously to redo that activity to correct the issues raised, then once again mark it as resolved. It will then be routed through to the reviewer again to carry our another peer review.

### When Review is not possible

The other option is that the reviewer is unable to successfully carry out a review. In this circumstance they should select 'Unable to complete'. The system will then ask the reviewer to provide a reason as to why they were unable to complete the review.&#x20;

Once that has been provided, they can mark the Action as resolved.&#x20;

This closes the Action and marks it as 'not done successfully'. This escalates up to the Case, which will now display a warning symbol and the notification that the case needs intervention in order to move forward.

## Bypassing the Peer Review

It IS sometimes the case that the peer review activity gets automatically bypassed if it meets certain criteria set as part of the Case configuration.&#x20;

If that happens, then as soon as the manual Action is completed, the system will move straight on to the next Action and will avoid routing the work to someone to peer review.&#x20;

Further to this, a note will subsequently be displayed in the Actions list on the Case screen, showing that the peer review activity was not required.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtsUOt1JROZYV7l4vLTjk%2Fimage.png?alt=media&#x26;token=2a9cc1c8-9dd7-4c57-856c-b42a07735d87" alt=""><figcaption></figcaption></figure>


# 'Send Email' and 'Send Email and Wait' Actions

## Overview

'Send Email' Actions involve Enate auto-sending an email and then the Action will immediately close. Work Manager Users should not have to do any work on this type of Action.

'Send Email and Wait' Actions involve Enate auto-sending an email. The Action will then move to a state of Waiting until a response has been received. Once a response has been received, the Action will move to a state of To Do to be processed further.&#x20;

The To address and any CC or BCC addresses on the email are configured in Builder - see this article about how to configure 'Send Email' Actions in Builder:

{% content-ref url="../../../builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab" %}
[email-action-info-tab](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab)
{% endcontent-ref %}

Once the email has been sent, an entry will appear in the timeline showing when it was sent, who it sent from and to, any CC or BCC addresses, the email subject and if you click to expand, the email body itself.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FC1k6yxkA8RGOKK0huxob%2Fimage.png?alt=media&#x26;token=c5378c66-4216-4eea-a1c3-35847b0aed54" alt=""><figcaption></figcaption></figure>

## Exceptions

If an invalid To, CC or BCC email address is used, the email for the Send Email/Send Email and Wait Action will fail to auto-send and the Action will then be moved back to its Queue.&#x20;

A warning will appear in the timeline:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ft9LYFTaD3Z1TU8mIKeU1%2Fimage.png?alt=media&#x26;token=412e9ad4-9b89-4196-9613-cb625e1e17d0" alt=""><figcaption></figcaption></figure>

The Case owner can then decide if they want to manually send the email and will need to correct the email address and add the email body manually. They should also contact their system administrator to alert them about the issue so that they can correct the email address to prevent future email failure.


# 'Trigger External API' Actions

Details around how to configure actions to trigger external APIs, and how they will display in Work Manager for operational users.

Similar to other action archetypes, 'Trigger External API' actions can be used in Case processes, and are used for when you need to automatically call out to another system, passing data to it and potentially getting the external system to pass updated custom data back into Enate.&#x20;

For information on how to configure 'Trigger External API' Actions check out this [Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/external-api-action-info-tab) section.&#x20;

Sometimes there can be a delay when waiting for the external system to respond. When that happens, i.e. when the ‘Trigger External API’ Action is waiting for information to come back from an external system, the Action info card will display in Work Manager as being in a state of 'Waiting'.&#x20;

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-McU3cKMEIYWF9riB2uC%2F-McU6B2BgbLS_LpfgULK%2Fimage.png?alt=media\&token=4712f166-4ffb-4165-a0b4-99f2ffa2fdd3)

When the external system ultimately responds to Enate with the data update, it will be with a marker to say whether it has been successful OR unsuccessful:

#### Response with Successful Completion <a href="#response-with-successful-completion" id="response-with-successful-completion"></a>

If the system is responding to say it has been successful, the Action will automatically move to a state of 'Closed', with a Resolution Method of 'Done Successfully'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9WvQ6V0GYb5oTaxfz%2Fassets--MR4uErt41EMkGUOTvyd--Me4nXVVivC9tN5_y8Tc--Me4pmsGKb7y-1iaOoRl-image.png?alt=media\&token=eb9f0713-10d4-4afa-8996-9674d14743f1)

**Response with Unsuccessful Completion**

If the system is responding to say it has been unsuccessful, the Action move into a state of 'To Do', with a reason of 'Updated by Integration'. The external API can also respond with additional information regarding why it was unsuccessful. This information will display in the Info card of the Action in the 'Rejected Reason' section.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9X5nHvRThI7f88B2F%2Fassets--MR4uErt41EMkGUOTvyd--Me4W11a8zINusWiW0PH--Me4XiRtr6apeOq2V0iB-image.png?alt=media\&token=12d32879-6acb-42ae-bd0b-77d468d74d0d)

If the Action isn't successful because it did not complete within the time set for it ([configured in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/external-api-action-info-tab)), then it will moved to a state of 'To Do' with a reason of 'Timeout' and it will allocate to a Queue / human user based on the configured allocation rules.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9XBIc1A2Oa-VxdDV1%2Fassets--MR4uErt41EMkGUOTvyd--Me4V2NPSrNWSL9p2SGv--Me4VnDXPrKFxOsTeN8b-image.png?alt=media\&token=0c092438-7226-4092-9f86-088a917edf73)

Such unsuccessful Actions will now effectively behave as a standard manual action.

{% hint style="info" %}
Please note that the Case owner will NOT be notified in these situations.
{% endhint %}

### Automatic Retries <a href="#automatic-retries" id="automatic-retries"></a>

If the Action is not able to connect to the external system, it will automatically retry connecting for a certain number of times, depending on how your system has been configured in Builder (see [here](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern) for more information). You will also be shown an error message bar on the Action showing:

* when the error occurred
* when the system will retry establishing a connection automatically
* how many times the system has automatically retried establishing a connection, and&#x20;
* how many times the system will automatically retry establishing a connection.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9XShUwr41of83YG-Q%2Fimage.png?alt=media\&token=4ab525b8-1ed6-4c83-9f38-4e528415296e)

You are able to manually retry establishing a connection from here too, by clicking the 'Retry' link in the error message.

{% hint style="info" %}
Please note that when you do a manual retry, this will be counted as an attempted retry and will therefore be included in the number showing how many times the system has 'automatically' retried establishing a connection.
{% endhint %}

If the Action fails to establish a connection following the automatic retries (e.g. if the retry setting is set to 5 and the system fails to establish a connection following 5 automatic retries), it will move to a state of 'Closed' with a resolution method of 'Not Done Successfully'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9XbhYQw2hJBzskPeH%2Fimage.png?alt=media\&token=89a88b3e-e29b-4570-aca7-4657f9885178)

{% hint style="info" %}
In *this* circumstance of the Action failing to establish connection with the external system, this will escalate to the Case Owner, highlighting in the Action section of the Case screen that this Action was Closed  - Not Done Successfully.
{% endhint %}

When the Action receives the required information, it will close automatically.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9Xhjxo1mG2dqg6KMX%2Fimage.png?alt=media\&token=5c0f485e-9799-47dc-b20d-47e866bdca36)

#### Adjusting the retry settings in Builder during / after retries have begun <a href="#adjusting-the-retry-settings-in-builder-during-after-retries-have-begun" id="adjusting-the-retry-settings-in-builder-during-after-retries-have-begun"></a>

If the automatic retry setting in Builder is changed *after* the system has automatically retried establishing a connection with an external system, the following will occur:

If, for example, the retry setting was originally set to 5 and the system automatically retried establishing a    connection 5 times but failed, the Action will have moved to a state of Closed with an error message showing a retry count of 5/5.&#x20;

If the retry setting then gets subsequently increased to anything above 5, for example 7, the error message will display a retry count of 5/7, but the system will NOT automatically retry establishing a connection for a 6th and 7th time as the Action is already closed.&#x20;

However, if the Action had not yet moved to a state of Closed because it had not yet reached the maximum number of automatic retries (e.g. it had only retried 4 times out of the 5), then increasing the retry setting to 7 means that the Action will automatically retry establishing connecting until the count has reached 7. &#x20;

Conversely, if you reduce the retry setting after retries have started, e.g. you're on retry 4 of 10 but then reduce the max down to 4, the system will still display 4 of 10 but will in fact be closed.


# Approval Actions

## What are Approval Actions? How do they work?

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEwNw==>" %}

Often within the Case flows of business processes which are built in Enate there are points where external people (i.e. people working **outside** Enate - this could be business managers within your company or the relevant client company) need to sign off on activities before the process can continue. Payroll processes are good examples of such processes, where client management need to sign off on payroll reports before the process can be allowed to continue.

Enate's Approval Action is built to specifically support these approval request scenarios in a more integrated way - to ensure that this 'approval cycle' is tightly managed and visible within the flow of activities in Enate.&#x20;

## How Approval Actions work at Runtime

Approval requests get sent out to agents working externally from Enate to approve or decline.

There are a few different types of approval that affect how the decision is made:

* In a multilevel scenario, the request email is sent to each new level upon successful approval from previous, up to a maximum of 3 levels. If any person declines, the approval is declined.&#x20;
* In a parallel any scenario, the request email is sent to all approvers and the first decision is taken.&#x20;
* In a parallel all scenario, the request email is sent to all approvers and ALL must approve for the request to be approved. If any decline, the approval is declined.

If the request gets approved by all necessary parties, the approval Action gets successfully resolved and closed automatically, so no Work Manager Agent will need to pick it up, although the closed Action can always be viewed by manually clicking on it.

## Exceptions - handled by Agent in Work Manager

There are, however, a couple of scenarios where a Work Manager agent might need to pick up and carry out any required activities to further process an approval Action:

* The approval has been declined&#x20;
* No approvers (or insufficient approvers) have been determined automatically

### Approval Request Declined

In the scenario where an approval request has been **declined**, the Action will move into a state of 'To Do' and so will ultimately need to be dealt with by a Work Manager Agent. They should review the approval decline reason provided by the approver and decide how to proceed. They can either:

1. **Update as needed and Resend the request by setting the Action to 'Wait'.** This will auto-send out the approval request email again\*\* and place the Action in a state of 'Wait for More Information' - since we're waiting for external information (an approval response) to be registered back into the system before activity can proceed.&#x20;
2. **Mark the Action as Unable to complete.** This will alert the Case owner who then needs to decide how to proceed - perhaps by reworking the Case or closing the Case entirely.
3. **Mark the Action as Resolved** which will manually mark the request as approved. The Case with then progress to the next Action.

{% hint style="info" %}
\*\*Note: Approval request email sending will start again from the beginning, i.e. all requesters will be mailed again. If they click on any previously sent emails, they will be met with a message telling them that THAT specific approval request is no longer valid, as the details of what is being requested may have changed). &#x20;
{% endhint %}

### **Insufficient Approvers**

In the scenario where an agent needs to add in approvers because one or more required approvers is blank (or make changes which result in the approval requests needing to be sent out again), the Agent will pick up the Approval Action in a state of To Do. Once they have finished making any adjustments and / or filling in missing Approver names, the must **then place the Action in a state of Wait**. Once they do this will auto-send the approval request email and then move the Action to a state of 'Wait for more information' as it is waiting for external info (approval) before proceeding.

{% hint style="info" %}
Note: While an Approval Action is state of 'To Do', or 'In Progress', external parties who were mailed out approval requests will NOT be able to approve or decline. Instead the will be met with a message informing them that the item in question is currently being processed. Work Manager Agents MUST move the Action back to a state of 'Wait for more information' if they wish the approval activity to recommence.&#x20;
{% endhint %}

### If Approval Requests Time out..

Another potential scenario is that the approval Action might auto-close because it has timed out as no/insufficient responses were received in time. In this case, the Action will automatically be set to Resolved, and the Case will continue. No Work Manager agent will need to pick up an Action in this scenario, although the closed Action can always be viewed by manually clicking on it.


# Working with Linked Work Items

Various features in Enate allow you to manage activities being carried out by different teams, letting you easily create and oversee work items even when you don't have full permissions on each other's work.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTg5NQ==>" %}

{% content-ref url="working-with-linked-work-items/linking-existing-work-items" %}
[linking-existing-work-items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/linking-existing-work-items)
{% endcontent-ref %}

{% content-ref url="working-with-linked-work-items/creating-new-linked-work-items" %}
[creating-new-linked-work-items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/creating-new-linked-work-items)
{% endcontent-ref %}

{% content-ref url="working-with-linked-work-items/viewing-linked-work-items" %}
[viewing-linked-work-items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/viewing-linked-work-items)
{% endcontent-ref %}

{% content-ref url="working-with-linked-work-items/sharing-emails-between-linked-work-items" %}
[sharing-emails-between-linked-work-items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/sharing-emails-between-linked-work-items)
{% endcontent-ref %}

{% content-ref url="working-with-linked-work-items/related-group-vs-linked-work-items" %}
[related-group-vs-linked-work-items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items)
{% endcontent-ref %}


# Linking Existing Work Items

## Overview

In addition to having the ability to [create new linked work items from a Case or Ticket](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/creating-new-linked-work-items), you can also create links between existing Cases and Tickets to allow you to better manage activities being carried out by different teams.

You can create links between existing work items in two ways:

1. [From the home page](#linking-work-items-from-the-home-page)
2. [From a work item](#linking-existing-work-items-from-within-a-work-item)

{% hint style="info" %}
Note that you can only create links between Cases and Tickets and you **cannot** copy communications, files, defects, links or custom data when creating a link between existing work items.
{% endhint %}

## Linking Work Items from the Home Page

You can link existing work items from your Home page by selecting the Cases and Tickets from the Home Page grid (which could be displaying your Work Inbox, Team's Work Inbox, Owned Work or Team's Owned Work) that you want to link together and selecting the 'Link' option that appears at the top of the grid.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBGd3afBv7yOJH6tKnwX2%2Fimage.png?alt=media\&token=5a441dc3-7da0-41b7-aaa6-4cc51e9bf341)

The first Case or Ticket that you select will be the work item that all of the subsequent selected work items will be linked to (or the first in your list if you've used the 'Select All' option).

The resulting pop-up will confirm to you the Case / Ticket the items will be linked to, and the specific items themselves, before allowing you to complete the linking confirmation:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fjs445c2z6swtVz0RPGsX%2Fimage.png?alt=media\&token=303a27be-c781-40e6-8369-e268f5d06470)

You can link up to a maximum of 50 work items at one time, but there is no upper limit on the number of work items that can ever be linked.&#x20;

If you subsequently go to this main Ticket / Case that everything has been linked to, on its [Linked Work tab](#viewing-linked-work-items-the-links-tab) you'll see ALL of the items you chose to link to it.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FadCZKxG7t8EwLodsdK8J%2Fimage.png?alt=media\&token=20ca3858-4557-4521-80ff-7afa2f255cf0)

However if you're in one of the works items you chose to link *to* this main Ticket / Case, on that Linked Work tab you'll only see a record of that main Ticket / Case (and not all of the other ones which were linked).

## Linking Existing Work Items from within a Work Item

You can link existing work items from within a work item itself by going to the work item's screen and selecting the '+ Work item' option and then choosing to add an 'Existing item'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvhOHVn9tqEvkmgNkHJEe%2Fimage.png?alt=media\&token=9e307b56-adfb-427c-af38-05ad59de2269)

In the resulting pop-up you can search for the Cases and/or Tickets you want to link this work item to.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FlavttozhnGFhmuOY6oCG%2Fimage.png?alt=media\&token=0a04e690-e948-47a2-84e4-0d9d239aaa27)

You link up to a maximum of 50 work items at one time, but there is no limit on the number of work items that can ever be linked.&#x20;

A link to the new linked Case or Ticket will appear in the [Linked Work tab](#viewing-linked-work-items-the-links-tab) in screen of the  work items that have been linked.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5Y57haPlSPBT5LLWQybt%2Fimage.png?alt=media\&token=7b8e3c38-33d0-4189-92b6-5e021591b6a7)

## Unlinking Work Items

You can unlink work items at any time by going to the Linked Work tab in the work item's screen and selecting the Unlink icon.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fh25KUp7VEyFd9yoxLyae%2FUnlink-Work-Items.gif?alt=media\&token=240e25e4-e4f3-490e-9b0b-2f5dc4817ac9)


# Creating New Linked Work Items

## Overview

Launching a Case or Ticket from within an existing one creates a ['Linked' relationship](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items) between the work items.&#x20;

Work items with a 'linked' relationship will retain a link to the original Case / Ticket but are completely independent, behaving according to their own specific configuration and not needing to wait for the other to complete before they can complete themselves. This is useful when the original Case/Ticket's due date is not dependent on some sub part being completed (e.g. by a different department).&#x20;

Linked work items will show on a [Linked Work tab](#viewing-linked-work-items-the-links-tab) in the work item screen, making it easy to track a group of work items which relate to each other.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8nmQi4DvzgH-T6v-J%2FClicking-on-links-tab.gif?alt=media\&token=8b5a6cf3-f6c5-4189-9dde-8c7c7efaf398)

Note that only Cases and Tickets can be 'linked' and  when a work item is linked to another work item and it is subsequently merged, split or converted into a Case, the subsequent work items resulting from this will also be linked to the original work item.

For example:

* When a Ticket is linked to another work item and that Ticket is merged in with another work the remaining merged item will be linked to the original work item.
* When a Ticket is linked to another work item and that Ticket is split into multiple Tickets, the subsequent child Tickets will also be linked to the original work item.
* When a Ticket is linked to another work item and that Ticket is later converted into a Case, the subsequent Case will also be linked to the original work item.

## Creating a new linked Ticket

To create a new linked Ticket from an existing Case or Ticket, click the ‘+ Work item’ link shown near the tabs section of the work item and the choose the 'Ticket' option from the dropdown.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F9RgXTZ0BL32R3dzkyb7Q%2Fimage.png?alt=media\&token=444275f4-4fa8-4747-8e03-8361ef9f0eae)

In the resulting pop up, you can filter to search for the new type of Ticket process you want to create in two ways:

* by searching by email route - you can specify the mailbox address which people would normally send emails into to create work items. Often an email mailbox represent a certain part of the business within which you want to create your new work item. As a useful shortcut we've added a feature here where you can search by mailbox and narrow down straight away the Ticket processes that you can choose from. Selecting a mailbox will filter the dropdown options to only the processes linked to that mailbox.
* by selecting a Customer, Contract, Service and a Ticket process to launch (these will default in values if there is only one option to choose).&#x20;

{% hint style="info" %}
Please note that the Tickets available for you to launch will depend on the permissions settings in Builder. Additionally, you will also only be able to select a Ticket process from an email route that has been enabled in Builder ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes)). You will also only be able to select a Ticket process in [Test Mode](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/test-mode) if the email route for that Ticket process has been configured to run in [Test Mode](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/test-mode).&#x20;
{% endhint %}

You can then adjust the following settings for the Ticket:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHRyZjtMbkGsJRvacJN5h%2Fimage.png?alt=media&#x26;token=a41677c9-9538-4a64-ad5d-660710a05129" alt=""><figcaption></figcaption></figure>

| Setting                   | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title                     | You can modify the title of the new Ticket you are creating                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Short Description         | You can modify the description of the new Ticket you are creating                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Category & Sub Categories | You need to select the category & sub categories of the new Ticket                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Override Due Date         | If your system has been configured this way ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours)), you can select to override the due date of the new Ticket you are creating.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Copy Defects              | You can copy existing defects from the original Case/Ticket to the new Ticket you are creating. Note that making updates to the Defects in the new linked Ticket will NOT update the defects in the original Ticket/Case it was created from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Copy Files                | <p>You can copy existing files that you have uploaded (including tags & file notes) from the original Case/Ticket to the new Ticket you are creating by selecting the Files option. <br><br><strong>Please Note</strong>: For Files that have been received via communications i.e emails, you will need to select Communications in the options in order to copy these files over. Note that making updates to the files in the new linked Ticket will NOT update the files in the original Ticket/Case it was created from.</p>                                                                                                                                                                                                                                                                                                                                          |
| Copy Links                | You can copy existing links (including tags & link notes) from the original Case/Ticket to the new Ticket you are creating. Note that making updates to the links in the new linked Ticket will NOT update the links in the original Ticket/Case it was created from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Copy Custom Data          | You can copy existing custom data (e.g. custom data fields) from the original Case/Ticket to the new Ticket you are creating. Note that making updates to the custom data in the new linked Ticket will NOT update the custom data in the original Ticket/Case it was created from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Copy Communications       | You can copy work item communications i.e. emails (this will include all email attachments i.e files) and notes from the original Case/Ticket to the new linked Ticket you are creating. Note that when choosing to copy communications, you will not only copy communications from the original work item, but you will also copy communications from the original work item's related group, e.g. its Actions if it was a Case, or the parent/child Ticket if it was from a split Ticket. Also note that making updates to the communications in the new linked Ticket will NOT update the communications in the original Ticket/Case it was created from. You can find out more about related groups vs linked work items [here](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items). |
| Send Automated Emails     | You can choose to send auto-generated system emails (e.g. Ticket creation acknowledgement emails) to contacts tagged as the the primary contact, requester or subject.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Adding Contacts           | You can choose to add a contact. If [permissions in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-groups) have been configured to allow you to do so, you can even choose to add multiple different contacts for the new Ticket and divide the tags between them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Select All                | You can chose to select all options that have been outlined above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

{% hint style="info" %}
If you wish to copy files that are attached to communications i.e emails, you will need to select the Communications option.
{% endhint %}

Then click to Create. A link to the new linked Ticket will appear in the ['Linked Work' tab](#viewing-linked-work-items-the-links-tab).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8nmQi4DvzgH-T6v-J%2FClicking-on-links-tab.gif?alt=media\&token=8b5a6cf3-f6c5-4189-9dde-8c7c7efaf398)

## Creating a new linked Case

Linked Cases will retain a link to the original Case / Ticket but are completely independent, behaving according to their own specific configuration and not needing to wait for the other to complete before they can complete themselves. This is useful when the original Case/Ticket's due date is not dependent on some sub part being completed (e.g. by a different department).&#x20;

To create a new linked Case from an existing Case or Ticket, click the ‘+ Work item’ link shown near the tabs section of the work item and the choose the 'Case' option from the dropdown.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fkh0p1fD44UgSbfF5beWB%2Fimage.png?alt=media\&token=7a1705fe-e03c-4efe-8b79-072f9551d8a2)

In the resulting pop up, you can filter to search for the new type of Case process you want to create in two ways:

* by searching by email route - you can specify the mailbox address which people would normally send emails into to create work items. Often an email mailbox represent a certain part of the business within which you want to create your new work item. As a useful shortcut we've added a feature here where you can search by mailbox and narrow down straight away the Case processes that you can choose from. Selecting a mailbox will filter the dropdown options to only the processes linked to that mailbox.
* by selecting a Customer, Contract, Service and a Case process to launch (these will default in values if there is only one option to choose).

{% hint style="info" %}
Please note that the Cases available for you to launch will depend on the permissions settings in Builder. Additionally, you will also only be able to select a Case process from an email route that has been enabled in Builder ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes)). You will also only be able to select a Case process in [Test Mode](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/test-mode) if the email route for that Case process has been configured to run in [Test Mode](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/test-mode).&#x20;
{% endhint %}

You can then adjust the following settings for the Case:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FK4obNHpKijIRF92f6LD0%2Fimage.png?alt=media&#x26;token=c5439d94-84d5-42b0-9c1f-e62055881032" alt=""><figcaption></figcaption></figure>

| Setting               | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Short Description     | You can modify the short description of the new Case you are creating                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Schedule              | If your system has been configured this way ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules)), you must select a schedule for the new Case you are creating.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Override Due Date     | If your system has been configured this way ([see here for more information](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours)), you can select to override the due date of the new Case you are creating.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Copy Defects          | You can copy existing defects from the original Case/Ticket to the new Case you are creating. Note that making updates to the defects in the new linked Case will NOT update the defects in the original Ticket/Case it was created from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Copy Files            | You can copy existing files (including tags and file notes) from the original Case/Ticket to the new Case you are creating. Note that making updates to the files in the new linked Case will NOT update the files in the original Ticket/Case it was created from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Copy Links            | You can copy existing links (including tags and link notes) from the original Case/Ticket to the new Case you are creating. Note that making updates to the links in the new linked Case will NOT update the links in the original Ticket/Case it was created from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Copy Custom Data      | You can copy existing custom data (e.g. custom data fields) from the original Case/Ticket with the new Case you are creating. Note that making updates to the custom data in the new linked Case will NOT update the custom data in the original Ticket/Case it was created from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Copy Communications   | You can copy work item communications i.e. emails (including email attachments) and notes from the original Case/Ticket to the new linked Case you are creating. Note that when choosing to copy communications, you will not only copy communications from the original work item, but you will also copy communications from the original work item's related group, e.g. its Actions if it was a Case, or the parent/child Ticket if it was from a split Ticket. Also note that making updates to the communications in the new linked Case will NOT update the communications in the original Ticket/Case it was created from. You can find out more about related groups vs linked work items [here](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items). |
| Send Automated Emails | You can choose if you want to send auto-generated system emails (e.g. Case creation acknowledgement emails) to contacts tagged as the the primary contact, requester or subject.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Adding Contacts       | Unless the '[Makes Contacts Mandatory](https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen/creating-new-case-types-in-a-service-line)' option in the Case type in the Service Line screen has been selected, it is optional for you to add a contact. You can even choose to add multiple different contacts and divide the tags between.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

Then click to Create. A link to the new linked Case will appear in the ['Linked Work' tab](#viewing-linked-work-items-the-links-tab).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8nmQi4DvzgH-T6v-J%2FClicking-on-links-tab.gif?alt=media\&token=8b5a6cf3-f6c5-4189-9dde-8c7c7efaf398)


# Viewing Linked Work Items

## **The '**&#x4C;inked Work' Tab

The Linked Work tab is where you can view all linked work items of a Ticket or Case.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8nmQi4DvzgH-T6v-J%2FClicking-on-links-tab.gif?alt=media\&token=8b5a6cf3-f6c5-4189-9dde-8c7c7efaf398)

{% hint style="info" %}
Note that Sub-Cases created via the '+ Work item' link will still display in the ['Sub Cases' tab](#sub-cases-tab) for the time-being, and do not show in the Links tab.
{% endhint %}

Within the Links tab grid you can a list of Linked work item, showing their reference, title, assignee, Queue and due date of a work item.

There is also an icon to unlink the work item if they have been linked in error.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjAK7hCvl3c29Z5AC5i%2F-MjAM4fjXwEFLXVpYTie%2FUnlink-Work-Items.gif?alt=media\&token=821b4c7f-6cf7-485e-b00b-e850314a0347)

You can also expand linked Cases to see their Actions.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8ndyBgMbiPJ-CCA8l%2FViewing-Actions-in-Links-Tab.gif?alt=media\&token=8298e2c7-ecff-403d-8f36-11d5f994c3db)

#### Linked Work Items you don't have permissions on

If you don't have permissions on a certain business process, the work items from that process will be greyed out and you won't be able to open or edit them. You'll still be able to see higher level information about the work item, e.g. who they're assigned to, which Queue they're in and when they're due.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8bfsVZGXLvBbi6qyKtvM%2Fimage.png?alt=media\&token=25bd33dd-65eb-4a2a-8f76-4b1874fc3563)


# Sharing Emails between Linked Work Items

As part of supporting work being carried out across multiple Cases & Tickets, you can share emails between Linked work items to allow them to be viewed more widely. You can even do this for work items which you don't have permissions on.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTkzMA==>" %}

You can share emails between linked work items in two ways.

**1. From an existing email -** Clicking on the '+' icon at the top of an existing email in the timeline and selecting the relevant work item you wish to share the email with.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj-yYmN4szIJhLTG8vB%2F-Mj01UH9EUpjZT_y_CLt%2FShare-Emails.gif?alt=media\&token=b0f8c92c-52ec-4b48-b47a-97d213c3d1e0)

**2. From composing new email -** Another way is when writing a new email, you can simply add the work item reference number into the To / CC / BCC of an email by clicking the '+' icon, just as you wold when adding an email address:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj-yYmN4szIJhLTG8vB%2F-Mj01PAuqmvGpPtNc2_f%2FSharing-Emails-Email-Address.gif?alt=media\&token=65dbbaaa-5e69-4b7b-9240-e502dbfba35b)

You can even use this approach when you just want to share emails between linked work items, without needing to add an email address.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj3Soql1rjdvHod10El%2F-Mj3Xgwpf2dxbspKNeix%2FShare-email-with-just-work-item.gif?alt=media\&token=93186f2b-00f8-4d7f-a3e3-fe407b247b42)

{% hint style="info" %}
Please note that you can only share emails between work items that are linked. You cannot share emails between Closed work items. Additionally, once an email has been shared between work items, it cannot be unshared.
{% endhint %}

The email will be sent as normal to any emails addresses specified, and it will also be shared with the selected work items.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj3ZyCIIEjWWqfh2mV3%2F-Mj3_1cZVLqWGox97zHS%2FClicking-on-shared-email.gif?alt=media\&token=3097d533-4f03-4392-95e5-b43deae8a21d)

When someone responds to the shared email, that response will be attached to both work items.


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


# Working Between Teams

## Communications between Internal Teams - Overview

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTk1MQ==>" %}

Sometimes when you're sending an email on a Work Item and you need to involve teams in other parts of your business, you may not know if they're using Enate yet to manage their work - particularly in larger organisations - and so it can be unclear precisely how to proceed.

**Now, when you're working in Enate, you no longer have to worry about this - the system will take care of this for you.** You can just write your mail and the system will know what to do next; if anyone internal is involved and they're using Enate, we'll prompt you with tickets or cases of theirs that you might want to share this email with, or quickly create a new work item if needed.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FywjKrldLFfslB6gfZArN%2Fimage.png?alt=media&#x26;token=0a8d55fc-a09c-4121-940e-632716b01315" alt=""><figcaption></figcaption></figure>

Doing so helps keep all subsequent communications tightly synched up between those teams and any external parties. If you're sending the email to someone who is not using Enate, the system will just send them the email.

## Example Scenarios

If we take an example where we have:

* Jane, an Agent working out of Team A in the UK
* Karina, an agent in Team B in Poland
* An external party who has mailed in a query initially relating to the UK, which lands with Team A

Jane in Team A is writing a response email to the external requestor also see that part of the query needs to involve their Polish team, Team B. Jane doesn't need to know if the Polish team are using Enate, she just adds their email address to her outgoing email.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FiYaRiJ11tvJ7sro1EtRI%2Fimage.png?alt=media&#x26;token=347d4b76-3cd4-4d29-9256-1fd11b45e801" alt=""><figcaption></figcaption></figure>

Enate knows that the Polish team's email address is connected to an Enate mailbox and so it's going to result in Ticket or Case for them. Upon clicking to send the email, Enate will bring up a pop-up explaining this to the Agent, and asking for some more information which will help in the creation of of the work item for the other team.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FC8cIYHSRImglHkLBZU2O%2Fimage.png?alt=media&#x26;token=e2b7f3df-5682-46d2-b2d8-9f26ae0e11b5" alt=""><figcaption></figcaption></figure>

Once the agent adds this further information to create a linked work item she can confirm to proceed. The email gets sent out to any external recipients, and the other team, Team B in Poland, see the email within a relevant, LINKED, Ticket or Case. Both Teams are aware of the other team's Linked ticket or Case and can keep themselves in the loop on progress.&#x20;

#### Teams working between Permissions boundaries

If Team B's activities happen to fall outside of Team A's permissions, they're still able to see at least the header-level information for it on the Linked Items screen.&#x20;

#### Downstream Emails kept in Synch

Importantly, all the downstream communications get kept tightly in synch.&#x20;

The External recipient can see both team's addresses on their email and, if they send back a response, BOTH teams will be updated at the same time. Everyone is kept in the loop.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUN2UuxBc9D7VR4BEv5VI%2Fimage.png?alt=media&#x26;token=93a35380-8343-4b89-8dc5-e07ceeb6915f" alt=""><figcaption></figcaption></figure>

In the most regular scenario, the pop-up would likely show the single, already linked ticket or Case which Team B are working on, essentially saying 'do you want to share this mail with Team B's running ticket?'.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCViyKRS3xlPeYNiEmNkY%2Fimage.png?alt=media&#x26;token=235e5d2b-1d3c-4bc8-9df5-b8a249eb738b" alt=""><figcaption></figcaption></figure>

#### What about other Teams not yet using Enate?

If there's any other internal email addresses added to a mail, going to areas of your business that *aren't* yet using Enate that's fine - they'll simply go out as emails to communicate with that other team as they normally would.&#x20;

### Requirement: 'Plus Addressing' Enabled on Your Company Mail Server

{% hint style="warning" %}
**IMPORTANT NOTE:** in order to make use of these features, your email admin team MUST have enabled the 'Plus Addressing' setting in your email server setup - this is what helps route all mails through to the right work items downstream.
{% endhint %}

For more information on Plus Addressing and how to enable it, see this article:

{% embed url="<https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#work-item-plus-addressing>" %}


# Assigning / Reassigning / Unassigning Work

## Assigning / Reassigning a Work Item to Yourself

Both Team Leaders and Team Members, (provided the Team Member has been set up with the 'Can Assign' permission in Builder, see [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/service-agents)for more information) have the ability to assign/reassign one or more work items to themselves or to other members of their team.  You can assign/reassign a work item to yourself in a number of ways:

1\) If the work item is not assigned to anyone, as soon as you start to do any activity which requires assignment the system will automatically assign the work to you (i.e. you do not need to manually set yourself as the assignee).&#x20;

2\)  If the work item is assigned to a different user, the system will display a short message when opening the work letting you know this. Click the ‘Take it’ grab icon to instantly assign the work item to yourself.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZDgAuFRyLxGN6vfFp6%2F-MZDya3ld_0eJMIp2MA0%2FAssign-Work-to-Me.gif?alt=media\&token=adc07bc1-05cd-42bc-befb-2d8bff2cf2b3)

3\) From the homepage grid by selecting which work items you want to reassign to yourself and clicking on the 'Reassign' button that will have appeared at the top of the grid. This will open up a popup where you can can then select the 'Reassign to me' option and you can also add a note if you wish.

### Alerting users when work is assigned to someone else

If you open an unassigned work item and subsequently make a change which would result in it being auto-assigned to you, if during the interim period another user has opened the same work item and has already assigned to themselves, the system will display a warning popup explaining that if you assign the work to you, any unsaved changes from the other user will be lost.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsSOirSEtRz8g5mP6S%2F-MWsUkq8vrFQqKut4pkJ%2Fimage.png?alt=media\&token=a53c8358-1671-460a-9856-b491dafcbbd4)

You have the choice to continue with assigning the work to you (which will discard the other person’s unsaved changes) or cancel your reassignment / update.

### Item Access vs. Assignment - Rules <a href="#item-access-vs-assignment-rules" id="item-access-vs-assignment-rules"></a>

Note that some activities can be performed even if the work is not assigned to you since they are purely additive:

* Adding a Note
* Sending an Email
* Adding an Action while in a Case

## Reassigning work items to someone else

Both Team Leaders and Team Members, (provided the Team Member has been set up with the 'Can Assign' permission in Builder, see [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/service-agents)for more information) have the ability to reassign one or more work items to themselves or to other members of their team. You can do this in a couple of ways.

1\) From the work item itself by clicking on the assignee dropdown in the header ribbon and selecting to reassign it to a different user. A popup will display; you can search for a user to assign work to and add a note to go along with the assignment. A notification message (including the note) will be sent to the new user.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZE0-5ewGX11JlZbWY-%2F-MZE0GaOSvt8u8nmYkWU%2FReassign-Work-Item.gif?alt=media\&token=b77704ce-bbd8-49df-be1c-7e930c12d1c1)

2\) From the homepage grid by selecting which work items you want to reassign and clicking on the 'Reassign' button that will have appeared at the top of the grid. Clicking on reassign will open up a popup where you can search for which team member you wish to reassign the work items to, and you can also add a note if you wish.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MY9zvqzI_emKhH87k8e%2F-MYAIAem9ck2jaTE-QpE%2FReassigning-Work.gif?alt=media\&token=6e20048a-fb22-4e46-bc0d-593bf8e4d3b3)

### **Reassigning Work Items to a Bot**

If a work item can be done by a robot, you can also choose to reassign the item to any individual bots that are in your team.&#x20;

You can also make that reassignment choice at the farm level by selecting ‘Any Bot within \[farm name]’. The system will then automatically assign the work item to one of the bots in the farm.

## Unassigning Work Items

Both Team Leaders and Team Members are able to unassign one or more work items. You are able to unassign work items in any state apart from Closed.

To unassign work items, select which work items you want to unassign from your Work Inbox. This will make the option to Reassign and Unassign appear at the top of the grid.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWqMXrK_ZvY1cj8JBqs%2F-MWqShfRNxgF9HFZDaBA%2Fimage.png?alt=media\&token=e621988b-272e-418a-9903-abb9d5641ebe)

Once you have unassigned the desired work items, they will then become available for users to pick up from their work Queue.

## Completing Work Items

If your system is set up to allow it, you are able to mark one or more work items from your Work Inbox as 'Complete' directly from the Work Inbox grid. Both Team Leaders and Team Members can use this function.

{% hint style="info" %}
Note: this is only possible for work items in your Work Inbox. Additionally, this is not possible for Cases or Peer Review Actions.
{% endhint %}


# Feedback Features

Information on how client users can provide feedback to you on specific work items, via feeback links available in the footer of emails sent from Enate.

## Customers can provide feedback via Email links <a href="#a-getting-customer-feedback-via-email" id="a-getting-customer-feedback-via-email"></a>

If the ‘Allow Feedback’ setting is ticked in the Ticket's Builder settings (see [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen/creating-ticket-case-and-action-types-in-a-service-line#c-creating-a-new-type-of-ticket)for more information on how to do this), outgoing emails will contain a footer-based link for recipients to give feedback scores.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4zO29YrBmW4yQ6Uqjt0y%2FEmail%20Feedback%20Link.png?alt=media&#x26;token=fce313ae-915d-476a-8d20-33a25cbe1be7" alt=""><figcaption></figcaption></figure>

They can do this at any point in the processing of the Ticket. When a client user clicks on any of these links, a browser window will be opened for them showing the Enate Feedback for&#x6D;*.* It offers the same feedback icons as shown in their email, but allows a user to change their selection should they wish, and also to add an additional comment before submitting.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqJeCsHClg50UMMQ99RpL%2Fimage.png?alt=media&#x26;token=b0cff73a-9481-450d-bca5-612cf16c05c1" alt=""><figcaption></figcaption></figure>

All feedback and comments are subsequently stored in Work Manager against this Ticket, for Agents to [view](#c-displaying-recent-feedback-details-via-work-items).&#x20;

Further to this, feedback data is stored in the Data Warehouse, allowing longer-term analysis of feedback data (i.e. you can build reports to analyse this data across multiple different criteria).

## Displaying client Feedback details on Tickets for Agents to View <a href="#c-displaying-recent-feedback-details-via-work-items" id="c-displaying-recent-feedback-details-via-work-items"></a>

When dealing with a Ticket, if a client user has provided feedback (via the feedback footer links in one of the emails they have received from Enate) Agents are able to see the customer’s current feedback rating via the 'smiley face' icon link in the ribbon bar of the Ticket:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPpVg6BeJDl6NCU5lsAN9%2FEmail%20Feedback%20Ribbon%20Link.png?alt=media&#x26;token=6c475b00-4f51-4cff-bbe8-1e4520cac29b" alt=""><figcaption></figcaption></figure>

Clicking on this will open a feedback popup displaying the client user's feedback rating/s (via emoticon), along with any associated comments.  The overall average rating, between 1 and 5 - calculated when feedback is given multiple times on a single Ticket - is also show at the top of the popup. Latest feedback is shown at the top of the screen.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fsm8rG0kpdepdw8QE1WXJ%2Fimage.png?alt=media&#x26;token=9132e523-c704-42ea-832f-1feef7450545" alt=""><figcaption></figcaption></figure>

Further to this, this feedback data is also stored in the Data Warehouse, allowing longer-term analysis of feedback data (i.e. you can build reports to analyse this data across multiple different criteria).


# Reports

## Overview

Enate's Work Manager provides you with embedded reporting capabilities, driven by [Microsoft's Power BI reporting platform](https://learn.microsoft.com/en-us/power-bi/), which gives you lots of additional information at your disposal to gain new insights and support for your business operations.

You get:

* [Standard, out of the box reports](#standard-reports-available) based on Enate data. Your user role will determine which standard reports you are able to see
* The ability to build on the standard reports to [create your own personalized reports](#editing-a-report) with exactly what you want
* The ability to [save your personalized reports](#saving-a-report) so you can easily navigate back to them
* The ability to [share your reports](#sharing-a-report) with whoever you think needs to see it
* Team Leaders or users with the 'Can customize reports' permission will also get access to [advanced editing options](#sharing-a-report) which allows them to create brand new visuals and to delete visuals, as well as the ability to create and delete cards

Watch this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQzOTIyMQ==>" %}

{% hint style="info" %}
Please note:

* Dates given to the creation of reports will be according to UTC time zone.
* When a report has been open for more than an hour, an error may appear within the visuals. Simply refresh your page to see the data again.
* Information regarding closed work items will only be shown for the past year. Open/running work items will show information spanning the entirety of its processing time, even if it has been longer than one year.
* Currently the moment reports are only available in English.
* Additionally, report data is not updated in real-time, and will be updated on regular scheduled intervals (last updated time stamp is shown on a report).
  {% endhint %}

## Accessing Reports

You can access reports from the brand new section in the Work Manager the nav menu.

Clicking on the main Reports link will open up the Reports page, with the default [standard report](#standard-reports-available) depending on your role displayed. For Team Leaders this will be the [Team View](#team-view) report and for Team Members it will be the [User's Overview](#users-view) report.

If you hover over the Reports link, you'll see a list of reports that you have access to, divided into various sections:

* [Standard Reports](#standard-reports-available) - here you'll see the standard, out of the box reports associated with your role data. Your user role will determine which standard reports you are able to see - generally, if you're someone with team member level access, you'll see the '[User's Overview](#users-view)' report, which shows data about your own work and if you've got more team leader-like access, you'll also be able to see the '[Team View](#team-view)', which looks at data about work across your team.&#x20;
* My Reports - here you'll see reports that you have personalized in some way and then saved as a new report
* Shared with Me - these are reports, custom or standard, that have been shared with you by someone else

Reports are sorted alphabetically and you can mark a report as a favorite. Favorite reports will appear above your 'non-favorite' reports.

## Report Structure Overview

Once you've opened up a report, you'll see the report name and when it was last updated at the top.

The 'All Reports' button will show you the list of reports that you have access to, divided into various sections:

* [Standard Reports](#standard-reports-available) - these are standard, out of the box reports associated with your role data.&#x20;
* My Reports - here you'll reports that you have personalized in some way and then saved as a new report
* Shared with Me - these are reports, custom or standard, that have been shared with you by someone else

You can [save a personalized report](#saving-a-report) by clicking the 'Save As' option and you can [share a report](#sharing-a-report) via the Share button.

A report will generally contain a mixture of cards, showing you headline level information, and a number of visuals.&#x20;

The data fields you'll have access to will depend on the report you have access to - each report has its own set of data fields. If you have access to a report, you have access to all of the data fields within the report too. For example, the 'User's Overview' report, and any report which was created from it, displays data about you and your work. The Team View report or, again, any report created from it, allows access to data about your team and the work in your business area more generally.

If there are any of your custom data fields that you'd like to see in your reports, ask your admin to get in touch with Enate Customer Support to get these made available for you.

All users have the ability to personalize a report to get the data to show just how they want, for example by applying filters or by adjusting the data fields. See the [personalizing a report](#personalizing-a-report) section to find out more about what options you have.

If you have the 'Can customize reports' permission, you'll be able to click on 'Advanced' mode and get access to more [advanced editing options](#advanced-mode), which includes all the standard personalization options as well the ability to create brand new visuals, to delete visuals, and to create and delete cards.

## Personalizing a Report

All users have the ability to personalize a report to get the data to show just how they want.

There are a number of filter options at the top that you can apply to the report. You can choose to filter the report by, customers, contacts and so forth, plus specific types of Case or Ticket (under the Process dropdown) and certain Queues or work in a given state. If you want to remove all these filters, click on the main Filter display button and scroll down to find the Clear Filters link.

Hovering over a visual also gives you further editing options. Links in the header of each visual will let you drill down and apply further filters.&#x20;

If you click on the personalize link you'll see much more options that you have to play with. You can change the visualisation type to show your data in a different way and you can change the data fields used in the visual. &#x20;

The data fields you'll have access to will depend on the report you have access to - each report has its own set of data fields. If you have access to a report, you have access to all of the data fields within the report too.&#x20;

For example, the 'User's Overview' report, and any report which was created from it, displays data about you and your work. The Team View report or, again, any report created from it, allows access to data about your team and the work in your business area more generally.

If there are any of your custom data fields that you'd like to see in your reports, ask your admin to get in touch with Enate Customer Support to get these made available for you.

You can also export an individual visual into Excel. There's also a 'focus' option to give a dedicated view of a single visual, and you can also choose to see the underlying data in a table.

You can easily discard your changes at any time by reverting back to the previous view of a visual.

You can find out more about the editing options you have from Microsoft's own Power BI documentation, available here:

{% embed url="<https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-personalize-visuals?tabs=powerbi-service>" %}

You can also [save a personalized report](#saving-a-report) by clicking the 'Save As' option, making it easier for you to come back to, and you can [share a report](#sharing-a-report) via the Share button.

## Saving a Report

You can save your personalized report so that you can access it easily ongoing by clicking the 'Save As' button.

Depending upon who originally created the report, there are a couple of options when it comes to saving a report:

* If you have made adjustments to a report created by someone else, you will have to save the report as a brand new (the 'saved as a new report' checkbox is auto-selected for you) since it's not your original report.
* If you have made adjustments to a report created by yourself (and the report is in your 'My Reports' section), you can either:

  * Update the existing report by clicking on 'Save As' and then de-selecting the 'Save as a new report' option
  * Save the report as a brand new report by clicking on 'Save As' and then selecting the option of saving the report as a brand new report&#x20;

  <figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fb5rtXuGF45b8VxR1FqGC%2Fimage.png?alt=media&#x26;token=92afd9e2-0e48-44b3-9b86-0a28e55665b5" alt=""><figcaption></figcaption></figure>

Once you have clicked 'Confirm', the saved report will appear in the 'My Reports' section, which you can access from the main system header, or from the reports list in your reports page. All your saved reports will appear here.

## Advanced Mode

In addition to all the [report personalization options](#personalizing-a-report) listed above, Team Leaders or people with the 'Can customize reports' permission will also get access to advanced editing options.

This lets them completely remove and create brand new visuals within a report, rather than just having the ability to modify existing ones, and gives them the ability to create and delete cards with headline level information.

You can easily discard your changes at any time by reverting back to the previous view of a visual

You can find out more about the advanced editing options you have from Microsoft's own Power BI documentation, available here:

{% embed url="<https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-personalize-visuals?tabs=powerbi-service>" %}

## Sharing a Report

You can also share reports with other users by clicking on the 'Share' option and selecting which users you want to share it with.&#x20;

The report will then show in the user(s) Shared Reports section.

{% hint style="info" %}
Note that you will only be able to share reports with someone if they have permission to view all of the data in the report.
{% endhint %}

You can also copy the Report link URL here too, if you want to share the report via another app.&#x20;

Reports that have been shared with you will appear in your Shared Reports list.

## Deleting a Report

When it comes to deleting reports, there are a few of things to be aware of.

* You can delete any of your own personalized reports i.e. any of the reports under the 'My Reports' section.
* You can delete any reports that have been shared with you i.e. any of the reports under the 'Shared Reports' section. Deleting a report that has been shared with you will not delete the report for anyone else.
* You cannot delete an original standard report. However, if you have personalized a standard report and saved that personalized report (and it therefore appears under the 'My Reports' section), you can delete that personalized report (see above point).
* Deleting a report that you have shared with another user will delete the 'original' report for you, as well as deleting the shared report for the other user. The report will also no longer be accessible for that user via a saved URL link.
* Any reports deleted by yourself will still be accessible via a saved URL link.

## Standard Reports Available

Currently, Enate provides three standard, out of the box reports:

* [User's Overview Report](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/reports/users-overview-report)
* [User Insights Report](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/reports/user-insights-report)
* [Team View Report](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/reports/team-view-report)
* [Sentiment Analysis Report](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/reports/sentiment-analysis-report)

Your user role will determine which standard reports you are able to see.&#x20;


# Team View Report

The Team View report displays information relating to email sentiment analysis allowing users to quickly and clearly see developing trends regarding incoming emails and take action where necessary.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FhM4LTJIKJdJ2smcGNH1o%2Fimage.png?alt=media&#x26;token=abf9e210-a14d-4bb7-9018-66ef4e2476a6" alt=""><figcaption></figcaption></figure>

### Accessing the Team View Report

Access to and the ability to edit the Team View is controlled by permissions in user roles, in the same way as all other reports within Enate. If users do not have the right permissions enabled, they will not be able to access or edit the report.

Here are some of the type of information which can be found within the report

### Team view Report Default Structure

#### Work Items Started by Month

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmELCxDvWMKYkxrJxIoUp%2FUntitled%20(7).png?alt=media&#x26;token=07ad2542-4981-4338-a61e-d8bcbe8ac93e" alt=""><figcaption></figcaption></figure>

* Ensure uninterrupted service and efficient workload planning by tracking monthly work item initiation volumes.

#### Work Items Closed by Month

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FH0vyJKcNSgD2eUUG9GGc%2FUntitled%20(8).png?alt=media&#x26;token=49a5ee9b-c96d-4b16-b3f4-39c9fecbed7c" alt=""><figcaption></figcaption></figure>

* Optimize resource availability and streamline operational efficiency by monitoring monthly work item closures.

#### Work Items Open by Ageing Category

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4FK09y7uriB0jCudSTRM%2FUntitled%20(9).png?alt=media&#x26;token=369f45ae-9479-4b82-ab08-47b96dd35cd1" alt=""><figcaption></figcaption></figure>

* Prioritize backlog resolution and task management by categorizing open work items by age in days.

#### Work item Count by Defect Category & Status

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZSg2vl69ZJ6N6GzX0k80%2FUntitled%20(10).png?alt=media&#x26;token=2386bd1a-ca5c-4d1b-b947-11dcc75086db" alt=""><figcaption></figcaption></figure>

* Aid targeted defect resolution and service quality improvement by highlighting defect categories needing attention.

#### Total Number of Users & Active Users by Month

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPvx8XbL8aUfOYyXTDkbi%2FUntitled%20(11).png?alt=media&#x26;token=304601f4-88e5-48f6-9d5d-af71f939451a" alt=""><figcaption></figcaption></figure>

* Enable efficient resource allocation and service delivery optimization with monthly user and active user counts.

### Available Data Fields for User Insights

See below for a complete list of all the available data fields that can be used within the User Insights report:

<table><thead><tr><th width="133">Table</th><th width="261">Fields</th><th width="380">Description</th></tr></thead><tbody><tr><td>Activity</td><td>Active Users</td><td>Count of users who are active on a selected date</td></tr><tr><td>Activity</td><td>Total Hrs Logged</td><td>Total time in hours spent by an Agent on all the Work Items they worked on for the selected date range</td></tr><tr><td>Activity</td><td>Total Users</td><td>Total number of users responsible for all the Work Items in a Queue</td></tr><tr><td>Activity</td><td>Activity Type</td><td>The type of activity performed on the Work Item by an Agent (e.g. 'Saved' or 'Completed')</td></tr><tr><td>Activity</td><td>Duration in Sec</td><td>Time spent in seconds on a Work Item by an Agent. Manually entered time is considered if available.</td></tr><tr><td>Activity</td><td>StartDate</td><td>The Work Item activity Start Date in date/time format</td></tr><tr><td>Activity</td><td>StartDate_date</td><td>The Work Item activity Start Date in date only format</td></tr><tr><td>Activity</td><td>User Name</td><td>The user who performed the activity</td></tr><tr><td>Context</td><td>Contract</td><td>The name of the contract</td></tr><tr><td>Context</td><td>Customer</td><td>The name of the customer</td></tr><tr><td>Context</td><td>Service</td><td>The name of the service</td></tr><tr><td>Context</td><td>Supplier</td><td>The name of the supplier</td></tr><tr><td>Date</td><td>Date</td><td>Calendar range of dates for filtering data</td></tr><tr><td>Date</td><td>Month</td><td>Months of the dates</td></tr><tr><td>Date</td><td>Week</td><td>Weeks of the dates</td></tr><tr><td>Date</td><td>Year</td><td>Year of the dates</td></tr><tr><td>Defects</td><td>Work Item Count</td><td>Number of Work Items that have defects</td></tr><tr><td>Defects</td><td>Date Raised</td><td>Date on which the defect was raised for a Work Item</td></tr><tr><td>Defects</td><td>Defect Category</td><td>Category of the defect</td></tr><tr><td>Defects</td><td>Description</td><td>Description of the defect</td></tr><tr><td>Defects</td><td>Status</td><td>States whether the defect is resolved or not</td></tr><tr><td>Feedback</td><td>Avg. rating</td><td>Average of ratings for each Work Item</td></tr><tr><td>Feedback</td><td>Rating</td><td>User rating for each Work Item</td></tr><tr><td>Feedback</td><td>Reference</td><td>Reference number of a Work Item that has feedback</td></tr><tr><td>Process</td><td>Process</td><td>Name of the process each Work Item belongs to</td></tr><tr><td>Process</td><td>Work Item Type</td><td>Type of the Work Item (Ticket, Action or Case)</td></tr><tr><td>Queues</td><td>Queue</td><td>Name of the queue the Work Item was last present in</td></tr><tr><td>Status</td><td>Status</td><td>Work Item Status (To Do, In Progress, Waiting , Resolved , Closed)</td></tr><tr><td>Status Reason</td><td>Status Reason</td><td>Reason behind the status change of the Work Item (Newly Created, new Info Receieved, Blocked by Business rule etc.)</td></tr><tr><td>Wait Status History</td><td>Waiting each Day</td><td>Count of Work Items that are set to waiting status on a particular day by the Agent (out of the Work Items he/she working/worked on)</td></tr><tr><td>Wait Status History</td><td>EndDate</td><td>End Date in Date time format when Work Item was in waiting state</td></tr><tr><td>Wait Status History</td><td>EndDate_date</td><td>End Date in Date only format when Work Item was in waiting state</td></tr><tr><td>Wait Status History</td><td>StartDate</td><td>Start Date in Date time format when Work Item was in waiting state</td></tr><tr><td>Wait Status History</td><td>StartDate_date</td><td>Start Date in Date only format when Work Item was in waiting state</td></tr><tr><td>Wait Status History</td><td>User Name</td><td>Agent who set the status of Work Item to Waiting</td></tr><tr><td>Work Items</td><td>Action</td><td>Sum of Closed and Waiting work items on a particular day by an Agent</td></tr><tr><td>Work Items</td><td>Work Items Assigned Today</td><td>Count of Work Items that are assgined to the agent today</td></tr><tr><td>Work Items</td><td>Work Items Closed</td><td>Total Work Items closed by agent for the selected date range</td></tr><tr><td>Work Items</td><td>Work Items Closed Today</td><td>Count of Work Items that are closed by agent today</td></tr><tr><td>Work Items</td><td>Work Items Due Today</td><td>Count of Work Items that are due today by agent</td></tr><tr><td>Work Items</td><td>Work Items Open</td><td>Total Work Items that are Open by agent</td></tr><tr><td>Work Items</td><td>Work Items Overdue</td><td>Total Work Items that are Overdue by agent</td></tr><tr><td>Work Items</td><td>Work Items Reopened</td><td>Total Tickets that are reopened for the agent</td></tr><tr><td>Work Items</td><td>Work Items Resolved</td><td>Total Work Items that are Resolved by agent for the selected date range</td></tr><tr><td>Work Items</td><td>Work Items Started</td><td>Total Work Items started by agent for the selected date range</td></tr><tr><td></td><td>Ageing Category</td><td>Grouping of Aging in Days into different buckets</td></tr><tr><td>Work Items</td><td>Ageing In Days</td><td>Ageing in calendar days. For completed Work Items its (end date - start date), for open items its (today - start date).</td></tr><tr><td>Work Items</td><td>Count of Affected Records</td><td>Records affected count</td></tr><tr><td>Work Items</td><td>Count of Defects</td><td>Count of defects each Work Item has (if any)</td></tr><tr><td>Work Items</td><td>Count of Rework</td><td>Count of rework each Work Item has (if any)</td></tr><tr><td>Work Items</td><td>DueDate</td><td>Work Item Due Date in date time format</td></tr><tr><td>Work Items</td><td>DueDate_date</td><td>Work Item Due Date in date only format</td></tr><tr><td>Work Items</td><td>EndDate</td><td>Work Item End Date in date time format</td></tr><tr><td>Work Items</td><td>EndDate_date</td><td>Work Item End Date in date only format</td></tr><tr><td>Work Items</td><td>Has Defects</td><td>Whether the Work Item has defect or not (Yes or No)</td></tr><tr><td>Work Items</td><td>Is Reopened</td><td>Tickets that got opened after going to resolved status</td></tr><tr><td>Work Items</td><td>Reference</td><td>Reference number of each Work Item</td></tr><tr><td></td><td>Resolved Date</td><td>Work Item resolved date in date/time format</td></tr><tr><td></td><td>Resolved Date_date</td><td>Work Item resolved date in date format</td></tr><tr><td>Work Items</td><td>SLA</td><td>Service Level Agreement to indicate where Work Item is Overdue or not</td></tr><tr><td>Work Items</td><td>StartDate</td><td>Work Item Start Date in date time format</td></tr><tr><td>Work Items</td><td>Start Date_date</td><td>Work Item Start Date in date only format</td></tr><tr><td>Work Items</td><td>Title</td><td>Title of the Work Item</td></tr></tbody></table>


# User's Overview Report

The User's Overview report displays information regarding the Enate user who's account has been used to sign in. The report shows all work relating to user allowing them to quickly plan their day and week accordingly.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzYrx0JUaoc59a9jAFznt%2Fimage.png?alt=media&#x26;token=b10006b0-b2f2-4de2-8da8-ff0769dae9ae" alt=""><figcaption></figcaption></figure>

### Accessing the User's Overview Report

Access to and the ability to edit the User's Overview is controlled by permissions in user roles, in the same way as all other reports within Enate. If users do not have the right permissions enabled, they will not be able to access or edit the report.

Here are some of the type of information which can be found within the report

### User's Overview Report Default Structure

#### Open Work Items by Queue & SLA

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fhi68Bu0tsd6QM1B79Yx0%2Fimage.png?alt=media&#x26;token=01ab32a3-1929-4de3-83b9-7498d3e3bde6" alt=""><figcaption></figcaption></figure>

* Pinpoint priority areas with SLA-tracked open work items by queues for efficient task management.

#### Closed Work Items by Month & SLA

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FF9ATemRiMcLGVHezEb76%2Fimage.png?alt=media&#x26;token=a0d77025-8985-49dc-9643-cc404fbfb461" alt=""><figcaption></figcaption></figure>

* Streamline workload management with monthly counts of started and closed work items, ensuring timely service delivery.

#### Started & Closed Work Item Count by Month

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIDb4Dnbb6MaHQm7EVMk8%2Fimage.png?alt=media&#x26;token=481a6389-e7fc-4b3b-bec7-0b96b328d2d6" alt=""><figcaption></figcaption></figure>

* Prioritize corrective actions with counts of resolved and unresolved defects by category, enhancing service quality.

#### Most Used Defect Categories

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4FdJqrJ0OWiutCYJa1HJ%2FUntitled%20(1).png?alt=media&#x26;token=7308eeef-cde8-4f41-8777-0092e07852e1" alt=""><figcaption></figcaption></figure>

* See which defect categories are being used and how many times they are used.

#### Active Hours Logged by Month

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5WfkPGjUNecArw0B1Vob%2Fimage.png?alt=media&#x26;token=1c2b2ad5-ccbd-4d9c-a72f-54b2a3717940" alt=""><figcaption></figcaption></figure>

* Gauge resource utilization and boost productivity with monthly-tracked active hours logged in Enate.

### Available Data Fields for User's Overview

See below for a complete list of all the available data fields that can be used within the User's Overview report:

<table><thead><tr><th width="133">Table</th><th width="261">Fields</th><th width="380">Description</th></tr></thead><tbody><tr><td>Activity</td><td>Total Hrs Logged</td><td>Total time (in Hrs) spent by the Agent on all the Work Items he/she worked on for the selected date range</td></tr><tr><td>Activity</td><td>Activity Type</td><td>Type of the activity performed on the Work Item by Agent ('Save' or 'Complete')</td></tr><tr><td>Activity</td><td>Duration in Sec</td><td>Time spent (in seconds) on the Work Item by Agent.  Manually entered time is considered if available.</td></tr><tr><td>Activity</td><td>StartDate</td><td>Work Item activity Start Date in date time format</td></tr><tr><td>Activity</td><td>StartDate_date</td><td>Work Item activity Start Date in date only format</td></tr><tr><td>Activity</td><td>User Name</td><td>User who performed the activity</td></tr><tr><td>Context</td><td>Contract</td><td>Name of the Contract</td></tr><tr><td>Context</td><td>Customer</td><td>Name of the Customer</td></tr><tr><td>Context</td><td>Service</td><td>Name of the Service</td></tr><tr><td>Context</td><td>Supplier</td><td>Name of the Supplier</td></tr><tr><td>Date</td><td>Date</td><td>Calendar range of dates for filtering data</td></tr><tr><td>Date</td><td>Month</td><td>Months of the dates</td></tr><tr><td>Date</td><td>Week</td><td>Weeks of the dates</td></tr><tr><td>Date</td><td>Year</td><td>Year of the dates</td></tr><tr><td>Defects</td><td>Work Item Count</td><td>Count of work items that have defects against them</td></tr><tr><td>Defects</td><td>Date Raised</td><td>Date on which the defect was raised for a Work Item</td></tr><tr><td>Defects</td><td>Defect Category</td><td>Category of the defect</td></tr><tr><td>Defects</td><td>Desciption</td><td>Description of the defect</td></tr><tr><td>Defects</td><td>Status</td><td>Stated whether the defect is resolved or not</td></tr><tr><td>Process</td><td>Process</td><td>Name of the process each Work Item belongs to</td></tr><tr><td>Process</td><td>Work Item Type</td><td>Type of the Work Item (Ticket, Action or Case)</td></tr><tr><td>Queues</td><td>Queue</td><td>Name of the queue the Work Item was last present in</td></tr><tr><td>Status</td><td>Status</td><td>Work Item Status (To Do, In Progress, Waiting , Resolved , Closed)</td></tr><tr><td>Status Reason</td><td>Status Reason</td><td>Reason behind the status change of the Work Item (Newly Created, new Info Receieved, Blocked by Business rule etc.)</td></tr><tr><td>Wait Status History</td><td>Waiting each Day</td><td>Count of Work Items that are set to waiting status on a particular day by the Agent (out of the Work Items he/she working/worked on)</td></tr><tr><td>Wait Status History</td><td>EndDate</td><td>End Date in Date time format when Work Item was in waiting state</td></tr><tr><td>Wait Status History</td><td>EndDate_date</td><td>End Date in Date only format when Work Item was in waiting state</td></tr><tr><td>Wait Status History</td><td>StartDate</td><td>Start Date in Date time format when Work Item was in waiting state</td></tr><tr><td>Wait Status History</td><td>StartDate_date</td><td>Start Date in Date only format when Work Item was in waiting state</td></tr><tr><td>Wait Status History</td><td>User Name</td><td>Agent who set the status of Work Item to Waiting</td></tr><tr><td>Work Items</td><td>Action</td><td>Sum of Closed and Waiting work items on a particular day by an Agent</td></tr><tr><td>Work Items</td><td>Work Items Assigned Today</td><td>Count of Work Items that are assgined to the agent today</td></tr><tr><td>Work Items</td><td>Work Items Closed</td><td>Total Work Items closed by agent for the selected date range</td></tr><tr><td>Work Items</td><td>Work Items Closed Today</td><td>Count of Work Items that are closed by agent today</td></tr><tr><td>Work Items</td><td>Work Items Due Today</td><td>Count of Work Items that are due today by agent</td></tr><tr><td>Work Items</td><td>Work Items Open</td><td>Total Work Items that are Open by agent</td></tr><tr><td>Work Items</td><td>Work Items Overdue</td><td>Total Work Items that are Overdue by agent</td></tr><tr><td>Work Items</td><td>Work Items Reopened</td><td>Total Tickets that are reopened for the agent</td></tr><tr><td>Work Items</td><td>Work Items Resolved</td><td>Total Work Items that are Resolved by agent for the selected date range</td></tr><tr><td>Work Items</td><td>Work Items Started</td><td>Total Work Items started by agent for the selected date range</td></tr><tr><td>Work Items</td><td>Ageing In Days</td><td>Aeing in calendar days. For completed Work Items its (end date - start date), for open items its (today - start date).</td></tr><tr><td>Work Items</td><td>Count of Affected Records</td><td>Records affected count</td></tr><tr><td>Work Items</td><td>Count of Defects</td><td>Count of defects each Work Item has (if any)</td></tr><tr><td>Work Items</td><td>Count of Rework</td><td>Count of rework each Work Item has (if any)</td></tr><tr><td>Work Items</td><td>DueDate</td><td>Work Item Due Date in date time format</td></tr><tr><td>Work Items</td><td>DueDate_date</td><td>Work Item Due Date in date only format</td></tr><tr><td>Work Items</td><td>EndDate</td><td>Work Item End Date in date time format</td></tr><tr><td>Work Items</td><td>EndDate_date</td><td>Work Item End Date in date only format</td></tr><tr><td>Work Items</td><td>Has Defects</td><td>Whether the Work Item has defect or not (Yes or No)</td></tr><tr><td>Work Items</td><td>Reference</td><td>Reference number of each Work Item</td></tr><tr><td>Work Items</td><td>Is Reopened</td><td>Tickets that got opened after going to resolved status</td></tr><tr><td>Work Items</td><td>SLA</td><td>Service Level Agreement to indicate where Work Item is Overdue or not</td></tr><tr><td>Work Items</td><td>StartDate</td><td>Work Item Start Date in date time format</td></tr><tr><td>Work Items</td><td>Start Date_date</td><td>Work Item Start Date in date only format</td></tr><tr><td>Work Items</td><td>Title</td><td>Title of the Work Item</td></tr></tbody></table>


# Sentiment Analysis Report

The Sentiment Analysis report displays information relating to email sentiment analysis allowing users to quickly and clearly see developing trends regarding incoming emails and take action where necessary.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F79rMZWJqGs9J1bfVurAp%2FSentiment%20Analysis.png?alt=media&#x26;token=cea9f992-001e-4c04-b573-d823e3c4d34c" alt=""><figcaption></figcaption></figure>

### How does the sentiment report work

In order for the Sentiment Analysis report to be available, the EnateAI Sentiment Analysis integration must be enabled (this can be done in Enate's Marketplace in Builder). When this integration runs it generates the data needed for the report. Once this integration has been activated, information will automatically begin to be sent into and displayed in the report.

### Accessing the Sentiment Analysis Report

Access to and the ability to edit the sentiment report is controlled by permissions in user roles, in the same way as all other reports within Enate. If users do not have the right permissions enabled, they will not be able to access the report. To edit the report users will need the 'Create Custom Reports' permission enabled.

Here are some of the type of information which can be found within the report

### Sentiment Analysis Report Default Structure

#### Email Count by Sentiment Type

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F12OyPivDvBQiMtIWvGOW%2Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_MtDEOm00cFDVBzGMarDS_image.webp?alt=media&#x26;token=c9d16bc8-0d3f-42fc-bb63-0ce78996b1fa" alt=""><figcaption></figcaption></figure>

* View the overall share and count of incoming emails analysed as having a positive, neutral or negative sentiment.

#### Sentiment Trend

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fultn9sTpbe7wDSLR1hk8%2Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_BR61C5evpdYFONob3G5P_image.webp?alt=media&#x26;token=55768a8d-e61a-4009-9d6f-e00cf90d3b04" alt=""><figcaption></figcaption></figure>

* Track the fluctuation of email sentiment over time. Look out for any significant changes and address them accordingly.

#### Sentiment Comparison by Context

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnXYvp7EZsYP377IVGlkR%2Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_k9cHkXc0mK2xsPQxcjWl_image.webp?alt=media&#x26;token=1967c612-3594-488e-9ed4-de937b7e0d28" alt=""><figcaption></figcaption></figure>

* Compare email sentiment across your companies, regions, services and processes. Take action accordingly.

#### Senders with Email Count

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnoIOcySBg0xvv32Bnz1s%2Fimage.png?alt=media&#x26;token=612ede02-e466-447d-9fca-1e93a2924e2f" alt=""><figcaption></figcaption></figure>

* Identify top senders based on email volume and sentiments to address customer concerns effectively and efficiently.

#### Agents with Email Count

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6ZGY42RdcKwIpAt0sUol%2Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_XB00vuNVuaznOg1wxNNc_image.webp?alt=media&#x26;token=ee00ed70-f0c8-4c07-ad31-865a5126e7b6" alt=""><figcaption></figcaption></figure>

* View the agents that receive the highest volume of positive or negative emails, highlighting areas for improvement or recognition.

#### Sentiment by Workitems with Multiple Handoffs

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fu9zLG2I3B7J04fKckLiC%2Fimage.png?alt=media&#x26;token=e25f1a2e-fc04-46dd-9e56-60f224843543" alt=""><figcaption></figcaption></figure>

* View how the number of agents a work item is assigned to affects client sentiment. Take action accordingly.

#### Sentiment by Work Items Total Elapsed (Hrs)

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHirfYVuLKI5BOhCnKgAH%2Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_Dt4bUZZ00ZPgvbJZjitb_image.webp?alt=media&#x26;token=a42f4cfa-724e-4cc2-b7f4-93c4a7974a66" alt=""><figcaption></figcaption></figure>

* View how the length of time a work item is open for affects client sentiment. Take action accordingly.

#### Sentiment by SLA

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPB37Ciq18IeTKu9064qJ%2Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_GgdhIgIScPNMg5hfDehq_image.webp?alt=media&#x26;token=2abc94f2-58cc-4377-8207-3ebebb3ab116" alt=""><figcaption></figcaption></figure>

* View how meeting and not meeting the SLA on a work item affects client sentiment. Take action accordingly.

#### Sentiment by Reopened Workitems

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIcsIydPFasJnzQ3fAk1r%2Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_53swI0vm9cpgYyxgrwUs_image.webp?alt=media&#x26;token=fbedd8cf-1a4a-4afd-8050-998cb0a43fab" alt=""><figcaption></figcaption></figure>

* View how reopening work items affects client sentiment. Take action accordingly.

#### Sentiment by Workitems with Defects

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjfU22h9kN0kyeHyvdQJJ%2Fspaces_8xJkS0SKlesb8bmVBtGc_uploads_nvj3FPgBduHXXQshYF35_image.webp?alt=media&#x26;token=1dc8cc83-9911-4fd3-9a13-4a104f9e25a5" alt=""><figcaption></figcaption></figure>

* View how raising defects on work items affects client sentiment. Take action accordingly.

### Available Data Fields for Sentiment Analysis

See below for a complete list of all the available data fields that can be used within the Sentiment Analysis report:

<table><thead><tr><th width="171">Table</th><th width="240">Fields</th><th width="319">Description</th></tr></thead><tbody><tr><td>Context</td><td>Contract</td><td>Name of the Contract</td></tr><tr><td>Context</td><td>Customer</td><td>Name of the Customer</td></tr><tr><td>Context</td><td>Service</td><td>Name of the Service</td></tr><tr><td>Context</td><td>Supplier</td><td>Name of the Supplier</td></tr><tr><td>Date</td><td>Date</td><td>Calendar range of dates for filtering data</td></tr><tr><td>Date</td><td>Month</td><td>Months of the dates</td></tr><tr><td>Date</td><td>Year</td><td>Year of the dates</td></tr><tr><td>Feedback</td><td>Comments</td><td>Feedback comments given on each workitem</td></tr><tr><td>Feedback</td><td>Logged</td><td>Feedback logged date in date time format</td></tr><tr><td>Feedback</td><td>LoggedDate</td><td>Feedback logged date in date format</td></tr><tr><td>Feedback</td><td>Rating</td><td>Feedback rating from 1 - 5</td></tr><tr><td>Feedback</td><td>6M Moving Avg(Ratings)</td><td>6 months moving average over the number of ratings. To be visualised against dates.</td></tr><tr><td>Feedback</td><td>Avg. Rating</td><td>Average ratings given across all workitems</td></tr><tr><td>Feedback</td><td>Total Ratings</td><td>Total number of ratings given</td></tr><tr><td>Feedback Types</td><td>Feedback Type</td><td>Ratings grouped as Happy, Unhappy &#x26; Neutral</td></tr><tr><td>Process</td><td>Process</td><td>Name of the process each Work Item belongs to</td></tr><tr><td>Process</td><td>Process Group</td><td>Process group given for Cases / Tickets</td></tr><tr><td>Process</td><td>Work Item Type</td><td>Type of the Work Item (Ticket, Action or Case)</td></tr><tr><td>Sentiment Scores</td><td>Logged</td><td>Email logged date in date time format</td></tr><tr><td>Sentiment Scores</td><td>LoggedDate</td><td>Email logged date in date format</td></tr><tr><td>Sentiment Scores</td><td>Sender</td><td>Email sender's full name or email address (depending on whichever is availible)</td></tr><tr><td>Sentiment Scores</td><td>Sentiment Confidence</td><td>Confidence level of the email classification (or sentiment score) in percentage (0 - 100%)</td></tr><tr><td>Sentiment Scores</td><td>6M Moving Avg</td><td>6 months moving average over the number of emails that have sentiment scores. To be visualised against dates.</td></tr><tr><td>Sentiment Scores</td><td>Email Count</td><td>Total number of emails that sentiment score</td></tr><tr><td>Sentiment Scores</td><td>Work Item Count</td><td>Total number of workitems with emails that have sentiment score</td></tr><tr><td>Sentiment Types</td><td>Sentiment Type</td><td>Types of sentiment (Positve, Negative or Neutral)</td></tr><tr><td>Ticket Categories</td><td>Ticket Category1</td><td>Ticket Category level 1</td></tr><tr><td>Ticket Categories</td><td>Ticket Category2</td><td>Ticket Category level 2</td></tr><tr><td>Ticket Categories</td><td>Ticket Category3</td><td>Ticket Category level 3</td></tr><tr><td>Users</td><td>User Name</td><td>Full name of the user responsible for the work item</td></tr><tr><td>Users</td><td>Email Address</td><td>Email address of the user responsible for the work item</td></tr><tr><td>Users</td><td>Team Manager</td><td>Full name of the manager of the users responsible for the work item</td></tr><tr><td>Work Items</td><td>Assigned User Count Groups</td><td>Grouping of Assigned User Count into different buckets (e.g., 0, 1-3, 3-5, 5-7 etc.). Assigned User Count is the unique number of users assigned to the work item througout it's lifecycle (from start to end).</td></tr><tr><td>Work Items</td><td>Customer Duration(Hrs)</td><td>Total time (in working hours) taken to complete the work item as per the customer calendar. Value will be blank if the work item is still in progress.</td></tr><tr><td>Work Items</td><td>Customer Duration Groups</td><td>Grouping of Customer Durations into different buckets (e.g., 0-24, 24-48, 48-72, 5-7 etc.)</td></tr><tr><td>Work Items</td><td>DueDate</td><td>Work Item Due Date in date time format</td></tr><tr><td>Work Items</td><td>EndDate</td><td>Work Item End Date in date time format</td></tr><tr><td>Work Items</td><td>Has Defects</td><td>Whether the Work Item has defect or not (Yes or No)</td></tr><tr><td>Work Items</td><td>Is Reopened</td><td>Tickets that got opened after going to resolved status</td></tr><tr><td>Work Items</td><td>Reference</td><td>Reference number of each Work Item</td></tr><tr><td>Work Items</td><td>ResolvedDate</td><td>Work Items Resolved Date in date time format</td></tr><tr><td>Work Items</td><td>SLA</td><td>Service Level Agreement to indicate where Work Item is Overdue or not</td></tr><tr><td>Work Items</td><td>StartDate</td><td>Work Item Start Date in date time format</td></tr><tr><td>Work Items</td><td>Title</td><td>Title of the Work Item</td></tr><tr><td>Work Items</td><td>Supplier Duration(Hrs)</td><td>Total time (in working hours) taken to complete the work item as per the supplier calendar. Value will be blank if the work item is still in progress.</td></tr></tbody></table>


# User Insights Report

The User Insights report provides information about a team such as when they are due to go on leave and how they are feeling. This allows team leaders to take prompt action and make adjustments to cover any team absences or drops in team morale.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FG9gy0j74A9A0xEuJvxK9%2Fimage.png?alt=media&#x26;token=4fec58b4-d2f9-48f4-a5b6-bddf6f9b77aa" alt=""><figcaption></figcaption></figure>

### Accessing the User Insights Report

Access to and the ability to edit the User Insights is controlled by permissions in user roles, in the same way as all other reports within Enate. If users do not have the right permissions enabled, they will not be able to access or edit the report.

Here are some of the type of information which can be found within the report

Here are some of the type of information which can be found within the report

### User Insights Report Default Structure

#### Leave

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FV2Z7gVOPcCZSIy34LO0o%2FUntitled%20(2).png?alt=media&#x26;token=c7f89ad6-5c55-4f36-920a-e0c9628ace22" alt=""><figcaption></figcaption></figure>

* Optimize resource management by exploring your team's leave dynamics.

#### Non-working days & Public Holidays

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FxnEVfVhhZcoJi4tlCxrg%2FUntitled%20(3).png?alt=media&#x26;token=7bdcb7b7-9cec-4554-86d1-a80e96c167f6" alt=""><figcaption></figcaption></figure>

* Strategically plan downtime using public holidays and breaks for work scheduling.

#### Where Time is Spent

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkrrvksprXCNISCatCV8U%2Fimage.png?alt=media&#x26;token=da19cb35-6c3b-4d55-bba3-99c093ffbb34" alt=""><figcaption></figcaption></figure>

* Understand team productivity through efficiency analysis and time allocation metrics.

#### Overall sentiment

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FD0L0mPILmEqxBVMsUzec%2FUntitled%20(5).png?alt=media&#x26;token=02f99e63-63b2-4b95-aad4-efb63abc2b8f" alt=""><figcaption></figcaption></figure>

* Enhance performance by assessing team morale and fostering a positive work environment.

#### Sentiment trend

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5T2EyExJN8G9XxsDwoNL%2FUntitled%20(6).png?alt=media&#x26;token=969bae28-abce-456e-81d2-a2f8f090695d" alt=""><figcaption></figcaption></figure>

* Cultivate consistent success with daily mood assessments, promoting productivity and positivity.

### Available Data Fields for User Insights

See below for a complete list of all the available data fields that can be used within the User Insights report:

<table><thead><tr><th width="261">Table</th><th width="261">Fields</th><th width="380">Description</th></tr></thead><tbody><tr><td>Date</td><td>Date</td><td>Day of the week in DDMM Format</td></tr><tr><td>Date</td><td>Week</td><td>Week of the year</td></tr><tr><td>Date</td><td>Month</td><td>Month of the Year in MMYY format</td></tr><tr><td>Date</td><td>Year</td><td>Calendar Year</td></tr><tr><td>Sentiment type</td><td>Sentiment</td><td>Sentiments options (Excellent, Very Good, Good, Bad, Worse). It will be none if not entered.</td></tr><tr><td>Insights</td><td>Avg. other hours</td><td>Avg. hours spent on ad hoc tasks</td></tr><tr><td>Insights</td><td>Avg. contractual break hours</td><td>Avg. hours spent on breaks</td></tr><tr><td>Insights</td><td>Avg. idle hours</td><td>Avg. hours spent on system downtime</td></tr><tr><td>Insights</td><td>Avg. feedback/1-2-1 hours</td><td>Avg. hours spent on feedback sessions</td></tr><tr><td>Insights</td><td>Avg. work performed within Enate </td><td>Avg. hours spent in Enate (on cases, actions or tickets)</td></tr><tr><td>Insights</td><td>Avg. work performed outside Enate</td><td>Avg. value added hours spent outside the Enate</td></tr><tr><td>Insights</td><td>Avg. meeting hours</td><td>Avg. hours spent on meetings</td></tr><tr><td>Insights</td><td>Avg. training hours</td><td>Avg. hours spent on training sessions</td></tr><tr><td>Insights</td><td>Avg. working hours</td><td>Avg. working hours</td></tr><tr><td>Insights</td><td>Other hours </td><td>Total hours spent on adhoc tasks</td></tr><tr><td>Insights</td><td>Contractual break hours</td><td>Total hours spent on breaks</td></tr><tr><td>Insights</td><td>Idle hours </td><td>Total hours spent on system downtime</td></tr><tr><td>Insights</td><td>Feedback/1-2-1 hours </td><td>Total hours spent on feedback sessions</td></tr><tr><td>Insights</td><td>Work performed within Enate</td><td>Total hours spent in Enate (specifically on Cases, Actions or Tickets)</td></tr><tr><td>Insights</td><td>Work performed outside Enate</td><td>Total value-added hours spent outside the Enate</td></tr><tr><td>Insights</td><td>Leaves count</td><td>Planned leave count for the user(s)</td></tr><tr><td>Insights</td><td>Meeting hours </td><td>Total hours spent on meetings</td></tr><tr><td>Insights</td><td>Non-working days count</td><td>Non-working day count for the user(s) includes holidays weekends etc</td></tr><tr><td>Insights</td><td>Sentiment count</td><td>Count of sentiments entered by user(s) for a particular day</td></tr><tr><td>Insights</td><td>Training hours</td><td>Total hours spent on training sessions</td></tr><tr><td>Insights</td><td>Working hours</td><td>Total working hours</td></tr><tr><td>Insights</td><td>Comment</td><td>Comments added by user for the sentiment chosen</td></tr><tr><td>Insights</td><td>Insights date</td><td>Date when the durations/sentiments captured from the user</td></tr><tr><td>Users</td><td>Email address</td><td>Email address of the user(s)</td></tr><tr><td>Users</td><td>User name</td><td>Full name of the user(s)</td></tr><tr><td>WorkDay type</td><td>Work day</td><td>Type of the day (Working, Non-working Day, Leave). It will be none if nothing is chosen by the user.</td></tr></tbody></table>


# User Availability Insights

## Overview - what is the Insights feature?

The optional 'Insights' feature lets you capture key information regarding the availability of agent users. This can help Team leads and Operations Managers to better schedule work by giving them a view of where time is being spent day-to-day.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTcyNTQ4MQ==>" %}

### How does it work?

If Insights is switched on in your system (see [Enabling Insights](#enabling-insights)), when users log into Work Manager for the first time each day, they'll be met with a **popup** after a short while, asking them to confirm:

* **Their working hours for the day**, e.g. 8 hrs (this may default in a value from their working calendar if one is set for them, or from the previous day's entered value.
* **a rundown of any non-core activities they may have planned for the day**, for example a training session, or 1-2-1 meetings, plus their expected working hours for the day.&#x20;
* **optionally,** they can note down how they're currently feeling too.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVKQR2GsFyEQeSftVjbpS%2FSm%20Insights%20Popup2.png?alt=media&#x26;token=382a1f5b-fa73-4208-a53f-3829347260b5" alt=""><figcaption></figcaption></figure>

The purpose of this popup is to allow agents to note down the time when they will be busy on activities such as meetings or 1-to-1 feedback sesssions.

This data can then be assessed by Team Leader and Operations Managers to help form a clearer picture of how much time is available for actively working on Cases, Ticket and & Actions versus other indirect activities such as attending Meetings or Training courses or similar. As part of this, obviously the overall number of working hours available for a given day for that user needs to be captured, as well as things like expected break totals.&#x20;

Over time, Team Leaders will be able to form a picture of the overall amount of time available for these different activities, and spot trends to help them predict capacity going forward. There's also the ability for some short term *forward* planning if we have visibility of agents' expected time available over the next few days.

#### Enabling Insights

The Insights feature can be enabled / disabled by Admin This feature can be enabled from the [General Settings](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#employee-availability-insights) section of Builder.

### The different section of Insights

The Insights Feature has the following main sections:

{% content-ref url="user-availability-insights/the-insights-popup" %}
[the-insights-popup](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-availability-insights/the-insights-popup)
{% endcontent-ref %}

{% content-ref url="user-availability-insights/main-insights-page" %}
[main-insights-page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-availability-insights/main-insights-page)
{% endcontent-ref %}

{% content-ref url="user-availability-insights/main-insights-page-team-leader-features" %}
[main-insights-page-team-leader-features](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-availability-insights/main-insights-page-team-leader-features)
{% endcontent-ref %}

{% content-ref url="user-availability-insights/the-user-insights-report" %}
[the-user-insights-report](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-availability-insights/the-user-insights-report)
{% endcontent-ref %}

## Whose Data can I see?

In the Main Insights Page, and the Insights Report, you will only see your own availability insight data. If you have people that report to you in Enate, you'll also be able to see the data from your team members, depending on the level of feature access you have set in your user role, specifically:

* Users with the 'Set up Team & Queues' feature access option - set in the User Roles section of Builder - will be able to see the information entered by **themselves and their team** (i.e. the people who they manage).
* Users *without* the 'Set up Team & Queues' feature access option will only be able to see their **own** data.&#x20;


# The Insights Popup

If Insights is switched on in your system (see [Enabling Insights](#enabling-insights)), when users log into Work Manager for the first time each day, they'll be met with a **popup** after a short while, asking them to confirm:

* **Their working hours for the day**, e.g. 8 hrs (this may default in a value from their working calendar if one is set for them, or from the previous day's entered value.
* **a rundown of any non-core activities they may have planned for the day**, for example a training session, or 1-2-1 meetings, plus their expected working hours for the day.&#x20;
* **optionally,** they can note down how they're currently feeling too.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FK3llrG2L0f588G76oGSB%2FSm%20Insights%20Popup2.png?alt=media&#x26;token=2ddb2bc9-9b8c-40c1-885d-876bd4c6339f" alt=""><figcaption></figcaption></figure>

There are three sections to the popup, which will ask Agents about:

* **Today -** what their working hours and break is for today, plus if they have any non-core work activities planned.
* **Yesterday** - confirm if the data tey entered yesterday ended up being correct, amending if needed.
* **Tomorrow** - if they have visibility on what tomorrow looks like, they can fill this in too.

{% hint style="info" %}
**If you are going to be using the Insights feature, every agent should ensure that they have confirmed their data for any day they are working.** \
**Team Leaders have visibility on who has not filled in data, and on which days.**
{% endhint %}

Note that agents don't have to fill in their data straight away when the popup appears - they can always revisit the popup later in the day by clicking on the Insights link in their toolbar. If data is incomplete for that user, it will show with a red dot icon..

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F2jFVTQmRHPQpRqYTKxKR%2Fimage.png?alt=media&#x26;token=7df2858f-1d23-47fd-b2ea-6c34d257fa3e" alt=""><figcaption></figcaption></figure>

They can also fill in and amend data via the main 'Insights' page, which they can get to from the nav icon.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXu6d3AuO5zdgS7Shjqpo%2Fimage.png?alt=media&#x26;token=7ac072a9-0b2d-48e2-81a5-75bf2b6ab154" alt=""><figcaption></figcaption></figure>

### Filling in the Insights Popup

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Figy04OM1bpR9C3coQKcc%2FSm%20Insights%20Popup2.png?alt=media&#x26;token=fea4a9d8-9cc0-4bd7-87e7-5d0bfbb15029" alt=""><figcaption></figcaption></figure>

The user can either provide the data in the pop-up pages then and there, or click 'X' to close the popup without saving any data. If a user hasn't filled in the data in the pop-up and they they logout and log back in again on the same day, the pop-up will reappear when they log back in.&#x20;

### The 'How are you feeling?' section

This section is optional - users can select an emoji to represent how they are feeling. They can also choose to enter an additional comment.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F98uNl5THmdV1kSCLjV7j%2Fimage.png?alt=media&#x26;token=711d32d9-a766-4fe5-9dbb-560037222918" alt=""><figcaption></figcaption></figure>

### Working Hours confirmation section

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7PvHb9Zzvyrj1MFVHvxm%2Fimage.png?alt=media&#x26;token=82455a43-3661-4a62-bf7d-eab20cf75b5e" alt=""><figcaption></figcaption></figure>

The next section is asking the agent to confirm their overall working hours for the day. There may be defaulted numbers in for your expected working hours (e.g. 8 hours) and expected break (e.g. 1 hour). These may come from the working calendar if one has been set up in Enate, or from whatever values wer entered the previous day. If not such data is available, these will default to 08:00 hrs and 00:00 hrs respectively.

**If either of these these need to be changed, clicking the link provided takes the user to the** [**Main Insights Page**](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-availability-insights/main-insights-page) **where they can set this information.**

There's also the option to set this day as:

* **A Non-working day** - e.g. a weekend day or time-in-lieu equivalent
* **On leave** - i.e. the agent is on leave / vacation that day.\*

*\*Note that users can set this information a number of days in advance via the main Insights page if  e.g. they are going on vacation.*

If either of the 'Non-Working Daya / On-Leave' settings are marked for this day, the user won't be asked to fill in a break-out of their time for that day.

### Activity Breakdown section - Today

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNSfywGk8gk8FyJr2n5DV%2Fimage.png?alt=media&#x26;token=c74a5360-adcf-4ca3-ae5c-29a81bb36494" alt=""><figcaption></figcaption></figure>

The next sections of the pop-up will ask the user for expected time they'll be spending that day on non-core activities. Agents can use the slider or manually enter a value between 0 and 8 hrs.&#x20;

### What Should I fill in for the Insights Activities?

{% hint style="info" %}
For clarity here: This section is where you should add any time which you know *can't* be spent actively working to deliver service because you have e.g a meeting. The expectation is absolutely *not* that you add in numbers to add up to e.g. 7 hours to 'fill your day' - doing that would signal to your Team Leader that you've no availability to work. &#x20;

Instead, this is where you enter that e.g. you know you've got 2 hours of meetings today, so your Team Leader will know that of the 7 working hours left in your day after breaks, only 5 of them can be time available to actively work.
{% endhint %}

Options available to enter for 'Today' are:

* **Meetings** - time spent in any collaborative gathering or group meeting.
* **Feedback / 1-2-1** - time spent in individual sessions with e.g. team leader, manager, mentor.
* **Training** - time in organised training or knowledge-transfer sessions.
* **Other** - time spent on any other activities which are not listed above, or any additional breaks taken in a day.

When finished filling in data (inlcuding if there are no such activities and the day is fre for active work), users have two options:

**Click 'Save & Close'** to close the popup and get back to Enate Home Screen OR

**Click 'Save & Next'** to add further data for yesterday (prev. working day) and Tomorrow.

If they click 'Save and Close', they are done and the system will mark their mandatory Insights data as filled in for that day. Clicking 'Save & Next'

### Confirming Yesterday's Activities

Confirming data for yesterday / the previous working day is much the same as entering for today..

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbMg4BwycuZrRJyxALCdu%2Fimage.png?alt=media&#x26;token=22b83d45-0266-41cd-a9bd-807f9044b045" alt=""><figcaption></figcaption></figure>

In addition to the categories available for 'Today', two further options are available to confirm where time was spent:

* **Active Time not tracked by Enate** - Time spent actively working to provide service but where a Ticket, Case or Action screen (or Enate email) is NOT open in Enate to auto-track this time.

  Examples might be: time spent on the Enate homepage or working in another system where an Enate work item tab is not open and so not auto-tracking time. This does NOT include activities such as meetings or training, which should be noted separately.
* **Downtime** - Time lost due to, e.g. system issues, or non-availability of work.

All data can be modified, including the working hours and break times. If all expected hours entered the day before were correct, the user can hit 'Save and Next'. Otherwise, adjust the data before moving on.

### Entering Data for Tomorrow

Entering data for tomorrow gives the same options as entering for 'Today'

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fa9BisIfXdpA3GluIL6z7%2Fimage.png?alt=media&#x26;token=0f6b232c-997d-461b-82c0-49658df03bc8" alt=""><figcaption></figcaption></figure>

Once fully complete, users shoud click 'Save and Done'.

At any point users can click back to the popup to adjust data enetered for today, yesterday & tomorrow, and can access the [Main Insights Page](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-availability-insights/main-insights-page).


# Main Insights Page

The Insights page, available from the main menu, shows a daily breakout of your Insights Data, relating to how time is spent each day. [**Team Members**](#insights-page-for-team-members) use this screen to **view and adjust** their Insights data across a number of days via the calendar control. [ **Team Leaders**](#insights-page-for-team-leaders) have these same options, plus additional features available for this page, [detailed here](#insights-page-for-team-leaders).

Team Leaders can use this data to see patterns in how time is being spent through their team, both here and in the [Insights Report.](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-availability-insights/the-user-insights-report) Insights into upcoming availability of their team can also be seen here and such data can contribute to further reports to help with short-term capacity planning.\
\
**Team Leaders should primarily use this page to help ensure all required data has been filled in by their team.**

### Accessing the Insights page

You can access the Insights page from the Nav item option, and via a link at the top of the [Insights Popup](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-availability-insights/the-insights-popup).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkcwaK7OQ7YN5r8VFAubQ%2Fimage.png?alt=media&#x26;token=ff60015c-5256-464a-928d-481ca8abb60d" alt=""><figcaption></figcaption></figure>

## Insights Page for Team Members

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F44U753yOKomllp9o9WXr%2Fimage.png?alt=media&#x26;token=f063cfaa-3a03-4285-9a2d-a98c7afd39a8" alt=""><figcaption></figcaption></figure>

### **Main View of Insights Data**

The view defaults to today's date. For each day a user will see in the main section:

* **The 'How are you feeling' value to the day** - this can also be set here, but once set is read-only and comment shows as a mouse-over tool-tip.
* **Data they manually entered on the Insights popup** - or indeed on this same main Insights Screen.
* **Time auto-tracked by Enate** - This is Time which Enate has tracked being spent on the Ticket, Case, Action screen or on an Enate email on this day (includes manual adjustments).
* **The overall total hours -** This is the total combined number of hours input by the agent.

These values are grouped into two section showing:

* **'Operational value added hours'** - spent actively performing work for service delivery
* **'Business value added hours'** - spent on supporting activity which indirectly contributes to service delivery

#### Modifying / Adding Insights values

**Modifying Values**

The Insights values (number of hours and minutes) can be modified by users for each day selected.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fx9HwT0B3Fhivnfj2EXS2%2Fimage.png?alt=media&#x26;token=45abd1a3-9a72-497c-863f-f56a42e37dff" alt=""><figcaption></figcaption></figure>

Users can change all these values manually except for the 'Time auto-tracked by Enate' value, which comes from the Time Tracker control on all work items the users worked on that day (and any work item-related emails they worked on in the Email view). Note that the time tracker data will take manually applied overrides set on work items in preferences to auto-tracked time, wherever they have been entered.&#x20;

**Click Submit to save any adjustments.**

**Adding missing data**

For days marked as still missing any confirmed data, a message will show at the top of the table. All missing data should be added, including confirming of the Working Hours for that day (a suggested value will often be displayed).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fh1qBqJTigMyRE6gPbLsf%2Fimage.png?alt=media&#x26;token=422ae6be-b0a4-4564-adbb-cc04bd5f6031" alt=""><figcaption></figcaption></figure>

**Click Submit to save any adjustments.**

### Insights Data Displayed

The following data is displayed on the main section, corresponding with the data options shown on the Insights Popup.&#x20;

* **Working Hours -** Standard amount of working hours for this day.
* **Breaks -** Time spent on breaks, e.g. lunch, throughout this day.
* **Downtime -** Time lost due to, e.g. system issues, or non-availability of work.
* **Time auto-tracked by Enate** - Time which Enate has tracked being spent on the Ticket, Case, Action screen or on an Enate email on this day, (includes manual adjustments).
* **Active time not tracked by Enate** - (only available for historic dates). Time spent actively working to provide service but where a Ticket, Case or Action screen, or Enate email, is NOT open in Enate to auto-track this time.

{% hint style="info" %}
Examples might be: time spent on the Enate homepage or working in another system while an Enate work item tab is NOT open and so not auto-tracking time. *This should NOT include activities such as meetings or training, which should be noted separately.*
{% endhint %}

* **Meetings** - time spent in any collaborative gathering or group meeting.
* **Feedback / 1-2-1** - time spent in individual sessions with e.g. team leader, manager, mentor.
* **Training** - time in organised training or knowledge-transfer sessions.
* **Other** - time spent on any other activities which are not listed above, or any additional breaks taken in a day.

### Calendar view

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXNBLVA7MOHkIoAD9VQHt%2Fimage.png?alt=media&#x26;token=02a8fb48-df8d-43a5-9663-a1b5b61ba0a9" alt=""><figcaption></figcaption></figure>

Users can use the calendar control to flip between dates, updating the Insights data displayed in the main section to show data for that date. They also have the following options:

* View and mark dates as 'On Leave', i.e. vacation days (shown in <mark style="color:yellow;">**yellow**</mark>).
* View and mark dates as a 'non-working day' for that user, e.g. a weekend day or equivalent (shown in <mark style="color:purple;">**purple**</mark>).
* View dates where their Insights data is currently incomplete (date shown in <mark style="color:red;">**RED**</mark>). **Use this control to help identify which dates you need to fill in gaps in Insights data.**

*Dates where they can no longer adjust data are shown grayed out.*

#### How far back can I Add / Edit my Insights Data?

Team members can add or Edit Insights data (including setting dates as 'On Leave' or 'Non-Working Day' for up to **7 days in the past**). If you need your data to be adjusted for dates beyond that, speak with your Team Leader who can make necessary adjustment for up to 31 days.

### Entering data in advance

{% hint style="info" %}
Remember that users can enter future Insights data, particularly planned leave and non-working days can be entered in advance if missing, the help Team Leaders withe future capacity planning.
{% endhint %}


# Main Insights Page: Team Leader Features

## Insights Page For Team Leaders

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTcyNjc3MA==>" %}

Team Leaders\* have all the same features that Team Members have on the Insights page, PLUS additional features available to them, with a Team section, and an additional tab in the Calendar section.\
\&#xNAN;*\*(Specifically: users with the 'Set up Team & Queues' feature access option enabled )*

### Finding & Fixing missing Insight data - Summary 'Cheat Sheet' <a href="#finding-and-fixing-missing-insight-data-summary-cheat-sheet" id="finding-and-fixing-missing-insight-data-summary-cheat-sheet"></a>

To identify missing Insights data quickly, Team Leaders can:

* Look at the **Teams section first**, click on a user with a red circle (showing they have missing data on that date). Fix their data, then look at the Calendar to see any other 'red' highlighted days where data is missing for that user, and go through each until data is complete.&#x20;

**OR**

* Select the **Team Calendar first**, select a date highlighted in red (showing that at least one team member has missing data). Then select the users from the Team section circled in red and work to fix their data. Cycle through each red date until all missing user data is complete.

### Team section <a href="#team-section" id="team-section"></a>

Team Leaders can see their team members in the Teams section.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fq9n0EZWfrTL2K19mimYe%2Fimage.png?alt=media&#x26;token=72f6509d-20a4-4863-b584-d9e7695c4baf" alt=""><figcaption></figcaption></figure>

Clicking on any team member will show their calendar and the Insights Data in the main section for the selected date. They can flip between dates, viewing and if necessary adjusting the Insights data. They also have the following options to adjust that user's data, in the user's calendar displayed:

* View and mark dates as 'On Leave', i.e. vacation days (shown in <mark style="color:yellow;">**yellow**</mark>).
* View and mark dates as a 'non-working day' for that user, e.g. a weekend day or equivalent (shown in <mark style="color:purple;">**purple**</mark>).
* View dates where their Insights data is currently incomplete for the selected user (date shown in <mark style="color:red;">**RED**</mark>).

*Dates where they can no longer adjust data are shown greyed out.*

Finding missing data: Team Leader should use this view to click on a user with a red circle (showing they have missing data on that date). Fix their data, then look at the Calendar to see any other 'red' highlighted days where data is missing for that user, and go through each until data is complete.

### Team Leader Calendar options

Team Leaders have are able to see each of the team member's detailed calendar when they click on them. They also have a Team Calendar tab. This will display in red any day where at least one team member has incomplete Insights data.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FznzJzNzWA6jL6Se7IYW8%2Fimage.png?alt=media&#x26;token=30603ef3-c79b-4ec8-b8ff-e4ef223aba9f" alt=""><figcaption></figcaption></figure>

Finding missing data: Team Leader should use this Team Calendar to identify each date highlighted in red, the select the users from the Team section who are circled in red, and work to fix their data. Cycle through each red date until all missing user data is complete.

### How far back can Team Leaders Add / Edit Insights Data?

* Team Leader can add or Edit Insights data (including setting dates as 'On Leave' or 'Non-Working Day') for up to **31 days in the past**, including their own data.


# The User Insights Report

Report detailing User Availability Insights data of how their work time is being spent.

### User Insights Report <a href="#user-insights-report" id="user-insights-report"></a>

As part of the Insights feature, a standard report is available that summarizes you or your team's availability data. It shows:

* Planned leave data
* Non-working days
* Trend of duration of activities
* Overall sentiment
* Sentiment trend

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtJZmEB1yEvgdwNTOZ7On%2Fimage.png?alt=media&#x26;token=fd3f70cc-9ab5-4e98-aaa5-b2ebb435b179" alt=""><figcaption></figcaption></figure>

More information about these visuals can be seen in the table below:

| Report Visual                | Description                                                                                                                                                                                                          | Logic                                                                                                                                                                                                                                                                                                                                                                                                                                        | Filters Applicable |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Leaves                       | Shows the Daily/Weekly/Monthly trend of planned leave count by the user. If the logged in user is a team manager then it will also show leave count for their team members.                                          | 1. Count all rows where Work Day Type = "Leave" 2. Filter the rows for the "logged in user" and any user whose manager is "logged in user"                                                                                                                                                                                                                                                                                                   | Date, User name    |
| Non-working days             | Shows the Daily/Weekly/Monthly trend of non working days count for the user. If the logged in user is a team manager then it will also show non working days count for their team members.                           | 1. Count all rows where Work Day Type = "WeekOff" 2. Filter the rows for the "logged in user" and any user whose manager is "logged in user"                                                                                                                                                                                                                                                                                                 | Date, User name    |
| Avg. duration trend (in hrs) | Shows the average Daily/Weekly/Monthly trend of various durations entered by the user. If the logged in user is a team manager then it will also show average durations for their team members.                      | 1. Calculate the average of DurationSpentInEnate, AdHocDuration, DowntimeDuration, FeedbackDuration, MeetingDuration, DurationSpentOutsideEnate, TrainingDuration by excluding any WeekOff and leaves 2. DurationSpentInEnate is calculated as total duration recorded in packet activities by each user on each day where activity type in (2,3) 3. Filter the rows for the "logged in user" and any user whose manager is "logged in user" | Date, User name    |
| Overall sentiment            | Shows the overall percentage share of each sentiment opted by the user. If the logged in user is a team manager then it will also show the percentage share of sentiments for their team members.                    | 1. Calculate the count of sentiments for each sentiment type 2. Filter the rows for the "logged in user" and any user whose manager is "logged in user"                                                                                                                                                                                                                                                                                      | Date, User name    |
| Sentiment trend              | Shows the Daily/Weekly/Monthly trend of percentage share of sentiment entered by the user. If the logged in user is a team manager then it will also show the percentage share of sentiments for their team members. | 1. Calculate the count of sentiments for each sentiment type 2. Filter the rows for the "logged in user" and any user whose manager is "logged in user"                                                                                                                                                                                                                                                                                      | Date, User name    |

#### Available Datasets

The Team View Report contains the following available data sets:

| Table          | Fields                            | Description                                                                                          |
| -------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Date           | Date                              | Day of the week in DDMM Format                                                                       |
| Date           | Week                              | Week of the year                                                                                     |
| Date           | Month                             | Month of the Year in MMYY format                                                                     |
| Date           | Year                              | Calendar Year                                                                                        |
| Sentiment type | Sentiment                         | Sentiments options (Excellent, Very Good, Good, Bad, Worse). It will be none if not entered.         |
| Insights       | Avg. other hours                  | Avg. hours spent on ad hoc tasks                                                                     |
| Insights       | Avg. contractual break hours      | Avg. hours spent on breaks                                                                           |
| Insights       | Avg. idle hours                   | Avg. hours spent on system downtime                                                                  |
| Insights       | Avg. feedback/1-2-1 hours         | Avg. hours spent on feedback sessions                                                                |
| Insights       | Avg. work performed within Enate  | Avg. hours spent in Enate (on cases, actions or tickets)                                             |
| Insights       | Avg. work performed outside Enate | Avg. value added hours spent outside the Enate                                                       |
| Insights       | Avg. meeting hours                | Avg. hours spent on meetings                                                                         |
| Insights       | Avg. training hours               | Avg. hours spent on training sessions                                                                |
| Insights       | Avg. working hours                | Avg. working hours                                                                                   |
| Insights       | Other hours                       | Total hours spent on adhoc tasks                                                                     |
| Insights       | Contractual break hours           | Total hours spent on breaks                                                                          |
| Insights       | Downtime hours                    | Total hours spent on system downtime                                                                 |
| Insights       | Feedback/1-2-1 hours              | Total hours spent on feedback sessions                                                               |
| Insights       | Work performed within Enate       | Total hours spent in Enate (specifically on Cases, Actions or Tickets)                               |
| Insights       | Work performed outside Enate      | Total value-added hours spent outside the Enate                                                      |
| Insights       | Leaves count                      | Planned leave count for the user(s)                                                                  |
| Insights       | Meeting hours                     | Total hours spent on meetings                                                                        |
| Insights       | Non-working days count            | Non-working day count for the user(s) includes holidays weekends etc                                 |
| Insights       | Sentiment count                   | Count of sentiments entered by user(s) for a particular day                                          |
| Insights       | Training hours                    | Total hours spent on training sessions                                                               |
| Insights       | Working hours                     | Total working hours                                                                                  |
| Insights       | Comment                           | Comments added by user for the sentiment chosen                                                      |
| Insights       | Insights date                     | Date when the durations/sentiments captured from the user                                            |
| Users          | Email address                     | Email address of the user(s)                                                                         |
| Users          | User name                         | Full name of the user(s)                                                                             |
| WorkDay type   | Work day                          | Type of the day (Working, Non-working Day, Leave). It will be none if nothing is chosen by the user. |


# Advanced Search

The advanced search feature gives you a flexible way to view the work items in your business area by allowing you to specify multiple different combinations of search criteria, letting you view your work item data precisely how you want to.

You can access the ‘Advanced Search’ tab from the Nav section. When you hover over the 'Advanced Search' option here, you'll also see a list of your [Saved Views](#d-saving-your-views) (if you have any), sorted in alphabetical order. You can easily created Saved Views from the Advanced Search feature so you don't have to enter your search criteria each time.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQwNzYzOA==>" %}

{% hint style="info" %}
Note: Access to this Export feature is not switched on for standard Team Member and Team Leader Roles. To give users access to this feature, a [Custom Role](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-roles-and-feature-access) must be created via the User Management section of Builder, with the 'Can Export Advanced Search views to Excel' option switched on in the 'Advanced Search' feature access section.
{% endhint %}

## Searching

To use the Advanced Search feature, enter your search criteria by setting its Field, Condition (e.g. Equals, Greater Than etc.), and Value against which to evaluate the Condition.

The table below gives more detailed information about the standard fields available in the system.&#x20;

<table><thead><tr><th width="189">Field Name</th><th>Description of Field</th><th width="175">Type of condition that can be used</th><th>Value</th></tr></thead><tbody><tr><td>Action Type</td><td>This lets you search for Actions of a particular type. </td><td><p>Begins With</p><p>Equals</p></td><td>Select from: Manual, Manual with Peer Review, Send Email, Send Email and Wait, Start Case, ABBYY OCR, Wait for Sub Cases to Complete, and Trigger External API.</td></tr><tr><td>Assigned To</td><td>This lets you search for work items based on who they are assigned to or whether or not they have been assigned to someone.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Context</td><td>This lets you search for work items with a specific context i.e. customer, contract, service</td><td>Equals</td><td>Select a customer, contract and service from the dropdown</td></tr><tr><td>Due</td><td>This lets you search for work items based on when they are due. </td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>End Date</td><td>This lets you search work items based on when they have been completed i.e. they have been marked as Closed.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>Has Been Reopened</td><td>This lets you search for work items that have been reopened from a Resolved state.</td><td>Equals</td><td>Select from Yes or No</td></tr><tr><td>Initial Request On</td><td>If a further work item has been created from an original request (when a Sub Case is created, when a Ticket is converted into a Case, when a Case or Action gets reworked, when an Action is created via the 'Start Action' option or when a new linked work item is created), this due date method captures the start date of the original request, allowing you to capture the entire length of time it has taken to complete a request, as opposed to just the length of time an individual work item has been being worked on.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>Is Overdue</td><td>This lets you search for work items that are overdue.</td><td>Equals</td><td>Select from Yes or No</td></tr><tr><td>Last Reopened By</td><td>This lets you search for who last reopened a work item from a Resolved state. </td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Last Reopened On</td><td>This lets you search for the last time when a work item was reopened from a Resolved state.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td><p></p><p>Last Updated By</p></td><td>This lets you search for work items based on the human/digital worker who last updated the work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Last Updated On</td><td>This lets you search for work items based on the datetime the item was last updated by a human/digital worker.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>Original Requester Email</td><td>This lets you search for work items based on the email address of the original requester of a work item, i.e. the person who initially raised the request.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Original Requester Name</td><td>This lets you search for work items based on the name of the original requester of a work item, i.e. the person who initially raised the request.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Owned By</td><td>This lets you search for work items based on the owner of the item i.e. the person who currently has ultimate responsibility for the work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Overdue By Days</td><td>This shows how many days or working days (depending upon the due date configuration) a work item is overdue by.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Enter the desired number of days.</td></tr><tr><td>Parent Process Name</td><td>This lets you search for work items based on their parent process e.g. searching for the name of a Case will return the Actions of the Case in your search.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a parent process</td></tr><tr><td>Parent Reference</td><td>The reference number of the work item which started this one, e.g. parent Case<strong>.</strong></td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a reference number</td></tr><tr><td>Primary Contact Email</td><td>This lets you search for work items based on the email address of the primary contact of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Primary Contact Name</td><td>This lets you search for work items based on the name of the primary contact of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td><p>Queue</p><p></p></td><td>The work Queue which Cases/Tickets/Actions get sent to based on their routing rule.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a Queue</td></tr><tr><td>Reference</td><td>The unique reference number e.g. 101342-T.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a reference number</td></tr><tr><td>Requester Email</td><td>This lets you search for work items based on the email address of the requester of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Requester Name</td><td>This lets you search for work items based on the name of the requester of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Running</td><td>This lets you search for work items based on their status. Running work items are work items in a state or To Do, In Progress, Waiting</td><td>Equals</td><td><p>Select Yes if you want to search for work items that are in a state of To Do, In Progress or Waiting.</p><p>Select No if you want to search for work items that are not in a state of To Do, In Progress or Waiting.</p></td></tr><tr><td>Schedule</td><td>This lets you search for Cases based on their <a href="https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule">schedule</a></td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, select a schedule from the dropdown</td></tr><tr><td>Schedule Period</td><td>This lets you search for Cases based on their <a href="https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule">schedule period</a>. </td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a schedule period</td></tr><tr><td>Schedule Structure</td><td>This lets you search for Cases based on their <a href="https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule-structure">schedule structure</a>. </td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, select a schedule structure from the dropdown</td></tr><tr><td>Schedule Year</td><td>This lets you search for Cases based on their <a href="https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule">schedule year</a>. </td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td><p>If the condition you have selected is Equals, Not Equal, Greater Than, </p><p>Greater Than Or Equals To, Less Than or Less Than Or Equals To then enter a year. </p><p></p><p>If the condition you have selected is Between, enter the two different years that you want to search between.</p></td></tr><tr><td>Service Line</td><td>This lets you search for work items based on the overall area of the business the work item runs under, e.g. ‘Payroll’.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>Select a service line from the dropdown</td></tr><tr><td>Service Provider</td><td>This lets you search for work items based on the company delivering service for the work item, usually <em>your</em> company.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>Select a service provider from the dropdown</td></tr><tr><td>Started</td><td>This lets you search for work items based on when the when the work item was started.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal </p><p>Greater Than</p><p>Greater Than Or Equals To</p><p>Less Than </p><p>Less Than Or Equals To </p><p>Between</p></td><td>Select a date</td></tr><tr><td>Started By</td><td>This lets you search for work items based on who started the work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a worker</td></tr><tr><td>Started By Method</td><td>This lets you search for work items based on how they got started, e.g. incoming email, automatic schedule, manually.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, select from: Workflow, Manual, Self Service, Robotics, Email, Ticket, Bulk Upload, Schedule, Linked Work Item</td></tr><tr><td>Status</td><td>This lets you search for work items based on their current status.</td><td><p>Equals </p><p>Not Equal</p></td><td><p>Draft</p><p>To Do</p><p>In Progress</p><p>Waiting</p><p>Resolved</p><p>Closed</p></td></tr><tr><td>Status Reason</td><td>This lets you search for work items based on their current status reason.</td><td><p>Equals </p><p>Not Equal</p></td><td><p>Action Unable to Complete</p><p>All relevant Actions completed</p><p>All Split Tickets Completed</p><p>Blocked By Business Rule</p><p>Cancelled</p><p>Completed</p><p>Failed</p><p>Feedback Received</p><p>Feedback Window Passed</p><p>File not found during IDP extraction</p><p>Marketplace not configured</p><p>New Information Received</p><p>Newly Created</p><p>One or more Actions not completed successfully</p><p>Previous Step Completed</p><p>Reopened By Resource</p><p>Rework</p><p>Schedule Date and Time Reached</p><p>Sub Case Completed</p><p>Sub Case Cancelled</p><p>Sub Case Not Yet Started</p><p>Timeout</p><p>Unknown</p><p>Updated by Enate</p><p>Updated by Enate (as End Case Action reached)</p><p>Updated By Integration</p><p>Updated By Resource</p><p>Updated By Support Team</p><p>Waiting for Human Validation</p><p>Waiting for Marketplace</p></td></tr><tr><td>Subject Email</td><td>This lets you search for work items based on the email address of the subject of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Subject Name</td><td>This lets you search for work items based on the name of the subject of a work item.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter the name of a contact</td></tr><tr><td>Ticket Category Level 1</td><td>This lets you search for Tickets based on their Ticket category level 1 i.e. the highest level of Ticket categorisation e.g. ‘Healthcare Request’.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a Ticket Category Level 1 value</td></tr><tr><td>Ticket Category Level 2</td><td>This lets you search for Tickets based on their Ticket category level 2 i.e. the next level of Ticket categorisation e.g. ‘International Travel Coverage’.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a Ticket Category Level 2 value</td></tr><tr><td>Ticket Category Level 3</td><td>This lets you search for Tickets based on their Ticket category level 3 i.e. the most detailed-level of Ticket categorisation e.g. ‘Eligibility Query’.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a Ticket Category Level 3 value</td></tr><tr><td>Title</td><td>This lets you search for work items based on their title - a brief text description of the work item, often the subject of the original email.</td><td><p>Begins With</p><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p></td><td>If the condition you have selected is Begins With or Equals, enter a title of the work item</td></tr><tr><td>Wait Type</td><td>This lets you search for work items based on their wait type i.e. if they have a wait type of 'Waiting for more information', etc.</td><td><p>Equals</p><p>Is Empty</p><p>Is Not Empty</p><p>Not Equal</p></td><td><p>External System</p><p>Pause</p><p>Related Work Items</p><p>Wait for more information</p><p>Wait Until</p></td></tr><tr><td>Work Item Type</td><td>This lets you search for work items based on their work item type i.e. if they're a Ticket, Case or Action.</td><td>Equals</td><td>Select Case, Ticket or Action</td></tr></tbody></table>

You can also select Fields based on any [custom data fields that have been configured in your system](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/creating-custom-data-fields), excluding custom data tables.

You can add as many additional sets of conditions as you wish by clicking on the green plus icon.

Once you have entered your search conditions, click Search to reveal your search results. Your total number of search results will be shown at the top of the grid.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYtIGa1fzfRh5j7mWcw%2F-MYtv2hLoeSBnTaMcjeo%2FExample-View-Search.gif?alt=media\&token=57e6a52d-885d-4ab6-a504-2a8968120d51)

## Choosing which data to see in Search Results <a href="#b-choosing-which-data-columns-to-see-in-search-results" id="b-choosing-which-data-columns-to-see-in-search-results"></a>

As with your Work Inbox and Owned work grids, you can choose which data columns you wish to see or hide in your search results grid by clicking on the Cog icon above the Search Results grid.

A ‘Display and Columns Settings’ popup will appear, allowing you to select which data columns you would like your search results to display.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYtz7NIF5ed0SdI8MIe%2F-MYu-kenHwpZZG5g3Dsh%2FOrder-Views-Data-Columns.gif?alt=media\&token=05996cb2-015b-4df9-b8a7-611bf66e686b)

{% hint style="info" %}
Note: These custom data column preferences will stay the same when you do multiple searches, and when you next log back in.
{% endhint %}

## Grouping and Ordering <a href="#c-grouping-and-ordering" id="c-grouping-and-ordering"></a>

You are also able to Group and Order your search results by selecting your Group By and Order By preferences from their respective dropdown lists.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYtz7NIF5ed0SdI8MIe%2F-MYuRfsx8PRyTd41m_Xv%2FGrouping-Views-Searches.gif?alt=media\&token=4155693a-8007-47d7-bafa-585ea9cf8a0e)

{% hint style="info" %}
Note: Only a single grouping criteria can be specified, and results will be loaded when you click on and expand an individual group.
{% endhint %}

## Saving Your Advanced Searches <a href="#d-saving-your-views" id="d-saving-your-views"></a>

You can also save your Advanced Searches as views which allows you to call them up again whenever you want. There is no limit to the number of views that you can save.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fr7fAR2GPKOylTDyXrdA4%2FSaved-Views.gif?alt=media&#x26;token=0ae3d4d0-0e11-402f-b60d-8f777c320502" alt=""><figcaption></figcaption></figure>

You can access your Saved Views by clicking on the Saved Views link.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8YLpozrh6IEX97caDNGD%2Fimage.png?alt=media\&token=40324e8f-4f35-409b-b620-9eb03c242abe)

Here you can search for a specific Saved View and rename and delete your Saved Views.

You can copy the name of your Saved View by clicking on the copy button on the tab:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fh0nOnpI9DoeMhLhc9ZSN%2Fimage.png?alt=media\&token=338e56d8-d88c-4c1c-b485-42878c9112c8)

## Exporting Advanced Search Views into Excel

You can export your views data from your Advances Searches into Excel. Watch this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQwNzYzOQ==>" %}

To export your views data into an Excel spreadsheet, enter your search criteria in the Advanced Search page and then click to 'Switch to Export'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSRBBn5B9LITmtAR2GHwA%2Fimage.png?alt=media&#x26;token=1067adfb-4b51-496b-9d2d-f30f2132d7fd" alt=""><figcaption></figcaption></figure>

This will show you a list of all of your previously exported files, as well as when they were downloaded, the size of the file, the total number of rows in the file, when the file export was requested, when the export began and when it was completed.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F530WLNQs3Um548Jd3Ro1%2Fimage.png?alt=media&#x26;token=79ea2d5b-ae95-44a6-808e-b83bc0c7361d" alt=""><figcaption></figcaption></figure>

Before you export your search, you can edit the name of the file it will be exported as.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQgFvclpsc0PYsC98o8gt%2Fimage.png?alt=media&#x26;token=1cff9746-47e0-4040-a1aa-4438a8a0e95c" alt=""><figcaption></figcaption></figure>

You can also adjust which columns you would like to view in your excel export by clicking on 'Select columns'. The columns selected in your search will be automatically selected, but you can adjust your selection here too.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKRTEZDlJlq1iN84eY7QM%2Fimage.png?alt=media&#x26;token=6aaf1620-06c7-4b24-9492-188d47144f8b" alt=""><figcaption></figcaption></figure>

Then click to 'Export'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fw5dMVGkg1OfFXxJyF8Sw%2Fimage.png?alt=media&#x26;token=1a1a3a26-4b3d-474d-ba71-0b2dff0ecad2" alt=""><figcaption></figcaption></figure>

Your file will appear as a new row in the Exported Files section with a 'queued' icon next to it. Click to refresh the grid.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FsiBdI1ORI0vQnSB6XgBG%2Fimage.png?alt=media&#x26;token=ad3962be-10b0-482b-ab3b-ef5c1a40675f" alt=""><figcaption></figcaption></figure>

Once refreshed, the icon will change to a green single tick to show that the export is complete.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfGBza8YOgfKc2WjpmZsU%2Fimage.png?alt=media&#x26;token=28c331c1-0421-453a-bf1a-6385e35ecd03" alt=""><figcaption></figcaption></figure>

If there has been an error in exporting the file, a red warning icon will appear next to it.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6ywCwvG0Whd1vmwR6YGV%2Fimage.png?alt=media&#x26;token=e5dc0f48-3825-489b-accf-f2bdcb1c8e32" alt=""><figcaption></figcaption></figure>

You can download the file by clicking on the file name.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpykMJd6up8FgKV5WxH9l%2Fimage.png?alt=media&#x26;token=4ea3ab3b-d51f-41b6-8a8d-349ba790f100" alt=""><figcaption></figcaption></figure>

Once it has been downloaded, the icon will change to a green double tick to show that it has been downloaded.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDfFQRe3sTydmifx9gr3d%2Fimage.png?alt=media&#x26;token=42b0bda2-34e8-4dad-9239-f1767554fd6f" alt=""><figcaption></figcaption></figure>

The time and date that it was downloaded will then appear in the 'Downloaded On' column.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBb7ernbWDEyt7URjoReX%2Fimage.png?alt=media&#x26;token=1478be1c-28de-4e43-b3a4-0461cca0b1ec" alt=""><figcaption></figcaption></figure>

The data from your Advanced Search will have been exported into a .xlsx file, including the column titles selected.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdeM8tLrMWpNsM8gv4Dlx%2Fimage.png?alt=media&#x26;token=24a2c623-796f-454e-9c33-249c80dd29fb" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Please note that in this initial release, column titles will only appear in English. They will be localized in a future release.

Additionally, please note that you can export up to a maximum of one million rows.

Column names in the exported file are different to the names that are displayed in the UI in the Advanced Search page.
{% endhint %}

## Copy/Paste into Excel <a href="#e-copy-paste-into-excel" id="e-copy-paste-into-excel"></a>

You can copy and paste information from the Advanced Search grid into an Excel spreadsheet by selecting the information you want to copy and using Ctrl C and Ctrl V. The information that is copied and pasted includes any applied filters. The column titles will automatically be copied and pasted as well.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYuS6h2QRhLllsba5Dk%2F-MYuTgl-EXI_C_I4eJLQ%2FCopy-Views-to-Excel.gif?alt=media\&token=e89b9890-c260-48f0-867c-6ab7bd5293c4)

You are also able to to copy and paste all of the information from the Views grid by using Ctrl-A.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYuS6h2QRhLllsba5Dk%2F-MYuUled-D4l_4a1Z5V4%2FCtrl-A-Into-Excel-from-Views.gif?alt=media\&token=a1c81a29-3b81-4b31-aa1d-903abe8ba7a0)

{% hint style="info" %}
Note: only information that has loaded in the Advanced Search grid will be copied across.
{% endhint %}


# User Settings

Clicking on the user dropdown will show the following dropdown:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYzQmkKW2pv6XWGPf7q%2F-MYzSybJ0DuPNpBtR01l%2FUser-Dropdown.gif?alt=media\&token=7dc2e0fc-4a48-46ef-b344-67e1aabca9ca)

## User Info <a href="#a-user-profile" id="a-user-profile"></a>

Clicking on your name or picture will bring up User Settings. Here you can select your preferred language, add a profile picture, change your password and select the date and time.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZCX5sRzULdwwap_qSX%2F-MZCYxEqO7XSmdqDy7oY%2FClick-on-User-Settings.gif?alt=media\&token=1de23615-4868-4c1a-b12c-1241b67b243a)

### **Language**

Enate currently supports the following languages:

* British English
* US English
* Spanish
* Portuguese (Brazilian)
* Romanian
* Hungarian
* Polish
* Russian
* French
* German

If you choose a non-English language, the UI and labels will be changed to the selected language. If your system admin has configured translation for Case/Ticket/Action in these languages, then all Case/Ticket/Action information will also appear in given language, see [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/adding-localisations)for more information.

### **Profile Picture** <a href="#profile-picture" id="profile-picture"></a>

Clicking ‘Edit Profile Picture’ will bring up picture control to pick up new image from your machine. Clicking the edit button will allow you to navigate to select picture. You can also delete the existing picture via the delete button.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWqVjt5Za-7iH_NtTb-%2F-MWqWhiUhTdshI8k3V4I%2Fimage.png?alt=media\&token=267c93f5-4389-4b87-8f2c-60c94a86024a)

### **Personalised Email Signature** <a href="#personalised-email-signature" id="personalised-email-signature"></a>

Enate’s Email Signature feature allows you to configure your own signature for outgoing emails. You can use the Email Signature section to define the signature content to be sent in outgoing emails which you write.

{% hint style="info" %}
Note: The configured email signature will only be included with the outgoing emails if the ‘**Include my signature in the outgoing emails’** checkbox at the foot of this section is checked.
{% endhint %}

After you have created a signature, clicking on any of the links to bring up the ‘compose new email’ section in any work item will display the configured email signature at the bottom of the email body.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYzQmkKW2pv6XWGPf7q%2F-MYzWrCH41AY__7Gq2S6%2FEmail-Signature%20\(1\).gif?alt=media\&token=1d648cb4-1093-4dcb-8802-33b5e61074c5)

### **Change your password** <a href="#change-your-password" id="change-your-password"></a>

If you wish to reset your password, enter your old and desired new password here, and then click the Save button. After a successful password reset, you will be redirected to the login page to log back in with your new password.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fe3THILZZsyiLAHYI27ME%2Fimage.png?alt=media&#x26;token=b8e1b736-65bf-4d05-8577-a85d955dc4dc" alt=""><figcaption></figcaption></figure>

### Other System Personalisation Options

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCKoT6E1L5OLmjVs1oTZC%2Fimage.png?alt=media&#x26;token=05b19386-4dc0-456c-a067-e71436864a41" alt=""><figcaption></figcaption></figure>

* The 'Include my signature in outgoing emails' option lets you choose whether or not to include your personalised signature in the emails you send.
* 'Don't show create contact popup' lets you choose whether you want to get a Create Contact popup every time you communicate with a contact that isn't already in the system.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmBlScjaAjXaqAa03NzK9%2Fimage.png?alt=media\&token=eec9a324-b562-4ffd-b21c-c6efb4ac69ce)

* The 'Don't show new information warning' option lets you choose whether or not you wish to be notified every time you update a work item and you have not clicked on the new information icon to see the latest changes to the work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkYTFx3vGTcVGfBn3LbrU%2Fimage.png?alt=media\&token=37eefb92-6950-47c0-9e27-088c5b68b831)

* 'Don't show Global agent warning' lets you choose whether or not you want to be notified every time you add a global agent (i.e. an agent who is not linked to a specific company) to a work item.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUH7MU3jWuxhI8KNTxP4g%2Fimage.png?alt=media\&token=5a9b8c38-83d2-4429-9150-774491df1cdd)

* IF [Plus Addressing](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/broken-reference) is enabled in your system to help with matching of emails to work items, then the 'Don't show Check Details warning' option lets you choose whether or not you want to be warned every time you are sending an email to more than one address that is already connected to an Enate mailbox and you have not clicked to view the details for each work item that is being created/linked via that email address.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMJB0K08Qu0P8nIBrDbc5%2Fimage.png?alt=media&#x26;token=ee040c24-9164-4723-a8ae-f648838e94c3" alt=""><figcaption></figcaption></figure>

* IF [Plus Addressing](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/broken-reference) is enabled in your system to help with matching of emails to work items, then the 'Don't show 'Remove Route Address' warning' option lets you choose whether or not you want to be warned every time you decide to remove an email address when sending an email to more than one address that is already connected to an Enate mailbox.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F9QimqOLT9u0DvalWMDjz%2Fimage.png?alt=media&#x26;token=5fb7e03d-d1a6-41ba-9558-de9e37736719" alt=""><figcaption></figcaption></figure>

* The 'Open links in new browser tab' option lets you decide how you would like the links you click on in Enate Work Manager to open - either in a new, dedicated browser tab or in your current browser tab. By default, this option is set to OFF, meaning that when you click on a link the new content displays in your current browser tab. If you'd prefer that the links you click on open in new, different browser tabs, switch this option to ON and save your change. Now when you click on links, you'll see that a new dedicated browser tab will open up to show that content.&#x20;

### Logging Out <a href="#c-logging-out" id="c-logging-out"></a>

Clicking on the Logout link will end your Enate session and take you back to the login screen.

### Forgotten Password <a href="#d-forgotten-password" id="d-forgotten-password"></a>

If you’ve forgotten your password you can reset this from the logon page by clicking on the ‘Forgot password’ link:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3aYageZT6iYBtmDBJA5h%2Fimage.png?alt=media&#x26;token=6502fa35-352f-4f49-a380-2601e9333c99" alt=""><figcaption></figcaption></figure>

Enter your username in the resulting screen.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUdkBsU3bSJmnPYdI4DyR%2Fimage.png?alt=media&#x26;token=8e7e3801-7215-4171-940a-7378ff09ad68" alt=""><figcaption></figcaption></figure>

If your username is associated with an email address then you will receive an email with a link to reset your password.

Whenever your password is reset via this method, you will receive an email confirming this.

## Undo Send

The Undo Send setting lets you add a time delay to when your emails will be sent, giving you the opportunity to cancel sending an email, or reviewing an email before it gets sent, [click here fore more information](https://docs.enate.net/enate-help/work-manager/emails/scheduling-of-emails-and-the-outbox-page#undo-send-option).

You can set an Undo Send time by moving the slider along to the desired setting.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOfOequNs6XiHewbiDsMs%2Fimage.png?alt=media&#x26;token=35c09fbf-d513-4cf4-b507-4d87555cbf42" alt=""><figcaption></figcaption></figure>

## Notification Settings

Enate's Notifications keep you up to date on what's happening with any Tickets, Actions and Cases you're interested in to keep you in the loop at all times. You've got lots of flexibility with how you receive notifications, in terms of which items you follow, what events you're notified about for them and how they're delivered to you.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTY5Mg==>" %}

This is where you can choose which notifications you want to receive and how.&#x20;

In addition to choosing to follow an individual work item, you can also use the notifications settings page to specify more generally which notifications you want to automatically receive. There are two parts to this:

* First, you specify which work items you want to receive, e.g. item's in your own Work Inbox.
* Further to this, you specify which *events* about those work items you want to be notified about.

See below for details ..&#x20;

### Which Items to notify me about - Scope

You can choose to receive notifications for work items in you [Work Inbox ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/home-page)and/or for work items in your [Queues](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/setting-teams-and-queues).&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F53ZIz7kiDGGowsYDQnKm%2Fimage.png?alt=media&#x26;token=e64c40d5-c8b3-43cf-bf40-d82d42ae2494" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="247.37282229965155">Work Item Type</th><th>Detail</th><th>Notes</th></tr></thead><tbody><tr><td>My Work Inbox</td><td>You will receive notifications for work items that are in your Work Inbox i.e. work items that are assigned to you. </td><td>This is switched on by default for all users.</td></tr><tr><td>My Queues</td><td>You will receive notifications for work items that are in Queues that you are in and/or manage. </td><td>This option is switched on by default for Team Leaders.</td></tr></tbody></table>

### Which Events to notify me about

In addition to this, you need to choose which events you want to be notified about for these Work Items.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXjl568nHlJ4XG65oHftl%2Fimage.png?alt=media&#x26;token=7f568c37-451a-4f9e-957e-306fcf179ece" alt=""><figcaption></figcaption></figure>

The options are as follows:

<table><thead><tr><th>Type of Notification</th><th width="241.33333333333331">Detail</th><th>Notes</th></tr></thead><tbody><tr><td>New Information Received </td><td>New information (Email/Notes/Self Service Note) has been received on the work item</td><td>Users subscribed to receive notifications for a work item related to this (e.g. Case/Actions or the child/parent of a split Ticket) will also receive the notification.</td></tr><tr><td>Work Item Assigned to Me</td><td>Assigned user of a work item has changed to me</td><td></td></tr><tr><td>New Work Item into Queue</td><td>Assigned Queue of a work item has changed to a Queue that I am in and/or manage</td><td></td></tr><tr><td>New File/Link Added</td><td>New file/link has been added to the work item</td><td></td></tr><tr><td>Due Date 'At Risk' Reminder</td><td>Due date of the work item is deemed to be at risk. This is calculated by subtracting the expected time for the work item to take with an additional 30 minutes from the due date/time. </td><td><p>E.g. if the work item is due to be completed at 17.00 and the time expected to complete the work item is 1 hour, the Due Date 'At Risk' Reminder will be sent at 15.30. </p><p></p><p>Note that this notification will not be sent if:</p><ul><li>the work item is in a state of Draft</li><li>the work item is in a state of In Progress and assigned to a user</li><li>the work item is in a state of Waiting AND its due date has been configured with the option 'Add Wait Time To Due Date'</li></ul><p>Anyone subscribed to receive notifications for the parent of this work item (if there is one) will also receive this notification.</p></td></tr><tr><td>Work Item is Overdue</td><td>The due date of the work item has been missed and it is now overdue.</td><td></td></tr><tr><td>Action Rejected</td><td>A robot has actively rejected an Action, or repeatedly failed to process it.</td><td></td></tr><tr><td>Case Needs Attention</td><td>A Case has encountered a problem and requires intervention before it can proceed. </td><td></td></tr><tr><td>Peer Review Changes</td><td>The peer review of an Action has been marked as 'Passed', 'Failed', or 'Unable to be Completed'.</td><td><p>Note that in order to receive this notification, users must:</p><ul><li>be in the Queue that this Action belongs to (or manage it), AND</li><li>be subscribed to receive notifications about this Action (being subscribed to the Case is not enough), AND</li><li>have the setting to receive notifications from 'My Queues' switched on.</li></ul><p>Additionally, the person who completed the peer review will not receive the notification.</p></td></tr></tbody></table>

{% hint style="info" %}
Note that you will only ever receive **one** notification about the same event for a work item.&#x20;
{% endhint %}

### How to notify me - different types of Notifications&#x20;

For each event you subscribe to, you will automatically get notified in Work Manager in the [Notifications Centre](#notifications-centre) (via the Notifications icon in the header bar) - with a counter showing the number of unread notifications. However you can additionally choose if you also want to be notified by [email](#email-notifications) and/or by [browser pop-up](#browser-pop-up-notifications).&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fhte5EotPM8Hb5j2Iyj6e%2Fimage.png?alt=media\&token=d801d1d8-c1dc-4b85-aa04-6cd797a6ff63)

## Useful Links

There are three useful navigation links:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MYzQmkKW2pv6XWGPf7q%2F-MYzXQx5A87HSffYLXOo%2FUseful-Links.gif?alt=media\&token=4ff71f66-200d-4bc1-ba3b-a53b8714b94c)

1\. [**Enate Homepage**](https://www.enate.net/) – This is the Enate Company website. Here you can see latest resources, industry insight and product release info.

2\. [**Enate Academy**](https://www.enate.academy/learn) – Here you can sign up for different Enate learning courses in English, Spanish and Portuguese languages.

3\. [**Enate Help**](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1) – This is a link to Enate's Work Manager help files.


# Email Signature Optimisation

Enate has features and rules to help keep emails (and email chain) file sizes optimised – this helps keeps overall system performance of your - and your clients’ - systems running well.

As part of this, changes have been made relating to your email signature templates, i.e. the standard content that you’ve defined to go at the footer of mails you send. If the image files for signatures aren’t chosen appropriately (for example pasting in a very large image file and adjusting to fit), this can often lead to unnecessarily large email file sizes each time you send, which over time can reduce performance of the systems handling the mails.

To help combat this, the following features can be found:

### Recommendation to optimise your signature: <a href="#recommendation-to-optimise-your-signature" id="recommendation-to-optimise-your-signature"></a>

If your email signature template is over 200KB, when you’re in a Work Item and you select to write a mail, the system will show a message recommending you optimise the signature size, along with a link to your User Settings page to let you do this.

{% hint style="info" %}
*Please note that you will still be able to send your emails as normal, even with the larger signature template still in use.*
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTDjLsqrsw5yZtDHCjxkp%2Fimage.png?alt=media&#x26;token=eac298c1-1340-41ae-830e-00758390919d" alt=""><figcaption></figcaption></figure>

This message may also show immediately upon logging into Work Manager, until your signature is below the 200KB recommendation. You can click the warning popup link link, or independently go to your User Settings page.&#x20;

### How to Optimise your Email Signature: <a href="#how-to-optimise-your-email-signature" id="how-to-optimise-your-email-signature"></a>

Whenever you are adjusting your email signature template here, you'll be able to see the file size. If it exceeds the limit it will show in red and you'll be asked to reduce the size. You can either choose a smaller file, or hit the ‘Optimise’ button.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMjVachaV3oUe7nRKOY6i%2Fimage.png?alt=media&#x26;token=ddd21248-acff-4fef-a35e-2b8ef035cfcf" alt=""><figcaption></figcaption></figure>

Click the Optimise button to compress the file sizes (this won't change the image dimensions).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5deI4cHNDzW2LfFor8Hc%2Fimage.png?alt=media&#x26;token=3a52e6b9-8d71-46c2-a0d6-6049c2613e3e" alt=""><figcaption></figcaption></figure>

Once you’ve optimised the signature size, you’ll be able to Save your changes.


# Test Mode

How to use Enate's Test mode to check your config changes before setting them live.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Switching to Test mode <a href="#switching-to-test-mode" id="switching-to-test-mode"></a>

If your user account is set to allow you to access test data, you can switch your Work Manager environment over to ‘Test Mode’. This link is available in the user dropdown on the right of the header bar.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDnJO5KvN4VBsavId2HlW%2F16-Switching-to-Test-Mode.gif?alt=media\&token=e1d891de-d4b1-4a4c-826f-8aea573d4576)

## Test Mode Explanation <a href="#test-mode-explanation" id="test-mode-explanation"></a>

Once you are running in test mode you will only see test data; allowing you to create and run test work items through test versions of processes to verify them before setting live, all without affecting live production data.

As a visual reminder, the header bar is set to red when you are in Test mode.

## Defining Different Managers and Members of Queues in Test Mode <a href="#defining-different-managers-and-members-of-queues-in-test-mode" id="defining-different-managers-and-members-of-queues-in-test-mode"></a>

Test mode functionality allows you to set a different manager for a Queue when running in Test mode vs. Live mode.

Example: Consider **Manager 1** who has access to live mode and is responsible for managing two Queues, **Funding** and **Master** **Case** Queue.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9gm1OMy6tLbgy9Dy%2Fimage.png?alt=media\&token=bf28b64a-3e8e-4c3d-b9a8-66472c51830b)

In Test Mode, the same two Queues can be managed by another user who has Team Lead and Test Mode permission – see below example where **Manager 2** has been set to be in charge of the Queues in Testing Mode.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9kGgY1W_t3ul-aLF%2Fimage.png?alt=media\&token=7ec9b6f7-c3c3-4bc3-8eb7-3513f2308dea)

## Switch Robots between Live and Test <a href="#switch-robots-between-live-and-test" id="switch-robots-between-live-and-test"></a>

It is possible to switch a robot so that it can run in test mode or live mode. Specifically, two new activities have been added to the activity libraries for UiPath, Automation Anywhere and BluePrism (and the standard APIs adjusted so this can be called generically) as follows

* Set Live Mode
* Set Test Mode

These Actions allow you to flip a robot between test and live states. Once a robot has been flipped into Test mode, subsequent activity calls which the robot might make, e.g. ‘Get more work’ and ‘Create Ticket/Case etc.’ take place within that context of Test mode, getting and creating only test work items. The robot should be switched back to Live mode once the process is set to live, so ensure it is then creating live work items.

## Test Contacts - Separate test contacts in the system <a href="#test-contacts-separate-test-contacts-in-the-system" id="test-contacts-separate-test-contacts-in-the-system"></a>

Enate supports the creation of separate Contact records in Test Mode, i.e. any contact records you create in Test mode will be accessible only to Test Mode users (and contacts created in live mode will be accessible only to Live mode users).  This helps to ensure that emails from test work items are not accidentally sent to production users, and vice versa.

### Warning - Do Not Use Production Email Addresses when creating Test Contacts

{% hint style="warning" %}
**IMPORTANT:** Do NOT create Test Contact records using information (specifically email address) for people you will be using in normal production. \
**If you create a Contact record while you are in Test mode this will be created as a Test Contact, and ALL emails arriving into the system from that email address will create a Case/Ticket in Test Mode.** This would result in incoming production emails creating work test work items which would not be visible by production users.\
\
If you have created a production Contact record as a Test Contract record in error, you should edit the Test contact by changing the email address, then switch back to normal production mode to create the desired normal Contact record.<br>
{% endhint %}


# Multilingual Support

Enate Work Manager supports the following languages:

1. English (British)
2. English (US)
3. French
4. German
5. Romanian
6. Hungarian
7. Polish
8. Spanish
9. Portuguese Brazilian
10. Russian

The Operations environment for end users to deliver the service fully supports these languages and each user will be allowed to choose their preferred language along with date-time pattern in their user profile settings.

To set a preferred language, select a language from the Language dropdown list in User Settings.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZCCjQMZrIXW_c-JAut%2F-MZCWE2H20vuRKMcEY_D%2FChange-Language.gif?alt=media\&token=112e24b6-1177-4eba-8d46-043d1fae0317)

The display of labels will appear in the logged-on user’s preferred language - this is achieved by adding a ‘language package’ into **Enate**. Each language package will have mapping for user-specific language like Portuguese, for example, ‘**Queue**’ will be ‘**Fila’** and ‘**Action’** will be ‘**Açao’** in Portuguese.

Here is the list of UI elements which will be available in the logged-on user’s preferred language:

| Item               | Details                                                                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Home Page          | <ol><li>RAG filters</li><li>My Team</li><li>Bot Farm</li><li>Queue</li><li>Chart</li><li>Grids and column settings</li></ol><p>Same behaviour in Inbox page as well.</p> |
| Quick Find         | People, Comms and work items search                                                                                                                                      |
| Queue Page         |                                                                                                                                                                          |
| Navigation Links   | Link to Builder, Queue Page or recent accessed work items etc.                                                                                                           |
| User Profile Page  | Here user can also change preferred language along with datetime pattern.                                                                                                |
| Call Handling Page | This page shows all communications and work items related to individual users                                                                                            |
| Work item UI       | Labels and Button like Category picker, state etc.                                                                                                                       |

{% hint style="info" %}
Note – Real names such as customer names and usernames will be remained in the original language, as entered by the configurers in Builder.
{% endhint %}

## Data entered by Work Manager End Users <a href="#data-entered-by-work-manager-end-users" id="data-entered-by-work-manager-end-users"></a>

Enate fully supports a User’s preferred language in Work Manager display and UI elements including labels, links and buttons, however anything added by you will stay in same language you originally entered it in and will not be auto-translated into any other language when being viewed by other users with a different preferred language.

For example, if a Brazilian user adds a note to a Case in Portuguese, Enate will then save the note in Portuguese in the database and will only ever show the note in Portuguese.

Here is full list of items which will be driven by user input and which **WILL NOT** be auto translated by the product:

| Item               | Detail                                                                                                                                                                                                                                                     |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Case               | <p></p><ol><li>Notes</li><li>Emails</li><li>Case - short description/title</li><li>Override Action instruction o new Action launched by end user</li></ol>                                                                                                 |
| Action             | <p></p><ol><li>Notes</li><li>Emails</li><li>Checklist comments</li><li>Action State- 'Unable to complete' reason text</li><li>Override Action Instruction of new Action launched by end user</li><li>Action Peer Review note entered by reviewer</li></ol> |
| Ticket             | <p></p><ol><li>Title and description of new child Tickets</li><li>Name of new Action launched by user</li><li>Name of new Case launched by user</li></ol>                                                                                                  |
| Contact            | Details about contact like address.                                                                                                                                                                                                                        |
| Files              | File name and note about file                                                                                                                                                                                                                              |
| Defect             | Defect description                                                                                                                                                                                                                                         |
| Reassignment Notes | Text entered by user while reassigning a piece of work to another teammate.                                                                                                                                                                                |

### Custom Data and Cards <a href="#custom-data-and-cards" id="custom-data-and-cards"></a>

The initial releases of multilingual functionality will not support configurers defining multiple languages when creating Custom Data and Smart Cards in Builder. Multiple cards and data items would be required for this.

### In App Notifications <a href="#in-app-notifications" id="in-app-notifications"></a>

The initial releases of multilingual functionality will not support notifications in languages other than English.


# Appendix


# How to enable spell check in Enate

To ensure that you are able to carry out your work in Enate spelling error-free, you can enable spell check in your web browser to help check your spelling as you go about your tasks.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzIa5LER3gs88BWPvciIg%2Fimage.png?alt=media&#x26;token=0814004b-e728-48b9-bb45-cce9bdfc75b5" alt=""><figcaption></figcaption></figure>

Below are the steps to activate spell checker in three of the most popular browsers: Google Chrome, Mozilla Firefox and Microsoft Edge.

### Google Chrome&#x20;

1. Open Chrome Settings:&#x20;

* Click on the three vertical dots in the upper right corner.&#x20;
* Select Settings.&#x20;

2. Access Language Settings:&#x20;

* In the settings menu, type "language" in the search box.&#x20;
* Click on Languages.&#x20;

3. Enable Spell Check:&#x20;

* Under the Spell check section, choose between Basic spell check or Enhanced spell check.&#x20;
* You can also add new languages if necessary.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8May4nin3LmwYiO8dzBA%2Fimage.png?alt=media&#x26;token=3d341f20-b24d-4944-a0e0-a664a4099afd" alt=""><figcaption></figcaption></figure>

### Mozilla Firefox&#x20;

1. Open Firefox Menu:&#x20;

* Click on the three horizontal lines in the upper right corner.&#x20;
* Select Settings.&#x20;

2. Navigate to Language Settings:&#x20;

* In the left sidebar, select General.&#x20;
* Scroll down to the Language and Appearance section.&#x20;

3. Turn on Spell Check:&#x20;

* Check the box next to Check my spelling as I type.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FB2pTkWTUdgB1ryQ69ETs%2Fimage.png?alt=media&#x26;token=e9384f95-78f8-4995-ab89-c1cae3201543" alt=""><figcaption></figcaption></figure>

### Microsoft Edge&#x20;

1. Open Edge Settings:&#x20;

* Click on the three horizontal dots in the top-right corner.&#x20;
* Select Settings.&#x20;

2. Find Language Options:&#x20;

* Scroll down and click on Languages.&#x20;

3. Enable Spell Check:&#x20;

* Toggle on the option for Enable spell check for your preferred languages.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkFpZM44hzPctIqYYrzDh%2Fimage.png?alt=media&#x26;token=e6f20c9b-b4a2-4b93-93fe-b66202db098c" alt=""><figcaption></figcaption></figure>


# Potential Validation Errors for Bulk Creation of Work Items

| **Error Area**                                                                     | **Description**                                                                                       |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Status Error**                                                                   |                                                                                                       |
| "not\_valid": "Data not valid or Something went wrong"                             | When wrong information is input into a cell, so work items are not able to be created                 |
| "completed": "Completed"                                                           | When work items are successfully created                                                              |
| "in\_progress": "In progress"                                                      | When work item creation is in progress                                                                |
| **Error**                                                                          |                                                                                                       |
| "1": "Uploaded file is not a \*.xls or \*.xlsx file"                               | When the upload file format is other than .xls or .xlsx file                                          |
| "3": "Workbook has multiple worksheets. Only first sheet will be processed"        | When the same file has multiple sheets of work data to be processed                                   |
| "5": "Master Process Instance not live"                                            | When the process instance is not live or the versions are draft                                       |
| "101": "Worksheet is missing the required column '{{v0}}'"                         | When the excel sheet does not have required column to process work items                              |
| "102": "Column '{{v0}}' is of type '{{v1}}' which is not supported in Bulk Create" | When we use unsuported dat types like Entity relastionship , Table                                    |
| "103": "No field found to link Column '{{v0}}' to"                                 | When Validate bulk create api is not able to map the column data with the system data                 |
| "200": "Creation of a schedule-driven Case is not supported"                       | When a Case is linked to schedules and use the Case in the excel                                      |
| "300": "Title is not unique in file"                                               | When uploaded file has same title for multiple work items in the file                                 |
| "301": "Title is not unique"                                                       | When uploaded file has same title that is already created in system                                   |
| "302": "Value is blank and column is required"                                     | When there are no input values for mandatory fields                                                   |
| "303": "Value in not valid for data type '{{v0}}'"                                 | When custom field cannot input the particular data or data is not related to custom field             |
| "304": "No person could be found from email address"                               | When we input a wrong email id or email id is not present in the system                               |
| "305": "Customer not found or you do not have permission to see it"                | When we input a wrong Customer name or we don’t access to create work items under particular customer |
| "306": "Contract not found under Customer or you do not have permission to see it" | When we input a wrong Contract name or we don’t access to create work items under particular customer |
| "307": "Service not found under Contract or you do not have permission to see it"  | When we input a wrong service name or we don’t access to create work items under particular Contract  |
| "308": "Process not found under Service or you do not have permission to see it"   | When we input a wrong Process name or we don’t access to create work items under particular service   |
| "309": "Ticket Category not found"                                                 | When we input wrong tickect category value                                                            |
| "310": "Value is not valid for list"                                               | When the input value doesn’tmatch the configured list/Multi level List data                           |
| **UI ERROR**                                                                       |                                                                                                       |
| "1001": "There are no valid items to process."                                     | Where there is no data to process in excel                                                            |
| "1002": "All valid items have been processed."                                     | When all the valid work items are created                                                             |
| "file\_upload\_limit": "{{name}} is bigger than the server limit ({{limit}})"      | When the uploaded file size is larger than the system configured upload limit                         |
| "file\_upload\_failure": "Failed to upload file"                                   | when file upload is failed                                                                            |


# Search terms ignored - further details

Information about terms which are auto-removed from various searches that users can perform in the system

As part of standard underlying features in Enate to optimise searches which users perform, certain commonly used terms are removed from searches if they've been manually entered. This is in order to ensure timely response for search results, plus avoid the returning of vast volumes of qualifying results which would obscure the desired results from the users. One of the approaches used for this is the use of 'Stop Lists'.

## Stop List

A stop list is a list of standard common words such as ‘and’ ‘the’, ‘me’ etc., which are ignored from searches that would otherwise return too many results.&#x20;

Below is a comprehensive list of all of the words in the stop list that ALL searches within Enate will ignore - this not only includes searches in Quickfind, but also searches which are performed for users, searches for emails, searches for Work Items e.g. for Tickets when merging Tickets etc. If you enter any of these terms, they will be auto-ignored as terms to return search results for.

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaqRBSvFoWXuUWFtMezjn%2FEnate%20SQL%20Stop%20List.xlsx?alt=media&token=566d3255-db99-4036-ba08-62124a3452a2>" %}

Multiple Stop Lists are supported for various user languages.

{% hint style="info" %}
Note: When searching for Users and Emails, the English (British) stop list is always used. For work items (Title, Customer Name, Contract Name, Service Name, Case/Ticket Name, etc.) we use the language of the logged-on user to find the stop list. Additionally, please note that Hungarian is not directly supported by SQL, so the stop list applied for searches for Hungarian users is also the English stop list.
{% endhint %}

## Characters Ignored in Quickfind

Specific further characters are set to be ignored when performing searches in Quickfind, e.g. “\*”, “?”, “@” etc. This will mean for example that when searching for customer.com in Quickfind, the words 'customer' and 'com' would be searched for. As such, it’s recommended to place such word combinations in quotes to search for them as a specific phrase - i.e. searching for “customer.com” will likely bring back the results you are looking for.&#x20;

Below is a comprehensive list of all of the characters that searches in Quickfind will ignore:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdSaH4pw6gEgxw6-JX9%2F-MdSaPOm6gF11tKAu3JA%2FCharacters%20ignored%20in%20Quickfind.pdf?alt=media&token=0599d71d-22b9-4495-87ce-62addf780433>" %}
Characters ignored in Quickfind
{% endfile %}


# System behaviour for Determining Assignee, Owner & Queue for Work Items

As part of managing Tickets, Cases & Actions in your workflows in Enate, the system will regularly evaluate who the work is assigned to, who is set as the Owner, and which Queue the work item is linked to. There are detailed sets of rules which are followed, in order, when determining this.&#x20;

Before looking at these detailed sets of rules, it’s important to understand the higher-level pattern of how such work item allocations are evaluated, and indeed when. The way this works is as follows:

1. First we [determine WHEN such re-evaluations occur](#determining-when-re-evaluations-occur) – essentially this happens when anything changes in the 'Status’ card of a Work item.
2. When the system determines it needs to do such an evaluation, we initially use the work item’s status/situation to [determine which of the Assignee, Owner and Queue values need to be Set, and which need to be Cleared](#determining-if-assignee-owner-and-queue-values-need-to-be-set-or-cleared) completely.
3. [For those which require setting](#how-an-assignee-owner-and-queue-are-set):

   a. If a Queue is to be set, it's simple - just select the Queue referenced in the Allocation rule (there are only two types of Queue allocation rule to follow).

   b. For Assignee and Owner, there's more detail - we have to run through a series of rules, in order, for these - stopping when the rule is met and a valid\* target is selected.

\*[Validity check](#validity-checks) - As part of the Assignee / Owner allocation rule check, we have to determine if the target is **valid** (there are a number of validity check rules which it must pass). If not, we continue through the rules in part 3 until a valid target is found.

Now that the higher-level pattern at play has been described, we can go look at each set of rules which are run through for sections 1-3 above, and for the target validity checks.

## **Determining WHEN re-evaluations occur**

The system will re-evaluate the Assigned User, Owner and Queue whenever the information in the Status card changes, specifically:

* the Status changes
* the Wait Type changes
* the Scheduled Follow Up On date changes
* the Wait for More Information Until date changes
* the Waiting For option changes (for Cases only)
* the Ticket Context changes
* the Ticket Category changes
* the In Peer Review status changes
* New Information is received on the work item
* A Case encounters a Problem

## **Determining if Assignee, Owner and Queue values need to be set or cleared**

When the system determines it needs to do such an evaluation, we initially use the work item’s STATE to determine which of the Assignee, Owner and Queue values need to be Set, and which need to be Cleared completely. You can see this information in the table below:

| **Work Item Status/Situation**               | **Assignee** | **Owner**   | **Queue**   |
| -------------------------------------------- | ------------ | ----------- | ----------- |
| Closed                                       | Clear value  | Clear value | Clear value |
| Draft                                        | Set a value  | Clear value | Clear value |
| New Information Received                     | Set a value  | Clear value | Set a value |
| Needs Attention (only relevant to a Case)    | Set a value  | Clear value | Set a value |
| To Do or In Progress for an Action or Ticket | Set a value  | Clear value | Set a value |
| To Do or In Progress for a Case              | Clear value  | Set a value | Clear value |
| Resolved or Waiting                          | Clear value  | Set a value | Clear value |

&#x20;

## **How an Assignee, Owner and Queue are set**

* **Queues** - If a Queue is to be set, it's simple – the configured [Queue Allocation Method](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method) is run.
* **Assignee and Owner** - If an Assignee or Owner is to be set, there's more detail. We have to run through a series of rules, in order, stopping when the rule is met and a [valid target](#validity-checks) is selected.

Before the list of rules is run, there is one higher check: if an Assignee/Owner is currently set, **don't change the Assignee/Owner unless the Ticket Category has changed**.

Otherwise, run the following rules, in order, stopping when you a valid target is identified:

1. If the ‘Keep with me' option has been set on a work item, the Assignee/Owner is set as the user who has selected ‘Keep with me’. If not or the resulting user is not valid, then
2. If the Owner user is not blank, then set Assignee to that value also. If not or the resulting user is not valid, then
3. If the work item is a Ticket and the Ticket Category has changed and either the Wait Type has changed or the status is Resolved then the Assignee/Owner is set as the user currently updating the Ticket. If not then
4. If the work item is not a Ticket OR it is a Ticket (where the Ticket Category hasn't changed AND we have more than 2 status history rows - i.e. it is not in its first non-draft state), then:
   1. Set Assignee and Owner to the last user/robot to update work item. If none or the resulting user is not valid, then
   2. Set Assignee/Owner as (any) previously assigned to user/robot in descending order of when it was assigned to them. If none or the resulting user is not valid, then    &#x20;
   3. If Action started by Workflow (i.e. not manual ad-hoc), then set the Assignee/Owner as the last user/robot to work on the same previously completed Action in the Case (or Peer Review the Action if in peer review). If none or the resulting user is not valid, then
5. Run the [Allocation Rule](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours) for this work item:       &#x20;
   1. If the primary push allocation is configured to a specific user, set Assignee/Owner to that user. If none or the resulting user is not valid, then
   2. If the secondary push allocation is configured to a specific user, set Assignee/Owner to that user. If none or the resulting user is not valid, then
   3. If Primary push allocation configured to Position, from the users that occupy this position set the Assignee/Owner as the user with the fewest work items in their inbox. If none or the resulting user is not valid, then
   4. If Secondary push allocation configured to Position from the users that occupy this position set the Assignee/Owner as the user with the fewest work items in their inbox. If none or the resulting user is not valid, then
6. If the work item is a Case, set Assignee/Owner as the user/robot that started that Case.&#x20;

## **Validity Checks**

As part of the Assignee / Owner allocation rule check, we have to determine if the target is valid. To be valid, there are a number of validity check rules which it must pass. If not, we continue through the rules of setting an Assignee/Owner until a valid target is found. The validity checks that are run through are as follows:

* If the User/Robot is not allowed to work on work items of this type (i.e. Live/Testing) then block    &#x20;
* If the User/Robot is retired then block&#x20;
* If the User does not have permission then block (no permission check for Robots)         &#x20;
* If the Robot is suspended then block   &#x20;
* If the Robot has performed Get More Work more than 3 times for this work item then block
* If the user selected is a Robot and the work item is an Action that is in the Peer Review stage then block (Robots cannot perform Peer Reviews)           &#x20;
* If the user selected is a Robot and the work item is an Action and no Robot Farm is configured for the Action then block&#x20;
* If the user selected is a Robot and the work item is an Action and the Robot is not a member of the Robot Farm configured for the Action then block
* If the user selected is a Robot and the work item is a Case then block (Robots cannot be assigned Cases)
* If the work item is a manual with Peer Review Action that is on the Peer Review stage and the User performed 1 or more updates while it was on the Doing stage then block (users can’t peer review their own work)           &#x20;
* If the work item is a manual with Peer Review Action that is on the Doing stage and the User performed 1 or more updates while it was on the Peer Review stage then block (users can’t be asked to do work if they have previously peer reviewed it)


# Screen Resolution Support

Details on screen resolutions supported by Enate

### Minimum Supported Screen Resolution

The minimum screen resolution supported by Enate at 100% DPI is: **1366 x 768**. \
This means that resolutions of 1280x1024 and below are NOT supported.

### Supported Screen Resolutions vs. DPI

Higher resolutions screens may run with DPI settings in excess of 100%. With this in mind, the list below shows the minimum 'screen resolution & DPI' combinations supported by Enate. Industry definitions for these screen resolutions are also provided here to help clarification:

* 1366 x 768 High Definition (HD) – Supported at 100% DPI Only
* 1600 x 900 High Definition Plus (HD+) – Supported at 100% DPI Only
* 1920 x 1080 Full High Definition (FHD) – Supported up to 125% DPI
* 1920 x 1200 Wide Ultra Extended Graphics Array (WUXGA) – Supported up to 125% DPI
* 2560 x 1440 Quad High Definition (QHD) – Supported up to 150% DPI
* 3440 x 1440 Wide Quad High Definition (WQHD) – Supported up to 150% DPI
* 3840 x 2160 4K or Ultra High Definition (UHD) – Supported up to 200% DPI

### Additional Browser Toolbars vs. Screen Resolution support

Particularly when running on minimum supported resolution, Enate always recommends users to run Enate in Full-screen mode (access this via F11 key in browser) to give maximum screen real-estate for display. If you have additional toolbars installed in the browsers above the 'default' system browsers (e.g. browser add-ins), this can significantly reduce available screen space and may go below minimum supported screen dimensions.




---

[Next Page](/enate-help/llms-full.txt/1)

