# Source: https://docs.solidfi.com/v2/api-reference/getting-started/metadata.md

# Metadata

> Solid Platform supports metadata

The Solid Platform support includes metadata on all the resources.

Metadata takes the form of free-form key-value pairs. You may send metadata when you create an object (POST) and when updating the object (PATCH). If you would like to remove metadata that is already on an object, you can unset it by passing in the key-value pair with an empty string, like this:

```json
{
  "key": ""
}
```

Current limitations:

* Max of 20 keys for any single metadata object
* Max of 4KB for any single metadata object

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
  },
  "metadata": {
    "user_type": "pro"
  }
}
```
