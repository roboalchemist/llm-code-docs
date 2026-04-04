# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/creating-new-work/bulk-create-work-items.md

# Bulk Create Work Items

## Overview

The Bulk Create feature lets you create large numbers of Cases and/or Tickets via the uploading of data from Excel spreadsheets.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc3Nw==>" %}

You can find a link to the Bulk Create page in the ‘Bulk Create’ link in the ‘Create New Work Item’ dropdown.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FooJaBoamzT3URAqBjFqC%2F10%20Bulk%20Create.gif?alt=media&#x26;token=28fc19e2-4206-480b-bbec-418508ccb790" alt=""><figcaption></figcaption></figure>

This will bring up the Bulk Create screen in a new tab. From this screen select whether you want to bulk create Cases or Tickets. You can then download the relevant Excel template, populate it, then upload it to the page - making sure to fill in any [mandatory fields](#mandatory-fields) beforehand. &#x20;

You can download a template of the excel file. The excel templates available will conform to whichever language you currently have set in your Enate user preferences.

Once you have added the data into the excel file, save and close it, then on the Bulk Create screen click to select the file.

You can then choose if you want to allow work items with duplicate titles to be created by using the ‘Unique Title’ option. Leaving this option off allows work items with duplicate titles to be created. Switching this option on will ensure that any work item which is due to have the same title as another item in the upload file will [fail validation](#validation-errors).

Once you are happy, click on the ‘Upload’ button. This will upload your information about the Cases or Tickets from your file on-screen.

You will see the following information:

* **Total** – the total number of items contained in the uploaded file that will be created&#x20;
* **Created** – the number of items that have been created successfully (this will be zero before you start to create)
* **Issues** – the number of items with [validation issues](#validation-errors) (these need to be fixed before the items can be successfully created)
* **Not Started** – the number of items that are waiting to be created

Additionally, in the grid you will see that a 'Status' and 'Reference' column have been added - these will be filled in by the system when the items get created.

All you need to for now is to click ‘Create Items’ and the system will start creating your Cases/Tickets. The information displayed will update to show the number of items that have been successfully create and the reference numbers of the work items created.

{% hint style="info" %}
**It should be noted that excel uploads of up to 2000 rows are supported in bulk create. Sheets with more rows than this can lead to potential errors.**&#x20;
{% endhint %}

## Bulk Create Templates

If you are using version 2022.5 or above of Enate, please use the in-product templates from the bulk create page. If you are using version 2022.4 or below of Enate, please use the templates below

### Bulk Create Ticket Templates

You can download the excel file templates to bulk create Tickets from the following links:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOshXkiGInF7ld1YcvwfL%2Fbulk-create-ticket_en-gb.xlsx?alt=media&token=eff2aaba-c493-4292-b339-891254acccff>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVbsS5rlfK6s2lYXbLcV7%2Fbulk-create-ticket_en-us.xlsx?alt=media&token=a7cdc5e9-ddf6-4c97-926f-f9347de933d6>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNV5i9uYCcGGNyt5sDJXv%2Fbulk-create-ticket_fr-fr.xlsx?alt=media&token=29ce366d-7c3c-4b00-8d4d-0177a3b14171>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FznbcN7Fjl486dn5kIDhk%2Fbulk-create-ticket_de-de.xlsx?alt=media&token=e36ddc24-c4c3-4eef-a19b-99610b07c0fa>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FN4ZtAhlbNxSCwdGIBChf%2Fbulk-create-ticket_es-419.xlsx?alt=media&token=c006b1d5-152d-41cd-bbfb-49bf82c439af>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fk5dppQNgsYZIwO7N7wfX%2Fbulk-create-ticket_pt-br.xlsx?alt=media&token=4ceefdc8-042f-44ee-84a5-e67966bf07f0>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvhodJBF9Y6665GG6G0Kg%2Fbulk-create-ticket_pt-br%20(v23.1%20onwards).xlsx?alt=media&token=0f44a312-6d5c-4199-b884-7101650ab183>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeDbSxHuyu0MvTbcuO5Q0%2Fbulk-create-ticket_ro-ro.xlsx?alt=media&token=be0450e8-9545-4eac-ae3d-24e77fd53578>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ftu8Xamas8k8jDpMxFcRm%2Fbulk-create-ticket_pl-pl.xlsx?alt=media&token=3fe331db-7fd2-4851-8410-72fd87c2b8a0>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtlrMizq7KQSHQV5j1Wkw%2Fbulk-create-ticket_hu-hu.xlsx?alt=media&token=fdc5e705-d6a7-4305-ab55-8c1681a62a72>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5aFIJkdzGs4Pu9e3Jdc6%2Fbulk-create-ticket_ru-ru.xlsx?alt=media&token=b8d48fed-3968-4980-b468-c2bb8817ac4b>" %}

### Bulk Create Case Templates

You can download the excel file templates to bulk create Cases from the following links:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkzMyVMsyNx9EejJlH2VS%2Fbulk-create-case_en-gb.xlsx?alt=media&token=09fd10cc-9167-443e-85f2-bcc0c2b64391>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F392GDtfbliR1iyz0LcXD%2Fbulk-create-case_en-us.xlsx?alt=media&token=997ef861-490c-491a-a039-95dc5e2df6c8>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7zNyBDVYqR09aGqBxd2B%2Fbulk-create-case_fr-fr.xlsx?alt=media&token=c36f0624-5aba-4740-b4f2-251b3fad689b>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FxxZzicTJavcJV3BtJDlB%2Fbulk-create-case_de-de.xlsx?alt=media&token=6bd8b250-e2d6-4d31-82b1-f01f0cf910d8>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7ws0OtVe0m9ilVdFGy7E%2Fbulk-create-case_es-419.xlsx?alt=media&token=b9c9fd9e-951b-4a95-824e-3368fb9c773a>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCEFqplCDyZB455W05uJv%2Fbulk-create-case_pt-br.xlsx?alt=media&token=a6d36dd7-c8e0-4bb7-89c1-36c4e0510ddc>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FgvbslumrVcgIe1djeanh%2Fbulk-create-case_pt-br%20(v23.1%20onwards).xlsx?alt=media&token=c6e326a5-e9b6-480e-87cb-1b9c9866c3b6>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXq8Ic8OsvTS8jCahFSqe%2Fbulk-create-case_ro-ro.xlsx?alt=media&token=1f850df7-37d4-4ff4-935d-e51c3531600a>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBIxWuBnpQ5ZxGyyFgaDq%2Fbulk-create-case_pl-pl.xlsx?alt=media&token=2a366e7c-bf6a-495f-9def-5a625aa8a735>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzPfe1y7yaIqM46ejXVyg%2Fbulk-create-case_hu-hu.xlsx?alt=media&token=86a6f142-4e9d-46c1-bb04-4625033afedb>" %}

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fg2KhMWCygUeRlfbcV8AR%2Fbulk-create-case_ru-ru.xlsx?alt=media&token=67508a29-4f56-437d-9b38-ad5144583fab>" %}

## Mandatory Fields

The mandatory fields which must be filled in order to create a Case are:

* Customer
* Contract
* Service
* Case - the process name
* Title - the title for the individual Case work item.&#x20;

{% hint style="info" %}
Note that the Primary Contact and Requester fields are only mandatory for a Case when the '[Make Contacts Mandatory](https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen/creating-new-case-types-in-a-service-line#a-creating-a-new-type-of-case)' option is set to 'on' for the Case type you are bulk creating in the Service Lines screen in Builder. If you do want to fill these fields in, make sure to[ adhere to contact record requirements](#requirement-for-contact-records-within-your-bulk-upload-file).&#x20;
{% endhint %}

The mandatory fields which must be filled in order to create a Ticket are:

* Customer
* Contract
* Service
* Ticket - the process name
* Title - the title for the individual Ticket
* Ticket Description
* Ticket Category Level 1&#x20;
* Ticket Category Level 2&#x20;
* Ticket Category Level 3&#x20;
* Primary contact - the main contact you are dealing with for this query.  [See section about contact record requirements](#requirement-for-all-contact-records-within-your-bulk-upload-file).
* Requester - the contact that raised the initial request. [See section about contact record requirements](#requirement-for-all-contact-records-within-your-bulk-upload-file).

{% hint style="info" %}
Note that all data entered must match existing values in the system, otherwise [validation errors](#validation-errors) will be displayed.
{% endhint %}

### Requirement for contact records within your bulk upload file

Any contact records used in a bulk create file i.e. Primary Contact, Requester, Subject and CC contacts must adhere to the following rules:

* the email address of the contact must be used
* the contact must already exist in the system&#x20;
* the contact must be [scoped to the same customer](https://docs.enate.net/enate-help/work-manager/managing-contacts/adding-editing-and-deleting-contacts#company-name-external-contact-scoping) that the Case/Ticket will be created under

## Optional Fields

Optional fields that can be filled in for both Tickets and Cases are:

* Subject - the contact the work item is about. [See section about contact record requirements](#requirement-for-all-contact-records-within-your-bulk-upload-file).
* CC email address(es) - any further contacts which can be copied on any correspondence. [See section about contact record requirements](#requirement-for-all-contact-records-within-your-bulk-upload-file). Also note that when adding two or more CC email addresses, please make sure to separate the addresses with a semi colon (;) with no spaces either side e.g. <mark style="color:blue;"><user.one@example.net></mark>;<mark style="color:blue;"><user.two@example.net></mark>.
* Override Due Date - enter the new due date. [See date formatting section](#date-formatting).
* Do Not Send Automated Emails To Contacts - whether or not you want to send system-automated emails, such as request acknowledgement emails, to the contacts of the work item. Enter 'True' or 'False', this also applies for languages other than English.

### Date Formatting

Please be aware that any dates entered must have the following formatting:

DD-MM-YYYY HH:MM

Note that hours and minutes entered can either be in the 24 hour system format i.e. 23:00 or in the 12 hour system format with an AM/PM after it i.e. 11:00 AM.

Valid date format examples:

* 25-05-2022 23:25
* 25-05-2022 11:25 PM

If you choose not to enter hours or minutes, the system will set a default time of 00:00.

## Custom Data Fields

You can also pass custom data fields into the Cases/Tickets as they are being created. To do this, add a column name which precisely matches the data field name in Enate. If any of these bespoke fields are marked as mandatory in your Case process configuration, you MUST supply a value in this field’s column for every row in the upload file (otherwise that row will fail validation and a Case will not be created for it).

### **Supported Fields** <a href="#supported-fields" id="supported-fields"></a>

Bulk create supports below list of custom field type:

1. Check Box
2. Date Only - [see date formatting section](#date-formatting).
3. Date and Time - [see date formatting section](#date-formatting).
4. Decimal Number
5. Email Address
6. Hyperlink - note that hyperlinks with customised display text are not supported i.e. the text entered in a hyperlink field must be the entire URL of the hyperlink e.g. <https://www.enate.io/> and NOT [Enate Website](https://www.enate.io/)
7. List
8. Long Text
9. Multiple level list
10. Short Text
11. Whole Number

### **Unsupported Fields** <a href="#unsupported-fields" id="unsupported-fields"></a>

Bulk create does not support below custom field type:

1. Tables
2. Entity Relationship

Additionally, the following system property fields are not supported when bulk creating work:

1. Keep with me
2. Keep Action with me
3. Defects
4. Files

## Validation Errors

If you do have any validation errors, these will be highlighted in red and a ‘warning’ status icon will be displayed. If the input values are wrong throughout an entire column, validation errors will be displayed at the bottom of the grid e.g. if a field column is referenced in the upload file which does not exist in the system. If the input values are wrong for an individual row, a ‘warning’ status icon will be displayed at the start of the row and the individual validation errors will be highlighted in red. You will then need to modify the file, click to 'change file' and select to upload your updated file.

You can still proceed with creation of the valid Case items in your upload file. The system will skip over the invalid rows and confirm creation of the valid ones, but the invalid items will need to be resolved before they can be created. You can do this by modifying the file and then clicking to 'change file' and select to upload your updated file.

Click here to see the full list of potential validation errors for Bulk Create:

{% content-ref url="../appendix/potential-validation-errors-for-bulk-creation-of-work-items" %}
[potential-validation-errors-for-bulk-creation-of-work-items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/appendix/potential-validation-errors-for-bulk-creation-of-work-items)
{% endcontent-ref %}

## Multilingual Support

Bulk Create is also supported in all of the languages that Enate offers: French, German, Spanish, Portuguese Brazilian, Romanian, Polish, Hungarian and Russian.&#x20;

{% hint style="info" %}
Note: the bulk create template uploaded should be in the same language as the logged-in user’s preferred language. For example, if a Spanish user wants to upload a bulk create template, then the template they upload should be in Spanish.&#x20;

Additionally, the column header values in the bulk create template should match the values that are configured in Enate Builder in the [Localisations page](https://docs.enate.net/enate-help/builder/builder-2021.1/adding-localisations). If the translations for fields like Primary contact, Requester, CC, Subject or any Custom Data Fields have been modified in the Localisations page, then the column headings in the bulk create template need to match these values.
{% endhint %}
