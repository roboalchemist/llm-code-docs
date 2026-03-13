# Source: https://docs.logrocket.com/docs/shopify-capture-app.md

# Shopify Capture (Shopify App)

How to capture additional data from your Shopify site using the LogRocket App from the Shopify App store

LogRocket makes it easy to capture valuable data and understand user behavior on your Shopify checkout pages. Shopify has specific restrictions on how data can be sent to other tools from their checkout pages, which may limit the tracking options you’re used to. However, by following the steps below, you can collect checkout data and send it to LogRocket for deeper insights into customer behavior.

<Callout icon="📘" theme="info">
  **Who can use this feature?**

  In order for LogRocket to capture video replay on checkout pages the store must be on a Shopify Plus plan, as that is the only Shopify plan that includes [Shopify's Advanced DOM Pixel Events API](https://shopify.dev/docs/api/web-pixels-api/advanced-dom-events). If your shop is not currently on a Shopify Plus plan then LogRocket will only capture standard Shopify events without any video replay on Shopify checkout pages.
</Callout>

## Step 1 - Install the LogRocket App from the Shopify App Store

Shopify limits the ability for scripts to run on checkout pages. Instead, they make it possible to capture some events from the checkout process for tracking user behavior on these pages. To enable this capture, follow these steps:

1. Go to the [LogRocket App](https://apps.shopify.com/logrocket) in the Shopify App Store.
2. Click **Install**
3. Review the information that the LogRocket App requires access to and then click **Install**.
4. Fill in the **App ID** field on the LogRocket App configuration page with your LogRocket project's App ID and then click **Save**.
5. Your store is now configured to capture additional Shopify events throughout user sessions, including on checkout pages.

<Callout icon="⚠️" theme="warn">
  If you have previously installed LogRocket on your Shopify store using the [Custom Pixel approach](https://docs.logrocket.com/docs/beta-shopify-capture#/), then be sure to deactivate and delete the custom pixel after installing the LogRocket App. If you leave the custom pixel activated then this will lead to duplicate Shopify events being captured in LogRocket sessions.
</Callout>

## Step 2 - Add the LogRocket snippet to your Shopify theme

In order to capture user activity across your entire Shopify store using LogRocket, the LogRocket script snippet must be added to your store's Shopify theme.

### Option A - Use the LogRocket Script Initializer app embed block

This is the **Recommended** approach to adding the LogRocket snippet to your Shopify theme.

1. From the configuration page of the LogRocket App click on the link to the *Script Initializer app embed block* in the **Required Settings** section. This should take you directly to the theme customization screen in your store with the LogRocket Script Initializer app embed selected and opened up.
2. Fill in the **App ID** field with your LogRocket project's App ID.
3. Optional: Fill in any LogRocket configuration options as a JavaScript object in the **Options** field.
4. Toggle the Script Initializer app embed on.
5. Save the changes to your theme.

### Option B - Manually install the snippet

1. Review the [Quickstart](https://docs.logrocket.com/docs/quickstart) instructions to get the LogRocket script tag.
2. Edit the code of your store's theme and at the start of the `<head>` tag in your Shopify site's `theme.liquid` layout insert the LogRocket script tag.
3. Save the changes to your theme.

## Step 3 - Identify your customers in LogRocket (Optional)

We recommend adding code similar to this into your `theme.liquid` template to identify the customers who have an account with your store. Make sure the code is added *below* where the LogRocket script is initialized on the page. If you are using the Script Initializer app embed block to initialize LogRocket then it is recommended to insert the script with the `<body>` of the page before the closing `</body>` tag to ensure that LogRocket is available when the identify script runs:

```javascript
var customerOrders = {{ customer.orders | json }} || [];
var customerData = {
  id: "{{ customer.id }}",
  email: "{{ customer.email }}",
  name: "{{ customer.name }}",
  phone: "{{ customer.phone }}",
  totalSpent: "{{ customer.total_spent | money }}",
  customerOrders: customerOrders.length,
};

if (customerData.id !== '') {
  window.LogRocket && window.LogRocket.identify(customerData.id, customerData);
}
```

### Include user identity information on Shopify events

If you want user identity information associated with all Shopify events (including checkout activity) then we recommend that you set the the `persistUserIdInfo` configuration setting to `true` when initializing LogRocket. This will allow user identity information to be persisted within a LogRocket session while a user navigates between web applications on different subdomains (i.e. from `www.mystore.com` to `checkout.mystore.com`). This type of situation is common if you are running a [headless Shopify store](https://www.shopify.com/plus/solutions/headless-commerce) on a separate domain from your Shopify store checkout page.

Ensuring that user identity is associated with Shopify events is necessary for calculating user retention metrics tied to any Shopify event (ex. determining what percentage of users complete another purchase after making their first purchase).

## Known Limitations

Please note that Conditional Recording is not yet supported based on Shopify Events.

LogRocket can provide valuable insights into your Shopify Plus checkout experience, but it’s important to note that Shopify’s security model places certain limits on the data that any third-party analytics or session replay tool can access. The points below outline what Shopify’s data access policies allow (and restrict) for third-party tools like LogRocket:

1. Checkout methods like Apple Pay, PayPal, and other accelerated flows may not be fully captured. Events occurring before the redirect can appear in session replay, but the steps that take place inside the accelerated checkout environment are outside the merchant’s control and not exposed through Shopify’s APIs.
2. Due to Shopify’s security restrictions, browser-side LogRocket calls — such as [logrocket.identify](https://docs.logrocket.com/reference/identify#/) or [logrocket.track](https://docs.logrocket.com/reference/track#/) — aren’t allowed to run on Checkout pages. These APIs are disabled to prevent code execution within the secure checkout environment.
3. Shopify does not provide access to [Performance Data](https://docs.logrocket.com/docs/data-collected#/performance-data) through its APIs, so LogRocket cannot display these metrics for checkout pages. Shopify monitors and optimizes checkout performance directly for all merchants.
4. Console logs and network requests are not exposed to LogRocket from Shopify Checkout. This means uncaught exceptions, HTTP request/response details, timings, and network error URLs will not appear in session replay.
5. Checkout activity for customers using ShopPay will not be captured because it runs on a unique domain (shop.app) from the standard web checkout and will not run the LogRocket Shopify App.
6. If a buyer has opted out of Marketing & Analytics permissions within Shopify (i.e. declined the cookie policy), their checkout activity and Shopify events will not be captured by LogRocket in compliance with Shopify’s consent framework.