# Source: https://docs.intelligems.io/analytics/how-to-add-product-groups-to-intelligems-analytics.md

# How to Add Product Groups to Intelligems Analytics

## Background

By default, analytics will display for all products. For certain tests, it may be beneficial to look at the results for certain product groups, or even get as granular as looking at the results for individual products. To do this, you can use the Product Groups dropdown in the Results dashboard. Follow these steps below to set up Product Groups. Product groups can be added anytime before, during or after a test.

## Step 1: Download the COGS template from the Intelligems App

This template pulls data from Shopify and includes a list of all products in your store. As the name states, this template is typically used for uploading cost of goods sold (COGS), but it is also used to upload Product Groups. Feel free to upload both COGS and Product Groups at the same time! You can find the template in the Settings tab under your plan options.

When you click "Download Template" you'll see the download process at the top of the app. Once it has processed, click "Download" and open the file in a spreadsheet editing tool.

## Step 2: Using a spreadsheet editing tool, populate the 'productGroup' column

Input Product Group information into the productGroup column for each product and variant. How you set your product groups up is fully customizable. A few common ways we see brands use this feature include:

* Creating a product group for each unique product
* Creating a product group for each category (e.g. shirts vs pants vs accessories)
* Creating a product group for different price or size tiers (e.g. travel size vs. 8oz vs. 32oz)

In Intelligems, product group mix will be shown on a stacked bar chart. Any product group accounting for at least 1% of net revenue will be shown — others will be grouped together as "Other":

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-945d29892657c7cb6d2ea554cf0032799d268706%2Fproduct_groups.png?alt=media" alt=""><figcaption></figcaption></figure>

You can also [export the data](https://docs.intelligems.io/analytics/experiment-analytics/exporting-data) and analyze in Excel or your preferred data visualization tool.

## Step 3: Save your file and upload it to Intelligems

{% hint style="danger" %}
Before saving your file, convert the `product_id` and `variant_id` from scientific notation to unformatted number notation (No commas, No decimals). Many spreadsheet editors default to scientific notation, but an upload will fail if IDs are not converted.
{% endhint %}

<details>

<summary>Formatting IDs in Excel</summary>

In Excel, choose "Number" formatting, and then remove the decimal places.

The ID should look like: `10732173902`

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-4b973c827cda76d3840c70bf19a17afde758a91b%2Fimage%20\(61\).png?alt=media)

</details>

<details>

<summary>Formatting IDs in Google Sheets</summary>

In Google Sheets, choose "Plain Text" formatting.

The ID should look like: `10732173902`

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-8a2564e528c7784ab1cce4d6ceff808afcd614c4%2Fimage.png?alt=media)

</details>

Once you have added all data and converted the product\_id and variant\_id columns, save your file as an Excel file (.xlsx). Once you have saved your file, head back to the settings tab in the Intelligems app. Select the button to 'Upload COGS Excel File' and upload your file.

## Step 4: Analyze Product Group results in the Intelligems app

{% hint style="warning" %}
Product Group data will be available 1-2 hours after you have uploaded it.
{% endhint %}

Once the data has been uploaded, you'll be able to track the experiment's results by product group in the Product Group tab.
