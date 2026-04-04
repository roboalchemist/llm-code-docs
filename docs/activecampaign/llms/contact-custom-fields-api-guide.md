# Source: https://developers.activecampaign.com/reference/contact-custom-fields-api-guide.md

# Contact Custom Fields API Guide

Using the API to add and manage Custom Fields for your Contacts

This guide will show you how to use the API to create Custom Fields on your Contacts, and populate those fields with data.

<Image title="new_custom_field.jpg" alt={2228} align="center" width="smart" border={true} src="https://files.readme.io/dec3025-new_custom_field.jpg">
  Example Custom Field on a Contact
</Image>

#### Custom fields are a vital tool for adding data to your contacts. Creating the Custom Fields, assigning those fields to subscribers, and populating those fields with options and data is easily done through the API.

## Glossary of Terms

### Field

* **Fields** are places for storing various types of data on Contact Record.
* **Custom Fields** are Fields created by an organization to store unique data points that fall beyond the scope of the standard Fields already provided on a Contact record, ie: *first name, last name, email, etc*

### Field Type

* **Field Types** are the different types of data a Field can store, and must be set on Field creation. These types include text area, *text*, *date*, *dropdown*, *multiselect*, *radio*, *checkbox*, *hidden*, and *datetime*.

### Field Option

* **Field Options** are the available options provided for certain Field Types. **Example:** A dropdown Field needs to be populated with a list of options, but a text field would not need Field Options, as it is empty field for entering any type of text.

### Field Value

* **Field Values** are the actual data points stored inside the Custom Fields. **Example:** A Custom *text* Field on a Contact called "Team" could have the Field Value "Blue", or a *dropdown* Custom Field called "Team Selection" has the options: "Blue", "Red", "Green". If "Blue" is selected, "Blue" the Field Value for that Custom Field is "Blue".

### Field Relationship

* **Field Relationships** are the relationship between a Contact List, and a Custom Field. **Example:** An organization has a Contact List called "Employees" and another list named "Customers." A Custom Field called "Department" could be placed on all Contacts in the "Employees" list, and another Custom Field called "Uses Coupons" could be placed on all Contacts in the "Customers" list, these are *Field Relationships to Contact Lists.*

## Creating Your First Custom Field

There are [several different available types of Custom Fields](https://developers.activecampaign.com/reference/create-a-contact-custom-field), but we will be creating a "listbox" type for this example. Creating a Custom Field can be accomplished in three steps.

### STEP 1: Create the Custom Field

#### Create a Custom Field by making a `POST` to `https://{{yourAccountName}}.api-us1.com/api/3/fields`.

In addition to `type`, there are several other options you can change inside the JSON body to manipulate the formatting, visibility, and description for the field:

```json POST - https://{{yourAccountName}}.api-us1.com/api/3/fields
{
    "field": {
        "title": "Example List Box",
        "descript": "Field description goes here",
        "type": "listbox",
        "perstag": "listBoxTagName",
        "group": 1,
        "show_in_list": true,
        "rows": 0,
        "cols": 0,
        "visible": true,
        "ordernum": 0
    }
}
```

The `type` key is what defines the type of Custom Field being created. There are multiple options, including:

<Image title="Image 6-2-2022 at 3.42 PM.jpg" alt={358} align="center" src="https://files.readme.io/4b826e1-Image_6-2-2022_at_3.42_PM.jpg">
  "listbox" - A list of options, similar to `dropdown` , enabling a single selection
</Image>

<Image title="Image 6-2-2022 at 3.43 PM.jpg" alt={770} align="center" src="https://files.readme.io/2cb4917-Image_6-2-2022_at_3.43_PM.jpg">
  "radio" - A list of radio buttons/options, enable a single selection
</Image>

<Image title="Image 6-2-2022 at 3.43 PM (1).jpg" alt={656} align="center" src="https://files.readme.io/d6fa8ac-Image_6-2-2022_at_3.43_PM_1.jpg">
  "checkbox" - A list of selectable checkboxes, enabling multiple selection
</Image>

You should receive a response from your API call of `201 - CREATED` upon completion. The response will contain the randomly-generated `id` of the Custom Field, as well as other metadata :

```json 201 RESPONSE
{
    "field": {
        "title": "Example List Box",
        "descript": "Description goes here",
        "type": "listbox",
        "perstag": "LISTBOXTAGNAME",
        "show_in_list": 1,
        "rows": 0,
        "cols": 0,
        "visible": 1,
        "ordernum": 1,
        "created_by": "1",
        "updated_by": "1",
        "cdate": "2022-06-15T15:04:11-05:00",
        "udate": "2022-06-15T15:04:11-05:00",
        "links": {
            "options": "https://yourAccountName.api-us1.com/api/3/fields/34/options",
            "relations": "https://yourAccountname.api-us1.com/api/3/fields/34/relations"
        },
        "id": "34"
    }
}
```

Note that for this guide, the automatically assigned `id` for this custom field is `34`.

Your listbox should now be created, and it's existence can be verified with a `GET` call to\
`https://{{yourAccountName}}.api-us1.com/api/3/fields`:

```json POST - https://{{yourAccountName}}.api-us1.com/api/3/fields
{
    "fieldOptions": [],
    "fieldRels": [],
    "fields": [
        {
            "title": "Example List Box",
            "descript": "Description goes here",
            "type": "listbox",
            "perstag": "LISTBOXTAGNAME",
            "defval": null,
            "show_in_list": "1",
            "rows": "0",
            "cols": "0",
            "visible": "1",
            "service": "",
            "ordernum": "1",
            "cdate": "2022-06-15T15:04:11-05:00",
            "udate": "2022-06-15T15:04:11-05:00",
            "created_timestamp": "2022-06-15 15:04:11",
            "updated_timestamp": "2022-06-15 15:04:11",
            "created_by": "1",
            "updated_by": "1",
            "options": [],
            "relations": [],
            "links": {
                "options": "https://yourAccountName.api-us1.com/api/3/fields/34/options",
                "relations": "https://yourAccountName.api-us1.com/api/3/fields/34/relations"
            },
            "id": "34"
        }
    ],
    "meta": {
        "total": "1",
        "selected": null
    }
}
```

Note that `fieldOptions` and `fieldRels` are empty lists. That is because we have not populated this field with options (step 2) or assigned this Field to a list (step 3).

### STEP 2: Populate the Custom Field with Options

Populate the Custom Field created in Step 1 with a call to `https://{{yourAccountName}}.api-us1.com/api/3/fieldOption/bulk`, with a JSON body containing the options you want contained in this Custom Field:

```json POST - https://{{yourAccountName}}.api-us1.com/api/3/fieldOption/bulk
{ 
     "fieldOptions": [
        {
            "orderid": 1,
            "value": "Option A",
            "label": "Option A",
            "isdefault": false,
            "field": "34"
        },
        {
            "orderid": 2,
            "value": "Option B",
            "label": "Option B",
            "isdefault": false,
            "field": "34"
        },
        {
            "orderid": 3,
            "value": "Option C",
            "label": "Option C",
            "isdefault": false,
            "field": "34"
        }
    ]
}
```

In this JSON body:

* `orderid`: Edits the order these options will be displayed in
* `value`: The value of the option
* `label`: The label displayed in the UI for the option
* `isdefault`: If the option should be pre-selected/default
* `field`: The custom field these options should appear inside

You should receive a `201 - CREATED` response to a successful call:

```json 201
{
    "fieldOptions": [
        {
            "orderid": 1,
            "value": "Option A",
            "label": "Option A",
            "isdefault": 0,
            "field": "34",
            "cdate": "2022-06-15T15:17:14-05:00",
            "udate": "2022-06-15T15:17:14-05:00",
            "links": {
                "field": "https://yourAccountName.api-us1.com/api/3/fieldOptions/58/field"
            },
            "id": "58"
        },
        {
            "orderid": 2,
            "value": "Option B",
            "label": "Option B",
            "isdefault": 0,
            "field": "34",
            "cdate": "2022-06-15T15:17:14-05:00",
            "udate": "2022-06-15T15:17:14-05:00",
            "links": {
                "field": "https://yourAccountName.api-us1.com/api/3/fieldOptions/59/field"
            },
            "id": "59"
        },
        {
            "orderid": 3,
            "value": "Option C",
            "label": "Option C",
            "isdefault": 0,
            "field": "34",
            "cdate": "2022-06-15T15:17:14-05:00",
            "udate": "2022-06-15T15:17:14-05:00",
            "links": {
                "field": "https://yourAccountName.api-us1.com/api/3/fieldOptions/60/field"
            },
            "id": "60"
        }
    ]
}
```

### STEP 3: Assign the Custom Field to a List

Step 1 created the field, and step 2 assigned it options, but the field isn't being displayed on any Contacts inside the ActiveCampaign user interface. That is because we need to assign this Custom Field to the contacts in a List. This connection between a List and a Custom Field is called a "field relationship."

You can get the `id` of the list you want to assign this Custom Field to with a `GET` call to `https://{{yourAccountName}}.api-us1.com/api/3/lists`. This call will return the Contact Lists for this account. An `id` is assigned to each list. For this tutorial, we will be using the `id` of `1`

Using this Contact List `id`, assign the Custom Field to the list by making a `POST` call to `https://{{yourAccountName}}.api-us1.com/api/3/fieldRels`:

```json POST - https://{{yourAccountName}}.api-us1.com/api/3/fieldRels
{
    "fieldRel": {
        "relid": 1,
        "field": "34"
    }
}
```

In this JSON body:

* `relid`: The `id` of the Contact List you want to assign the Custom Field to
* `field`: The `id` of the Custom Field created in Step 1

A `201 - Created` response should return a `relid` when successful. This `relid` will be used to remove a custom field from a Contact List.

<Image title="Image 6-15-2022 at 4.41 PM.jpg" alt={889} align="center" src="https://files.readme.io/5d46134-Image_6-15-2022_at_4.41_PM.jpg">
  The custom field should now be available on every contact subscribed to the List you assigned the Field Relationship.
</Image>

## Populating Custom Field Values on a Contact

To populate a Custom Field for an individual Contact, make a `POST` call to `https://{{yourAccountName}}.api-us1.com/api/3/fieldValues`

```json POST - https://{{yourAccountName}}.api-us1.com/api/3/fieldValues
{
    "fieldValue": {
        "contact": 19,
        "field": 34,
        "value": "||Option A||Option C||"
    }
}
```

In this JSON body:

* `contact`: The `id` of the contact
* `field`: The `id` of the custom field
* `label`: The label displayed in the UI for the option
* `value`: The value to be entered into that custom field

In Step 1 we created a Custom Field with the type of `listbox`, which supports multiple selections. Therefore,  `value` of `||Option A||Option C||` is valid data because the `||` divides the selections we want chosen for this Contact.

* [Learn about Custom Field Types](https://developers.activecampaign.com/reference/create-a-contact-custom-field)
* [Learn more about acceptable Custom Field Values](https://developers.activecampaign.com/reference/create-fieldvalue)

<Image title="Image 6-15-2022 at 5.05 PM.jpg" alt={836} align="center" src="https://files.readme.io/49dfa28-Image_6-15-2022_at_5.05_PM.jpg">
  This Contact's Custom Field has successfully been populated with the data sent via the API.
</Image>

> 📘 Values not showing up? Check the following:
>
> * The Value being sent must match the type of data the field was built to accept (see step 1).
> * The Value being sent must match *exactly* to the Options provided (see step 2).
> * The Contact must be subscribed to the List the Custom Field has a Relationship to (see step 3).

## Additional Resources

### Custom Field Documentation

* [Create a custom field](https://developers.activecampaign.com/reference/create-a-contact-custom-field)
* [Retrieve a custom field](https://developers.activecampaign.com/reference/retrieve-a-custom-field-contact)
* [Update a custom field](https://developers.activecampaign.com/reference/update-a-field)
* [Delete a custom field](https://developers.activecampaign.com/reference/delete-a-field)
* [List all custom fields](https://developers.activecampaign.com/reference/retrieve-fields)\
  -[ Create a custom field/list relationship](https://developers.activecampaign.com/reference/create-a-custom-field-relationship-to-lists)
* [Bulk create custom field options](https://developers.activecampaign.com/reference/create-custom-field-options)
* [Delete a custom field relationship](https://developers.activecampaign.com/reference/delete-a-custom-field-relationship-to-lists)

### Custom Field Values Documentation

* [Create a custom field value](https://developers.activecampaign.com/reference/create-fieldvalue)
* [Retrieve a custom field value](https://developers.activecampaign.com/reference/retrieve-a-fieldvalues)
* [Update a custom field value for a contact](https://developers.activecampaign.com/reference/update-a-custom-field-value-for-contact)
* [Delete a custom field value](https://developers.activecampaign.com/reference/delete-a-fieldvalue-1)
* [List all custom field values](https://developers.activecampaign.com/reference/list-all-custom-field-values)