# Source: https://docs.solidfi.com/v2/api-reference/getting-started/authentication.md

# Authentication

> API key based authentication

All requests to Solid's platform must be made over HTTPS and authenticated via API key. You need to pass the API key in the header. You can view and manage your API keys in the Solid Dashboard. API keys must be kept secret. They should not be in your client-side code or checked into your application's code.

As an example:

1. Proceed to Create a Sub Account Holder with the API key. Set the api-key in the header.
2. Once you create a Sub Account Holder, you will receive the Sub Account Holder ID in the response.

```bash EXAMPLE
curl --request POST \
  --url https://api.sandbox.solidfi.com/v2/accounts/sub_account_holder \
  --header 'Content-Type: application/json' \
  --header 'api-key: <api-key>' \
  --data '{
  "master_account_id": "mas_743fa071316bc6beaf5dddfd05f49c30",
  "type": "person",
  "person": {
    "first_name": "Jane",
    "last_name": "Doe",
    "id_type": "ssn",
    "id_number": "223902234",
    "date_of_birth": "1974-01-25",
    "phone": "+19418405843",
    "email": "jane.doe@gmail.com",
    "address": {
      "line1": "123 Main St",
      "line2": "",
      "city": "New York",
      "state": "NY",
      "country": "US",
      "postal_code": "10001"
    }
  },
  "verification": {
    "status": "pass",
    "method": "persona",
    "url": "https://withpersona.com/verify?inquiry-id=inq_p1LgZj3wp5xWMk5XUhWAMrgV"
  }
}'
```

<Warning>IP Whitelisting is not required in Sandbox environment, but mandatory in Prod.</Warning>

To further secure your data in Production, the Solid platform only accepts API requests if the originating IP address is whitelisted in the Prod Dashboard. If the IP address is mismatched, the request is discarded.
