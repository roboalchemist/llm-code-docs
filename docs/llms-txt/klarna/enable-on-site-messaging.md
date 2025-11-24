# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/vtex/conversion-boosters/enable-on-site-messaging.md

# Enable On Site Messaging via Vtex

## Klarna’s **On-site messaging** enhances customer engagement and boosts conversions by displaying Klarna’s flexible payment options throughout the shopping experience. This section provides step-by-step guidance on installing, configuring, and optimizing Klarna On-site messaging in VTEX.

## **Activating On-site messaging in Klarna merchant portal**

Before setting up On-Site Messaging in VTEX, you need to activate it in the Klarna Merchant Portal and retrieve your **Client Identifier**.

### **Steps to activate On-site messaging in Klarna merchant portal**

**Log in to the Klarna Merchant Portal** using your merchant credentials and navigate to **Conversion boosters\> On-site messaging**, select the appropriate **store** from the dropdown menu, and click **Get started**.


![OSM merchant portal](MP_-_OSM.png)
*OSM merchant portal*

A pop up will appear asking you to **register the origin domain** of the store where you will be using On-site Messaging, enter the origin and click **Register**.


![Register origin](Register_origin.png)
*Register origin*

Your **Client Identifier** will be generated. Copy it as you will need it to configure OSM in VTEX.


![Client ID for OSM in merchant portal](Enable_On_Site_Messaging_via_Vtex_1740778816378.png)
*Client ID for OSM in merchant portal*

## **Installing Klarna On-site messaging app in VTEX**

To enable Klarna’s On-site Messaging in VTEX, you need to install the app.

1.  Open a terminal and log in to your **VTEX account** using the **VTEX IO CLI**.
2.  Run the following command to install the Klarna OSM App: `vtex install klarnapartnerglobal.klarna-osm@2.0.0`
3.  Once installed, go to **VTEX Admin\> Apps** and verify that Klarna OSM appears under Installed Apps.

## **Configuring Klarna On-site messaging**

Once the Klarna OSM app is installed, you need to configure it in VTEX.

### **Steps to configure Klarna On-site messaging**

In **VTEX Admin**, navigate to **Apps\> Installed Apps\> Klarna On-Site Messaging**, then click **Edit** to unlock the configuration fields.


![Navigate to OSM app](Enable_On_Site_Messaging_via_Vtex_1740779289488.png)
*Navigate to OSM app*

Enable **On-Site messaging** by toggling **Enable OSM** on.


![Enable OSM](Enable_On_Site_Messaging_via_Vtex_1740779355551.png)
*Enable OSM*

Enter your **Client ID** retrieved from the Klarna Merchant Portal.


![Enable_On_Site_Messaging_via_Vtex_1740779419744.png](Enable_On_Site_Messaging_via_Vtex_1740779419744.png)
*Enable_On_Site_Messaging_via_Vtex_1740779419744.png*

Choose a **language (locale)** for the messaging, and select a **design theme**:

- **Default** → Light background.


![default theme OSM](default_theme_OSM.png)
*default theme OSM*

- **Dark** → Dark background.


![Dark theme OSM](Dark_theme.png)
*Dark theme OSM*

![language and theme](Enable_On_Site_Messaging_via_Vtex_1740779516881.png)
*language and theme*

**Test Mode:** Set depending on the Klarna environment you want to use:

- **On** – Uses Klarna’s Playground (test) environment.
- **Off** – Uses Klarna’s Production environment.


![Test mode toggle](Enable_On_Site_Messaging_via_Vtex_1740779839564.png)
*Test mode toggle*

Toggle on or off the placements you want to use in your store.<em>Important</em> Enabling the toggle in the Klarna OSM app **only activates the placement settings**. You must still **manually insert the placement blocks** into your store’s theme for the messaging to appear. For detailed instructions, refer to the next section of this guide.


![Placements OSM](Placements_OSM.png)
*Placements OSM*

​Click **Save** to apply the changes.


![Save OSM config](Enable_On_Site_Messaging_via_Vtex_1740780042186.png)
*Save OSM config*

### Placements

To display Klarna’s On-site Messaging in your store, you need to **enable placements** in the Klarna OSM app and **insert placement blocks** into your store’s theme.

#### **Insert placement blocks in your store theme**

Identify the **placement theme block name**, which appears in parentheses next to each placement in the Klarna OSM configuration.


![Placement blocks](Enable_On_Site_Messaging_via_Vtex_1740785485074.png)
*Placement blocks*

To learn more about the different types of placements check [this article](https://docs.klarna.com/conversion-boosters/on-site-messaging/additional-resources/placements.md). Open your **VTEX Store Theme** configuration.

``` json
{
  "flex-layout.col#right-col": {
    "children": [
      "product-name",
      "Klarna-osm.product-credit-promotion-badge",
      "Klarna-osm.product-credit-promotion-auto-size",
      "buy-button"
    ]
  }
}
```

Add the **placement block** to the appropriate store sections as specified in the [VTEX documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-4-declaring-a-theme-block#step-2-using-your-new-theme-block). Once the placement blocks are added, Klarna’s On-Site Messaging should be visible in your store.


![OSM Placement on VTEX PDP](Enable_On_Site_Messaging_via_Vtex_1740785958477.png)
*OSM Placement on VTEX PDP*
<em>Important</em>If the placements do not appear:

- Ensure **Klarna OSM is enabled** in the app configuration.
- Verify that the **correct placement blocks** are added to your store theme.
- Double-check the **Client ID** entered in the Klarna OSM settings.

By completing these steps, Klarna’s messaging will be successfully integrated into your VTEX store.