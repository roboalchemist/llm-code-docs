# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/creating-custom-data-fields.md

# Creating Custom Data Fields

## Overview of custom data fields

Enate's custom data fields let you model any bespoke data you need for managing and running your processes. This can help you to capture key information as part of processing your Tickets, Cases and Actions, and store for example incoming data as work gets created.&#x20;

Custom data fields are easy to create and, once you have them, they can be used in lots of places throughout the system:

* You can use [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/types-of-custom-cards) to display and edit your data fields in Tickets, Cases & Actions
* You can search by them in [Quickfind](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/quickfind/quickfind-searches-with-custom-data-fields)
* They're available to use in your [Homepage ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/home-page/home-page-bar-chart-and-grid#displaying-by-custom-data-fields)and [Views ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/views-of-your-data)grids and can be used for the breakout display chart
* They're available in the data warehouse for use in custom reports.

Custom data fields can be used in conjunction with [Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/types-of-custom-cards) - these are auto-generated or manually created cards which can be added to your Tickets, Cases and Actions to let you view and maintain your data. Custom Cards can also contain bespoke code to display any manner of information alongside your data.

There are two types of custom data field that you can create

1. [Custom data fields](#a-creating-a-field) - these are used for defining individual fields of information
2. [Custom data tables](#b-creating-tables) - these are useful for the storing of repeating rows of information

The Custom Data Fields section in Builder is where you can create new custom data fields and view, edit and even delete existing custom data fields.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpoexenQNy5S5HDnEw%2Fimage.png?alt=media\&token=0f768e54-d1cf-4ac3-8b1a-82da2a74c8fd)

Once you have created your desired custom data fields, you'll want to [add them to Custom Cards](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/types-of-custom-cards) to start using them.

## Creating new custom data <a href="#a-creating-a-field" id="a-creating-a-field"></a>

See this video to find out how to create custom data, or read the information below.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTMxNTc3Mg==>" fullWidth="true" %}

To create a custom data field, go to the Custom Data Fields section in Builder and click the ‘+’ icon at the top right of the screen and then select to 'Add Field'.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FThAgqAgFV4Xvvd7ewh5O%2Fimage.png?alt=media&#x26;token=83889ad0-adff-4683-b94d-2aafb4d84eae" alt=""><figcaption></figcaption></figure>

In the following pop-up, fill in the following information:

| Attribute     | Description                                                                                                                                                                                                 | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name          | The field name                                                                                                                                                                                              | Mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Safe Name     | The name of the field to be used if you're referencing it in code.                                                                                                                                          | <p>The system will autogenerate this name as you type (a copy of the field name with spaces removed). </p><p></p><p>This Safe Name should be used in any subsequent Custom Card HTML / Typescript / CSS references. </p><p></p><p>You can copy the Custom Field safe name by clicking on the copy icon.</p>                                                                                                                                                                                                                                                                                                                                                                                            |
| Description   | The description for the field                                                                                                                                                                               | Not mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Type          | The type of data you want the field to collect e.g. long text / date time etc.                                                                                                                              | See here for more information about the [available types of custom data field](#types-of-field). Mandatory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Default Value | Depending on the type of field you select, you may be able to set a default value for the field.                                                                                                            | Not mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Private       | Whether the field's value should be shared among [related work items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items) | <p>By default, any changes in a field's value when made have an immediate effect in all its <a href="../../../work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items">related work items</a>. For example, any changes in a field's value in an Action have an immediate effect in all its related work items i.e. its parent Case, the other Actions of that Case and even any originating Ticket.</p><p></p><p>Switch this option on if you DO want data to be shared among its <a href="../../../work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items">related work items</a> or leave if off if not.</p> |
| Searchable    | Whether the field should be available to search by in [Quickfind](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/quickfind)                                                             | <p>This option only appear when the <a href="#types-of-field">type of custom data field</a> you select is 'Short Text' or 'List'. </p><p></p><p>If you set a field as Searchable you will need to provide a short code to use in Quickfind. </p><p></p><p>See this section for more information about <a href="quickfind-with-custom-data-configuration-and-rules">configuring custom data fields to be searchable in Quickfind</a>.</p><p></p><p>See this section for more details about how to use <a href="../../../work-manager/work-manager-2021.1/quickfind/quickfind-searches-with-custom-data-fields">Quickfind searches with custom data fields</a> in Work Manager. </p>                     |

### Types of custom data field <a href="#types-of-field" id="types-of-field"></a>

The following Types of fields are supported:

| Type                | Description                                                                                                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Check Box           | True / False Boolean marker                                                                                                                                                                           |
| Currency            | If you would like to enter a default value, you must enter a default currency code and a default currency amount.                                                                                     |
| Date and Time       | Stores both the date and time component.                                                                                                                                                              |
| Date Only           | Stores only the date component                                                                                                                                                                        |
| Decimal Number      | e.g. 3.2                                                                                                                                                                                              |
| Email Address       | Must be a valid email address.                                                                                                                                                                        |
| Hyperlink           | URL. The URL entered must be a valid URL and the maximum length that can be entered is 2048 characters.                                                                                               |
| List                | A dropdown list. If you select this type, you can manually enter a list of available dropdown items along with the field. This supports copy / pasting of tabular information from e.g. spreadsheets. |
| Long Text           | Text fields of over 255 characters.                                                                                                                                                                   |
| Multiple Level List | A dropdown list with multiple levels. Up to 3 levels are supported. See here for more details about a [multiple-level list](#multiple-level-lists).                                                   |
| Short Text          | Text field limited to 255 characters.                                                                                                                                                                 |
| Whole Number        | e.g. 4                                                                                                                                                                                                |

#### Multiple-Level Lists <a href="#multiple-level-lists" id="multiple-level-lists"></a>

This type of custom data field allows users to create lists with up to two additional nested sub-lists, so three levels of list in total.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpp-QP2GtfyDRtSeL4%2Fimage.png?alt=media\&token=687fe844-849a-4d14-b9d6-57834e422202)

{% hint style="info" %}
Please note:

* Parent list items and their children are sorted alphanumerically by default
* Duplicate child entries per single parent are not allowed
  {% endhint %}

When you choose this type of custom data field, an additional option of 'Include blank 'select' value' will appear. Selecting this option will make the list appear with a default 'select from dropdown' option in the Custom Card in Work Manager, if a default value hasn't been set.

### Editing a field

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHNHwpvuUxVqFXWJafqqX%2Fimage.png?alt=media&#x26;token=8931f9e3-939b-47d8-95c6-aa660fc06765" alt=""><figcaption></figcaption></figure>

When editing a custom field, you are also able to see its activity history by clicking on the Show Activity button. You can see when the custom field was created and by who, as well as if any edits have been made to the custom field, when they were made and by who.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpp6-X3-AbXY7B2dfX%2Fimage.png?alt=media\&token=13e0c630-9a38-4a31-876d-3e4b358034f5)

### Deleting custom data fields

You can delete a custom field by clicking on the menu option on the right of the row:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXkzr1XA5W_O_KoJJ7b%2F-MXl6hrDOIZwldL-VBhr%2Fimage.png?alt=media\&token=8e23c986-0ace-419c-ae5f-e762ff8e7b26)

## Using Data Fields for Reference Numbers <a href="#using-data-fields-for-reference-numbers" id="using-data-fields-for-reference-numbers"></a>

One of the many things you may wish to store with custom data fields is your own Reference numbers, perhaps to help tie things up with other systems that may be in use. You are strongly encouraged to define **text fields** for this, even if the reference field contains nothing but numbers, e.g. '22345216'.  Some simple things to take into account when selecting data types here:

* Are you going to be performing maths on the field? If No, you should choose a text string data type.
* Could there be leading zeros in the reference number? If Yes, definitely choose a text string data type. If you don't, and choose numeric data type instead, you run the risk that e.g. entering '01234' will save as '1234', as most systems dealing with a numeric value are likely to trim leading zeroes.<br>

## Creating a new table <a href="#b-creating-tables" id="b-creating-tables"></a>

In addition to defining individual custom data fields, you can also define tables to allow for storing of repeating rows of information.

To create a new custom data field, click the ‘+’ icon at the top right of the screen and then select to 'Add Table'.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FThAgqAgFV4Xvvd7ewh5O%2Fimage.png?alt=media&#x26;token=83889ad0-adff-4683-b94d-2aafb4d84eae" alt=""><figcaption></figcaption></figure>

This will bring up a screen where you can define the table data.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWppARc6L_UACQm3RRE%2Fimage.png?alt=media\&token=68312511-b37c-4131-b52e-51b23c942f94)

Fill in the following table-level information:

| Attribute   | Description                                                                                                                                                                                                | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name        | The table name                                                                                                                                                                                             | Mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Safe Name   | The name by which the table should be referenced on Custom Cards                                                                                                                                           | <p>The system will autogenerate this name as you type (a copy of the field name with spaces removed). </p><p></p><p>This Safe Name should be used in any subsequent Custom Card HTML / Typescript / CSS references. </p><p></p><p>You can copy the custom field safe name by clicking on the copy icon.</p>                                                                                                                                                                                                                                                                                                                                                                                            |
| Description | A description for the table                                                                                                                                                                                | Not mandatory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Private     | Whether the fields value should be shared among [related work items](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items) | <p>By default, any changes in a field's value when made have an immediate effect in all its <a href="../../../work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items">related work items</a>. For example, any changes in a field's value in an Action have an immediate effect in all its related work items i.e. its parent Case, the other Actions of that Case and even any originating Ticket.</p><p></p><p>Switch this option on if you DO want data to be shared among its <a href="../../../work-manager/work-manager-2021.1/working-with-linked-work-items/related-group-vs-linked-work-items">related work items</a> or leave if off if not.</p> |

Click ‘Save’. Now you can create custom data fields *within* the table.

### Adding a field to a table

To add a custom data field to a custom data table, click the '+' icon on the right.

In the following pop-up, fill in the following information:

| Attribute     | Description                                                                                      | Notes                                                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name          | The field name                                                                                   |                                                                                                                                                                                                  |
| Safe Name     | The name of the field to be used if you're referencing it in code.                               | The system will autogenerate this name as you type (a copy of the field name with spaces removed). This Internal Name should be used in any subsequent Custom Card HTML / Typescript references. |
| Description   | A description for the field                                                                      |                                                                                                                                                                                                  |
| Type          | The type of data you want the field to collect e.g. long text / date time etc.                   | See here for more information about the [available types of custom data field](#types-of-field). Mandatory.                                                                                      |
| Default Value | Depending on the type of field you select, you may be able to set a default value for the field. | This is not mandatory                                                                                                                                                                            |

### Editing fields in a table

To edit a field in a custom data table, click to edit the custom table and then click on the menu option on the right of the row of the field you want to edit and select 'Edit'.

When editing a custom table, you are also able to see its activity history by clicking on the Show Activity button. You can see when the custom table was created and by who, as well as if any edits have been made to the custom table, when they were made and by who.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWppRpAP7W8To4ra0xt%2Fimage.png?alt=media\&token=38151e35-3241-43b0-830c-0718519b85f8)

## Creating new fields within the Custom Cards screen <a href="#b-creating-new-fields-within-the-cards-screen" id="b-creating-new-fields-within-the-cards-screen"></a>

Alternatively, you can easily create new custom data fields in the Custom Cards screen itself - simply select the Custom Cards screen from the the menu on the left-hand side of Builder, click the 'add' icon above the list of system fields and fill in the required information in the resulting popup.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpqCDMmRSuwEbES_ZO%2Fimage.png?alt=media\&token=7038377c-3a2d-4d9f-98d6-d8f32b5d246c)
