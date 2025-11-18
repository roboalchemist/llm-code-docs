# Source: https://docs.stripe.com/financial-connections/ownership.md

# Access ownership details for a Financial Connections account

Learn how to access an account's ownership details with your user's permission.

The Financial Connections API allows you to retrieve the ownership details of a [Financial Connections account](https://docs.stripe.com/api/financial_connections/accounts/object.md). Ownership data is useful for a variety of applications, including reducing the risk of fraud when onboarding users or underwriting.

## Before you begin

You must have a completed Financial Connections registration to access ownership in live mode. Visit your [Dashboard settings](https://dashboard.stripe.com/settings/financial-connections) to check the state of your registration or begin the registration process. Financial Connections test data is always available.

## Create a customer [Recommended] [Server-side]

We recommend that you create a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) with an email address to represent your user, that you then attach to your payment. Attaching a `Customer` object allows you to [list previously linked accounts ](https://docs.stripe.com/api/financial_connections/accounts/list.md) later. By providing an email address on the `Customer` object, Financial Connections can improve the authentication flow by simplifying sign-in or sign-up for your user, depending on whether they’re a returning [Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses) user.

```curl
curl https://api.stripe.com/v1/customers \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d email={{CUSTOMER_EMAIL}}
```

```cli
stripe customers create  \
  --email={{CUSTOMER_EMAIL}}
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer = client.v1.customers.create({email: '{{CUSTOMER_EMAIL}}'})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
customer = client.v1.customers.create({"email": "{{CUSTOMER_EMAIL}}"})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customer = $stripe->customers->create(['email' => '{{CUSTOMER_EMAIL}}']);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerCreateParams params =
  CustomerCreateParams.builder().setEmail("{{CUSTOMER_EMAIL}}").build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Customer customer = client.v1().customers().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  email: '{{CUSTOMER_EMAIL}}',
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerCreateParams{Email: stripe.String("{{CUSTOMER_EMAIL}}")}
result, err := sc.V1Customers.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new CustomerCreateOptions { Email = "{{CUSTOMER_EMAIL}}" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers;
Customer customer = service.Create(options);
```

## Request access to an account's ownership data [Server-side]

You must collect an account before you can access its ownership data. To learn more about how to collect Financial Connections Accounts, read the integration guide most relevant to your use case (for example, [accept payments](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md), [facilitate Connect payouts](https://docs.stripe.com/financial-connections/connect-payouts.md), or [build other-data powered products](https://docs.stripe.com/financial-connections/other-data-powered-products.md)).

If you use [Connect Onboarding for Custom Accounts](https://docs.stripe.com/connect/payouts-bank-accounts.md?bank-account-collection-integration=prebuilt-web-form) to collect Financial Connections Accounts, configure which data you want access to in the [Dashboard](https://dashboard.stripe.com/settings/connect/custom).

If you use an API integration to collect accounts, specify the data you need access to with the [permissions](https://docs.stripe.com/financial-connections/fundamentals.md#data-permissions) parameter. The set of requested data permissions are viewable by the user in the [authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow). Financial Connections Accounts are collectible through various integration paths, and how you specify the parameter varies slightly by API.

#### Setup Intents

```curl
curl https://api.stripe.com/v1/setup_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer="{{CUSTOMER_ID}}" \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method
```

```cli
stripe setup_intents create  \
  --customer="{{CUSTOMER_ID}}" \
  -d "payment_method_types[0]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][0]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][1]"=payment_method
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {permissions: ['ownership', 'payment_method']},
    },
  },
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
setup_intent = client.v1.setup_intents.create({
  "customer": "{{CUSTOMER_ID}}",
  "payment_method_types": ["us_bank_account"],
  "payment_method_options": {
    "us_bank_account": {
      "financial_connections": {"permissions": ["ownership", "payment_method"]},
    },
  },
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$setupIntent = $stripe->setupIntents->create([
  'customer' => '{{CUSTOMER_ID}}',
  'payment_method_types' => ['us_bank_account'],
  'payment_method_options' => [
    'us_bank_account' => [
      'financial_connections' => ['permissions' => ['ownership', 'payment_method']],
    ],
  ],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SetupIntentCreateParams params =
  SetupIntentCreateParams.builder()
    .setCustomer("{{CUSTOMER_ID}}")
    .addPaymentMethodType("us_bank_account")
    .setPaymentMethodOptions(
      SetupIntentCreateParams.PaymentMethodOptions.builder()
        .setUsBankAccount(
          SetupIntentCreateParams.PaymentMethodOptions.UsBankAccount.builder()
            .setFinancialConnections(
              SetupIntentCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.builder()
                .addPermission(
                  SetupIntentCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.OWNERSHIP
                )
                .addPermission(
                  SetupIntentCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.PAYMENT_METHOD
                )
                .build()
            )
            .build()
        )
        .build()
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
SetupIntent setupIntent = client.v1().setupIntents().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        permissions: ['ownership', 'payment_method'],
      },
    },
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SetupIntentCreateParams{
  Customer: stripe.String("{{CUSTOMER_ID}}"),
  PaymentMethodTypes: []*string{stripe.String("us_bank_account")},
  PaymentMethodOptions: &stripe.SetupIntentCreatePaymentMethodOptionsParams{
    USBankAccount: &stripe.SetupIntentCreatePaymentMethodOptionsUSBankAccountParams{
      FinancialConnections: &stripe.SetupIntentCreatePaymentMethodOptionsUSBankAccountFinancialConnectionsParams{
        Permissions: []*string{
          stripe.String(stripe.SetupIntentPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionOwnership),
          stripe.String(stripe.SetupIntentPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionPaymentMethod),
        },
      },
    },
  },
}
result, err := sc.V1SetupIntents.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new SetupIntentCreateOptions
{
    Customer = "{{CUSTOMER_ID}}",
    PaymentMethodTypes = new List<string> { "us_bank_account" },
    PaymentMethodOptions = new SetupIntentPaymentMethodOptionsOptions
    {
        UsBankAccount = new SetupIntentPaymentMethodOptionsUsBankAccountOptions
        {
            FinancialConnections = new SetupIntentPaymentMethodOptionsUsBankAccountFinancialConnectionsOptions
            {
                Permissions = new List<string> { "ownership", "payment_method" },
            },
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SetupIntents;
SetupIntent setupIntent = service.Create(options);
```

#### Payment Intents

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=20000 \
  -d currency=usd \
  -d customer="{{CUSTOMER_ID}}" \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method
```

```cli
stripe payment_intents create  \
  --amount=20000 \
  --currency=usd \
  --customer="{{CUSTOMER_ID}}" \
  -d "payment_method_types[0]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][0]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][1]"=payment_method
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.create({
  amount: 20000,
  currency: 'usd',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {permissions: ['ownership', 'payment_method']},
    },
  },
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
payment_intent = client.v1.payment_intents.create({
  "amount": 20000,
  "currency": "usd",
  "customer": "{{CUSTOMER_ID}}",
  "payment_method_types": ["us_bank_account"],
  "payment_method_options": {
    "us_bank_account": {
      "financial_connections": {"permissions": ["ownership", "payment_method"]},
    },
  },
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->create([
  'amount' => 20000,
  'currency' => 'usd',
  'customer' => '{{CUSTOMER_ID}}',
  'payment_method_types' => ['us_bank_account'],
  'payment_method_options' => [
    'us_bank_account' => [
      'financial_connections' => ['permissions' => ['ownership', 'payment_method']],
    ],
  ],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentCreateParams params =
  PaymentIntentCreateParams.builder()
    .setAmount(20000L)
    .setCurrency("usd")
    .setCustomer("{{CUSTOMER_ID}}")
    .addPaymentMethodType("us_bank_account")
    .setPaymentMethodOptions(
      PaymentIntentCreateParams.PaymentMethodOptions.builder()
        .setUsBankAccount(
          PaymentIntentCreateParams.PaymentMethodOptions.UsBankAccount.builder()
            .setFinancialConnections(
              PaymentIntentCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.builder()
                .addPermission(
                  PaymentIntentCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.OWNERSHIP
                )
                .addPermission(
                  PaymentIntentCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.PAYMENT_METHOD
                )
                .build()
            )
            .build()
        )
        .build()
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
  amount: 20000,
  currency: 'usd',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        permissions: ['ownership', 'payment_method'],
      },
    },
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentCreateParams{
  Amount: stripe.Int64(20000),
  Currency: stripe.String(stripe.CurrencyUSD),
  Customer: stripe.String("{{CUSTOMER_ID}}"),
  PaymentMethodTypes: []*string{stripe.String("us_bank_account")},
  PaymentMethodOptions: &stripe.PaymentIntentCreatePaymentMethodOptionsParams{
    USBankAccount: &stripe.PaymentIntentCreatePaymentMethodOptionsUSBankAccountParams{
      FinancialConnections: &stripe.PaymentIntentCreatePaymentMethodOptionsUSBankAccountFinancialConnectionsParams{
        Permissions: []*string{
          stripe.String(stripe.PaymentIntentPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionOwnership),
          stripe.String(stripe.PaymentIntentPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionPaymentMethod),
        },
      },
    },
  },
}
result, err := sc.V1PaymentIntents.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new PaymentIntentCreateOptions
{
    Amount = 20000,
    Currency = "usd",
    Customer = "{{CUSTOMER_ID}}",
    PaymentMethodTypes = new List<string> { "us_bank_account" },
    PaymentMethodOptions = new PaymentIntentPaymentMethodOptionsOptions
    {
        UsBankAccount = new PaymentIntentPaymentMethodOptionsUsBankAccountOptions
        {
            FinancialConnections = new PaymentIntentPaymentMethodOptionsUsBankAccountFinancialConnectionsOptions
            {
                Permissions = new List<string> { "ownership", "payment_method" },
            },
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.Create(options);
```

#### Sessions

```curl
curl https://api.stripe.com/v1/financial_connections/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "account_holder[type]"=customer \
  -d "account_holder[customer]"="{{CUSTOMER_ID}}" \
  -d "permissions[]"=ownership
```

```cli
stripe financial_connections sessions create  \
  -d "account_holder[type]"=customer \
  -d "account_holder[customer]"="{{CUSTOMER_ID}}" \
  -d "permissions[0]"=ownership
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

session = client.v1.financial_connections.sessions.create({
  account_holder: {
    type: 'customer',
    customer: '{{CUSTOMER_ID}}',
  },
  permissions: ['ownership'],
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
session = client.v1.financial_connections.sessions.create({
  "account_holder": {"type": "customer", "customer": "{{CUSTOMER_ID}}"},
  "permissions": ["ownership"],
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$session = $stripe->financialConnections->sessions->create([
  'account_holder' => [
    'type' => 'customer',
    'customer' => '{{CUSTOMER_ID}}',
  ],
  'permissions' => ['ownership'],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SessionCreateParams params =
  SessionCreateParams.builder()
    .setAccountHolder(
      SessionCreateParams.AccountHolder.builder()
        .setType(SessionCreateParams.AccountHolder.Type.CUSTOMER)
        .setCustomer("{{CUSTOMER_ID}}")
        .build()
    )
    .addPermission(SessionCreateParams.Permission.OWNERSHIP)
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Session session = client.v1().financialConnections().sessions().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.financialConnections.sessions.create({
  account_holder: {
    type: 'customer',
    customer: '{{CUSTOMER_ID}}',
  },
  permissions: ['ownership'],
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.FinancialConnectionsSessionCreateParams{
  AccountHolder: &stripe.FinancialConnectionsSessionCreateAccountHolderParams{
    Type: stripe.String(stripe.FinancialConnectionsSessionAccountHolderTypeCustomer),
    Customer: stripe.String("{{CUSTOMER_ID}}"),
  },
  Permissions: []*string{
    stripe.String(stripe.FinancialConnectionsSessionPermissionOwnership),
  },
}
result, err := sc.V1FinancialConnectionsSessions.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new Stripe.FinancialConnections.SessionCreateOptions
{
    AccountHolder = new Stripe.FinancialConnections.SessionAccountHolderOptions
    {
        Type = "customer",
        Customer = "{{CUSTOMER_ID}}",
    },
    Permissions = new List<string> { "ownership" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.FinancialConnections.Sessions;
Stripe.FinancialConnections.Session session = service.Create(options);
```

#### Checkout

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer="{{CUSTOMER_ID}}" \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method
```

```cli
stripe checkout sessions create  \
  --customer="{{CUSTOMER_ID}}" \
  -d "payment_method_types[0]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][0]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][1]"=payment_method
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

session = client.v1.checkout.sessions.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {permissions: ['ownership', 'payment_method']},
    },
  },
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
session = client.v1.checkout.sessions.create({
  "customer": "{{CUSTOMER_ID}}",
  "payment_method_types": ["us_bank_account"],
  "payment_method_options": {
    "us_bank_account": {
      "financial_connections": {"permissions": ["ownership", "payment_method"]},
    },
  },
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$session = $stripe->checkout->sessions->create([
  'customer' => '{{CUSTOMER_ID}}',
  'payment_method_types' => ['us_bank_account'],
  'payment_method_options' => [
    'us_bank_account' => [
      'financial_connections' => ['permissions' => ['ownership', 'payment_method']],
    ],
  ],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SessionCreateParams params =
  SessionCreateParams.builder()
    .setCustomer("{{CUSTOMER_ID}}")
    .addPaymentMethodType(SessionCreateParams.PaymentMethodType.US_BANK_ACCOUNT)
    .setPaymentMethodOptions(
      SessionCreateParams.PaymentMethodOptions.builder()
        .setUsBankAccount(
          SessionCreateParams.PaymentMethodOptions.UsBankAccount.builder()
            .setFinancialConnections(
              SessionCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.builder()
                .addPermission(
                  SessionCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.OWNERSHIP
                )
                .addPermission(
                  SessionCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.PAYMENT_METHOD
                )
                .build()
            )
            .build()
        )
        .build()
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Session session = client.v1().checkout().sessions().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        permissions: ['ownership', 'payment_method'],
      },
    },
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CheckoutSessionCreateParams{
  Customer: stripe.String("{{CUSTOMER_ID}}"),
  PaymentMethodTypes: []*string{stripe.String("us_bank_account")},
  PaymentMethodOptions: &stripe.CheckoutSessionCreatePaymentMethodOptionsParams{
    USBankAccount: &stripe.CheckoutSessionCreatePaymentMethodOptionsUSBankAccountParams{
      FinancialConnections: &stripe.CheckoutSessionCreatePaymentMethodOptionsUSBankAccountFinancialConnectionsParams{
        Permissions: []*string{
          stripe.String(stripe.CheckoutSessionPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionOwnership),
          stripe.String(stripe.CheckoutSessionPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionPaymentMethod),
        },
      },
    },
  },
}
result, err := sc.V1CheckoutSessions.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new Stripe.Checkout.SessionCreateOptions
{
    Customer = "{{CUSTOMER_ID}}",
    PaymentMethodTypes = new List<string> { "us_bank_account" },
    PaymentMethodOptions = new Stripe.Checkout.SessionPaymentMethodOptionsOptions
    {
        UsBankAccount = new Stripe.Checkout.SessionPaymentMethodOptionsUsBankAccountOptions
        {
            FinancialConnections = new Stripe.Checkout.SessionPaymentMethodOptionsUsBankAccountFinancialConnectionsOptions
            {
                Permissions = new List<string> { "ownership", "payment_method" },
            },
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Checkout.Sessions;
Stripe.Checkout.Session session = service.Create(options);
```

#### Invoices

```curl
curl https://api.stripe.com/v1/invoices \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer="{{CUSTOMER_ID}}" \
  -d "payment_settings[payment_method_types][]"=us_bank_account \
  -d "payment_settings[payment_method_options][us_bank_account][financial_connections][permissions][]"=ownership \
  -d "payment_settings[payment_method_options][us_bank_account][financial_connections][permissions][]"=payment_method
```

```cli
stripe invoices create  \
  --customer="{{CUSTOMER_ID}}" \
  -d "payment_settings[payment_method_types][0]"=us_bank_account \
  -d "payment_settings[payment_method_options][us_bank_account][financial_connections][permissions][0]"=ownership \
  -d "payment_settings[payment_method_options][us_bank_account][financial_connections][permissions][1]"=payment_method
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice = client.v1.invoices.create({
  customer: '{{CUSTOMER_ID}}',
  payment_settings: {
    payment_method_types: ['us_bank_account'],
    payment_method_options: {
      us_bank_account: {
        financial_connections: {permissions: ['ownership', 'payment_method']},
      },
    },
  },
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
invoice = client.v1.invoices.create({
  "customer": "{{CUSTOMER_ID}}",
  "payment_settings": {
    "payment_method_types": ["us_bank_account"],
    "payment_method_options": {
      "us_bank_account": {
        "financial_connections": {"permissions": ["ownership", "payment_method"]},
      },
    },
  },
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoice = $stripe->invoices->create([
  'customer' => '{{CUSTOMER_ID}}',
  'payment_settings' => [
    'payment_method_types' => ['us_bank_account'],
    'payment_method_options' => [
      'us_bank_account' => [
        'financial_connections' => ['permissions' => ['ownership', 'payment_method']],
      ],
    ],
  ],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceCreateParams params =
  InvoiceCreateParams.builder()
    .setCustomer("{{CUSTOMER_ID}}")
    .setPaymentSettings(
      InvoiceCreateParams.PaymentSettings.builder()
        .addPaymentMethodType(
          InvoiceCreateParams.PaymentSettings.PaymentMethodType.US_BANK_ACCOUNT
        )
        .setPaymentMethodOptions(
          InvoiceCreateParams.PaymentSettings.PaymentMethodOptions.builder()
            .setUsBankAccount(
              InvoiceCreateParams.PaymentSettings.PaymentMethodOptions.UsBankAccount.builder()
                .setFinancialConnections(
                  InvoiceCreateParams.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.builder()
                    .addPermission(
                      InvoiceCreateParams.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.OWNERSHIP
                    )
                    .addPermission(
                      InvoiceCreateParams.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.PAYMENT_METHOD
                    )
                    .build()
                )
                .build()
            )
            .build()
        )
        .build()
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Invoice invoice = client.v1().invoices().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.create({
  customer: '{{CUSTOMER_ID}}',
  payment_settings: {
    payment_method_types: ['us_bank_account'],
    payment_method_options: {
      us_bank_account: {
        financial_connections: {
          permissions: ['ownership', 'payment_method'],
        },
      },
    },
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceCreateParams{
  Customer: stripe.String("{{CUSTOMER_ID}}"),
  PaymentSettings: &stripe.InvoiceCreatePaymentSettingsParams{
    PaymentMethodTypes: []*string{
      stripe.String(stripe.InvoicePaymentSettingsPaymentMethodTypeUSBankAccount),
    },
    PaymentMethodOptions: &stripe.InvoiceCreatePaymentSettingsPaymentMethodOptionsParams{
      USBankAccount: &stripe.InvoiceCreatePaymentSettingsPaymentMethodOptionsUSBankAccountParams{
        FinancialConnections: &stripe.InvoiceCreatePaymentSettingsPaymentMethodOptionsUSBankAccountFinancialConnectionsParams{
          Permissions: []*string{
            stripe.String(stripe.InvoicePaymentSettingsPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionOwnership),
            stripe.String(stripe.InvoicePaymentSettingsPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionPaymentMethod),
          },
        },
      },
    },
  },
}
result, err := sc.V1Invoices.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new InvoiceCreateOptions
{
    Customer = "{{CUSTOMER_ID}}",
    PaymentSettings = new InvoicePaymentSettingsOptions
    {
        PaymentMethodTypes = new List<string> { "us_bank_account" },
        PaymentMethodOptions = new InvoicePaymentSettingsPaymentMethodOptionsOptions
        {
            UsBankAccount = new InvoicePaymentSettingsPaymentMethodOptionsUsBankAccountOptions
            {
                FinancialConnections = new InvoicePaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsOptions
                {
                    Permissions = new List<string> { "ownership", "payment_method" },
                },
            },
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Invoices;
Invoice invoice = service.Create(options);
```

#### Subscriptions

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_settings[payment_method_types][]"=us_bank_account \
  -d "payment_settings[payment_method_options][us_bank_account][financial_connections][permissions][]"=ownership \
  -d "payment_settings[payment_method_options][us_bank_account][financial_connections][permissions][]"=payment_method
```

```cli
stripe subscriptions create  \
  --customer={{CUSTOMER_ID}} \
  -d "payment_settings[payment_method_types][0]"=us_bank_account \
  -d "payment_settings[payment_method_options][us_bank_account][financial_connections][permissions][0]"=ownership \
  -d "payment_settings[payment_method_options][us_bank_account][financial_connections][permissions][1]"=payment_method
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

subscription = client.v1.subscriptions.create({
  customer: '{{CUSTOMER_ID}}',
  payment_settings: {
    payment_method_types: ['us_bank_account'],
    payment_method_options: {
      us_bank_account: {
        financial_connections: {permissions: ['ownership', 'payment_method']},
      },
    },
  },
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
subscription = client.v1.subscriptions.create({
  "customer": "{{CUSTOMER_ID}}",
  "payment_settings": {
    "payment_method_types": ["us_bank_account"],
    "payment_method_options": {
      "us_bank_account": {
        "financial_connections": {"permissions": ["ownership", "payment_method"]},
      },
    },
  },
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$subscription = $stripe->subscriptions->create([
  'customer' => '{{CUSTOMER_ID}}',
  'payment_settings' => [
    'payment_method_types' => ['us_bank_account'],
    'payment_method_options' => [
      'us_bank_account' => [
        'financial_connections' => ['permissions' => ['ownership', 'payment_method']],
      ],
    ],
  ],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SubscriptionCreateParams params =
  SubscriptionCreateParams.builder()
    .setCustomer("{{CUSTOMER_ID}}")
    .setPaymentSettings(
      SubscriptionCreateParams.PaymentSettings.builder()
        .addPaymentMethodType(
          SubscriptionCreateParams.PaymentSettings.PaymentMethodType.US_BANK_ACCOUNT
        )
        .setPaymentMethodOptions(
          SubscriptionCreateParams.PaymentSettings.PaymentMethodOptions.builder()
            .setUsBankAccount(
              SubscriptionCreateParams.PaymentSettings.PaymentMethodOptions.UsBankAccount.builder()
                .setFinancialConnections(
                  SubscriptionCreateParams.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.builder()
                    .addPermission(
                      SubscriptionCreateParams.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.OWNERSHIP
                    )
                    .addPermission(
                      SubscriptionCreateParams.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.PAYMENT_METHOD
                    )
                    .build()
                )
                .build()
            )
            .build()
        )
        .build()
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Subscription subscription = client.v1().subscriptions().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const subscription = await stripe.subscriptions.create({
  customer: '{{CUSTOMER_ID}}',
  payment_settings: {
    payment_method_types: ['us_bank_account'],
    payment_method_options: {
      us_bank_account: {
        financial_connections: {
          permissions: ['ownership', 'payment_method'],
        },
      },
    },
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SubscriptionCreateParams{
  Customer: stripe.String("{{CUSTOMER_ID}}"),
  PaymentSettings: &stripe.SubscriptionCreatePaymentSettingsParams{
    PaymentMethodTypes: []*string{
      stripe.String(stripe.SubscriptionPaymentSettingsPaymentMethodTypeUSBankAccount),
    },
    PaymentMethodOptions: &stripe.SubscriptionCreatePaymentSettingsPaymentMethodOptionsParams{
      USBankAccount: &stripe.SubscriptionCreatePaymentSettingsPaymentMethodOptionsUSBankAccountParams{
        FinancialConnections: &stripe.SubscriptionCreatePaymentSettingsPaymentMethodOptionsUSBankAccountFinancialConnectionsParams{
          Permissions: []*string{
            stripe.String(stripe.SubscriptionPaymentSettingsPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionOwnership),
            stripe.String(stripe.SubscriptionPaymentSettingsPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionPaymentMethod),
          },
        },
      },
    },
  },
}
result, err := sc.V1Subscriptions.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new SubscriptionCreateOptions
{
    Customer = "{{CUSTOMER_ID}}",
    PaymentSettings = new SubscriptionPaymentSettingsOptions
    {
        PaymentMethodTypes = new List<string> { "us_bank_account" },
        PaymentMethodOptions = new SubscriptionPaymentSettingsPaymentMethodOptionsOptions
        {
            UsBankAccount = new SubscriptionPaymentSettingsPaymentMethodOptionsUsBankAccountOptions
            {
                FinancialConnections = new SubscriptionPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsOptions
                {
                    Permissions = new List<string> { "ownership", "payment_method" },
                },
            },
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Subscriptions;
Subscription subscription = service.Create(options);
```

When using dynamic payment methods for certain payments APIs, you can also configure requested permissions in the Dashboard. Learn how to [access additional account data on Financial Connections accounts](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md?dashboard-or-api=dashboard#access).

## Initiate an ownership refresh [Server-side]

All Financial Connections data retrievals are asynchronous. You initiate an ownership refresh and wait for it to complete, then retrieve the results. You can initiate ownership refreshes with the `prefetch` API parameter or the [Refresh API](https://docs.stripe.com/api/financial_connections/accounts/refresh.md).

### Prefetch ownership data

Specify whether you want to prefetch account ownership details *before* account collection. This initiates the refresh process as soon as your user connects their account in the [authentication flow](https://docs.stripe.com/financial-connections/fundamentals.md#authentication-flow). Set `prefetch` when you require ownership data for every linked account, to make sure you receive it with minimal delay. The `prefetch` parameter is available on all APIs that support Financial Connections.

```curl
curl https://api.stripe.com/v1/setup_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer="{{CUSTOMER_ID}}" \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][prefetch][]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership
```

```cli
stripe setup_intents create  \
  --customer="{{CUSTOMER_ID}}" \
  -d "payment_method_types[0]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][prefetch][0]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][0]"=payment_method \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][1]"=ownership
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        prefetch: ['ownership'],
        permissions: ['payment_method', 'ownership'],
      },
    },
  },
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
setup_intent = client.v1.setup_intents.create({
  "customer": "{{CUSTOMER_ID}}",
  "payment_method_types": ["us_bank_account"],
  "payment_method_options": {
    "us_bank_account": {
      "financial_connections": {
        "prefetch": ["ownership"],
        "permissions": ["payment_method", "ownership"],
      },
    },
  },
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$setupIntent = $stripe->setupIntents->create([
  'customer' => '{{CUSTOMER_ID}}',
  'payment_method_types' => ['us_bank_account'],
  'payment_method_options' => [
    'us_bank_account' => [
      'financial_connections' => [
        'prefetch' => ['ownership'],
        'permissions' => ['payment_method', 'ownership'],
      ],
    ],
  ],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SetupIntentCreateParams params =
  SetupIntentCreateParams.builder()
    .setCustomer("{{CUSTOMER_ID}}")
    .addPaymentMethodType("us_bank_account")
    .setPaymentMethodOptions(
      SetupIntentCreateParams.PaymentMethodOptions.builder()
        .setUsBankAccount(
          SetupIntentCreateParams.PaymentMethodOptions.UsBankAccount.builder()
            .setFinancialConnections(
              SetupIntentCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.builder()
                .addPermission(
                  SetupIntentCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.PAYMENT_METHOD
                )
                .addPermission(
                  SetupIntentCreateParams.PaymentMethodOptions.UsBankAccount.FinancialConnections.Permission.OWNERSHIP
                )
                .build()
            )
            .build()
        )
        .build()
    )
    .putExtraParam(
      "payment_method_options[us_bank_account][financial_connections][prefetch][0]",
      "ownership"
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
SetupIntent setupIntent = client.v1().setupIntents().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ['us_bank_account'],
  payment_method_options: {
    us_bank_account: {
      financial_connections: {
        prefetch: ['ownership'],
        permissions: ['payment_method', 'ownership'],
      },
    },
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SetupIntentCreateParams{
  Customer: stripe.String("{{CUSTOMER_ID}}"),
  PaymentMethodTypes: []*string{stripe.String("us_bank_account")},
  PaymentMethodOptions: &stripe.SetupIntentCreatePaymentMethodOptionsParams{
    USBankAccount: &stripe.SetupIntentCreatePaymentMethodOptionsUSBankAccountParams{
      FinancialConnections: &stripe.SetupIntentCreatePaymentMethodOptionsUSBankAccountFinancialConnectionsParams{
        Permissions: []*string{
          stripe.String(stripe.SetupIntentPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionPaymentMethod),
          stripe.String(stripe.SetupIntentPaymentMethodOptionsUSBankAccountFinancialConnectionsPermissionOwnership),
        },
      },
    },
  },
}
params.AddExtra(
  "payment_method_options[us_bank_account][financial_connections][prefetch][0]", "ownership")
result, err := sc.V1SetupIntents.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new SetupIntentCreateOptions
{
    Customer = "{{CUSTOMER_ID}}",
    PaymentMethodTypes = new List<string> { "us_bank_account" },
    PaymentMethodOptions = new SetupIntentPaymentMethodOptionsOptions
    {
        UsBankAccount = new SetupIntentPaymentMethodOptionsUsBankAccountOptions
        {
            FinancialConnections = new SetupIntentPaymentMethodOptionsUsBankAccountFinancialConnectionsOptions
            {
                Prefetch = new List<string> { "ownership" },
                Permissions = new List<string> { "payment_method", "ownership" },
            },
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SetupIntents;
SetupIntent setupIntent = service.Create(options);
```

### Initiate an on-demand refresh

Use the [Refresh API](https://docs.stripe.com/api/financial_connections/accounts/refresh.md) to initiate on-demand ownership refreshes *after* account collection, and fetch ownership information for a specific account at your convenience, allowing you to defer the decision until a later time. Although account ownership data can change, it generally doesn’t change as frequently as [balance](https://docs.stripe.com/financial-connections/balances.md) or [transaction](https://docs.stripe.com/financial-connections/transactions.md) data.

Use the Financial Connections account ID to initiate a refresh. If you’re integrating through a payments flow, find the account ID [on the associated Payment Method](https://docs.stripe.com/financial-connections/ach-direct-debit-payments.md#finding-the-financial-connections-account-id). When using a Financial Connections Session, retrieve it [through the session](https://docs.stripe.com/financial-connections/other-data-powered-products.md?platform=web#collect-an-account).

```curl
curl https://api.stripe.com/v1/financial_connections/accounts/{{FINANCIALCONNECTIONSACCOUNT_ID}}/refresh \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "features[]"=ownership
```

```cli
stripe financial_connections accounts refresh {{FINANCIALCONNECTIONSACCOUNT_ID}} \
  -d "features[0]"=ownership
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.financial_connections.accounts.refresh(
  '{{FINANCIALCONNECTIONSACCOUNT_ID}}',
  {features: ['ownership']},
)
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.financial_connections.accounts.refresh(
  "{{FINANCIALCONNECTIONSACCOUNT_ID}}",
  {"features": ["ownership"]},
)
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->financialConnections->accounts->refresh(
  '{{FINANCIALCONNECTIONSACCOUNT_ID}}',
  ['features' => ['ownership']]
);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountRefreshParams params =
  AccountRefreshParams.builder()
    .addFeature(AccountRefreshParams.Feature.OWNERSHIP)
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account =
  client.v1().financialConnections().accounts().refresh(
    "{{FINANCIALCONNECTIONSACCOUNT_ID}}",
    params
  );
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.financialConnections.accounts.refresh(
  '{{FINANCIALCONNECTIONSACCOUNT_ID}}',
  {
    features: ['ownership'],
  }
);
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.FinancialConnectionsAccountRefreshParams{
  Features: []*string{stripe.String("ownership")},
  Account: stripe.String("{{FINANCIALCONNECTIONSACCOUNT_ID}}"),
}
result, err := sc.V1FinancialConnectionsAccounts.Refresh(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new Stripe.FinancialConnections.AccountRefreshOptions
{
    Features = new List<string> { "ownership" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.FinancialConnections.Accounts;
Stripe.FinancialConnections.Account account = service.Refresh(
    "{{FINANCIALCONNECTIONSACCOUNT_ID}}",
    options);
```

> Refreshes aren’t allowed on inactive accounts.

### Wait for the ownership refresh to complete

The [ownership_refresh](https://docs.stripe.com/api/financial_connections/accounts/object.md#financial_connections_account_object-ownership_refresh) field on a Financial Connections account represents the ownership refresh state. This field remains `null` until you request the `ownership` permission and initiate a refresh. After you start an ownership refresh, the state changes to `pending`, and after completion, it moves to either `succeeded` or `failed`. We send the [financial_connections.account.refreshed_ownership](https://docs.stripe.com/api/events/types.md#event_types-financial_connections.account.refreshed_ownership) event when the ownership refresh completes. To determine the success of the ownership refresh, check the `ownership_refresh.status` field while handling the webhook.
Ownership refresh flow (See full diagram at https://docs.stripe.com/financial-connections/ownership)
After an ownership refresh completes, Stripe sets the availability of future refreshes through the [ownership_refresh.next_refresh_available_at](https://docs.stripe.com/api/financial_connections/accounts/object.md#financial_connections_account_object-ownership_refresh-next_refresh_available_at) field. Check this field before initiating a new ownership refresh to make sure that refreshes are currently available. If you attempt a refresh while the value is `null` (as is always the case when the refresh is pending or the account is inactive) or the current time is less than the `next_refresh_available_at` timestamp, the refresh won’t be initiated.

> In the unlikely event that a refresh fails, the `error` field on the refresh hash is a preview feature that provides the cause of the failure and recommended next steps. If you’d like to use it, [email us](mailto:financial-connections-beta+refresh-error@stripe.com) for access.

## Retrieve an account's ownership data [Server-side]

After the ownership refresh completes, retrieve the Financial Connections account from the API and expand the [ownership](https://docs.stripe.com/api/financial_connections/accounts/object.md#financial_connections_account_object-ownership) field to see ownership details.

```curl
curl -G https://api.stripe.com/v1/financial_connections/accounts/{{FINANCIALCONNECTIONSACCOUNT_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "expand[]"=ownership
```

```cli
stripe financial_connections accounts retrieve {{FINANCIALCONNECTIONSACCOUNT_ID}} \
  -d "expand[0]"=ownership
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.financial_connections.accounts.retrieve(
  '{{FINANCIALCONNECTIONSACCOUNT_ID}}',
  {expand: ['ownership']},
)
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.financial_connections.accounts.retrieve(
  "{{FINANCIALCONNECTIONSACCOUNT_ID}}",
  {"expand": ["ownership"]},
)
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->financialConnections->accounts->retrieve(
  '{{FINANCIALCONNECTIONSACCOUNT_ID}}',
  ['expand' => ['ownership']]
);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountRetrieveParams params =
  AccountRetrieveParams.builder().addExpand("ownership").build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account =
  client.v1().financialConnections().accounts().retrieve(
    "{{FINANCIALCONNECTIONSACCOUNT_ID}}",
    params
  );
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.financialConnections.accounts.retrieve(
  '{{FINANCIALCONNECTIONSACCOUNT_ID}}',
  {
    expand: ['ownership'],
  }
);
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.FinancialConnectionsAccountRetrieveParams{
  Account: stripe.String("{{FINANCIALCONNECTIONSACCOUNT_ID}}"),
}
params.AddExpand("ownership")
result, err := sc.V1FinancialConnectionsAccounts.GetByID(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new Stripe.FinancialConnections.AccountGetOptions
{
    Expand = new List<string> { "ownership" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.FinancialConnections.Accounts;
Stripe.FinancialConnections.Account account = service.Get(
    "{{FINANCIALCONNECTIONSACCOUNT_ID}}",
    options);
```

This returns the Financial Connections account with the ownership field expanded to list the account’s owners:

```json
{
  "id": "fca_zbyrdjTrwcYZJZc6WBs6GPid",
  "object": "financial_connections.account",
  "ownership": {
    "id": "fcaowns_1MzTG4IG1CZuezXppfPbUpXb",
    "object": "financial_connections.account_ownership",
    "created": 1651784999,
    "owners": {
      "object": "list",
      "data": [{
          "name": "Jenny Rosen",
          "email": "jenny.rosen@example.com",
          "phone": "+1 555-555-5555",
          "ownership": "fcaowns_1MzTG4IG1CZuezXppfPbUpXb",
          "raw_address": "510 Townsend San Francisco, CA 94103",
          "refreshed_at": 1651784999
        }
      ],
      "has_more": false,
      "url": "/v1/financial_connections/accounts/fca_zbyrdjTrwcYZJZc6WBs6GPid/owners?ownership=fcaowns_1MzTG4IG1CZuezXppfPbUpXb"
    }
  },
  "ownership_refresh": {
    "status": "succeeded",
    "last_attempted_at": 1651784999,
    "next_refresh_available_at": 1651785000
  },
  // ...
}
```

Stripe returns the ownership information made available by a financial institution, and the availability of ownership details varies. We return all available fields and owners provided by the bank. Ownership details can include account owner name, address, email, and phone number.

> The Ownership Match API is a preview feature that returns match scores using Financial Connections ownership data compared with input owner information. Your business might use this data to reduce exposure to fraudulent actors and account takeovers when accepting ACH payments or paying out funds. If you’re interested in using this preview feature, [email us](mailto:financial-connections-beta+ownership-match@stripe.com) for access.
