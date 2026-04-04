# Source: https://plivo.com/docs/messaging/api/numberpool.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Number Pool

> Manage numbers, shortcodes, and toll-free numbers in Powerpack number pools

An empty number pool resource is created automatically when a new Powerpack is created. You can add phone numbers, shortcodes, and toll-free numbers to the pool to use for messaging.

## The Number Pool Object

<ParamField body="uuid" type="string">
  Unique identifier for the number pool.
</ParamField>

<ParamField body="numbers" type="string">
  Subresource URI for numbers in the pool.
</ParamField>

<ParamField body="shortcodes" type="string">
  Subresource URI for shortcodes in the pool.
</ParamField>

```json Example Object theme={null}
{
    "api_id": "d7e9a038-0a88-11ea-b072-0242ac110007",
    "numbers": "/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Number/",
    "shortcodes": "/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Shortcode/",
    "uuid": "{number_pool_uuid}"
}
```

***

## Numbers

Numbers in a number pool have the following attributes:

<ParamField body="number_pool_uuid" type="string">
  Unique identifier for the number pool.
</ParamField>

<ParamField body="number" type="string">
  The phone number.
</ParamField>

<ParamField body="type" type="string">
  The type of number. One of: `fixed`, `mobile`, `toll-free`.
</ParamField>

<ParamField body="service" type="string">
  The service capability of number. One of: `sms`, `mms`.
</ParamField>

<ParamField body="country_iso2" type="string">
  The ISO2 code of the country associated with the number.
</ParamField>

<ParamField body="added_on" type="string">
  Timestamp in ISO 8601 format.
</ParamField>

<ParamField body="account_phone_number_resource" type="string">
  Account phone number resource URI.
</ParamField>

```json Example Number Object theme={null}
{
    "account_phone_number_resource": "/v1/Account/{auth_id}/Number/{your_number}/",
    "added_on": "2022-10-09T11:10:59.741978Z",
    "country_iso2": "US",
    "number": "{your_number}",
    "number_pool_uuid": "{number_pool_uuid}",
    "type": "fixed"
}
```

### Add a Number

Add SMS- and MMS-enabled numbers to a number pool resource.

```text POST theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Number/{number}/
```

#### Arguments

<ParamField body="service" type="string">
  Set this parameter to `sms` for SMS-enabled numbers or `mms` for MMS-enabled numbers. Defaults to `sms`.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid="<powerpack_uuid>")
  response = powerpack.add_number('<your_number>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.add_number('<your_number>'))
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.add_number('<your_number>')
  puts response
  ```

  ```bash cURL theme={null}
  curl -X POST -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Number/{number}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "account_phone_number_resource": "/v1/Account/{auth_id}/Number/{your_number}/",
    "added_on": "2022-10-09T11:24:35.085797Z",
    "api_id": "612982e8-0a87-11ea-b072-0242ac110007",
    "country_iso2": "CA",
    "number": "{your_number}",
    "number_pool_uuid": "{number_pool_uuid}",
    "service": "mms",
    "type": "fixed"
}
```

### Retrieve a Number

Retrieve the details of a specific number from a number pool.

```text GET theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Number/{number}/
```

#### Arguments

No arguments need to be passed.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid="<powerpack_uuid>")
  response = powerpack.find_number('<your_number>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.find_number('<your_number>'))
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.find_number('<your_number>')
  puts response
  ```

  ```bash cURL theme={null}
  curl -X GET -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Number/{number}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "account_phone_number_resource": "/v1/Account/{auth_id}/Number/{your_number}/",
    "added_on": "2022-10-09T11:24:35.085797Z",
    "api_id": "612982e8-0a87-11ea-b072-0242ac110007",
    "country_iso2": "CA",
    "number": "{your_number}",
    "number_pool_uuid": "{number_pool_uuid}",
    "type": "fixed"
}
```

### List All Numbers

Fetch a list of numbers from a number pool.

```text GET theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Number/
```

#### Arguments

<ParamField query="starts_with" type="string">
  A comma-separated list of prefixes. Values provided should exclude the country code prefix. A maximum of 10 prefixes may be specified.
</ParamField>

<ParamField query="type" type="string">
  Filter by number type: `fixed`, `toll-free`, or `mobile`. Note that local and national numbers should be considered as `fixed`.
</ParamField>

<ParamField query="service" type="string">
  Filter by capability: `sms` or `mms`.
</ParamField>

<ParamField query="country_iso2" type="string">
  ISO2 code of the phone number country. Required if the `starts_with` filter is specified.
</ParamField>

<ParamField query="limit" type="integer">
  Number of results per page. Maximum is 20. Defaults to 20.
</ParamField>

<ParamField query="offset" type="integer">
  Number of value items by which the results should be offset. Defaults to 0.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid="<powerpack_uuid>")
  response = powerpack.list_numbers(starts_with='512', country_iso2='US')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.list_numbers({ limit: '2', offset: '0' }))
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.list_numbers(limit: 2, offset: 0)
  puts response
  ```

  ```bash cURL theme={null}
  curl -X GET -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      "https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Number/?starts_with=484&country_iso2=US"
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "06c15d7c-7ed5-11ea-855f-0242ac110003",
    "meta": {
        "limit": 20,
        "next": "",
        "offset": 0,
        "previous": "",
        "total_count": 2
    },
    "objects": [
        {
            "account_phone_number_resource": "/v1/Account/{auth_id}/Number/{your_number}/",
            "added_on": "2023-03-18T16:07:39.379739Z",
            "country_iso2": "US",
            "number": "{your_number}",
            "number_pool_uuid": "{number_pool_uuid}",
            "service": "mms",
            "type": "fixed"
        },
        {
            "account_phone_number_resource": "/v1/Account/{auth_id}/Number/{your_number}/",
            "added_on": "2022-10-09T11:24:35.085797Z",
            "country_iso2": "CA",
            "number": "{your_number}",
            "number_pool_uuid": "{number_pool_uuid}",
            "service": "sms",
            "type": "fixed"
        }
    ]
}
```

### Remove a Number

Remove a number from a number pool.

```text DELETE theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Number/{number}/
```

#### Arguments

<ParamField query="unrent" type="boolean">
  Set to `true` to also unrent the number. Defaults to `false`.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid="<powerpack_uuid>")
  response = powerpack.remove_number('<your_number>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.remove_number('<your_number>', true))
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.remove_number('<your_number>', unrent: true)
  puts response
  ```

  ```bash cURL theme={null}
  curl -X DELETE -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Number/{number}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "c378d44c-0a89-11ea-b072-0242ac110007",
    "response": "success"
}
```

***

## Shortcodes

Shortcodes in a number pool have the following attributes:

<ParamField body="number_pool_uuid" type="string">
  Unique identifier for the number pool.
</ParamField>

<ParamField body="shortcode" type="string">
  The shortcode value.
</ParamField>

<ParamField body="country_iso2" type="string">
  ISO2 code of the country associated with the shortcode.
</ParamField>

<ParamField body="added_on" type="string">
  Timestamp in ISO 8601 format.
</ParamField>

```json Example Shortcode Object theme={null}
{
    "added_on": "2022-10-09T11:10:59.741978Z",
    "api_id": "b42933e8-0a88-11ea-b072-0242ac110007",
    "country_iso2": "US",
    "number_pool_uuid": "{number_pool_uuid}",
    "shortcode": "{your_shortcode}"
}
```

### Retrieve a Shortcode

Retrieve the details of a specific shortcode from a number pool.

```text GET theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Shortcode/{shortcode}/
```

#### Arguments

No arguments need to be passed.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid='<powerpack_uuid>')
  response = powerpack.find_shortcode('<shortcode>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.find_shortcode('<shortcode>'))
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.find_shortcode('<shortcode>')
  puts response
  ```

  ```bash cURL theme={null}
  curl -X GET -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Shortcode/{shortcode}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "added_on": "2022-10-09T11:10:59.741978Z",
    "api_id": "b42933e8-0a88-11ea-b072-0242ac110007",
    "country_iso2": "US",
    "number_pool_uuid": "{number_pool_uuid}",
    "shortcode": "{your_shortcode}"
}
```

### List All Shortcodes

Fetch a list of shortcodes from a number pool.

```text GET theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Shortcode/
```

#### Arguments

No arguments need to be passed.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid='<powerpack_uuid>')
  response = powerpack.list_shortcodes()
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.list_shortcodes())
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.list_shortcodes()
  puts response
  ```

  ```bash cURL theme={null}
  curl -X GET -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Shortcode/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "614b2776-0a88-11ea-b072-0242ac110007",
    "meta": {
        "limit": 20,
        "next": "",
        "offset": 0,
        "previous": "",
        "total_count": 1
    },
    "objects": [
        {
            "added_on": "2019-10-09T11:10:59.741978Z",
            "country_iso2": "US",
            "number_pool_uuid": "{number_pool_uuid}",
            "shortcode": "{your_shortcode}"
        }
    ]
}
```

### Remove a Shortcode

Remove a shortcode from a number pool. Note that the shortcode is only unlinked from the number pool, not unrented.

```text DELETE theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Shortcode/{shortcode}/
```

#### Arguments

No arguments need to be passed.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid='<powerpack_uuid>')
  response = powerpack.remove_shortcode('<shortcode>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.remove_shortcode('<shortcode>'))
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.remove_shortcode('<shortcode>')
  puts response
  ```

  ```bash cURL theme={null}
  curl -X DELETE -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Shortcode/{shortcode}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "c378d44c-0a89-11ea-b072-0242ac110007",
    "response": "success"
}
```

***

## Toll-Free Numbers

Toll-free numbers in a number pool have the following attributes:

<ParamField body="number_pool_uuid" type="string">
  Unique identifier for the number pool.
</ParamField>

<ParamField body="number" type="string">
  The toll-free number.
</ParamField>

<ParamField body="type" type="string">
  The type of number. Always `tollfree` for toll-free numbers.
</ParamField>

<ParamField body="service" type="string">
  The service capability: `sms` or `mms`.
</ParamField>

<ParamField body="country_iso2" type="string">
  ISO2 code of the country associated with the toll-free number.
</ParamField>

<ParamField body="added_on" type="string">
  Timestamp in ISO 8601 format.
</ParamField>

<ParamField body="account_phone_number_resource" type="string">
  Account phone number resource URI.
</ParamField>

```json Example Toll-Free Object theme={null}
{
    "account_phone_number_resource": "/v1/Account/{auth_id}/Number/{your_tollfree_number}/",
    "added_on": "2021-04-15T04:49:51.228392Z",
    "api_id": "8a6bba9c-7ed4-11ea-b82e-0242ac110006",
    "country_iso2": "US",
    "number": "{your_tollfree_number}",
    "number_pool_uuid": "{number_pool_uuid}",
    "service": "mms",
    "type": "tollfree"
}
```

### Add a Toll-Free Number

Add existing SMS- and MMS-enabled toll-free numbers to a number pool.

```text POST theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Tollfree/{toll_free_number}/
```

#### Arguments

No arguments need to be passed.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid='<powerpack_uuid>')
  response = powerpack.add_tollfree('<tollfree_number>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.add_tollfree('<tollfree_number>'))
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.add_tollfree('<tollfree_number>')
  puts response
  ```

  ```bash cURL theme={null}
  curl -X POST -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Tollfree/{toll_free_number}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "account_phone_number_resource": "/v1/Account/{auth_id}/Number/{your_tollfree_number}/",
    "added_on": "2021-04-15T04:49:51.228392Z",
    "api_id": "8a6bba9c-7ed4-11ea-b82e-0242ac110006",
    "country_iso2": "US",
    "number": "{your_tollfree_number}",
    "number_pool_uuid": "{number_pool_uuid}",
    "service": "mms",
    "type": "tollfree"
}
```

### Retrieve a Toll-Free Number

Retrieve the details of a specific toll-free number from a number pool.

```text GET theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Tollfree/{toll_free_number}/
```

#### Arguments

No arguments need to be passed.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid='<powerpack_uuid>')
  response = powerpack.find_tollfree('<tollfree_number>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.find_tollfree('<tollfree_number>'))
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.find_tollfree('<tollfree_number>')
  puts response
  ```

  ```bash cURL theme={null}
  curl -X GET -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Tollfree/{toll_free_number}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "account_phone_number_resource": "/v1/Account/{auth_id}/Number/{your_tollfree_number}/",
    "added_on": "2023-03-18T16:07:39.379739Z",
    "api_id": "df0519d6-7ed4-11ea-b82e-0242ac110006",
    "country_iso2": "US",
    "number": "{your_tollfree_number}",
    "number_pool_uuid": "{number_pool_uuid}",
    "type": "tollfree"
}
```

### List All Toll-Free Numbers

Fetch a list of all toll-free numbers from a number pool.

```text GET theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Tollfree/
```

#### Arguments

No arguments need to be passed.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid='<powerpack_uuid>')
  response = powerpack.list_tollfree()
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      .then(powerpack => powerpack.list_tollfree())
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  response = powerpack.list_tollfree()
  puts response
  ```

  ```bash cURL theme={null}
  curl -X GET -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Tollfree/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "06c15d7c-7ed5-11ea-855f-0242ac110003",
    "meta": {
        "limit": 20,
        "next": "",
        "offset": 0,
        "previous": "",
        "total_count": 1
    },
    "objects": [
        {
            "account_phone_number_resource": "/v1/Account/{auth_id}/Number/{your_tollfree_number}/",
            "added_on": "2022-10-09T11:24:35.085797Z",
            "country_iso2": "US",
            "number": "{your_tollfree_number}",
            "number_pool_uuid": "{number_pool_uuid}",
            "service": "mms",
            "type": "tollfree"
        }
    ]
}
```

### Remove a Toll-Free Number

Remove a toll-free number from a number pool.

```text DELETE theme={null}
https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Tollfree/{tollfree_number}/
```

#### Arguments

<ParamField query="unrent" type="boolean">
  Set to `true` to also unrent the toll-free number. Defaults to `false`.
</ParamField>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  powerpack = client.powerpacks.get(uuid='<powerpack_uuid>')
  # Set second parameter to True to also unrent the number
  response = powerpack.remove_tollfree('<tollfree_number>', True)
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.powerpacks.get('<powerpack_uuid>')
      // Set second parameter to true to also unrent the number
      .then(powerpack => powerpack.remove_tollfree('<tollfree_number>', true))
      .then(result => console.log(result))
      .catch(error => console.log(error));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  powerpack = api.powerpacks.get('<powerpack_uuid>')
  # Set unrent to true to also unrent the number
  response = powerpack.remove_tollfree('<tollfree_number>', true)
  puts response
  ```

  ```bash cURL theme={null}
  curl -X DELETE -i --user auth_id:auth_token \
      -H "Content-Type: application/json" \
      "https://api.plivo.com/v1/Account/{auth_id}/NumberPool/{number_pool_uuid}/Tollfree/{tollfree_number}/?unrent=true"
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "57936fb0-7ed5-11ea-aa79-0242ac110003",
    "response": "success"
}
```
