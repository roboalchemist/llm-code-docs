# Source: https://docs.apify.com/platform/integrations/airtable.md

# Airtable integration

**Learn how to integrate Apify with Airtable. This article shows you how to use the Apify extension on Airtable.**

***

https://www.airtable.com/ is a cloud-based platform for organizing, managing, and collaborating on data. With the Apify integration for Airtable, you can automatically upload Actor run results to Airtable after a successful run.

This integration uses OAuth 2.0, a secure authorization protocol, to connect your Airtable account to Apify and manage data transfers.

## Connect Apify with Airtable

To use the Apify integration for Airtable, ensure you have:

* An https://console.apify.com/
* An https://www.airtable.com/

## Types of integration

You can integrate Apify with Airtable using one of two options:

* *Apify extension* on Airtable website.
* *Console integration* on the Actor page.

This guide explains how to use the *Apify extension*. For console integration instructions, see the https://docs.apify.com/platform/integrations/airtable/console.md documentation

## Setup

### Install Apify extension

Go to https://airtable.com and open the base you would like to work with. Press the **Tools** dropdown in the top right corner and click **Extensions**.

![Access the extensions tab on Airtable UI by pressing tools button](/assets/images/airtable_tools_button-97e8312a2de4dee3486a59846cccc25e.png)

Search for Apify extenison and install it

![Search for the Apify extension on Airtable](/assets/images/airtable_search_apify_extenison-55d37506218ef2a1bc40db96e920122c.png)

Open the Apify extension and login using OAuth 2.0 with your Apify account. If you dont have an account, visit https://console.apify.com/sign-up page.

![Open Apify extension and login](/assets/images/airtable_login-730de1f8e5f8d8c81dac5142be8218db.png)

## Extension overview

The Apify extension helps you map and import data into your Airtable base.

### Features

The extension provides the following capabilities:

* Run Actors
* Run tasks
* Get dataset items
* Map and import the data into your base

![Apify extension overview](/assets/images/airtable_overview-f520e2f269afc4a1cd2a4466e2e8b039.png)

### Run Actor

1. Select any Actor from **Apify store** or **recently used Actors** ![Select Actor screen](/assets/images/airtable_actor_select-9e370b7eaa0f3a36237df7c28139794c.png)

2. Fill in the Actor input form. ![Configure Actor screen](/assets/images/airtable_configure_actor-4df721d03570aefc09a86675b56de3b8.png)

3. Run the Actor and wait for results ![Run the Actor](/assets/images/airtable_actor_run-50a70bdc1245024200fb4e5d0bde4817.png)

### Run task

You can select and run any saved Apify task directly from the extension to reuse preconfigured inputs.

![Run task](/assets/images/airtable_task-4381890f7ba3e022f7c5c2bc0f943570.png)

### Get dataset items

Retrieve items from any Apify dataset and import them into your Airtable base with a single click.

![Get dataset](/assets/images/airtable_dataset-fbe6da8509ec634034235eec569211fb.png)

### Map data to Airtable

This section explains how to map your Actor run results or dataset items into your Airtable base.

#### Understanding mapping rows

The Apify extension provides UI elements that allow you to map dataset fields to Airtable fields.

![Run the Actor](/assets/images/airtable_mapping_row-b2cf0e9b2bcf1f5781468a89cbbe8f02.png)

**Source:** The dataset field from Apify. **Target:** The target Airtable field label. For **new** mode, this creates new fields in your table. **Field Type:** The type of the target Airtable field. For **new** mode, you must specify this field type.

#### Select fields to map

The preview window next to the mapping rows will help you view and pick fields from the dataset. A period (`.`) in field labels indicates nested elements within an object.


```
{
    crawl: {
        depth: 'the field you selected',
    }
}
```


![Preview dataset fields](/assets/images/airtable_field_previews-d957ceda06800df4067eee29c5793b54.png)

#### Automatic field matching

The Apify extension examines the field labels in your table and matches them with dataset fields, providing a default list of mappings.

*How it works*: For a source field like `crawl.depth`, the extension checks for fields in your table with labels matching either `depth` or `crawl.depth`. When it finds a match, it automatically adds a mapping row.

#### Import operations

1. **CREATE**: Creates a new table for each run of this integration.
2. **APPEND**: Adds new records to the specified table. If the table doesn't exist, a new one is created.
3. **OVERWRITE**: Replaces all records in the specified table with new data. If the table doesn't exist, a new one is created.

#### Filter duplicate records

To prevent duplicate records, select a **Unique ID** on the data mapping step. The unique ID is added to the list of mapping rows. Ensure it points to the correct field in your table. During import, the extension filters data by existing values in the table. ![Select unique ID](/assets/images/airtable_unique_id-56f97681a59d1a2ff9a42d14ec3f08ce.png)

#### Preview Mapped Data

Preview the results and start the import

![Preview Mapped Data](/assets/images/airtable_preview-a9b08f9eb595d9a98bcfba6b59c5c138.png)
