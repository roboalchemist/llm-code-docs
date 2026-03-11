# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-groups.md

# User Groups & Data Permissions

## Overview

User Groups are, as the name suggest, ways of grouping together a number of users - specifically Service Agent type users. User Groups can be used for [setting Permissions](#setting-permissions) (see below) for a number service agents to specific parts of your business operations, i.e. for certain Customers, their Contracts, Services or even down to specific Case & Ticket processes.

Watch this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MzAyOA==>" %}

## Creating User Groups

To create a user group, navigate to the 'User Groups' section of User Management, create a new group and add one or more users into it. Once saved, the User group is ready to use with permissions linking.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq-Pf1QM1544JFrMeJ%2F-MWq1BFZdoijBX1lUTLr%2FCreate-User-Group-Gif.gif?alt=media\&token=904dec91-ac1f-418a-920d-752535a85693)

## Adding a User to a User Group

When creating or editing a User account, you can select which user groups they should be in via their settings on the Access tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq-Pf1QM1544JFrMeJ%2F-MWq1M0UiyusQAqkr9lX%2FAdd-User-To-UserGroup-Gif.gif?alt=media\&token=418fe099-e4d1-4f0a-be59-ac572116dd82)

There are also further access options within the tab, see the section about [managing access for service agents](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/service-agents) here

## Setting Permissions <a href="#setting-permissions" id="setting-permissions"></a>

You can set user Permissions in conjunction with [User Groups](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-groups) to control levels of access for your Service Agents to the various parts of your business operations (as represented in the Service Matrix screen - who are your customers, what services are you delivering to them).

You do this by linking the user group to the 'Permissions' setting at various points in the Service Matrix. You can either add permissions [at customer/contract/service-level](#setting-permissions-at-customer-contract-service-level) or [at Case or Ticket process-level](#setting-for-specific-customers-case-or-ticket-process).&#x20;

Link up at the customer/contract/service-level, that User group has access to all work items under that customer/contract/service. Conversely if you set down at the Case-process level, that User Group has access to work items within that Case process specifically within that customer/contract/service combination.

### At Customer/Contract/Service-Level <a href="#setting-permissions-at-customer-contract-service-level" id="setting-permissions-at-customer-contract-service-level"></a>

Setting User groups with permissions at customer/contract/service can easily be done by navigating the to Service Matrix screen and clicking to edit the desired customer/contract/service.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq-Pf1QM1544JFrMeJ%2F-MWq1t28djO0H4s25UfS%2FAdd-Permissions-to-a-Contract-Gi.gif?alt=media\&token=37d9f5f7-5060-410c-9055-c9a3401d1f97)

Once that has been set, only users within this User Group have access to work items (creation, editing etc.) for that customer, contract or service.&#x20;

For example, if you link up at the customer-level, that User group has access to all work items under that customer. Conversely if you set down at the Case-process level, that User Group has access to work items within that Case process specifically within that customer/contract/service combination.

### At Case/Ticket Process-Level <a href="#setting-for-specific-customers-case-or-ticket-process" id="setting-for-specific-customers-case-or-ticket-process"></a>

To set permissions for a specific customer's Case or Ticket process, go to the Service Matrix, select the Permissions link and add the User Groups you want to be able to access it.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq-Pf1QM1544JFrMeJ%2F-MWq1eWXpfa_TKzLSnDN%2FAdd-Permissions-to-a-Ticket-Gif.gif?alt=media\&token=7ed9fe81-e476-4bbf-8617-8cf63be327a6)

Note that any Permissions set at higher level will show read-only when accessing settings for any item in the Service Matrix.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq-Pf1QM1544JFrMeJ%2F-MWq1iIrw7nf1YE-QMGE%2Fimage.png?alt=media\&token=385b78f9-22c6-410e-9469-50ac73395c8d)

Once that has been set, only users within this User Group have access to work items (creation, editing etc.) within that Case process specifically within that customer/contract/service combination.
