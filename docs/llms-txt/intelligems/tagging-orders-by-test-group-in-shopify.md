# Source: https://docs.intelligems.io/analytics/experiment-analytics/tagging-orders-by-test-group-in-shopify.md

# Tagging Orders by Test Group in Shopify

## Background

By default, when an order is created in Shopify and the user was included in an Intelligems test(s), there are a few ways that Intelligems will show up on the order within your Shopify admin portal. One thing that will not show up by default is which test or test groups a customer was in. You can always get this information by using our order export feature in the Intelligems app, but by following the below steps to setup a Shopify Flow, you will automatically get a tag on your Shopify orders to give you this information.

{% hint style="warning" %}
You'll have to set up a Shopify Flow for each test as they are based on the unique Test Group IDs that are assigned to each test group.
{% endhint %}

## Step 1: Confirm that the "Add Test Group ID" setting is toggle on

Before completing any other steps please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for help enabling the setting that allows Intelligems to add the test group ID. Please note that this will add the test group ID as a line item property - some brands use line item properties for other workflows, so it is important to check that this will not break anything that you are currently doing.

## Step 2: Get Test Group IDs

For every test set up in the Intelligems app, each test group receives a unique ID. You can get this information by clicking the "Show Info" option in the more options menu:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-4d7f6f30f80395af7916baccf5cf8ec7c09001e6%2FShow%20Info.gif?alt=media" alt=""><figcaption></figcaption></figure>

## Step 3: Set up a workflow in Shopify Flow

If you have not already, download the Shopify Flow app [here](https://apps.shopify.com/flow?shpxid=c54acb63-0029-409E-E10D-2F3BA56235EC). Once you are in the app:

1. Click "Create workflow" in the top right, followed by "Select a trigger".
2. For the trigger, select "Order created".
3. Click the blue plus sign in the "Order created" card and select "Condition".
4. Click "Add criteria" > "Order" > "lineItems" > "customAttributes" > "value".
5. Change the "Equal to" dropdown to "Includes" and paste the test group ID (from Step 2) in the "Value" box.
6. Click the blue plus sign next to "Then" in the "Check if..." card and select "Action".
7. Click "Add order tags" and type the tag you would like to add to the orders for this test group(s). This tag will be added to all orders completed in this test group(s) in Shopify. When it is done, your Shopify Flow should look similar to the below.
8. Click "Turn on workflow" in the top right.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-e2dd01c4c24e3f8a9b9f2ec532cbb0f3ab0ef1d0%2FScreenshot%202023-06-16%20at%2012-29-14%20PM-png.webp?alt=media" alt=""><figcaption></figcaption></figure>
