# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours.md

# Allocation Flavours

## Overview

There are several allocation options available which allow you to route work items to the most appropriate resources for your business. These allocation options are defined when configuring your processes in Enate Builder.&#x20;

Watch the following video to find out more about allocation options in Enate.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2Mjc3MA==>" %}

### Allocation Approaches – Push vs Pull

There are two main approaches to allocating work in Enate, these are ‘Pull’ Approach and ‘Push’ Approach:

* **Pull Approach** – work gets routed to Work Queues. This allows a) the work to be visible to the Manager(s) of that Queue and b) for people working out of that Queue to be allocated unassigned work items from it when they next bit the ‘Get more work from Queue’ button in their Enate Inbox.\
  **To use the Pull approach, you specify to allocate to a Queue, and then leave the Primary / Secondary allocations blank.**
* **Push Approach** – works gets routed directly to a user, either because of a specific user allocation, or to a position (from which the system selects one of the users holding that position).\
  **To use a Push approach, you specify and Primary (and, if you would want a backup in case no users are found with first rule, a Secondary) allocation.**

{% hint style="info" %}
Note: that when specifying a Push allocation it’s still highly recommended to specify a Queue allocation so that the work is linked to a Queue. If you do not, and the work becomes unassigned, the Team Leader will lose visibility of the Work item.
{% endhint %}

## Allocation Flavour **Configuration**

To configure a new allocation flavour, click to add a new allocation. Alternatively, you can click to clone an existing allocation flavour and adjust the settings for the new allocation flavour from there.

This will bring up the Allocation pop-up where you will need to enter a name and description for the new allocation flavour, as well as the Queue, Queue Method and Primary allocoation method for it.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpx0L2Vahwz3uf8kdK%2Fimage.png?alt=media\&token=e0ff6f0d-d053-4058-b2c6-e7250571bd74)

| Setting                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                                 | Name of the allocation method. This name will subsequently be seen in the selection dropdown.                                                                                                                                                                                                                                                                                                                                                              |
| Description                          | Description for the allocation flavour.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Queue Method                         | For Pull allocations: There are two methods through which Queues can be determined: By Queue Name alone (you then just select from a list of Queues), or by the Queue Name for a specific Team. See here for [more details](#setting-a-queue-method).                                                                                                                                                                                                      |
| Queue                                | For use with the standard ‘Pull’ allocation approach. This determines the Queue into which this Work Item should be allocated. The majority of allocations should use this pull approach where work is sent to a Queue and agents then pull work from this Queue when they are available to perform the activity. You can also create a new queue from here, see here for [further information](#creating-queues).                                         |
| Primary                              | If you are using ‘push’ allocation – where work is more directly allocated straight to a user, this is where you set the allocation method used for determining which positions or team to allocate the work to. A number of standard methods are available to choose from. Depending upon the method selected, additional parameters may be required. See here for [more information about allocation methods. ](#setting-a-primary-secondary-allocation) |
| Inform Via Email                     | For Push allocations, whether to send an email to the person who the work is allocated to.                                                                                                                                                                                                                                                                                                                                                                 |
| CC on Emails to all Primary Position | For Push Allocations, whether to email every person who occupies the position being used to determine someone to allocate to.                                                                                                                                                                                                                                                                                                                              |

## Creating Queues

The following video shows you how to create Queues and set Queue methods.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2Mjc3Mg==>" %}

You can create a new queue from here by clicking on the plus icon from the Queue dropdown.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mexq_YyACsG6rbM-PyE%2F-Mey1Oay4HYPDwhMAxAD%2Fimage.png?alt=media\&token=87b95f07-7312-489f-b5de-9d32d820c3dd)

Enter the new Queue's name and hit 'Create'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mexq_YyACsG6rbM-PyE%2F-Mey1MLkGqkr8t8AT-ye%2Fimage.png?alt=media\&token=9368c31a-19dc-42be-a916-9f84d9c68f76)

This newly added queue will be automatically selected.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mexq_YyACsG6rbM-PyE%2F-Mey1RLG3YcCni-AFP-h%2Fimage.png?alt=media\&token=4ef0a674-6099-49f8-b81b-c7d5eb729c00)

{% hint style="info" %}
Please note that you can't delete and edit queues here, this can only be done from the [system-settings](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/queues).
{% endhint %}

## **Setting a Queue Method**

!\[Graphical user interface, text, application

Description automatically generated]\(<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdWibl0gbFLhHv3_AU6%2F-MdWjFUaAsZG6TJImQDl%2F0.png?generation=1625137416716083\\&alt=media>)

| **Method**                  | **Notes / Further Variables**     |
| --------------------------- | --------------------------------- |
| From Queue by Name          | Select a Queue from the dropdown  |
| From Queue by Name and Team | Select a Queue from the dropdown. |

### ‘From Queue by Name and Team’ allocation method

This method is used when you have a very large number of Queues you might have to configure, e.g. a different Queue for each contract but you have a thousand contracts.

To use this method you should first create a Queue in the general settings section with a name which will be used as a suffix to the eventually used Queue name, e.g. ‘+L1’.

The system will use this information and will then auto-generate a new Queue for you with the text specified in the ‘Team’ attribute of the Contract (see Service Matrix section).\
e.g. if you set a name of ‘ACMEContract’ in the ‘Team’ attribute of a Contract, the system will autogenerate a Queue called ‘ACMEContract +L1.

!\[Graphical user interface, text, application, email

Description automatically generated]\(<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdWibl0gbFLhHv3_AU6%2F-MdWjFUbE026VxFej93j%2F1.png?generation=1625137416711737\\&alt=media>)

This method saves large amounts of effort having to manually create and maintain the Queues – instead they are auto-generated based on this information.

## **Setting a Primary / Secondary Allocation Method**

If you are using ‘push’ allocations where work is directly allocated straight to a user, you should then select an allocation method to determine position or team to allocate the work to.

This can be configured in the Allocation pop-up of a work item.

There are a number of standard methods available to choose from and, depending upon the method selected, additional parameters may be required. There is more detailed information for each of these options below.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FR0dpdx1H1JR5YzEO9fm0%2Fimage.png?alt=media&#x26;token=c5c17898-29ef-41a4-9f37-6d59abe0ee2d" alt=""><figcaption></figcaption></figure>

Watch this video for more information about setting primary and secondary allocation methods.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MjgxNA==>" %}

### ‘Completer Of Previous Action’ allocation method

With this allocation method, you can allocate certain Actions to the user who completed the previous Action. By doing so it decreases the load on the Queue and directly assigns the Work Item to a specified user as per config.

Simply select the particular Action Type from the resulting dropdown.

!\[Graphical user interface, text, application

Description automatically generated]\(<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdWibl0gbFLhHv3_AU6%2F-MdWjFUdxR94eAmg7lOR%2F3.png?generation=1625137416720014\\&alt=media>)

### 'Contact Tags' allocation method

This allocation method lets you allocates work based on a contact tag. At runtime, the system will look for users associated with the work item which have been tagged with the configured user type tag, and allocate the work to them. If multiple users share this tag, the system will select the user with the least amount of work items in their inbox to allocate to.

Simply select the desired contact tag from the resulting dropdown. The list of contact tags you can can choose from are defined in the [General Settings section of Builder](https://docs.enate.net/enate-help/builder/system-wide-settings#contact-tags).&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FiFEC9GbxghKzdWOuKzNe%2Fimage.png?alt=media&#x26;token=7e960d30-e748-437d-b08c-58a5120827fb" alt=""><figcaption></figcaption></figure>

### 'Individual from User Group' allocation method

This allocation method will allocate work items to an individual in a particular User Group based on a round robin basis i.e. user 1, then user 2, then user 3, then user 1 etc.

Simply select the desired User Group from the resulting dropdown. The list of User Groups you can can choose from are defined in the [User Management section of Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-groups).&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaSN4d1wd8ojvy8r7cb1l%2Fimage.png?alt=media&#x26;token=b6fc2dc2-40e4-4f89-95ab-c268a8e03708" alt=""><figcaption></figcaption></figure>

### 'Individual from User Group (by capacity)' allocation method

This allocation method allocates work items  to an individual in a particular User Group who has the lowest amount of estimated hours of work in their inbox.

Simply select the desired User Group from the resulting dropdown. The list of User Groups you can can choose from are defined in the [User Management section of Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/user-groups).&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQjtiA2uqrAM4aX3yFFlR%2Fimage.png?alt=media&#x26;token=1fcfc461-01a2-421f-a5ef-83d0fd91bbe6" alt=""><figcaption></figcaption></figure>

### 'Parent Work Item Owner' allocation method

This allocation method allocates work items to the owner of the parent work item. This allocation method is often used to ‘escalate’ Actions up to the Case owner.

### 'Parent Work Item Starter' allocation method

This allocation method allocates work items to the user who started the parent work item.

### ‘Username from Custom Data Field’ allocation method

This allocation method allocates work items to an individual based on the username supplied at runtime in a [custom data field](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration).

Simply select the desired Custom Data Field from the resulting dropdown.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNCpxDBnxsIZjvGA33kvG%2Fimage.png?alt=media&#x26;token=da32295a-7984-44fc-9c9c-d42e7c4bf0df" alt=""><figcaption></figcaption></figure>

### 'Work Item Starter' allocation method

This allocation method allocates a work item to the user who started the work item.

## Further Options

### Show Activity

Clicking on Show Activity button in the ellipsis will show you the activity history of the Allocation Flavour. You can see when the Allocation Flavour was created and by who, as well as if any edits have been made to the Allocation Flavour, when they were made and by who.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpx71IAzRCbzlPa40e%2Fimage.png?alt=media\&token=59526a6c-40c7-4ac5-9646-bd2b81571063)

### References - See where Allocation rule is used <a href="#completer-of-previous-action-allocation-method" id="completer-of-previous-action-allocation-method"></a>

Clicking on the 'References' tab of a flavour will show you where this Allocation rule is being used.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpxMX2duXW4rMmuju-%2Fimage.png?alt=media\&token=efe08a18-8feb-48c6-aa22-6e2238ebc1b9)
