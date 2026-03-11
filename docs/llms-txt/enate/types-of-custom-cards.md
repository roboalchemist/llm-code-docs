# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/types-of-custom-cards.md

# Creating a Custom Card

Custom cards let you add custom content into your Tickets, Cases and Actions. You can instantly create cards of your custom data fields, or switch to Advanced mode to show richer content such as external systems and webforms.

To create a Custom Card that you are able to quickly auto-generate from an ordered list of the fields listed on the cards, select the Custom Cards section from the toolbar.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpp_zhBWIMnDwVu24N%2Fimage.png?alt=media\&token=3c70639c-0d89-4eec-baae-c52c2d7f3332)

This will bring you to a list of all Custom Cards. This is where you can create, edit and delete Custom Cards.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FM5ZDoGgjnhToa0peg4Us%2Fimage.png?alt=media&#x26;token=663f4f4d-479b-422c-8cfa-aef19979ecfe" alt=""><figcaption></figcaption></figure>

You can also export and import Custom Cards - see here for more information:

{% content-ref url="importing-exporting-custom-cards" %}
[importing-exporting-custom-cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/importing-exporting-custom-cards)
{% endcontent-ref %}

## Creating a Custom Cards <a href="#a-creating-editing-super-simple-cards" id="a-creating-editing-super-simple-cards"></a>

To find out how to create a Custom Card in Enate, you can watch the following video or read the information below.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM3NTk2Mg==>" %}

Clicking the '+' icon on the top right of the page will give you the option to 'Add a Work Manager Card' or to 'Add a Self Service Card'.  As the name suggests, Work Manager cards are used for presenting data to agents looking at work items in Work Manager; Self Service cards are used for presenting data to customers in Self Service, usually used to give end service recipients a view on their data for a service request they are submitting or reviewing via Self Service.&#x20;

Clicking on either of these links will bring up the card details:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmEuWelpVRCAArW5S9jKo%2Fimage.png?alt=media&#x26;token=3ebaa128-6880-416d-81a4-2eb99e8cb4b2" alt=""><figcaption></figcaption></figure>

The screen will show you card header data to be filled in, plus two columns showing a list of custom data fields. The 'Added Fields' section on the left shows the fields currently added to the card (which will be empty for brand new card); the 'Available' section on the right lists all other custom data fields that are available in your system.

### Adding Custom Card settings <a href="#c-card-attributes" id="c-card-attributes"></a>

You then need to configure the following information for the Custom Card:

<table data-header-hidden><thead><tr><th>Attribute</th><th width="415">Description</th></tr></thead><tbody><tr><td>Attribute</td><td>Description</td></tr><tr><td>Name</td><td>The card name. Mandatory.</td></tr><tr><td>Description</td><td>A description for the card</td></tr><tr><td>Advanced</td><td>Whether you want the Custom Card to include advanced content. <a href="#undefined">See here for more information.</a></td></tr></tbody></table>

### Adding fields to the Custom Card

To add a custom data field to a custom card, you can click on a field from the 'Available' section on the right-hand side which shows a list of all the custom data fields in the system. This will add the field to the 'Added Fields' section on the left which shows a list of all the custom data fields which have been added to the Custom Card.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fghp9k5PSNBmLT87CLSxo%2Fimage.png?alt=media&#x26;token=9c903775-6feb-40b9-8215-398cc34734e1" alt=""><figcaption></figcaption></figure>

If you have many fields to choose from, you can click to filter the list by type of data or you can search for the field name itself.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpq4CfxQ3yWyCyIQu5%2Fimage.png?alt=media\&token=ea58d056-81a0-46a6-8504-e05c93f6e4ad)

### Ordering fields on a Custom Card

After adding the desired custom data fields to your Custom Card, drag and drop the fields to modify the order in which you want your custom data fields them to display in Work Manager.

## Making a field mandatory

You can choose if you want end users in Work Managers to have to fill in the field by selecting to make a custom data field mandatory.

To make a field mandatory, select a custom data field from the list of Added Fields on the left and click the '+' icon. This will open the Field Settings pop-up.

Selecting the 'Mandatory' option will mean that an agent in Work Manager will be required to fill out the fields marked as mandatory before they are able to submit or change the status of the work item.&#x20;

The validation check for when only the 'mandatory' option is set runs every time a work item gets submitted or the status gets changed. This means that when an agent clicks to change the status of the work item, regardless of what that status is the system will still run a check and ask the agent to complete any mandatory fields that are yet to be filled in in order to proceed every time the user clicks to change the status of the work item.

{% hint style="info" %}
Please note: Checkbox fields cannot be made mandatory.
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVqVbPSeFF78gc7wDpTJW%2Fimage.png?alt=media&#x26;token=7c0aa2bb-2281-4797-a956-b63e0c1fcecd" alt=""><figcaption></figcaption></figure>

### Set a field Mandatory 'Only on Resolve'

Selecting the 'Only on Resolve' option will mean that an agent in Work Manager will only be required to fill out the fields marked as mandatory at the point of Resolving a ticket or Action, rather that for any update.&#x20;

When this setting is ticked, the validation check to make sure that all mandatory fields are filled in only occurs when an agent clicks to mark the work item as successfully resolved, instead of every time the submit or change the status of the work item.&#x20;

This means that when an agent clicks to change the status of the work item to resolved successfully but has not filled out the mandatory fields, the system will prevent the agent from resolving the work item and will ask the agent to complete the mandatory fields in order to proceed.&#x20;

However, if the agent is changing the status to something other than successfully resolved, e.g. 'Waiting' because they do not have the data required to fill in the mandatory data fields, or they are rejecting or cancelling the work item, the system will not ask the user to fill in the mandatory fields; they will instead be able to proceed without being forced to fill in the mandatory data fields.

This should help avoid scenarios where agents must fill in any mandatory fields, even though the change in work item status no longer requires the data fields to be filled in e.g. when rejecting a Ticket as spam.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FebC8ksU1U8WAceUKSqPN%2Fimage.png?alt=media&#x26;token=d5f564dd-6535-466d-abae-78a358239faa" alt=""><figcaption></figcaption></figure>

#### What counts a resolving a work item successfully?

For a Ticket, this is when choosing to resolve a Ticket

* With Customer Response, or with
* No customer response

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FygbZfRu8xuepSe8WIsv7%2Fimage.png?alt=media&#x26;token=12b89ec3-ebb6-46d7-96cf-8466267007ce" alt=""><figcaption></figcaption></figure>

For an Action, this is when you click to resolve the Action and mark it as 'complete'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F82y2TQ6AwupRPmRQGNtp%2Fimage.png?alt=media&#x26;token=f07b98f4-d68c-4837-b19f-3af7382e5c6f" alt=""><figcaption></figcaption></figure>

Once you have marked a field as 'Mandatory' or 'Mandatory Only on Resolve' and clicked 'Apply', the field will now be marked with an 'M' to show that it is mandatory.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FppB14qLEj6jqxaLu6TrV%2Fimage.png?alt=media&#x26;token=1f457ccb-916b-4675-a4bb-2949a86c644d" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note that when it comes to making a custom data table mandatory, you cannot make the whole table mandatory but you can make individual fields within the table mandatory.
{% endhint %}

## Making a field read-only

You can choose if you want end users in Work Manager to be unable to edit the field by selecting to make a custom data field read-only.

To make a field read-only, select a custom data field from the list of Added Fields on the left and click the '+' icon. This will open the Field Settings pop-up.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaG3WHJuyl6LBFgddXJhV%2Fimage.png?alt=media&#x26;token=4def6175-c19e-4057-9a45-1a3b96d1b36f" alt=""><figcaption></figcaption></figure>

Click the 'Mark this field as read-only' option and click 'Apply'.

The field will now be marked with an 'R' to show that it is mandatory.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FppB14qLEj6jqxaLu6TrV%2Fimage.png?alt=media&#x26;token=1f457ccb-916b-4675-a4bb-2949a86c644d" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note that when making a field read-only your options for providing a value to it are as follows:

* Set a default value for the field by adjusting the custom data field settings, or if you leave the default settings blank,&#x20;
* Users in Work Manager can enter a value into the field on a Work Item, but once the field has been filled in and the work item has been subsequently submitted, the field will become read-only and users will no longer be able to edit it.&#x20;

Note that you cannot set a default value for the following types of data:&#x20;

* multiple-level lists&#x20;
* decimal numbers.
  {% endhint %}

#### Making table field read-only

When it comes to making a custom data table read-only, you cannot make the *whole* table read-only but you can make individual fields within the table read-only.

## Showing/hiding a field based on conditions

You can also choose if you want to hide a custom data field from end users in Work Manager based on the value of another field on the card by selecting to Add Conditions. For example, you could choose to hide the field 'Type of hardware required' if the answer for the field 'Is hardware required' is no by adding the following condition:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyMZhPQu97fU9hihKUq8t%2Fimage.png?alt=media&#x26;token=955a4d26-3e0d-46ed-a9d6-a76dae281a24" alt=""><figcaption></figcaption></figure>

Then if any one of these conditions are met, the field 'Type of hardware required' will not show on the Custom Card in Work Manager (**this can happen instantly on field value change when users a changing field values**).

To add a condition, a field from the list of Added Fields on the left and click the '+' icon. This will open the Field Settings pop-up.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaG3WHJuyl6LBFgddXJhV%2Fimage.png?alt=media&#x26;token=4def6175-c19e-4057-9a45-1a3b96d1b36f" alt=""><figcaption></figcaption></figure>

Click the '+' option to add a condition and then select the field and the condition.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaezDPuUtOsGEkq7YuObX%2Fimage.png?alt=media&#x26;token=c21b0072-1ad1-40a3-b811-f82866c04593" alt=""><figcaption></figcaption></figure>

You can add a condition based on any of the existing custom data fields that have been added to a Custom Card and for all custom field data types.&#x20;

{% hint style="info" %}
'OR' logic applies if multiple conditions are added to a field, i.e. if any one of the conditions added to a field are met, the field will not show on the Custom Card in Work Manager.
{% endhint %}

The conditions you can add depend upon the type of custom field. See the following table for further information:

<table><thead><tr><th width="286">Type of custom data field</th><th>Type of condition that can be used</th></tr></thead><tbody><tr><td>Check Box</td><td><p>Equals</p><p>Does Not Equal </p></td></tr><tr><td>Date and Time</td><td><p>Equals</p><p>Does Not Equal </p><p>Is Between </p><p>Is greater than </p><p>Is less than </p><p>Is greater than or equals </p><p>Is less than or equals</p></td></tr><tr><td>Date Only</td><td><p>Equals</p><p>Does Not Equal </p><p>Is Between </p><p>Is greater than </p><p>Is less than </p><p>Is greater than or equals </p><p>Is less than or equals</p></td></tr><tr><td>Decimal Number</td><td><p>Equals</p><p>Does Not Equal </p><p>Is Between </p><p>Is greater than </p><p>Is less than </p><p>Is greater than or equals </p><p>Is less than or equals</p></td></tr><tr><td>Email Address</td><td><p>Equals</p><p>Does Not Equal </p></td></tr><tr><td>Hyperlink</td><td><p>Equals</p><p>Does Not Equal </p></td></tr><tr><td>List</td><td><p>Equals</p><p>Does Not Equal </p></td></tr><tr><td>Long Text</td><td><p>Equals</p><p>Does not equal</p></td></tr><tr><td>Multiple Level List</td><td><p>Equals</p><p>Does Not Equal </p></td></tr><tr><td>Short Text</td><td><p>Equals</p><p>Does Not Equal </p></td></tr><tr><td>Whole Number</td><td><p>Equals</p><p>Does Not Equal </p><p>Is Between </p><p>Is greater than </p><p>Is less than </p><p>Is greater than or equals </p><p>Is less than or equals</p></td></tr><tr><td>Custom Data Table</td><td>See below.</td></tr></tbody></table>

#### Showing & Hiding Table Fields

When adding conditions to determine whether a data table should be shown or hidden depending on whether certain conditions are met, note that the entire data table will either be shown or hidden - you cannot choose to show or hide individual fields within a custom data table. This includes any fields that you have selected as mandatory.

## Creating New Fields within the Custom Cards Screen <a href="#b-creating-new-fields-within-the-cards-screen" id="b-creating-new-fields-within-the-cards-screen"></a>

You can easily create new custom data fields without leaving the Cards editing screen - simply click the 'add' icon above the list of system fields and fill in the required information in the resulting popup.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fdu3ntFbPod8Oh74vLDWO%2Fimage.png?alt=media&#x26;token=c8c30659-960d-4a20-b34a-f412c1093d92" alt=""><figcaption></figcaption></figure>

## Advanced Custom Cards

If you wish your Custom Card to contain bespoke content, you can select the 'Advanced' option while editing the card. This will allow you to add HTML and Typescript.&#x20;

See here for more information about Advanced Custom Cards:

{% content-ref url="super-flexible-cards" %}
[super-flexible-cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/super-flexible-cards)
{% endcontent-ref %}
