# Source: https://docs.stripe.com/payments/accept-stablecoin-payments.md

# Accept stablecoin payments

Start accepting stablecoins by enabling the Crypto payment method.

You can accept *stablecoin* (A cryptocurrency that's pegged to the value of a fiat currency or other asset in order to limit volatility) payments through *Payment Links* (A link to a secure, hosted payment page that you can generate without code. Share it directly with your customers, or point them to it with a button or QR code), *Checkout* (A low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website, redirect customers to a Stripe-hosted payment page, or create a customized checkout page with Stripe Elements), *Elements* (A set of UI components for building a web checkout flow. They adapt to your customer's locale, validate input, and use tokenization, keeping sensitive customer data from touching your server), or the *Payment Intents API* (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods). When paying with stablecoins such as USDC, customers get redirected to [crypto.stripe.com](https://crypto.stripe.com) to connect their crypto wallet and complete the transaction. Funds settle in your Stripe balance in USD.

## Before you begin

> Customers can use stablecoins as payment globally, but currently only US businesses can accept stablecoin payments.

To start accepting stablecoin payments, activate the **Crypto** payment method:

1. Make sure your Stripe account is [Active](https://docs.stripe.com/get-started/account/activate.md).
1. Go to **Settings > Payments > [Payment methods](https://dashboard.stripe.com/settings/payment_methods)** and request the **Crypto** payment method.
1. Stripe reviews your access request, and might contact you for more details if necessary. In this case, the payment method appears as **Pending** while we review your request.
1. After you’re approved, **Crypto** becomes active in the Dashboard.

## Use with dynamic payment methods (Recommended)

If you use Stripe’s default [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) with Payment Links, Hosted Checkout, Embedded Checkout Forms, or Elements, then you don’t need to make any further updates. Stripe automatically displays stablecoin payment options to eligible customers.

## Use with a custom integration

If necessary, you can add the crypto payment method to your payment integration manually.

# Stripe-hosted page

> This is a Stripe-hosted page for when platform is web and payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/accept-stablecoin-payments?platform=web&payment-ui=stripe-hosted.

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `crypto` to the list of `payment_method_types`.

1. Make sure all `line_items` use `usd`.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u <<YOUR_SECRET_KEY>>: \
  -d mode=payment \
  -d "payment_method_types[0]"=crypto \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][price_data][product_data][name]"=T-shirt \
  -d "line_items[0][price_data][unit_amount]"=2000 \
  -d "line_items[0][quantity]"=1 \
  --data-urlencode success_url="https://example.com/success"
```

## Test your integration 

Test your crypto payment integration by opening the payment redirect page using your test API keys. You can test a successful payment flow at no cost using [testnet assets](https://docs.stripe.com/payments/accept-stablecoin-payments.md#testnet-assets).

1. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), create a new transaction using your chosen integration method, and open its redirect URL.
1. Connect your preferred wallet and payment network.
1. Complete the payment, and validate that you’re redirected to the expected URL.

### Test payments with testnet assets 

Most cryptocurrencies offer testnet assets, or tokens that have no monetary value, that you can use to test blockchain transactions. Stripe recommends the MetaMask wallet, Polygon Amoy testnet, and Circle faucet for testing, but you can use your own preferred services.

#### Install a wallet

1. [Download the MetaMask extension](https://metamask.io/download) for your web browser.
1. [Create a new wallet](https://support.metamask.io/start/creating-a-new-wallet/) or [import an existing one](https://support.metamask.io/start/use-an-existing-wallet/).

#### Enable a testnet

1. In your MetaMask wallet, select **Networks** from the main menu.
1. Click **Add custom network**.
1. Enter the following details:
   - **Network name**: `Polygon Amoy`
   - **Default RPC URL**: `https://rpc-amoy.polygon.technology/`
   - **Chain ID**: `80002`
   - **Currency symbol**: `POL`
   - **Block explorer URL**: `https://amoy.polygonscan.com/`
1. Click **Save**.

#### Import a token

1. In your MetaMask wallet, under **Tokens**, select **Polygon Amoy** from the network dropdown.
1. Click the overflow menu (⋯), and select **Import tokens**.
1. Click **Select a network** > **Polygon Amoy**.
1. Under **Token contract address**, paste the Polygon Amoy testnet contract address:
   ```
   0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582
   ```
The **Token symbol** field automatically updates with `USDC` and the **Decimals** field with `6`.
1. Click **Next**.
1. Verify that you’re importing the `USDC` token, and then click **Import**.

Your MetaMask wallet now shows **Polygon Amoy** and **USDC** in the tokens list.

#### Get testnet assets

1. Open [faucet.circle.com](https://faucet.circle.com/)
1. Click **USDC**.
1. Under **Network**, select **Polygon PoS Amoy**.
1. Under **Send to**, paste your wallet address.
1. Click **Send 10 USDC**.

In addition to USDC for making payments, you need POL to pay transaction costs:

1. Open [faucet.polygon.technology](https://faucet.polygon.technology/).
1. Under **Select Chain & Token**, select **Polygon Amoy** and **POL**.
1. Under **Verify your identity**, click the third-party platform you want to authenticate with, and complete the login process.
1. Under **Enter Wallet Address**, paste your wallet address.
1. Click **Claim**.

Testnet transactions can take a few minutes to complete. Check your wallet to confirm that the USDC and POL has transferred.

### More testnet faucets

Check these faucet services for more testing token options:

- [Paxos USDP](https://faucet.paxos.com/)
- [Devnet SOL](https://faucet.solana.com/)
- [Sepolia ETH](https://faucets.chain.link/sepolia)
- [Amoy POL](https://faucet.polygon.technology/)


# Advanced integration

> This is a Advanced integration for when platform is web and payment-ui is elements. View the full page at https://docs.stripe.com/payments/accept-stablecoin-payments?platform=web&payment-ui=elements.

Embed a custom payment form in your website or application using the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element automatically supports crypto and other payment methods. For additional configuration and customization options, see [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?platform=web&ui=elements).

## Set up Stripe [Server-side]

First, [create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).

Use our official libraries to access the Stripe API from your application:

#### Ruby

```bash
# Available as a gem
sudo gem install stripe
```

```ruby
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

#### Python

```bash
# Install through pip
pip3 install --upgrade stripe
```

```bash
# Or find the Stripe package on http://pypi.python.org/pypi/stripe/
```

```python
# Find the version you want to pin:
# https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md
# Specify that version in your requirements.txt file
stripe>=5.0.0
```

#### PHP

```bash
# Install the PHP library with Composer
composer require stripe/stripe-php
```

```bash
# Or download the source directly: https://github.com/stripe/stripe-php/releases
```

#### Java

```java
/*
  For Gradle, add the following dependency to your build.gradle and replace with
  the version number you want to use from:
  - https://mvnrepository.com/artifact/com.stripe/stripe-java or
  - https://github.com/stripe/stripe-java/releases/latest
*/
implementation "com.stripe:stripe-java:30.0.0"
```

```xml
<!--
  For Maven, add the following dependency to your POM and replace with the
  version number you want to use from:
  - https://mvnrepository.com/artifact/com.stripe/stripe-java or
  - https://github.com/stripe/stripe-java/releases/latest
-->
<dependency>
  <groupId>com.stripe</groupId>
  <artifactId>stripe-java</artifactId>
  <version>30.0.0</version>
</dependency>
```

```bash
# For other environments, manually install the following JARs:
# - The Stripe JAR from https://github.com/stripe/stripe-java/releases/latest
# - Google Gson from https://github.com/google/gson
```

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

#### Go

```bash
# Make sure your project is using Go Modules
go mod init
# Install stripe-go
go get -u github.com/stripe/stripe-go/v83
```

```go
// Then import the package
import (
  "github.com/stripe/stripe-go/v83"
)
```

#### .NET

```bash
# Install with dotnet
dotnet add package Stripe.net
dotnet restore
```

```bash
# Or install with NuGet
Install-Package Stripe.net
```

## Create a PaymentIntent and retrieve the client secret [Server-side]

The [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object represents your intent to collect payment from your customer and tracks the lifecycle of the payment process. Create a PaymentIntent on your server and specify the amount to collect and a supported currency. If you have an existing PaymentIntents integration, add `crypto` to the list of [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=usd \
  -d "payment_method_types[]"=crypto
```

```cli
stripe payment_intents create  \
  --amount=1099 \
  --currency=usd \
  -d "payment_method_types[0]"=crypto
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['crypto'],
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
payment_intent = client.v1.payment_intents.create({
  "amount": 1099,
  "currency": "usd",
  "payment_method_types": ["crypto"],
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->create([
  'amount' => 1099,
  'currency' => 'usd',
  'payment_method_types' => ['crypto'],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentCreateParams params =
  PaymentIntentCreateParams.builder()
    .setAmount(1099L)
    .setCurrency("usd")
    .addPaymentMethodType("crypto")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
PaymentIntent paymentIntent = client.v1().paymentIntents().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['crypto'],
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentCreateParams{
  Amount: stripe.Int64(1099),
  Currency: stripe.String(stripe.CurrencyUSD),
  PaymentMethodTypes: []*string{stripe.String("crypto")},
}
result, err := sc.V1PaymentIntents.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new PaymentIntentCreateOptions
{
    Amount = 1099,
    Currency = "usd",
    PaymentMethodTypes = new List<string> { "crypto" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.Create(options);
```

### Retrieve the client secret

The PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Ruby

```ruby
get '/secret' do
  intent = # ... Create or retrieve the PaymentIntent
  {client_secret: intent.client_secret}.to_json
end
```

#### Python

```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/secret')
def secret():
  intent = # ... Create or retrieve the PaymentIntent
  return jsonify(client_secret=intent.client_secret)
```

#### PHP

```php
<?php
    $intent = # ... Create or retrieve the PaymentIntent
    echo json_encode(array('client_secret' => $intent->client_secret));
?>
```

#### Java

```java
import java.util.HashMap;
import java.util.Map;

import com.stripe.model.PaymentIntent;

import com.google.gson.Gson;

import static spark.Spark.get;

public class StripeJavaQuickStart {
  public static void main(String[] args) {
    Gson gson = new Gson();

    get("/secret", (request, response) -> {
      PaymentIntent intent = // ... Fetch or create the PaymentIntent

      Map<String, String> map = new HashMap();
      map.put("client_secret", intent.getClientSecret());

      return map;
    }, gson::toJson);
  }
}
```

#### Node.js

```javascript
const express = require('express');
const app = express();

app.get('/secret', async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
  res.json({client_secret: intent.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Go

```go
package main

import (
  "encoding/json"
  "net/http"

  stripe "github.com/stripe/stripe-go/v76.0.0"
)

type CheckoutData struct {
  ClientSecret string `json:"client_secret"`
}

func main() {
  http.HandleFunc("/secret", func(w http.ResponseWriter, r *http.Request) {
    intent := // ... Fetch or create the PaymentIntent
    data := CheckoutData{
      ClientSecret: intent.ClientSecret,
    }
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    json.NewEncoder(w).Encode(data)
  })

  http.ListenAndServe(":3000", nil)
}
```

#### .NET

```csharp
using System;
using Microsoft.AspNetCore.Mvc;
using Stripe;

namespace StripeExampleApi.Controllers
{
  [Route("secret")]
  [ApiController]
  public class CheckoutApiController : Controller
  {
    [HttpGet]
    public ActionResult Get()
    {
      var intent = // ... Fetch or create the PaymentIntent
      return Json(new {client_secret = intent.ClientSecret});
    }
  }
}
```

And then fetch the client secret with JavaScript on the client side:

```javascript
(async () => {
  const response = await fetch('/secret');
  const {client_secret: clientSecret} = await response.json();
  // Render the form using the clientSecret
})();
```

#### Server-side rendering

Pass the client secret to the client from your server. This approach works best if your application generates static content on the server before sending it to the browser.

Add the [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) in your checkout form. In your server-side code, retrieve the client secret from the PaymentIntent:

#### Ruby

```erb
<form id="payment-form" data-secret="<%= @intent.client_secret %>">
  <div id="payment-element">
    <!-- placeholder for Elements -->
  </div>
  <button id="submit">Submit</button>
</form>
```

```ruby
get '/checkout' do
  @intent = # ... Fetch or create the PaymentIntent
  erb :checkout
end
```

#### Python

```html
<form id="payment-form" data-secret="{{ client_secret }}">
  <div id="payment-element">
    <!-- placeholder for Elements -->
  </div>
  <button id="submit">Submit</button>
</form>
```

```python
@app.route('/checkout')
def checkout():
  intent = # ... Fetch or create the PaymentIntent
  return render_template('checkout.html', client_secret=intent.client_secret)
```

#### PHP

```php
<?php
  $intent = # ... Fetch or create the PaymentIntent;
?>
...
<form id="payment-form" data-secret="<?= $intent->client_secret ?>">
  <div id="payment-element">
    <!-- placeholder for Elements -->
  </div>
  <button id="submit">Submit</button>
</form>
...
```

#### Java

```html
<form id="payment-form" data-secret="{{ client_secret }}">
  <div id="payment-element">
    <!-- placeholder for Elements -->
  </div>
  <button id="submit">Submit</button>
</form>
```

```java
import java.util.HashMap;
import java.util.Map;

import com.stripe.model.PaymentIntent;

import spark.ModelAndView;

import static spark.Spark.get;

public class StripeJavaQuickStart {
  public static void main(String[] args) {
    get("/checkout", (request, response) -> {
      PaymentIntent intent = // ... Fetch or create the PaymentIntent

      Map map = new HashMap();
      map.put("client_secret", intent.getClientSecret());

      return new ModelAndView(map, "checkout.hbs");
    }, new HandlebarsTemplateEngine());
  }
}
```

#### Node.js

```html
<form id="payment-form" data-secret="{{ client_secret }}">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>

  <button id="submit">Submit</button>
</form>
```

```javascript
const express = require('express');
const expressHandlebars = require('express-handlebars');
const app = express();

app.engine('.hbs', expressHandlebars({ extname: '.hbs' }));
app.set('view engine', '.hbs');
app.set('views', './views');

app.get('/checkout', async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
  res.render('checkout', { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Go

```html
<form id="payment-form" data-secret="{{ .ClientSecret }}">
  <div id="payment-element">
    <!-- placeholder for Elements -->
  </div>
  <button id="submit">Submit</button>
</form>
```

```go
package main

import (
  "html/template"
  "net/http"

  stripe "github.com/stripe/stripe-go/v76.0.0"
)

type CheckoutData struct {
  ClientSecret string
}

func main() {
  checkoutTmpl := template.Must(template.ParseFiles("views/checkout.html"))

  http.HandleFunc("/checkout", func(w http.ResponseWriter, r *http.Request) {
    intent := // ... Fetch or create the PaymentIntent
    data := CheckoutData{
      ClientSecret: intent.ClientSecret,
    }
    checkoutTmpl.Execute(w, data)
  })

  http.ListenAndServe(":3000", nil)
}
```

#### .NET

```html
<form id="payment-form" data-secret="@ViewData["ClientSecret"]">
  <div id="payment-element">
    <!-- placeholder for Elements -->
  </div>
  <button id="submit">Submit</button>
</form>
```

```csharp
using System;
using Microsoft.AspNetCore.Mvc;
using Stripe;

namespace StripeExampleApi.Controllers
{
  [Route("/[controller]")]
  public class CheckoutApiController : Controller
  {
    public IActionResult Index()
    {
      var intent = // ... Fetch or create the PaymentIntent
      ViewData["ClientSecret"] = intent.ClientSecret;
      return View();
    }
  }
}
```

## Collect payment details [Client-side]

Collect payment details on the client with the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

If you do choose to use an iframe and want to accept Apple Pay or Google Pay, the iframe must have the [allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest) attribute set to equal `"payment *"`.

The checkout page address must start with `https://` rather than `http://` for your integration to work. You can test your integration without using HTTPS, but remember to [enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

#### HTML + JS

### Set up Stripe.js

The Payment Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/clover/stripe.js"></script>
</head>
```

Create an instance of Stripe with the following JavaScript on your checkout page:

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
```

### Add the Payment Element to your payment page

The Payment Element needs a place to live on your payment page. Create an empty DOM node (container) with a unique ID in your payment form:

```html
<form id="payment-form">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>
  <button id="submit">Submit</button>
  <div id="error-message">
    <!-- Display error message to your customers here -->
  </div>
</form>
```

When the previous form loads, create an instance of the Payment Element and mount it to the container DOM node. Pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from the previous step into `options` when you create the [Elements](https://docs.stripe.com/js/elements_object/create) instance:

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

```javascript
const options = {
  clientSecret: '{{CLIENT_SECRET}}',
  // Fully customizable with appearance API.
  appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained in a previous stepconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion'};
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');

```

#### React

### Set up Stripe.js

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the Elements provider to your payment page

To use the Payment Element component, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key, and pass the returned `Promise` to the `Elements` provider. Also pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from the previous step as `options` to the `Elements` provider.

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

import CheckoutForm from './CheckoutForm';

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe('<<YOUR_PUBLISHABLE_KEY>>');

function App() {
  const options = {
    // passing the client secret obtained in step 3
    clientSecret: '{{CLIENT_SECRET}}',
    // Fully customizable with appearance API.
    appearance: {/*...*/},
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
```

### Add the Payment Element component

Use the `PaymentElement` component to build your form:

```jsx
import React from 'react';
import {PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
  return (
    <form><PaymentElement />
      <button>Submit</button>
    </form>
  );
};

export default CheckoutForm;
```

Stripe Elements is a collection of drop-in UI components. To further customize your form or collect different customer information, browse the [Elements docs](https://docs.stripe.com/payments/elements.md).

The Payment Element renders a dynamic form that allows your customer to pick a payment method. For each payment method, the form automatically asks the customer to fill in all necessary payment details.

### Customize appearance

Customize the Payment Element to match the design of your site by passing the [appearance object](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-appearance) into `options` when creating the `Elements` provider.

### Collect addresses

By default, the Payment Element only collects the necessary billing address details. Some behavior, such as [calculating tax](https://docs.stripe.com/api/tax/calculations/create.md) or entering shipping details, requires your customer’s full address. You can:

- Use the [Address Element](https://docs.stripe.com/elements/address-element.md) to take advantage of autocomplete and localization features to collect your customer’s full address. This helps ensure the most accurate tax calculation.
- Collect address details using your own custom form.

### Request Apple Pay merchant token

If you’ve configured your integration to [accept Apple Pay payments](https://docs.stripe.com/payments/accept-a-payment.md?platform=web&ui=elements#apple-pay-and-google-pay), we recommend configuring the Apple Pay interface to return a merchant token to enable merchant initiated transactions (MIT). [Request the relevant merchant token type](https://docs.stripe.com/apple-pay/merchant-tokens.md?pay-element=web-pe) in the Payment Element.

## Optional: Fetch updates from the server [Client-side]

You might want to update attributes on the PaymentIntent after the Payment Element renders, such as the [amount](https://docs.stripe.com/api/payment_intents/update.md#update_payment_intent-amount) (for example, discount codes or shipping costs). You can [update the PaymentIntent](https://docs.stripe.com/api/payment_intents/update.md) on your server, then call [elements.fetchUpdates](https://docs.stripe.com/js/elements_object/fetch_updates) to see the new amount reflected in the Payment Element. This example shows you how to create the server endpoint that updates the amount on the PaymentIntent:

#### Ruby

```ruby
get '/update' do
  intent = Stripe::PaymentIntent.update(
    '{{PAYMENT_INTENT_ID}}',
    {amount: 1499},
  )
  {status: intent.status}.to_json
end
```

#### Python

```python
@app.route('/update')
def secret():
  intent = stripe.PaymentIntent.modify(
    "{{PAYMENT_INTENT_ID}}",
    amount=1499,
  )
  return jsonify(status=intent.status)
```

#### PHP

```php
<?php
    $intent = $stripe->paymentIntents->update(
      '{{PAYMENT_INTENT_ID}}',
      ['amount' => 1499]
    );
    echo json_encode(array('status' => $intent->status));
?>
```

#### Java

```java
import java.util.HashMap;
import java.util.Map;

import com.stripe.model.PaymentIntent;

import com.google.gson.Gson;

import static spark.Spark.get;

public class StripeJavaQuickStart {
  public static void main(String[] args) {
    Gson gson = new Gson();

    get("/update", (request, response) -> {
      PaymentIntent paymentIntent =
        PaymentIntent.retrieve(
          "{{PAYMENT_INTENT_ID}}"
        );

      Map<String, Object> params = new HashMap<>();
      params.put("amount", 1499);
      PaymentIntent updatedPaymentIntent =
        paymentIntent.update(params);

      Map<String, String> response = new HashMap();
      response.put("status", updatedPaymentIntent.getStatus());

      return map;
    }, gson::toJson);
  }
}
```

#### Node.js

```javascript
app.get('/update', async (req, res) => {
  const intent = await stripe.paymentIntents.update(
    '{{PAYMENT_INTENT_ID}}',
    {amount: 1499}
  );
  res.json({status: intent.status});
});
```

#### Go

```go
package main

import (
  "encoding/json"
  "net/http"

  stripe "github.com/stripe/stripe-go/v76.0.0"
)

type UpdateData struct {
  Status string `json:"status"`
}

func main() {
  http.HandleFunc("/update", func(w http.ResponseWriter, r *http.Request) {
    params := &stripe.PaymentIntentParams{
      Amount: stripe.Int64(1499),
    }
    pi, _ := paymentintent.Update(
      "{{PAYMENT_INTENT_ID}}",
      params,
    )

    data := UpdateData{
      Status: pi.Status,
    }
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    json.NewEncoder(w).Encode(data)
  })

  http.ListenAndServe(":3000", nil)
}
```

#### .NET

```csharp
using System;
using Microsoft.AspNetCore.Mvc;
using Stripe;

namespace StripeExampleApi.Controllers
{
  [Route("update")]
  [ApiController]
  public class CheckoutApiController : Controller
  {
    [HttpPost]
    public ActionResult Post()
    {
      var options = new PaymentIntentUpdateOptions
      {
        Amount = 1499,
      };
      var service = new PaymentIntentService();
      var intent = service.Update(
        "{{PAYMENT_INTENT_ID}}",
        options);
      return Json(new {status = intent.Status});
    }
  }
}
```

This example demonstrates how to update the UI to reflect these changes on the client side:

```javascript
(async () => {
  const response = await fetch('/update');
  if (response.status === 'requires_payment_method') {
    const {error} = await elements.fetchUpdates();
  }
})();
```

## Submit the payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element. Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe should redirect the user after they complete the payment. Your user may be first redirected to an intermediate site, like a bank authorization page, before being redirected to the `return_url`. Card payments immediately redirect to the `return_url` when a payment is successful.

If you don’t want to redirect for card payments after payment completion, you can set [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect) to `if_required`. This only redirects customers that check out with redirect-based payment methods.

#### HTML + JS

```javascript
const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
const {error} = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
      return_url: 'https://example.com/order/123/complete',
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    const messageContainer = document.querySelector('#error-message');
    messageContainer.textContent = error.message;
  } else {
    // Your customer will be redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer will be redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
```

#### React

To call [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks.

If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

```jsx
import React, {useState} from 'react';
import {useStripe, useElements, PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
  const stripe = useStripe();
  const elements = useElements();

  const [errorMessage, setErrorMessage] = useState(null);

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }
const {error} = await stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      confirmParams: {
        return_url: 'https://example.com/order/123/complete',
      },
    });


    if (error) {
      // This point will only be reached if there is an immediate error when
      // confirming the payment. Show error to your customer (for example, payment
      // details incomplete)
      setErrorMessage(error.message);
    } else {
      // Your customer will be redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer will be redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Submit</button>
      {/* Show error message to your customers */}
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  )
};

export default CheckoutForm;
```

Make sure the `return_url` corresponds to a page on your website that provides the status of the payment. When Stripe redirects the customer to the `return_url`, we provide the following URL query parameters:

| Parameter                      | Description                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. |

> If you have tooling that tracks the customer’s browser session, you might need to add the `stripe.com` domain to the referrer exclude list. Redirects cause some tools to create new sessions, which prevents you from tracking the complete session.

Use one of the query parameters to retrieve the PaymentIntent. Inspect the [status of the PaymentIntent](https://docs.stripe.com/payments/paymentintents/lifecycle.md) to decide what to show your customers. You can also append your own query parameters when providing the `return_url`, which persist through the redirect process.

#### HTML + JS

```javascript

// Initialize Stripe.js using your publishable key
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');

// Retrieve the "payment_intent_client_secret" query parameter appended to
// your return_url by Stripe.js
const clientSecret = new URLSearchParams(window.location.search).get(
  'payment_intent_client_secret'
);

// Retrieve the PaymentIntent
stripe.retrievePaymentIntent(clientSecret).then(({paymentIntent}) => {
  const message = document.querySelector('#message')

  // Inspect the PaymentIntent `status` to indicate the status of the payment
  // to your customer.
  //
  // Some payment methods will [immediately succeed or fail][0] upon
  // confirmation, while others will first enter a `processing` state.
  //
  // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
  switch (paymentIntent.status) {
    case 'succeeded':
      message.innerText = 'Success! Payment received.';
      break;

    case 'processing':
      message.innerText = "Payment processing. We'll update you when payment is received.";
      break;

    case 'requires_payment_method':
      message.innerText = 'Payment failed. Please try another payment method.';
      // Redirect your user back to your payment page to attempt collecting
      // payment again
      break;

    default:
      message.innerText = 'Something went wrong.';
      break;
  }
});
```

#### React

```jsx
import React, {useState, useEffect} from 'react';
import {useStripe} from '@stripe/react-stripe-js';

const PaymentStatus = () => {
  const stripe = useStripe();
  const [message, setMessage] = useState(null);

  useEffect(() => {
    if (!stripe) {
      return;
    }

    // Retrieve the "payment_intent_client_secret" query parameter appended to
    // your return_url by Stripe.js
    const clientSecret = new URLSearchParams(window.location.search).get(
      'payment_intent_client_secret'
    );

    // Retrieve the PaymentIntent
    stripe
      .retrievePaymentIntent(clientSecret)
      .then(({paymentIntent}) => {
        // Inspect the PaymentIntent `status` to indicate the status of the payment
        // to your customer.
        //
        // Some payment methods will [immediately succeed or fail][0] upon
        // confirmation, while others will first enter a `processing` state.
        //
        // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
        switch (paymentIntent.status) {
          case 'succeeded':
            setMessage('Success! Payment received.');
            break;

          case 'processing':
            setMessage("Payment processing. We'll update you when payment is received.");
            break;

          case 'requires_payment_method':
            // Redirect your user back to your payment page to attempt collecting
            // payment again
            setMessage('Payment failed. Please try another payment method.');
            break;

          default:
            setMessage('Something went wrong.');
            break;
        }
      });
  }, [stripe]);


  return message;
};

export default PaymentStatus;
```

## Redirect and authenticate transactions

Customers can authenticate crypto transactions in the browser. After calling `confirmPayment`, we redirect customers to a page hosted by *crypto.stripe.com* to confirm their payment. When confirmation is complete, we redirect customers to the `return_url`.

## Test your integration

Test your crypto payment integration by opening the payment redirect page using your test API keys. You can test a successful payment flow at no cost using [testnet assets](https://docs.stripe.com/payments/accept-stablecoin-payments.md#testnet-assets).

1. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), create a new transaction using your chosen integration method, and open its redirect URL.
1. Connect your preferred wallet and payment network.
1. Complete the payment, and validate that you’re redirected to the expected URL.

### Test payments with testnet assets 

Most cryptocurrencies offer testnet assets, or tokens that have no monetary value, that you can use to test blockchain transactions. Stripe recommends the MetaMask wallet, Polygon Amoy testnet, and Circle faucet for testing, but you can use your own preferred services.

#### Install a wallet

1. [Download the MetaMask extension](https://metamask.io/download) for your web browser.
1. [Create a new wallet](https://support.metamask.io/start/creating-a-new-wallet/) or [import an existing one](https://support.metamask.io/start/use-an-existing-wallet/).

#### Enable a testnet

1. In your MetaMask wallet, select **Networks** from the main menu.
1. Click **Add custom network**.
1. Enter the following details:
   - **Network name**: `Polygon Amoy`
   - **Default RPC URL**: `https://rpc-amoy.polygon.technology/`
   - **Chain ID**: `80002`
   - **Currency symbol**: `POL`
   - **Block explorer URL**: `https://amoy.polygonscan.com/`
1. Click **Save**.

#### Import a token

1. In your MetaMask wallet, under **Tokens**, select **Polygon Amoy** from the network dropdown.
1. Click the overflow menu (⋯), and select **Import tokens**.
1. Click **Select a network** > **Polygon Amoy**.
1. Under **Token contract address**, paste the Polygon Amoy testnet contract address:
   ```
   0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582
   ```
The **Token symbol** field automatically updates with `USDC` and the **Decimals** field with `6`.
1. Click **Next**.
1. Verify that you’re importing the `USDC` token, and then click **Import**.

Your MetaMask wallet now shows **Polygon Amoy** and **USDC** in the tokens list.

#### Get testnet assets

1. Open [faucet.circle.com](https://faucet.circle.com/)
1. Click **USDC**.
1. Under **Network**, select **Polygon PoS Amoy**.
1. Under **Send to**, paste your wallet address.
1. Click **Send 10 USDC**.

In addition to USDC for making payments, you need POL to pay transaction costs:

1. Open [faucet.polygon.technology](https://faucet.polygon.technology/).
1. Under **Select Chain & Token**, select **Polygon Amoy** and **POL**.
1. Under **Verify your identity**, click the third-party platform you want to authenticate with, and complete the login process.
1. Under **Enter Wallet Address**, paste your wallet address.
1. Click **Claim**.

Testnet transactions can take a few minutes to complete. Check your wallet to confirm that the USDC and POL has transferred.

### More testnet faucets

Check these faucet services for more testing token options:

- [Paxos USDP](https://faucet.paxos.com/)
- [Devnet SOL](https://faucet.solana.com/)
- [Sepolia ETH](https://faucets.chain.link/sepolia)
- [Amoy POL](https://faucet.polygon.technology/)


# Direct API

> This is a Direct API for when platform is web and payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/accept-stablecoin-payments?platform=web&payment-ui=direct-api.

Integrate Pay with Crypto directly through the *Payment Intents API* (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods).

## Set up Stripe [Server-side]

First, [create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).

Use our official libraries to access the Stripe API from your application:

#### Ruby

```bash
# Available as a gem
sudo gem install stripe
```

```ruby
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

#### Python

```bash
# Install through pip
pip3 install --upgrade stripe
```

```bash
# Or find the Stripe package on http://pypi.python.org/pypi/stripe/
```

```python
# Find the version you want to pin:
# https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md
# Specify that version in your requirements.txt file
stripe>=5.0.0
```

#### PHP

```bash
# Install the PHP library with Composer
composer require stripe/stripe-php
```

```bash
# Or download the source directly: https://github.com/stripe/stripe-php/releases
```

#### Java

```java
/*
  For Gradle, add the following dependency to your build.gradle and replace with
  the version number you want to use from:
  - https://mvnrepository.com/artifact/com.stripe/stripe-java or
  - https://github.com/stripe/stripe-java/releases/latest
*/
implementation "com.stripe:stripe-java:30.0.0"
```

```xml
<!--
  For Maven, add the following dependency to your POM and replace with the
  version number you want to use from:
  - https://mvnrepository.com/artifact/com.stripe/stripe-java or
  - https://github.com/stripe/stripe-java/releases/latest
-->
<dependency>
  <groupId>com.stripe</groupId>
  <artifactId>stripe-java</artifactId>
  <version>30.0.0</version>
</dependency>
```

```bash
# For other environments, manually install the following JARs:
# - The Stripe JAR from https://github.com/stripe/stripe-java/releases/latest
# - Google Gson from https://github.com/google/gson
```

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

#### Go

```bash
# Make sure your project is using Go Modules
go mod init
# Install stripe-go
go get -u github.com/stripe/stripe-go/v83
```

```go
// Then import the package
import (
  "github.com/stripe/stripe-go/v83"
)
```

#### .NET

```bash
# Install with dotnet
dotnet add package Stripe.net
dotnet restore
```

```bash
# Or install with NuGet
Install-Package Stripe.net
```

## Create a PaymentIntent and retrieve the client secret [Server-side]

The [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object represents your intent to collect payment from your customer and tracks the lifecycle of the payment process. Create a PaymentIntent on your server and specify the amount to collect and a supported currency. If you have an existing PaymentIntents integration, add `crypto` to the list of [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types).

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=usd \
  -d "payment_method_types[]"=crypto
```

```cli
stripe payment_intents create  \
  --amount=1099 \
  --currency=usd \
  -d "payment_method_types[0]"=crypto
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['crypto'],
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
payment_intent = client.v1.payment_intents.create({
  "amount": 1099,
  "currency": "usd",
  "payment_method_types": ["crypto"],
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->create([
  'amount' => 1099,
  'currency' => 'usd',
  'payment_method_types' => ['crypto'],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentCreateParams params =
  PaymentIntentCreateParams.builder()
    .setAmount(1099L)
    .setCurrency("usd")
    .addPaymentMethodType("crypto")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
PaymentIntent paymentIntent = client.v1().paymentIntents().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['crypto'],
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentCreateParams{
  Amount: stripe.Int64(1099),
  Currency: stripe.String(stripe.CurrencyUSD),
  PaymentMethodTypes: []*string{stripe.String("crypto")},
}
result, err := sc.V1PaymentIntents.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new PaymentIntentCreateOptions
{
    Amount = 1099,
    Currency = "usd",
    PaymentMethodTypes = new List<string> { "crypto" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.Create(options);
```

### Retrieve the client secret

The PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Ruby

```ruby
get '/secret' do
  intent = # ... Create or retrieve the PaymentIntent
  {client_secret: intent.client_secret}.to_json
end
```

#### Python

```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/secret')
def secret():
  intent = # ... Create or retrieve the PaymentIntent
  return jsonify(client_secret=intent.client_secret)
```

#### PHP

```php
<?php
    $intent = # ... Create or retrieve the PaymentIntent
    echo json_encode(array('client_secret' => $intent->client_secret));
?>
```

#### Java

```java
import java.util.HashMap;
import java.util.Map;

import com.stripe.model.PaymentIntent;

import com.google.gson.Gson;

import static spark.Spark.get;

public class StripeJavaQuickStart {
  public static void main(String[] args) {
    Gson gson = new Gson();

    get("/secret", (request, response) -> {
      PaymentIntent intent = // ... Fetch or create the PaymentIntent

      Map<String, String> map = new HashMap();
      map.put("client_secret", intent.getClientSecret());

      return map;
    }, gson::toJson);
  }
}
```

#### Node.js

```javascript
const express = require('express');
const app = express();

app.get('/secret', async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
  res.json({client_secret: intent.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Go

```go
package main

import (
  "encoding/json"
  "net/http"

  stripe "github.com/stripe/stripe-go/v76.0.0"
)

type CheckoutData struct {
  ClientSecret string `json:"client_secret"`
}

func main() {
  http.HandleFunc("/secret", func(w http.ResponseWriter, r *http.Request) {
    intent := // ... Fetch or create the PaymentIntent
    data := CheckoutData{
      ClientSecret: intent.ClientSecret,
    }
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    json.NewEncoder(w).Encode(data)
  })

  http.ListenAndServe(":3000", nil)
}
```

#### .NET

```csharp
using System;
using Microsoft.AspNetCore.Mvc;
using Stripe;

namespace StripeExampleApi.Controllers
{
  [Route("secret")]
  [ApiController]
  public class CheckoutApiController : Controller
  {
    [HttpGet]
    public ActionResult Get()
    {
      var intent = // ... Fetch or create the PaymentIntent
      return Json(new {client_secret = intent.ClientSecret});
    }
  }
}
```

And then fetch the client secret with JavaScript on the client side:

```javascript
(async () => {
  const response = await fetch('/secret');
  const {client_secret: clientSecret} = await response.json();
  // Render the form using the clientSecret
})();
```

#### Server-side rendering

Pass the client secret to the client from your server. This approach works best if your application generates static content on the server before sending it to the browser.

Add the [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) in your checkout form. In your server-side code, retrieve the client secret from the PaymentIntent:

#### Ruby

```erb
<form id="payment-form" data-secret="<%= @intent.client_secret %>">
  <button id="submit">Submit</button>
</form>
```

```ruby
get '/checkout' do
  @intent = # ... Fetch or create the PaymentIntent
  erb :checkout
end
```

#### Python

```html
<form id="payment-form" data-secret="{{ client_secret }}">
  <button id="submit">Submit</button>
</form>
```

```python
@app.route('/checkout')
def checkout():
  intent = # ... Fetch or create the PaymentIntent
  return render_template('checkout.html', client_secret=intent.client_secret)
```

#### PHP

```php
<?php
  $intent = # ... Fetch or create the PaymentIntent;
?>
...
<form id="payment-form" data-secret="<?= $intent->client_secret ?>">
  <button id="submit">Submit</button>
</form>
...
```

#### Java

```html
<form id="payment-form" data-secret="{{ client_secret }}">
  <button id="submit">Submit</button>
</form>
```

```java
import java.util.HashMap;
import java.util.Map;

import com.stripe.model.PaymentIntent;

import spark.ModelAndView;

import static spark.Spark.get;

public class StripeJavaQuickStart {
  public static void main(String[] args) {
    get("/checkout", (request, response) -> {
      PaymentIntent intent = // ... Fetch or create the PaymentIntent

      Map map = new HashMap();
      map.put("client_secret", intent.getClientSecret());

      return new ModelAndView(map, "checkout.hbs");
    }, new HandlebarsTemplateEngine());
  }
}
```

#### Node.js

```html
<form id="payment-form" data-secret="{{ client_secret }}">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>

  <button id="submit">Submit</button>
</form>
```

```javascript
const express = require('express');
const expressHandlebars = require('express-handlebars');
const app = express();

app.engine('.hbs', expressHandlebars({ extname: '.hbs' }));
app.set('view engine', '.hbs');
app.set('views', './views');

app.get('/checkout', async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
  res.render('checkout', { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Go

```html
<form id="payment-form" data-secret="{{ .ClientSecret }}">
  <button id="submit">Submit</button>
</form>
```

```go
package main

import (
  "html/template"
  "net/http"

  stripe "github.com/stripe/stripe-go/v76.0.0"
)

type CheckoutData struct {
  ClientSecret string
}

func main() {
  checkoutTmpl := template.Must(template.ParseFiles("views/checkout.html"))

  http.HandleFunc("/checkout", func(w http.ResponseWriter, r *http.Request) {
    intent := // ... Fetch or create the PaymentIntent
    data := CheckoutData{
      ClientSecret: intent.ClientSecret,
    }
    checkoutTmpl.Execute(w, data)
  })

  http.ListenAndServe(":3000", nil)
}
```

#### .NET

```html
<form id="payment-form" data-secret="@ViewData["ClientSecret"]">
  <button id="submit">Submit</button>
</form>
```

```csharp
using System;
using Microsoft.AspNetCore.Mvc;
using Stripe;

namespace StripeExampleApi.Controllers
{
  [Route("/[controller]")]
  public class CheckoutApiController : Controller
  {
    public IActionResult Index()
    {
      var intent = // ... Fetch or create the PaymentIntent
      ViewData["ClientSecret"] = intent.ClientSecret;
      return View();
    }
  }
}
```

## Redirect to the stablecoin payments page

Use [Stripe.js](https://docs.stripe.com/js.md) to submit the payment to Stripe when a customer chooses **Crypto** as a payment method. Stripe.js is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and lets you extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `<head>` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/clover/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page:

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
```

Use the PaymentIntent [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) and call `stripe.confirmPayment` to handle the Pay with Crypto redirect. Add a `return_url` to determine where Stripe redirects the customer after they complete the payment:

```javascript
const form = document.getElementById('payment-form');

form.addEventListener('submit', async function(event) {
  event.preventDefault();

  // Set the clientSecret of the PaymentIntent
  const { error } = await stripe.confirmPayment({
    clientSecret: clientSecret,
    confirmParams: {
      payment_method_data: {
        type: 'crypto',
      },
      // Return URL where the customer should be redirected after the authorization
      return_url: `${window.location.href}`,
    },
  });

  if (error) {
    // Inform the customer that there was an error.
    const errorElement = document.getElementById('error-message');
    errorElement.textContent = result.error.message;
  }
});
```

The `return_url` corresponds to a page on your website that displays the result of the payment. You can determine what to display by [verifying the status](https://docs.stripe.com/payments/payment-intents/verifying-status.md#checking-status) of the PaymentIntent. To verify the status, the Stripe redirect to the `return_url` includes the following URL query parameters. You can also append your own query parameters to the `return_url`. They persist throughout the redirect process.

| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. |

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom [webhook](https://docs.stripe.com/webhooks.md), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer might close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events can also help you accept more payment methods in the future. To see the differences between all supported payment methods, see our [payment methods](https://stripe.com/payments/payment-methods-guide) guide.

### Receive events and run business actions 

There are a few options for receiving and running business actions:

- **Manually:** Use the [Stripe Dashboard](https://dashboard.stripe.com/test/payments) to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.
- **Custom code:** [Build a webhook](https://docs.stripe.com/payments/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.
- **Prebuilt apps:** Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

### Supported currencies 

You can create crypto payments in the currencies that map to your country. The default local currency for crypto is USD, with customers also seeing their purchase amount in this currency.

## Test your integration 

Test your crypto payment integration by opening the payment redirect page using your test API keys. You can test a successful payment flow at no cost using [testnet assets](https://docs.stripe.com/payments/accept-stablecoin-payments.md#testnet-assets).

1. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), create a new transaction using your chosen integration method, and open its redirect URL.
1. Connect your preferred wallet and payment network.
1. Complete the payment, and validate that you’re redirected to the expected URL.

### Test payments with testnet assets 

Most cryptocurrencies offer testnet assets, or tokens that have no monetary value, that you can use to test blockchain transactions. Stripe recommends the MetaMask wallet, Polygon Amoy testnet, and Circle faucet for testing, but you can use your own preferred services.

#### Install a wallet

1. [Download the MetaMask extension](https://metamask.io/download) for your web browser.
1. [Create a new wallet](https://support.metamask.io/start/creating-a-new-wallet/) or [import an existing one](https://support.metamask.io/start/use-an-existing-wallet/).

#### Enable a testnet

1. In your MetaMask wallet, select **Networks** from the main menu.
1. Click **Add custom network**.
1. Enter the following details:
   - **Network name**: `Polygon Amoy`
   - **Default RPC URL**: `https://rpc-amoy.polygon.technology/`
   - **Chain ID**: `80002`
   - **Currency symbol**: `POL`
   - **Block explorer URL**: `https://amoy.polygonscan.com/`
1. Click **Save**.

#### Import a token

1. In your MetaMask wallet, under **Tokens**, select **Polygon Amoy** from the network dropdown.
1. Click the overflow menu (⋯), and select **Import tokens**.
1. Click **Select a network** > **Polygon Amoy**.
1. Under **Token contract address**, paste the Polygon Amoy testnet contract address:
   ```
   0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582
   ```
The **Token symbol** field automatically updates with `USDC` and the **Decimals** field with `6`.
1. Click **Next**.
1. Verify that you’re importing the `USDC` token, and then click **Import**.

Your MetaMask wallet now shows **Polygon Amoy** and **USDC** in the tokens list.

#### Get testnet assets

1. Open [faucet.circle.com](https://faucet.circle.com/)
1. Click **USDC**.
1. Under **Network**, select **Polygon PoS Amoy**.
1. Under **Send to**, paste your wallet address.
1. Click **Send 10 USDC**.

In addition to USDC for making payments, you need POL to pay transaction costs:

1. Open [faucet.polygon.technology](https://faucet.polygon.technology/).
1. Under **Select Chain & Token**, select **Polygon Amoy** and **POL**.
1. Under **Verify your identity**, click the third-party platform you want to authenticate with, and complete the login process.
1. Under **Enter Wallet Address**, paste your wallet address.
1. Click **Claim**.

Testnet transactions can take a few minutes to complete. Check your wallet to confirm that the USDC and POL has transferred.

### More testnet faucets

Check these faucet services for more testing token options:

- [Paxos USDP](https://faucet.paxos.com/)
- [Devnet SOL](https://faucet.solana.com/)
- [Sepolia ETH](https://faucets.chain.link/sepolia)
- [Amoy POL](https://faucet.polygon.technology/)


# iOS

> This is a iOS for when platform is mobile and payment-ui is ios. View the full page at https://docs.stripe.com/payments/accept-stablecoin-payments?platform=mobile&payment-ui=ios.

We recommend you use the [Mobile Payment Element](https://docs.stripe.com/payments/accept-a-payment.md?=ios), an embeddable payment form, to add Pay with Crypto and other payment methods to your integration with the least amount of effort.

Pay with Crypto is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers are redirected from your app, authorize the payment with Stripe Crypto, then return to your app. You’re [immediately notified](https://docs.stripe.com/payments/payment-methods.md#payment-notification) when the payment succeeds or fails.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side 

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Ruby

```bash
# Available as a gem
sudo gem install stripe
```

```ruby
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

#### Python

```bash
# Install through pip
pip3 install --upgrade stripe
```

```bash
# Or find the Stripe package on http://pypi.python.org/pypi/stripe/
```

```python
# Find the version you want to pin:
# https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md
# Specify that version in your requirements.txt file
stripe>=5.0.0
```

#### PHP

```bash
# Install the PHP library with Composer
composer require stripe/stripe-php
```

```bash
# Or download the source directly: https://github.com/stripe/stripe-php/releases
```

#### Java

```java
/*
  For Gradle, add the following dependency to your build.gradle and replace with
  the version number you want to use from:
  - https://mvnrepository.com/artifact/com.stripe/stripe-java or
  - https://github.com/stripe/stripe-java/releases/latest
*/
implementation "com.stripe:stripe-java:30.0.0"
```

```xml
<!--
  For Maven, add the following dependency to your POM and replace with the
  version number you want to use from:
  - https://mvnrepository.com/artifact/com.stripe/stripe-java or
  - https://github.com/stripe/stripe-java/releases/latest
-->
<dependency>
  <groupId>com.stripe</groupId>
  <artifactId>stripe-java</artifactId>
  <version>30.0.0</version>
</dependency>
```

```bash
# For other environments, manually install the following JARs:
# - The Stripe JAR from https://github.com/stripe/stripe-java/releases/latest
# - Google Gson from https://github.com/google/gson
```

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

#### Go

```bash
# Make sure your project is using Go Modules
go mod init
# Install stripe-go
go get -u github.com/stripe/stripe-go/v83
```

```go
// Then import the package
import (
  "github.com/stripe/stripe-go/v83"
)
```

#### .NET

```bash
# Install with dotnet
dotnet add package Stripe.net
dotnet restore
```

```bash
# Or install with NuGet
Install-Package Stripe.net
```

### Client-side 

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

#### Swift Package Manager

To install the SDK, follow these steps:

1. In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
1. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
1. Add the **StripePaymentsUI** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'StripePaymentsUI'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update StripePaymentsUI
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **StripePaymentsUI.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

#### Swift

```swift
import UIKitimportStripePaymentsUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {StripeAPI.defaultPublishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
        // do any other necessary launch configuration
        return true
    }
}
```

#### Objective-C

```objc
#import "AppDelegate.h"@import StripeCore;

@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {[StripeAPI setDefaultPublishableKey:@"<<YOUR_PUBLISHABLE_KEY>>"];
    // do any other necessary launch configuration
    return YES;
}
@end
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create a PaymentIntent [Server-side] [Client-side]

### Server-side

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

#### Manage payment methods in the Dashboard

You can manage payment methods in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

Create a PaymentIntent on your server with an amount and currency. Before creating the PaymentIntent, make sure to turn **Pay with Crypto** on in your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

> Always decide how much to charge on the server-side, a trusted environment, as opposed to the client. This prevents customers from being able to choose their own prices.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]"=true
```

```cli
stripe payment_intents create  \
  --amount=1099 \
  --currency=usd \
  -d "automatic_payment_methods[enabled]"=true
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.create({
  amount: 1099,
  currency: 'usd',
  automatic_payment_methods: {enabled: true},
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
payment_intent = client.v1.payment_intents.create({
  "amount": 1099,
  "currency": "usd",
  "automatic_payment_methods": {"enabled": True},
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->create([
  'amount' => 1099,
  'currency' => 'usd',
  'automatic_payment_methods' => ['enabled' => true],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentCreateParams params =
  PaymentIntentCreateParams.builder()
    .setAmount(1099L)
    .setCurrency("usd")
    .setAutomaticPaymentMethods(
      PaymentIntentCreateParams.AutomaticPaymentMethods.builder().setEnabled(true).build()
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
PaymentIntent paymentIntent = client.v1().paymentIntents().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  automatic_payment_methods: {
    enabled: true,
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentCreateParams{
  Amount: stripe.Int64(1099),
  Currency: stripe.String(stripe.CurrencyUSD),
  AutomaticPaymentMethods: &stripe.PaymentIntentCreateAutomaticPaymentMethodsParams{
    Enabled: stripe.Bool(true),
  },
}
result, err := sc.V1PaymentIntents.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new PaymentIntentCreateOptions
{
    Amount = 1099,
    Currency = "usd",
    AutomaticPaymentMethods = new PaymentIntentAutomaticPaymentMethodsOptions
    {
        Enabled = true,
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.Create(options);
```

#### List payment methods manually

If you don’t want to use the Dashboard or you want to manually specify payment methods, you can list them using the `payment_method_types` attribute.

Create a PaymentIntent on your server with an amount, currency, and a list of payment methods.

> Always decide how much to charge on the server-side, a trusted environment, as opposed to the client. This prevents customers from being able to choose their own prices.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=usd \
  -d "payment_method_types[]"=crypto
```

```cli
stripe payment_intents create  \
  --amount=1099 \
  --currency=usd \
  -d "payment_method_types[0]"=crypto
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['crypto'],
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
payment_intent = client.v1.payment_intents.create({
  "amount": 1099,
  "currency": "usd",
  "payment_method_types": ["crypto"],
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->create([
  'amount' => 1099,
  'currency' => 'usd',
  'payment_method_types' => ['crypto'],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentCreateParams params =
  PaymentIntentCreateParams.builder()
    .setAmount(1099L)
    .setCurrency("usd")
    .addPaymentMethodType("crypto")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
PaymentIntent paymentIntent = client.v1().paymentIntents().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['crypto'],
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentCreateParams{
  Amount: stripe.Int64(1099),
  Currency: stripe.String(stripe.CurrencyUSD),
  PaymentMethodTypes: []*string{stripe.String("crypto")},
}
result, err := sc.V1PaymentIntents.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new PaymentIntentCreateOptions
{
    Amount = 1099,
    Currency = "usd",
    PaymentMethodTypes = new List<string> { "crypto" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.Create(options);
```

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

#### Swift

```swift
class CheckoutViewController: UIViewController {
    var paymentIntentClientSecret: String?

    // ...continued from previous step

    override func viewDidLoad() {
        // ...continued from previous step
        startCheckout()
    }

    func startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
        // Click View full sample to see a complete implementation
    }
}
```

#### Objective C

```objc
@interface CheckoutViewController ()

// ...continued from previous step
@property (strong) NSString *paymentIntentClientSecret;

@end

@implementation CheckoutViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // ...continued from previous step
    [self startCheckout];
}

- (void)startCheckout {
    // Request a PaymentIntent from your server and store its client secret
    // Click View full sample to see a complete implementation
}

@end
```

## Submit the payment to Stripe [Client-side]

When a customer taps to pay with Pay with Crypto, confirm the `PaymentIntent` to complete the payment. Configure an `STPPaymentIntentParams` object with the `PaymentIntent` [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret).

The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Set up a return URL

The iOS SDK presents a webview in your app to complete the Pay with Crypto payment. When authentication is finished, the webview can automatically dismiss itself instead of having your customer close it. To enable this behavior, configure a custom URL scheme or universal link and set up your app delegate to forward the URL to the SDK.

#### Swift

```swift
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
    let stripeHandled = StripeAPI.handleURLCallback(with: url)
    if (stripeHandled) {
        return true
    } else {
        // This was not a Stripe url – handle the URL normally as you would
    }
    return false
}

// This method handles opening universal link URLs (for example, "https://example.com/stripe_ios_callback")
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    if userActivity.activityType == NSUserActivityTypeBrowsingWeb {
        if let url = userActivity.webpageURL {
            let stripeHandled = StripeAPI.handleURLCallback(with: url)
            if (stripeHandled) {
                return true
            } else {
                // This was not a Stripe url – handle the URL normally as you would
            }
        }
    }
    return false
}
```

#### Objective C

```objc
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
    BOOL stripeHandled = [StripeAPI handleStripeURLCallbackWithURL:url];
    if (stripeHandled) {
        return YES;
    } else {
        // This was not a Stripe url – handle the URL normally as you would
    }
    return NO;
}

// This method handles opening universal link URLs (for example, "https://example.com/stripe_ios_callback")
- (BOOL)application:(UIApplication *)application continueUserActivity:(NSUserActivity *)userActivity restorationHandler:(void (^)(NSArray<id<UIUserActivityRestoring>> * _Nullable))restorationHandler {
    if (userActivity.activityType == NSUserActivityTypeBrowsingWeb) {
        if (userActivity.webpageURL) {
            BOOL stripeHandled = [StripeAPI handleStripeURLCallbackWithURL:userActivity.webpageURL];
            if (stripeHandled) {
                return YES;
            } else {
                // This was not a Stripe url – handle the URL normally as you would
            }
            return NO;
        }
    }
    return NO;
}
```

Pass the URL as the `return_url` when you confirm the PaymentIntent. After webview-based authentication finishes, Stripe redirects the user to the `return_url`.

### Confirm the Pay with Crypto payment

Complete the payment by calling `STPPaymentHandler.confirmPayment`. This presents a webview where the customer can complete the payment with Pay with Crypto. After completion, Stripe calls the completion block with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)

// Pay with Crypto does not require additional parameters so we only need to pass the initialized
// STPPaymentMethodCryptoParams instance to STPPaymentMethodParams
let crypto = STPPaymentMethodCryptoParams()
let paymentMethodParams = STPPaymentMethodParams(crypto: crypto, billingDetails: nil, metadata: nil)

paymentIntentParams.paymentMethodParams = paymentMethodParams
paymentIntentParams.returnURL = "payments-example://stripe-redirect"

STPPaymentHandler.shared().confirmPayment(paymentIntentParams,
                                          with: self)
{ (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Payment succeeded
        // ...

    case .canceled:
        // Payment canceled
        // ...

    case .failed:
        // Payment failed
        // ...

    @unknown default:
        fatalError()
    }
}
```

#### Objective C

```objc
STPPaymentIntentParams *paymentIntentParams = [[STPPaymentIntentParams alloc] initWithClientSecret:clientSecret];

STPPaymentMethodCryptoParams *crypto = [[STPPaymentMethodCryptoParams alloc] init];

// Pay with Crypto does not require additional parameters so we only need to pass the initialized
// STPPaymentMethodCryptoParams instance to STPPaymentMethodParams
paymentIntentParams.paymentMethodParams = [STPPaymentMethodParams paramsWithCrypto:crypto billingDetails:nil metadata:nil];
paymentIntentParams.returnURL = @"payments-example://stripe-redirect";

[[STPPaymentHandler sharedHandler] confirmPayment:paymentIntentParams withAuthenticationContext:self.delegate completion:^(STPPaymentHandlerActionStatus handlerStatus,    STPPaymentIntent * handledIntent, NSError * _Nullable handlerError) {
    switch (handlerStatus) {
        case STPPaymentHandlerActionStatusFailed:
            // Payment failed
            // ...
            break;
        case STPPaymentHandlerActionStatusCanceled:
            // Payment canceled
            // ...
            break;
        case STPPaymentHandlerActionStatusSucceeded:
            // Payment succeeded
            // ...
            break;
    }
}];

```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/payments/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.


# Android

> This is a Android for when platform is mobile and payment-ui is android. View the full page at https://docs.stripe.com/payments/accept-stablecoin-payments?platform=mobile&payment-ui=android.

We recommend you use the [Mobile Payment Element](https://docs.stripe.com/payments/accept-a-payment.md?platform=android), an embeddable payment form, to add Pay with Crypto and other payment methods to your integration with the least amount of effort.

Pay with Crypto is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers are redirected from your app, authorize the payment with Stripe, then return to your app. You’re [immediately notified](https://docs.stripe.com/payments/payment-methods.md#payment-notification) when the payment succeeds or fails.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side 

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Ruby

```bash
# Available as a gem
sudo gem install stripe
```

```ruby
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

#### Python

```bash
# Install through pip
pip3 install --upgrade stripe
```

```bash
# Or find the Stripe package on http://pypi.python.org/pypi/stripe/
```

```python
# Find the version you want to pin:
# https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md
# Specify that version in your requirements.txt file
stripe>=5.0.0
```

#### PHP

```bash
# Install the PHP library with Composer
composer require stripe/stripe-php
```

```bash
# Or download the source directly: https://github.com/stripe/stripe-php/releases
```

#### Java

```java
/*
  For Gradle, add the following dependency to your build.gradle and replace with
  the version number you want to use from:
  - https://mvnrepository.com/artifact/com.stripe/stripe-java or
  - https://github.com/stripe/stripe-java/releases/latest
*/
implementation "com.stripe:stripe-java:30.0.0"
```

```xml
<!--
  For Maven, add the following dependency to your POM and replace with the
  version number you want to use from:
  - https://mvnrepository.com/artifact/com.stripe/stripe-java or
  - https://github.com/stripe/stripe-java/releases/latest
-->
<dependency>
  <groupId>com.stripe</groupId>
  <artifactId>stripe-java</artifactId>
  <version>30.0.0</version>
</dependency>
```

```bash
# For other environments, manually install the following JARs:
# - The Stripe JAR from https://github.com/stripe/stripe-java/releases/latest
# - Google Gson from https://github.com/google/gson
```

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

#### Go

```bash
# Make sure your project is using Go Modules
go mod init
# Install stripe-go
go get -u github.com/stripe/stripe-go/v83
```

```go
// Then import the package
import (
  "github.com/stripe/stripe-go/v83"
)
```

#### .NET

```bash
# Install with dotnet
dotnet add package Stripe.net
dotnet restore
```

```bash
# Or install with NuGet
Install-Package Stripe.net
```

### Client-side 

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `stripe-android` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

#### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
  // ...

  // Stripe Android SDK
  implementation("com.stripe:stripe-android:22.2.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:22.2.0")
}
```

#### Groovy

```groovy
apply plugin: 'com.android.application'

android { ... }

dependencies {
  // ...

  // Stripe Android SDK
  implementation 'com.stripe:stripe-android:22.2.0'
  // Include the financial connections SDK to support US bank account as a payment method
  implementation 'com.stripe:financial-connections:22.2.0'
}
```

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-android/releases) page on GitHub. To receive notifications when a new release is published, [watch releases for the repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/apikeys) so that it can make requests to the Stripe API, such as in your `Application` subclass:

#### Kotlin

```kotlin
import com.stripe.android.PaymentConfiguration

class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        PaymentConfiguration.init(
            applicationContext,
            "<<YOUR_PUBLISHABLE_KEY>>"
        )
    }
}
```

#### Java

```java
import com.stripe.android.PaymentConfiguration;

public class MyApp extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        PaymentConfiguration.init(
            getApplicationContext(),
            "<<YOUR_PUBLISHABLE_KEY>>"
        );
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

Stripe samples also use [OkHttp](https://github.com/square/okhttp) and [GSON](https://github.com/google/gson) to make HTTP requests to a server.

## Create a PaymentIntent [Server-side] [Client-side]

### Server-side

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

#### Manage payment methods in the Dashboard

You can manage payment methods in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors, such as the transaction’s amount, currency, and payment flow.

Create a PaymentIntent on your server with an amount and currency. Before creating the PaymentIntent, make sure to turn **Pay with Crypto** on in the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) page.

> Always decide how much to charge on the server-side, a trusted environment, as opposed to the client. This prevents customers from being able to choose their own prices.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]"=true
```

```cli
stripe payment_intents create  \
  --amount=1099 \
  --currency=usd \
  -d "automatic_payment_methods[enabled]"=true
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.create({
  amount: 1099,
  currency: 'usd',
  automatic_payment_methods: {enabled: true},
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
payment_intent = client.v1.payment_intents.create({
  "amount": 1099,
  "currency": "usd",
  "automatic_payment_methods": {"enabled": True},
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->create([
  'amount' => 1099,
  'currency' => 'usd',
  'automatic_payment_methods' => ['enabled' => true],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentCreateParams params =
  PaymentIntentCreateParams.builder()
    .setAmount(1099L)
    .setCurrency("usd")
    .setAutomaticPaymentMethods(
      PaymentIntentCreateParams.AutomaticPaymentMethods.builder().setEnabled(true).build()
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
PaymentIntent paymentIntent = client.v1().paymentIntents().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  automatic_payment_methods: {
    enabled: true,
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentCreateParams{
  Amount: stripe.Int64(1099),
  Currency: stripe.String(stripe.CurrencyUSD),
  AutomaticPaymentMethods: &stripe.PaymentIntentCreateAutomaticPaymentMethodsParams{
    Enabled: stripe.Bool(true),
  },
}
result, err := sc.V1PaymentIntents.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new PaymentIntentCreateOptions
{
    Amount = 1099,
    Currency = "usd",
    AutomaticPaymentMethods = new PaymentIntentAutomaticPaymentMethodsOptions
    {
        Enabled = true,
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.Create(options);
```

#### List payment methods manually

If you don’t want to use the Dashboard or you want to manually specify payment methods, you can list them using the `payment_method_types` attribute.

Create a PaymentIntent on your server with an amount, currency, and a list of payment methods.

> Always decide how much to charge on the server-side, a trusted environment, as opposed to the client. This prevents customers from being able to choose their own prices.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=usd \
  -d "payment_method_types[]"=crypto
```

```cli
stripe payment_intents create  \
  --amount=1099 \
  --currency=usd \
  -d "payment_method_types[0]"=crypto
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['crypto'],
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
payment_intent = client.v1.payment_intents.create({
  "amount": 1099,
  "currency": "usd",
  "payment_method_types": ["crypto"],
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->create([
  'amount' => 1099,
  'currency' => 'usd',
  'payment_method_types' => ['crypto'],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentCreateParams params =
  PaymentIntentCreateParams.builder()
    .setAmount(1099L)
    .setCurrency("usd")
    .addPaymentMethodType("crypto")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
PaymentIntent paymentIntent = client.v1().paymentIntents().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['crypto'],
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentCreateParams{
  Amount: stripe.Int64(1099),
  Currency: stripe.String(stripe.CurrencyUSD),
  PaymentMethodTypes: []*string{stripe.String("crypto")},
}
result, err := sc.V1PaymentIntents.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new PaymentIntentCreateOptions
{
    Amount = 1099,
    Currency = "usd",
    PaymentMethodTypes = new List<string> { "crypto" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.Create(options);
```

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {

  private lateinit var paymentIntentClientSecret: String

  override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      // ...
      startCheckout()
  }

  private fun startCheckout() {
      // Request a PaymentIntent from your server and store its client secret in paymentIntentClientSecret
      // Click View full sample to see a complete implementation
  }
}
```

#### Java

```java
public class CheckoutActivity extends AppCompatActivity {

    private String paymentIntentClientSecret;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        // ...
        startCheckout();
    }

    private void startCheckout() {
        // Request a PaymentIntent from your server and store its client secret in paymentIntentClientSecret
        // Click View full sample to see a complete implementation
    }
}
```

## Submit the payment to Stripe [Client-side]

When a customer taps to pay with Pay with Crypto, confirm the `PaymentIntent` to complete the payment. Configure a `ConfirmPaymentIntentParams` object with the `PaymentIntent` [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret).

The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Confirm Pay with Crypto payment

Complete the payment by calling [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/confirm.html). This redirects the customer to *https://crypto.stripe.com/pay*, where they can complete the payment with Pay with Crypto. After completion, Stripe calls the `PaymentResultCallback` you set with the result of the payment.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {

    // ...

    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(applicationContext)
        PaymentLauncher.create(
            activity = this,
            publishableKey = paymentConfiguration.publishableKey,
            stripeAccountId = paymentConfiguration.stripeAccountId,
            callback = ::onPaymentResult,
        )
    }

    // …

    private fun startCheckout() {
        // ...

        val cryptoParams = PaymentMethodCreateParams.createCrypto()

        val confirmParams = ConfirmPaymentIntentParams
            .createWithPaymentMethodCreateParams(
                paymentMethodCreateParams = cryptoParams,
                clientSecret = paymentIntentClientSecret,
            )

        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        // Handle the payment result…
    }
}
```

#### Java

```java
public class CheckoutActivity extends AppCompatActivity {

    // ...
    private PaymentLauncher paymentLauncher;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        // ...
        final PaymentConfiguration paymentConfiguration = PaymentConfiguration.getInstance(context);

        paymentLauncher = PaymentLauncher.create(
            this,
            paymentConfiguration.getPublishableKey(),
            paymentConfiguration.getStripeAccountId(),
            this::onPaymentResult
        );
    }

    private void startCheckout() {
        // ...

        PaymentMethodCreateParams cryptoParams = PaymentMethodCreateParams.createCrypto();

        ConfirmPaymentIntentParams createParams = ConfirmPaymentIntentParams
            .createWithPaymentMethodCreateParams(
                cryptoParams,
                paymentIntentClientSecret
            );

        paymentLauncher.confirm(confirmParams);
    }

    // ...

    private void onPaymentResult(PaymentResult paymentResult) {
        // Handle the payment result…
    }
}
```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/payments/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

### Test your integration 

Test your crypto payment integration by opening the payment redirect page using your test API keys. You can test a successful payment flow at no cost using [testnet assets](https://docs.stripe.com/payments/accept-stablecoin-payments.md#testnet-assets).

1. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), create a new transaction using your chosen integration method, and open its redirect URL.
1. Connect your preferred wallet and payment network.
1. Complete the payment, and validate that you’re redirected to the expected URL.

### Test payments with testnet assets 

Most cryptocurrencies offer testnet assets, or tokens that have no monetary value, that you can use to test blockchain transactions. Stripe recommends the MetaMask wallet, Polygon Amoy testnet, and Circle faucet for testing, but you can use your own preferred services.

#### Install a wallet

1. [Download the MetaMask extension](https://metamask.io/download) for your web browser.
1. [Create a new wallet](https://support.metamask.io/start/creating-a-new-wallet/) or [import an existing one](https://support.metamask.io/start/use-an-existing-wallet/).

#### Enable a testnet

1. In your MetaMask wallet, select **Networks** from the main menu.
1. Click **Add custom network**.
1. Enter the following details:
   - **Network name**: `Polygon Amoy`
   - **Default RPC URL**: `https://rpc-amoy.polygon.technology/`
   - **Chain ID**: `80002`
   - **Currency symbol**: `POL`
   - **Block explorer URL**: `https://amoy.polygonscan.com/`
1. Click **Save**.

#### Import a token

1. In your MetaMask wallet, under **Tokens**, select **Polygon Amoy** from the network dropdown.
1. Click the overflow menu (⋯), and select **Import tokens**.
1. Click **Select a network** > **Polygon Amoy**.
1. Under **Token contract address**, paste the Polygon Amoy testnet contract address:
   ```
   0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582
   ```
The **Token symbol** field automatically updates with `USDC` and the **Decimals** field with `6`.
1. Click **Next**.
1. Verify that you’re importing the `USDC` token, and then click **Import**.

Your MetaMask wallet now shows **Polygon Amoy** and **USDC** in the tokens list.

#### Get testnet assets

1. Open [faucet.circle.com](https://faucet.circle.com/)
1. Click **USDC**.
1. Under **Network**, select **Polygon PoS Amoy**.
1. Under **Send to**, paste your wallet address.
1. Click **Send 10 USDC**.

In addition to USDC for making payments, you need POL to pay transaction costs:

1. Open [faucet.polygon.technology](https://faucet.polygon.technology/).
1. Under **Select Chain & Token**, select **Polygon Amoy** and **POL**.
1. Under **Verify your identity**, click the third-party platform you want to authenticate with, and complete the login process.
1. Under **Enter Wallet Address**, paste your wallet address.
1. Click **Claim**.

Testnet transactions can take a few minutes to complete. Check your wallet to confirm that the USDC and POL has transferred.

### More testnet faucets

Check these faucet services for more testing token options:

- [Paxos USDP](https://faucet.paxos.com/)
- [Devnet SOL](https://faucet.solana.com/)
- [Sepolia ETH](https://faucets.chain.link/sepolia)
- [Amoy POL](https://faucet.polygon.technology/)

