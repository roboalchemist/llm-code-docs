# Source: https://docs.stripe.com/connect/migrate-to-controller-properties.md

# Migrate your Connect integration to use controller properties instead of account types

Learn how to work with account controller properties instead of specifying account types.

You can configure connected accounts using account controller properties instead of defining accounts as Standard, Express, or Custom. These controller properties let you specify discrete account behaviors, such as access to a Stripe-hosted Dashboard and whether Stripe collects fees from the account or the platform. This modularity allows for more flexible configuration options.

Using account controller properties doesn’t require you to update your API version. **Migrating your integration to use controller properties is optional**. If you only use one type of connected account and aren’t interested in using a new configuration, you don’t need to update your integration.

We recommend you update your integration to take advantage of the increased modularity and new configurations available. The new properties are fully backwards compatible, so you can migrate your integration incrementally while continuing to work with account types.

Each account type maps to a set of controller properties. We automatically set those properties on your existing connected accounts and on any accounts that you create with account types going forward. When you update your integration to work with controller properties, you don’t have to update any of your connected accounts.

> You can start using features such as [embedded components](https://docs.stripe.com/connect/get-started-connect-embedded-components.md) without making any of the changes in this guide.

## Before you begin

- Learn how account controller properties work and how they map to your existing connected accounts.
- Determine which of the new account configurations make sense for your integration.

Updating your integration involves:

- Identifying code in your integration that references the account type, and updating it to reference the corresponding controller properties instead.
- Updating your account creation process to specify controller properties instead of `type`. Specifying `type` is no longer required.

## Account controller properties

You can specify values for the controller properties when you create a connected account using the [Accounts API](https://docs.stripe.com/api/accounts/create.md#create_account-controller). Any property that you don’t specify is set to a default value that has the least complex integration requirements.

If you’re building a new integration, you can get a configuration recommendation by completing [Connect platform onboarding](https://dashboard.stripe.com/connect).

| Property                                                                                                                             | Default value       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [controller.losses.payments](https://docs.stripe.com/api/accounts/create.md#create_account-controller-losses-payments)               | `stripe`            | Possible values:
  - `application`: Your platform is *responsible for negative balances* (The responsibility for managing risk and recovering negative balances on connected accounts. Stripe or the Connect platform can be liable for negative balances on connected accounts) and manages credit and fraud risk on the connected account, which requires you to review and acknowledge your responsibilities in [the Dashboard](https://dashboard.stripe.com/settings/connect/platform_profile)
  - `stripe`: Stripe is liable when this account can’t pay back negative balances resulting from payments. Your platform is still liable for a negative balance on your platform account.                                                                                                                                                                                                                                                                                                            |
| [controller.fees.payer](https://docs.stripe.com/api/accounts/create.md#create_account-controller-fees-payer)                         | `account`           | Possible values:

  - `account`: The connected account pays all Stripe fees directly to Stripe, inclusive of payment processing fees
  - `application`: The Connect platform pays all Stripe fees, inclusive of payment processing fees
  - `application_custom`: The account was created with type=custom
  - `application_express`: The account was created with type=express

  When you create an account, you can only specify `application` or `account`.

  `application_express` and `application_custom` are not valid creation parameters.

  For a comprehensive description of Stripe fee payment models, see the [fee behavior documentation](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior.md).                                                                                                                                                                                                                                                                       |
| [controller.requirement_collection](https://docs.stripe.com/api/accounts/create.md#create_account-controller-requirement_collection) | `stripe`            | Possible values:

  - `application`: Your platform is responsible for collecting updated information when *requirements are due or change* (The responsibility for collecting required information from connected accounts to keep their Stripe accounts active. Stripe or the Connect platform can be responsible for requirement collection)
  - `stripe`: Stripe is responsible for collecting updated information when *requirements are due or change* (The responsibility for collecting required information from connected accounts to keep their Stripe accounts active. Stripe or the Connect platform can be responsible for requirement collection)

  A value of `application` means that your platform can fully access the [KYC properties](https://docs.stripe.com/connect/identity-verification.md) on the account, as well as attest that the account has seen and accepted the [Stripe service agreement](https://docs.stripe.com/connect/service-agreement-types.md) using the API. |
| [controller.stripe_dashboard.type](https://docs.stripe.com/api/accounts/create.md#create_account-controller-stripe_dashboard-type)   | `full`              | Possible values:
  - `express`: The connected account can access the Express Dashboard
  - `full`: The  connected account can access the full Stripe Dashboard
  - `none`: The account can’t access the Express or Stripe Dashboard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [type](https://docs.stripe.com/api/accounts/create.md#create_account-type)                                                           | See the description | Possible values:

  - `custom`: The account was created as a Custom connected account
  - `express`: The account was created as an Express connected account
  - `standard`: The account was created as a Standard connected account or with controller properties matching Standard accounts
  - `none`: The account was created with no type value and its controller properties don’t match any of the three account types

  Specifying `type` is optional. If you create an account using `type`, you can only specify `custom`, `express`, or `standard`. `none` isn’t a valid account creation parameter.                                                                                                                                                                                                                                                                                                                                                                                        |

## Mapping account types to controller parameters

Each of the three account types maps to values in the `controller` hash of `v1/accounts` that match the behavior of that type.

### Standard

If you create an account without specifying any controller properties, the default values match the behavior of a Standard account. You can also create the equivalent of a Standard account by specifying the values that map to Standard account behavior.

These values map to a Standard account’s behavior:

- `losses.payments`: `stripe`
- `fees.payer`: `account`
- `requirement_collection`: `stripe`
- `stripe_dashboard.type`: `full`

#### Creation with controller properties

Request (using default values for all properties):

```curl
curl -X POST https://api.stripe.com/v1/accounts \
  -u "<<YOUR_SECRET_KEY>>:"
```

```cli
stripe accounts create
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.create()
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.accounts.create()
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->create([]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCreateParams params = AccountCreateParams.builder().build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account = client.v1().accounts().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.create();
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountCreateParams{}
result, err := sc.V1Accounts.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new AccountCreateOptions();
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Create(options);
```

Response:

```
{
  controller: {
    type: "application",
    is_controller: true,
    losses: {
      payments: "stripe"
    },
    requirement_collection: "stripe",
    fees: {
      payer: "account",
    },
    stripe_dashboard: {
      type: "full"
    }
  },
  type: "standard"
}
```

#### Creation with type

Request:

```curl
curl https://api.stripe.com/v1/accounts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d type=standard
```

```cli
stripe accounts create  \
  --type=standard
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.create({type: 'standard'})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.accounts.create({"type": "standard"})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->create(['type' => 'standard']);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCreateParams params =
  AccountCreateParams.builder().setType(AccountCreateParams.Type.STANDARD).build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account = client.v1().accounts().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.create({
  type: 'standard',
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountCreateParams{Type: stripe.String(stripe.AccountTypeStandard)}
result, err := sc.V1Accounts.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new AccountCreateOptions { Type = "standard" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Create(options);
```

Response:

```json
{
  controller: {
    type: "application",
    is_controller: true,
    losses: {
      payments: "stripe"
    },
    requirement_collection: "stripe",
    fees: {
      payer: "account",
    },
    stripe_dashboard: {
      type: "full"
    }
  },
  type: "standard"
}
```

### Express

These values map to an Express account’s behavior:

- `losses.payments`: `application`
- `fees.payer`: `application` (see note)
- `requirement_collection`: `stripe`
- `stripe_dashboard.type`: `express`

> Creating an Express account using `type`, sets the `controller.fees.payer` property to `application_express` instead of `application`. This difference denotes a variation in Stripe [fee billing behavior](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior.md) when your platform is using Direct charges.

#### Creation with controller properties

Request:

```curl
curl https://api.stripe.com/v1/accounts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "controller[stripe_dashboard][type]"=express \
  -d "controller[fees][payer]"=application \
  -d "controller[losses][payments]"=application
```

```cli
stripe accounts create  \
  -d "controller[stripe_dashboard][type]"=express \
  -d "controller[fees][payer]"=application \
  -d "controller[losses][payments]"=application
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.create({
  controller: {
    stripe_dashboard: {type: 'express'},
    fees: {payer: 'application'},
    losses: {payments: 'application'},
  },
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.accounts.create({
  "controller": {
    "stripe_dashboard": {"type": "express"},
    "fees": {"payer": "application"},
    "losses": {"payments": "application"},
  },
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->create([
  'controller' => [
    'stripe_dashboard' => ['type' => 'express'],
    'fees' => ['payer' => 'application'],
    'losses' => ['payments' => 'application'],
  ],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCreateParams params =
  AccountCreateParams.builder()
    .setController(
      AccountCreateParams.Controller.builder()
        .setStripeDashboard(
          AccountCreateParams.Controller.StripeDashboard.builder()
            .setType(AccountCreateParams.Controller.StripeDashboard.Type.EXPRESS)
            .build()
        )
        .setFees(
          AccountCreateParams.Controller.Fees.builder()
            .setPayer(AccountCreateParams.Controller.Fees.Payer.APPLICATION)
            .build()
        )
        .setLosses(
          AccountCreateParams.Controller.Losses.builder()
            .setPayments(AccountCreateParams.Controller.Losses.Payments.APPLICATION)
            .build()
        )
        .build()
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account = client.v1().accounts().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.create({
  controller: {
    stripe_dashboard: {
      type: 'express',
    },
    fees: {
      payer: 'application',
    },
    losses: {
      payments: 'application',
    },
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountCreateParams{
  Controller: &stripe.AccountCreateControllerParams{
    StripeDashboard: &stripe.AccountCreateControllerStripeDashboardParams{
      Type: stripe.String(stripe.AccountControllerStripeDashboardTypeExpress),
    },
    Fees: &stripe.AccountCreateControllerFeesParams{
      Payer: stripe.String(stripe.AccountControllerFeesPayerApplication),
    },
    Losses: &stripe.AccountCreateControllerLossesParams{
      Payments: stripe.String(stripe.AccountControllerLossesPaymentsApplication),
    },
  },
}
result, err := sc.V1Accounts.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new AccountCreateOptions
{
    Controller = new AccountControllerOptions
    {
        StripeDashboard = new AccountControllerStripeDashboardOptions
        {
            Type = "express",
        },
        Fees = new AccountControllerFeesOptions { Payer = "application" },
        Losses = new AccountControllerLossesOptions { Payments = "application" },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Create(options);
```

Response:

```json
{
  controller: {
    type: "application",
    is_controller: true,
    losses: {
      payments: "application"
    },
    requirement_collection: "stripe",
    fees: {
      payer: "application",
    },
    stripe_dashboard: {
      type: "express"
    }
  },
  type: "none"
}
```

#### Creation with type

Request:

```curl
curl https://api.stripe.com/v1/accounts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d type=express
```

```cli
stripe accounts create  \
  --type=express
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.create({type: 'express'})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.accounts.create({"type": "express"})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->create(['type' => 'express']);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCreateParams params =
  AccountCreateParams.builder().setType(AccountCreateParams.Type.EXPRESS).build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account = client.v1().accounts().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.create({
  type: 'express',
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountCreateParams{Type: stripe.String(stripe.AccountTypeExpress)}
result, err := sc.V1Accounts.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new AccountCreateOptions { Type = "express" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Create(options);
```

Response:

```json
{
  controller: {
    type: "application",
    is_controller: true,
    losses: {
      payments: "application"
    },
    requirement_collection: "stripe",
    fees: {
      payer: "application_express",
    },
    stripe_dashboard: {
      type: "express"
    }
  },
  type: "express"
}
```

### Custom

These values map to a Custom account’s behavior:

- `losses.payments`: `application`
- `fees.payer`: `application` (see note)
- `requirement_collection`: `application`
- `stripe_dashboard.type`: `none`

You must also specify the account country when creating a Custom account, and request the `card_payments` and `transfers` capabilities.

> Creating a Custom account using `type`, sets the `controller.fees.payer` property to `application_custom` instead of `application`. This difference denotes a variation in Stripe [fee billing behavior](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior.md) when your platform is using Direct charges.

#### Creation with controller properties

Request:

```curl
curl https://api.stripe.com/v1/accounts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "controller[stripe_dashboard][type]"=none \
  -d "controller[fees][payer]"=application \
  -d "controller[losses][payments]"=application \
  -d "controller[requirement_collection]"=application \
  -d "capabilities[transfers][requested]"=true \
  -d country=US
```

```cli
stripe accounts create  \
  -d "controller[stripe_dashboard][type]"=none \
  -d "controller[fees][payer]"=application \
  -d "controller[losses][payments]"=application \
  -d "controller[requirement_collection]"=application \
  -d "capabilities[transfers][requested]"=true \
  --country=US
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.create({
  controller: {
    stripe_dashboard: {type: 'none'},
    fees: {payer: 'application'},
    losses: {payments: 'application'},
    requirement_collection: 'application',
  },
  capabilities: {transfers: {requested: 'true'}},
  country: 'US',
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.accounts.create({
  "controller": {
    "stripe_dashboard": {"type": "none"},
    "fees": {"payer": "application"},
    "losses": {"payments": "application"},
    "requirement_collection": "application",
  },
  "capabilities": {"transfers": {"requested": True}},
  "country": "US",
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->create([
  'controller' => [
    'stripe_dashboard' => ['type' => 'none'],
    'fees' => ['payer' => 'application'],
    'losses' => ['payments' => 'application'],
    'requirement_collection' => 'application',
  ],
  'capabilities' => ['transfers' => ['requested' => true]],
  'country' => 'US',
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCreateParams params =
  AccountCreateParams.builder()
    .setController(
      AccountCreateParams.Controller.builder()
        .setStripeDashboard(
          AccountCreateParams.Controller.StripeDashboard.builder()
            .setType(AccountCreateParams.Controller.StripeDashboard.Type.NONE)
            .build()
        )
        .setFees(
          AccountCreateParams.Controller.Fees.builder()
            .setPayer(AccountCreateParams.Controller.Fees.Payer.APPLICATION)
            .build()
        )
        .setLosses(
          AccountCreateParams.Controller.Losses.builder()
            .setPayments(AccountCreateParams.Controller.Losses.Payments.APPLICATION)
            .build()
        )
        .setRequirementCollection(
          AccountCreateParams.Controller.RequirementCollection.APPLICATION
        )
        .build()
    )
    .setCapabilities(
      AccountCreateParams.Capabilities.builder()
        .setTransfers(
          AccountCreateParams.Capabilities.Transfers.builder().setRequested(true).build()
        )
        .build()
    )
    .setCountry("US")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account = client.v1().accounts().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.create({
  controller: {
    stripe_dashboard: {
      type: 'none',
    },
    fees: {
      payer: 'application',
    },
    losses: {
      payments: 'application',
    },
    requirement_collection: 'application',
  },
  capabilities: {
    transfers: {
      requested: true,
    },
  },
  country: 'US',
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountCreateParams{
  Controller: &stripe.AccountCreateControllerParams{
    StripeDashboard: &stripe.AccountCreateControllerStripeDashboardParams{
      Type: stripe.String(stripe.AccountControllerStripeDashboardTypeNone),
    },
    Fees: &stripe.AccountCreateControllerFeesParams{
      Payer: stripe.String(stripe.AccountControllerFeesPayerApplication),
    },
    Losses: &stripe.AccountCreateControllerLossesParams{
      Payments: stripe.String(stripe.AccountControllerLossesPaymentsApplication),
    },
    RequirementCollection: stripe.String(stripe.AccountControllerRequirementCollectionApplication),
  },
  Capabilities: &stripe.AccountCreateCapabilitiesParams{
    Transfers: &stripe.AccountCreateCapabilitiesTransfersParams{
      Requested: stripe.Bool(true),
    },
  },
  Country: stripe.String("US"),
}
result, err := sc.V1Accounts.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new AccountCreateOptions
{
    Controller = new AccountControllerOptions
    {
        StripeDashboard = new AccountControllerStripeDashboardOptions { Type = "none" },
        Fees = new AccountControllerFeesOptions { Payer = "application" },
        Losses = new AccountControllerLossesOptions { Payments = "application" },
        RequirementCollection = "application",
    },
    Capabilities = new AccountCapabilitiesOptions
    {
        Transfers = new AccountCapabilitiesTransfersOptions { Requested = true },
    },
    Country = "US",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Create(options);
```

Response:

```json
{
  controller: {
    type: "application",
    is_controller: true,
    losses: {
      payments: "application"
    },
    requirement_collection: "application",
    fees: {
      payer: "application",
    },
    stripe_dashboard: {
      type: "none"
    }
  },
  type: "none"
}
```

#### Creation with type

Request:

```curl
curl https://api.stripe.com/v1/accounts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d type=custom \
  -d "capabilities[transfers][requested]"=true \
  -d country=US
```

```cli
stripe accounts create  \
  --type=custom \
  -d "capabilities[transfers][requested]"=true \
  --country=US
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.create({
  type: 'custom',
  capabilities: {transfers: {requested: 'true'}},
  country: 'US',
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.accounts.create({
  "type": "custom",
  "capabilities": {"transfers": {"requested": True}},
  "country": "US",
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->create([
  'type' => 'custom',
  'capabilities' => ['transfers' => ['requested' => true]],
  'country' => 'US',
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCreateParams params =
  AccountCreateParams.builder()
    .setType(AccountCreateParams.Type.CUSTOM)
    .setCapabilities(
      AccountCreateParams.Capabilities.builder()
        .setTransfers(
          AccountCreateParams.Capabilities.Transfers.builder().setRequested(true).build()
        )
        .build()
    )
    .setCountry("US")
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account = client.v1().accounts().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.create({
  type: 'custom',
  capabilities: {
    transfers: {
      requested: true,
    },
  },
  country: 'US',
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountCreateParams{
  Type: stripe.String(stripe.AccountTypeCustom),
  Capabilities: &stripe.AccountCreateCapabilitiesParams{
    Transfers: &stripe.AccountCreateCapabilitiesTransfersParams{
      Requested: stripe.Bool(true),
    },
  },
  Country: stripe.String("US"),
}
result, err := sc.V1Accounts.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new AccountCreateOptions
{
    Type = "custom",
    Capabilities = new AccountCapabilitiesOptions
    {
        Transfers = new AccountCapabilitiesTransfersOptions { Requested = true },
    },
    Country = "US",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Create(options);
```

Response:

```json
{
  controller: {
    type: "application",
    is_controller: true,
    losses: {
      payments: "application"
    },
    requirement_collection: "application",
    fees: {
      payer: "application_custom",
    },
    stripe_dashboard: {
      type: "none"
    }
  },
  type: "custom"
}
```

## Migrate code to use controller properties

In addition to updating your account creation process to use controller properties, update your integration by reviewing your code and looking for references to account types.

For each reference to an account type, determine which controller property or properties are relevant and update the code accordingly.

For example, say that your code includes a conditional statement that applies to Express and Custom accounts because it relates to your platform being responsible for negative balances. Update that logic from `if type == express` or `if type == custom` to `if controller.losses.payments == application`.

If you create connected accounts that don’t match an account type, consider their controller properties as well when updating your code. The logic for handling those accounts can differ from your existing logic that’s based on account types.

You can use this table to identify the controller properties associated with each account type:

| Account Type | losses.payments | fees.payer            | requirement_collection | stripe_dashboard.type |
| ------------ | --------------- | --------------------- | ---------------------- | --------------------- |
| Custom       | `application`   | `application_custom`  | `application`          | `none`                |
| Express      | `application`   | `application_express` | `stripe`               | `express`             |
| Standard     | `stripe`        | `account`             | `stripe`               | `full`                |

> Remember that Express and Custom accounts have a different value for `fees.payer` than equivalent accounts created using controller properties. When updating code related to collecting fees, you must take into account the difference in behavior.

## Unsupported configurations

When creating accounts with controller properties, the following combinations aren’t supported:

`controller.requirement_collection` = `application` isn’t compatible with any of the following values:

- `controller.losses.payments` = `stripe`
- `controller.fees.payer` = `account`
- `controller.stripe_dashboard.type` = `express`
- `controller.stripe_dashboard.type` = `full`

`controller.stripe_dashboard.type` = `express` isn’t compatible with any of the following values:

- `controller.losses.payments` = `stripe`
- `controller.fees.payer` = `account`
- `controller.requirement_collection` = `application`

`controller.stripe_dashboard.type` = `full` isn’t compatible with any of the following values:

- `controller.losses.payments` = `application`
- `controller.fees.payer` = `application`
- `controller.requirement_collection` = `application`

`controller.stripe_dashboard.type` = `none` isn’t supported when both of the following values are set (it’s supported when only one of them is set):

- `controller.requirement_collection` = `stripe`
- `controller.losses.payments` = `application`
