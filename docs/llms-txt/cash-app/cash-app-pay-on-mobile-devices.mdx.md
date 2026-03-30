# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/product-overview/cash-app-pay-on-mobile-devices.mdx

***

## stoplight-id: 24dfa8d83fc34

# Cash App Pay on Mobile devices

![Mobile Experience](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/mobile-experience.png)

When doing online shopping on their mobile devices (both Android and Apple) and Android tablets, the Customer can use Cash App Pay as their payment method. This is also a simple three-step process for the Customer and is as follows:

1. At checkout, the Customer chooses Cash App Pay as their payment method.

   ![Customer chooses Cash App Pay](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/demo-mobile-customer-chooses-cash-app-pay.png)

2. The Customer is redirected to Cash App, where the Merchant’s Business Name and Logo, transaction amount (optional), and Continue to checkout button is displayed.

   ![Customer redirected to Cash App](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/demo-mobile-redirect-to-cash-app.png)

3. The Customer selects Continue to checkout in Cash App and is automatically redirected to the Merchant's online store. Cash App Pay is displayed as the selected payment method. The Customer can also see their Cashtag displayed next to the Cash App Pay logo and brand. From here, they complete their purchase as usual.

   ![Customer continues to checkout](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/demo-mobile-continue-checkout.png)

   <Note>
     The Customer can also be redirected directly to the order confirmation page of the Merchant.
   </Note>

   <Note>
     If you are using React Native applications in your development, there are some extra configurations that are required for iOS and Android. See [React Native Requirements](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/react-native-requirements) for more details.
   </Note>
