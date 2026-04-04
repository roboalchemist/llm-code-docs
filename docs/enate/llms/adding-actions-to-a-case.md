# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case.md

# Adding Actions to a Case

## What are Actions?

Actions are the constituent parts of a Case, i.e. a Case is made up of a flow of Actions.&#x20;

The Actions that you can add to a Case flow come from a standard menu of Actions, but can be added in any order.

You can add a variety of types of Actions - [see below for more details](#what-types-of-action-can-i-add).

Actions can be manual (i.e. can be carried out by humans and bots) or the can be automatic, e.g. auto sending an email.&#x20;

You can choose to add a set of instructions to an Action, often a checklist of activities, to track progress within the Action.&#x20;

All the manual Actions that are added to the process flow are shown under \[Action Info] tab, and you can configure their standard attributes there. Additionally, specific types of Action (e.g. Email and Peer Review) Actions have further attributes which are displayed in subsequent tabs in the same location. These will only display once you add an Action of that type to your flow.

## What types of Action can I add?

Depending on which Action types have been creating in your system, you can add the following types of Action:

* [ABBYY FlexiCapture Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/abbyy-flexicapture-action-info-tab-1) - these Actions provide integration with [ABBYY FlexiCapture](https://www.abbyy.com/flexicapture/)
* [Approval Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/approval-actions) - these Actions enable the creation of [approval request flows](https://docs.enate.net/enate-help/builder/builder-2021.1/approval-flows).&#x20;
* [Manual Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/manual-actions) - these Actions are carried out by humans or bots
* [Manual with Peer Review Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/peer-review-action-info-tab) - these Actions allow different members of a team to crosscheck each other's work. They involve two parts: the first part is the "doing" of the Action by one user, the second part involves reviewing to check if the Action was completed correctly - this review is done by a different user.
* [Send Email Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab) - these Actions involve the user sending out an email
* [Send Email and Wait Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/send-email-and-wait-actions) - these Actions involve the user sending an email and waiting for a response.
* [Start Case Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/start-new-case-action-info-tab) - these Actions&#x20;
* [Trigger External API Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/external-api-action-info-tab) - these Actions are used when you need to automatically call out to another system, passing data to it and potentially getting the external system to pass updated custom data back into Enate.&#x20;
* [Wait for Sub Cases to Complete Actions](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/hold-case-action-info-tab) - these Actions wait for a specific Sub-Case to reach completion before allowing the Case to move on to the next Action.

Action types can be configured in the Service Lines page, see this [article ](https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen/creating-new-action-types-in-a-service-line)for more details, or directly from within a Case screen itself.

## How do I add Actions to a Case?

If you need to add additional Actions to your Case, you can do this by:

1. [Adding an Action from a step](#adding-actions-from-a-step)
2. [Adding an Action from an existing Action](#adding-actions-from-an-existing-action)
3. [Adding an ad-hoc Action](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/adding-ad-hoc-actions)

### Adding Actions from a step

Clicking on the menu icon on the right of a Step will give you the option to:

* Add a Condition (click [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/case-conditionality)for more details)
* Add an Action in series
* Add a parallel Action

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWp_fQpjpz0j2866Jq0%2F-MWp_oTlvXsB0zqeePmy%2Fimage.png?alt=media\&token=bda31e83-3c84-4491-82f4-984619c78b02)

You then need to choose which Action you want to add to the flow

### Adding Actions from an existing Action

Clicking on the menu icon on the right of an Action will give you the option to:

* Delete the Action
* [Cut / copy / paste the Action](#copy-paste-actions-in-case-flow-configuration)
* Move the Action up or down within the Step flow
* Add further Actions, either before, after or parallel to the selected Action&#x20;

When adding an Action from another Action, you can choose to add an Action before, after or in parallel to the selected Action.

## How do I edit a Case Flow

Once you have added an Action, clicking on the menu icon on the right of it in the flow will give you the option to:

* Add further Actions, either before, after or parallel to the selected Action&#x20;
* Rearrange the order of Actions by moving the Action up or down within the same Step
* Merge multiple Actions - adding a new merged Action or editing an existing merged Action
* [Cut / copy / paste the Action](#copy-paste-actions-in-case-flow-configuration)
* Delete the Action

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FgUZ7eJPGiQMJBST9ODPP%2Fimage.png?alt=media&#x26;token=36d2fc58-036e-42da-a1d6-12fdc6f686a2" alt=""><figcaption></figcaption></figure>

### Copy/Paste Actions <a href="#copy-paste-actions-in-case-flow-configuration" id="copy-paste-actions-in-case-flow-configuration"></a>

You can also cut, copy and paste Actions within a Case Flow diagram.&#x20;

Selecting the Action to be cut/copied and pasted in the Flow Diagram will highlight the Action in the Grid below as well.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWp_fQpjpz0j2866Jq0%2F-MWpa-BgnbLGTZAng62n%2Fimage.png?alt=media\&token=0c1598b8-7357-4582-ae61-f46459dffb04)

{% hint style="info" %}
Note: this feature is only available within a single Case diagram. Copying or pasting between difference processes or systems is not currently supported.&#x20;
{% endhint %}

## How do I configure an Action's settings?

Clicking on an Action in the Case flow will open the Action Info tab in the info grid and highlight that particular Action in the grid.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpaP-7H9QReEXdkc06%2F-MWpaRYZ5F0ll-fqoltn%2Fimage.png?alt=media\&token=760c8fdf-e26f-41c5-b89b-17f49c44990c)

Here you can the configure the following settings for that Action:

| Setting               | Description                                                                                                                                                                                                                                    | Notes                                                                                                                                                                                           |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When is it due?       | Select a value from the dropdown menu of Due Date ‘flavours’                                                                                                                                                                                   | <p>Mandatory to set live.</p><p>(See <a href="../shared-standardised-settings-flavours/due-date-flavours">Due Date Flavours Settings</a> for more information).</p>                             |
| Who does it go to?    | Select a value from the dropdown menu of Allocation ‘flavours’                                                                                                                                                                                 | <p>Mandatory to set live.</p><p>(See <a href="../shared-standardised-settings-flavours/allocation-flavours">Allocation Flavours Settings</a> for more information).</p>                         |
| General Settings      | Select a value from the dropdown menu of Follow Up ‘flavours’                                                                                                                                                                                  | <p>Mandatory to set live.</p><p>(See <a href="../shared-standardised-settings-flavours/general-settings-flavours-action-only">General Settings Flavours Settings</a> for more information).</p> |
| Allow Manual Creation | Ticket to display the category as an option on Self Service submission forms. This allows you to show a subset of categories for end user submission.                                                                                          |                                                                                                                                                                                                 |
| Main Card             | Custom Data for this Case can be displayed on the Case screen at runtime.                                                                                                                                                                      | Select the Custom Card to be used for displaying this data in the main section of the Case screen.                                                                                              |
| Side Card             | Custom Data for this Case can be displayed on the Case screen at runtime.                                                                                                                                                                      | Select the Custom Card to be used for displaying this data in the right hand side panel section of the Case screen.                                                                             |
| Manual Creation       | Ticking this will make the Action an ad hoc Action that appears in the Case flow. See [here ](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/adding-ad-hoc-actions)for more information. |                                                                                                                                                                                                 |
| Checklist             | See [here](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/checklists-on-actions) for more information.                                                                                   |                                                                                                                                                                                                 |

Different types of Action might require additional settings. These can be added in the additional tabs that will appear when these Actions are added to the flow. See [here ](#what-types-of-action-can-i-add)for more information.

### Copy/Paste Data

In every tab in the Info Section apart from the Case tab, you can copy and paste data to make configuring attributes quicker and easier.

You can select data from multiple cells and paste that data into selected destination cells.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FgFuiyfgQH6hi0iOYo1F1%2FCopy-and-Paste.gif?alt=media\&token=2a2f75a1-5b6f-4070-863b-0b20c1ac893d)

{% hint style="info" %}
Please note that you cannot copy and paste data between columns.&#x20;
{% endhint %}

If you want to copy more that one cell from multiple columns, you must make sure to copy the same number of cells from each column:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCAeTYcgL1YJUELsavDfb%2FCopy-And-Paste-2-cells.gif?alt=media\&token=099d13ad-acfa-404b-9985-d67a5a4eef61)

If the number of cells you select to paste data to is more than the number of cells you have copied, the data you have copied will repeat itself to fill the highlighted cells.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpqGWiZlbFRDZa5Z950Pb%2FCopy-Paste-too-many.gif?alt=media\&token=af00bcf1-8b94-4f05-9b76-50270fafcad9)

If the number of cells you select to paste data in is less than the number of cells you have copied, you will only paste data to fill the highlighted cells i.e. if you copy the data from 4 cells but select to paste that data into 3 cells, then only the data from the first 3 cells you copied will be pasted.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXMNR83uLcB7Oi1lxRCmD%2FCopy-Paste-too-few%20\(1\).gif?alt=media\&token=3e951cfd-4bf4-44f2-b514-3ca8ae12c36b)

If you select to paste data into multiple places, the data that is pasted will begin from the start of the first cell you copied.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F78dbnK6NL1JcahSFh8IE%2FCopy-Paste-Multiple-Locations.gif?alt=media\&token=9716132e-5fb4-4590-b459-4f593961f9bd)

The data from the first cell you select will be pasted first:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVS2BtC4fxyX5WYaMnAYc%2FCopy-Paste-Order.gif?alt=media\&token=cca46511-c17b-4834-9c05-8a9cb4559663)
