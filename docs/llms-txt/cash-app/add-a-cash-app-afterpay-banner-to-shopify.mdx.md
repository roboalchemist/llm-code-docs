# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/shopify/add-a-cash-app-afterpay-banner-to-shopify.mdx

***

stoplight-id: zhskam418976m
internal: true
--------------

# Add a Cash App Afterpay Banner to Shopify

Banners display Cash App Afterpay information at the top of your Shopify page, as shown in the images below.

To add a Cash App Afterpay banner, you must edit your store's code. Before proceeding, ensure that:

* The [Afterpay US](https://apps.shopify.com/afterpay-us) payment app is already installed and running on your online store

* You have chosen a banner that aligns with the guidelines

<Info title="Recommendation">
  You are changing your online store's code, so be careful. We recommend you create a duplicate page and only publish it once you have verified the changes.
</Info>

## Steps to Add the Banner

1. Click **Actions** and select *Edit Code* from the drop-down menu.

2. Scroll down to *Sections* and click **Add a new section**.

3. In the *Create a new section called* field enter **cash-app-afterpay-banner**. The *cash-app-afterpay-banner.liquid* tab appears.

4. Delete the code that populates the *cash-app-afterpay-banner.liquid* tab.

### Add the Liquid file

1. Click the link to the [banner code snippet](https://static.afterpay.com/shopify-cash-app-afterpay-banner-liquid.html).

2. Click the **Copy to Clipboard** button.

3. Paste the banner code snippet into the *cash-app-afterpay-banner.liquid* tab.

4. Click **Save**.

### Editing the Theme Liquid file

1. Open the `theme-liquid` file.

2. Locate the line `{% sections 'header-group' %}` or `{% section 'header' %}`.

3. Add `{% section 'cash-app-afterpay-banner' %}` above this line. In the example below, it is added to line 4:

   ```
   <div class = "black-body"></div>
   {% section 'popup' %}
   {% section 'announcement-bar' %}
   {% section 'cash-app-afterpay-banner' %}
   {% section 'header' %}
   <div id="PageContainer" class="is-moved-by-drawer">
   ```

4. Click **Save**.

To verify the changes, click **Preview** and check for the banners appearance at the top of the page.

The images below illustrate a white, black, and green banner:

![white-banner-new.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/white-banner-new.png)

<br />

![black-banner-new.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/black-banner-new.png)

<br />

![green-banner-new.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/green-banner-new.png)

### Changing the Banner Color

To change the banner color:

1. Login to your **Shopify Admin** and navigate to your **Theme Settings** page: Go to **Online Store**> **Themes**.

2. Click **Customize** to change the theme with the Cash App Afterpay Banner.

   ![publish-customize.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/publish-customize.png)

3. Click **Cash App Afterpay Banner**.

   ![home-page.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/home-page.png)

4. Click **Banner color**.

5. Select **Black**, **White**, or **Green**.

   ![shopify-banner-for-caap.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/shopify-banner-for-caap.png)

6. Click **Save**.

## Brand Assets

For more examples and information on brand assets, including banners, see the [Brand Assets](/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/brand-assets) section of this guide.
