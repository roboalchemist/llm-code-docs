# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/linking-a-schedule-to-a-case.md

# Linking a Schedule to a Case

Once you have [created a schedule](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules/creating-a-schedule), you can start to make use of the schedule information when configuring a Case process. To do this, you can:

* [Link the Case process to a specific Schedule](#linking-schedules-to-case-processes-in-builder)
* [Link its Steps to a date from within that Schedule](#linking-schedule-structure-dates-to-steps)
* [Create due date rules which reference dates within the Schedule](#setting-a-due-date-which-references-a-schedule-date)

Check out this explainer video for how to link schedules to Case processes in Builder or read the information below.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MjcyMw==>" %}

## Linking Schedules to Case Processes in Builder

To link a schedule to a Case process, open the Case screen in Edit mode and select the desired schedule from the ‘Schedule’ dropdown in the Case Info Screen.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWptJC91nVQmbMNI2xS%2Fimage.png?alt=media\&token=134266a4-0514-497f-8e5b-a8e962ef1689)

If you want the Cases to be automatically startable based on this schedule, set the 'Auto Start By Schedule' option to on.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWptMQJypK032clPtih%2Fimage.png?alt=media\&token=075116bb-9216-422b-a813-2a4969598f43)

## Linking Schedule Structure Dates to Steps

The next activity available is to link the steps of the Case to the schedule so they reference one of the dates in the schedule. To do this, click the schedule icon in the steps running along the top of the Case flow diagram and select the date you want to like the step to.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWptRqomrpZ1VB3b8FF%2Fimage.png?alt=media\&token=07ec4eea-86d5-4870-ba44-502c26784b92)

## Setting a Due Date which References a Schedule Date

There are two options when it comes to creating due date rules that reference a schedule date:

* [Use a due date method that directly references one of the schedule dates](#reference-an-explicit-schedule-date)
* [Use a due date which references the Step due date](#reference-the-step-date)

### **Referencing a Schedule Date**

To set a due date that directly references a schedule date, when [defining a new due date option](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours) select a [Due Date Method](https://docs.enate.net/enate-help/builder/shared-standardised-settings-flavours/due-date-flavours#due-date-methods) of ‘From Explicit Schedule Date’, and then select which of the schedule dates you wish to reference.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWptawKujKUxtRbprj2%2Fimage.png?alt=media\&token=d5b96941-bd4e-4c92-bf1c-f298be18a2f6)

As with any other due date rule, you can define a +/- offset of days (and hours) from the date referenced in order to reach the precise due date/time desired for the Action.

### **Referencing a Step Date**

You can set a due date that references the due date of a Case step by creating a [due date rule](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours) for the step due date e.g. ‘2 days before Step Due Date’. This gives you the flexibility of subsequently modifying the schedule date you have linked to the step without having to reconfigure your due dates.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpth-CNh1YPDVQ-8J7%2Fimage.png?alt=media\&token=bbb13d93-fa70-4ca9-bad3-c13a1764a2aa)

{% hint style="warning" %}
Validation point to note: If you use a due date rule in an Action which references the step due date, but you have not [linked that step to any schedule date](#linking-schedule-structure-dates-to-steps), you will receive a validation message on saving the Case process and will not be able to set the Case live until you have resolved the issue.
{% endhint %}

## Viewing Cases Linked to a Schedule

The 'Show Case Process Linked to Schedule' icon in the Schedules page lets you see the list of all the Case processes which are linked to a schedule.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_QeGLM1Ii0Mq5a3ySL%2F-M_QklhSoemw1hgpGYa9%2Fimage.png?alt=media\&token=5acfa8c6-f545-43dc-b7ec-d2241919b013)

It shows you the Customer, Contract and Service of the Case, as well as what state the Case is in, such as Live, Testing and Draft. If the schedule is linked with more than one version of a Case, then all versions will be shown in the list. You are also able to filter the list of Cases by Customer, Contract, Service and State.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_QeGLM1Ii0Mq5a3ySL%2F-M_QknULWWOtlRUkdbSX%2Fimage.png?alt=media\&token=73f58849-dac4-43c4-b3e7-9b92ac22ae80)

Clicking on the Case process will take you to the Case screen for that particular Case.&#x20;

{% hint style="info" %}
Note: You will be taken to the latest version of the Case screen, regardless of which version of the Case process is linked to the Schedule. However you can choose which version of the Case process you see once you are in the Case screen.&#x20;
{% endhint %}

The Linked Processes list will also show retired process versions if the '[Show Deleted Objects](https://docs.enate.net/enate-help/builder/user-dropdown#b-show-deleted-items)' option is switched on.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M_QeGLM1Ii0Mq5a3ySL%2F-M_QktAMizCmsJAaguoo%2Fimage.png?alt=media\&token=d00e14d4-2b72-463b-b7e7-84e33d805e82)
