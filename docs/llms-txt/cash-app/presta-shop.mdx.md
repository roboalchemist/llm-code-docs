# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/presta-shop.mdx

***

## stoplight-id: 3l0yydo6wiecy

# Getting Started

<Info title="Migrate from Afterpay to Cash App Afterpay">If you are an Afterpay merchant, see the [Migration page](/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/platforms/presta-shop-migration) for information on the migration from Afterpay to Cash App Afterpay.</Info>
Follow the instructions below.

### Setting up Cash App Afterpay with PrestaShop

Cash App Afterpay has a module that you can install in the back office admin area for PrestaShop.

<Note>
  Before you begin you must:

  * Have a Cash App Afterpay merchant account to use the Cash App Afterpay module with PrestaShop. Click [here](https://get.afterpay.com) to sign up for a Cash App Afterpay merchant account.

  * Ensure that the Cash App Afterpay module for PrestaShop is compatible with PrestaShop versions 8, 1.7.x. and 1.6.x
</Note>

#### Install the Module

To install the module do the following:

1. In the *Modules* section of the PrestaShop admin area, select **Module Catalog**.

2. Enter `Afterpay` in the module search box.

3. Select **Install**.

4. Select **Configure**. The Afterpay configuration panel appears.

5. Enter your merchant ID and secret key and your API region and environment.

6. Click **Save** in the lower-right corner.

<Info>
  From time to time the Cash App Afterpay module is updated. To ensure you have the most up-to-date module, follow the procedure(s) in the [Updating the Cash App Afterpay Module](/cash-app-afterpay/guides/platforms/presta-shop/updating-the-cash-app-afterpay-module) page.
</Info>

| Setting                                    | Value                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Module is enabled                          | **Yes** - Cash App Afterpay turned on <br /> **No** - Cash App Afterpay disabled.                                                                                                                                                                                                                                                                                                                                    |
| Merchant ID                                | Your 9 digit Cash App Afterpay Merchant ID.                                                                                                                                                                                                                                                                                                                                                                          |
| Secret Key                                 | Your 128 character Cash App Afterpay secret key.                                                                                                                                                                                                                                                                                                                                                                     |
| API Environment                            | **Sandbox** - for testing. <br /> **Production** - For live order processing.                                                                                                                                                                                                                                                                                                                                        |
| Min Payment Limit/Max Payment Limit        | Current minimum and maximum Cash App Afterpay order thresholds. **These values are for information purposes and cannot be customized in Prestashop.**                                                                                                                                                                                                                                                                |
| Enable Multicurrency                       | Enable multicurrency support.                                                                                                                                                                                                                                                                                                                                                                                        |
| CBT Countries                              | [Cross Border Trade (CBT)](/cash-app-afterpay/guides/welcome/getting-started/cross-border-trade) allows you to sell internationally. Customers in foreign countries pay in their local currencies, while Afterpay continues to settle with you in your local currency. This information is supplied by Afterpay and cannot be edited. This value is for information purposes and cannot be customized in Prestashop. |
| Restricted Categories                      | This enables you to restrict Cash App Afterpay to selected product categories.                                                                                                                                                                                                                                                                                                                                       |
| Payment Info on Individual Product Page    | Enable to display Cash App Afterpay elements on individual product pages.                                                                                                                                                                                                                                                                                                                                            |
| Product Page HOOK                          | This property sets the HOOK where Cash App Afterpay messaging is linked to on the product page. Only change this value if the messaging doesn't appear correctly.                                                                                                                                                                                                                                                    |
| Price CSS (Cascading Style Sheet) Selector | This property sets the CSS selector needed to show the assets on the product page. Only change this value if it doesn't appear correctly.                                                                                                                                                                                                                                                                            |
| Product Page CSS Position Selector         | Cash App Afterpay messaging is moved after the CSS Selector DOM (Document Object Model) Element. Only change this value if it doesn't appear correctly.                                                                                                                                                                                                                                                              |
| Payment Info on Cart Page                  | Enable to display Cash App Afterpay elements on the cart page (available for PS 1.7 and higer).                                                                                                                                                                                                                                                                                                                      |
| Cart Page CSS Selector                     | This property set the CSS selector needed to show the assets on the cart page. Only change this value if it doesn't appear correctly.                                                                                                                                                                                                                                                                                |
| Canonical URLs                             | Only Enable this option if the checkout doesn't redirect correctly to the payment gateway and shows a 404 error.                                                                                                                                                                                                                                                                                                     |
| Debug mode                                 | Enable the debug logging. You can see these logs in the *Configure* > *Advanced Parameters* > *Logs* section.                                                                                                                                                                                                                                                                                                        |
| Enable Reversal                            | If Prestashop throws an exception while attempting to finalise an order after payment is approved by Cash App Afterpay, the payment can be reversed automatically. This may help to prevent scenarios where customers pay for orders that can't be fulfilled. Not recommended if an external Order Management System (OMS) is in use.                                                                                |

## Store currency and language

The module relies on a dedicated Website Scope being used for each market region (country) with a corresponding base currency and languages set in the PrestaShop admin area. As Cash App Afterpay is only available in the USA, set the market region to USA and the base currency to US dollars.

<Warning>
  Warning

  Check that your store's base currency is set to USD (\$).
</Warning>

To set the Base Currency:

1. Go to *International*.

2. Select the *Localization* page and use the *Default currency* option from the *Configuration* section.

For more information see this section of the [PrestaShop 1.7](http://doc.prestashop.com/display/PS17/Localization) & [PrestaShop 1.6](http://doc.prestashop.com/display/PS16/Understanding+Local+Settings) documentation.

## Testing your configuration

1. Go to a product page to check whether Cash App Afterpay appears as a payment option. If the Cash App Afterpay widget does not appear, check that you have entered your Cash App  Afterpay credentials correctly when you set up the Afterpay module.

2. If Cash App Afterpay appears correctly as a payment option, go to the checkout page to test that the Cash App Afterpay information displays correctly.

### Troubleshooting

If Cash App Afterpay does not update/display as expected, provide staff access to your PrestaShop admin panel for our Integration Support Team.

Send an email to [merchantadminus@afterpay.com](mailto:merchantadminus@afterpay.com) and include the:

* Admin panel URL

* Admin panel user

* Admin panel password
