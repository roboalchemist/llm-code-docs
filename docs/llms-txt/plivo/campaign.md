# Source: https://plivo.com/docs/messaging/api/10dlc/campaign.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Campaign

> Register and manage 10DLC campaigns

Register campaigns for your messaging use cases. Campaigns define the purpose and content of your 10DLC messaging and must be associated with a registered brand.

***

## API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/
```

***

## The Campaign Object

<ParamField body="brand_id" type="string">
  The brand\_id associated with the campaign.
</ParamField>

<ParamField body="campaign_id" type="string">
  Unique identifier for the campaign created.
</ParamField>

<ParamField body="campaign_alias" type="string">
  A friendly name for your campaign. This name appears on the Plivo console.
</ParamField>

<ParamField body="campaign_attributes" type="object">
  Tuple indicating status of the following attributes that were specified at the time of campaign creation: `affiliate_marketing`, `age_gated`, `direct_lending`, `embedded_link`, `embedded_phone`, `subscriber_help`, `subscriber_optin`, `subscriber_optout`.
</ParamField>

<ParamField body="description" type="string">
  A brief description of the campaign and how it's relevant to your business.
</ParamField>

<ParamField body="registration_status" type="string">
  Indicates status of a campaign.
</ParamField>

<ParamField body="usecase" type="string">
  Use case used to create the campaign.
</ParamField>

<ParamField body="sub_usecases" type="array">
  Sub-use cases used to create mixed campaigns.
</ParamField>

<ParamField body="sample1" type="string">
  Sample message indicated at campaign creation time. Campaign creation requires at least two sample messages.
</ParamField>

<ParamField body="sample2" type="string">
  Sample message indicated at campaign creation time. Campaign creation requires at least two sample messages.
</ParamField>

<ParamField body="mno_metadata" type="object">
  Tuple containing allowed transactions per minute (TPM) and brand\_tier (specific to T-Mobile transactions per day (TPD)).
</ParamField>

<ParamField body="message_flow" type="string">
  A brief description of how a customer opts in to the campaign and provides consent to the sender to receive their messages.
</ParamField>

<ParamField body="help_message" type="string">
  Response to HELP keyword on this campaign's numbers.
</ParamField>

<ParamField body="optin_message" type="string">
  Message sent to subscribers to confirm their opt-in to the campaign.
</ParamField>

<ParamField body="optout_message" type="string">
  Response to STOP keyword on this campaign's numbers.
</ParamField>

<ParamField body="optin_keywords" type="string">
  Opt-in keyword(s) associated with the campaign. If more than one, provide a comma-separated list with no special characters or embedded spaces.
</ParamField>

<ParamField body="optout_keywords" type="string">
  Opt-out keyword(s) associated with the campaign. If more than one, provide a comma-separated list with no special characters or embedded spaces.
</ParamField>

<ParamField body="help_keywords" type="string">
  Help keyword(s) associated with the campaign. If more than one, provide a comma-separated list with no special characters or embedded spaces.
</ParamField>

<ParamField body="campaign_source" type="string">
  Indicates how a campaign has been created. If you have created this campaign on Plivo, campaign\_source will be `plivo`. If you have created a campaign directly on TCR and imported to Plivo, campaign\_source will be `shared`.
</ParamField>

### Example Object

```json  theme={null}
{
    "api_id": "497b1284-3a49-11ed-a2ca-0242ac110004",
    "campaign": {
        "brand_id": "BHXDNDJ",
        "campaign_id": "CZISKSM",
        "mno_metadata": {
            "at&t": {
                "tpm": "4500",
                "brand_tier": null
            },
            "t-mobile": {
                "tpm": null,
                "brand_tier": "TOP"
            },
            "us cellular": {
                "tpm": "4500",
                "brand_tier": null
            },
            "verizon wireless": {
                "tpm": "4500",
                "brand_tier": null
            }
        },
        "reseller_id": "",
        "usecase": "MIXED",
        "sub_usecase": "CUSTOMER_CARE,2FA",
        "message_flow": "Message flow is a mandatory parameter, minimum 40 characters",
        "optin_keywords": "YES, SUBSCRIBE, TRUE",
        "optin_message": "Opt-in message should have a minimum of 20 characters",
        "optout_keywords": "NO, STOP",
        "optout_message": "Opt-out message should have a minimum of 20 characters",
        "help_keywords": "HELP, INFO, MORE",
        "help_message": "Help message is a mandatory parameter, minimum 20 characters"
    }
}
```

***

## Register a Campaign

This API lets you register a campaign using a preexisting brand.

```
POST https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/
```

### Arguments

<ParamField body="campaign_alias" type="string" required>
  A friendly name for your campaign. This name appears on the Plivo console.
</ParamField>

<ParamField body="brand_id" type="string" required>
  ID of the brand for which campaign creation request is being submitted.
</ParamField>

<ParamField body="vertical" type="string" required>
  Indicates the industry specific to the message use case. Allowed values: `PROFESSIONAL`, `REAL_ESTATE`, `HEALTHCARE`, `HUMAN_RESOURCES`, `ENERGY`, `ENTERTAINMENT`, `RETAIL`, `TRANSPORTATION`, `AGRICULTURE`, `INSURANCE`, `POSTAL`, `EDUCATION`, `HOSPITALITY`, `FINANCIAL`, `POLITICAL`, `GAMBLING`, `LEGAL`, `CONSTRUCTION`, `NGO`, `MANUFACTURING`, `GOVERNMENT`, `TECHNOLOGY`, `COMMUNICATION`.
</ParamField>

<ParamField body="description" type="string" required>
  A brief description of the campaign and how it's relevant to your business - minimum of 40 characters.
</ParamField>

<ParamField body="usecase" type="string" required>
  Indicates your messaging use case. Allowed values: `2FA`, `ACCOUNT_NOTIFICATION`, `CUSTOMER_CARE`, `DELIVERY_NOTIFICATION`, `FRAUD_ALERT`, `HIGHER_EDUCATION`, `LOW_VOLUME`, `MARKETING`, `MIXED`, `POLLING_VOTING`, `PUBLIC_SERVICE_ANNOUNCEMENT`, `SECURITY_ALERT`, `STARTER`. STARTER brands can only use `STARTER` as their use case.
</ParamField>

<ParamField body="sample1" type="string" required>
  The content of a sample message that you will send through this campaign. You must provide at least two samples, each with a minimum of 20 characters.
</ParamField>

<ParamField body="sample2" type="string" required>
  The content of the second sample message.
</ParamField>

<ParamField body="subscriber_optin" type="boolean" required>
  A confirmation that you are collecting and processing customer opt-ins. Allowed value: `true`.
</ParamField>

<ParamField body="subscriber_optout" type="boolean" required>
  A confirmation that you are collecting and processing customer opt-outs. Allowed value: `true`.
</ParamField>

<ParamField body="subscriber_help" type="boolean" required>
  A confirmation that you have implemented a message reply that tells customers how they can contact the message sender when they reply with the "HELP" keyword. Allowed value: `true`.
</ParamField>

<ParamField body="direct_lending" type="boolean" required>
  Indicates whether this campaign includes content related to direct lending or other loan arrangements. Allowed values: `true`, `false`.
</ParamField>

<ParamField body="embedded_link" type="boolean" required>
  Indicates whether embedded links are being used. Operators do not accept public URL shorteners. Allowed values: `true`, `false`.
</ParamField>

<ParamField body="embedded_phone" type="boolean" required>
  Indicates whether the campaign is using an embedded phone number other than the required HELP contact number. Allowed values: `true`, `false`.
</ParamField>

<ParamField body="age_gated" type="boolean" required>
  Indicates whether the campaign includes any age-gated content as defined by operator and CTIA guidelines. Allowed values: `true`, `false`.
</ParamField>

<ParamField body="affiliate_marketing" type="boolean" required>
  Indicates whether affiliate marketing was used in the construction of this campaign. Allowed values: `true`, `false`.
</ParamField>

<ParamField body="sub_usecases" type="array">
  Only applicable when use case is `STARTER`, `MIXED`, or `LOW_VOLUME`. Indicates two to five comma-separated use cases. Allowed values: `2FA`, `ACCOUNT_NOTIFICATION`, `CUSTOMER_CARE`, `DELIVERY_NOTIFICATION`, `FRAUD_ALERT`, `HIGHER_EDUCATION`, `MARKETING`, `POLLING_VOTING`, `PUBLIC_SERVICE_ANNOUNCEMENT`, `SECURITY_ALERT`.
</ParamField>

<ParamField body="message_flow" type="string" required>
  Describes how a customer opts in to a campaign, thereby giving consent to the sender to send messages. The message flow must be clear and inform customers about the nature of the campaign. If a campaign supports multiple opt-in mechanisms, you must mention all of them here. Check [documentation](https://docs.plivo.com/docs/messaging/a2p-10dlc/registration-guidelines) for samples.
</ParamField>

<ParamField body="help_message" type="string" required>
  Indicates the response to the HELP keyword. It may include the brand name and support contact information. Check [documentation](https://docs.plivo.com/docs/messaging/a2p-10dlc/registration-guidelines) for samples.
</ParamField>

<ParamField body="optout_message" type="string" required>
  Indicates the response to the STOP keyword. It must include acknowledgement of the opt-out request and confirmation that no further messages will be sent, and may include the brand name. Check [documentation](https://docs.plivo.com/docs/messaging/a2p-10dlc/registration-guidelines) for samples.
</ParamField>

<ParamField body="optin_message" type="string">
  Message sent to subscribers to confirm their opt-in to the campaign.
</ParamField>

<ParamField body="optin_keywords" type="string">
  Opt-in keywords associated with the campaign. If more than one, provide a comma-separated list with no special characters or embedded spaces.
</ParamField>

<ParamField body="help_keywords" type="string">
  Help keywords associated with the campaign, in all capital letters. If more than one, provide a comma-separated list with no special characters or embedded spaces.
</ParamField>

<ParamField body="url" type="string">
  The fully qualified URL to which status update callbacks for the message should be sent.
</ParamField>

<ParamField body="method" type="string">
  The HTTP method to be used when calling the URL defined above. Allowed values: `GET`, `POST`. Defaults to `POST`.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  sub_usecase = ["CUSTOMER_CARE", "2FA"]
  response = client.campaign.create(
      brand_id="<brand_id>",
      campaign_alias="campaign_sample message",
      vertical="INSURANCE",
      usecase="MIXED",
      sub_usecases=sub_usecase,
      description="Campaign description is a mandatory parameter, minimum 40 characters",
      embedded_link=False,
      embedded_phone=False,
      age_gated=False,
      subscriber_optin=True,
      subscriber_optout=True,
      subscriber_help=True,
      affiliate_marketing=False,
      sample1="Sample message 1 should have a minimum of 20 characters",
      sample2="Sample message 2 should have a minimum of 20 characters",
      url="https://<yoursite>.com/test",
      method="POST",
      message_flow="Message flow is a mandatory parameter, minimum 40 characters",
      help_keywords="HELP,INFO,MORE",
      help_message="Help message is a mandatory parameter, minimum 20 characters",
      optin_keywords="YES,SUBSCRIBE",
      optin_message="Opt-in message should have a minimum of 20 characters",
      optout_keywords="NO,STOP",
      optout_message="Opt-out message should have a minimum of 20 characters",
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  var callback = {
      "url": "http://example.com/callback",
      "method": "POST",
      "optout_keywords": "NO,STOP",
      "optin_keywords": "YES,SUBSCRIBE",
      "help_keywords": "HELP,INFO,MORE",
      "optin_message": "Opt-in message should have a minimum of 20 characters"
  };

  client.campaign.create(
      "<brand_id>",
      "campaign name",
      "INSURANCE",
      "MIXED",
      ["CUSTOMER_CARE", "2FA"],
      "sample description text should 40 character following attributes",
      false,
      false,
      false,
      false,
      true,
      true,
      true,
      true,
      "Sample message 1 should have a minimum of 20 characters",
      "Sample message 2 should have a minimum of 20 characters",
      "Message flow is a mandatory parameter, minimum 40 characters",
      "Help message is a mandatory parameter, minimum 20 characters",
      "Opt-out message should have a minimum of 20 characters",
      callback
  ).then(function(response) {
      console.log(JSON.stringify(response));
  }).catch(function(error) {
      console.log(error);
  });
  ```

  ```curl cURL theme={null}
  curl -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      -d '{
              "brand_id": "{brand_id}",
              "vertical": "INSURANCE",
              "usecase": "MIXED",
              "sub_usecases":["2FA","ACCOUNT_NOTIFICATION", "CUSTOMER_CARE", "DELIVERY_NOTIFICATION", "FRAUD_ALERT"],
              "description": "OTP registration",
              "direct_lending": true,
              "affiliate_marketing": false,
              "embedded_link": false,
              "embedded_phone": false,
              "age_gated": false,
              "subscriber_optin": true,
              "subscriber_optout": true,
              "subscriber_help": true,
              "sample1": "Your OTP is 1234",
              "sample2": "Your order {ID} is out for delivery",
              "url": "https://<yourdomain>.com/tendlc_status/",
              "method": "POST"
          }' \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "apiId": "a640fba2-3b14-11ed-95d8-0242ac110004",
    "campaignId": "CVWMV6V",
    "message": "Request to create campaign was received and is being processed."
}
```

***

## Retrieve a Campaign

This API lets you fetch details about a specific campaign associated with your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/
```

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.campaign.get("<campaign_id>")
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  client.campaign.get("<campaign_id>")
      .then(function(response) {
          console.log(JSON.stringify(response));
      }).catch(function(error) {
          console.log(error);
      });
  ```

  ```curl cURL theme={null}
  curl -i --user auth_id:auth_token \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "4dea744b-7b9b-4525-a380-d2b2c26c523c",
    "campaign": {
        "campaign_id": "CY5JZZZ",
        "registration_status": "ACTIVE",
        "reseller_id": "",
        "brand_id": "BOANNZO",
        "usecase": "CUSTOMER_CARE",
        "campaign_alias": "campaign name",
        "mno_metadata": {
            "AT&T": {
                "tpm": 4500
            },
            "T-Mobile": {
                "brand_tier": "TOP"
            },
            "US Cellular": {
                "tpm": 4500
            },
            "Verizon Wireless": {
                "tpm": 4500
            }
        },
        "sample1": "You can confirm by responding to this text or by logging into the customer portal.",
        "sample2": "Your next scheduled deposit is on [Deposit Date]",
        "description": "We use this campaign for customer care communications for opted in customers.",
        "campaign_attributes": {
            "embedded_link": true,
            "embedded_phone": true,
            "age_gated": false,
            "direct_lending": false,
            "subscriber_optin": true,
            "subscriber_optout": true,
            "subscriber_help": true,
            "affiliate_marketing": false
        },
        "message_flow": "Customer opts in by sending an inbound YES message.",
        "help_message": "Reply YES to receive text communications, STOP to opt out. Call [Company Phone] for support. Msg rates may apply.",
        "optout_message": "You will not receive any more text communications. Reply YES to subscribe.",
        "created_at": "2023-04-04T15:21:01.064199Z",
        "vertical": "ENTERTAINMENT",
        "campaign_source": "plivo"
    }
}
```

***

## List All Campaigns

This API lets you fetch all the campaigns associated with an account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/
```

### Query Parameters

<ParamField query="limit" type="integer">
  Denotes the number of results per page. The maximum number of results that can be fetched is 20. Defaults to 20.
</ParamField>

<ParamField query="offset" type="integer">
  Denotes the number of value items by which the results should be offset. Defaults to 0. Read more about [offset-based pagination](https://docs.plivo.com/docs/messaging/api/request/pagination).
</ParamField>

<ParamField query="usecase" type="string">
  Filter by use case. Allowed values: `2FA`, `ACCOUNT_NOTIFICATION`, `CUSTOMER_CARE`, `DELIVERY_NOTIFICATION`, `FRAUD_ALERT`, `HIGHER_EDUCATION`, `LOW_VOLUME`, `MARKETING`, `MIXED`, `POLLING_VOTING`, `PUBLIC_SERVICE_ANNOUNCEMENT`, `SECURITY_ALERT`, `STARTER`.
</ParamField>

<ParamField query="brand_id" type="string">
  Filters results by a brand\_id.
</ParamField>

<ParamField query="registration_status" type="string">
  Filter by registration status of a campaign. Allowed values: `Active`, `Failed`, `Processing`, `Expired`.
</ParamField>

<ParamField query="campaign_source" type="string">
  Filters results by campaign source. Allowed values: `plivo`, `shared`.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.campaign.list(limit=20, offset=0)
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  client.campaign.list({
          limit: 20,
          offset: 0
      })
      .then(function(response) {
          console.log(JSON.stringify(response));
      }).catch(function(error) {
          console.log(error);
      });
  ```

  ```curl cURL theme={null}
  curl -i --user auth_id:auth_token \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "f5013b11-8d0e-4156-b7a2-feeea076b6fb",
    "meta": {
        "limit": 1,
        "offset": 0,
        "next": "/v1/Account/<auth_id>/10dlc/Campaign/?limit=1&offset=1",
        "previous": null,
        "total_count": 16
    },
    "campaigns": [
        {
            "campaign_id": "CY2UXXX",
            "registration_status": "FAILED",
            "reseller_id": "",
            "brand_id": "BANGXXX",
            "usecase": "2FA",
            "campaign_alias": "campaign name",
            "mno_metadata": {
                "AT&T": {
                    "tpm": 4500
                },
                "T-Mobile": {
                    "brand_tier": "TOP"
                },
                "US Cellular": {
                    "tpm": 4500
                },
                "Verizon Wireless": {
                    "tpm": 4500
                }
            },
            "sample1": "Your one-time passcode is {{6 DIGIT CODE}}. Please do not reply to this message.",
            "sample2": "Your one-time passcode is {{6 DIGIT CODE}}.",
            "description": "We use this campaign to send multi factor authentication 6 digit codes to end users and customers.",
            "campaign_attributes": {
                "embedded_link": false,
                "embedded_phone": false,
                "age_gated": false,
                "direct_lending": false,
                "subscriber_optin": true,
                "subscriber_optout": true,
                "subscriber_help": true,
                "affiliate_marketing": false
            },
            "message_flow": "Agents and customers using our service daily. Agents login required to validate the MFA code. Customers login required to validate the MFA code.",
            "help_message": "Please call {800 number} if you're having issues with login.",
            "optout_message": "You are not going to receive MFA codes by SMS moving forward.",
            "created_at": "2023-09-25T20:36:00.83971Z",
            "vertical": "ENTERTAINMENT",
            "campaign_source": "plivo"
        }
    ]
}
```

***

## Update a Campaign

Update a 10DLC campaign from your account. This action is only allowed for campaigns that failed to register previously - that is, current registration\_status = `failed`.

Note that updating a campaign submits it for another vetting review with the carriers at a cost of \$15. See our [10DLC support page](https://support.plivo.com/hc/en-us/articles/18193205054361) for more details on vetting.

Please note that updates to campaigns will be allowed when the registration\_status is set to processing. However, in some cases, when the registration\_status is in the processing stage, updates to campaigns will not be allowed (via console) or may result in an error through the API, as the campaign may be undergoing carrier approval with the registry.

```
POST https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/
```

### Arguments

You can update only these fields of a campaign. You can pass one or more of the fields during the update.

<ParamField body="campaign_alias" type="string">
  A friendly name for your campaign. This name appears on the Plivo console.
</ParamField>

<ParamField body="description" type="string">
  A brief description of the campaign and how it's relevant to your business - minimum of 40 characters.
</ParamField>

<ParamField body="sample1" type="string">
  The content of a sample message that you will send through this campaign. You must provide at least two samples, each with a minimum of 20 characters.
</ParamField>

<ParamField body="sample2" type="string">
  The content of the second sample message.
</ParamField>

<ParamField body="message_flow" type="string">
  Describes how a customer opts in to a campaign, thereby giving consent to the sender to send messages. The message flow must be clear and inform customers about the nature of the campaign. If a campaign supports multiple opt-in mechanisms, you must mention all of them here. Check [documentation](https://docs.plivo.com/docs/messaging/a2p-10dlc/registration-guidelines) for samples.
</ParamField>

<ParamField body="help_message" type="string">
  Indicates the response to the HELP keyword. It may include the brand name and support contact information. Check [documentation](https://docs.plivo.com/docs/messaging/a2p-10dlc/registration-guidelines) for samples.
</ParamField>

<ParamField body="optout_message" type="string">
  Indicates the response to the STOP keyword. It must include acknowledgement of the opt-out request and confirmation that no further messages will be sent, and may include the brand name. Check [documentation](https://docs.plivo.com/docs/messaging/a2p-10dlc/registration-guidelines) for samples.
</ParamField>

<ParamField body="optout_keywords" type="string">
  Opt-out keywords associated with the campaign. If more than one, provide a comma-separated list with no special characters or embedded spaces.
</ParamField>

<ParamField body="optin_message" type="string">
  Message sent to subscribers to confirm their opt-in to the campaign.
</ParamField>

<ParamField body="optin_keywords" type="string">
  Opt-in keywords associated with the campaign. If more than one, provide a comma-separated list with no special characters or embedded spaces.
</ParamField>

<ParamField body="help_keywords" type="string">
  Help keywords associated with the campaign, in all capital letters. If more than one, provide a comma-separated list with no special characters or embedded spaces.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.campaign.update(
      '<campaign_id>',
      sample1='update sample1 on plivo and tcr',
      message_flow='message flow is mandatory param and minimum 40 characters',
      help_message='help message is mandatory param and minimum 20 character'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  client.campaign.update(
      "<campaign_id>",
      "",
      "Campaign description should have a minimum of 40 characters",
      "Sample message 1 should have a minimum of 20 characters",
      "Sample message 2 should have a minimum of 20 characters",
      "Message flow is a mandatory parameter, minimum 40 characters",
      "Help message is mandatory parameter, minimum 20 characters",
      "YES,SUBSCRIBE",
      "Opt-in message should have a minimum of 20 characters",
      "NO,STOP",
      "Opt-out message should have a minimum of 20 characters",
      "HELP,INFO,MORE"
  ).then(function(response) {
      console.log(JSON.stringify(response));
  }).catch(function(error) {
      console.log(error);
  });
  ```

  ```curl cURL theme={null}
  curl --location --request POST 'https://api.plivo.com/v1/Account/<auth_id>/10dlc/Campaign/<campaign_id>/' \
  --header 'Authorization: Basic XXXX==' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "description":"Description should have minimum of 40 characters",
      "sample1": "Sample message 1 should have minimum of 20 characters",
      "sample2": "Sample message 2 should have minimum of 20 characters",
      "message_flow":"Message flow is a mandatory parameter, minimum 40 characters",
      "help_message":"Help message is a mandatory parameter, minimum 20 characters",
      "optout_message":"Opt-out message should have a minimum of 20 characters",
      "optout_keywords":"NO,STOP",
      "optin_message":"Opt-in message should have a minimum of 20 characters",
      "optin_keywords":"YES,SUBSCRIBE",
      "help_keywords":"HELP,INFO,MORE"
  }'
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "6739b738-80ff-11ed-95f2-0242ac110003",
    "campaign": {
        "brand_id": "BSJXPJH",
        "campaign_attributes": {
            "affiliate_marketing": false,
            "age_gated": false,
            "direct_lending": false,
            "embedded_link": false,
            "embedded_phone": false,
            "subscriber_help": true,
            "subscriber_optin": true,
            "subscriber_optout": true
        },
        "campaign_id": "CDB3KGW",
        "description": "Campaign description is a mandatory parameter, minimum 40 characters",
        "help_keywords": "HELP,INFO,MORE",
        "help_message": "Help message is a mandatory parameter, minimum 20 characters",
        "message_flow": "Message flow is a mandatory parameter, minimum 40 characters",
        "mno_metadata": {
            "AT&T": {
                "tpm": 4500
            },
            "T-Mobile": {
                "brand_tier": "TOP"
            },
            "US Cellular": {
                "tpm": 4500
            },
            "Verizon Wireless": {
                "tpm": 4500
            }
        },
        "optin_keywords": "YES,SUBSCRIBE",
        "optin_message": "Opt-in message should have a minimum of 20 characters",
        "optout_keywords": "NO,STOP",
        "optout_message": "Opt-out message should have a minimum of 20 characters",
        "registration_status": "FAILED",
        "reseller_id": "",
        "sample1": "Sample message 1 should have a minimum of 20 characters",
        "sample2": "Sample message 2 should have a minimum of 20 characters",
        "usecase": "2FA"
    }
}
```

***

## Delete a Campaign

Deletes a 10DLC campaign from your account. This action is irreversible and is only allowed for campaigns that have no numbers in processing status.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/{campaign_id}/
```

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.campaign.delete(campaign_id='<campaign_id>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  client.campaign.deleteCampaign("<campaign_id>").then(function(response) {
      console.log(JSON.stringify(response));
  }).catch(function(error) {
      console.log(error);
  });
  ```

  ```curl cURL theme={null}
  curl --location --request DELETE 'https://api.plivo.com/v1/Account/<auth_id>/10dlc/Campaign/<campaign_id>/' \
  --header 'Authorization: Basic XXXX=='
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "d899b83a-7464-11ed-9120-0242ac110003",
    "campaign_id": "CTPC3HL",
    "message": "Campaign Deactivated"
}
```

***

## Import a Campaign (Beta)

This API lets you import a campaign that you have registered directly with The Campaign Registry (TCR). This feature is currently in private beta - please contact our [support team](https://support.plivo.com/hc/en-us/requests/new?ticket_form_id=360000156292) to enable this feature for your account.

```
POST https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/Import/
```

### Arguments

<ParamField body="campaign_alias" type="string" required>
  A friendly name for your campaign.
</ParamField>

<ParamField body="campaign_id" type="string" required>
  ID for the campaign that needs to be imported. Make sure you have shared the campaign with Plivo from your TCR portal before submitting the API request.
</ParamField>

<ParamField body="url" type="string">
  The fully qualified URL to which status update callbacks for the message should be sent.
</ParamField>

<ParamField body="method" type="string">
  The HTTP method to be used when calling the URL defined above. Allowed values: `GET`, `POST`. Defaults to `POST`.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient("<auth_id>", "<auth_token>")
  response = client.campaign.import_campaign(
      campaign_id="C1234567",
      campaign_alias="campaign name"
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  let plivo = require('plivo');

  let client = new plivo.Client("<auth_id>", "<auth_token>");
  client.campaign.import("C1234567", "campaign name")
      .then(function(response) {
          console.log(JSON.stringify(response));
      }).catch(function(error) {
          console.log(error);
      });
  ```

  ```curl cURL theme={null}
  curl -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      -d '{
          "campaign_alias": "Friendly Name",
          "campaign_id": "C1234567",
          "url": "https://<yourdomain>.com/tendlc_status/",
          "method": "POST"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/10dlc/Campaign/Import/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "a640fba2-3b14-11ed-95d8-0242ac110003",
    "campaign_id": "<Campaign ID used in the request API>",
    "message": "Request to import campaign was received and is being processed."
}
```
