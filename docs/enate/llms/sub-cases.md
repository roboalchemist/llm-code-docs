# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/sub-cases.md

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
