# Source: https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions/espresso-api/submit-api.md

# Source: https://docs.espressosys.com/network/api-reference/espresso-api/submit-api.md

# Submit API

## Endpoints

### POST `/submit/submit`

Returns the hash of the transaction if it was successfully submitted. This does not mean the transaction has yet been sequenced. The user can check for inclusion of the transaction using `/availability/transaction/hash/:hash` from the [availability API](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api).

{% hint style="warning" %}
This endpoint will fail with a 400 status code if the submitted transaction has a `namespace` ID larger than 4294967295 (2^32 - 1).
{% endhint %}

#### Request Body `Transaction`

#### Returns `tagged<TX>`
