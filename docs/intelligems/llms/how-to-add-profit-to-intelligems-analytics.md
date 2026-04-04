# Source: https://docs.intelligems.io/analytics/how-to-add-profit-to-intelligems-analytics.md

# How to Add Profit to Intelligems Analytics

## Background

While top-line metrics such as conversion and revenue are possible for us to track "out of the box", additional cost data is required to measure profit.

Updating cost assumptions, including COGS per product, will apply retroactively to existing experiments, so you can do this even after an experiment has started collecting data.

There are two ways that you can provide COGS information to Intelligems, both found on the [Settings page](https://app.intelligems.io/settings) of the Intelligems app.

## Option 1: Automatic Management

If you include your COGS information in Shopify and don't need to make any changes to it before uploading to Intelligems, this is your best option. We will pull in all COGS that you have in Shopify when you click this button, and you can toggle on a daily update as well. Note that you can still set values for your average shipping / fulfillment cost per order and transaction fee percent within the manual section if you choose this option. Also note that if you choose this option, any manually defined Product Groups in your COGS upload will be ignored.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-236a7679bde317a1692c7ed898a1164b24cdafa2%2FScreenshot%202023-11-28%20at%2012.50.40%20PM.png?alt=media" alt=""><figcaption></figcaption></figure>

## Option 2: Manual Management

If you do not include your COGS information in Shopify or would like to make any changes to how it is uploaded to Intelligems, this is your best option. Follow the steps below to upload COGS using this method.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-8c574abf155162e9fd66ee00dde8870e4f5ce915%2FScreenshot%202024-06-04%20at%201.02.59%20PM.png?alt=media" alt=""><figcaption></figcaption></figure>

### Step 1: Determine what cost structure best aligns with your store or business model

We have two options for how we incorporate the cost of shipping and fulfillment:

* **Option 1:** *Include* the cost of shipping and fulfillment in COGS for each product variant. For example, Product A has COGS of $5, including shipping and fulfillment
* **Option 2:** *Exclude* the cost of shipping and fulfillment from product cost and, instead, factor it in at the order level. For example, Product A has COGS of $3, Product B has COGS of $4 and each order costs $10 to ship and fulfill. If this reflects the way your store accounts for COGS, please include the shipping and fulfillment cost per order in the body of the email you send to Intelligems with your COGS data

{% hint style="info" %}
Incorporating other cost models will require custom analyses outside of the Intelligems analytics product. Such analyses may be possible using our data exports. Please reach out to <support@intelligems.io> if you have questions around this.
{% endhint %}

### Step 2: Download the COGS template from the Intelligems App

You can find this in the Settings tab. When you click "Download Template", you'll see the download process at the top of the page. Once it is processed, click "Download" and open the file in a spreadsheet editing tool.

### Step 3: Using a spreadsheet editing tool, populate the 'cogs' column

The file will download as an .xlsx file, and should be saved as a .xlsx file to upload it.

Input COGS information into the cogs column for each product and variant. This information may already be filled out if your COGS is up to date in Shopify! Feel free to edit as needed.

A few notes as you do this:

#### Formatting Product and Variant IDs

{% hint style="danger" %}
Before saving your file, convert the `productId` and `variantId` from scientific notation to unformatted number notation (no commas, no decimals). Many spreadsheet editors default to scientific notation, but an upload will fail if IDs are not converted.
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

#### Pulling data from your own datasets

If you keep COGS data in a separate spreadsheet, we recommend copying that spreadsheet into the download from Intelligems. There are several fields (product\_id, variant\_id, SKU, etc.) that you can use to pull in existing COGS data. The example below shows how you could use an Excel formula to add COGS data from a source that contains COGS by SKU. In this example, column B of the `COGS Data Source` tab (not pictured) contains SKUs and column C contains COGS corresponding to those SKUs. In this case, the COGS for SKU-38 is $5.00.

<div><img src="https://help.intelligems.io/hubfs/Knowledge%20Base%20Import/d33v4339jhl8k0.cloudfront.netdocsassets624c7e54ed4a0c44b4e6013aimages6283f47cb2de5178f88848e1file-kQUoNaQyiv.png" alt=""> <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f0cdb77b0d15e9660ff790d09b69f5c8e2d7a7db%2FExcel%20example%20%E2%80%93%20COGS%20%E2%80%93%20M39.png?alt=media" alt=""><figcaption></figcaption></figure></div>

The formula in cell M39 above is:

```excel-formula
  =INDEX('COGS Source Data'!$C:$C,MATCH(E39,'COGS Source Data'!$B:$B,0))
```

{% hint style="info" %}
We recommend including COGS for all products on your store, even if they're not part of the test. Providing COGS for only some products may result in overstated profit for the products with missing COGS information.
{% endhint %}

### Step 4: Save your file and upload it to Intelligems

Once you have added all data and converted the `productId` and `variantId` columns, save your file. See below for a list of best practices to keep in mind when saving your COGS files:

* A file saved with a .csv extension will automatically convert any numbers in scientific notation to rounded numbers and cause information to be lost. To prevent this, be sure to convert all numbers from scientific notation to unformatted numbers (i.e. 12345678890) before saving a document as a CSV
* If you're working from a spreadsheet that has multiple tabs, it cannot be saved as a CSV. You'll need to start a new file with only one tab and save that to a CSV

Once you have saved your file, head back to the settings tab in the Intelligems app. Select the button to 'Upload COGS' and upload your file.

If you have chosen to incorporate shipping and fulfillment costs at the order level, you can also input your average shipping and fulfillment cost here. If you have chosen to include that cost at the product level in your COGS download, you can leave this field blank. You can also add a transaction fee percentage if you would like to include that information in the profit analysis.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-151b2d9e750f3d1ac64ce83e5282b4ba9b66c7be%2FScreenshot%202023-10-20%20at%203.30.44%20PM.png?alt=media" alt="" width="373"><figcaption></figcaption></figure>

### Step 5: Analyze profit results in the Intelligems app

{% hint style="info" %}
Profit data should be available immediately after you have uploaded COGS, and will update retroactively for all tests.
{% endhint %}

Once the data has been uploaded, you'll see a 'Profit' tab in the drop down views, on your Results page. You'll be able to track the experiment's measurement of profit per site visitor and profit per order. See more in the analytics dashboard for the analytics included under the Profit tab.
