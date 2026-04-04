# Fraud Protection Advanced

Fraud Protection Advanced (FPA) is a robust fraud protection tool integrated into PayPal’s core processing services. It enables your fraud teams to conduct in-depth risk analysis and investigations to help identify and mitigate fraud.

Fraud Protection Advanced combines decades of intelligence from the PayPal network with advanced machine learning (ML) and analytics to continuously adapt to changes in both a merchant's business and evolving fraud tactics. It is integrated with PayPal Complete Payments (PPCP) for merchants who are on the Advanced Checkout integration.

## Why is FPA essential?

FPA provides a range of powerful capabilities:

- Fraud profile identification: Initial fraud strategies are customized based on historical risk patterns. The effectiveness of these profiles is monitored post-onboarding and adjusted as needed to enhance performance.
- Fraud detection and risk scoring: Mitigate fraud by declining high-risk transactions using advanced features, including:
  - Custom filters: Tailor rules to identify and block fraudulent activities.
  - Manual review: Assess and review flagged transactions manually for further validation.
  - Blocklists, allowlists, and reviewlists: Enhance filters with supplementary lists to manage trusted and suspicious entities.
  - Activity tracking and audit trail: Track changes and user actions and maintain a detailed audit trail.
  - ML-based AI model: Utilize machine learning techniques to analyze data points such as card details, buyer information, purchasing patterns, and device intelligence to generate a risk score.

Hence, we strongly recommend that you choose FPA as your fraud protection tool.

## What are the benefits?

FPA provides the following benefits on top of [Fraud Protection](https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/) (FP) for merchants enrolling in PPCP capabilities:

- It is a self-serve tool that you can customize to meet your specific business requirements. It is not pre-configured to fit any business needs by default.
- PayPal can view both merchant and consumer activities across 25 billion transactions annually. This rich data fuels PayPal’s machine learning models, which adapt to new transactions as they occur and historical fraud trends seen across the network, leading to more accurate fraud detection.
- Due to enhanced fraud decision-making by merchants, consumers will experience fewer declines, less friction, and faster order processing.

Additionally, PayPal enhances the onboarding experience for fraud protection tools by offering:

- The right product recommendation for fraud prevention tools, better discoverability, and comprehension of products.
- A streamlined, guided setup and activation experience.
- A better description of the advanced capabilities and flexibility of the fraud tools.

## Essential prerequisites for optimal FPA performance

To enhance risk and fraud management, we strongly recommend that you provide additional data. This data is incorporated into PayPal's machine learning models, allowing them to analyze historical transactions and to improve the model’s efficiency in detecting fraud. This approach optimizes the performance of your risk and fraud management processes. To include this data, you must pass the following fields to all requests sent to the Orders v2 API for processing.

### Create order

The following table shows the required parameters for optimal FPA performance when making a POST call to the Create order endpoint of the Orders v2 API.

| **Field name** | **Description** | **Type** | **Notes** |
| --- | --- | --- | --- |
| PayPal-Client-Metadata-Id | The device ID for this purchase. See the [parameter definition](/docs/api/orders/v2/#orders_create!in=header<path=PayPal-Client-Metadata-Id>t=request) for more information. | String | - Minimum characters: 1
- Maximum characters: 36 |

### Header

| **Field name** | **Description** | **Type** | **Notes** |
| --- | --- | --- | --- |
| PayPal-Client-Metadata-Id | The device ID for this purchase. See the [parameter definition](/docs/api/orders/v2/#orders_create!in=header<path=PayPal-Client-Metadata-Id>t=request) for more information. | String | - Minimum characters: 1

- Maximum characters: 36 |

### Body

| **Field name** | **Description** | **Type** | **Notes** |
| --- | --- | --- | --- |
| payment\_source.card.attributes.customer.email\_address | Email address of the buyer as provided to the merchant or on file with the merchant. Email Address is required if you are processing the transaction using PayPal Guest Processing, which is offered to select partners and merchants. For all other use cases, we do not expect partners or merchant to send email\_address of their customer. See the [parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/attributes/customer/email_address>t=request) for more information. | String | - Minimum characters: 3

- Maximum characters: 254

- Pattern: (?:[a-zA-Z0-9!#$%\u0026'*+/=?^_`{|}~-]+(?:\\.[a-zA-Z0-9!#$%\u0026'*+/=?^_`{|}~-]+)*|(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\]) |
| payment\_source.card.attribues.customer.phone | The phone number of the buyer as provided to the merchant or on file with the merchant. The phone number supports only national\_number. See the [parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/attributes/customer/phone>t=request) for more information. | Object |  |
| payment\_source.card.billing\_address | The billing address for this card. Supports only the address\_line\_1, address\_line\_2, admin\_area\_1, admin\_area\_2, postal\_code, and country\_code properties. See the [parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/billing_address>t=request) for more information. | Object |  |
| purchase\_units.shipping.address | The address of the person to whom to ship the items. Supports only the address\_line\_1, address\_line\_2, admin\_area\_1, admin\_area\_2, postal\_code, and country\_code properties. See the [parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/attributes/customer/phone>t=request) for more information. | Object |  |
| purchase\_units.items | An array of line items that the customer purchases from the merchant. See the [parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/billing_address>t=request) for more information. | Array of Objects |  |
| purchase\_units\[\].supplementary\_data.risk.customer.ip\_address | An Internet Protocol address (IP address). This address assigns a numerical label to each device that is connected to a computer network through the Internet Protocol. Supports IPv4 and IPv6 addresses.

- If your merchant is integrated through PayPal JS SDK, the Customer IP will be passed by default.
- If your merchant is integrated through APIs, they can send in the Customer IP through [Orders v2 API](/docs/api/orders/v2/) requests. In the request object for Orders v2 API, the Customer IP is structured as follows:

  "supplementary\_data": { "risk": { "customer": { "ip\_address": "192.158.1.38" } } } |

## Capture payment for order

| **Field name** | **Description** | **Type** | **Notes** |
| --- | --- | --- | --- |
| payment\_source.card.name | The cardholder's name as it shows up on the card. See the [parameter definition](/docs/api/orders/v2/#orders_capture!path=payment_source/card/name>t=request) for more information. | String | - Minimum characters: 1

- Maximum characters: 300 |
| payment\_source.card.number | The primary account number (PAN) for the payment card. See the [parameter definition](/docs/api/orders/v2/#orders_capture!path=payment_source/card/number>t=request) for more information. | String | - Minimum characters: 13

- Maximum characters: 19 |

## Targeted users, eligible markets, and pricing details

FPA is available for both direct merchants and through marketplaces, which are payment platforms that host merchants. The following table outlines the pricing details for each FPA-screened transaction across the available markets:

| **Country code** | **Country** | **Headline price** |
| --- | --- | --- |
| US | United States | 0.07 USD |
| CA | Canada | 0.09 CAD |
| AU | Australia | 0.1 AUD |
| AT | Austria | 0.06 EUR |
| DE | Germany | 0.06 EUR |
| GB | United Kingdom | 0.06 GBP |
| FR | France | 0.06 EUR |
| ES | Spain | 0.06 EUR |
| IT | Italy | 0.06 EUR |
| PL | Poland | 0.3 PLN |
| PT | Portugal | 0.06 EUR |
| IE | Ireland | 0.06 EUR |
| BG | Bulgaria | 0.06 EUR |
| CY | Cyprus | 0.06 EUR |
| CZ | Czech Republic | 1.6 CZK |
| DK | Denmark | 0.5 DKK |
| EE | Estonia | 0.06 EUR |
| FI | Finland | 0.06 EUR |
| GR | Greece | 0.06 EUR |
| HU | Hungary | 25 HUF |
| LT | Lithuania | 0.06 EUR |
| LV | Latvia | 0.06 EUR |
| MT | Malta | 0.06 EUR |
| RO | Romania | 0.35 RON |
| SE | Sweden | 0.7 SEK |
| SI | Slovenia | 0.06 EUR |
| SK | Slovakia (Slovak Republic) | 0.06 EUR |
| BE | Belgium | 0.06 EUR |
| LU | Luxembourg | 0.06 EUR |
| NL | Netherlands | 0.75 EUR |
| LI | Lichtenstein | 0.06 EUR |
| NO | Norway | 0.75 NOK |
| SM | San Marino | 0.06 EUR |
| SG | Singapore | 0.1 SGD |
| HK | Hong Kong | 0.6 HKD |

## Discovery and access

You can find FPA using either of the following options:

- In **Business Tools**, navigate to the **Manage Risk** section. Select the **Fraud Tools** tile.
![](https://www.paypalobjects.com/devdoc/FPA_Home_Discovery_BusinessTools.png)
- Alternatively, go to your **Account Settings**, and select **Payment preferences**. Next to the **Manage fraud** section, select **Choose a fraud tool.**
![](https://www.paypalobjects.com/devdoc/Activate_dirmerch_acct_settingSS.png)

### Enable FPA

You can enable FPA using the following steps:

- Select **Do it yourself using PayPal’s fraud tool** and select **Next**.
![](https://www.paypalobjects.com/devdoc/FPA_Home_DIY_FPA_Recommended.png)
- You will see a recommended solution based on your business metrics. However, you can modify the selection if you want. Choose **Fraud Protection Advanced Tool** and select **Next**.
![](https://www.paypalobjects.com/devdoc/Activate_Dir_Mer_Select_FPA.png)
- Confirm your details to set up automatic bank payments for your fraud tool, and select **Next**.
![](https://www.paypalobjects.com/devdoc/Activate_Dir_Mer_Set_Up_auto_debit.png)
- Select **Let’s Go** to go to the Fraud Protection Advanced tool and begin customizing your fraud tool.
![](https://www.paypalobjects.com/devdoc/Activate_DirMer_EndOfFlow_.png)

### View the FPA Dashboard

Once activated, Fraud Protection Advanced will open in a new tab that will display the **Dashboard**, which presents fraud metrics related to your business. The dashboard displays fraud metrics over the past 180 days.

Now, you're ready to begin customizing the tool to suit your business needs.

![](https://www.paypalobjects.com/devdoc/FPA_Home_Dashboard.png)

## Next steps

A comprehensive overview of onboarding with Fraud Protection Advanced (FPA).