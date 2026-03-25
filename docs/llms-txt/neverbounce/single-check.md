# Source: https://developers.neverbounce.com/reference/single-check.md

# /check

## The Timeout Parameter

The timeout parameter tells the API how long it should try to verify an email before giving up and returning an `unknown` result code. The total request time can exceed this timeout, as network latency is not taken into consideration. This can be helpful when verifying emails at the point of entry to prevent long wait times for your users.

> 📘 Usage Guidelines
>
> Please be sure to review our usage guidelines for the API [here](/v4.0/reference#section-single-verification).

> 📘 Handling Aliases
>
> When verifying emails that contain aliases that use a `+` character extra consideration needs to be taken when encoding these for `x-www-form-urlencoded` content-types. Make sure this character is being encoded as `%2B`, as the `+` character is treated as a non-breaking space when the string is decoded.

## Result Codes

The `result` property contains a string that correlates to a result codes listed int the table below. For detailed information about result codes visit our [help docs](https://neverbounce.com/help/getting-started/result-codes/) or click the "Learn More" links next to the result codes below.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Result Code
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        valid
      </td>

      <td>
        Verified as real address. [Learn More](https://neverbounce.com/help/understanding-and-downloading-results/result-codes#valid)
      </td>
    </tr>

    <tr>
      <td>
        invalid
      </td>

      <td>
        Verified as not valid.  [Learn More](https://neverbounce.com/help/understanding-and-downloading-results/result-codes#invalid)
      </td>
    </tr>

    <tr>
      <td>
        disposable
      </td>

      <td>
        A temporary, disposable address. [Learn More](https://neverbounce.com/help/understanding-and-downloading-results/result-codes#disposable)
      </td>
    </tr>

    <tr>
      <td>
        catchall
      </td>

      <td>
        A domain wide-setting, also known as Accept-all (Unverifiable). [Learn More](https://neverbounce.com/help/understanding-and-downloading-results/result-codes#catchall)
      </td>
    </tr>

    <tr>
      <td>
        unknown
      </td>

      <td>
        The server cannot be reached. [Learn More](https://neverbounce.com/help/understanding-and-downloading-results/result-codes#unknown)
      </td>
    </tr>
  </tbody>
</Table>

## Flags

The flags will give you additional information that we discovered about the domain during verification. Below is a list of common flags you may encounter.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Flag
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        has\_dns
      </td>

      <td>
        The input has one or more DNS records associated with the hostname.
      </td>
    </tr>

    <tr>
      <td>
        has\_dns\_mx
      </td>

      <td>
        The input has mail exchanger DNS records configured.
      </td>
    </tr>

    <tr>
      <td>
        bad\_syntax
      </td>

      <td>
        The input given doesn't appear to be an email.
      </td>
    </tr>

    <tr>
      <td>
        free\_email\_host
      </td>

      <td>
        This email is registered on a free-mail host. (e.g: yahoo.com, hotmail.com)
      </td>
    </tr>

    <tr>
      <td>
        profanity
      </td>

      <td />
    </tr>

    <tr>
      <td>
        role\_account
      </td>

      <td>
        This email is a role-based email address (e.g: admin@, help@, sales@)
      </td>
    </tr>

    <tr>
      <td>
        disposable\_email
      </td>

      <td>
        The input given is a disposable email.
      </td>
    </tr>

    <tr>
      <td>
        government\_host
      </td>

      <td>
        The input given is a government email.
      </td>
    </tr>

    <tr>
      <td>
        academic\_host
      </td>

      <td>
        The input given is a acedemic email.
      </td>
    </tr>

    <tr>
      <td>
        military\_host
      </td>

      <td>
        The input given is a military email.
      </td>
    </tr>

    <tr>
      <td>
        international\_host
      </td>

      <td>
        INT designated domain names.
      </td>
    </tr>

    <tr>
      <td>
        squatter\_host
      </td>

      <td>
        Host likely intended to look like a big-time provider (type of spam trap).
      </td>
    </tr>

    <tr>
      <td>
        spelling\_mistake
      </td>

      <td>
        The input was misspelled
      </td>
    </tr>

    <tr>
      <td>
        bad\_dns
      </td>

      <td />
    </tr>

    <tr>
      <td>
        temporary\_dns\_error
      </td>

      <td />
    </tr>

    <tr>
      <td>
        connect\_fails
      </td>

      <td>
        Unable to connect to remote host.
      </td>
    </tr>

    <tr>
      <td>
        accepts\_all
      </td>

      <td>
        Remote host accepts mail at any address.
      </td>
    </tr>

    <tr>
      <td>
        contains\_alias
      </td>

      <td>
        The email address supplied contains an address part and an alias part.
      </td>
    </tr>

    <tr>
      <td>
        contains\_subdomain
      </td>

      <td>
        The host in the address contained a subdomain.
      </td>
    </tr>

    <tr>
      <td>
        smtp\_connectable
      </td>

      <td>
        We were able to connect to the remote mail server.
      </td>
    </tr>

    <tr>
      <td>
        spamtrap\_network
      </td>

      <td>
        Host is affiliated with a known spam trap network.
      </td>
    </tr>

    <tr>
      <td>
        historical\_response
      </td>

      <td>
        Indicates the result was generated using the historical-driven algorithm
      </td>
    </tr>
  </tbody>
</Table>

## Suggested Correction

These are soft suggestions that may correct common typos such as "gmal.com" or "hotmal.com".

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "neverbounce-api",
    "version": "4.2"
  },
  "servers": [
    {
      "url": "https://api.neverbounce.com/v4.2"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "query",
        "name": "key"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/single/check": {
      "get": {
        "summary": "/check",
        "description": "",
        "operationId": "single-check",
        "parameters": [
          {
            "name": "email",
            "in": "query",
            "description": "The email to verify",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "address_info",
            "in": "query",
            "description": "Include additional address info in response (default: false)",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "credits_info",
            "in": "query",
            "description": "Include account credit info in response (default: false)",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "timeout",
            "in": "query",
            "description": "The maximum time in seconds we should try to verify the address",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"status\": \"success\",\n  \"result\": \"valid\",\n  \"flags\": [\n    \"has_dns\",\n    \"has_dns_mx\"\n  ],\n  \"suggested_correction\": \"\",\n  \"execution_time\": 499\n}"
                  },
                  "Address Info": {
                    "value": "{\n  \"status\": \"success\",\n  \"result\": \"valid\",\n  \"flags\": [\n    \"has_dns\",\n    \"has_dns_mx\",\n    \"role_account\"\n  ],\n  \"suggested_correction\": \"\",\n  \"address_info\": {\n    \"original_email\": \"support@neverbounce.com\",\n    \"normalized_email\": \"support@neverbounce.com\",\n    \"addr\": \"support\",\n    \"alias\": \"\",\n    \"host\": \"neverbounce.com\",\n    \"fqdn\": \"neverbounce.com\",\n    \"domain\": \"neverbounce\",\n    \"subdomain\": \"\",\n    \"tld\": \"com\"\n  },\n  \"execution_time\": 399\n}"
                  },
                  "Credits Info": {
                    "value": "{\n    \"status\": \"success\",\n    \"result\": \"valid\",\n    \"flags\": [\n        \"smtp_connectable\",\n        \"has_dns\",\n        \"has_dns_mx\"\n    ],\n    \"suggested_correction\": \"\",\n    \"credits_info\": {\n        \"paid_credits_used\": 1,\n        \"free_credits_used\": 0,\n        \"paid_credits_remaining\": 9950778,\n        \"free_credits_remaining\": 0\n    },\n    \"execution_time\": 350\n}"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "type": "object",
                      "properties": {
                        "status": {
                          "type": "string",
                          "example": "success"
                        },
                        "result": {
                          "type": "string",
                          "example": "valid"
                        },
                        "flags": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "has_dns"
                          }
                        },
                        "suggested_correction": {
                          "type": "string",
                          "example": ""
                        },
                        "execution_time": {
                          "type": "integer",
                          "example": 499,
                          "default": 0
                        }
                      }
                    },
                    {
                      "title": "Address Info",
                      "type": "object",
                      "properties": {
                        "status": {
                          "type": "string",
                          "example": "success"
                        },
                        "result": {
                          "type": "string",
                          "example": "valid"
                        },
                        "flags": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "has_dns"
                          }
                        },
                        "suggested_correction": {
                          "type": "string",
                          "example": ""
                        },
                        "address_info": {
                          "type": "object",
                          "properties": {
                            "original_email": {
                              "type": "string",
                              "example": "support@neverbounce.com"
                            },
                            "normalized_email": {
                              "type": "string",
                              "example": "support@neverbounce.com"
                            },
                            "addr": {
                              "type": "string",
                              "example": "support"
                            },
                            "alias": {
                              "type": "string",
                              "example": ""
                            },
                            "host": {
                              "type": "string",
                              "example": "neverbounce.com"
                            },
                            "fqdn": {
                              "type": "string",
                              "example": "neverbounce.com"
                            },
                            "domain": {
                              "type": "string",
                              "example": "neverbounce"
                            },
                            "subdomain": {
                              "type": "string",
                              "example": ""
                            },
                            "tld": {
                              "type": "string",
                              "example": "com"
                            }
                          }
                        },
                        "execution_time": {
                          "type": "integer",
                          "example": 399,
                          "default": 0
                        }
                      }
                    },
                    {
                      "title": "Credits Info",
                      "type": "object",
                      "properties": {
                        "status": {
                          "type": "string",
                          "example": "success"
                        },
                        "result": {
                          "type": "string",
                          "example": "valid"
                        },
                        "flags": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "smtp_connectable"
                          }
                        },
                        "suggested_correction": {
                          "type": "string",
                          "example": ""
                        },
                        "credits_info": {
                          "type": "object",
                          "properties": {
                            "paid_credits_used": {
                              "type": "integer",
                              "example": 1,
                              "default": 0
                            },
                            "free_credits_used": {
                              "type": "integer",
                              "example": 0,
                              "default": 0
                            },
                            "paid_credits_remaining": {
                              "type": "integer",
                              "example": 9950778,
                              "default": 0
                            },
                            "free_credits_remaining": {
                              "type": "integer",
                              "example": 0,
                              "default": 0
                            }
                          }
                        },
                        "execution_time": {
                          "type": "integer",
                          "example": 350,
                          "default": 0
                        }
                      }
                    }
                  ]
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "# Be sure to encode email before making the request (@ becomes %40)\ncurl --request GET\\\n  --url 'https://api.neverbounce.com/v4.2/single/check?key={api_key}&email={email}'"
            },
            {
              "language": "php",
              "code": "<?php\n\n// Set API key\n\\NeverBounce\\Auth::setApiKey($api_key);\n\n// Make verification request, specify optional $max_execution_time\n$result = \\NeverBounce\\Single::check(\n  'support@neverbounce.com', // Email to verify\n  true, // Address info\n  true, // Credits info\n  10 // Timeout in seconds\n);"
            },
            {
              "language": "javascript",
              "code": "// Initialize NeverBounce client\nconst client = new NeverBounce({apiKey: myApiKey});\n\n/// Verify an email\nclient.single.check(\n  'support@neverbounce.com', \n  true, // Address info\n  true // Credits info\n  10 // timeout\n).then(\n    result => // Handle success response\n    err => // Handle error response\n);",
              "name": "NodeJs"
            },
            {
              "language": "python",
              "code": "import neverbounce_sdk\n\n# Create sdk client\nclient = neverbounce_sdk.client(api_key='api_key')\n\n# Verify email\nverification = client.single_check(\n  email='support@neverbounce.com',\n  address_info=True,\n  credits_info=True,\n  timeout=10  # Timeout in seconds\n)"
            },
            {
              "language": "go",
              "code": "// Instantiate wrapper\nclient := neverbounce.New(\"api_key\")\n\n// Verify an email\nsingleResults, err := client.Single.Check(&nbModels.SingleCheckRequestModel{\n  Email:       \"support@neverbounce.com\",\n  AddressInfo: true,\n  CreditInfo:  true,\n  Timeout:     10,\n})"
            },
            {
              "language": "ruby",
              "code": "# Instantiate API client\nclient = NeverBounce::API::Client.new(api_key: \"api_key\")\n\n# Get account info\nresp = client.single_check(\n  email: \"support@neverbounce.com\", \n  address_info: true, \n  credits_info: true, \n  timeout: 10)"
            },
            {
              "language": "csharp",
              "code": "// Create SDK object\nvar sdk = new NeverBounceSdk(\"api_key\");\n\n// Create request model\nvar model = new SingleRequestModel();\nmodel.email = \"support@neverbounce.com\";\nmodel.credits_info = true;\nmodel.address_info = true;\nmodel.timeout = 10; \n\n// Verify single email\nSingleResponseModel resp = await sdk.Single.Check(model);",
              "name": ".NET"
            },
            {
              "language": "java",
              "code": "// Instantiate Client\nNeverbounceClient neverbounceClient = NeverbounceClientFactory.create(apiKey);\n\n// Perform verification\nSingleCheckResponse singleCheckResponse = neverbounceClient\n            .prepareSingleCheckRequest()\n            .withEmail(\"support@neverbounce.com\")\n            .withAddressInfo(true)\n            .withCreditsInfo(true)\n            .withTimeout(10)\n            .build()\n            .execute()"
            },
            {
              "language": "node",
              "code": "// Initialize NeverBounce client\nconst client = new NeverBounce({apiKey: myApiKey});\ntry {\n  const result = await client.single.check('support@neverbounce.com');\n  console.log('Result:', result);\n} catch (error) {\n  console.error('Error:', error);\n}"
            }
          ],
          "samples-languages": [
            "curl",
            "php",
            "javascript",
            "python",
            "go",
            "ruby",
            "csharp",
            "java",
            "node"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```