# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/before-you-start/operations-and-maintenance.md

# Salesforce operations and maintenance

## Data storage

### System Object Extensions

#### Basket

| **Parameter name** | **Attribute ID** | **Description** |
|----|----|----|
| Klarna Session ID | `kpSessionId` | The Klarna session ID returned after “Create Session” API  endpoint is called (Applicable from version 21.2.0) |
| Klarna Client Token | `kpClientToken` | Client token returned by “Create Session” API endpoint and  used to  initialize the JS SDK (Applicable from version 21.2.0) |
| Klarna Client Token Frequency | `kpSubscriptionFrequency` | Subscription frequency values (day, month, etc.) |
| Klarna Subscription Period | `kpSubscriptionPeriod` | Predefined subscription period in numbers |
| Klarna Is Express Checkout | `kpIsExpressCheckout` | Determines if the basket is an express checkout |
| Klarna Session ID | `kpSessionId` | The Klarna session ID returned after “Create Session” API  endpoint is called (Applicable from version 21.2.0) |

#### Order

| **Parameter name** | **Attribtute ID** | **Description** |
|----|----|----|
| Klarna Payments Order ID | `kpOrderID` | The Klarna Payments Order ID for Klarna payment method selected by customer |
| VCN Brand | `kpVCNBrand` | Klarna Payments virtual card scheme name |
| VCN Holder | `kpVCNHolder` | Klarna Payments virtual card holder name |
| VCN Card ID | `kpVCNCardID` | Klarna Payments Virtual Card - Card ID |
| VCN PCI Data | `kpVCNPCIData` | Klarna Payments Virtual Card PCI Data in encrypted format |
| VCN Initialization Vector | `kpVCNIV` | Klarna Payments Virtual Card Initialization Vector |
| VCN AES Key | `kpVCNAESKey` | Klarna Payments Virtual Card AES Key |
| Is VCN Used | `kpIsVCN` | True if virtual card is enabled & used for payment of the order, otherwise false |
| Klarna Session ID | `kpSessionId` | The Klarna session ID returned after “Create Session” API endpoint is called (Applicable from version 21.2.0) |
| Klarna Client Token | `kpClientToken` | Client token returned by “Create Session” API endpoint and used to  initialize the JS SDK (Applicable from version 21.2.0) |
| Klarna Subscription Frequency | `kpSubscriptionFrequency` | Subscription frequency values (day, month, etc.) |
| Klarna Subscription Period | `kpSubscriptionPeriod` | Predefined subscription period in numbers |

#### Order Payment Instrument

| Parameter name | Attribute ID | Description |
|----|----|----|
| Klarna Payment Category ID | `klarnaPaymentCategoryID` | ID of Klarna payment category |
| Klarna Payment Category Name | `klarnaPaymentCategoryName` | Name of Klarna payment category |

#### Payment Transaction

| Parameter name | Attribute ID | Description |
|----|----|----|
| Fraud Status | `kpFraudStatus` | Klarna Payments order fraud status |
| Klarna Authorization Token | `kpAuthorizationToken` | This attribute stores the Klarna authorization token, which is a string value used to authenticate and finalize the order creation process with Klarna's payment system. (Applicable from version 23.2.0) |
| Klarna Redirect URL | `kpRedirectURL` | This attribute holds the URL to which the customer is redirected after the payment authorization is successfully completed by Klarna's system. (Applicable from version 23.2.0) |

#### Site preferences

| Parameter name | Attribute ID | Description |
|----|----|----|
| Enable Klarna Payments | `kp_enable` | Enable/Disable Klarna Payments.Boolean attribute with Default value as true |
| Color Customization | `kpColorCustomization` | JSON attribute to customize color |
| Enable Extra Merchant Data | `kpEMD` | Enable this option to include `customer_account_info` and `other_delivery_address` as attachments when creating an order. Boolean with default value `false`. |
| VCN - Enable settlement retry | `kpVCNRetry` | When set to “Yes”, SFCC will automatically retry the VCN settlement in the event of a service error. Boolean with default value false |
| Log Extra debug data | `kpLogExtraData` | Attribute to log debug data.Boolean with default value true |
| Merchant Reference 2 | `merchant_reference2` | Enter the attribute from the SCC order (basket) object that you would like to forward as an additional merchant reference to Klarna. This attribute must be a class attribute of the SCC LineItemCtnr. String attribute |
| Agent username for subscriptions | `kpSubsUsername` |  |
| Agent password for subscriptions | `kpSubsPassword` | Agent password to login on behalf of customers to create subscription orders. Password Attribute |
| Enable retry for subscriptions | `kpSubsRetryEnable` | Boolean with default value false |
| Number of Retries | `kpSubsRetryNumber` | Number attribute |
| Recurring retry frequency | `kpSubsRetryFrequency` | Number attribute |

| Parameter name | Attribute ID | Description |
|----|----|----|
| Enable Express Checkout | `kec_enable` | Boolean flag to enable/disable Klarna Express checkout |
| Theme | `kec_theme` | The theme of the button. Options include default, light & dark |
| Button Shape | `kec_shape` | The shape of the button. Options include default, rect & pill |
| Placement | `kec_placement` | Multi-select attribute to choose where to display express checkout buttons. Values: cart, PDP, mini cart |

| Parameter name | Attribute ID | Description |
|----|----|----|
| Enable On-Site Messaging | `osm_enable` | Enable/Disable OSM functionality |
| Theme | `osm_theme` | Theme for on site messaging .Options include default,dark and custom |
| Placement | `osm_placement` | Multi-select dropdown which includes cart, pdp, header, footer and info. Placement Tag IDs are hardcoded in code. |
| Custom styling | `osm_custom_styling` | JSON to store custom styling |

| Parameter name | Attribute ID | Description |
|----|----|----|
| Enable Sign-in with Klarna | `siwk_enable` | Boolean flag to enable/disable Klarna SIWK |
| Scope | `siwk_scope` | Multi Selection list of available scopes that can be requested |
| Redirect URL | `siwk_redirect_url` | Login redirect url |
| Button theme | `siwk_theme` | The theme of the button. Options include default, light & dark |
| Button Shape | `siwk_shape` | The shape of the button. Options include default, rect & pill |
| Logo alignment | `siwk_alignment` | Klarna logo alignment. Options include badge, left & center |
| Placement | `siwk_placement` | Multiselect attribute to choose where to display SIWK buttons. Values: login and checkout |

#### Product parameters for Klarna subscriptions

| Parameter name | Attribute ID | Description |
|----|----|----|
| Is Klarna Standard Product | `kpIsStandardProduct` | Boolean attribute to define if the product is standard. |
| Is Klarna Subscription Product | `kpIsSubscriptionProduct` | Boolean attribute to define if the product is eligible for subscription. |
| Klarna Trial Days Usage | `kpTrialDaysUsage` | Numeric value used for free trial definition. |

#### ProductLineItem

| Parameter name | Attribute ID | Description |
|----|----|----|
| Is Selected for Subscription product | `kpSubscription` | Boolean attribute to define if the product is selected for subscription in the basket. |
| Enriched data for product line item. | `klarna_oms_lineItemJSON` | String data for product line item. |
|  |  |  |

#### Profile

| Parameter name | Attribute ID | Description |
|----|----|----|
| Klarna Subscriptions | `kpSubscriptions` | Text attribute to store customer subscriptions to Klarna |

#### Klarna activation

KlarnaActivation custom object gives an opportunity to configure multiple MIDs per site. Merchants could have different credentials, clientIDs and VCN keys per country or group of countries. It has a similar structure to the Klarna Activation Site preferences group. Klarna Activation Key is the unique key for each Klarna Activation CO entry. It should be defined by the merchant and could have any unique string value.


![ Klarna activation attributes](Zwf0iYF3NbkBXN0J_sfcc-KlarnaActivationattributes.jpeg)
*Klarna activation attributes*

| Parameter name | Attribute ID | Description |
|----|----|----|
| Klarna Activation Key | `kp_activation_key` | Unique identifier for a single KlarnaActivation entry. It is a free text entered by the merchant. |
| Region | `kp_region_countries` | Klarna regions (Europe, North America, Oceania) |
| Market(s) | `kp_market_countries` | Klarna available countries |
| Client ID | `kp_client_id_countries` | Client ID generated in Klarna Merchant Portal |
| API Username | `KP_API_Username_countries` | API username generated in Klarna Merchant Portal |
| API Password | `KP_API_Password_countries` | API password generated in Klarna Merchant Portal |
| Enable Virtual Card Number (VCN) | `kpVCNEnabled_countries` | Flag to enable virtual card number for selected countries. This will override the globally selected in Klarna Payments. |
| Public Key ID | `kpVCNkeyId_countries` | Countries specific public key for VCN |
| Enable settlement retry | `kpVCNRetry_countries` | Flag to enable settlement retry for selected countries. This will override the globally selected in Klarna Payments. |

### Session attributes and cookies

The following session custom attributes are saved in session.privacy storage and accessible in checkout. The attributes are retained for the session lifetime & cleared when the customer logs out of their profile.

| Attribute | Description |
|----|----|
| `KlarnaLocale` | The Klarna locale in use |
| `KlarnaPaymentsSessionID` (Not included as session attributes from version 21.2.0) | The Klarna session ID returned after “Create Session” API endpoint is called |
| `KlarnaPaymentsClientToken` (Not included as session attribute from version 21.2.0) | Client token returned by “Create Session” API endpoint and used to  initialize the JS SDK |
| `KlarnaPaymentMethods` | The available payment method categories for the respective Klarna session; Saved in JSON format |
| `KlarnaPaymentsAuthorizationToken` | The authorization token returned by JS SDK “Authorize” call |
| `KPAuthInfo` | Whether finalization is required for the payment method; Returned by JS SDK “Authorize” call; Saved in JSON format |
| `KlarnaExpressCategory` | The KEB payment category; Currently applicable for US and defaults to “pay_over_time” |
| `KlarnaPaymentsRedirectURL` | The URL to redirect the customer to after placing the order; Returned by the “Create Order” API call |
| `'kpActive_' + countryCode` | Flag to indicate if Klarna is enabled for current site country |
| `'kpActivationSource_' + countryCode` | Klarna Activation source per country - Custom Object or Site Preferences. It is empty for old Klarna Countries config |
| `'kpActivationKey_' + countryCode` | Klarna Activation key in case of Custom object usage. |

The following cookies are being set by the Klarna cartridge integration:

| Cookie name | Description |
|----|----|
| `selectedKlarnaPaymentCategory` | The selected payment method on checkout (e.g. “pay_later”) |

### Library

In addition to the configurations, the following two library assets will be added:

- **footer-about**: An updated Out-of-the-Box (OOTB) asset that includes a link to the Klarna On-site messaging (OSM) dedicated page in the footer.
- **klarna-email-info**: An asset containing links to review Klarna Payment information, which is used in the confirmation email sent to customers.

### Services

An HTTP service, `klarna.http.defaultendpoint`, has been added with the `klarna.http.service` profile.

- **Deprecation Notice for Version 24.4.0:**Service credentials and the `KlarnaCountries` custom object have been deprecated as of version 24.4.0. Please use the Klarna Activation Site Preferences or the Klarna Activation custom object to enter API credentials.
- **Replication Guidance for Version 21.2.0:**Prior to version 21.2.0, the `KlarnaCountries` custom object was replicable. To avoid issues with service credentials during replication, merchants should use the same service credential name across staging, development, and production environments.

For more details on updating the KlarnaCountries definition in your instances, please review Section [Update KlarnaCountries Definition](https://docs.google.com/document/d/1-sMIxC4BTmvqZRHifFOUT-Wo2bc0oVQNh1GP7piaQsM/edit#heading=h.wtrcq16yy4rn). **Klarna Sign In Service** klarna.http.signIn with klarna.http.signIn profile and klarna.signin.credentials credentials. URL is populated dynamically for Activation configuration. For deprecated Klarna Countries setup service credentials URL should be updated on production.

## Logs

The integration includes the following types of logs:

- **Service Communication Logs**: These logs start with `service-klarna-***` and contain every request and response to the Klarna endpoints. Personal information, such as emails and names required for the Klarna API calls, is masked in these logs.
- **Custom Errors and Debug Info**: Depending on the case, custom errors and debug information are logged under `customerror-***`, `custodebug-***`, and `custominfo-***` files.

## Availability

Cartridge functionality is dependent on the availability of the Klarna API service. The current operational status of Klarna can be viewed at [Klarna Status](http://status.klarna.com/).

#### Merchant support

For reporting core SFCC functionality issues in the Klarna cartridge technical integration, please contact: commercecloud@klarna.com. For production issues related to Klarna API availability, merchant representatives should reach out to their Klarna Account Manager after reviewing the current operational status at [Klarna Status](http://status.klarna.com/). ​**Pre-requisite information to provide when reporting an incident**:

- Merchant's affected MID or market
- Impact and examples of customer orders (order_id or Klarna session_id if available)
- Screenshots, timeframe, and any additional information as required

This information helps speed up the investigation and resolution process.