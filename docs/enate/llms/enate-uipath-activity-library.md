# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/uipath/enate-uipath-activity-library.md

# Enate UiPath Activity Libraries

## Enate UiPath Activity Library - Overview

The Enate Workflow Activity Library allows easy integration with Enate’s enterprise workflow engine. It allows bots to get work from the Enate platform, edit the data, add or download files and update the Enate platform.  We can also create new work items on the Enate platform using the activities.

The .Net Workflow Activity library allows easy integration with Enate v2021.1 and above. The Activities will perform authentication when necessary and allow a single authentication token to be passed between concurrent calls to improve performance.

Authentication will be done through the Authenticate Activity. This will return an Authentication Token which can then be passed to the other Enate Activities.

All date/time values are passed in UTC and each Enate Activity has a standard set of 4 arguments:

* **PlatformURL (String)** - This should be set to the URL of your Enate instance, as you would type in a portal to get to the login page. e.g. <https://hosting.enate.net/MyInstance>
* **Username (String)** - Any valid Username for your Enate instance. Only required if AuthenticationToken is not set or has expired.
* **Password (String)** - The current Password for the user account specified in Username. Only required if AuthenticationToken is not set or has expired.
* **AuthenticationToken (String)** - After an initial call to an Activity has succeeded its authentication token can be reused if the next call is made within the configured timeout window. The timeout is configured per customer instance so please check your token validity duration with Enate Support.

{% hint style="info" %}
**Note: Username/Password has been removed from all activities except Authenticate\***\
Username/Password has now been removed from all activities and you now need to use the Authenticate Activity to get an Authentication Token, which can then be passed to the other activities.  This change was required for the “SwitchToLive/SwitchToTest” activities as they rely on the token.
{% endhint %}

Each successful Activity will output a new AuthenticationToken that resets the timeout window.

All activities can be found in the **Activities panel, under Enate > Workflow > Activities**.

These activities enable you to build complex rules for interacting with the Enate platform combining them with UiPath’s built-in functionality for **if/else** or **switching** to make conditional decisions for powerful workflows.

You can find all of Enate's Activity Libraries in the sections below, as well as explanations of each of the activities available.

Check out the [setting up the Enate Activity Library in UiPath Studio](#2.-setting-up-the-enate-activity-library-in-uipath-studio) section which details how to install this file in UiPath Studio to get access to Enate's dedicated Activity library.

## Latest Enate Activity Library

### Activity Library v1.3.3

Changes made as part of this release is:

* Fixed a bug related to  CreateCase and CreateSubCase Activities.

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FscHeqrHObTPpDTDXKQNZ%2FEnate%20UiPath%20Activity%20Library%20V1.3.3.pdf?alt=media&token=1903d241-2c44-4a36-8ab8-bb60c6a1afac>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FoKlCvXjMa5PWqAYYMUo7%2FEnate.UiPath.Activities.1.3.3.nupkg?alt=media&token=efbdf9ec-77cd-4ec0-a34d-c1b50ceac7b4>" %}

### Activity Library v1.3.1

In this version we have fixed the CreateCase and CreateTicket activities to add Service Agents contact while creating Case or Ticket - Previously while creating a Ticket or Case We were allowing only external contact to be added whereas Now users should be able to add service agent contact and external contacts as well.

{% hint style="info" %}
This version of the UiPath package only works with version 2023.5 and above of Enate.
{% endhint %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FX6LRKPml8CFqVF0zzhX7%2FEnate%20UiPath%20Activity%20Library%20V1.3.1.docx?alt=media&token=53005d74-db10-4548-90cb-72033364332f>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fa8opzIPnasxesd2ZZW72%2FEnate.UiPath.Activities.1.3.1.nupkg?alt=media&token=d166adae-5882-4dbc-aa9e-efca0f45427c>" %}

### Activity Library v1.2.19

This release focuses on supporting workflows in Windows Legacy which is in sync with the release of version 2024.1 of Enate. In this version, we have fixed the CreateCase and CreateTicket activities to add Service Agents' contact while creating a Case or Ticket.

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fmcvk81WXvXwdazCA5aZr%2FEnate%20UiPath%20Activity%20Library%20V1.2.19.pdf?alt=media&token=ea7415fd-5f2f-4d3e-9555-925d0e50cce3>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPdkEPUOCc8xMdexsXjcY%2FEnate.UiPath.Activities.1.2.19.nupkg?alt=media&token=ad4eaa8c-361d-4d48-a9e1-96707ee4911b>" %}

This version of the UiPath package only works with version 2024.1 and above of Enate and is the final release for Windows Legacy Previous Activity Libraries

## Previous Activity Library

### Activity Library v1.3.0

This release focuses on upgrading workflows from Windows Legacy to Windows.

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fn2HmYF6ZJA9VDldQPhw9%2FEnate%20UiPath%20Activity%20Library%20V1.3.0%20.docx?alt=media&token=2c11907a-8e8c-4fc3-83da-a533c39f9af1>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/UiPath/Enate.UiPath.Activities.1.3.0.nupkg>" %}

### Activity Library v1.2.18

In this release we have updated the GetCommunications and SendEmailCommunication activities to align with the updated APIs in Enate following the most recent product release.

{% hint style="info" %}
This Version of the UiPath Package only works from 2022.5 to 2023.5 of Enate
{% endhint %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FWF5lUI9JiwPfp1nhKyXU%2FEnate%20UiPath%20Activity%20Library%20V1.2.18.docx?alt=media&token=662a924e-ca1b-41e5-b54d-8609e6625854>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/UiPath/Enate.UiPath.Activities.1.2.18.nupkg>" %}

### Activity Library v1.2.13

In sync with the release of [version 2022.5](https://docs.enate.net/whats-new/2022.5/2022.5-changes-overview) of Enate and the customer GUID field in the /Packet/GetContexts API being made mandatory, the GetTicketProcess, GetCaseProcess, GetCaseProcesses and GetCaseAttribute activities have been updated.

Note that the GUI for the GetCaseProcess activity is yet to be finalised, but users can still enter property fields in the Properties window on the right.

Also note that for the GetCaseProcesses activity, the Customer Name property has now been made mandatory.

{% hint style="info" %}
This version of the UiPath package only works with version 2022.4 and above of Enate.&#x20;
{% endhint %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fsc9j2W8hafpOGNCVQVDe%2FEnate%20UiPath%20Activity%20Library%20V1.2.13.docx?alt=media&token=62c0bc67-baef-4d39-9ec4-bbbf674d2daa>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/UiPath/Enate.UiPath.Activities.1.2.13.nupkg>" %}

### Activity Library v1.2.8

You can download the **Enate UiPath Activity Library v1.2.8** from the links below. In this version we have improved saving work item communication attachments. Previously when saving an email attachment, if a special character(s) was present in the file name, the special character(s) would be replaced by an empty space upon saving. Now when saving email attachments with special character(s) in their name, the name of the file is not changed - the special character(s) are included.

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FuPGNmtehMpKFg923tr3P%2FEnate%20UiPath%20Activity%20Library%20V1.2.8.pdf?alt=media&token=0c97d7bc-e1a0-4677-af3c-189eabdf55f7>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/UiPath/Enate.UiPath.Activities.1.2.8.nupkg>" %}

### Activity Library v1.2.5

In this version we have added a new field in the CreateCase and CreateTicket activities called **‘**&#x44;o Not Send Automated Emails’. When the Boolean value is set to True, the request acknowledgement email will not be triggered/sent. When the Boolean value is set to False or the field is left empty,  the request acknowledgement email will be triggered/sent.

{% hint style="info" %}
**Note:** the **‘**&#x44;o Not Send Automated Emails’ field in the CreateCase activity will only work in Enate versions of 2022.4 and above. However, the **‘**&#x44;o Not Send Automated Emails’ field in the CreateTicket activity will work in Enate versions of 2021.1 and above.
{% endhint %}

You can download the **Enate UiPath Activity Library v1.2.5** from the links below.&#x20;

{% embed url="<https://media.enate.net/Integrations/RPA/UiPath/Enate.UiPath.Activities.1.2.5.nupkg>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3Sx46f6bXjjamPf0B7n3%2FEnate%20UiPath%20Activity%20Library%20V1.2.5.docx?alt=media&token=87d2cfdd-049e-40b8-bca4-a339839e4a47>" %}

### Activity Library v1.1.9

Below is a copy of the Enate UiPath Workflow Activity Library for v1.1.9. In this version we have fixed the ‘AttachFile’ activity - previously it was mandatory when attach a file to a work item for the file to have a file tag whereas now users are able to attach a file to a work item with or without a file tag.

{% embed url="<https://media.enate.net/Integrations/RPA/UiPath/Enate.UiPath.Activities.1.1.9.nupkg>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3Ypjia7oQARXFvuUSEnq%2FEnate%20UiPath%20Activity%20Library%20V1.1.9.docx?alt=media&token=8ab69685-48dd-4079-a72b-f941d4621de2>" %}

### Activity Library v1.1.8

Below is a copy of the Enate UiPath Workflow Activity Library for v1.1.8.  In this version we have added the Nito.AsyncEx library within the latest UiPath package so that you no longer need to add it manually.

{% embed url="<https://media.enate.net/Integrations/RPA/UiPath/Enate.UiPath.Activities.1.1.8.nupkg>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fr7mtLY9YTO0OCgpaahiY%2FEnate%20UiPath%20Activity%20Library%20V1.1.8.docx?alt=media&token=84b36b22-b5e8-412f-a51e-15f50e8893fc>" %}

### Activity Library v1.1.4

Below is a copy of the Enate UiPath Workflow Activity Library for v1.1.4:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeksbdanYxdC9BVO8fHqQ%2FEnate%20UiPath%20Activity%20Library%20V1.1.4.pdf?alt=media&token=8bb5f8a8-ce0f-461d-bb85-9f877c6c5103>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/Enate.UiPath.Activities.1.1.4.nupkg>" %}

### Activity Library v7.3.12

Below is a copy of the Enate UiPath Workflow Activity Library for v7.3.12:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8orMihn26kLOlEmnBJbS%2FEnate%20UiPath%20Workflow%20Activity%20Library%20v7.3.12.docx?alt=media&token=fce18544-c5ab-4c5c-9b77-3ae1770ecd6c>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/UiPath/Enate.Workflow.Activities.7.3.12.nupkg>" %}

### Activity Library v7.3.10

Below is a copy of the Enate UiPath Workflow Activity Library for v7.3.10:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FC2JGPNe0VcvIH3NdAfSK%2FEnate%20UiPath%20Workflow%20Activity%20Library%20v7.3.10.docx?alt=media&token=ea16876e-77d0-4312-b2bb-a34244a08a4e>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/UiPath/Enate.Workflow.Activities.7.3.10.nupkg>" %}

### Activity Library v7.3.7

{% hint style="info" %}
**The library has been updated to match all the DTO’s in v2021.1 of Enate - you’ll need to use this updated activity library to be compatible with this latest version of Enate**
{% endhint %}

Below is a copy of the Enate UiPath Workflow Activity Library for v7.3.7:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MkMOzI4ckxa5nZ5N2ri%2F-MkMPVjrdSUL6wiuZ7xa%2FEnate%20UiPath%20Workflow%20Activity%20Library%20v7.3.7.docx?alt=media&token=f9e1a1ae-8c9f-46f8-9c67-a1cbe8eda59c>" %}
Enate UiPath Workflow Activity Library v7.3.7
{% endfile %}

{% embed url="<https://media.enate.net/Integrations/RPA/Enate.Workflow.Activities.7.3.7nupkg>" %}

Enate UiPath Connector v7.3.7 works best with v2021.1.

The key updates for this connector are:&#x20;

* Ability to add file tags and contact tags to Cases and Tickets
* Ability to launch a Case linked to a Schedule
* Ability to launch ad-hoc Actions
* Ability to extracting communications and saving the communication attachments locally
* Ability to attaching files to Cases, Tickets and Actions

In v2021.1 bots can access Builder APIs to get contact tags, file tags etc. To enable this:

Edit the bot in User management

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MkM8M2xlRzINsxc8JQu%2F-MkMNYJ9XjFhZzuSiR5r%2Fimage.png?alt=media\&token=968c27d5-664e-48fb-9d28-c363f28315bc)

Update the bots access permissions and save

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MkM8M2xlRzINsxc8JQu%2F-MkMNZwrizZbuSln0jpt%2Fimage.png?alt=media\&token=a2fcfa83-ab0e-4183-a4af-cc31602bf58d)

### Activity Library v7.2.10

Below is a copy of the Enate UiPath Workflow Activity Library for v7.2.10:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWjir_C75752ZA2nL01%2F-MWjkfC4w1ifsLupGs60%2FEnate%20UiPath%20Workflow%20Activity%20Library%20v7.2.10.docx?alt=media&token=31767599-bf4b-4165-8229-23c67d5a74a8>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/Enate.Workflow.Activities.7.2.10.nupkg>" %}

### Activity Library v7.2.9

Below is a copy of the Enate UiPath Workflow Activity Library for v7.2.9:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIuEUJ2b0PftSoCVoEAbh%2FEnate%20UiPath%20Workflow%20Activity%20Library%20v7.2.9.docx?alt=media&token=01a8929c-25f3-4723-90fc-1756f0b8a52f>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/Enate.Workflow.Activities.7.2.9.nupkg>" %}

### Activity Library v7.1.1

Below is a copy of the Enate UiPath Workflow Activity Library for v7.1.1:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPWlqiyhPfkZyQvBoP9av%2FEnate%20UiPath%20Workflow%20Activity%20Library%20v7.1.1.docx?alt=media&token=d845e03b-41f1-45d2-9f6a-5b72532fef6b>" %}

{% embed url="<https://media.enate.net/Integrations/RPA/Enate.Workflow.Activities.7.1.1.nupkg>" %}
