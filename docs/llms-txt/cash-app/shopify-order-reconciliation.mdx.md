# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/shopify/shopify-order-reconciliation.mdx

***

## stoplight-id: rhohfoj4ymco7

# Shopify Order Reconciliation

Reconcile Afterpay US (New) or Cash App Pay orders on Shopify and ensure all transactions are accounted for.

This page consists of six sections:

* [Search for a specific order in Shopify](#search-for-a-specific-order-in-shopify)
* [Reconcile orders from Shopify Orders export](#reconcile-orders-from-shopify-orders-export)
* [Search for all orders by payment method in Shopify](#search-for-all-orders-by-payment-method-in-shopify)
* [Export all orders by payment method in Shopify](#export-all-orders-by-payment-method-in-shopify)
* [Search for country-specific orders in Shopify](#search-for-country-specific-orders-in-shopify)
* [Create custom report by payment method](#create-custom-report-by-payment-method)

<Note>
  Shopify provide a detailed guide to 

  [Searching, viewing, and printing orders](https://help.shopify.com/en/manual/orders/manage-orders/search-view-print-orders)

  . Use this Shopify guide along with the information on this page.
</Note>

## Search for a specific order in Shopify

To find a specific order, do the following:

1. Go to *Shopify Admin* > *Orders*.

2. Enter the following in the *Orders* search bar, that is the search bar called *Filter Orders*: `receipt.payment_id:`

3. Copy the *Merchant Order No.* from the [Business Hub](https://hub.us.afterpay.com/us) and paste it in search bar after `receipt.payment_id:`

Here is an example in the Shopify *Orders* tab:

![search-for-a-specific-order-new.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/search-for-a-specific-order-new.png)

To access the Shopify Admin, use this [URL](http://shopify.com/admin/orders?query=receipt.payment_id%3A).

## Reconcile orders from Shopify Orders export

To reconcile orders from the export, do the following:

1. Go to *Shopify Admin* > *Orders*

2. Optional: Enter **afterpay** in the Orders search bar.

3. Optional: Enter **"cash app pay"** in the Orders search bar. Notice the quotes for an exact match.

   ![cash-app-pay.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/cash-app-pay.png)

4. Click **Export**.

5. Towards the right side of the exported table, a *Payment ID* column is now available. For both Afterpay US (New) and Cash App Pay orders, this column is populated with the Merchant Reference No. from the [Business Hub](https://hub.us.afterpay.com/us).

For example, here is a Shopify export file:

{/* <img alt="Shopify export file" src="../../../assets/images/Screenshot 2025-03-25 at 10.55.00 AM.png" width="400px"> */}

For example, within the Business Hub the information appears like this:

<img alt="Shopify business hub" src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Screenshot 2025-03-25 at 10.50.01 AM.png" width="700px" />

## Search for all orders by payment method in Shopify

To search for all orders by payment method, do the following:

1. Go to *Shopify Admin* > *Orders*.

2. Enter **"Afterpay US (New)"** or **"Cash App Pay"** (include the quotation marks for an exact match) in the *Orders* search bar.

   ![search-for-all-orders.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/search-for-all-orders.png)

3. Click **Save as** to save this order filter.

<Info>
  If you use both the 

  **Afterpay US (New)**

   payment app and the 

  **Afterpay (New)**

   payment app, you can search for them separately.
</Info>

## Export all orders by payment method in Shopify

To export all your orders by payment method in Shopify, do the following:

1. Go to *Shopify Admin* > *Orders*.

2. Enter **"Afterpay US (New)"** or **"Cash App Pay"** (include the quotation marks for an exact match) in the *Orders* search bar.

3. Click the checkbox at the top of the column on the extreme left to select all the orders (see picture below) and click **Export** at the top right of the window.

   ![export.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/export.png)

4. The Export orders popup appears. Click the **Selected \[n] orders** radio button, and select what type of file you want for the exported data.

   ![export-orders.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/export-orders.png)

5. Click **Export orders**.

## Search for country-specific orders in Shopify

This is a useful way to identify cross-border trade (CBT) orders. Do the following:

1. Go to *Shopify Admin* > *Orders*.

2. Enter a search term in the search bar. For example, in the picture below, the search term is **canada afterpay**. This search shows all the Canadian Afterpay orders with their status and other information.

   ![country-specific.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/country-specific.png)

## Create custom report by payment method

If you use Advanced Shopify or Shopify Plus to host your store, you can use the Custom Report feature to find Afterpay US (New) and Cash App Pay orders.

To do this, you create and run a custom report for Orders by Payment Type. Start by going to your store's Shopify Admin page. Then go to *Analytics* > *Reports* > *Create custom report*.

For more information about how to run reports, see [this information](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types) from Shopify, along with [this information](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/custom-reports) on custom reports.
