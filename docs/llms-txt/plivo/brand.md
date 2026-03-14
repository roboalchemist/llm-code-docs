# Source: https://plivo.com/docs/messaging/api/10dlc/brand.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Brand

> Register and manage 10DLC brands

Register brands for your or your customers' businesses to enable 10DLC messaging campaigns. A brand represents the business entity that will be sending messages.

<Note>
  Starter brand registrations are currently paused. See [10DLC Starter Paused](https://www.plivo.com/blog/10dlc-starter-paused/) for more information.
</Note>

***

## API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/10dlc/Brand/
```

***

## The Brand Object

<ParamField body="brand_id" type="string">
  Unique identifier for the brand created.
</ParamField>

<ParamField body="brand_alias" type="string">
  A friendly name for the brand.
</ParamField>

<ParamField body="brand_type" type="string">
  Type of registration indicated during brand creation. Values: `STANDARD`, `STARTER`.
</ParamField>

<ParamField body="company_name" type="string">
  Legal name of the company.
</ParamField>

<ParamField body="ein" type="string">
  Employer Identification Number associated with a Standard brand.
</ParamField>

<ParamField body="ein_issuing_country" type="string">
  ISO alpha-2 code for the country that issued the EIN.
</ParamField>

<ParamField body="entity_type" type="string">
  Type of ownership indicated during brand creation.
</ParamField>

<ParamField body="vertical" type="string">
  Company industry.
</ParamField>

<ParamField body="profile_uuid" type="string">
  Unique identifier for the profile used to create brand.
</ParamField>

<ParamField body="registration_status" type="string">
  Indicates status of brand.
</ParamField>

<ParamField body="vetting_score" type="integer">
  Vetting score assigned to brand by TCR.
</ParamField>

<ParamField body="vetting_status" type="string">
  Vetting status of a brand.
</ParamField>

<ParamField body="address" type="object">
  Postal address indicated during brand creation. Contains `street`, `city`, `state`, `postal_code`, and `country`.
</ParamField>

<ParamField body="authorized_contact" type="object">
  Authorized contact information indicated during brand creation. Contains `first_name`, `last_name`, `email`, `phone`, `title`, and `seniority`.
</ParamField>

### Example Object

```json  theme={null}
{
  "brand": {
    "address": {
      "city": "New York",
      "country": "US",
      "postal_code": "10001",
      "state": "NY",
      "street": "123"
    },
    "authorized_contact": {
      "email": "john@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "phone": "+12125557777",
      "seniority": "admin",
      "title": "Doe"
    },
    "brand_id": "BCDEF1G",
    "brand_type": "STANDARD",
    "company_name": "ABC Inc.",
    "ein": "111111111",
    "ein_issuing_country": "US",
    "entity_type": "PRIVATE_PROFIT",
    "profile_uuid": "09849948-656a-41a2-99da-8370251c804b",
    "registration_status": "COMPLETED",
    "vertical": "ENERGY",
    "vetting_score": 80,
    "vetting_status": "ACTIVE"
  }
}
```

***

## Register a Standard Brand

This API lets you register a standard brand using a preexisting profile.

```
POST https://api.plivo.com/v1/Account/{auth_id}/10dlc/Brand/
```

### Arguments

<ParamField body="profile_uuid" type="string" required>
  Unique identifier for the profile that you want to use for creating a brand. The profile should not have been used to create another brand.
</ParamField>

<ParamField body="brand_alias" type="string" required>
  A friendly name for the brand.
</ParamField>

<ParamField body="brand_type" type="string">
  Indicate type of registration. Allowed values: `STANDARD`, `STARTER`. STANDARD not allowed for profiles not containing an EIN. Defaults to `STARTER`.
</ParamField>

<ParamField body="secondary_vetting" type="boolean">
  Allowed values: `true`, `false`. Only applicable for STANDARD registration. Defaults to `true`. Plivo strongly recommends opting for vetting to get the highest throughput for your brands and campaigns.
</ParamField>

<ParamField body="url" type="string">
  The fully qualified URL to which status update callbacks for the message should be sent.
</ParamField>

<ParamField body="method" type="string">
  The HTTP method to be used when calling the URL defined above. Allowed values: `GET`, `POST`. Defaults to `POST`.
</ParamField>

### Returns

Returns `api_id` for the request, unique `brand_id`, and success message.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.brand.create(
      brand_alias="brand name sample",
      brand_type="STANDARD",
      profile_uuid="7bc67ed6-dc92-4958-9acc-e4fdb09bd923",
      secondary_vetting=False,
      url="https://example.com/test",
      method="POST",
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  var callback = {"url":"https://<yourdomain>.com/tendlc_status/", "method":"POST"}

  client.brand.create("govt", "<profile_uuid>", "STANDARD", true, callback)
      .then(function (response) {
          console.log(JSON.stringify(response));
      }).catch(function (error) {
          console.log("err");
          console.log(error);
      });
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      -d '{
              "brand_alias": "gov234t",
              "profile_uuid": "d61eaaaa-18b1-4473-8810-0b9d80573aa9",
              "brand_type": "STANDARD",
              "secondary_vetting": true,
              "url": "https://<yourdomain>.com/tendlc_status/",
              "method": "POST"
          }' \
          https://api.plivo.com/v1/Account/{auth_id}/10dlc/Brand/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "5df3fffa-64ab-11ed-b94d-0242ac110002",
  "brand_id": "BB9TT3V",
  "message": "Request to create brand was received and is being processed."
}
```

***

## Retrieve a Brand

This API lets you fetch details about a specific brand associated with your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/10dlc/Brand/{brand_id}/
```

### Arguments

No arguments need to be passed.

### Returns

Returns `api_id` and the brand object identified by the `brand_id` specified in the request URL.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.brand.get("<brand_id>")
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  client.brand.get("<brand_id>")
      .then(function (response) {
          console.log(JSON.stringify(response));
      }).catch(function (error) {
          console.log("err");
          console.log(error);
      });
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Brand/{brand_id}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "0215c238-1701-11ed-9d48-0242ac110003",
  "brand": {
    "address": {
      "city": "New York",
      "country": "IN",
      "postal_code": "10001",
      "state": "NY",
      "street": "123"
    },
    "authorized_contact": {
      "email": "test@plivo.com",
      "first_name": "John",
      "last_name": "Doe",
      "phone": "1890342302",
      "seniority": "admin",
      "title": "Doe"
    },
    "brand_id": "BVMN1EM",
    "brand_type": "STARTER",
    "ein_issuing_country": "IN",
    "entity_type": "PRIVATE",
    "profile_uuid": "dd0b418d-73df-4eb4-a7ab-171b774bf4a9",
    "registration_status": "COMPLETED",
    "vertical": "ENERGY",
    "website": "www.google.com"
  }
}
```

***

## List All Brands

This API lets you fetch all the brands associated with an account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/10dlc/Brand/
```

### Arguments

<ParamField query="limit" type="integer">
  Denotes the number of results per page. The maximum number of results that can be fetched is 20. Defaults to 20.
</ParamField>

<ParamField query="offset" type="integer">
  Denotes the number of value items by which the results should be offset. Defaults to 0.
</ParamField>

<ParamField query="registration_status" type="string">
  Filter by registration\_status. Allowed values: `FAILED`, `PROCESSING`, `COMPLETED`.
</ParamField>

<ParamField query="type" type="string">
  Filter by registration type. Allowed values: `STARTER`, `STANDARD`.
</ParamField>

### Returns

Returns `api_id` and a dictionary with an objects property that contains up to 20 brands. Each tuple in the list is a separate Brand object.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.brand.list(limit=1, offset=0)
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  client.brand.list()
      .then(function (response) {
          console.log(JSON.stringify(response));
      }).catch(function (error) {
          console.log("err");
          console.log(error);
      });
  ```

  ```bash cURL theme={null}
  curl -i --user auth_id:auth_token \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Brand/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "553379bc-6c9a-4f5d-8e8f-e0999euejene8",
  "meta": {
    "limit": 1,
    "offset": 0,
    "next": "/v1/Account/<AUTH_ID>/10dlc/Brand/?limit=1&offset=1",
    "previous": null,
    "total_count": 45
  },
  "brands": [
    {
      "brand_alias": "sample name",
      "brand_id": "BXXXXX",
      "brand_type": "STANDARD",
      "company_name": "sample company",
      "ein": "123456789",
      "ein_issuing_country": "US",
      "entity_type": "PUBLIC",
      "profile_uuid": "7b8ff904-a1d2-46b2-888d-34d4df4cf95a",
      "registration_status": "COMPLETED",
      "vertical": "COMMUNICATION",
      "vetting_score": 80,
      "vetting_status": "ACTIVE",
      "website": "www.samplewebsite.com",
      "Address": {
        "city": "Dallas",
        "country": "US",
        "postal_code": "10001",
        "state": "Texas",
        "street": "#11, Nashville Street"
      },
      "Authorized_contact": {
        "email": "xxxx@gmail.com",
        "first_name": "John",
        "last_name": "Doe",
        "phone": "14845355113",
        "seniority": "Admin",
        "title": "Mr"
      },
      "created_at": "2023-03-06T20:59:26.040592Z"
    }
  ]
}
```

***

## Delete a Brand

Deletes a particular 10DLC brand from your account. This action is irreversible and is only allowed for brands with no associated active campaigns.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/10dlc/Brand/{brand_id}/
```

### Arguments

No arguments need to be passed.

### Returns

Returns `api_id`, `brand_id`, and a confirmation (or error message).

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.brand.delete(brand_id='<brand_id>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  client.brand.deleteBrand("<brand_id>").then(function(response) {
      console.log(JSON.stringify(response));
  }).catch(function(error) {
      console.log("err");
      console.log(error);
  });
  ```

  ```bash cURL theme={null}
  curl --location --request DELETE 'https://api.plivo.com/v1/Account/<auth_id>/10dlc/Brand/<brand_id>/' \
      --header 'Authorization: Basic XXXX=='
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "785ed2dc-7493-11ed-97ac-0242ac110003",
  "brand_id": "BCHVILW",
  "message": "Brand Deactivated"
}
```

***

## Get Brand Use Cases

Fetches details about what kind of campaigns are supported under a particular brand ID.

```
GET https://api.plivo.com/v1/Account/{auth_id}/10dlc/Brand/{brand_id}/usecases/
```

### Arguments

No arguments need to be passed.

### Returns

Returns `api_id`, `brand_id`, and a list containing all the types of campaign types allowed for the brand.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.brand.get_usecases(brand_id='<brand_id>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  client.brand.get_usecases("<brand_id>")
      .then(function (response) {
          console.log(JSON.stringify(response));
      }).catch(function (error) {
          console.log("err");
          console.log(error);
      });
  ```

  ```bash cURL theme={null}
  curl --location --request GET 'https://api.plivo.com/v1/Account/<auth_id>/10dlc/Brand/<brand_id>/usecases/' \
      --header 'Authorization: Basic XXXX=='
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "0db62668-5f2d-11ed-bee0-0242ac110002",
  "brand_id": "BJZN6KW",
  "use_cases": [
    {
      "code": "2FA",
      "details": "Any two-factor authentication with passcodes used to unlock accounts",
      "name": "Two-Factor Authentication"
    },
    {
      "code": "ACCOUNT_NOTIFICATION",
      "details": "Notification sent to account holders about changes in accounts",
      "name": "Account Notification"
    },
    {
      "code": "CUSTOMER_CARE",
      "details": "Customer care interactions by the support and other customer-facing teams",
      "name": "Customer Care"
    },
    {
      "code": "DELIVERY_NOTIFICATION",
      "details": "Updates about the delivery of products and services",
      "name": "Delivery Notification"
    },
    {
      "code": "FRAUD_ALERT",
      "details": "Notifications of suspicious behavior identified the business",
      "name": "Fraud Alert"
    },
    {
      "code": "HIGHER_EDUCATION",
      "details": "Messages sent by colleges, universities, and other educational institutions",
      "name": "Higher Education"
    },
    {
      "code": "LOW_VOLUME",
      "details": "A combination of two to five standard usage cases - for low throughput requirements",
      "name": "Low Volume"
    },
    {
      "code": "MARKETING",
      "details": "Communications related to time-bound events and sales",
      "name": "Marketing"
    },
    {
      "code": "MIXED",
      "details": "A combination of two to five standard usage cases",
      "name": "Mixed"
    },
    {
      "code": "POLLING_VOTING",
      "details": "Surveys, polling, and voting campaigns used for non-political purposes",
      "name": "Polling Voting"
    },
    {
      "code": "PUBLIC_SERVICE_ANNOUNCEMENT",
      "details": "Messages aimed at creating awareness about important topics",
      "name": "Public Service Announcement"
    },
    {
      "code": "SECURITY_ALERT",
      "details": "Notifications that alert users about a potential breach of systems",
      "name": "Security Alert"
    }
  ]
}
```
