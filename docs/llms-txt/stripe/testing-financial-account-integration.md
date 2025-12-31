# Source: https://docs.stripe.com/treasury/account-management/testing-financial-account-integration.md

# Testing financial account integration

Learn how to ensure your financial accounts are functioning correctly.

Stripe *Treasury* (A collection of API endpoints and cloud- and web-based features that enable platforms to offer embedded financial solutions to their users) includes a live mode and test mode. You can toggle between modes from your Dashboard using the mode toggle in the upper-right corner.
![Upper-corner of Dashboard with a red box highlighting the test mode toggle.](https://b.stripecdn.com/docs-statics-srv/assets/test-mode.13546c94012a516a6d6069120f064c99.png)

Test mode toggle

> You must complete the [Gaining API access to Treasury](https://docs.stripe.com/financial-accounts/connect/access.md) guide’s live mode steps before you have access to live mode financial accounts.

To access test mode in the API, use the test mode API key with your requests. The test mode API key is included within most documentation code examples, but you can also find it in the **Developers** page of your [Dashboard](https://dashboard.stripe.com/test/apikeys). Make sure to use the test key for testing and not the live one. The test key has the form `sk_test_xxx`, whereas the live key is in the form `sk_live_xxx`.

Before creating a test financial account, create a test connected account using `POST /v1/accounts`. Use the connected account ID you receive from the response to assign the financial account you create in the next step to this account. Treasury is supported only in the US, so assign `US` to the `country` parameter. You’re also requesting capabilities for the connected account that Treasury requires to function properly. Make note of the `id` value in the response. As mentioned, you use the ID as the value for the `Stripe-Account` header in the following code example.

```curl
curl https://api.stripe.com/v1/accounts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d country=US \
  -d type=custom \
  -d business_type=company \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d "capabilities[treasury][requested]"=true
```

```cli
stripe accounts create  \
  --country=US \
  --type=custom \
  --business-type=company \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d "capabilities[treasury][requested]"=true
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.create({
  country: 'US',
  type: 'custom',
  business_type: 'company',
  capabilities: {
    card_payments: {requested: true},
    transfers: {requested: true},
    treasury: {requested: true},
  },
})
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.accounts.create({
  "country": "US",
  "type": "custom",
  "business_type": "company",
  "capabilities": {
    "card_payments": {"requested": True},
    "transfers": {"requested": True},
    "treasury": {"requested": True},
  },
})
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->create([
  'country' => 'US',
  'type' => 'custom',
  'business_type' => 'company',
  'capabilities' => [
    'card_payments' => ['requested' => true],
    'transfers' => ['requested' => true],
    'treasury' => ['requested' => true],
  ],
]);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountCreateParams params =
  AccountCreateParams.builder()
    .setCountry("US")
    .setType(AccountCreateParams.Type.CUSTOM)
    .setBusinessType(AccountCreateParams.BusinessType.COMPANY)
    .setCapabilities(
      AccountCreateParams.Capabilities.builder()
        .setCardPayments(
          AccountCreateParams.Capabilities.CardPayments.builder()
            .setRequested(true)
            .build()
        )
        .setTransfers(
          AccountCreateParams.Capabilities.Transfers.builder().setRequested(true).build()
        )
        .build()
    )
    .putExtraParam("capabilities[treasury][requested]", true)
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account = client.v1().accounts().create(params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.create({
  country: 'US',
  type: 'custom',
  business_type: 'company',
  capabilities: {
    card_payments: {
      requested: true,
    },
    transfers: {
      requested: true,
    },
    treasury: {
      requested: true,
    },
  },
});
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountCreateParams{
  Country: stripe.String("US"),
  Type: stripe.String(stripe.AccountTypeCustom),
  BusinessType: stripe.String(stripe.AccountBusinessTypeCompany),
  Capabilities: &stripe.AccountCreateCapabilitiesParams{
    CardPayments: &stripe.AccountCreateCapabilitiesCardPaymentsParams{
      Requested: stripe.Bool(true),
    },
    Transfers: &stripe.AccountCreateCapabilitiesTransfersParams{
      Requested: stripe.Bool(true),
    },
  },
}
params.AddExtra("capabilities[treasury][requested]", true)
result, err := sc.V1Accounts.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new AccountCreateOptions
{
    Country = "US",
    Type = "custom",
    BusinessType = "company",
    Capabilities = new AccountCapabilitiesOptions
    {
        CardPayments = new AccountCapabilitiesCardPaymentsOptions { Requested = true },
        Transfers = new AccountCapabilitiesTransfersOptions { Requested = true },
        Treasury = new AccountCapabilitiesTreasuryOptions { Requested = true },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Create(options);
```

If successful, the response returns the new connected account [Account](https://docs.stripe.com/api/accounts.md) object.

```json
{
  "id": "{{CUSTOM_ACCOUNT_ID}}",
  "livemode": false,
  ...
}
```

Next, create a financial account using `POST /v1/treasury/financial_accounts`. Include a `Stripe-Account` header set to the value of the connected account ID you created in the previous instruction. The only required value in the body is to set `supported_currencies[]` to `usd`. To learn more about financial accounts, see [Working with financial accounts](https://docs.stripe.com/financial-accounts/connect/account-management/financial-accounts.md) or the [FinancialAccounts](https://docs.stripe.com/api/treasury/financial_accounts.md) object description in the Stripe API reference.

```curl
curl https://api.stripe.com/v1/treasury/financial_accounts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "supported_currencies[]"=usd \
  -d "features[financial_addresses][aba][requested]"=true
```

```cli
stripe treasury financial_accounts create  \
  --stripe-account {{CONNECTEDACCOUNT_ID}} \
  -d "supported_currencies[0]"=usd \
  -d "features[financial_addresses][aba][requested]"=true
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

financial_account = client.v1.treasury.financial_accounts.create(
  {
    supported_currencies: ['usd'],
    features: {financial_addresses: {aba: {requested: true}}},
  },
  {stripe_account: '{{CONNECTEDACCOUNT_ID}}'},
)
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
financial_account = client.v1.treasury.financial_accounts.create(
  {
    "supported_currencies": ["usd"],
    "features": {"financial_addresses": {"aba": {"requested": True}}},
  },
  {"stripe_account": "{{CONNECTEDACCOUNT_ID}}"},
)
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$financialAccount = $stripe->treasury->financialAccounts->create(
  [
    'supported_currencies' => ['usd'],
    'features' => ['financial_addresses' => ['aba' => ['requested' => true]]],
  ],
  ['stripe_account' => '{{CONNECTEDACCOUNT_ID}}']
);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

FinancialAccountCreateParams params =
  FinancialAccountCreateParams.builder()
    .addSupportedCurrency("usd")
    .setFeatures(
      FinancialAccountCreateParams.Features.builder()
        .setFinancialAddresses(
          FinancialAccountCreateParams.Features.FinancialAddresses.builder()
            .setAba(
              FinancialAccountCreateParams.Features.FinancialAddresses.Aba.builder()
                .setRequested(true)
                .build()
            )
            .build()
        )
        .build()
    )
    .build();

RequestOptions requestOptions =
  RequestOptions.builder().setStripeAccount("{{CONNECTEDACCOUNT_ID}}").build();
// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.

FinancialAccount financialAccount =
  client.v1().treasury().financialAccounts().create(params, requestOptions);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const financialAccount = await stripe.treasury.financialAccounts.create(
  {
    supported_currencies: ['usd'],
    features: {
      financial_addresses: {
        aba: {
          requested: true,
        },
      },
    },
  },
  {
    stripeAccount: '{{CONNECTEDACCOUNT_ID}}',
  }
);
```

```go
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TreasuryFinancialAccountCreateParams{
  SupportedCurrencies: []*string{stripe.String("usd")},
  Features: &stripe.TreasuryFinancialAccountCreateFeaturesParams{
    FinancialAddresses: &stripe.TreasuryFinancialAccountCreateFeaturesFinancialAddressesParams{
      ABA: &stripe.TreasuryFinancialAccountCreateFeaturesFinancialAddressesABAParams{
        Requested: stripe.Bool(true),
      },
    },
  },
}
params.SetStripeAccount("{{CONNECTEDACCOUNT_ID}}")
result, err := sc.V1TreasuryFinancialAccounts.Create(context.TODO(), params)
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new Stripe.Treasury.FinancialAccountCreateOptions
{
    SupportedCurrencies = new List<string> { "usd" },
    Features = new Stripe.Treasury.FinancialAccountFeaturesOptions
    {
        FinancialAddresses = new Stripe.Treasury.FinancialAccountFeaturesFinancialAddressesOptions
        {
            Aba = new Stripe.Treasury.FinancialAccountFeaturesFinancialAddressesAbaOptions
            {
                Requested = true,
            },
        },
    },
};
var requestOptions = new RequestOptions
{
    StripeAccount = "{{CONNECTEDACCOUNT_ID}}",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Treasury.FinancialAccounts;
Stripe.Treasury.FinancialAccount financialAccount = service.Create(
    options,
    requestOptions);
```

If successful, the response returns the newly created `FinancialAccount` object.

```json
{
  "id": "{{FINANCIAL_ACCOUNT_ID}}",
  "livemode": false,
  "active_features": [],
  "pending_features": [],
  "restricted_features": ["financial_addresses.aba"],
  ...
}
```

You now have a test mode financial account attached to a test mode connected account. However, the connected account hasn’t been onboarded so required information is missing from the `requirements` hash. If you call `GET /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}` using the financial account ID in the JSON response of the previous instruction, you see the `financial_addresses` array of hashes has an entry for the requested `aba` with a `status` of `restricted` because the connected account has `requirements_past_due`.

```json
{
  …
  "financial_addresses": {
    "aba": {
      "requested": true,
      "status": "restricted",
      "status_details": [
        {
          "code": "requirements_past_due",
          "resolution": "provide_information"
        }
      ]
    }
  }
  …
}
```

To enable requested features on your test mode financial account without first going through connected account onboarding, you must use `POST /v1/accounts/{{CONNECTED_ACCOUNT_ID}}` to [provide test values](https://docs.stripe.com/connect/testing-verification.md) that fulfill all the requirements, as in the following request that uses a previously created connected account to apply the required account details.

> You can’t create a test mode financial account attached to a live mode connected account.

```curl
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "tos_acceptance[date]"=1547923073 \
  -d "tos_acceptance[ip]"="172.18.80.19" \
  -d "settings[treasury][tos_acceptance][date]"=1547923073 \
  -d "settings[treasury][tos_acceptance][ip]"="172.18.80.19" \
  -d "business_profile[mcc]"=5045 \
  --data-urlencode "business_profile[url]"="https://bestcookieco.com" \
  -d "company[address][city]"=Schenectady \
  -d "company[address][line1]"="123 State St" \
  -d "company[address][postal_code]"=12345 \
  -d "company[address][state]"=NY \
  -d "company[tax_id]"=000000000 \
  -d "company[name]"="The Best Cookie Co" \
  -d "company[phone]"=8888675309 \
  -d "individual[first_name]"=Jenny \
  -d "individual[last_name]"=Rosen
```

```cli
stripe accounts update {{CONNECTED_ACCOUNT_ID}} \
  -d "tos_acceptance[date]"=1547923073 \
  -d "tos_acceptance[ip]"="172.18.80.19" \
  -d "settings[treasury][tos_acceptance][date]"=1547923073 \
  -d "settings[treasury][tos_acceptance][ip]"="172.18.80.19" \
  -d "business_profile[mcc]"=5045 \
  -d "business_profile[url]"="https://bestcookieco.com" \
  -d "company[address][city]"=Schenectady \
  -d "company[address][line1]"="123 State St" \
  -d "company[address][postal_code]"=12345 \
  -d "company[address][state]"=NY \
  -d "company[tax_id]"=000000000 \
  -d "company[name]"="The Best Cookie Co" \
  -d "company[phone]"=8888675309 \
  -d "individual[first_name]"=Jenny \
  -d "individual[last_name]"=Rosen
```

```ruby
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

account = client.v1.accounts.update(
  '{{CONNECTED_ACCOUNT_ID}}',
  {
    tos_acceptance: {
      date: 1547923073,
      ip: '172.18.80.19',
    },
    settings: {
      treasury: {
        tos_acceptance: {
          date: 1547923073,
          ip: '172.18.80.19',
        },
      },
    },
    business_profile: {
      mcc: '5045',
      url: 'https://bestcookieco.com',
    },
    company: {
      address: {
        city: 'Schenectady',
        line1: '123 State St',
        postal_code: '12345',
        state: 'NY',
      },
      tax_id: '000000000',
      name: 'The Best Cookie Co',
      phone: '8888675309',
    },
    individual: {
      first_name: 'Jenny',
      last_name: 'Rosen',
    },
  },
)
```

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
client = StripeClient("<<YOUR_SECRET_KEY>>")

# For SDK versions 12.4.0 or lower, remove '.v1' from the following line.
account = client.v1.accounts.update(
  "{{CONNECTED_ACCOUNT_ID}}",
  {
    "tos_acceptance": {"date": 1547923073, "ip": "172.18.80.19"},
    "settings": {
      "treasury": {"tos_acceptance": {"date": 1547923073, "ip": "172.18.80.19"}},
    },
    "business_profile": {"mcc": "5045", "url": "https://bestcookieco.com"},
    "company": {
      "address": {
        "city": "Schenectady",
        "line1": "123 State St",
        "postal_code": "12345",
        "state": "NY",
      },
      "tax_id": "000000000",
      "name": "The Best Cookie Co",
      "phone": "8888675309",
    },
    "individual": {"first_name": "Jenny", "last_name": "Rosen"},
  },
)
```

```php
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$account = $stripe->accounts->update(
  '{{CONNECTED_ACCOUNT_ID}}',
  [
    'tos_acceptance' => [
      'date' => 1547923073,
      'ip' => '172.18.80.19',
    ],
    'settings' => [
      'treasury' => [
        'tos_acceptance' => [
          'date' => 1547923073,
          'ip' => '172.18.80.19',
        ],
      ],
    ],
    'business_profile' => [
      'mcc' => '5045',
      'url' => 'https://bestcookieco.com',
    ],
    'company' => [
      'address' => [
        'city' => 'Schenectady',
        'line1' => '123 State St',
        'postal_code' => '12345',
        'state' => 'NY',
      ],
      'tax_id' => '000000000',
      'name' => 'The Best Cookie Co',
      'phone' => '8888675309',
    ],
    'individual' => [
      'first_name' => 'Jenny',
      'last_name' => 'Rosen',
    ],
  ]
);
```

```java
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountUpdateParams params =
  AccountUpdateParams.builder()
    .setTosAcceptance(
      AccountUpdateParams.TosAcceptance.builder()
        .setDate(1547923073L)
        .setIp("172.18.80.19")
        .build()
    )
    .setSettings(
      AccountUpdateParams.Settings.builder()
        .setTreasury(
          AccountUpdateParams.Settings.Treasury.builder()
            .setTosAcceptance(
              AccountUpdateParams.Settings.Treasury.TosAcceptance.builder()
                .setDate(1547923073L)
                .setIp("172.18.80.19")
                .build()
            )
            .build()
        )
        .build()
    )
    .setBusinessProfile(
      AccountUpdateParams.BusinessProfile.builder()
        .setMcc("5045")
        .setUrl("https://bestcookieco.com")
        .build()
    )
    .setCompany(
      AccountUpdateParams.Company.builder()
        .setAddress(
          AccountUpdateParams.Company.Address.builder()
            .setCity("Schenectady")
            .setLine1("123 State St")
            .setPostalCode("12345")
            .setState("NY")
            .build()
        )
        .setTaxId("000000000")
        .setName("The Best Cookie Co")
        .setPhone("8888675309")
        .build()
    )
    .setIndividual(
      AccountUpdateParams.Individual.builder()
        .setFirstName("Jenny")
        .setLastName("Rosen")
        .build()
    )
    .build();

// For SDK versions 29.4.0 or lower, remove '.v1()' from the following line.
Account account = client.v1().accounts().update("{{CONNECTED_ACCOUNT_ID}}", params);
```

```node
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.accounts.update(
  '{{CONNECTED_ACCOUNT_ID}}',
  {
    tos_acceptance: {
      date: 1547923073,
      ip: '172.18.80.19',
    },
    settings: {
      treasury: {
        tos_acceptance: {
          date: 1547923073,
          ip: '172.18.80.19',
        },
      },
    },
    business_profile: {
      mcc: '5045',
      url: 'https://bestcookieco.com',
    },
    company: {
      address: {
        city: 'Schenectady',
        line1: '123 State St',
        postal_code: '12345',
        state: 'NY',
      },
      tax_id: '000000000',
      name: 'The Best Cookie Co',
      phone: '8888675309',
    },
    individual: {
      first_name: 'Jenny',
      last_name: 'Rosen',
    },
  }
);
```

```dotnet
// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
var options = new AccountUpdateOptions
{
    TosAcceptance = new AccountTosAcceptanceOptions
    {
        Date = DateTimeOffset.FromUnixTimeSeconds(1547923073).UtcDateTime,
        Ip = "172.18.80.19",
    },
    Settings = new AccountSettingsOptions
    {
        Treasury = new AccountSettingsTreasuryOptions
        {
            TosAcceptance = new AccountSettingsTreasuryTosAcceptanceOptions
            {
                Date = DateTimeOffset.FromUnixTimeSeconds(1547923073).UtcDateTime,
                Ip = "172.18.80.19",
            },
        },
    },
    BusinessProfile = new AccountBusinessProfileOptions
    {
        Mcc = "5045",
        Url = "https://bestcookieco.com",
    },
    Company = new AccountCompanyOptions
    {
        Address = new AddressOptions
        {
            City = "Schenectady",
            Line1 = "123 State St",
            PostalCode = "12345",
            State = "NY",
        },
        TaxId = "000000000",
        Name = "The Best Cookie Co",
        Phone = "8888675309",
    },
    Individual = new AccountIndividualOptions { FirstName = "Jenny", LastName = "Rosen" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account account = service.Update("{{CONNECTED_ACCOUNT_ID}}", options);
```

```go

// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
stripe.Key = "<<YOUR_SECRET_KEY>>"

params := &stripe.AccountParams{
  TOSAcceptance: &stripe.AccountTOSAcceptanceParams{
    Date: stripe.Int64(1547923073),
    IP: stripe.String("172.18.80.19"),
  },
  Settings: &stripe.Settings{
    Treasury: &stripe.Settings.Treasury{
      TOSAcceptance: &stripe.Settings.Treasury.TOSAcceptance{
        Date: stripe.Int64(1547923073),
        IP: stripe.String("172.18.80.19"),
      }
    }
  },
  BusinessProfile: &stripe.AccountBusinessProfileParams{
    MCC: stripe.String("5045"),
    URL: stripe.String("https://bestcookieco.com"),
  },
  Company: &stripe.AccountCompanyParams{
    Address: &stripe.AccountCompanyAddressParams{
      City: stripe.String("Schenectady"),
      Line1: stripe.String("123 State St"),
      PostalCode: stripe.String("12345"),
      State: stripe.String("NY"),
    },
    TaxID: stripe.String("000000000"),
    Name: stripe.String("The Best Cookie Co"),
    Phone: stripe.String("8888675309"),
  },
  Individual: &stripe.AccountIndividualParams{
    FirstName: stripe.String("Jenny"),
    LastName: stripe.String("Rosen"),
  },
};
result, _ := account.Update("{{CONNECTED_ACCOUNT_ID}}", params);
```
