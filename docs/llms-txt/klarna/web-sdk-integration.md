# Source: https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/web-sdk-integration.md

# Web SDK integration for Sign in with Klarna

## Integrate Sign in with Klarna to offer a fast, simple and smooth login to your customers.

## Quick Start

The simplest and fastest way to start using **Sign in with Klarna** is to use the minimal template below. Please refer to the [Before you start](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/before-you-start/) article for instructions on how to obtain your CLIENT_ID. This guide applies to the PUBLIC client type. If your client is set to CONFIDENTIAL, please refer to the next section. Basic example: Assume that you are serving these 2 files from your web server.

### index.html

```html
<html>
<head>
<!-- 
       1. Add SDK with `defer` attribute 
       to ensure DOM creation was finished. 
    -->
<script data-client-id="[YOUR CLIENT ID]" defer="" src="https://js.klarna.com/web-sdk/v1/klarna.js"></script>
<!-- 
       2. Implement KlarnaSDKCallback
       to add the Sign in with Klarna button and
       handle signin event 
    -->
<script type="text/javascript">
      window.KlarnaSDKCallback = function (klarna) {
        // Listen for `signin` event to receive signin response object
        klarna.Identity.on("signin", async (signinResponse) => {
          console.log(signinResponse);
        });
        // Listen for `error` event to handle error object
        klarna.Identity.on("error", async (error) => {
          console.log(error);
        });
        // Create Sign in with Klarna Button
        const siwkButton = klarna.Identity.button({
          scope: "openid offline_access payment:request:create profile:name",
          redirectUri: "http://localhost:3000/callback.html",
          locale: "en-GB",
        });
        // Mount the button to DOM
        siwkButton.mount('#siwk-button-container')
      };
    </script>
</head>
<body>
<!-- 
       3. Add a container in which 
       the button should be displayed.
     -->
<div id="siwk-button-container">
</div></body>
</html>
```

### callback.html

```html
<html>
<head>
<!-- 
       1. Add SDK with `defer` attribute 
       to ensure DOM creation was finished. 
    -->
<script data-client-id="[YOUR CLIENT ID]" defer="" src="https://js.klarna.com/web-sdk/v1/klarna.js"></script>
<!-- 
       2. Implement KlarnaSDKCallback
       to add the Sign in with Klarna button and
       handle signin event 
    -->
<script type="text/javascript">
      window.KlarnaSDKCallback = function (klarna) {
        // Listen for `signin` event to receive signin response object
        klarna.Identity.on("signin", async (signinResponse) => {
          console.log(signinResponse);
        });
        // Listen for `error` event to handle error object
        klarna.Identity.on("error", async (error) => {
          console.log(error);
        });
      };
    </script>
</head>
<body>
<!-- 
       Notice that the head section is almost 
       exactly the same as the index.html page.
       The only difference is, on callback page,
       we do NOT need to create the 
       Sign in with Klarna button.
     -->
</body>
</html>
```

### signinResponse Example

```json
// When user is successfully signed in,
// the `signin` event callback function 
// receives the payload below
{
  user_account_profile: {
    billing_address: {
      city: 'Stockholm',
      country: 'SE',
      postal_code: '11460',
      region: null,
      street_address: 'Karlaplan 3',
      street_address2: null,
      street_address_2: null,
    },
    shipping_address: {
      city: 'Stockholm',
      country: 'SE',
      postal_code: '11460',
      region: null,
      street_address: 'Karlaplan 3',
      street_address2: null,
    },
    country: 'SE',
    date_of_birth: '1984-09-21',
    email: 'test-customer-se@klarna.com',
    email_verified: true,
    family_name: 'Karlsson',
    given_name: 'Karl',
    national_identification_number: '198409219667',
    national_identification_number_country: 'SE',
    locale: 'en-SE',
    sub: 'krn:kuid:5zzA3kBIfav9PyrAvzRukv',
  },
  user_account_linking: {
    user_account_linking_refresh_token:
      'ory_rt_EuYm5MBm3j2mlnqxN8lA36YuTaNzxelTkCcV-77kUKE.M9arpltHuhDGb....',
    user_account_linking_id_token:
      'eyJhbGciOiJSU...',
  },
}
```

### For confidential client

You would need to also obtain the \`CLIENT_SECRET\`. Please refer to the [Before you start](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/before-you-start/) article for instructions on how to obtain your CLIENT_SECRET.

### index.html

```html
<html>
<head>
<!-- 
       1. Add SDK with `defer` attribute 
       to ensure DOM creation was finished. 
    -->
<script data-client-id="[YOUR CLIENT ID]" defer="" src="https://js.klarna.com/web-sdk/v1/klarna.js"></script>
<!-- 
       2. Implement KlarnaSDKCallback
       to add the Sign in with Klarna button and
       handle signin event 
    -->
<script type="text/javascript">
      window.KlarnaSDKCallback = function (klarna) {
        // Listen for `signin` event for the authorization_code
        klarna.Identity.on("signin", async (codeResponse) => {
          console.log(codeResponse);
          // You would need to pass this code to your backend to exchange the token with the Klarna /token endpoint, please see the example on the token exchange tab.
        });
        // Listen for `error` event to handle error object
        klarna.Identity.on("error", async (error) => {
          console.log(error);
        });
        // Create Sign in with Klarna Button
        const siwkButton = klarna.Identity.button({
          scope: "openid offline_access payment:request:create profile:name",
          redirectUri: "http://localhost:3000/callback.html",
          locale: "en-GB",
          clientType: "confidential"
        });
        // Mount the button to DOM
        siwkButton.mount('#siwk-button-container');
      };
    </script>
</head>
<body>
<!-- 
       3. Add klarna-identity-button element 
       with required attributes.
     -->
<div id="siwk-button-container">
</div></body>
</html>
```

### callback.html

```html
<html>
<head>
<!-- 
       1. Add SDK with `defer` attribute 
       to ensure DOM creation was finished. 
    -->
<script data-client-id="[YOUR CLIENT ID]" defer="" src="https://js.klarna.com/web-sdk/v2/klarna.js"></script>
<!-- 
       2. Implement KlarnaSDKCallback
       to add the Sign in with Klarna button and
       handle signin event 
    -->
<script type="text/javascript">
      window.KlarnaSDKCallback = function (klarna) {
        // Listen for `signin` event for the authorization_code
        klarna.Identity.on("signin", async (codeResponse) => {
          console.log(codeResponse);
          // You would need to pass this code to your backend to exchange the token with the Klarna /token endpoint, please see the example on the token exchange tab.
        });
        // Listen for `error` event to handle error object
        klarna.Identity.on("error", async (error) => {
          console.log(error);
        });
      };
    </script>
</head>
<body>
<!-- 
       Notice that the head section is almost 
       exactly the same as the index.html page.
       The only difference is, on callback page,
       we do NOT need to create the 
       Sign in with Klarna button.
     -->
</body>
</html>
```

### codeResponse Example

```json
// When user is successfully signed in,
// the `signin` event callback function 
// receives the payload below
{
  "code": "ory_ac_79aOXXm39rfMunrYXglwHZn3dseaMpGAb5b_kJB6WcE..."
}
```

After obtaining the code response, pass it to your server to perform the token exchange. Here’s a JavaScript snippet demonstrating how to send a request to the token endpoint for the exchange:

```javascript
// An example of the request to exchange for the token.
const { URLSearchParams } = require('url');
const fetch = require('node-fetch');
const encodedParams = new URLSearchParams();
encodedParams.set('grant_type', 'authorization_code');
encodedParams.set('client_id', '[YOUR CLIENT ID]');
encodedParams.set('client_secret', '[YOUR API KEY]');
encodedParams.set('code', 'ory_ac_79aOXXm39rfMunrYXglwHZn3dseaMpGAb5b_kJB6WcE...');
let url = 'https://login.klarna.com/eu/lp/idp/oauth2/token';
let options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
  },
  body: encodedParams
};
fetch(url, options)
  .then(res => res.json())
  .then(result => console.log(result))
  .catch(err => console.error('error:' + err));
// result 
// {
//  "access_token": "ory_at_rZtxAHxrjVE3k2BhOg0F9aQ4EjkrC7EhhIvc7rRFRg0.oO0KaI3hxTEeqwtqVXnGqphYIG9thp3c2R7HH2alNZE",
//  "expires_in": 300,
//  "id_token": "eyJhbGciOiJSUzI1.....",
//  "refresh_token": "ory_rt_Cg-heIYDS-nhPh2N5KQppfMXr6Nj3EckzB2wXcWBKPw....",
//  "scope": "[REQUESTED_SCOPE]",
//  "token_type": "bearer"
// }
```

### IMPORTANT: Why do you need the callback page?

Sign in with Klarna ideally will start in a Popup window to avoid users leaving the merchant's website. However, due to various reasons popup window can be **blocked**. Thus, having a `redirect callback page` is **REQUIRED** to allow users to continue their sign in flow in case their popup is blocked. You can use the callback.html template provided in the example above. To successfully implement the REDIRECT mode, below prerequisites must be met:

- The redirect URL must match exactly with one of the URLs whitelisted for your client.
- The redirect URL must be either passed to the `button` **method** with the redirectUri property or `klarna-identity-button` **element** with `data-redirect-uri` attribute.
- The redirect URL page must contain the Web SDK and event handler for `signin` must be registered.

### Understanding the interaction modes

The Sign in with Klarna flow can be initiated in two main modes: DEVICE_BEST or REDIRECT.

#### DEVICE_BEST (default)

DEVICE_BEST allows Web SDK to automatically decide the most suitable mode, based on user's device configurations. For instance, Web SDK may opt for a REDIRECT if popup blockers are enabled or the page is loaded in an web frame. By default, DEVICE_BEST mode starts the flow in a popup window for web browsers. This is ideal for merchants who don't want their customers to leave their website. However, if the popup is blocked, Web SDK will switch to REDIRECT mode and the user will be redirected to the login page on the current tab.

#### REDIRECT

`REDIRECT` mode redirects the user to the login page on the current tab. However, user will be redirected back to the merchant's redirect callback page at the end of the sign in flow with Authorization tokens or **OAuth2Error** parameters.

## Initialising the Web SDK programmatically

Please note that you can also just load the Web SDK script **without** the dataset attributes and use the `init` method to initialise the Web SDK.

```javascript
<script defer="" src="https://js.klarna.com/web-sdk/v1/klarna.js"></script>
<script>
  window.onload = async function () {
    const klarna = await Klarna.init({
      clientId: "<YOUR CLIENT ID>"
    });
  };
</script>
```

## Identity API Overview

After initialising the Web SDK, all **Sign in with Klarna** related API can be found under the `Identity` namespace.

### Type Definitions

```typescript
interface Identity {
  /**
   * Returns the button with given id
   *
   * If id is not provided, returns the first button instance
   *
   * If no button instance found returns undefined
   */
  button(id?: string): KlarnaIdentityButton | undefined;
  /**
   * Creates the button with given configuration
   *
   * `id` attribute is required for creating more than one Identity Button.
   */
  button(
    configuration: KlarnaIdentityButtonConfiguration
  ): KlarnaIdentityButton;
  /**
   * Registers `signin` event handler.
   *
   * This event handler needs to be registered also on the redirect callback page
   * to trigger handling redirect response.
   */
  on(
    event: "signin",
    callback: (response: IdentitySignInResponse) => Promise<void>
  ): void;
  /**
   * Registers `error` event handler.
   */
  on(event: "error", callback: (error: Error) => Promise<void>): void;
}
/**
 * Interface to the Identity Button interface.
 */
interface KlarnaIdentityButton {
  /**
   * The `ready` event can be used to load in data asynchronously,
   * it is triggered when the button was mounted or attached
   * and openid configuration was fetched successfully.
   */
  on(event: "ready", callback: () => Promise<void>): void;
  /**
   * Button click event handler, triggered when the consumer clicks on an Identity Button.
   */
  on(event: "click", callback: () => Promise<void>): void;
  /**
   * Programmatically adds a button to the DOM tree, inside the given container element.
   *
   * Semantically the same as creating a `<klarna-identity-button>` tag.
   * Timings
   *  - When using `mount` method the `ready` event is triggered after the button was added to DOM
   * and openid configuration was fetched.
   */
  mount(containerId: string): void;
  mount(container: HTMLElement): void;
  /**
   * Programmatically removes the button from the DOM tree
   */
  unmount(): void;
  /**
   * Programmatically attach the Identity Button behavior to a merchant's custom button element.
   *
   * Timings
   *  - When using `attach` method the `ready` event is triggered after the button event handlers
   * were attached to the custom button and openid configuration was fetched.
   */
  attach(customButtonId: string): void;
  attach(customButtonElement: HTMLElement): void;
  /**
   * Programmatically detaches the Identity Button behavior from merchant's custom button element
   */
  detach(): void;
}
interface KlarnaIdentityButtonConfiguration {
  scope: string;
  redirectUri: string;
  locale?: string;
  id?: string;
  shape?: "default" | "pill" | "rect";
  theme?: KlarnaTheme;
  logoAlignment?: KlarnaIdentityButtonLogoAlignment;
  hideOverlay?: boolean;
  interactionMode?: FlowInteractionMode;
}
type KlarnaIdentityButtonLogoAlignment = "left" | "center" | "right";
enum KlarnaTheme {
  DEFAULT = "default",
  LIGHT = "light",
  DARK = "dark",
  OUTLINED = "outlined",
}
type IdentitySignInResponse = {
  user_account_profile: UserAccountProfile;
  user_account_linking: UserAccountLinking;
};
interface UserAccountLinking {
  user_account_linking_refresh_token: string;
  user_account_linking_id_token: string;
}
interface UserAccountProfile {
  billing_address?: BillingAddress;
  country?: string | null;
  date_of_birth?: string | null;
  email?: string | null;
  email_verified?: boolean;
  family_name?: string | null;
  given_name?: string | null;
  phone?: string | null;
  national_identification_number?: string | null;
  national_identification_number_country?: string | null;
  locale?: string | null;
  sub: string;
}
interface BillingAddress {
  city: string | null;
  country: string | null;
  postal_code: string | null;
  region: string | null;
  street_address: string | null;
  street_address_2: string | null;
}
```

## Displaying the Sign in with Klarna Button

Web SDK provides a flexible API that allows merchants to integrate Sign in with Klarna based on their preference.

### 1. Using the default Sign in with Klarna button

Web SDK provides a default button that has all functionalities built-in and styled based on official Klarna design guidelines.

#### 1.1. Using <klarna-identity-button></klarna-identity-button> element

Web SDK registers a custom web component klarna-identity-button, that renders the Sign in with Klarna button where it is mounted.

```html
<klarna-identity-button data-locale="en-GB" data-redirect-uri="http://localhost:3000/callback.html" data-scope="openid offline_access payment:request:create profile:name" id="klarna-identity-button"></klarna-identity-button>
```

#### 1.2. Creating the button programmatically

Web SDK provides the `button` method that allows to create and mount the Sign in with Klarna button programmatically.

```javascript
window.KlarnaSDKCallback = function (klarna) {
  const siwkButton = klarna.Identity.button({
    id: "klarna-identity-button",
    scope: "openid offline_access payment:request:create profile:name",
    redirectUri: "http://localhost:3000/callback.html",
    locale: "en-GB"
  });
  siwkButton.mount("#button-container");
};
```

If the `button` method is called more than once with the configuration**object**, it will create multiple button instances. If you do not need more than one button, please make sure the button method is only called once. If you do need **multiple** buttons make sure you provide an `id` attribute to each button instance. You can provide a **string** button id to the button method, to retrieve an existing button instance. For more information, see the **Identity API Overview\> Type Definitions**.

### 2. Using your custom Sign in with Klarna button

If a merchant wants to use a custom button matching with Klarna's but also with their own design guidelines, they can use the attach method that is provided by Web SDK. The attach method will register the necessary event handlers to start the sign in flow. Please refer to our [Custom button](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/additional-resources/button-styling/) article for essential design considerations.

```javascript
window.KlarnaSDKCallback = function (klarna) {
  const siwkButton = klarna.Identity.button({
    id: "klarna-identity-button",
    scope: "openid offline_access payment:request:create profile:name",
    redirectUri: "http://localhost:3000/callback.html",
    locale: "en-GB"
  });
  // notice, we are using the `attach` method
  // and providing a button id instead of a container id
  siwkButton.attach("#merchants-custom-button-id");
};
```

## Events

### SDK Events

Web SDK Identity API can emit two events: `signin` and `error` which can be handled as below:

```javascript
window.KlarnaSDKCallback = function (klarna) {
  // 1. Listen for `signin` event to receive signin response object
  klarna.Identity.on("signin", async (signinResponse) => {
    console.log(signinResponse);
  });
  // 2. Listen for `error` event to handle error object
  klarna.Identity.on("error", async (error) => {
    console.log(error);
  });
};
```

### Button Events

Sign in with Klarna buttons can emit two events: `ready` and `click`.

```javascript
window.KlarnaSDKCallback = function (klarna) {
  // Please notice that we can retrieve the button instance,
  // by providing the button instance id to the button method
  const siwkButton = klarna.Identity.button("klarna-identity-button");
  siwkButton.on('ready', async () => {
    // handle ready event
  })
  siwkButton.on('click', async () => {
    // handle click event
  });
};
```

## Scopes and Claims

The table below lists the available scopes and how they correspond to claims and permissions. 

| Scope | Claims | Type | Can be toggled off |
|----|----|----|----|
| profile:name | given_name | string | No |
| profile:name | family_name | string | No |
| profile:email | email | string (Email) | No |
| profile:email | email_verified | boolean |  |
| profile:phone | phone | string (E. 164) | No |
| profile:phone | phone_verified | boolean |  |
| profile:date_of_birth | date_of_birth | string (ISO 8601) | Yes |
| profile:billing_address | street_address | string | Yes |
| profile:billing_address | street_address2 | string |  |
| profile:billing_address | postal_code | string |  |
| profile:billing_address | city | string |  |
| profile:billing_address | region | string |  |
| profile:billing_address | country | string (ISO 3166-1 alpha-2) |  |
| profile:shipping_address | street_address | string | Yes |
| profile:shipping_address | street_address2 | string |  |
| profile:shipping_address | postal_code | string |  |
| profile:shipping_address | city | string |  |
| profile:shipping_address | region | string |  |
| profile:shipping_address | country | string (ISO 3166-1 alpha-2) |  |
| profile:national_id | national_id | string | Yes |
| profile:country | country | string (ISO 3166-1 alpha-2) | Yes |
| profile:locale | locale | string (ISO 3166) | Yes |
| payment:consumer_present | trigger on-demand flow | N/A | N/A |
| payment:consumer_not_present | trigger subscription flow | N/A | N/A |

Remember to always add 'openid', 'offline_access' and 'payment:request:create' scopes to receive full functionality of Sign in with Klarna. The mock-ups below show how users will see required versus optional scopes when entering the Sign in with Klarna flow.   

![klarna docs image](e0d14625-c96b-4268-a3b0-dff196b42b93_Siwk_mock_up.jpeg)

## Finalizing the sign in the flow 

Before using data from the `id_token`, it needs to be validated. More about it under [Token Validation](https://docs.klarna.com/sign-in-with-klarna/additional-resources/other-operations/#token-validation). Upon completing the sign-in process, utilise a specific `claim` (such as phone, email, or national identification number for Sweden) as a unique customer identifier.  Make sure you are handling the following scenarios to ensure seamless integration:

- **New Users:** If the identifier does not match any existing user in your database, check if the consumer consented to share all the data you requested. If additional information is required, remember to show your onboarding UI after Sign in with Klarna flow. Once onboarding is complete, create a new user account using the data returned from Klarna and store the `user_account_linking_refresh_token` within that record.
- **Existing Klarna Users:** In cases where the identifier is already linked to a Klarna account, Sign in with Klarna always returns fresh customer data. Update your user record with this data to ensure that the information in your database remains current.
- **Existing Users:** For users already in your database but not connected to Klarna, consider these approaches:

| Account Merging | User Confirmation for Merging |
|----|----|
| Merge the account automatically, add customer data from Klarna that was missing in the existing record and save the `user_account_linking_refresh_token` in it | Prompt the user to confirm if they wish to merge their existing account. If yes, follow *Account Merging*above. If not, ask them to login with a different Klarna account |

By carefully managing these scenarios, you can provide a fluid and integrated user experience, leveraging the comprehensive data and functionality offered through the Sign in with Klarna.

## Integrating in purchase flow 

For those who have already integrated [Klarna Payments](https://docs.klarna.com/klarna-payments/), Sign in with Klarna enhances user experience by enabling automatic login within these products. To achieve this, simply pass the `access_token`, obtained from a token refresh call (see [Refresh Token](https://docs.klarna.com/sign-in-with-klarna/additional-resources/other-operations/#refresh-token)), to your existing integrations. You can find examples below depending if you have Klarna Payments. `access_token` has a limited lifespan of only 5 minutes. Therefore, it's essential to renew the token right before initiating the checkout process. To receive a new set of token, perform a token exchange through a POST request to the token endpoint. Remember to always save the new refreshed token in the database, since the old one will be invalid.

#### For Klarna Payments 

Include the access_token in the POST [create a payment session](https://docs.klarna.com/api/payments/#operation/createCreditSession) request to the Klarna payments API. Add the key to the [customer object](https://docs.klarna.com/api/checkout/#operation/createOrderMerchant!path=customer&t=request) as klarna\_access\_token key as shown in the example below.

```javascript
fetch("https://api.klarna.com/payments/v1/sessions", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: {
      ...
      "customer": {
            ...
            "klarna_access_token": "access_token",
            ...
      },
      ...
    }
})
```