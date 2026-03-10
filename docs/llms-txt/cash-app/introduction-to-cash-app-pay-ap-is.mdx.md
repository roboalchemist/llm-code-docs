# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/introduction-to-cash-app-pay-ap-is.mdx

***

## stoplight-id: c5c6ac99f471c

# Introduction to Cash App Pay APIs

The Cash App Pay developer product is composed of three REST APIs and a Javascript SDK:

* **Customer Request API:** Used to get permission from customers to perform actions on their accounts (like collecting a payment)
* **Network API:** Registers merchants and processes payments using grants
* **Management API:** Controls API keys and webhooks
* **Pay Kit (JS SDK):** Wraps the Customer Request API and provides prebuilt UI components to add Cash App Pay to websites

As a developer, you'll use all of these API suites to build a complete Cash App Pay integration.

## Payment processing workflow

Most Cash App Pay workflows follow a simple pattern: create a customer request, get it approved by the customer to generate a grant, then use the grant to create a payment.

![payment-processing-workflow.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/payment-processing-workflow.png)

1. **Initiate a customer request**
   * Use Pay Kit in the browser to create a customer request.
   * Define the actions you want to perform (e.g. "charge \$5 for a coffee")

2. **Present the approval user experience**
   * When a customer request is created, the API returns an approval URL, which allows customers to approve or decline the request.
   * The URL opens in a web browser or on a Cash App mobile client. It's represented through a QR code or a navigation button.
   * Pay Kit automatically selects and renders the optimal user experience according to Cash App brand guidelines.

3. **Customer approves the request**
   * The approval generates grants, which represent the customer's permission to perform the actions listed in the customer request.

4. **Front end receives grants**
   * Pay Kit detects that the customer request is approved and returns the grants to the webpage's JavaScript.
   * The webpage sends the grant information to the server to process the payment.

5. **Back end processes payment**
   * On the server, the grant ID is sent to the Network API [Create Payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment) endpoint along with the payment amount, currency, and merchant ID.
   * The Network API consumes the grant and charges the customer for the given amount.

6. **Settlement**
   * The payment settles later that day. Funds are delivered to the developer to distribute to the merchant.
