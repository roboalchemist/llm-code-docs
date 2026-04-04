# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/user-management/robots.md

# Robots

## Overview

The Robots page, accessed via the User Management section of Builder, is where you can add, edit and manage your Robots. Robots are the account for RPA bots to let them interact with the system.

You can see a list of your existing Robots, and information such as their name, their farm and whether or not they are externally managed.&#x20;

You can customise the order in which you want to view your Robots by clicking on each column header.&#x20;

You can also use the search function at the top of the page.

{% hint style="info" %}
Please note that if a Robot is Externally Managed (e.g. it is managed via a different robotics platform such as UiPath Orchestrator), you will be able to see the Robot in this list, but you will not be able to modify any of its attributes directly in Enate.
{% endhint %}

## Creating a Robot <a href="#creating-a-robot" id="creating-a-robot"></a>

To add a new Robot, go to the ‘Robots’ page in Builder’s User Management section and click on the '+' icon at the top of the screen. This will bring up the ‘Add Robot’ pop-up where you can enter the person's details.

### General Settings

In the General tab you can add the following details:&#x20;

| Attribute          | Description                                                                    | Notes                                                                                                                                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Username           | Auto-generated username                                                        | This cannot be manually set, but is viewable here after robot creation. You can copy the Username by clicking on the copy icon.                                                                                            |
| First Name         | The robot’s name, for use when tracking in Work Manager                        | Mandatory                                                                                                                                                                                                                  |
| Total Capacity     | The number of working hours per day that the robot can work for.               |                                                                                                                                                                                                                            |
| Cost per Hour      | The cost of the Robot resources                                                |                                                                                                                                                                                                                            |
| Allowed Work Types | Whether the Robot is set to work on Live work items, Test work items, or both. |                                                                                                                                                                                                                            |
| Time zone          | The user’s local time zone                                                     | Mandatory                                                                                                                                                                                                                  |
| Calendar           | The working calendar for this user                                             | Mandatory                                                                                                                                                                                                                  |
| Farms              | The farm(s) this robot belongs to                                              | <p>Note that when linking a robot to a farm, you may need to create a new farm. See here for <a href="#adding-a-new-farm">more information</a>.</p><p></p><p>Note that a robot can belong to more than a single farm. </p> |

### Access Settings

Enate allows for a granular level of granting access to people based on their role and business requirements. These settings are defined in the Access tab. Here you mu choose which Builder role to assign to the robot by selecting from the dropdown menu. This determines which Builder role the user has and therefore which Builder features the user will have access to. User roles are configured in the User Roles section of User Management in Builder. Select either a standard or custom role from the dropdown.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FF65JlGL67RTb60O0WToi%2Fimage.png?alt=media&#x26;token=f78a1597-9122-462a-95ee-23b879f99140" alt=""><figcaption></figcaption></figure>

### Password <a href="#password-attributes" id="password-attributes"></a>

In the Password Tab you must set the Robot's password according to your password policy.

See here for more information about setting your password policy:

{% content-ref url="../system-wide-settings/password-policy" %}
[password-policy](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/password-policy)
{% endcontent-ref %}

## Adding a New Robot Farm <a href="#adding-a-new-farm" id="adding-a-new-farm"></a>

When linking a robot to a farm, you may need to create a new Farm. This can be done by clicking the link in the farm dropdown.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq-Pf1QM1544JFrMeJ%2F-MWq0Yj5Z0ZeLuVHTeuo%2Fimage.png?alt=media\&token=b9b88f4d-c5ae-4f01-88cc-e4419dcd0a28)

You will be presented with a popup where you can define the name of the farm, a description, and choose the technology which it uses (current options: UiPath, BluePrism, Automation Anywhere).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq-Pf1QM1544JFrMeJ%2F-MWq0b2xFjuvClpb6vUH%2Fimage.png?alt=media\&token=5eff3d76-6134-4343-a5ae-fd26338f23f8)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWq-Pf1QM1544JFrMeJ%2F-MWq09xZI02ADLsoo18a%2Fimage.png?alt=media\&token=7fd53c1d-6886-452f-87c0-ef3187fa6bfe)

## Editing a Robot <a href="#c-editing-an-existing-user-robot" id="c-editing-an-existing-user-robot"></a>

You can edit the details of an existing Robot by clicking on the menu link on the right-hand side of the contact.  All attributes can be modified with the exception of the Robot's username.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FanI4sSFpfKrIeTRB7CEr%2Fimage.png?alt=media&#x26;token=be53debb-c334-4d1d-bf86-a0609b2761d9" alt=""><figcaption></figcaption></figure>

You can also see what edits have been made to a Robot and when, as well as when the Robot was created, by clicking on the Show Activity button.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpzj3mH2sI6jQmFeHv%2F-MWq-Lf0x4KFSaVo-fCh%2Fimage.png?alt=media\&token=0b166090-f3f9-4d51-bd81-c42ea2f92449)

## Deleting a Robot

You can delete a Robot by clicking on the menu link on the right-hand side of the contact.

{% hint style="info" %}
Note: deleting a Robot is a logical delete only; the user account is effectively retired. The account can be [reactivated ](#reactivating-a-retired-user)at any point.
{% endhint %}

### Reactivating a retired Robot

You are able to reactivate or "undelete" retired Robots by activating the system-wide ‘[Show deleted items](https://docs.enate.net/enate-help/builder/user-dropdown#b-show-deleted-items)’ button. This will show you your retired Robots which will be greyed out in your grid. Clicking on the menu option of a retired user will shows you an option that allows you to reactivate that Robot and set them as active.

## Resetting a Robot's password

You can reset a Robot's password by clicking on the menu link on the right-hand side of the contact and selecting 'Change password'. You can then give them a password according to your password policy.

See here for more information about setting your password policy:

{% content-ref url="../system-wide-settings/password-policy" %}
[password-policy](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/password-policy)
{% endcontent-ref %}
