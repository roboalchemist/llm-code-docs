# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen/creating-new-case-types-in-a-service-line.md

# Creating New Case Types in a Service Line

## Creating a new type of Case <a href="#a-creating-a-new-type-of-case" id="a-creating-a-new-type-of-case"></a>

You are able to create new types of Cases within a Service Line itself by clicking on the '+' icon next to the search bar and selecting 'Case'.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWowRyqtjfOiBDs_cLN%2F-MWowZJdyEkksHrmtGLq%2Fimage.png?alt=media\&token=1f03de64-a2d2-4a8b-81b2-3f6bfba030e8)

When creating a new type of Case, you can enter the following information:

<table data-header-hidden><thead><tr><th width="328">Attribute</th><th>Description</th></tr></thead><tbody><tr><td>Attribute</td><td>Description</td></tr><tr><td>Name</td><td>The name of the new type of Case</td></tr><tr><td>Description</td><td>The description of the new type of Case</td></tr><tr><td>Process Groups</td><td>Defining a Process group helps you sort your Cases on the Service Matrix Screen. See <a href="../service-matrix-screen/grouping-of-cases-in-a-service-line">here </a>for more information. </td></tr><tr><td>Make Contacts Mandatory</td><td>This controls whether Users need to enter a Primary Contact and a Requester when filling in details for a Case. It is unticked by default, making the addition of Contact information not mandatory. In order to make contact information mandatory for this type of Case, just tick this box. Additionally, ticking the 'make Contacts Mandatory' setting makes it mandatory to include a contact when launching a <a href="../../../../work-manager/work-manager-2021.1/processing-a-case/activities-available-for-case#starting-a-sub-case-independent-case-from-an-existing-case">Sub Case from an existing Case in Work Manager</a>. </td></tr><tr><td>Initial Estimated Effort Per Record</td><td>Established the estimated time it will take a Work Manager user to complete this Case.</td></tr><tr><td>Steps</td><td>Globally agreed steps a Case will run through every time that Case type is run. For all customers which use this Case type, these high level steps that run for each Case are the same, although the Actions that run within the steps them might differ.</td></tr><tr><td>Enable Record Count</td><td>Enables Work Manager users to use the Record Count for this Case.</td></tr><tr><td>Record Count Description</td><td>This only appears if Enabled Record Count has been switched on. You can add description text to a record count to describe to your Service Agents how they should use record count for in that particular process, e.g. Payslip Count. The description will show next to the record count setting in Work Manager at runtime.</td></tr></tbody></table>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXLbBety99XsATwTSuSVj%2Fimage.png?alt=media&#x26;token=917dec98-8eb3-40c9-bd04-17482be4c55c" alt=""><figcaption></figcaption></figure>

## Configuring Steps for a Case **Type** <a href="#configuring-steps-for-a-case" id="configuring-steps-for-a-case"></a>

You can add, edit and delete the steps of a Case type from the Service Lines page. You can easily reorder the steps by dragging and dropping them. The Milestone % is optional, it denotes the progress reached when this step is completed and it displays in the Case form status tracker control.

When you delete a step, any Actions that were underneath that step will now display as ad hoc Actions. When a step is reordered, the Actions underneath that step will move with the step.

### Effect on Live Case Processes <a href="#effect-on-live-case-processes" id="effect-on-live-case-processes"></a>

If you make changes to the steps of a Case type, live versions of Case processes of that Case type will not be affected. They will run as previously configured and the step changes won't apply until a new version of the Case process with the updated steps has been set live.

### Updating a Case Process to Match Updated Steps <a href="#updating-a-case-process-to-match-updated-steps" id="updating-a-case-process-to-match-updated-steps"></a>

You will be notified in the Case process screen if its steps are out of date i.e. if changes have been made at a Case type-level when you are in edit mode.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-MlAYBHCIyem9--x7OhD%2F-MlA_w_Hv9DAgltkZ8Zi%2Fimage.png?alt=media\&token=57e73b77-674d-4d4d-9062-1a30e5762b9e)

You can click on the Refresh Steps icon in the header of the Case screen to refresh the steps to the latest version.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-MlAYBHCIyem9--x7OhD%2F-MlAaiUSA6ZWR_smVfa-%2Fimage.png?alt=media\&token=a587ebdb-742e-42c3-870a-f2a2a8fc5c1f)

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-MlAYBHCIyem9--x7OhD%2F-MlAa20ycLr8EMMsTVKR%2Fimage.png?alt=media\&token=d0361287-8f8c-4d8f-baea-b06b0bc9fc1b)

When you click to confirm, you will be shown which changes have been made:

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-MlAYBHCIyem9--x7OhD%2F-MlAaJmQCO2R254_RP6j%2Fimage.png?alt=media\&token=7bfb79ee-5cd2-419f-8bfe-e5f042c2cb34)

Click OK to update the steps to match the steps configured at a Case-type level; new steps will be added to the Case process, steps in the Case process will be renamed, steps in the Case process will be moved along with the Actions underneath them and steps will be deleted and their Actions will become ad hoc Actions.

### Effect on Cloning Case Processes <a href="#effect-on-cloning-case-processes" id="effect-on-cloning-case-processes"></a>

You can clone any Case process which is live under the same service line and all data such as Actions etc. will be cloned, except for schedules.

If the Case you are cloning has the same Case type, then the step names and Actions will all be copied across.

If the Case you are cloning has a different Case type, then the step names will not be copied across, instead they will appear like this:

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-MlEjd0oGS8Ah2HjoPEH%2F-MlEqG6XQkq9p69bmFPr%2Fimage.png?alt=media\&token=0e253ab4-07b8-4667-ae5a-adb6f4bee262)

Actions will be cloned across in their original positions i.e. Actions under the first step of the process being cloned will be the Actions under the first step of the Case process they have been cloned to. If there are more steps in the source process being cloned than in the Case it is being cloned to, the Actions under the "extra" step will become ad hoc Actions.

To update the steps in the Case to the latest version of its own Case type, click to refresh the steps in edit mode.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-MlEjd0oGS8Ah2HjoPEH%2F-MlEq78g7XO22ae2MpW0%2Fimage.png?alt=media\&token=51a86bc3-a074-47c8-b6cd-a145eec53e18)

This will update the steps to the latest version in the Case type. If a step has been removed, any Actions that were underneath that step will now display as ad hoc Actions.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-MlEjd0oGS8Ah2HjoPEH%2F-MlEqUHTu1Xfr_OUxLJM%2Fimage.png?alt=media\&token=133ea3b7-1743-4f50-866b-942c3800be06)

## **Subsequent Editing of a Case Type** <a href="#d-subsequent-editing-of-case-action-ticket-type" id="d-subsequent-editing-of-case-action-ticket-type"></a>

To edit a Case type’s settings, click on the Case in the Service Lines Screen and edit the information in the right hand side of the screen. Click to save these changes.

{% hint style="info" %}
Note: these settings are not versioned i.e. when changes are made, they affect all new and running Work Items.
{% endhint %}

You are also able to see the activity history of your work items , by clicking on the Show Activity button. You can see when the work item was created and by who, as well as if any edits have been made to the work item, when they were made, as well as by who.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWowRyqtjfOiBDs_cLN%2F-MWoxR_TA5CUhtoTweBm%2Fimage.png?alt=media\&token=e2c6b70f-6328-46cc-9873-759b207de127)

You are also able to clone a Case type by clicking on the Clone button in the edit screen. This will clone all of the Case type's settings and data apart from its name. You are able to make changes to any of the settings and data once the Case type has been cloned.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXlL6td0YC_WekF49fg%2F-MXldkURjCqxuoyvOpF0%2Fimage.png?alt=media\&token=52bfbe4c-6521-41b3-b844-cdff021600d2)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXlL6td0YC_WekF49fg%2F-MXlgIHuuyw81kofSrtZ%2Fimage.png?alt=media\&token=5ad786fa-0e9f-4baa-bf09-934687d661b8)
