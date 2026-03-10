# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/big-commerce/add-payment-option.mdx

***

## stoplight-id: f96obua9wosa1

# Add Payment Option

## Configuration

Completing the below steps will enable and display Cash App Afterpay as a Payment Method. Do the following:

1. Go to *BigCommerce Control Panel*.

2. Go to *Settings* > *Payments*.

3. Under the *Online Payment Methods* section, click the drop-down arrow.

   ![add-payment-option-1.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/add-payment-option-1.png)

4. Locate *Afterpay* from the Online Payment Methods list and click **Set up**.

   ![add-payment-option-2.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/add-payment-option-2-2.png)

5. Enter the Merchant ID provided by Afterpay into the *Merchant ID* field.

6. Enter the Secret Key provided by Afterpay into the *Secret Key* field.

   ![add-payment-option-3.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/add-payment-option-3.png)

7. Additionally, you can configure the following settings:

   * **Transaction Type** — can be set to Authorize & Capture or Authorize Only. Authorize Only allows you to capture the funds manually. See [Manually Capturing Transactions (Authorize Only)](https://support.bigcommerce.com/s/article/Manually-Capturing-Transactions-Authorize-Only) to learn more.

   * **Test Mode** — set this to *Yes* to test checkout flow. Make sure this is set to *No* when your store goes live.

   <Note>
     You need Cash App Afterpay Sandbox Credentials to use Test Mode. Please contact your Afterpay Delivery Manager for assistance.
   </Note>

8. Click the **Save** button.
