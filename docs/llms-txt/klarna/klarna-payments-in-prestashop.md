# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/payments/klarna-payments-in-prestashop.md

# Klarna Payments in PrestaShop

## This page explains how to set up and configure the Klarna Payments module in your PrestaShop store.

## Overview

The Klarna Payments module connects your PrestaShop store to Klarna and gives you full control over setup, styling, payment capture, and order management. It supports sandbox and live environments, automatic status sync, multilingual checkout, and partial captures or refunds, all handled directly from your PrestaShop admin.

## Installation

There are two ways to install Klarna Payments in PrestaShop:

### Option 1: Upload via PrestaShop Back Office

1.  Go to **Modules\> Module Manager**
2.  Click **Upload a module**
3.  Select or drag the file `klarnapayments.zip`
4.  After upload, click **Configure**

### Option 2: Install via FTP

1.  Extract `klarnapayments.zip`
2.  Upload the **klarnapayments/** folder to your server’s **/modules/** directory
3.  Log into the Back Office
4.  Go to **Modules\> Module Catalog**
5.  Search for **Klarna Payments** and click **Install**

## Configuration

After installation, go to **Modules\> Module Manager**, search for **Klarna Official**, and click **Configure**.


![Klarna module on PrestaShop back office](Find_Klarna_module_on_PrestaShop_back_office.png)
*Klarna module on PrestaShop back office*

### Add your Klarna credentials

#### **1. Select the environment**


![Klarna module environment](Klarna_module_environment.png)
*Klarna module environment*

Mark the option **Run Klarna module in test mode** to choose whether the module uses the Klarna **test** or **production** environment. Enable this option for test orders, or disable it for real transactions (production). By default, this option is unmarked. Always confirm you’re using the correct environment when testing or going live.

#### **2. Add Klarna API credentials**


![Adding API credentials on Klarna module](Adding_API_credentials_on_Klarna_module.png)
*Adding API credentials on Klarna module*

Paste the API **username** and **password** you generated in the Klarna Playground or Merchant Portal. Also select the correct **API endpoint** (region) that matches your Klarna merchant account.

#### **3. Save credentials and verify connection**

After saving your credentials, a green checkmark confirms the connection succeeded.


![Successfully saving credentials](Successfully_saving_credentials.png)
*Successfully saving credentials*

If credentials are incorrect or the environment is wrong, you’ll see a red notification.


![Error saving API credentials](Error_saving_API_credentials.png)
*Error saving API credentials*

### Enable Klarna Payments


![Enable Klarna Payments](Enable_Klarna_Payments.png)
*Enable Klarna Payments*

In the **Klarna Payments** section, enable Klarna Payments if you have a direct merchant account with Klarna and want to add Klarna as a payment method in your checkout. This option uses Klarna API credentials created in the Klarna Merchant Portal.<em>Important</em> If you’re using Klarna through a payment service provider (Stripe, Adyen, Mollie, etc.), don’t enable Klarna Payments through this module. Instead, activate Klarna directly with the PSP.

### Map order statuses

Go to the **PrestaShop order settings** and map the Klarna order statuses to the corresponding statuses in your PrestaShop store.


![Mapping order statuses](Mapping_order_statuses.png)
*Mapping order statuses*

| **Status for:** | **Suggested status on PrestaShop** | **Definition** |
|----|----|----|
| New orders | `Payment accepted` | Payment authorized / order created |
| Captured orders | `Shipped` | Full payment amount captured |
| Canceled orders | `Canceled` | Payment cancelled |
| Refunded orders | `Refunded` | Refunded |
| Partially captured orders | `Partially captured` | Partial payment amount captured |

Default mapping

<em>Note</em> You can adjust these based on your store’s fulfillment process.

#### Capture upon fulfillment

This section shows how to automate Klarna capture when a PrestaShop order reaches a certain status, like **Shipped**. To enable:

1.  Check the **Capture upon fulfillment** option
2.  Select the status(es) that should trigger the capture (e.g. shipped, partially captured, etc.)
3.  Save the configuration


![Capture upon fulfillment](Capture_upon_fulfillment.png)
*Capture upon fulfillment*

Once active, Klarna captures the order when the status changes.

## Additional settings


![Additional settings](Additional_settings.png)
*Additional settings*

#### Debug mode

Enable **debug mode** if you want to log full API requests and responses during testing. You can view logs in the **Logs** tab.<em>Important</em> Turn this off in production environments to avoid unnecessary data capture.

#### Automatic order status change

You can choose if Klarna should auto-update PrestaShop order statuses.

- If enabled: Klarna updates PrestaShop status once per order
- If disabled: Klarna creates the order, but status changes are manual

#### Hosted payments page (HPP)

Redirects customers to a Klarna hosted page to complete their payment. This option improves compatibility with third-party or one-page checkout modules and is enabled automatically when an OPC module is detected.

#### B2B mode

Enable B2B mode to send customer’s company details to Klarna.

#### Default country

Select the fallback country for Klarna to use if the customer’s locale can’t be detected from their checkout address.

## Next steps

- [Managing Klarna orders on PrestaShop](https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/payments/order-management-in-prestashop/)
- [Set up On-site messaging](https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/conversion-boosters/configuring-on-site-messaging/)
- [Enable Express Checkout](https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/conversion-boosters/how-to-enable-express-checkout-in-prestashop/)
- [Enable Sign in with Klarna](https://docs.klarna.com/platform-solutions/e-commerce-platforms/prestashop/conversion-boosters/how-to-enable-sign-in-with-klarna-in-prestashop/)