# Source: https://plivo.com/docs/messaging/api/10dlc/profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Profile

> Create and manage profiles for 10DLC registration

Create a profile to provide details about your company to Plivo. You can use the profile to create 10DLC brands for messaging customers.

## API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/Profile/
```

***

## The Profile Object

### Attributes

<ParamField body="profile_uuid" type="string">
  A unique identifier for each profile.
</ParamField>

<ParamField body="profile_type" type="string">
  Indicates whether this is a primary or secondary profile.
</ParamField>

<ParamField body="primary_profile" type="string">
  A unique identifier for the account's primary profile.
</ParamField>

<ParamField body="profile_alias" type="string">
  A friendly name for the profile.
</ParamField>

<ParamField body="customer_type" type="string">
  Indicates the nature of your operations and how you use Plivo's voice and messaging offerings.
</ParamField>

<ParamField body="entity_type" type="string">
  Indicates ownership of the business.
</ParamField>

<ParamField body="company_name" type="string">
  Legal name of the company.
</ParamField>

<ParamField body="vertical" type="string">
  Company industry.
</ParamField>

<ParamField body="ein" type="string">
  Employer Identification Number.
</ParamField>

<ParamField body="ein_issuing_country" type="string">
  ISO country code of the country that issued the EIN.
</ParamField>

<ParamField body="address" type="object">
  Postal address of the company.
</ParamField>

<ParamField body="authorized_contact" type="object">
  Details of the authorized contact person at the company.
</ParamField>

<ParamField body="stock_symbol" type="string">
  Stock symbol of the company.
</ParamField>

<ParamField body="stock_exchange" type="string">
  Stock exchange where the company is listed.
</ParamField>

<ParamField body="alt_business_id" type="string">
  Alternate business identification number.
</ParamField>

<ParamField body="alt_business_id_type" type="string">
  Alternate business ID type.
</ParamField>

<ParamField body="website" type="string">
  Business website.
</ParamField>

<ParamField body="plivo_subaccount" type="string">
  Subaccount mapped to the profile.
</ParamField>

### Example Object

```json  theme={null}
{
    "profile": {
        "address": {
            "city": "New York",
            "country": "US",
            "postal_code": "10001",
            "state": "NY",
            "street": "123"
        },
        "alt_business_id": "ABC",
        "alt_business_id_type": "DUNS",
        "authorized_contact": {
            "email": "john@example.com",
            "first_name": "john",
            "last_name": "doe",
            "phone": "12125557777",
            "seniority": "admin",
            "title": "Doe"
        },
        "company_name": "ABC Inc.12345",
        "customer_type": "RESELLER",
        "ein": "12125552222",
        "ein_issuing_country": "US",
        "entity_type": "PUBLIC",
        "plivo_subaccount": "SA2025RK4E639VJFZAMM",
        "primary_profile": "c780f9d0-e3c9-4d13-87f7-b898654569b0",
        "profile_alias": "john_doe",
        "profile_type": "SECONDARY",
        "profile_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
        "stock_exchange": "NYSE",
        "stock_symbol": "HIBYE",
        "vertical": "ENTERTAINMENT",
        "website": "hibye.com"
    }
}
```

***

## Create a Profile

Create a business profile for your end customers.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Profile/
```

### Arguments

<ParamField body="profile_alias" type="string" required>
  A friendly name for your profile.
</ParamField>

<ParamField body="customer_type" type="string" required>
  Indicates the nature of your operations. Allowed values: `DIRECT`, `RESELLER`. Select `RESELLER` if your business provides communication services such as messaging and voice calling to other businesses.
</ParamField>

<ParamField body="entity_type" type="string" required>
  Indicates ownership of the company. Allowed values: `PRIVATE`, `PUBLIC`, `NON_PROFIT`, `GOVERNMENT`, `INDIVIDUAL`.
</ParamField>

<ParamField body="company_name" type="string" required>
  Legal name of the company.
</ParamField>

<ParamField body="vertical" type="string" required>
  Indicates industry. Allowed values: `PROFESSIONAL`, `REAL_ESTATE`, `HEALTHCARE`, `HUMAN_RESOURCES`, `ENERGY`, `ENTERTAINMENT`, `RETAIL`, `TRANSPORTATION`, `AGRICULTURE`, `INSURANCE`, `POSTAL`, `EDUCATION`, `HOSPITALITY`, `FINANCIAL`, `POLITICAL`, `GAMBLING`, `LEGAL`, `CONSTRUCTION`, `NGO`, `MANUFACTURING`, `GOVERNMENT`, `TECHNOLOGY`, `COMMUNICATION`.
</ParamField>

<ParamField body="address" type="object" required>
  Valid postal address of the company. Object fields: `street`, `city`, `state` (valid state code, e.g., TX for Texas), `postal_code` (ZIP code), `country` (ISO alpha-2 country code, e.g., US).
</ParamField>

<ParamField body="authorized_contact" type="object" required>
  Authorized contact person at the company. Object fields: `first_name`, `last_name`, `email`, `title` (salutation), `seniority` (allowed values: `DIRECTOR`, `GM`, `VP`, `CEO`, `CFO`, `GENERAL_COUNSEL`, `OTHER`), `phone` (E.164 format).
</ParamField>

<ParamField body="ein" type="string">
  Employer Identification Number. Plivo strongly recommends providing your EIN if your company is registered to unlock premium features like high throughput.
</ParamField>

<ParamField body="ein_issuing_country" type="string">
  The ISO country code of the country that issued the EIN.
</ParamField>

<ParamField body="stock_symbol" type="string">
  Stock symbol of the company.
</ParamField>

<ParamField body="stock_exchange" type="string">
  Stock exchange where your company is listed. Allowed values: `NASDAQ`, `NYSE`, `AMEX`, `AMX`, `ASX`, `B3`, `BME`, `BSE`, `FRA`, `ICEX`, `JPX`, `JSE`, `KRX`, `LON`, `NSE`, `OMX`, `SEHK`, `SGX`, `SSE`, `STO`, `SWX`, `SZSE`, `TSX`, `TWSE`, `VSE`, `OTHER`.
</ParamField>

<ParamField body="alt_business_id" type="string">
  Alternate business identification number.
</ParamField>

<ParamField body="alt_business_id_type" type="string">
  Alternate business ID type. Allowed values: `DUNS`, `LEI`, `GIIN`, `NONE`.
</ParamField>

<ParamField body="website" type="string">
  Website of the business.
</ParamField>

<ParamField body="plivo_subaccount" type="string">
  Subaccount mapped to the profile.
</ParamField>

<Note>
  If you specify `entity_type=INDIVIDUAL`, you can skip fields like `ein`, `ein_issuing_country`, `stock_symbol`, `stock_exchange`, `alt_business_id`, and `alt_business_id_type`.
</Note>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.profile.create(
      profile_alias="profile name sample",
      customer_type="DIRECT",
      entity_type="PRIVATE",
      company_name="ABC Inc.",
      ein="123456789",
      ein_issuing_country="US",
      stock_symbol="ABC",
      stock_exchange="NSE",
      website="www.example.com",
      vertical="REAL_ESTATE",
      alt_business_id="",
      alt_business_id_type="NONE",
      address={
          "street": "123",
          "city": "New York",
          "state": "NY",
          "postal_code": "10001",
          "country": "US"
      },
      authorized_contact={
          "first_name": "john",
          "last_name": "doe",
          "phone": "12025551234",
          "email": "john@example.com",
          "title": "Mr",
          "seniority": "admin"
      },
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>", "<auth_token>");

  const address = {
      street: "660 Broadway",
      city: "New York",
      state: "NY",
      postal_code: "10001",
      country: "US"
  };

  const authorizedContact = {
      first_name: "John",
      last_name: "Doe",
      email: "john@example.com",
      title: "manager",
      seniority: "admin",
      phone: "+12125551234"
  };

  client.profile.create(
      "my_profile",
      "",
      "DIRECT",
      "PRIVATE",
      "ABC Inc",
      "111111111",
      "PROFESSIONAL",
      "US",
      "ABC",
      "NASDAQ",
      "NONE",
      "example.com",
      address,
      authorizedContact
  ).then(console.log).catch(console.error);
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      -d '{
          "profile_alias": "john_new",
          "customer_type": "DIRECT",
          "entity_type": "PRIVATE",
          "company_name": "ABC Inc.",
          "vertical": "ENTERTAINMENT",
          "ein": "122321231",
          "ein_issuing_country": "US",
          "address": {
              "street": "660 Broadway",
              "city": "New York",
              "state": "NY",
              "postal_code": "10001",
              "country": "US"
          },
          "stock_symbol": "ABC",
          "stock_exchange": "NYSE",
          "alt_business_id_type": "DUNS",
          "alt_business_id": "ABC",
          "website": "example.com",
          "authorized_contact": {
              "first_name": "John",
              "last_name": "Doe",
              "email": "john@example.com",
              "title": "manager",
              "seniority": "admin",
              "phone": "12125551234"
          }
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Profile/
  ```
</CodeGroup>

```json Response theme={null}
{
    "api_id": "4e1f954c-baf3-11ec-bafe-0242ac110003",
    "message": "Profile created successfully.",
    "profile_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6"
}
```

***

## Retrieve a Profile

Fetch details about a specific profile associated with your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Profile/{profile_uuid}/
```

### Arguments

<ParamField path="profile_uuid" type="string" required>
  The unique identifier of the profile to retrieve.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.profile.get("<profile_uuid>")
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>", "<auth_token>");
  client.profile.get("<profile_uuid>")
      .then(console.log)
      .catch(console.error);
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      https://api.plivo.com/v1/Account/{auth_id}/Profile/{profile_uuid}/
  ```
</CodeGroup>

```json Response theme={null}
{
    "api_id": "752e99d0-baf3-11ec-ac74-0242ac110002",
    "profile": {
        "address": {
            "city": "New York",
            "country": "US",
            "postal_code": "10001",
            "state": "NY",
            "street": "123"
        },
        "alt_business_id": "ABC",
        "alt_business_id_type": "DUNS",
        "authorized_contact": {
            "email": "john@example.com",
            "first_name": "john",
            "last_name": "doe",
            "phone": "12125557777",
            "seniority": "admin",
            "title": "Doe"
        },
        "company_name": "ABC Inc.12345",
        "customer_type": "RESELLER",
        "ein": "12125552222",
        "ein_issuing_country": "US",
        "entity_type": "PUBLIC",
        "plivo_subaccount": "SAXXXXX",
        "primary_profile": "c780f9d0-e3c9-4d13-87f7-b898654569b0",
        "profile_alias": "john_doe",
        "profile_type": "SECONDARY",
        "profile_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
        "stock_exchange": "NYSE",
        "stock_symbol": "HIBYE",
        "vertical": "ENTERTAINMENT",
        "website": "hibye.com"
    }
}
```

***

## List All Profiles

Fetch all profiles created by your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Profile/
```

### Arguments

<ParamField query="limit" type="integer">
  Number of results per page. Maximum is 20. Default: 20.
</ParamField>

<ParamField query="offset" type="integer">
  Number of results to skip. Default: 0.
</ParamField>

<ParamField query="entity_type" type="string">
  Filter by entity type. Allowed values: `PRIVATE`, `PUBLIC`, `NON_PROFIT`, `GOVERNMENT`, `INDIVIDUAL`.
</ParamField>

<ParamField query="type" type="string">
  Filter by profile type. Allowed values: `PRIMARY`, `SECONDARY`.
</ParamField>

<ParamField query="vertical" type="string">
  Filter by vertical. Allowed values: `PROFESSIONAL`, `REAL_ESTATE`, `HEALTHCARE`, `HUMAN_RESOURCES`, `ENERGY`, `ENTERTAINMENT`, `RETAIL`, `TRANSPORTATION`, `AGRICULTURE`, `INSURANCE`, `POSTAL`, `EDUCATION`, `HOSPITALITY`, `FINANCIAL`, `POLITICAL`, `GAMBLING`, `LEGAL`, `CONSTRUCTION`, `NGO`, `MANUFACTURING`, `GOVERNMENT`, `TECHNOLOGY`, `COMMUNICATION`.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.profile.list(limit=10, offset=0)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>", "<auth_token>");
  client.profile.list({ limit: 10, offset: 0 })
      .then(console.log)
      .catch(console.error);
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      "https://api.plivo.com/v1/Account/{auth_id}/Profile/?limit=10&offset=0"
  ```
</CodeGroup>

```json Response theme={null}
{
    "api_id": "837b1e38-68a1-4fd6-a532-ea4jj888uuhh",
    "meta": {
        "limit": 10,
        "offset": 0,
        "next": "/v1/Account/<AUTH_ID>/Profile/?limit=10&offset=10",
        "previous": null
    },
    "profiles": [
        {
            "profile_uuid": "7a799f1a-5f44-43fb-ac82-999uujnnhhy",
            "profile_alias": "sample name",
            "profile_type": "SECONDARY",
            "primary_profile": "a7fe9aa3-dbca-401e-80a2-f88dudhdbhd",
            "customer_type": "DIRECT",
            "entity_type": "PRIVATE_PROFIT",
            "company_name": "Name of Company",
            "ein": "111111111",
            "ein_issuing_country": "US",
            "address": {
                "street": "660 Broadway",
                "city": "New York",
                "state": "NY",
                "postal_code": "10001",
                "country": "US"
            },
            "website": "www.example.com",
            "vertical": "COMMUNICATION",
            "plivo_subaccount": "SAXXXXX",
            "stock_symbol": "NSQ",
            "stock_exchange": "NASDAQ",
            "alt_business_id": "ABC",
            "alt_business_id_type": "DUNS",
            "authorized_contact": {
                "first_name": "First Name",
                "last_name": "Last Name",
                "phone": "919033998877",
                "email": "contact@example.com",
                "title": "Manager",
                "seniority": "Mr."
            },
            "created_at": "2023-10-17T20:57:54.164054Z"
        }
    ]
}
```

***

## Update a Profile

Update certain information in a profile.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Profile/{profile_uuid}/
```

### Arguments

<ParamField path="profile_uuid" type="string" required>
  The unique identifier of the profile to update.
</ParamField>

<ParamField body="entity_type" type="string">
  Ownership of the company. Allowed values: `PRIVATE`, `PUBLIC`, `NON_PROFIT`, `GOVERNMENT`, `INDIVIDUAL`.
</ParamField>

<ParamField body="company_name" type="string">
  Legal name of the company.
</ParamField>

<ParamField body="vertical" type="string">
  Company industry. Allowed values: `PROFESSIONAL`, `REAL_ESTATE`, `HEALTHCARE`, `HUMAN_RESOURCES`, `ENERGY`, `ENTERTAINMENT`, `RETAIL`, `TRANSPORTATION`, `AGRICULTURE`, `INSURANCE`, `POSTAL`, `EDUCATION`, `HOSPITALITY`, `FINANCIAL`, `POLITICAL`, `GAMBLING`, `LEGAL`, `CONSTRUCTION`, `NGO`, `MANUFACTURING`, `GOVERNMENT`, `TECHNOLOGY`, `COMMUNICATION`.
</ParamField>

<ParamField body="address" type="object">
  Postal address of the company.
</ParamField>

<ParamField body="authorized_contact" type="object">
  Details of the authorized contact person at the company.
</ParamField>

<ParamField body="website" type="string">
  Business website.
</ParamField>

<ParamField body="plivo_subaccount" type="string">
  Subaccount mapped to the profile.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  params = {"company_name": "New Company Name", "website": "www.example.com"}
  response = client.profile.update("<profile_uuid>", params)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>", "<auth_token>");
  const params = { company_name: "New Company Name" };
  client.profile.update("<profile_uuid>", params)
      .then(console.log)
      .catch(console.error);
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      -d '{
          "vertical": "ENTERTAINMENT",
          "company_name": "New Company Name"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Profile/{profile_uuid}/
  ```
</CodeGroup>

```json Response theme={null}
{
    "api_id": "752e99d0-baf3-11ec-ac74-0242ac110002",
    "profile": {
        "address": {
            "city": "New York",
            "country": "US",
            "postal_code": "10001",
            "state": "NY",
            "street": "123"
        },
        "alt_business_id": "ABC",
        "alt_business_id_type": "DUNS",
        "authorized_contact": {
            "email": "john@example.com",
            "first_name": "john",
            "last_name": "doe",
            "phone": "12125557778",
            "seniority": "admin",
            "title": "Doe"
        },
        "company_name": "New Company Name",
        "customer_type": "RESELLER",
        "ein": "12125552222",
        "ein_issuing_country": "US",
        "entity_type": "PUBLIC",
        "plivo_subaccount": "SA2025RK4E639VJFZAMM",
        "primary_profile": "c780f9d0-e3c9-4d13-87f7-b898654569b0",
        "profile_alias": "john_doe",
        "profile_type": "SECONDARY",
        "profile_uuid": "f19c4773-4ae6-4b75-92ea-9cf3ea4227d6",
        "stock_exchange": "NYSE",
        "stock_symbol": "HIBYE",
        "vertical": "ENTERTAINMENT",
        "website": "hibye.com"
    }
}
```

***

## Delete a Profile

Delete a specific profile from your account. This action is irreversible. You cannot delete the primary profile of an account.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Profile/{profile_uuid}/
```

### Arguments

<ParamField path="profile_uuid" type="string" required>
  The unique identifier of the profile to delete.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.profile.delete(profile_uuid="<profile_uuid>")
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>", "<auth_token>");
  client.profile.delete("<profile_uuid>")
      .then(console.log)
      .catch(console.error);
  ```

  ```bash cURL theme={null}
  curl -X DELETE -i --user auth_id:auth_token \
      https://api.plivo.com/v1/Account/{auth_id}/Profile/{profile_uuid}/
  ```
</CodeGroup>

```json Response theme={null}
{
    "api_id": "aaf7717a-c149-11ec-a932-0242ac110003",
    "message": "Profile deleted successfully."
}
```
