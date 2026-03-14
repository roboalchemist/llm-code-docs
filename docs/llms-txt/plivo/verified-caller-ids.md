# Source: https://plivo.com/docs/voice/api/verified-caller-ids.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Verified Caller IDs

> Verify phone numbers to use as caller ID for outbound calls

The Verified Caller ID API lets you authenticate phone numbers before using them as caller ID for outbound calls. This is required when using numbers you don't own through Plivo.

## API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/
```

***

## The Verified Caller ID Object

| Attribute           | Type   | Description                           |
| ------------------- | ------ | ------------------------------------- |
| `phone_number`      | string | Verified phone number in E.164 format |
| `alias`             | string | Friendly name for the caller ID       |
| `country`           | string | Country code (e.g., `US`)             |
| `verification_uuid` | string | Unique identifier for verification    |
| `created_at`        | string | When the verification was created     |

### Example Response

```json  theme={null}
{
    "api_id": "870e2ded-58b0-41bc-8c1c-ba00c6a90741",
    "phone_number": "+12025551234",
    "alias": "US Mainland",
    "country": "US",
    "verification_uuid": "f87836bd-f3c0-41bb-9498-125e6faaa4d4",
    "created_at": "2024-02-09T03:52:22.880097813Z"
}
```

***

## Initiate Verification

Start the verification process for a phone number. An OTP will be sent via SMS or voice call.

```
POST https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/
```

### Parameters

| Parameter      | Type   | Required | Description                                          |
| -------------- | ------ | -------- | ---------------------------------------------------- |
| `phone_number` | string | Yes      | Phone number in E.164 format                         |
| `alias`        | string | No       | Friendly name for the caller ID                      |
| `channel`      | string | No       | OTP delivery method: `sms` or `call`. Default: `sms` |
| `subaccount`   | string | No       | Subaccount Auth ID to associate                      |

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.verify_callerids.initiate_verify(
      phone_number='+12025551234',
      alias='Main Office',
      channel='sms'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.verify.initiate('+12025551234', {
      channel: 'sms',
      alias: 'Main Office'
  }).then(console.log);
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = api.verify_caller_id.initiate(
      phone_number: '+12025551234',
      channel: 'sms',
      alias_: 'Main Office'
  )
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->verifyCallerId->initiate('+12025551234', [
      'alias' => 'Main Office',
      'channel' => 'sms'
  ]);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.verify.Verify;

  Plivo.init("<auth_id>", "<auth_token>");

  var response = Verify.initiateVerify()
      .phoneNumber("+12025551234")
      .alias("Main Office")
      .channel("sms")
      .create();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.VerifyCallerId.Initiate(
      "+12025551234",
      "sms",
      "Main Office"
  );
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})

      response, _ := client.VerifyCallerId.InitiateVerify(plivo.InitiateVerify{
          PhoneNumber: "+12025551234",
          Alias:       "Main Office",
          Channel:     "sms",
      })
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"phone_number": "+12025551234", "alias": "Main Office", "channel": "sms"}' \
      https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "654a7ca7-b9cc-4285-86f7-cf581f50409f",
    "message": "Verification code is sent to number +12025551234 which is valid for 15 minutes",
    "verification_uuid": "f87836bd-f3c0-41bb-9498-125e6faaa4d4"
}
```

***

## Complete Verification

Submit the OTP received to complete verification.

```
POST https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/Verification/{verification_uuid}/
```

### Parameters

| Parameter | Type   | Required | Description                    |
| --------- | ------ | -------- | ------------------------------ |
| `otp`     | string | Yes      | The verification code received |

<CodeGroup>
  ```python Python theme={null}
  response = client.verify_callerids.verify_caller_id(
      verification_uuid='f87836bd-f3c0-41bb-9498-125e6faaa4d4',
      otp='123456'
  )
  ```

  ```javascript Node.js theme={null}
  client.verify.verify('f87836bd-f3c0-41bb-9498-125e6faaa4d4', '123456')
      .then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"otp": "123456"}' \
      https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/Verification/{verification_uuid}/
  ```
</CodeGroup>

***

## Retrieve a Verified Caller ID

Get details of a specific verified caller ID.

```
GET https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/{phone_number}/
```

<CodeGroup>
  ```python Python theme={null}
  response = client.verify_callerids.get_verified_caller_id('+12025551234')
  ```

  ```javascript Node.js theme={null}
  client.verify.get('+12025551234').then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/+12025551234/
  ```
</CodeGroup>

***

## List All Verified Caller IDs

Get all verified caller IDs for your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/
```

### Query Parameters

| Parameter    | Type    | Description               |
| ------------ | ------- | ------------------------- |
| `limit`      | integer | Results per page (max 20) |
| `offset`     | integer | Pagination offset         |
| `country`    | string  | Filter by country code    |
| `subaccount` | string  | Filter by subaccount      |

<CodeGroup>
  ```python Python theme={null}
  response = client.verify_callerids.list_verified_caller_id(
      limit=10,
      country='US'
  )
  ```

  ```javascript Node.js theme={null}
  client.verify.list({ limit: 10, country: 'US' }).then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      "https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/?limit=10&country=US"
  ```
</CodeGroup>

***

## Update a Verified Caller ID

Update the alias or subaccount of a verified caller ID.

```
POST https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/{phone_number}/
```

### Parameters

| Parameter    | Type   | Description            |
| ------------ | ------ | ---------------------- |
| `alias`      | string | New alias name         |
| `subaccount` | string | New subaccount Auth ID |

<CodeGroup>
  ```python Python theme={null}
  response = client.verify_callerids.update_verified_caller_id(
      '+12025551234',
      alias='New Name'
  )
  ```

  ```javascript Node.js theme={null}
  client.verify.update('+12025551234', { alias: 'New Name' }).then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"alias": "New Name"}' \
      https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/+12025551234/
  ```
</CodeGroup>

***

## Delete a Verified Caller ID

Remove a verified caller ID from your account.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/{phone_number}/
```

<CodeGroup>
  ```python Python theme={null}
  client.verify_callerids.delete_verified_caller_id('+12025551234')
  ```

  ```javascript Node.js theme={null}
  client.verify.delete('+12025551234').then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN -X DELETE \
      https://api.plivo.com/v1/Account/{auth_id}/VerifiedCallerId/+12025551234/
  ```
</CodeGroup>

**Response:** HTTP 204 No Content

***

## Verification Flow

1. **Initiate** - Call the initiate endpoint with the phone number
2. **Receive OTP** - OTP is sent via SMS or voice call (valid for 15 minutes)
3. **Verify** - Submit the OTP to complete verification
4. **Use** - The number can now be used as caller ID

***

## Use Cases

| Scenario             | Description                                 |
| -------------------- | ------------------------------------------- |
| **Personal Numbers** | Use your mobile number as caller ID         |
| **Business Lines**   | Verify existing business phone numbers      |
| **International**    | Use local numbers in different countries    |
| **Subaccounts**      | Assign verified IDs to specific subaccounts |

***

## Related

* [Make a Call](/voice/api/calls/#create-a-call) - Use verified caller ID
* [Dial XML](/voice/xml/routing#dial) - Use in XML applications
