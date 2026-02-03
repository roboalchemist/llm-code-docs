# Integrate FraudNet for PayPal APM

FraudNet is a PayPal-developed, JavaScript library embedded into a merchant’s web page to collect browser-based data to help reduce fraud. Upon checkout, data elements are sent to PayPal Risk Services for fraud and risk assessment.

Data collected by FraudNet is used for risk analysis and authentication. PayPal does not share FraudNet data with third parties for their own independent benefit.

To integrate FraudNet, embed a short code snippet in the merchant website and add a custom header to the PayPal call.

## Embed FraudNet snippet

Embed a FraudNet JavaScript and noscript/ snippet into the page where you're integrating FraudNet. The integration code is based on the non-blocking script loader pattern.

### JavaScript

There are 2 parts to the JavaScript snippet:

| Element | Description |
| --- | --- |
| **FraudNet parameters** | Ascript/parameter block that passesfnparamsinput parameters to FraudNet. |
| **Loading script** | Ascript/element with code that asynchronously loads the FraudNet JavaScript. |

### Noscript

The noscript/ snippet runs when JavaScript isn't enabled for the application. This element operates independently from the JavaScript snippet.

### Parameters

The JavaScript and noscript/ snippets pass parameters to FraudNet. The s and f FraudNet parameters are required for both integrations.

### Script attributes

The loading script of the JavaScript snippet uses this attribute in the `<script>` declaration:

| Parameter | Description | Type | Required |
| --- | --- | --- | --- |
| fncls | This attribute passes thefnparamskey needed to connect with the FraudNet service. The key isfnparams-dede7cc5-15fd-4c75-a9f4-36c430ee3a99. | string | Required for Javascript snippets |

### Parameter attributes

The JavaScript and noscript/ snippets use these 2 attributes:

| Parameter | Description | Type | Required | Notes |
| --- | --- | --- | --- | --- |
| `f` | The `FraudNet Session Identifier` passes a unique and random identifier for the current transaction or session. | String | Required | Maximum length: 32 |
| `s` | Passes a unique flow ID for each web page. See the [Modify the code](/docs/checkout/apm/pay-upon-invoice/fraudnet/#link-modifythecode) section for details about how to create this ID. | String | Required | Maximum length: 32 |

The JavaScript snippet also uses this attribute.

| Parameter | Description | Type | Required |
| --- | --- | --- | --- |
| sandbox | Set totruefor a transaction in a sandbox environment. For a live payment, you can either set this tofalseor omit this attribute. | boolean | Required for sandbox |

All other FraudNet parameters are optional.

## JavaScript

## JavaScript snippet

The JavaScript snippet requires an fncls attribute set to fnparams-dede7cc5-15fd-4c75-a9f4-36c430ee3a99 .

To find and process parameters, FraudNet JavaScript searches for a script of type application/json with an attribute fncls , and its value must match that string.

### FraudNet parameters

Run the following fnparams configuration script on a modern browser with JavaScript enabled to pass parameters to FraudNet.

1 `<scripttype="application/json"fncls="fnparams-dede7cc5-15fd-4c75-a9f4-36c430ee3a99">2{3"f":"<32_character_GUID>",4"s":"<merchant_id_\lt;page_id_\gt>",5"sandbox":false6}7</script>`

### Loading script

There are 2 options for passing the FraudNet data on the web page:

Option 1: Insert this code after the fnparams configuration script:

1 `<scripttype="text/javascript"src="https://c.paypal.com/da/r/fb.js">2</script>Option 2: Append this code after your logic and pass your configuration as options:

1 `{2fnUrl:"https://c.paypal.com/da/r/fb.js";3}4function_loadFraudnetConfig(options){5varscript=document.createElement("script");6script.src=options.fnUrl;7document.body.appendChild(script);8}`

## Noscript

### Noscript snippet

The noscript/ code block renders only in web browsers that don't have JavaScript enabled. The code collects data from a visitor, even when JavaScript isn't available:

1 `<noscript>2<imgsrc="https://c.paypal.com/v1/r/d/b/ns?f=<32_character_GUID>3<s=merchant_id_\lt;page_id_\gt;4</noscript>`

## Modify the code

- Set a unique and random identifier for the current transaction or session in the FraudNet f parameter, also known as FraudNet Session Identifier . The maximum length of the parameter is 32 characters.
- Send the FraudNet f parameter value in the PAYPAL-CLIENT-METADATA-ID HTTP header for the [Create order](/docs/api/orders/v2/#orders_create) API request in [Step 2](/docs/checkout/apm/pay-upon-invoice/integrate-pui-merchant/#2-create-an-order) of the Integrate Pay upon Invoice page.
- Set a unique identifier for each web page in the FraudNet s parameter, also known as Source Website Identifier . The maximum length of the parameter is 32 characters. Use <merchant_id_\lt;page_id_\gt; to create unique identifiers for the s parameter. Locate these values as follows:

- merchant_id - go to your profile and select **Account Settings \gt; Business Information \gt; PayPal Merchant ID** .
- page_id - use one of the following values: home-page , search-result-page , category-page , product-detail-page , cart-page , inline-cart-page , checkout-page .