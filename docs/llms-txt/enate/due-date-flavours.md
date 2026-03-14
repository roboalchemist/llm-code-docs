# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours.md

# Due Date Flavours

## Overview

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2Mjc0NQ==>" %}

In addition to Name and Description, Due Date flavours are made up of the following attributes:

| Setting                            | Description                                                                                                                                                                                                                                                                                                          |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Due Date Method                    | Various standard methods of calculating a due date can be selected from, Depending upon the method selected, additional parameters may be required, e.g. a specific schedule. See here for [more information about Due Date Methods](#due-date-methods).                                                             |
| Adjust by                          | Add or subtract a specified number of hours/working hours/day/working days (including minutes) from the starting date determined by the Due Date method selected, e.g. the Case start date.                                                                                                                          |
| Advanced                           | If set, further options are available (see following section)                                                                                                                                                                                                                                                        |
| Calendar                           | <p>If using working days / hours, you need to specify which calendar to use for the calculation. This can either be the supplier / customer calendar linked to the contract (there must be one if you select this option), or a standard system calendar.</p><p><em>Relevant only for working hours / days.</em></p> |
| Add Wait Time To Due Date          | If set, stops the SLA clock whenever the item is put into a waiting state.                                                                                                                                                                                                                                           |
| Move To Next Morning If End Of Day | If set, once the due date/time has been calculated, the time will be pushed to the first working moment of the following working day *(This allows you to set a calculated Due Date of '5pm Friday' to be  '9am Monday', assuming working calendars are set accordingly).*                                           |
| Move To End Of Day                 | If set, once the due date/time has been calculated, the time will be pushed to the end of the calculated day.                                                                                                                                                                                                        |

Clicking on Show Activity button in the ellipsis will show you the activity history of the Due Date Flavour. You can see when the Due Date Flavour was created and by who, as well as if any edits have been made to the Due Date Flavour, when they were made and by who.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpwHHWmCN7HWxbq-J3%2Fimage.png?alt=media\&token=7e971b21-7ca4-4d61-b7b0-13676b7d4b3c)

## Due Date Methods

There are several Due Date Methods available which allow you to set the start point for calculating the desired SLA for an activity. There are more Due Date methods available.

### Ticket Due Date Methods

Watch the following video to find out about the due date methods that re available when configuring Tickets:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2Mjc0OA==>" %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXvxxcpCGRLBZD8KzJPIF%2Fimage.png?alt=media&#x26;token=d46f23f1-77d0-4b83-ac7e-f0100a9beb0c" alt=""><figcaption><p>Ticket Due Date Methods</p></figcaption></figure>

| **Method**                                       | **Notes / Further Variables**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First Day of Current Month                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Fixed Day of Current Month                       | Set a specific day, e.g. ‘14’                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Fixed Day of Fixed Month                         | Set a specific day and month, e.g. ‘14’ and  ‘3’. Please note that if the month and day configured using a 'Fixed day of fixed month' due date method on a Case/Action/Ticket is earlier than the work item's start date, then the system will assume that the Case/Action/Ticket is due in the following year. For example, if the fixed day of fixed month value configured in the due date of a Ticket is 14th March 2022 but the Ticket's created/start date is 16th July 2022, then the system will assume that the Ticket's due date will be 14th March 2023.                    |
| Fixed Day of Fixed Month of Work Item Start Year | <p>Sets a specific day and month and year. The year is calculated as the year the work item was started.</p><p>It is different to the already existing 'Fixed Day of Fixed Month' due date method as it will set the due date of the work item as the same year as when the work item get started. For example, if a Ticket's due date is 14th March 2022 but the Ticket gets started on 16th July 2022, then the system will assume that the Ticket's due date is the same year as when the Ticket was started, so it will assume that the Ticket's due date is 14th March 2022. </p> |
| From a Custom Date Time Field                    | If any field of type Date Time is linked to the work item configuration, you can select it here. At run time, when this value is set / changed, the Due Date will be calculated.                                                                                                                                                                                                                                                                                                                                                                                                       |
| From Packet Start Date                           | The date the Ticket was first created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Initial Request Date                             | If a further work item has been created from an original request (when a Sub Case is created, when a Ticket is converted into a Case, when a Case or Action gets reworked, when an Action is created via the 'Start Action' option or when a new linked work item is created), this due date method captures the start date of the original request, allowing you to capture the entire length of time it has taken to complete a request, as opposed to just the length of time an individual work item has been being worked on.                                                     |
| Last Day of Current Month                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### Case & Action Due Date Methods

Additional Due Date methods are available when setting Due Dates for Cases and Actions, as schedules and parent work item / sub-work items data can be used. Watch this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2Mjc1Nw==>" %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F2PqvB17Ad5Ybropjfxum%2Fimage.png?alt=media&#x26;token=1af51f34-9603-42f2-bddc-b7cde5ef858b" alt=""><figcaption><p>Case Due Date Methods</p></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FV3vzBiwYMywi8pkCJVxQ%2Fimage.png?alt=media&#x26;token=abdf26e7-8096-45a8-9b2e-86bf11601f13" alt=""><figcaption><p>Action Due Date Methods</p></figcaption></figure>

| **Method**                                       | **Notes / Further Variables**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First Day of Current Month                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| First Day of Month from Explicit Schedule Date   | Requires a Schedule linked to the Case. Supply a Schedule Date, e.g. “Key Date 1”, “Key Date 2” etc. from the dates list.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Fixed Day of Current Month                       | Set a specific day, e.g. ‘14’                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Fixed Day of Fixed Month                         | Set a specific day and month, e.g. ‘14’ and  ‘3’. Please note that if the month and day configured using a 'Fixed day of fixed month' due date method on a Case/Action/Ticket is earlier than the work item's start date, then the system will assume that the Case/Action/Ticket is due in the following year. For example, if the fixed day of fixed month value configured in the due date of a Case is 14th March 2022 but the Ticket's created/start date is 16th July 2022, then the system will assume that the Case's due date will be 14th March 2023.              |
| Fixed Day of Fixed Month of Work Item Start Year | <p>Sets a specific day and month and year. The year is calculated as the year the work item was started.</p><p>It is different to the already existing 'Fixed Day of Fixed Month' due date method as it will set the due date of the work item as the same year as when the work item get started. For example, if a Case's due date is 14th March 2022 but the Case gets started on 16th July 2022, then the system will assume that the Case's due date is the same year as when the Case was started, so it will assume that the Case's due date is 14th March 2022. </p> |
| From a Custom Date Time Field                    | If any field of type Date Time is linked to the work item configuration, you can select it here. At run time, when this value is set / changed, the Due Date will be calculated.                                                                                                                                                                                                                                                                                                                                                                                             |
| From an Explicit Schedule Date                   | Requires a Schedule linked to the Case. Supply a Schedule Date, e.g. “Key Date 1”, “Key Date 2” etc. from the dates list.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| From Packet Start Date                           | <p>The date the Work Item was first created. <strong>Important note:</strong> for Actions this means this would be from the beginning of the Action, not its parent Case.<br> If you wish to drive an Action’s Due Date from the Case, use ‘From Parent Packet Start Date’.</p>                                                                                                                                                                                                                                                                                              |
| From Parent Packet Due Date                      | For Actions, the date its parent Case is Due                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| From Parent Packet Start Date                    | For Actions, the date its parent Case started                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| From Schedule Date Linked to Step                | Requires a Schedule linked to the Case. Requires a Schedule Date e.g. “Key Date 1”, “Key Date 2” etc. from the dates list to be set for the Step this Action appears in.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Initial Request Date                             | If a further work item has been created from an original request (when a Sub Case is created, when a Ticket is converted into a Case, when a Case or Action gets reworked, when an Action is created via the 'Start Action' option or when a new linked work item is created), this due date method captures the start date of the original request, allowing you to capture the entire length of time it has taken to complete a request, as opposed to just the length of time an individual work item has been being worked on.                                           |
| Last Day of Current Month                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Last Day of Month from Explicit Schedule Date    | Requires a Schedule linked to the Case. Supply a Schedule Date, e.g. “Key Date 1”, “Key Date 2” etc. from the dates list.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Advanced Options for Due Date Settings <a href="#b-advanced-options-for-due-date-settings" id="b-advanced-options-for-due-date-settings"></a>

### Adjust Days / Hours by Numeric Custom Field Value <a href="#adjust-days-hours-by-numeric-custom-field-value" id="adjust-days-hours-by-numeric-custom-field-value"></a>

An advanced option has been enabled for Due Date rules which allows for the use of Custom Data variables when setting time adjustments. Enabling the Advanced option when setting a Due Date rule will display an additional set of options in the ‘Adjust by’ section.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FU75Z4Yz9SOvIy6RtgTQL%2Fimage.png?alt=media&#x26;token=4f0b0654-3c4a-4c44-ba07-f978ed725098" alt=""><figcaption></figcaption></figure>

This will allow you to add / subtract a certain number of Hours/Days/Working Hours/Working Days by selecting from a dropdown of numeric custom data fields.

### The 'Custom Data Time Field' Due Dates Method <a href="#the-custom-data-time-field-due-dates-method" id="the-custom-data-time-field-due-dates-method"></a>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeJNbi6cyUzRcMggEjfsK%2Fimage.png?alt=media&#x26;token=d9fd62d7-32f5-4a86-88c9-7cee8891ba2b" alt=""><figcaption></figcaption></figure>

The due date method **‘From a Custom Date Time Field’** allows configuration of rules which allows end users to supply the base date/time value for the Due Date for the rule via a custom data field at runtime, when submitting a Case or Action. The custom field must be of type ‘DateTime’.

#### **Prerequisites** <a href="#prerequisites" id="prerequisites"></a>

* At least one Enate custom data field specifically of the *date time* type.
* An Enate Custom Card must be configured with the aforementioned data field.
* This card must be configured on the specific Action or Case you wish to set this rule for.

{% hint style="info" %}
Please note: If a value for the field is not specified, the system will use the default value set on the custom data field in its place. This could be because the user does not fill in a value, or the field does not exist on the Work Item’s custom card.
{% endhint %}

The end result of this functionality is to allow direct adjustment of Work Item due dates by modifying custom data field values, i.e. setting a value on a card..

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpw_dzZh25drnkvL-m%2Fimage.png?alt=media\&token=c191593d-c81f-4665-b8b4-97c0ccab092f)

..modifies the Work Item due date:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpwcNT7kn-yRnS2EhT%2Fimage.png?alt=media\&token=9f1e0784-d2b1-4629-9935-20fb6850b300)

### Calendar <a href="#move-to-next-morning-if-end-of-day-setting" id="move-to-next-morning-if-end-of-day-setting"></a>

This is only available when a unit of 'working hours' or 'working days' has been selected.

### ‘Move to Next Morning if End Of Day’ setting <a href="#move-to-next-morning-if-end-of-day-setting" id="move-to-next-morning-if-end-of-day-setting"></a>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FajsgzJ8nAjEcU4A5arnO%2Fimage.png?alt=media&#x26;token=42349485-f477-48dd-b136-d8d64507f5dd" alt=""><figcaption></figcaption></figure>

If this flag is set, whenever the due date calculation results in a value that would have been the very end point of a working day (e.g. Friday 5pm when a 9-5pm working calendar is in play), the system will instead return a value for the first working moment of the *following* working day e.g. Monday 9am.

This option is only available when a unit of 'working hours' or 'working days' has been selected.

### ‘Move to End of Day’ setting <a href="#move-to-end-of-day-setting" id="move-to-end-of-day-setting"></a>

Due Date method configuration includes a ‘Move to End of Day’ setting. When checked, the system will take the relevant date calculated based upon the rule’s settings, e.g. ‘add 5 working hours to start date’), and will set the due date to be the end of that working day.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkKQeENahoeuW6HXdQBUB%2Fimage.png?alt=media&#x26;token=af3062ae-509d-442d-96d5-5bd59432051c" alt=""><figcaption></figcaption></figure>

For example, if the system calculates a due date of ‘11am’ on a particular day, clicking this attribute automatically shifts the value to end of that working day. The sequence of the logic here is important when understanding how date / time values are arrived at with this method. The logic sequence is as follows:

1. Run the "method"
2. Adjust by fixed (working) days/hours
3. Adjust by dynamic (working) days/hours
4. Add wait time if the option is selected (and if wait time exists).
5. If using working time then ensure the result is within working hours - moving to the start of the next working day if precisely at the end of a working day
6. Finally move to the end of the (working) day if selected.

This option is only available when a unit of 'working hours' or 'working days' has been selected.

{% hint style="info" %}
Note: "Move to Next Morning if End of Day" and "Move to End of Day" are mutually exclusive.
{% endhint %}

## References - See where Due Date rule is used <a href="#c-references-see-where-due-date-rule-is-used" id="c-references-see-where-due-date-rule-is-used"></a>

Clicking on the 'References' tab of a flavour will show you where this Due Date rule is being used.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpv3TCDYg2A_ocQW_M%2F-MWpwwrMVOylSKPRbJwM%2Fimage.png?alt=media\&token=40eac070-16c0-423d-a83b-510520119d88)
